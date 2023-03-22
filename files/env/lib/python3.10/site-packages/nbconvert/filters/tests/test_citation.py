# -----------------------------------------------------------------------------
# Copyright (c) 2013, the IPython Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# -----------------------------------------------------------------------------

import pytest

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
from ..citation import citation2latex

# -----------------------------------------------------------------------------
# Tests
# -----------------------------------------------------------------------------
test_md = {
    """
# My Heading

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus ac magna non augue
porttitor scelerisque ac id diam <cite data-cite="granger">Granger</cite>. Mauris elit
velit, lobortis sed interdum at, vestibulum vitae libero <strong data-cite="fperez">Perez</strong>.
Lorem ipsum dolor sit amet, consectetur adipiscing elit
<em data-cite="takluyver">Thomas</em>. Quisque iaculis ligula ut ipsum mattis viverra.

<p>Here is a plain paragraph that should be unaffected. It contains simple
relations like 1<2 & 4>5.</p>

* One <cite data-cite="jdfreder">Jonathan</cite>.
* Two <cite data-cite="carreau">Matthias</cite>.
* Three <cite data-cite="ivanov">Paul</cite>.
""": r"""
# My Heading

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus ac magna non augue
porttitor scelerisque ac id diam \cite{granger}. Mauris elit
velit, lobortis sed interdum at, vestibulum vitae libero \cite{fperez}.
Lorem ipsum dolor sit amet, consectetur adipiscing elit
\cite{takluyver}. Quisque iaculis ligula ut ipsum mattis viverra.

<p>Here is a plain paragraph that should be unaffected. It contains simple
relations like 1<2 & 4>5.</p>

* One \cite{jdfreder}.
* Two \cite{carreau}.
* Three \cite{ivanov}.
""",
    # No citations
    r"""The quick brown fox jumps over the lazy dog.""": r"""The quick brown fox jumps over the lazy dog.""",
    # Simple inline
    r"""Foo <cite data-cite=asdf>Text</cite> bar""": r"""Foo \cite{asdf} bar""",
    # Multiline
    r"""<cite data-cite=ewqr>Text
</cite>Foo""": r"""\cite{ewqr}Foo""",
    # Nested tags
    r"""<div><div data-cite=Foo><div>Text</div></div></div> Bar""": r"""<div>\cite{Foo}</div> Bar""",
    # Including Maths
    r"""Foo $3*2*1$ <div data-cite=Foo>Text</div> Bar""": r"""Foo $3*2*1$ \cite{Foo} Bar""",
    # Missing end tag
    r"""<cite data-cite=asdf>Test Foo""": r"""\cite{asdf}""",
    r"""<cite data-cite=asdf><cite>Test Foo""": r"""\cite{asdf}""",
    r"""<cite data-cite=asdf><cite>Test</cite> Foo""": r"""\cite{asdf}""",
    # Multiple arguments
    r"""<cite width=qwer data-cite=asdf>Test</cite> Foo""": r"""\cite{asdf} Foo""",
    # Wrong capitalization
    r"""<CITE data-cite=asdf>Test</cite> Foo""": r"""\cite{asdf} Foo""",
    r"""<cite DATA-CITE=asdf>Test</cite> Foo""": r"""\cite{asdf} Foo""",
    # Wrong end tag
    r"""<asd data-cite=wer> ksjfs </asdf> sdf ds """: r"""\cite{wer}""",
    r"""<asd data-cite=wer>""": r"""\cite{wer}""",
    # Invalid tag names
    r"""<frog> <foo data-cite=wer></foo>""": r"""<frog> \cite{wer}""",
    # Non-nested tags
    r"""<strong> <h1> <cite data-cite=asdf></cite>Test</strong> Foo </h1>""": r"""<strong> <h1> \cite{asdf}Test</strong> Foo </h1>""",
    # LXML errors
    r"""Foo
\begin{eqnarray}
1 & <cite data-cite=bar>bar1</cite> \\
3 & 4 \\
\end{eqnarray}""": r"""Foo
\begin{eqnarray}
1 & \cite{bar} \\
3 & 4 \\
\end{eqnarray}""",
    r"""
1<2 is true, but 3>4 is false.

$1<2$ is true, but $3>4$ is false.

1<2 it is even worse if it is alone in a line.""": r"""
1<2 is true, but 3>4 is false.

$1<2$ is true, but $3>4$ is false.

1<2 it is even worse if it is alone in a line.""",
    r"""
1 < 2 is true, but 3 > 4 is false

$1 < 2$ is true, but $3 > 4$ is false

1 < 2 it is even worse if it is alone in a line.
""": r"""
1 < 2 is true, but 3 > 4 is false

$1 < 2$ is true, but $3 > 4$ is false

1 < 2 it is even worse if it is alone in a line.
""",
}


@pytest.mark.parametrize(
    ["in_arg", "out_arg"], [(in_arg, out_arg) for (in_arg, out_arg) in test_md.items()]
)
def test_citation2latex(in_arg, out_arg):
    """Are citations parsed properly?"""
    assert citation2latex(in_arg) == out_arg
