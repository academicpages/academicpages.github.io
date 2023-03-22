"""Test the bundler tools."""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import unittest
import os
import shutil
import tempfile
import notebook.bundler.tools as tools

HERE = os.path.abspath(os.path.dirname(__file__))

class TestBundlerTools(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_get_no_cell_references(self):
        '''Should find no references in a regular HTML comment.'''
        no_references = tools.get_cell_reference_patterns({'source':'''!<--
a
b
c
-->''', 'cell_type':'markdown'})
        self.assertEqual(len(no_references), 0)

    def test_get_cell_reference_patterns_comment_multiline(self):
        '''Should find two references and ignore a comment within an HTML comment.'''
        cell = {'cell_type':'markdown', 'source':'''<!--associate:
a
b/
#comment
-->'''}
        references = tools.get_cell_reference_patterns(cell)
        self.assertTrue('a' in references and 'b/' in references, str(references))
        self.assertEqual(len(references), 2, str(references))

    def test_get_cell_reference_patterns_comment_trailing_filename(self):
        '''Should find three references within an HTML comment.'''
        cell = {'cell_type':'markdown', 'source':'''<!--associate:c
a
b/
#comment
-->'''}
        references = tools.get_cell_reference_patterns(cell)
        self.assertTrue('a' in references and 'b/' in references and 'c' in references, str(references))
        self.assertEqual(len(references), 3, str(references))

    def test_get_cell_reference_patterns_precode(self):
        '''Should find no references in a fenced code block in a *code* cell.'''
        self.assertTrue(tools.get_cell_reference_patterns)
        no_references = tools.get_cell_reference_patterns({'source':'''```
foo
bar
baz
```
''', 'cell_type':'code'})
        self.assertEqual(len(no_references), 0)

    def test_get_cell_reference_patterns_precode_mdcomment(self):
        '''Should find two references and ignore a comment in a fenced code block.'''
        cell = {'cell_type':'markdown', 'source':'''```
a
b/
#comment
```'''}
        references = tools.get_cell_reference_patterns(cell)
        self.assertTrue('a' in references and 'b/' in references, str(references))
        self.assertEqual(len(references), 2, str(references))

    def test_get_cell_reference_patterns_precode_backticks(self):
        '''Should find three references in a fenced code block.''' 
        cell = {'cell_type':'markdown', 'source':'''```c
a
b/
#comment
```'''}
        references = tools.get_cell_reference_patterns(cell)
        self.assertTrue('a' in references and 'b/' in references and 'c' in references, str(references))
        self.assertEqual(len(references), 3, str(references))

    def test_glob_dir(self):
        '''Should expand to single file in the resources/ subfolder.'''
        self.assertIn(os.path.join('resources', 'empty.ipynb'),
            tools.expand_references(HERE, ['resources/empty.ipynb']))

    def test_glob_subdir(self):
        '''Should expand to all files in the resources/ subfolder.'''
        self.assertIn(os.path.join('resources', 'empty.ipynb'),
            tools.expand_references(HERE, ['resources/']))

    def test_glob_splat(self):
        '''Should expand to all contents under this test/ directory.'''
        globs = tools.expand_references(HERE, ['*'])
        self.assertIn('test_bundler_tools.py', globs, globs)
        self.assertIn('resources', globs, globs)

    def test_glob_splatsplat_in_middle(self):
        '''Should expand to test_file.txt deep under this test/ directory.'''
        globs = tools.expand_references(HERE, ['resources/**/test_file.txt'])
        self.assertIn(os.path.join('resources', 'subdir', 'test_file.txt'), globs, globs)

    def test_glob_splatsplat_trailing(self):
        '''Should expand to all descendants of this test/ directory.'''
        globs = tools.expand_references(HERE, ['resources/**'])
        self.assertIn(os.path.join('resources', 'empty.ipynb'), globs, globs)
        self.assertIn(os.path.join('resources', 'subdir', 'test_file.txt'), globs, globs)

    def test_glob_splatsplat_leading(self):
        '''Should expand to test_file.txt under any path.'''
        globs = tools.expand_references(HERE, ['**/test_file.txt'])
        self.assertIn(os.path.join('resources', 'subdir', 'test_file.txt'), globs, globs)
        self.assertIn(os.path.join('resources', 'another_subdir', 'test_file.txt'), globs, globs)

    def test_copy_filelist(self):
        '''Should copy select files from source to destination'''
        globs = tools.expand_references(HERE, ['**/test_file.txt'])
        tools.copy_filelist(HERE, self.tmp, globs)
        self.assertTrue(os.path.isfile(os.path.join(self.tmp, 'resources', 'subdir', 'test_file.txt')))
        self.assertTrue(os.path.isfile(os.path.join(self.tmp, 'resources', 'another_subdir', 'test_file.txt')))
        self.assertFalse(os.path.isfile(os.path.join(self.tmp, 'resources', 'empty.ipynb')))
