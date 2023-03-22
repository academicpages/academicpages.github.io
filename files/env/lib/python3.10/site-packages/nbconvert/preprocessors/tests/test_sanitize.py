"""Tests for the HTMLSanitize preprocessor"""

from nbformat import v4 as nbformat

from ..sanitize import SanitizeHTML
from .base import PreprocessorTestsBase


class TestSanitizer(PreprocessorTestsBase):
    """Contains test functions for sanitize.py"""

    maxDiff = None

    def build_preprocessor(self):
        """Make an instance of a preprocessor"""
        preprocessor = SanitizeHTML()
        preprocessor.enabled = True
        return preprocessor

    def preprocess_source(self, cell_type, source, preprocessor):
        nb = self.build_notebook()
        res = self.build_resources()

        nb.cells[0].cell_type = cell_type
        nb.cells[0].source = source

        nb, res = preprocessor(nb, res)

        return nb.cells[0].source

    def test_constructor(self):
        """Can a SanitizeHTML be constructed?"""
        self.build_preprocessor()

    def test_svg_handling(self):
        """
        Test to make sure that svgs are handled 'properly'

        We only allow <img> tags (via markdown syntax) and not all the other ways
        to embed svg: <object>, <embed>, <iframe> nor inline <svg>
        """
        preprocessor = self.build_preprocessor()
        preprocessor.strip = True

        self.assertEqual(
            self.preprocess_source(
                "markdown",
                """
                ![some image](http://example.com/something.svg)

                <object data="something.svg" type="image/svg+xml"></object>

                <embed data="something.svg" type="image/svg+xml" />

                <iframe src="http://example.com/something.svg"></iframe>

                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 68 65">
                    <path fill="#1A374D" d="M42 27v-20c0-3.7-3.3-7-7-7s-7 3.3-7 7v21l12 15-7 15.7c14.5 13.9 35 2.8 35-13.7 0-13.3-13.4-21.8-26-18zm6 25c-3.9 0-7-3.1-7-7s3.1-7 7-7 7 3.1 7 7-3.1 7-7 7z"/>
                    <path d="M14 27v-20c0-3.7-3.3-7-7-7s-7 3.3-7 7v41c0 8.2 9.2 17 20 17s20-9.2 20-20c0-13.3-13.4-21.8-26-18zm6 25c-3.9 0-7-3.1-7-7s3.1-7 7-7 7 3.1 7 7-3.1 7-7 7z"/>
                </svg>
                """,
                preprocessor,
            ).strip(),
            """
            ![some image](http://example.com/something.svg)
            """.strip(),
        )

    def test_tag_allowlist_stripping(self):
        """Test tag allowlisting + stripping out offending tags"""
        preprocessor = self.build_preprocessor()
        preprocessor.strip = True

        self.assertEqual(
            self.preprocess_source(
                "markdown", "_A_ <em>few</em> <script>tags</script>", preprocessor
            ),
            "_A_ <em>few</em> tags",
        )

    def test_comment_stripping(self):
        """Test HTML comment stripping"""
        preprocessor = self.build_preprocessor()

        self.assertEqual(
            self.preprocess_source("markdown", "_A_ <em>few</em> <!-- tags -->", preprocessor),
            "_A_ <em>few</em> ",
        )

        preprocessor.strip_comments = False
        self.assertEqual(
            self.preprocess_source("markdown", "_A_ <em>few</em> <!-- tags -->", preprocessor),
            "_A_ <em>few</em> <!-- tags -->",
        )

    def test_attributes_allowlist(self):
        """Test style"""
        preprocessor = self.build_preprocessor()

        preprocessor.attributes["a"] = ["href", "title"]

        self.assertEqual(
            self.preprocess_source(
                "markdown", '<a href="link" rel="nofollow">Hi</a>', preprocessor
            ),
            '<a href="link">Hi</a>',
        )

    def test_style_allowlist(self):
        """Test style"""
        preprocessor = self.build_preprocessor()

        if "*" in preprocessor.attributes:
            preprocessor.attributes["*"].append("style")
        else:
            preprocessor.attributes["*"] = ["style"]
        preprocessor.styles = [
            "color",
        ]

        self.assertEqual(
            self.preprocess_source(
                "markdown",
                '_A_ <em style="color: blue; background-color: pink">'
                "few</em> <script>tags</script>",
                preprocessor,
            ),
            '_A_ <em style="color: blue;">few</em> &lt;script&gt;tags&lt;/script&gt;',
        )

    def test_tag_passthrough(self):
        """Test passing through raw output"""
        preprocessor = self.build_preprocessor()

        self.assertEqual(
            self.preprocess_source("raw", "_A_ <em>few</em> <script>tags</script>", preprocessor),
            "_A_ <em>few</em> &lt;script&gt;tags&lt;/script&gt;",
        )

    def test_output_sanitizing(self):
        """Test that outputs are also sanitized properly"""
        preprocessor = self.build_preprocessor()
        nb = self.build_notebook()

        outputs = [
            nbformat.new_output(
                "display_data",
                data={
                    "text/plain": "b",
                    "text/html": "<script>more evil</script>",
                    "text/css": "<style> * {display:none}</style>",
                },
            ),
            nbformat.new_output("stream", name="stdout", text="wat"),
            nbformat.new_output("stream", name="stdout", text="<script>Evil tag</script>"),
        ]
        nb.cells[0].outputs = outputs

        res = self.build_resources()
        nb, res = preprocessor(nb, res)

        expected_output = [
            {
                "data": {"text/html": "&lt;script&gt;more evil&lt;/script&gt;", "text/plain": "b"},
                "metadata": {},
                "output_type": "display_data",
            },
            {"name": "stdout", "output_type": "stream", "text": "wat"},
            {"name": "stdout", "output_type": "stream", "text": "<script>Evil tag</script>"},
        ]
        self.assertEqual(nb.cells[0].outputs, expected_output)

    def test_tag_allowlist(self):
        """Test tag allowlisting"""
        preprocessor = self.build_preprocessor()

        self.assertEqual(
            self.preprocess_source(
                "markdown", "_A_ <em>few</em> <script>tags</script>", preprocessor
            ),
            "_A_ <em>few</em> &lt;script&gt;tags&lt;/script&gt;",
        )
