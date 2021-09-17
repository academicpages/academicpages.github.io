\ProvidesClass{clean_cv}[2021/07/28 v1.0.0 'CleanCV' Class]

\LoadClass[11pt]{article}

\RequirePackage[margin=0.5in]{geometry} % half-inch margins
\RequirePackage{microtype}
\RequirePackage{fancyhdr}
\RequirePackage{titlesec}
\RequirePackage{array}
\RequirePackage{xcolor}
\RequirePackage{xpatch}
\RequirePackage{enumitem}

% Load fonts
\RequirePackage[fixed]{fontawesome5}
\RequirePackage[scaled=.96,osf]{XCharter}
\linespread{1.04}

% Load biber
\RequirePackage[backend=biber,sorting=ydnt,block=none,bibstyle=nature,doi=false,isbn=false,url=false]{biblatex}

\RequirePackage[hidelinks]{hyperref}

\DeclareSourcemap{
    \maps[datatype=bibtex]{
        \map[overwrite]{
            \step[fieldsource=date, match=\regexp{(\d{4})},
                  fieldset=keywords, fieldvalue={YEAR-$1}, append, ]
	}
	\map[overwrite]{
	    \step[fieldset=note, null]
	}
}}

\AtBeginBibliography{\vspace*{-2em}}

%-----------------------------------------------------
% Bold one author's name
% https://tex.stackexchange.com/a/73246, CC-BY-SA 3.0
\def\makenamesetup{%
  \def\bibnamedelima{ }%
  \def\bibnamedelimb{ }%
  \def\bibnamedelimc{ }%
  \def\bibnamedelimd{ }%
  \def\bibnamedelimi{ }%
  \def\bibinitperiod{.}%
  \def\bibinitdelim{ }%
  \def\bibinithyphendelim{.-}}    
\newcommand*{\makename}[3]{\begingroup\makenamesetup\xdef#1{#2, #3}\endgroup}

\newbibmacro*{name:bold}[2]{%
  \makename{\currname}{#1}{#2}%
  \makename{\findname}{\lastname}{\firstname}%
  \makename{\findinit}{\lastname}{\firstinit}%
  \ifboolexpr{ test {\ifdefequal{\currname}{\findname}}
            or test {\ifdefequal{\currname}{\findinit}} }{\bfseries}{}}

\newcommand*{\highlightauthorname}[3]{%
  \def\lastname{#3}%
  \def\firstname{#1}%
  \def\firstinit{#2}}

\xpretobibmacro{name:family}{\begingroup\usebibmacro{name:bold}{#1}{#2}}{}{}
\xpretobibmacro{name:given-family}{\begingroup\usebibmacro{name:bold}{#1}{#2}}{}{}
\xpretobibmacro{name:family-given}{\begingroup\usebibmacro{name:bold}{#1}{#2}}{}{}
\xpretobibmacro{name:delim}{\begingroup\normalfont}{}{}

\xapptobibmacro{name:family}{\endgroup}{}{}
\xapptobibmacro{name:given-family}{\endgroup}{}{}
\xapptobibmacro{name:family-given}{\endgroup}{}{}
\xapptobibmacro{name:delim}{\endgroup}{}{}
%------------------------------------------------------
\newcommand{\printbibyear}[1]{\printbibliography[heading=none,keyword=YEAR-#1]\vspace*{-2.5em}\,}
\newcommand{\printallbib}{\printbibliography[heading=none]\vspace*{-2.5em}\,}


\definecolor{dateline}{gray}{0.5}
\definecolor{datecolor}{gray}{0.4}
\newcolumntype{R}{>{\raggedleft\arraybackslash}p{4em}}
\newcommand{\daterule}{\color{dateline}\vrule width 1pt}
\newcommand{\dateentry}[2]{{\leavevmode\color{datecolor}{#1}} & #2 \\ \noalign{\medskip}}
%\dimexpr(\textwidth - #1)\relax
\newenvironment{datetabular}[1]{%
    \begin{tabular}{@{}>{\raggedleft\arraybackslash}p{#1}!{\daterule}p{\dimexpr(\linewidth - #1 - 1em)\relax}}%
}{%
    \end{tabular}%
}

\newcommand{\faCenter}[1]{\raisebox{-2pt}{\faIcon{#1}}}
\newcommand{\faCenterStyle}[2]{\raisebox{-2pt}{\faIcon[#1]{#2}}}

\titleformat{\section}[display]{\large\bfseries}{}{0pt}{}[\vspace{-10pt}\rule{\linewidth}{1pt}]
\titlespacing*{\section}{0pt}{0em}{0.4em}

\setlength\parindent{0pt}
\setlength\parskip{0pt}

\setlist{noitemsep,topsep=0pt,parsep=0pt,partopsep=0pt}
\newcommand{\eatvspace}{\vspace*{-1.5em}\,}

\newcommand*{\headlineposition}[1]{\def\@headlineposition{#1}}

\let\@author\@empty
\let\@headlineposition\@empty

\renewcommand{\maketitle}{%
\begin{center}
    \ifx\@author\@empty\else{ \Huge \@author} \\\fi \ifx\@headlineposition\@empty\else\vspace{4pt} {\itshape \@headlineposition}\fi
\end{center}%
\vspace{-17.2pt}
\rule{\linewidth}{1pt}
}

\pagestyle{empty}
