"""Tests of the bs4.element.PageElement class"""
import copy
import pickle
import pytest

from soupsieve import SelectorSyntaxError

from bs4 import BeautifulSoup
from bs4.element import (
    Comment,
    SoupStrainer,
)
from . import SoupTest


class TestEncoding(SoupTest):
    """Test the ability to encode objects into strings."""

    def test_unicode_string_can_be_encoded(self):
        html = "<b>\N{SNOWMAN}</b>"
        soup = self.soup(html)
        assert soup.b.string.encode("utf-8") == "\N{SNOWMAN}".encode("utf-8")

    def test_tag_containing_unicode_string_can_be_encoded(self):
        html = "<b>\N{SNOWMAN}</b>"
        soup = self.soup(html)
        assert soup.b.encode("utf-8") == html.encode("utf-8")

    def test_encoding_substitutes_unrecognized_characters_by_default(self):
        html = "<b>\N{SNOWMAN}</b>"
        soup = self.soup(html)
        assert soup.b.encode("ascii") == b"<b>&#9731;</b>"

    def test_encoding_can_be_made_strict(self):
        html = "<b>\N{SNOWMAN}</b>"
        soup = self.soup(html)
        with pytest.raises(UnicodeEncodeError):
            soup.encode("ascii", errors="strict")

    def test_decode_contents(self):
        html = "<b>\N{SNOWMAN}</b>"
        soup = self.soup(html)
        assert "\N{SNOWMAN}" == soup.b.decode_contents()

    def test_encode_contents(self):
        html = "<b>\N{SNOWMAN}</b>"
        soup = self.soup(html)
        assert "\N{SNOWMAN}".encode("utf8") == soup.b.encode_contents(
            encoding="utf8"
        )

    def test_deprecated_renderContents(self):
        html = "<b>\N{SNOWMAN}</b>"
        soup = self.soup(html)
        assert "\N{SNOWMAN}".encode("utf8") == soup.b.renderContents()

    def test_repr(self):
        html = "<b>\N{SNOWMAN}</b>"
        soup = self.soup(html)
        assert html == repr(soup)

        
