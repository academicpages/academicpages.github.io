# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import ast
import json
import re
import sys
import textwrap


def split_lines(source):
    """
    Split selection lines in a version-agnostic way.

    Python grammar only treats \r, \n, and \r\n as newlines.
    But splitlines() in Python 3 has a much larger list: for example, it also includes \v, \f.
    As such, this function will split lines across all Python versions.
    """
    return re.split(r"[\n\r]+", source)


def _get_statements(selection):
    """
    Process a multiline selection into a list of its top-level statements.
    This will remove empty newlines around and within the selection, dedent it,
    and split it using the result of `ast.parse()`.
    """

    # Remove blank lines within the selection to prevent the REPL from thinking the block is finished.
    lines = (line for line in split_lines(selection) if line.strip() != "")

    # Dedent the selection and parse it using the ast module.
    # Note that leading comments in the selection will be discarded during parsing.
    source = textwrap.dedent("\n".join(lines))
    tree = ast.parse(source)

    # We'll need the dedented lines to rebuild the selection.
    lines = split_lines(source)

    # Get the line ranges for top-level blocks returned from parsing the dedented text
    # and split the selection accordingly.
    # tree.body is a list of AST objects, which we rely on to extract top-level statements.
    # If we supported Python 3.8+ only we could use the lineno and end_lineno attributes of each object
    # to get the boundaries of each block.
    # However, earlier Python versions only have the lineno attribute, which is the range start position (1-indexed).
    # Therefore, to retrieve the end line of each block in a version-agnostic way we need to do
    # `end = next_block.lineno - 1`
    # for all blocks except the last one, which will will just run until the last line.
    ends = []
    for node in tree.body[1:]:
        line_end = node.lineno - 1
        # Special handling of decorators:
        # In Python 3.8 and higher, decorators are not taken into account in the value returned by lineno,
        # and we have to use the length of the decorator_list array to compute the actual start line.
        # Before that, lineno takes into account decorators, so this offset check is unnecessary.
        # Also, not all AST objects can have decorators.
        if hasattr(node, "decorator_list") and sys.version_info >= (3, 8):
            # Using getattr instead of node.decorator_list or pyright will complain about an unknown member.
            line_end -= len(getattr(node, "decorator_list"))
        ends.append(line_end)
    ends.append(len(lines))

    for node, end in zip(tree.body, ends):
        # Given this selection:
        # 1: if (m > 0 and
        # 2:        n < 3):
        # 3:     print('foo')
        # 4: value = 'bar'
        #
        # The first block would have lineno = 1,and the second block lineno = 4
        start = node.lineno - 1

        # Special handling of decorators similar to what's above.
        if hasattr(node, "decorator_list") and sys.version_info >= (3, 8):
            # Using getattr instead of node.decorator_list or pyright will complain about an unknown member.
            start -= len(getattr(node, "decorator_list"))
        block = "\n".join(lines[start:end])

        # If the block is multiline, add an extra newline character at its end.
        # This way, when joining blocks back together, there will be a blank line between each multiline statement
        # and no blank lines between single-line statements, or it would look like this:
        # >>> x = 22
        # >>>
        # >>> total = x + 30
        # >>>
        # Note that for the multiline parentheses case this newline is redundant,
        # since the closing parenthesis terminates the statement already.
        # This means that for this pattern we'll end up with:
        # >>> x = [
        # ...   1
        # ... ]
        # >>>
        # >>> y = [
        # ...   2
        # ...]
        if end - start > 1:
            block += "\n"

        yield block


def normalize_lines(selection):
    """
    Normalize the text selection received from the extension.

    If it is a single line selection, dedent it and append a newline and
    send it back to the extension.
    Otherwise, sanitize the multiline selection before returning it:
    split it in a list of top-level statements
    and add newlines between each of them so the REPL knows where each block ends.
    """
    try:
        # Parse the selection into a list of top-level blocks.
        # We don't differentiate between single and multiline statements
        # because it's not a perf bottleneck,
        # and the overhead from splitting and rejoining strings in the multiline case is one-off.
        statements = _get_statements(selection)

        # Insert a newline between each top-level statement, and append a newline to the selection.
        source = "\n".join(statements) + "\n"
    except:
        # If there's a problem when parsing statements,
        # append a blank line to end the block and send it as-is.
        source = selection + "\n\n"

    return source


if __name__ == "__main__":
    # Content is being sent from the extension as a JSON object.
    # Decode the data from the raw bytes.
    stdin = sys.stdin if sys.version_info < (3,) else sys.stdin.buffer
    raw = stdin.read()
    contents = json.loads(raw.decode("utf-8"))

    normalized = normalize_lines(contents["code"])

    # Send the normalized code back to the extension in a JSON object.
    data = json.dumps({"normalized": normalized})

    stdout = sys.stdout if sys.version_info < (3,) else sys.stdout.buffer
    stdout.write(data.encode("utf-8"))
    stdout.close()
