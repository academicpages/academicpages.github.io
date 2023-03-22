"""Set of common tools to aid bundler implementations."""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
import os
import shutil
import errno
import nbformat
import fnmatch
import glob

def get_file_references(abs_nb_path, version):
    """Gets a list of files referenced either in Markdown fenced code blocks
    or in HTML comments from the nbclassic. Expands patterns expressed in
    gitignore syntax (https://git-scm.com/docs/gitignore). Returns the
    fully expanded list of filenames relative to the notebook dirname.

    Parameters
    ----------
    abs_nb_path: str
        Absolute path of the notebook on disk
    version: int
        Version of the notebook document format to use

    Returns
    -------
    list
        Filename strings relative to the notebook path
    """
    ref_patterns = get_reference_patterns(abs_nb_path, version)
    expanded = expand_references(os.path.dirname(abs_nb_path), ref_patterns)
    return expanded

def get_reference_patterns(abs_nb_path, version):
    """Gets a list of reference patterns either in Markdown fenced code blocks
    or in HTML comments from the nbclassic.

    Parameters
    ----------
    abs_nb_path: str
        Absolute path of the notebook on disk
    version: int
        Version of the notebook document format to use

    Returns
    -------
    list
        Pattern strings from the notebook
    """
    notebook = nbformat.read(abs_nb_path, version)
    referenced_list = []
    for cell in notebook.cells:
        references = get_cell_reference_patterns(cell)
        if references:
            referenced_list = referenced_list + references
    return referenced_list

def get_cell_reference_patterns(cell):
    '''
    Retrieves the list of references from a single notebook cell. Looks for
    fenced code blocks or HTML comments in Markdown cells, e.g.,

    ```
    some.csv
    foo/
    !foo/bar
    ```

    or

    <!--associate:
    some.csv
    foo/
    !foo/bar
    -->

    Parameters
    ----------
    cell: dict
        Notebook cell object

    Returns
    -------
    list
        Reference patterns found in the cell
    '''
    referenced = []
    # invisible after execution: unrendered HTML comment
    if cell.get('cell_type').startswith('markdown') and cell.get('source').startswith('<!--associate:'):
        lines = cell.get('source')[len('<!--associate:'):].splitlines()
        for line in lines:
            if line.startswith('-->'):
                break
            # Trying to go out of the current directory leads to
            # trouble when deploying
            if line.find('../') < 0 and not line.startswith('#'):
                referenced.append(line)
    # visible after execution: rendered as a code element within a pre element
    elif cell.get('cell_type').startswith('markdown') and cell.get('source').find('```') >= 0:
        source = cell.get('source')
        offset = source.find('```')
        lines = source[offset + len('```'):].splitlines()
        for line in lines:
            if line.startswith('```'):
                break
            # Trying to go out of the current directory leads to
            # trouble when deploying
            if line.find('../') < 0 and not line.startswith('#'):
                referenced.append(line)

    # Clean out blank references
    return [ref for ref in referenced if ref.strip()]

def expand_references(root_path, references):
    """Expands a set of reference patterns by evaluating them against the
    given root directory. Expansions are performed against patterns
    expressed in the same manner as in gitignore
    (https://git-scm.com/docs/gitignore).

    NOTE: Temporarily changes the current working directory when called.

    Parameters
    ----------
    root_path: str
        Assumed root directory for the patterns
    references: list
        Reference patterns from get_reference_patterns expressed with
        forward-slash directory separators

    Returns
    -------
    list
        Filename strings relative to the root path
    """
    # Use normpath to convert to platform specific slashes, but be sure
    # to retain a trailing slash which normpath pulls off
    normalized_references = []
    for ref in references:
        normalized_ref = os.path.normpath(ref)
        # un-normalized separator
        if ref.endswith('/'):
            normalized_ref += os.sep
        normalized_references.append(normalized_ref)
    references = normalized_references

    globbed = []
    negations = []
    must_walk = []
    for pattern in references:
        if pattern and pattern.find(os.sep) < 0:
            # simple shell glob
            cwd = os.getcwd()
            os.chdir(root_path)
            if pattern.startswith('!'):
                negations = negations + glob.glob(pattern[1:])
            else:
                globbed = globbed + glob.glob(pattern)
            os.chdir(cwd)
        elif pattern:
            must_walk.append(pattern)

    for pattern in must_walk:
        pattern_is_negation = pattern.startswith('!')
        if pattern_is_negation:
            testpattern = pattern[1:]
        else:
            testpattern = pattern
        for root, _, filenames in os.walk(root_path):
            for filename in filenames:
                joined = os.path.join(root[len(root_path) + 1:], filename)
                if testpattern.endswith(os.sep):
                    if joined.startswith(testpattern):
                        if pattern_is_negation:
                            negations.append(joined)
                        else:
                            globbed.append(joined)
                elif testpattern.find('**') >= 0:
                    # path wildcard
                    ends = testpattern.split('**')
                    if len(ends) == 2:
                        if joined.startswith(ends[0]) and joined.endswith(ends[1]):
                            if pattern_is_negation:
                                negations.append(joined)
                            else:
                                globbed.append(joined)
                else:
                    # segments should be respected
                    if fnmatch.fnmatch(joined, testpattern):
                        if pattern_is_negation:
                            negations.append(joined)
                        else:
                            globbed.append(joined)

    for negated in negations:
        try:
            globbed.remove(negated)
        except ValueError as err:
            pass
    return set(globbed)

def copy_filelist(src, dst, src_relative_filenames):
    """Copies the given list of files, relative to src, into dst, creating
    directories along the way as needed and ignore existence errors.
    Skips any files that do not exist. Does not create empty directories
    from src in dst.

    Parameters
    ----------
    src: str
        Root of the source directory
    dst: str
        Root of the destination directory
    src_relative_filenames: list
        Filenames relative to src
    """
    for filename in src_relative_filenames:
        # Only consider the file if it exists in src
        if os.path.isfile(os.path.join(src, filename)):
            parent_relative = os.path.dirname(filename)
            if parent_relative:
                # Make sure the parent directory exists
                parent_dst = os.path.join(dst, parent_relative)
                try:
                    os.makedirs(parent_dst)
                except OSError as exc:
                    if exc.errno == errno.EEXIST:
                        pass
                    else:
                        raise exc
            shutil.copy2(os.path.join(src, filename), os.path.join(dst, filename))
