% Les Clowney 
% ru-thesis document style (LaTeX)
%  ruthesis.cls is based on the LaTeX documentstyle ruthesis.sty, to which
%  both Dave Steiner and Tara Madhyastha contributed.

%  4/9/94 Modified for LaTeX2e [lsc]
%  11/18/94 [lsc] Removed uses of the \initials command. Use of initials,
%     e.g., Ph.D. is not acceptable until after the degree is awarded.
%  3/22/95  [lsc/dks] Changed the way the default 11pt gets setup.
%
%     This style  reflects the requirements set forth by the Graduate
%     School of Rutgers, The State  University. The style is initially defined
%     by the LaTex report style at 11 point.

% Class description
\NeedsTeXFormat{LaTeX2e}
\def\fileversion{1.2}
\def\filedate{3/22/95}
\ProvidesClass{ruthesis}[\filedate\space v\fileversion\space
			 Standard LaTeX2e document class]
% this style is really a driver for the report style, so pass all
% options through.
\newcommand\@pointsize{11pt}
\DeclareOption{10pt}{\renewcommand\@pointsize{10pt}}
\DeclareOption{11pt}{\renewcommand\@pointsize{11pt}}
\DeclareOption{12pt}{\renewcommand\@pointsize{12pt}}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{report}}
\ProcessOptions
\LoadClass[\@pointsize]{report}