class TestFormatters(SoupTest):
    """Test the formatting feature, used by methods like decode() and
    prettify(), and the formatters themselves.
    """
    
    def test_default_formatter_is_minimal(self):
        markup = "<b>&lt;&lt;Sacr\N{LATIN SMALL LETTER E WITH ACUTE} bleu!&gt;&gt;</b>"
        soup = self.soup(markup)
        decoded = soup.decode(formatter="minimal")
        # The < is converted back into &lt; but the e-with-acute is left alone.
        assert decoded == self.document_for(
                "<b>&lt;&lt;Sacr\N{LATIN SMALL LETTER E WITH ACUTE} bleu!&gt;&gt;</b>"
        )

    def test_formatter_html(self):
        markup = "<br><b>&lt;&lt;Sacr\N{LATIN SMALL LETTER E WITH ACUTE} bleu!&gt;&gt;</b>"
        soup = self.soup(markup)
        decoded = soup.decode(formatter="html")
        assert decoded == self.document_for(
            "<br/><b>&lt;&lt;Sacr&eacute; bleu!&gt;&gt;</b>"
        )

    def test_formatter_html5(self):
        markup = "<br><b>&lt;&lt;Sacr\N{LATIN SMALL LETTER E WITH ACUTE} bleu!&gt;&gt;</b>"
        soup = self.soup(markup)
        decoded = soup.decode(formatter="html5")
        assert decoded == self.document_for(
            "<br><b>&lt;&lt;Sacr&eacute; bleu!&gt;&gt;</b>"
        )
        
    def test_formatter_minimal(self):
        markup = "<b>&lt;&lt;Sacr\N{LATIN SMALL LETTER E WITH ACUTE} bleu!&gt;&gt;</b>"
        soup = self.soup(markup)
        decoded = soup.decode(formatter="minimal")
        # The < is converted back into &lt; but the e-with-acute is left alone.
        assert decoded == self.document_for(
                "<b>&lt;&lt;Sacr\N{LATIN SMALL LETTER E WITH ACUTE} bleu!&gt;&gt;</b>"
        )

    def test_formatter_null(self):
        markup = "<b>&lt;&lt;Sacr\N{LATIN SMALL LETTER E WITH ACUTE} bleu!&gt;&gt;</b>"
        soup = self.soup(markup)
        decoded = soup.decode(formatter=None)
        # Neither the angle brackets nor the e-with-acute are converted.
        # This is not valid HTML, but it's what the user wanted.
        assert decoded == self.document_for(
            "<b><<Sacr\N{LATIN SMALL LETTER E WITH ACUTE} bleu!>></b>"
        )

    def test_formatter_custom(self):
        markup = "<b>&lt;foo&gt;</b><b>bar</b><br/>"
        soup = self.soup(markup)
        decoded = soup.decode(formatter = lambda x: x.upper())
        # Instead of normal entity conversion code, the custom
        # callable is called on every string.
        assert decoded == self.document_for("<b><FOO></b><b>BAR</b><br/>")

    def test_formatter_is_run_on_attribute_values(self):
        markup = '<a href="http://a.com?a=b&c=é">e</a>'
        soup = self.soup(markup)
        a = soup.a

        expect_minimal = '<a href="http://a.com?a=b&amp;c=é">e</a>'

        assert expect_minimal == a.decode()
        assert expect_minimal == a.decode(formatter="minimal")

        expect_html = '<a href="http://a.com?a=b&amp;c=&eacute;">e</a>'
        assert expect_html == a.decode(formatter="html")

        assert markup == a.decode(formatter=None)
        expect_upper = '<a href="HTTP://A.COM?A=B&C=É">E</a>'
        assert expect_upper == a.decode(formatter=lambda x: x.upper())

    def test_formatter_skips_script_tag_for_html_documents(self):
        doc = """
  <script type="text/javascript">
   console.log("< < hey > > ");
  </script>
"""
        encoded = BeautifulSoup(doc, 'html.parser').encode()
        assert b"< < hey > >" in encoded

    def test_formatter_skips_style_tag_for_html_documents(self):
        doc = """
  <style type="text/css">
   console.log("< < hey > > ");
  </style>
"""
        encoded = BeautifulSoup(doc, 'html.parser').encode()
        assert b"< < hey > >" in encoded

    def test_prettify_leaves_preformatted_text_alone(self):
        soup = self.soup("<div>  foo  <pre>  \tbar\n  \n  </pre>  baz  <textarea> eee\nfff\t</textarea></div>")
        # Everything outside the <pre> tag is reformatted, but everything
        # inside is left alone.
        assert '<div>\n foo\n <pre>  \tbar\n  \n  </pre>\n baz\n <textarea> eee\nfff\t</textarea>\n</div>' == soup.div.prettify()

    def test_prettify_accepts_formatter_function(self):
        soup = BeautifulSoup("<html><body>foo</body></html>", 'html.parser')
        pretty = soup.prettify(formatter = lambda x: x.upper())
        assert "FOO" in pretty

    def test_prettify_outputs_unicode_by_default(self):
        soup = self.soup("<a></a>")
        assert str == type(soup.prettify())

    def test_prettify_can_encode_data(self):
        soup = self.soup("<a></a>")
        assert bytes == type(soup.prettify("utf-8"))

    def test_html_entity_substitution_off_by_default(self):
        markup = "<b>Sacr\N{LATIN SMALL LETTER E WITH ACUTE} bleu!</b>"
        soup = self.soup(markup)
        encoded = soup.b.encode("utf-8")
        assert encoded == markup.encode('utf-8')

    def test_encoding_substitution(self):
        # Here's the <meta> tag saying that a document is
        # encoded in Shift-JIS.
        meta_tag = ('<meta content="text/html; charset=x-sjis" '
                    'http-equiv="Content-type"/>')
        soup = self.soup(meta_tag)

        # Parse the document, and the charset apprears unchanged.
        assert soup.meta['content'] == 'text/html; charset=x-sjis'

        # Encode the document into some encoding, and the encoding is
        # substituted into the meta tag.
        utf_8 = soup.encode("utf-8")
        assert b"charset=utf-8" in utf_8

        euc_jp = soup.encode("euc_jp")
        assert b"charset=euc_jp" in euc_jp

        shift_jis = soup.encode("shift-jis")
        assert b"charset=shift-jis" in shift_jis

        utf_16_u = soup.encode("utf-16").decode("utf-16")
        assert "charset=utf-16" in utf_16_u

    def test_encoding_substitution_doesnt_happen_if_tag_is_strained(self):
        markup = ('<head><meta content="text/html; charset=x-sjis" '
                    'http-equiv="Content-type"/></head><pre>foo</pre>')

        # Beautiful Soup used to try to rewrite the meta tag even if the
        # meta tag got filtered out by the strainer. This test makes
        # sure that doesn't happen.
        strainer = SoupStrainer('pre')
        soup = self.soup(markup, parse_only=strainer)
        assert soup.contents[0].name == 'pre'


