"""Export to PDF via a headless browser"""

# Copyright (c) IPython Development Team.
# Distributed under the terms of the Modified BSD License.

import asyncio
import concurrent.futures
import os
import tempfile

from traitlets import Bool, default

from .html import HTMLExporter


class WebPDFExporter(HTMLExporter):
    """Writer designed to write to PDF files.

    This inherits from :class:`HTMLExporter`. It creates the HTML using the
    template machinery, and then run pyppeteer to create a pdf.
    """

    export_from_notebook = "PDF via HTML"

    allow_chromium_download = Bool(
        False,
        help="Whether to allow downloading Chromium if no suitable version is found on the system.",
    ).tag(config=True)

    paginate = Bool(
        True,
        help="""
        Split generated notebook into multiple pages.

        If False, a PDF with one long page will be generated.

        Set to True to match behavior of LaTeX based PDF generator
        """,
    ).tag(config=True)

    output_mimetype = "text/html"

    @default("file_extension")
    def _file_extension_default(self):
        return ".html"

    @default("template_name")
    def _template_name_default(self):
        return "webpdf"

    disable_sandbox = Bool(
        False,
        help="""
        Disable chromium security sandbox when converting to PDF.

        WARNING: This could cause arbitrary code execution in specific circumstances,
        where JS in your notebook can execute serverside code! Please use with
        caution.

        ``https://github.com/puppeteer/puppeteer/blob/main@%7B2020-12-14T17:22:24Z%7D/docs/troubleshooting.md#setting-up-chrome-linux-sandbox``
        has more information.

        This is required for webpdf to work inside most container environments.
        """,
    ).tag(config=True)

    def _check_launch_reqs(self):
        try:
            from pyppeteer import launch
            from pyppeteer.util import check_chromium
        except ModuleNotFoundError as e:
            raise RuntimeError(
                "Pyppeteer is not installed to support Web PDF conversion. "
                "Please install `nbconvert[webpdf]` to enable."
            ) from e
        if not self.allow_chromium_download and not check_chromium():
            raise RuntimeError(
                "No suitable chromium executable found on the system. "
                "Please use '--allow-chromium-download' to allow downloading one."
            )
        return launch

    def run_pyppeteer(self, html):
        """Run pyppeteer."""

        async def main(temp_file):
            args = ["--no-sandbox"] if self.disable_sandbox else []
            browser = await self._check_launch_reqs()(
                handleSIGINT=False, handleSIGTERM=False, handleSIGHUP=False, args=args
            )
            page = await browser.newPage()
            await page.emulateMedia("screen")
            await page.waitFor(100)
            await page.goto(f"file://{temp_file.name}", waitUntil="networkidle0")
            await page.waitFor(100)

            pdf_params = {"printBackground": True}
            if not self.paginate:
                # Floating point precision errors cause the printed
                # PDF from spilling over a new page by a pixel fraction.
                dimensions = await page.evaluate(
                    """() => {
                    const rect = document.body.getBoundingClientRect();
                    return {
                    width: Math.ceil(rect.width) + 1,
                    height: Math.ceil(rect.height) + 1,
                    }
                }"""
                )
                width = dimensions["width"]
                height = dimensions["height"]
                # 200 inches is the maximum size for Adobe Acrobat Reader.
                pdf_params.update(
                    {
                        "width": min(width, 200 * 72),
                        "height": min(height, 200 * 72),
                    }
                )
            pdf_data = await page.pdf(pdf_params)

            await browser.close()
            return pdf_data

        pool = concurrent.futures.ThreadPoolExecutor()
        # Create a temporary file to pass the HTML code to Chromium:
        # Unfortunately, tempfile on Windows does not allow for an already open
        # file to be opened by a separate process. So we must close it first
        # before calling Chromium. We also specify delete=False to ensure the
        # file is not deleted after closing (the default behavior).
        temp_file = tempfile.NamedTemporaryFile(suffix=".html", delete=False)
        with temp_file:
            temp_file.write(html.encode("utf-8"))
        try:
            # TODO: when dropping Python 3.6, use
            # pdf_data = pool.submit(asyncio.run, main(temp_file)).result()
            def run_coroutine(coro):
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                return loop.run_until_complete(coro)

            pdf_data = pool.submit(run_coroutine, main(temp_file)).result()
        finally:
            # Ensure the file is deleted even if pypeteer raises an exception
            os.unlink(temp_file.name)
        return pdf_data

    def from_notebook_node(self, nb, resources=None, **kw):
        self._check_launch_reqs()
        html, resources = super().from_notebook_node(nb, resources=resources, **kw)

        self.log.info("Building PDF")
        pdf_data = self.run_pyppeteer(html)
        self.log.info("PDF successfully created")

        # convert output extension to pdf
        # the writer above required it to be html
        resources["output_extension"] = ".pdf"

        return pdf_data, resources
