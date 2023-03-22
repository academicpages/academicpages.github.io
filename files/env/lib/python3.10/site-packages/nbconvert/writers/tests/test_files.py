"""
Module with tests for files
"""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import os

from ...tests.base import TestsBase
from ..files import FilesWriter


class Testfiles(TestsBase):
    """Contains test functions for files.py"""

    def test_basic_output(self):
        """Is FilesWriter basic output correct?"""

        # Work in a temporary directory.
        with self.create_temp_cwd():

            # Create the resoruces dictionary
            res = {}

            # Create files writer, test output
            writer = FilesWriter()
            writer.write("y", res, notebook_name="z")

            # Check the output of the file
            with open("z") as f:
                output = f.read()
                self.assertEqual(output, "y")

    def test_ext(self):
        """Does the FilesWriter add the correct extension to the output?"""

        # Work in a temporary directory.
        with self.create_temp_cwd():

            # Create the resoruces dictionary
            res = {"output_extension": ".txt"}

            # Create files writer, test output
            writer = FilesWriter()
            writer.write("y", res, notebook_name="z")

            # Check the output of the file
            assert os.path.isfile("z.txt")
            with open("z.txt") as f:
                output = f.read()
                self.assertEqual(output, "y")

    def test_extract(self):
        """Can FilesWriter write extracted figures correctly?"""

        # Work in a temporary directory.
        with self.create_temp_cwd():

            # Create the resoruces dictionary
            res = {"outputs": {os.path.join("z_files", "a"): b"b"}}

            # Create files writer, test output
            writer = FilesWriter()
            writer.write("y", res, notebook_name="z")

            # Check the output of the file
            with open("z") as f:
                output = f.read()
                self.assertEqual(output, "y")

            # Check the output of the extracted file
            extracted_file_dest = os.path.join("z_files", "a")
            assert os.path.isfile(extracted_file_dest)
            with open(extracted_file_dest) as f:
                output = f.read()
                self.assertEqual(output, "b")

    def test_build_dir(self):
        """Can FilesWriter write to a build dir correctly?"""

        # Work in a temporary directory.
        with self.create_temp_cwd():

            # Create the resoruces dictionary
            res = {"outputs": {os.path.join("z_files", "a"): b"b"}}

            # Create files writer, test output
            writer = FilesWriter()
            writer.build_directory = "build"
            writer.write("y", res, notebook_name="z")

            # Check the output of the file
            assert os.path.isdir(writer.build_directory)
            dest = os.path.join(writer.build_directory, "z")
            with open(dest) as f:
                output = f.read()
                self.assertEqual(output, "y")

            # Check the output of the extracted file
            extracted_file_dest = os.path.join(writer.build_directory, "z_files", "a")
            assert os.path.isfile(extracted_file_dest)
            with open(extracted_file_dest) as f:
                output = f.read()
                self.assertEqual(output, "b")

    def test_build_dir_default(self):
        """FilesWriter defaults to input path"""
        with self.create_temp_cwd():
            os.mkdir("sub")
            resources = {"metadata": {"path": "sub"}}
            writer = FilesWriter()
            writer.write("content", resources, notebook_name="out")
            dest = os.path.join("sub", "out")
            assert os.path.isfile(dest)
            with open(dest) as f:
                self.assertEqual(f.read().strip(), "content")

    def test_links(self):
        """Can the FilesWriter handle linked files correctly?"""

        # Work in a temporary directory.
        with self.create_temp_cwd():

            # Create test file
            os.mkdir("sub")
            with open(os.path.join("sub", "c"), "w") as f:
                f.write("d")

            # Create the resoruces dictionary
            res = {}

            # Create files writer, test output
            writer = FilesWriter()
            writer.files = [os.path.join("sub", "c")]
            writer.build_directory = "build"
            writer.write("y", res, notebook_name="z")

            # Check the output of the file
            assert os.path.isdir(writer.build_directory)
            dest = os.path.join(writer.build_directory, "z")
            with open(dest) as f:
                output = f.read()
                self.assertEqual(output, "y")

            # Check to make sure the linked file was copied
            path = os.path.join(writer.build_directory, "sub")
            assert os.path.isdir(path)
            dest = os.path.join(path, "c")
            assert os.path.isfile(dest)
            with open(dest) as f:
                output = f.read()
                self.assertEqual(output, "d")

    def test_glob(self):
        """Can the FilesWriter handle globbed files correctly?"""

        # Work in a temporary directory.
        with self.create_temp_cwd():

            # Create test files
            os.mkdir("sub")
            with open(os.path.join("sub", "c"), "w") as f:
                f.write("e")
            with open(os.path.join("sub", "d"), "w") as f:
                f.write("e")

            # Create the resoruces dictionary
            res = {}

            # Create files writer, test output
            writer = FilesWriter()
            writer.files = ["sub/*"]
            writer.build_directory = "build"
            writer.write("y", res, notebook_name="z")

            # Check the output of the file
            assert os.path.isdir(writer.build_directory)
            dest = os.path.join(writer.build_directory, "z")
            with open(dest) as f:
                output = f.read()
                self.assertEqual(output, "y")

            # Check to make sure the globbed files were copied
            path = os.path.join(writer.build_directory, "sub")
            assert os.path.isdir(path)
            for filename in ["c", "d"]:
                dest = os.path.join(path, filename)
                assert os.path.isfile(dest)
                with open(dest) as f:
                    output = f.read()
                    self.assertEqual(output, "e")

    def test_relpath(self):
        """Can the FilesWriter handle relative paths for linked files correctly?"""

        # Work in a temporary directory.
        with self.create_temp_cwd():

            # Create test file
            os.mkdir("sub")
            with open(os.path.join("sub", "c"), "w") as f:
                f.write("d")

            # Create the resoruces dictionary
            res = {}

            # Create files writer, test output
            writer = FilesWriter()
            writer.files = [os.path.join("sub", "c")]
            writer.build_directory = "build"
            writer.relpath = "sub"
            writer.write("y", res, notebook_name="z")

            # Check the output of the file
            assert os.path.isdir(writer.build_directory)
            dest = os.path.join(writer.build_directory, "z")
            with open(dest) as f:
                output = f.read()
                self.assertEqual(output, "y")

            # Check to make sure the linked file was copied
            dest = os.path.join(writer.build_directory, "c")
            assert os.path.isfile(dest)
            with open(dest) as f:
                output = f.read()
                self.assertEqual(output, "d")

    def test_relpath_default(self):
        """Is the FilesWriter default relative path correct?"""

        # Work in a temporary directory.
        with self.create_temp_cwd():

            # Create test file
            os.mkdir("sub")
            with open(os.path.join("sub", "c"), "w") as f:
                f.write("d")

            # Create the resoruces dictionary
            res = dict(metadata=dict(path="sub"))

            # Create files writer, test output
            writer = FilesWriter()
            writer.files = [os.path.join("sub", "c")]
            writer.build_directory = "build"
            writer.write("y", res, notebook_name="z")

            # Check the output of the file
            assert os.path.isdir(writer.build_directory)
            dest = os.path.join(writer.build_directory, "z")
            with open(dest) as f:
                output = f.read()
                self.assertEqual(output, "y")

            # Check to make sure the linked file was copied
            dest = os.path.join(writer.build_directory, "c")
            assert os.path.isfile(dest)
            with open(dest) as f:
                output = f.read()
                self.assertEqual(output, "d")

    def test_relpath_precedence(self):
        """Does the FilesWriter relpath option take precedence over the path?"""

        # Work in a temporary directory.
        with self.create_temp_cwd():

            # Create test file
            os.mkdir("sub")
            with open(os.path.join("sub", "c"), "w") as f:
                f.write("d")

            # Create the resoruces dictionary
            res = dict(metadata=dict(path="other_sub"))

            # Create files writer, test output
            writer = FilesWriter()
            writer.files = [os.path.join("sub", "c")]
            writer.build_directory = "build"
            writer.relpath = "sub"
            writer.write("y", res, notebook_name="z")

            # Check the output of the file
            assert os.path.isdir(writer.build_directory)
            dest = os.path.join(writer.build_directory, "z")
            with open(dest) as f:
                output = f.read()
                self.assertEqual(output, "y")

            # Check to make sure the linked file was copied
            dest = os.path.join(writer.build_directory, "c")
            assert os.path.isfile(dest)
            with open(dest) as f:
                output = f.read()
                self.assertEqual(output, "d")
