"""Tests for SlidesExporter"""

# Copyright (c) IPython Development Team.
# Distributed under the terms of the Modified BSD License.

from nbformat import v4 as nbformat

from ..slides import SlidesExporter, _RevealMetadataPreprocessor
from .base import ExportersTestsBase


class TestSlidesExporter(ExportersTestsBase):
    """Tests for SlidesExporter"""

    exporter_class = SlidesExporter
    should_include_raw = ["html"]

    def test_constructor(self):
        """
        Can a SlidesExporter be constructed?
        """
        SlidesExporter()

    def test_export(self):
        """
        Can a SlidesExporter export something?
        """
        (output, resources) = SlidesExporter().from_filename(self._get_notebook())
        assert len(output) > 0

    def test_export_reveal(self):
        """
        Can a SlidesExporter export using the 'reveal' template?
        """
        (output, resources) = SlidesExporter().from_filename(self._get_notebook())
        assert len(output) > 0

    def build_notebook(self):
        """Build a reveal slides notebook in memory for use with tests."""
        outputs = [nbformat.new_output(output_type="stream", name="stdout", text="a")]

        slide_metadata = {"slideshow": {"slide_type": "slide"}}
        subslide_metadata = {"slideshow": {"slide_type": "subslide"}}
        fragment_metadata = {"slideshow": {"slide_type": "fragment"}}

        cells = [
            nbformat.new_code_cell(source="", execution_count=1, outputs=outputs),
            nbformat.new_markdown_cell(source="", metadata=slide_metadata),
            nbformat.new_code_cell(source="", execution_count=2, outputs=outputs),
            nbformat.new_markdown_cell(source="", metadata=slide_metadata),
            nbformat.new_markdown_cell(source="", metadata=subslide_metadata),
            nbformat.new_markdown_cell(source="", metadata=fragment_metadata),
            nbformat.new_code_cell(source="", execution_count=1, outputs=outputs),
        ]

        return nbformat.new_notebook(cells=cells)

    def test_metadata_preprocessor(self):
        preprocessor = _RevealMetadataPreprocessor()
        nb = self.build_notebook()
        nb, resources = preprocessor.preprocess(nb)
        cells = nb.cells

        # Make sure correct metadata tags are available on every cell.
        for cell in cells:
            assert "slide_type" in cell.metadata

        # Make sure slide end is only applied to the cells preceeding slide
        # cells.
        assert not cells[1].metadata.get("slide_end", False)

        # Verify 'slide-end'
        assert cells[0].metadata["slide_end"]
        assert cells[2].metadata["slide_end"]
        assert cells[2].metadata["subslide_end"]

        assert not cells[3].metadata.get("slide_end", False)
        assert cells[3].metadata["subslide_end"]

        assert cells[-1].metadata["fragment_end"]
        assert cells[-1].metadata["subslide_end"]
        assert cells[-1].metadata["slide_end"]