class TestCSSSelectors(SoupTest):
    """Test basic CSS selector functionality.

    This functionality is implemented in soupsieve, which has a much
    more comprehensive test suite, so this is basically an extra check
    that soupsieve works as expected.
    """

    HTML = """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
"http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<title>The title</title>
<link rel="stylesheet" href="blah.css" type="text/css" id="l1">
</head>
<body>
<custom-dashed-tag class="dashed" id="dash1">Hello there.</custom-dashed-tag>
<div id="main" class="fancy">
<div id="inner">
<h1 id="header1">An H1</h1>
<p>Some text</p>
<p class="onep" id="p1">Some more text</p>
<h2 id="header2">An H2</h2>
<p class="class1 class2 class3" id="pmulti">Another</p>
<a href="http://bob.example.org/" rel="friend met" id="bob">Bob</a>
<h2 id="header3">Another H2</h2>
<a id="me" href="http://simonwillison.net/" rel="me">me</a>
<span class="s1">
<a href="#" id="s1a1">span1a1</a>
<a href="#" id="s1a2">span1a2 <span id="s1a2s1">test</span></a>
<span class="span2">
<a href="#" id="s2a1">span2a1</a>
</span>
<span class="span3"></span>
<custom-dashed-tag class="dashed" id="dash2"/>
<div data-tag="dashedvalue" id="data1"/>
</span>
</div>
<x id="xid">
<z id="zida"/>
<z id="zidab"/>
<z id="zidac"/>
</x>
<y id="yid">
<z id="zidb"/>
</y>
<p lang="en" id="lang-en">English</p>
<p lang="en-gb" id="lang-en-gb">English UK</p>
<p lang="en-us" id="lang-en-us">English US</p>
<p lang="fr" id="lang-fr">French</p>
</div>

<div id="footer">
</div>
"""

    def setup_method(self):
        self.soup = BeautifulSoup(self.HTML, 'html.parser')

    def assert_selects(self, selector, expected_ids, **kwargs):
        el_ids = [el['id'] for el in self.soup.select(selector, **kwargs)]
        el_ids.sort()
        expected_ids.sort()
        assert expected_ids == el_ids, "Selector %s, expected [%s], got [%s]" % (
                selector, ', '.join(expected_ids), ', '.join(el_ids)
        )

    assertSelect = assert_selects

    def assert_select_multiple(self, *tests):
        for selector, expected_ids in tests:
            self.assert_selects(selector, expected_ids)

    def test_one_tag_one(self):
        els = self.soup.select('title')
        assert len(els) == 1
        assert els[0].name == 'title'
        assert els[0].contents == ['The title']

    def test_one_tag_many(self):
        els = self.soup.select('div')
        assert len(els) == 4
        for div in els:
            assert div.name == 'div'

        el = self.soup.select_one('div')
        assert 'main' == el['id']

    def test_select_one_returns_none_if_no_match(self):
        match = self.soup.select_one('nonexistenttag')
        assert None == match


    def test_tag_in_tag_one(self):
        els = self.soup.select('div div')
        self.assert_selects('div div', ['inner', 'data1'])

    def test_tag_in_tag_many(self):
        for selector in ('html div', 'html body div', 'body div'):
            self.assert_selects(selector, ['data1', 'main', 'inner', 'footer'])


    def test_limit(self):
        self.assert_selects('html div', ['main'], limit=1)
        self.assert_selects('html body div', ['inner', 'main'], limit=2)
        self.assert_selects('body div', ['data1', 'main', 'inner', 'footer'],
                           limit=10)

    def test_tag_no_match(self):
        assert len(self.soup.select('del')) == 0

    def test_invalid_tag(self):
        with pytest.raises(SelectorSyntaxError):
            self.soup.select('tag%t')

    def test_select_dashed_tag_ids(self):
        self.assert_selects('custom-dashed-tag', ['dash1', 'dash2'])

    def test_select_dashed_by_id(self):
        dashed = self.soup.select('custom-dashed-tag[id=\"dash2\"]')
        assert dashed[0].name == 'custom-dashed-tag'
        assert dashed[0]['id'] == 'dash2'

    def test_dashed_tag_text(self):
        assert self.soup.select('body > custom-dashed-tag')[0].text == 'Hello there.'

    def test_select_dashed_matches_find_all(self):
        assert self.soup.select('custom-dashed-tag') == self.soup.find_all('custom-dashed-tag')

    def test_header_tags(self):
        self.assert_select_multiple(
            ('h1', ['header1']),
            ('h2', ['header2', 'header3']),
        )

    def test_class_one(self):
        for selector in ('.onep', 'p.onep', 'html p.onep'):
            els = self.soup.select(selector)
            assert len(els) == 1
            assert els[0].name == 'p'
            assert els[0]['class'] == ['onep']

    def test_class_mismatched_tag(self):
        els = self.soup.select('div.onep')
        assert len(els) == 0

    def test_one_id(self):
        for selector in ('div#inner', '#inner', 'div div#inner'):
            self.assert_selects(selector, ['inner'])

    def test_bad_id(self):
        els = self.soup.select('#doesnotexist')
        assert len(els) == 0

    def test_items_in_id(self):
        els = self.soup.select('div#inner p')
        assert len(els) == 3
        for el in els:
            assert el.name == 'p'
        assert els[1]['class'] == ['onep']
        assert not els[0].has_attr('class')

    def test_a_bunch_of_emptys(self):
        for selector in ('div#main del', 'div#main div.oops', 'div div#main'):
            assert len(self.soup.select(selector)) == 0

    def test_multi_class_support(self):
        for selector in ('.class1', 'p.class1', '.class2', 'p.class2',
            '.class3', 'p.class3', 'html p.class2', 'div#inner .class2'):
            self.assert_selects(selector, ['pmulti'])

    def test_multi_class_selection(self):
        for selector in ('.class1.class3', '.class3.class2',
                         '.class1.class2.class3'):
            self.assert_selects(selector, ['pmulti'])

    def test_child_selector(self):
        self.assert_selects('.s1 > a', ['s1a1', 's1a2'])
        self.assert_selects('.s1 > a span', ['s1a2s1'])

    def test_child_selector_id(self):
        self.assert_selects('.s1 > a#s1a2 span', ['s1a2s1'])

    def test_attribute_equals(self):
        self.assert_select_multiple(
            ('p[class="onep"]', ['p1']),
            ('p[id="p1"]', ['p1']),
            ('[class="onep"]', ['p1']),
            ('[id="p1"]', ['p1']),
            ('link[rel="stylesheet"]', ['l1']),
            ('link[type="text/css"]', ['l1']),
            ('link[href="blah.css"]', ['l1']),
            ('link[href="no-blah.css"]', []),
            ('[rel="stylesheet"]', ['l1']),
            ('[type="text/css"]', ['l1']),
            ('[href="blah.css"]', ['l1']),
            ('[href="no-blah.css"]', []),
            ('p[href="no-blah.css"]', []),
            ('[href="no-blah.css"]', []),
        )

    def test_attribute_tilde(self):
        self.assert_select_multiple(
            ('p[class~="class1"]', ['pmulti']),
            ('p[class~="class2"]', ['pmulti']),
            ('p[class~="class3"]', ['pmulti']),
            ('[class~="class1"]', ['pmulti']),
            ('[class~="class2"]', ['pmulti']),
            ('[class~="class3"]', ['pmulti']),
            ('a[rel~="friend"]', ['bob']),
            ('a[rel~="met"]', ['bob']),
            ('[rel~="friend"]', ['bob']),
            ('[rel~="met"]', ['bob']),
        )

    def test_attribute_startswith(self):
        self.assert_select_multiple(
            ('[rel^="style"]', ['l1']),
            ('link[rel^="style"]', ['l1']),
            ('notlink[rel^="notstyle"]', []),
            ('[rel^="notstyle"]', []),
            ('link[rel^="notstyle"]', []),
            ('link[href^="bla"]', ['l1']),
            ('a[href^="http://"]', ['bob', 'me']),
            ('[href^="http://"]', ['bob', 'me']),
            ('[id^="p"]', ['pmulti', 'p1']),
            ('[id^="m"]', ['me', 'main']),
            ('div[id^="m"]', ['main']),
            ('a[id^="m"]', ['me']),
            ('div[data-tag^="dashed"]', ['data1'])
        )

    def test_attribute_endswith(self):
        self.assert_select_multiple(
            ('[href$=".css"]', ['l1']),
            ('link[href$=".css"]', ['l1']),
            ('link[id$="1"]', ['l1']),
            ('[id$="1"]', ['data1', 'l1', 'p1', 'header1', 's1a1', 's2a1', 's1a2s1', 'dash1']),
            ('div[id$="1"]', ['data1']),
            ('[id$="noending"]', []),
        )

    def test_attribute_contains(self):
        self.assert_select_multiple(
            # From test_attribute_startswith
            ('[rel*="style"]', ['l1']),
            ('link[rel*="style"]', ['l1']),
            ('notlink[rel*="notstyle"]', []),
            ('[rel*="notstyle"]', []),
            ('link[rel*="notstyle"]', []),
            ('link[href*="bla"]', ['l1']),
            ('[href*="http://"]', ['bob', 'me']),
            ('[id*="p"]', ['pmulti', 'p1']),
            ('div[id*="m"]', ['main']),
            ('a[id*="m"]', ['me']),
            # From test_attribute_endswith
            ('[href*=".css"]', ['l1']),
            ('link[href*=".css"]', ['l1']),
            ('link[id*="1"]', ['l1']),
            ('[id*="1"]', ['data1', 'l1', 'p1', 'header1', 's1a1', 's1a2', 's2a1', 's1a2s1', 'dash1']),
            ('div[id*="1"]', ['data1']),
            ('[id*="noending"]', []),
            # New for this test
            ('[href*="."]', ['bob', 'me', 'l1']),
            ('a[href*="."]', ['bob', 'me']),
            ('link[href*="."]', ['l1']),
            ('div[id*="n"]', ['main', 'inner']),
            ('div[id*="nn"]', ['inner']),
            ('div[data-tag*="edval"]', ['data1'])
        )

    def test_attribute_exact_or_hypen(self):
        self.assert_select_multiple(
            ('p[lang|="en"]', ['lang-en', 'lang-en-gb', 'lang-en-us']),
            ('[lang|="en"]', ['lang-en', 'lang-en-gb', 'lang-en-us']),
            ('p[lang|="fr"]', ['lang-fr']),
            ('p[lang|="gb"]', []),
        )

    def test_attribute_exists(self):
        self.assert_select_multiple(
            ('[rel]', ['l1', 'bob', 'me']),
            ('link[rel]', ['l1']),
            ('a[rel]', ['bob', 'me']),
            ('[lang]', ['lang-en', 'lang-en-gb', 'lang-en-us', 'lang-fr']),
            ('p[class]', ['p1', 'pmulti']),
            ('[blah]', []),
            ('p[blah]', []),
            ('div[data-tag]', ['data1'])
        )

    def test_quoted_space_in_selector_name(self):
        html = """<div style="display: wrong">nope</div>
        <div style="display: right">yes</div>
        """
        soup = BeautifulSoup(html, 'html.parser')
        [chosen] = soup.select('div[style="display: right"]')
        assert "yes" == chosen.string

    def test_unsupported_pseudoclass(self):
        with pytest.raises(NotImplementedError):
            self.soup.select("a:no-such-pseudoclass")

        with pytest.raises(SelectorSyntaxError):
            self.soup.select("a:nth-of-type(a)")

    def test_nth_of_type(self):
        # Try to select first paragraph
        els = self.soup.select('div#inner p:nth-of-type(1)')
        assert len(els) == 1
        assert els[0].string == 'Some text'

        # Try to select third paragraph
        els = self.soup.select('div#inner p:nth-of-type(3)')
        assert len(els) == 1
        assert els[0].string == 'Another'

        # Try to select (non-existent!) fourth paragraph
        els = self.soup.select('div#inner p:nth-of-type(4)')
        assert len(els) == 0

        # Zero will select no tags.
        els = self.soup.select('div p:nth-of-type(0)')
        assert len(els) == 0

    def test_nth_of_type_direct_descendant(self):
        els = self.soup.select('div#inner > p:nth-of-type(1)')
        assert len(els) == 1
        assert els[0].string == 'Some text'

    def test_id_child_selector_nth_of_type(self):
        self.assert_selects('#inner > p:nth-of-type(2)', ['p1'])

    def test_select_on_element(self):
        # Other tests operate on the tree; this operates on an element
        # within the tree.
        inner = self.soup.find("div", id="main")
        selected = inner.select("div")
        # The <div id="inner"> tag was selected. The <div id="footer">
        # tag was not.
        self.assert_selects_ids(selected, ['inner', 'data1'])

    def test_overspecified_child_id(self):
        self.assert_selects(".fancy #inner", ['inner'])
        self.assert_selects(".normal #inner", [])

    def test_adjacent_sibling_selector(self):
        self.assert_selects('#p1 + h2', ['header2'])
        self.assert_selects('#p1 + h2 + p', ['pmulti'])
        self.assert_selects('#p1 + #header2 + .class1', ['pmulti'])
        assert [] == self.soup.select('#p1 + p')

    def test_general_sibling_selector(self):
        self.assert_selects('#p1 ~ h2', ['header2', 'header3'])
        self.assert_selects('#p1 ~ #header2', ['header2'])
        self.assert_selects('#p1 ~ h2 + a', ['me'])
        self.assert_selects('#p1 ~ h2 + [rel="me"]', ['me'])
        assert [] == self.soup.select('#inner ~ h2')

    def test_dangling_combinator(self):
        with pytest.raises(SelectorSyntaxError):
            self.soup.select('h1 >')

    def test_sibling_combinator_wont_select_same_tag_twice(self):
        self.assert_selects('p[lang] ~ p', ['lang-en-gb', 'lang-en-us', 'lang-fr'])

    # Test the selector grouping operator (the comma)
    def test_multiple_select(self):
        self.assert_selects('x, y', ['xid', 'yid'])

    def test_multiple_select_with_no_space(self):
        self.assert_selects('x,y', ['xid', 'yid'])

    def test_multiple_select_with_more_space(self):
        self.assert_selects('x,    y', ['xid', 'yid'])

    def test_multiple_select_duplicated(self):
        self.assert_selects('x, x', ['xid'])

    def test_multiple_select_sibling(self):
        self.assert_selects('x, y ~ p[lang=fr]', ['xid', 'lang-fr'])

    def test_multiple_select_tag_and_direct_descendant(self):
        self.assert_selects('x, y > z', ['xid', 'zidb'])

    def test_multiple_select_direct_descendant_and_tags(self):
        self.assert_selects('div > x, y, z', ['xid', 'yid', 'zida', 'zidb', 'zidab', 'zidac'])

    def test_multiple_select_indirect_descendant(self):
        self.assert_selects('div x,y,  z', ['xid', 'yid', 'zida', 'zidb', 'zidab', 'zidac'])

    def test_invalid_multiple_select(self):
        with pytest.raises(SelectorSyntaxError):
            self.soup.select(',x, y')
        with pytest.raises(SelectorSyntaxError):
            self.soup.select('x,,y')

    def test_multiple_select_attrs(self):
        self.assert_selects('p[lang=en], p[lang=en-gb]', ['lang-en', 'lang-en-gb'])

    def test_multiple_select_ids(self):
        self.assert_selects('x, y > z[id=zida], z[id=zidab], z[id=zidb]', ['xid', 'zidb', 'zidab'])

    def test_multiple_select_nested(self):
        self.assert_selects('body > div > x, y > z', ['xid', 'zidb'])

    def test_select_duplicate_elements(self):
        # When markup contains duplicate elements, a multiple select
        # will find all of them.
        markup = '<div class="c1"/><div class="c2"/><div class="c1"/>'
        soup = BeautifulSoup(markup, 'html.parser')
        selected = soup.select(".c1, .c2")
        assert 3 == len(selected)

        # Verify that find_all finds the same elements, though because
        # of an implementation detail it finds them in a different
        # order.
        for element in soup.find_all(class_=['c1', 'c2']):
            assert element in selected