% ***********************************************************************
% Sumary of New Commands (many are not to be used outside of the style file)
%
%       The flollowing are primarily for the titlepage et al....
%       \draft     (this invokes the macro  \draftrue, modifies title page)
%       \copyrightpage     (make a copyright page)
%       \figurespage     (make a page for list of figures)
%       \tablespage     (make a page for list of tables)
%       \title{thesis title} (this is defined by the report style)
%       \author{author's name}(this is defined by the report style)
%       \pagestyletopright. Place page numbers at topright corner.
%       \phd    (if invoked then \phdtrue is set.
%                The default is  not to be getting one. The command
%                \degree may be ignored if this command is 
%                used. The default is for the Master of Science.)
%       \degree{type of degree, e.g. Master of Science}
%               The default is Master of Science (or Doctor of Philosophy if
%                \phd is used.) 
%       **** joint  Degrees ****
%               The joint degree is always(?) offered in conjunction
%               with The University of Medicine and Dentistry of New
%               Jersey. Thus for a joint degree \jointumdnj will
%               probably always be used.                
%       \jointumdnj (Invokes the command \joint with the proper argument
%               for the University of Medicine of and Dentistry.)
%       \joint{argument}
%               (The degree is offered jointly with... . The command
%                \joint invokes the macro \jointtrue and gdefs @jointwith
%                to be the value of argument.
%                The command \jointumdnj will invoke joint.)
%       \abstract{the body of the abstract}
%       \acknowledgements{the body of the acknowledgements}
%       \dedication{the body of the dedication}
%       \director{the principal advisor's name}
%       \submissionyear{year of submission to the Graduate School}
%       \submissionmonth{month of submission to the Graduate School}
%               (The default dates used will be those at which the
%                document was prepared)
%      \begin-end{vita}  (begin single spacing after this point for the vita)
%       ******* Booleans ******* 
%       \ifpagestyletopright (invoke \pagestyle{topright})
%       \ifdraft  (Will do some things differently if draft. Set by \draft)
%       \ifcopyright (Add a copyright notice? (Set by \copyrightpage)
%       \ifabstract (set if command \abstract invoked)
%       \ifpreface (set if command \preface invoked)
%       \ifacknowledgements (set by \acknowledgements)
%       \ifabstract (set by \abstract)
%       \ifjoint (set by  \joint)
%       \iffigures
%       \iftables
%       \ifafterpreface (afterpreface sections pagenumber must be at topright 
%               corner. If user has chosen a hader then it must be overridden.)
%               (Produce a List of figures? The default is to do so.)
%       \tablestrue
%               (Produce a List of tables?)
%       \begin/end{descriptionlist} (Basically a modified  \description.)
%       \fullpagefigure Creates a figure where the page is a vbox whose
%                height is \textheight. 




%          **** PAGE LAYOUT ****
% We need 1" (~72pt) margins except on the binding edge, where it is 1 1/2".
% They are a bit larger to handle lines with overfull boxes.
% 
\@twocolumnfalse
\@twosidefalse
\oddsidemargin 36bp \evensidemargin 36bp  %%% was 40 and 25 -dks
\marginparwidth 40bp \marginparsep 10bp 
\topmargin -47bp        % Default margin is  73 points-- make 1/2 that
                        % plus a bit more to get page 1/2 inch down.
\headheight 11bp        % Height of box containing running head.
\headsep 36bp           % Distance between foot of head and text.
                        % headsep + headheight + topmargin ~ 72 pt
\textheight 648bp       % Height of text (including footnotes and  %%% was 620
                        % figures, excluding running head and foot).
\textwidth 412bp        % Give 92pt right margin;72 + extra for overfull boxes.
% disappeared from LaTeX\footheight 11bp        %    Height of box containing running foot.
\footnotesep \baselineskip
\footskip 36bp          %    Distance from baseline of box containing foot 
                        %    to baseline of last line of text.
\parindent 3.5ex
\parskip 1bp plus 1bp 
\setcounter{tocdepth}{3} % Put subsubsections in toc (set to 2 in
                         % report.sty). [lsc] 
\skip\footins 15pt plus3pt minus3pt % Add space between text and
                                    % footnotes.

% *******  Documentstyle Modifications *******
\brokenpenalty=10000 % Do not break pages at hyphens.
\def\baselinestretch{1.6}  % 1.6 space document ~ doublespace.
\@addtoreset{equation}{chapter} % Set things up so that theequation, 
        % thefigure, and thetable counters are reset by incrementing 
        % thechaphter. (The others are correct in the report style.)


% **** Make changes to the formats of table of contents and sectioning ****
% **** commands . 
%  Center chapter headings, add the string ``chapter #'', and reduce the
%  font size that is used in the report style. Must  modify fonts used for 
% other sectioning commands also.
\newcommand\chapter@topskip{\null\vskip40bp} % Chapters sink this much before
                                      % output.
\newcommand\chapter@bottomskip{\vskip30bp} % Chapters sink this much
                                         % after output. 
\def\@makechapterhead#1{\chapter@topskip { \parindent 0pt \centering
 \ifnum \c@secnumdepth >\m@ne {\Large \bf \@chapapp{} \thechapter} 
   \par  
   \vskip7bp 
 \fi 
 {\Large \bf #1}\par 
 \nobreak \chapter@bottomskip }}

% Chapter with only a string heading--as in unnumberedsections.
\renewcommand{\@makeschapterhead}[1]{\chapter@topskip{ \parindent 0pt \centering
{\Large\bfseries#1}\par 
 \nobreak \chapter@bottomskip } }
\renewcommand\chapter{\clearpage\global\@topnum\z@
 \@afterindentfalse \secdef\@chapter\@schapter} 
\def\@chapter[#1]#2{\ifnum \c@secnumdepth >\m@ne
 \refstepcounter{chapter}
 \typeout{\@chapapp\space\thechapter.}
 \addcontentsline{toc}{chapter}{\protect
 \numberline{\thechapter}#1} \else 
 \addcontentsline{toc}{chapter}{#1}\fi
 \chaptermark{#1}
 % Don't add extra space to lists of figures and tables after chapters.
 %  \addtocontents{lof}{\protect\addvspace{10bp}}
 %  \addtocontents{lot}{\protect\addvspace{10bp}}
 \if@twocolumn
 \@topnewpage[\@makechapterhead{#2}] 
 \else \@makechapterhead{#2}
 \@afterheading \fi} 
\renewcommand{\@schapter}[1]{\if@twocolumn \@topnewpage[\@makeschapterhead{#1}]
 \else \@makeschapterhead{#1} 
 \@afterheading\fi}


% use Table of Contents rather than default of Contents
\def\tableofcontents{\@restonecolfalse\if@twocolumn\@restonecoltrue\onecolumn
 \fi\chapter*{Table of Contents\@mkboth{TABLE OF CONTENTS}{TABLE OF CONTENTS}}
 \@starttoc{toc}\if@restonecol\twocolumn\fi}


% Add period after section numbers in table of contents.
\def\numberline#1{\advance\hangindent\@tempdima \hbox to\@tempdima{#1.\hfil}}

\newcommand{\l@unnumberedsection}[2]{\pagebreak[3]% \vskip 1em plus 1bp
\parindent \z@ \rightskip \@pnumwidth 
 \parfillskip -\@pnumwidth 
\interlinepenalty\@M\leavevmode 
\@tempdima 1.5em\relax \begingroup \bfseries
    #1\leaders\hbox{$\m@th \mkern \@dotsep mu.\mkern \@dotsep mu$}% \hfill 
\hskip 0pt plus 1filll % new line
   \hbox to\@pnumwidth{\hfil\rm #2}\endgroup\par}

% Add dotted leaders for chapters in the table of contents.
\renewcommand{\l@chapter}[2]{\pagebreak[3]\vskip 1em plus 1bp
\parindent \z@ \rightskip \@pnumwidth 
 \parfillskip -\@pnumwidth 
\interlinepenalty\@M\leavevmode 
\@tempdima 1.5em\relax \begingroup 
    \textbf{#1}\leaders\hbox{$\m@th \mkern \@dotsep mu.\mkern \@dotsep mu$}% \hfill 
\hskip 0pt plus 1filll % new line
   \hbox to\@pnumwidth{\hfil\rm #2}\endgroup\par}



\def\section{\@startsection {section}{1}{\z@}{-3.5ex plus -1ex minus 
 -.2ex}{2.3ex plus .2ex}{\large\bfseries}}
\def\subsection{\@startsection{subsection}{2}{\z@}{-3.25ex plus -1ex minus 
 -.2ex}{1.5ex plus .2ex}{\large\bfseries}}
\def\subsubsection{\@startsection{subsubsection}{3}{\z@}{-3.25ex plus
 -1ex minus -.2ex}{1.5ex plus .2ex}{\normalsize\bfseries}}
\let\paragraph=\subsubsection

% single space bibliography, quotations and verse. 

\def\thebibliography#1{\def\baselinestretch{1}\@normalsize 
\unnumberedsection{References}\list
 {[\arabic{enumi}]}{\settowidth\labelwidth{[#1]}\leftmargin\labelwidth
 \advance\leftmargin\labelsep
 \usecounter{enumi}}
 \def\newblock{\hskip .11em plus .33em minus -.07em}
 \sloppy
 \sfcode`\.=1000\relax}
% end bib with a new page
\def\endthebibliography{\endlist}

% Rutgers requires that quotations be indented at the left and 
% flush at the right margin. Center Verses.
\renewcommand\quotation{\def\baselinestretch{1}\@normalsize\list{}{%
\rightmargin -\z@ \listparindent 0.5ex
\itemindent\leftmargin\parsep 0pt}\item[]}
\let\endquotation=\endlist

\renewcommand\verse{\def\baselinestretch{1}\@normalsize\let\\=\centercr 
 \list{}{\itemsep\z@ \itemindent -1.5em\listparindent \itemindent 
 \rightmargin\leftmargin\advance\leftmargin 1.5em}\item[]}
\let\endverse=\endlist

% The pageheading style topright places numbers at top righthand corners.
% The macro \draftheading expands to show the rootfile and date
% if the \draft command has been given, otherwise it is empty.
% 8/1/88 Added \draftheading  [lsc]
\newcommand\ps@topright{\let\@mkboth\@gobbletwo
  \def\@oddhead{\rm\draftheading\hfil\thepage}\let\@evenhead\@oddhead
  \def\@evenfoot{}\def\@oddfoot{}}
% For drafts make this redefinition.


%  ***** Verbatim listing macro ****
%  Code from the TeXbook for inputting  a file and listing it 
%  verbatim in \texttt mode. Will not properly handle tabs.
%  This code hasn't been rigorously tested so it should be used cautiously.
%  Note that the left quote. "`", is redefined when the macro is finally used
%  or ` isn't properly handled.
\def\uncatcodespecials{\def\do##1{\catcode`##1=12 }\dospecials}
\newcommand{\setupverbatim}{\normalfont\ttfamily
        \def\par{\leavevmode\endgraf}\catcode`\`=\active
        \obeylines \uncatcodespecials \obeyspaces}
{	\obeyspaces\global\let =\ }


\def\verbatimfont{\ttfamily}
\def\uncatcodespecials{\def\do##1{\catcode`##1=12 }\dospecials}

\def\listing#1{%
\par\begingroup
\setupverbatim
\input{#1} \endgroup}

% \let\listing=\verbatimfile


% Single Space Figures, Tables, and Footnotes

% Redefine the macro used for floats (figures and tables)
% so that single spacing is used.
% (Note \def\figure{\@float{figure}<set single spacing>} doesn't work
%  because figure has an optional argument)
\def\@xfloat#1[#2]{\ifhmode \@bsphack\@floatpenalty -\@Mii\else
   \@floatpenalty-\@Miii\fi\def\@captype{#1}\ifinner
      \@parmoderr\@floatpenalty\z@
    \else\@next\@currbox\@freelist{\@tempcnta\csname ftype@#1\endcsname
       \multiply\@tempcnta\@xxxii\advance\@tempcnta\sixt@@n
       \@tfor \@tempa :=#2\do
                        {\if\@tempa h\advance\@tempcnta \@ne\fi
                         \if\@tempa t\advance\@tempcnta \tw@\fi
                         \if\@tempa b\advance\@tempcnta 4\relax\fi
                         \if\@tempa p\advance\@tempcnta 8\relax\fi
         }\global\count\@currbox\@tempcnta}\@fltovf\fi
    \global\setbox\@currbox\vbox\bgroup 
    \def\baselinestretch{1}\@normalsize
    \boxmaxdepth\z@
    \hsize\columnwidth \@parboxrestore}

% Single space footnotes.
\long\def\@footnotetext#1{\insert\footins{\def\baselinestretch{1}\footnotesize
    \interlinepenalty\interfootnotelinepenalty 
    \splittopskip\footnotesep
    \splitmaxdepth \dp\strutbox \floatingpenalty \@MM
    \hsize\columnwidth \@parboxrestore
   \edef\@currentlabel{\csname p@footnote\endcsname\@thefnmark}\@makefntext
    {\rule{\z@}{\footnotesep}\ignorespaces
      #1\strut}}}


% *******  User commands *******
% \if one of the following is invoked then set appropriate macros
\newcommand\draftheading{}
\newcommand\draft{\drafttrue
 \def\ps@plain{\let\@mkboth\@gobbletwo
  % redefine page styles so that appropriate headers are used.
   \def\@oddhead{\rm\draftheading\hfil\thepage}\let\@evenhead\@oddhead
   \def\@evenfoot{\hfil\thepage\hfil}\let\@oddfoot\@evenfoot}
 \def\draftheading{{\bfseries\jobname.tex\hfil\the\month/\the\day/\the\year}}}
\newcommand\copyrightpage{\copyrighttrue}
\newcommand\figurespage{\figurestrue}
\newcommand\tablespage{\tablestrue}
\newcommand\phd{\phdtrue\def\@degree{Doctor of Philosophy}}
\long\def\abstract#1{\abstracttrue\gdef\@abstract{#1}}
\long\def\preface#1{\prefacetrue\gdef\@preface{#1}}
\long\def\acknowledgements#1{\acknowledgementstrue\gdef\@acknowledgements{#1}}
\long\def\dedication#1{\dedicationtrue\gdef\@dedication{#1}}
\newcommand{\abbreviations}[1]{\abbreviationspagetrue\gdef\@abbreviations{#1}}
% Use of the \initials command is being stopped but keep the macro for old 
% files.
\newcommand{\initials}[1]{\gdef\@initials{#1}} % Ph.D. et al.
\newcommand{\degree}[1]{\phdfalse\gdef\@degree{#1}} % Master of Science et al.
\newcommand{\program}[1]{\gdef\@program{#1}}
\newcommand{\campus}[1]{\gdef\@campus{#1}}
\newcommand{\jointumdnj}{\joint{The Graduate School of Biomedical Sciences\\
         the University of Medicine and  Dentistry of New Jersey\\}}
\newcommand{\joint}[1]{\jointtrue\long\gdef\@jointwith{#1}} % if joint program
                                                  % then who with?      
\newcommand{\director}[1]{\gdef\@director{#1}}   
\newcommand{\approvals}[1]{\gdef\@approvals{#1}}
\newcommand{\submissionmonth}[1]{\gdef\@month{#1}}
\newcommand{\submissionyear}[1]{\gdef\@year{#1}}

%   ******** set defaults *******
\newcommand\@initials{M.S.}
\newcommand\@degree{Master of Science}
\newcommand\@campus{New Brunswick}
\renewcommand\@title{}\renewcommand\@author{\ }\newcommand\@program{}
\newcommand\@director{}
\edef\@month{\ifcase\the\month\or
  January\or February\or March\or April\or May\or June\or
  July\or August\or September\or October\or November\or December\fi}
\edef\@year{\number\the\year}

%    ******* conditionals  *******
\newif\ifdraft
\newif\ifafterpreface
\newif\ifcopyright \newif\iffigures\newif\iftables
\newif\ifabstract   \newif\ifpreface \newif\ifacknowledgements 
\newif\ifdedication \newif\ifabbreviationspage
\newif\ifjoint \newif\ifphd \newif\ifpagestyletopright

%    ******* conditional defaults ******* 
\draftfalse
\afterprefacefalse
\pagestyletoprighttrue
\abstractfalse
\prefacefalse
\dedicationfalse
\jointfalse
\phdfalse % default is not for PhD (currently is  Master of Science) 
\copyrightfalse  
\abbreviationspagefalse 

\newcommand\titlep{\vbox to \textheight{%
        \parskip0pt 
        \parindent0pt
        \typeout{Title}
        \null\nobreak\vskip 10bp 
        {\def\baselinestretch{1}\@normalsize
          \centering\Large\bfseries\uppercase\expandafter{\@title}\par\nobreak
         }
        \vskip 2ex plus 2ex minus 2ex 
        {\centering\bfseries
          BY \uppercase\expandafter{\@author}\par
          \nobreak
          \vskip 4ex plus 2ex minus 2ex 
          \ifdraft%
            {DRAFT VERSION CREATED ON \uppercase\expandafter{\today}\\}
          \else %
             A \ifphd{dissertation}\else{thesis}\fi\ submitted to the\\
             Graduate School---\@campus \\
             Rutgers, The State University of New Jersey\\
             \ifjoint{in conjunction with\\ \obeylines\@jointwith\par}\fi
             \ifjoint{in partial fulfillment of the requirements 
                for the\\ Joint Degree of}
                \else %
                  in partial fulfillment of the requirements \\
                  for the degree of\\ 
             \fi 
             \@degree\\
             Graduate Program in \@program\\
             \vskip 1ex
             Written under the direction of\\
             \@director\\
             and approved by\\ 
             \vskip 2ex plus 1ex minus 2ex

             \newcount\@aplines
             \@aplines=\@approvals
             \loop {} \ifnum\@aplines>0
                \advance\@aplines by-1
                \vskip 5bp
                % should really just copy to a box and reuse that...do later
                \hbox to\hsize{\hss\vrule width 200bp height 0.4bp\hss}
                \nobreak
             \repeat

        \vfil
        \@campus, New Jersey\\
        \@month, \@year\\
   \fi %   close ifdraft
   }}\newpage} % end titlep

\newcommand\copyrightp{%
        \null\vfil
        \typeout{Copyright}
        {\centering\bfseries
                \large\copyright\ \@year\\
                \@author\\
                \large ALL RIGHTS RESERVED\par}
        \vfil\newpage}

\newcommand{\desclabel}[1]{{\textbf{#1}\hfill}}
\def\descriptionlist#1{\list{}
         {\settowidth\labelwidth{#1}\leftmargin\labelwidth
         \let\makelabel\desclabel}}
\let\enddescriptionlist=\endlist

\newcommand\beforepreface{%
        \pagenumbering{roman}
        \pagestyle{empty}
        \titlep
        \ifcopyright\copyrightp\fi  
        \c@page2 % set page counter so that next is 2
        \pagestyle{plain}
        \ifabstract{%
                \typeout{Abstract}
                \addcontentsline{toc}{unnumberedsection}{Abstract}
                \null\vskip10bp
                \begin{center}
                {\large\bfseries
                ABSTRACT OF THE \ifphd DISSERTATION\else THESIS\fi
                \vskip72bp
                \Large\bfseries\expandafter{\@title} \large
                \vskip30bp
                by \@author\\
                \ifphd Dissertation\else Thesis\fi\ Director: \@director
                \vskip 31bp}
                \end{center}
                \@abstract}
        \fi }

\newcommand{\unnumberedsection}[1]{\chapter*{#1}
        \addcontentsline{toc}{unnumberedsection}{#1}\typeout{#1}}

%need to call addcontentsline before @starttoc. -dks
\renewcommand\listoffigures{\@restonecolfalse\if@twocolumn\@restonecoltrue\onecolumn
 \fi\chapter*{List of Figures\@mkboth
 {LIST OF FIGURES}{LIST OF FIGURES}}
 \addcontentsline{toc}{chapter}{List of Figures}
 \@starttoc{lof}\if@restonecol\twocolumn\fi}
\renewcommand\listoftables{\@restonecolfalse\if@twocolumn\@restonecoltrue\onecolumn
 \fi\chapter*{List of Tables\@mkboth
 {LIST OF TABLES}{LIST OF TABLES}}
 \addcontentsline{toc}{chapter}{List of Tables}
 \@starttoc{lot}\if@restonecol\twocolumn\fi}


\newcommand\afterpreface{%
%  Insert all of the text between the title (and copyright) pages and the main 
%  body of the thesis.
        \ifpreface{\unnumberedsection{Preface}
                \@preface}
        \fi   
        \ifacknowledgements%
                \unnumberedsection{Acknowledgements}
                \@acknowledgements 
        \fi
        \ifdedication%
                \unnumberedsection{Dedication}
                \@dedication
        \fi 

        \tableofcontents
        \iftables%
                \addvspace{10bp}
                \let\saveaddvspace=\addvspace
                \def\addvspace##1{}
                \listoftables
                \let\addvspace=\saveaddvspace
        \fi
        \iffigures%
                \addvspace{10bp}
                \let\saveaddvspace=\addvspace
                \def\addvspace##1{}
                \listoffigures
                \let\addvspace=\saveaddvspace
        \fi
        \ifabbreviationspage{\def\baselinestretch{1}\@normalsize
                \unnumberedsection{List of Abbreviations}
                \@abbreviations}
        \fi
        \newpage
        \afterprefacetrue
        \c@page0 % set page counter so that next is 1
        \pagenumbering{arabic}
        \pagestyle{topright}
        }
\newenvironment{vita}%
{\unnumberedsection{Vita}
 \bgroup\def\baselinestretch{1}\@normalsize}
{\egroup}

% Fullpage floats:
\newenvironment{fullpagefigure}%
{\@float{figure}[p]\vbox to \textheight \bgroup}
{\egroup\end@float}

\newenvironment{fullpagetable}
{\@float{table}[p]\vbox to \textheight \bgroup}
{\egroup\end@float}

% Redefine appendix to print Appendix []. ... page # in table of contents.
\newcommand{\appnumberline}[1]{\advance\hangindent\@tempdima \hbox{Appendix #1. }}
\renewcommand\appendix{\par
 \setcounter{chapter}{0}
 \setcounter{section}{0}
 \renewcommand\@chapapp{Appendix}
 \renewcommand\thechapter{\Alph{chapter}}
% Redefine @chapter  so that appnumberline (ratherline) is used.
 \def\@chapter[##1]##2{\ifnum \c@secnumdepth >\m@ne
  \refstepcounter{chapter}
  \typeout{\@chapapp\space\thechapter.}
  \addcontentsline{toc}{chapter}{\protect
  \appnumberline{\thechapter}##1} \else 
  \addcontentsline{toc}{chapter}{##1}\fi
  \chaptermark{##1}
  % Don't add extra space to lists of figures and tables after chapters.
  %  \addtocontents{lof}{\protect\addvspace{10pt}}
  %  \addtocontents{lot}{\protect\addvspace{10pt}}
  \if@twocolumn
  \@topnewpage[\@makechapterhead{##2}] 
  \else \@makechapterhead{##2}
  \@afterheading \fi}}
%
\newcommand\tempheading{\@startsection{donothing}{donothing}{\z@}{-3.25ex plus
 -1ex minus -.2ex}{1.5ex plus .2ex}{\centering\large\bfseries}}
\newcommand\heading{\tempheading*}
\newcommand\subheading{\subsection*}


