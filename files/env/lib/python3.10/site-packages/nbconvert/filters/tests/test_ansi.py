"""
Module with tests for ansi filters
"""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.


from ...tests.base import TestsBase
from ..ansi import ansi2html, ansi2latex, strip_ansi


class TestAnsi(TestsBase):
    """Contains test functions for ansi.py"""

    def test_strip_ansi(self):
        """strip_ansi test"""
        correct_outputs = {
            "\x1b[32m\x1b[1m\x1b[0;44m\x1b[38;2;255;0;255m\x1b[;m\x1b[m": "",
            "hello\x1b[000;34m": "hello",
            "he\x1b[1;33m\x1b[;36mllo": "hello",
            "\x1b[;34mhello": "hello",
            "\x1b[31mh\x1b[31me\x1b[31ml\x1b[31ml\x1b[31mo\x1b[31m": "hello",
            "hel\x1b[;00;;032;;;32mlo": "hello",
            "hello": "hello",
        }

        for inval, outval in correct_outputs.items():
            self.assertEqual(outval, strip_ansi(inval))

    def test_ansi2html(self):
        """ansi2html test"""
        correct_outputs = {
            "\x1b[31m": "",
            "hello\x1b[34m": "hello",
            "he\x1b[32m\x1b[36mllo": 'he<span class="ansi-cyan-fg">llo</span>',
            "\x1b[1;33mhello": '<span class="ansi-yellow-intense-fg ansi-bold">hello</span>',
            "\x1b[37mh\x1b[0;037me\x1b[;0037ml\x1b[00;37ml\x1b[;;37mo": '<span class="ansi-white-fg">h</span><span class="ansi-white-fg">e</span><span class="ansi-white-fg">l</span><span class="ansi-white-fg">l</span><span class="ansi-white-fg">o</span>',
            "hel\x1b[0;32mlo": 'hel<span class="ansi-green-fg">lo</span>',
            "hellø": "hellø",
            "\x1b[1mhello\x1b[33mworld\x1b[0m": '<span class="ansi-bold">hello</span><span class="ansi-yellow-intense-fg ansi-bold">world</span>',
            "he\x1b[4mll\x1b[24mo": 'he<span class="ansi-underline">ll</span>o',
            "\x1b[35mhe\x1b[7mll\x1b[27mo": '<span class="ansi-magenta-fg">he</span><span class="ansi-default-inverse-fg ansi-magenta-bg">ll</span><span class="ansi-magenta-fg">o</span>',
            "\x1b[44mhe\x1b[7mll\x1b[27mo": '<span class="ansi-blue-bg">he</span><span class="ansi-blue-fg ansi-default-inverse-bg">ll</span><span class="ansi-blue-bg">o</span>',
        }

        for inval, outval in correct_outputs.items():
            self.assertEqual(outval, ansi2html(inval))

    def test_ansi2latex(self):
        """ansi2latex test"""
        correct_outputs = {
            "\x1b[31m": "",
            "hello\x1b[34m": "hello",
            "he\x1b[32m\x1b[36mllo": r"he\textcolor{ansi-cyan}{llo}",
            "\x1b[1;33mhello": r"\textcolor{ansi-yellow-intense}{\textbf{hello}}",
            "\x1b[37mh\x1b[0;037me\x1b[;0037ml\x1b[00;37ml\x1b[;;37mo": r"\textcolor{ansi-white}{h}\textcolor{ansi-white}{e}\textcolor{ansi-white}{l}\textcolor{ansi-white}{l}\textcolor{ansi-white}{o}",
            "hel\x1b[0;32mlo": r"hel\textcolor{ansi-green}{lo}",
            "hello": "hello",
            "hello\x1b[34mthere\x1b[mworld": r"hello\textcolor{ansi-blue}{there}world",
            "hello\x1b[mthere": "hellothere",
            "hello\x1b[01;34mthere": r"hello\textcolor{ansi-blue-intense}{\textbf{there}}",
            "hello\x1b[001;34mthere": r"hello\textcolor{ansi-blue-intense}{\textbf{there}}",
            "\x1b[1mhello\x1b[33mworld\x1b[0m": r"\textbf{hello}\textcolor{ansi-yellow-intense}{\textbf{world}}",
            "he\x1b[4mll\x1b[24mo": "he\\underline{ll}o",
            "\x1b[35mhe\x1b[7mll\x1b[27mo": r"\textcolor{ansi-magenta}{he}\textcolor{ansi-default-inverse-fg}{\setlength{\fboxsep}{0pt}\colorbox{ansi-magenta}{ll\strut}}\textcolor{ansi-magenta}{o}",
            "\x1b[44mhe\x1b[7mll\x1b[27mo": r"\setlength{\fboxsep}{0pt}\colorbox{ansi-blue}{he\strut}\textcolor{ansi-blue}{\setlength{\fboxsep}{0pt}\colorbox{ansi-default-inverse-bg}{ll\strut}}\setlength{\fboxsep}{0pt}\colorbox{ansi-blue}{o\strut}",
        }

        for inval, outval in correct_outputs.items():
            self.assertEqual(outval, ansi2latex(inval))