class TestPersistence(SoupTest):
    "Testing features like pickle and deepcopy."

    def setup_method(self):
        self.page = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"
"http://www.w3.org/TR/REC-html40/transitional.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>Beautiful Soup: We called him Tortoise because he taught us.</title>
<link rev="made" href="mailto:leonardr@segfault.org">
<meta name="Description" content="Beautiful Soup: an HTML parser optimized for screen-scraping.">
<meta name="generator" content="Markov Approximation 1.4 (module: leonardr)">
<meta name="author" content="Leonard Richardson">
</head>
<body>
<a href="foo">foo</a>
<a href="foo"><b>bar</b></a>
</body>
</html>"""
        self.tree = self.soup(self.page)

    def test_pickle_and_unpickle_identity(self):
        # Pickling a tree, then unpickling it, yields a tree identical
        # to the original.
        dumped = pickle.dumps(self.tree, 2)
        loaded = pickle.loads(dumped)
        assert loaded.__class__ == BeautifulSoup
        assert loaded.decode() == self.tree.decode()

    def test_deepcopy_identity(self):
        # Making a deepcopy of a tree yields an identical tree.
        copied = copy.deepcopy(self.tree)
        assert copied.decode() == self.tree.decode()

    def test_copy_preserves_encoding(self):
        soup = BeautifulSoup(b'<p>&nbsp;</p>', 'html.parser')
        encoding = soup.original_encoding
        copy = soup.__copy__()
        assert "<p> </p>" == str(copy)
        assert encoding == copy.original_encoding

    def test_copy_preserves_builder_information(self):

        tag = self.soup('<p></p>').p

        # Simulate a tag obtained from a source file.
        tag.sourceline = 10
        tag.sourcepos = 33
        
        copied = tag.__copy__()

        # The TreeBuilder object is no longer availble, but information
        # obtained from it gets copied over to the new Tag object.
        assert tag.sourceline == copied.sourceline
        assert tag.sourcepos == copied.sourcepos
        assert tag.can_be_empty_element == copied.can_be_empty_element
        assert tag.cdata_list_attributes == copied.cdata_list_attributes
        assert tag.preserve_whitespace_tags == copied.preserve_whitespace_tags
        
    def test_unicode_pickle(self):
        # A tree containing Unicode characters can be pickled.
        html = "<b>\N{SNOWMAN}</b>"
        soup = self.soup(html)
        dumped = pickle.dumps(soup, pickle.HIGHEST_PROTOCOL)
        loaded = pickle.loads(dumped)
        assert loaded.decode() == soup.decode()

    def test_copy_navigablestring_is_not_attached_to_tree(self):
        html = "<b>Foo<a></a></b><b>Bar</b>"
        soup = self.soup(html)
        s1 = soup.find(string="Foo")
        s2 = copy.copy(s1)
        assert s1 == s2
        assert None == s2.parent
        assert None == s2.next_element
        assert None != s1.next_sibling
        assert None == s2.next_sibling
        assert None == s2.previous_element

    def test_copy_navigablestring_subclass_has_same_type(self):
        html = "<b><!--Foo--></b>"
        soup = self.soup(html)
        s1 = soup.string
        s2 = copy.copy(s1)
        assert s1 == s2
        assert isinstance(s2, Comment)

    def test_copy_entire_soup(self):
        html = "<div><b>Foo<a></a></b><b>Bar</b></div>end"
        soup = self.soup(html)
        soup_copy = copy.copy(soup)
        assert soup == soup_copy

    def test_copy_tag_copies_contents(self):
        html = "<div><b>Foo<a></a></b><b>Bar</b></div>end"
        soup = self.soup(html)
        div = soup.div
        div_copy = copy.copy(div)

        # The two tags look the same, and evaluate to equal.
        assert str(div) == str(div_copy)
        assert div == div_copy

        # But they're not the same object.
        assert div is not div_copy

        # And they don't have the same relation to the parse tree. The
        # copy is not associated with a parse tree at all.
        assert None == div_copy.parent
        assert None == div_copy.previous_element
        assert None == div_copy.find(string='Bar').next_element
        assert None != div.find(string='Bar').next_element

