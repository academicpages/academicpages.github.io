# Changelog

## 2023.3.11 (1 March 2023) PreRelease

Notable changes:

-   Bug fix: incomplete movement expression while Refactor -> Move symbol to [pylance-release#4018](https://github.com/microsoft/pylance-release/issues/4018)
-   Bug fix: Keywords force completions to stop [pylance-release#3968](https://github.com/microsoft/pylance-release/issues/3968)
-   Bug fix: quick fix places # type: ignore on wrong line. [pylance-release#3959](https://github.com/microsoft/pylance-release/issues/3959)
-   Bug fix: Accepting refactor "type: ignore" puts newline in wrong spot [pylance-release#3858](https://github.com/microsoft/pylance-release/issues/3858)
-   Bug fix: Inline docstrings for attributes don't show up unless docstring is on very next line [pylance-release#3769](https://github.com/microsoft/pylance-release/issues/3769)

Pylance's copy of Pyright has been updated from 1.1.295 to 1.1.296.

-   See Pyright's release notes for details: [1.1.296](https://github.com/microsoft/pyright/releases/tag/1.1.296).

-   Unreleased in Pyright, but included in Pylance:
    -   Bug fix: Fixed a bug that caused the variance for type parameters to be incorrectly inferred when an auto-variance class derived from a non-auto-variance class. This addresses [#4713](https://github.com/microsoft/pyright/issues/4713).
    -   Enhancement: Performance optimization: reduced formatting of error messages in cases where it can be determined that they are not needed (e.g. in speculative evaluation code paths).
    -   Enhancement: Declare workspaceFolders support in server capabilities (https://github.com/microsoft/pyright/pull/4666)
    -   Bug fix: Added logic to detect when a type alias is used in a generic class declaration's base class list and a type parameter used with the type alias is incompatible with the variance required for the type alias. This addresses [#4699](https://github.com/microsoft/pyright/issues/4699).
    -   Bug fix: Implemented missing check for generic type alias specialization when too few type arguments are provided. This addresses [#4709](https://github.com/microsoft/pyright/issues/4709).
    -   Bug fix: Fixed a recent regression that resulted in an incorrect type evaluation when using a `__new__` method whose return type annotation is `Self`. This addresses [#4705](https://github.com/microsoft/pyright/issues/4705).
    -   Bug fix: Fixed a bug that led to a false positive error when using the | operator with two dicts whose keys or values are defined as literals. This addresses part of [#4707](https://github.com/microsoft/pyright/issues/4707).

## 2023.3.10 (1 March 2023) Release

Notable changes:

-   Release version that includes changes through version [2023.2.43](https://github.com/microsoft/pylance-release/blob/main/CHANGELOG.md#2023243-24-february-2023-prerelease) prerelease build.

## 2023.2.43 (24 February 2023) PreRelease

Notable changes:

-   Bug fix: Issues when moving symbol to a different file [pylance-release#4002](https://github.com/microsoft/pylance-release/issues/4002)
-   Bug fix: Unexpected indent when pressing Enter at start of dedented line [pylance-release#3974](https://github.com/microsoft/pylance-release/issues/3974)

## 2023.2.42 (23 February 2023) PreRelease

Notable changes:

-   Rollback changes for [pylance-release#4001](https://github.com/microsoft/pylance-release/discussions/4001). Fix broke imports of stubs.

## 2023.2.41 (22 February 2023) PreRelease

Notable changes:

-   Bug fix: Pytest fixtures that yield should show the yielded result [pylance-release#3973](https://github.com/microsoft/pylance-release/issues/3973)
-   Bug fix: Missing syntax highlighting for multi variable declaration [pylance-release#3904](https://github.com/microsoft/pylance-release/issues/3904)
-   Bug fix: Source directory hiding build directory in analysis and autocomplete [pylance-release#3429](https://github.com/microsoft/pylance-release/issues/3429)
-   Enhancement: Updated pandas stubs.
-   Enhancement: Updated typeshed.

Pylance's copy of Pyright has been updated from 1.1.294 to 1.1.295.

-   See Pyright's release notes for details: [1.1.295](https://github.com/microsoft/pyright/releases/tag/1.1.295).

## 2023.2.40 (22 February 2023) Release

Notable changes:

-   Release version that includes changes through version [2022.2.31](https://github.com/microsoft/pylance-release/blob/main/CHANGELOG.md#2023231-15-february-2023-prerelease) prerelease build.

## 2023.2.31 (15 February 2023) PreRelease

Notable changes:

-   Enhancement: Make "Fields without default values cannot appear after fields with default values" a toggle-able diagnostic rule [pylance-release#3939](https://github.com/microsoft/pylance-release/issues/3939)
-   Bug fix: New partial typeshed tensorflow stubs break pylance for tensorflow [pylance-release#3937](https://github.com/microsoft/pylance-release/issues/3937)
-   Bug fix: Pandas Dataframe.explode function parameter TypeError [pylance-release#3871](https://github.com/microsoft/pylance-release/issues/3871)
-   Bug fix: Named parameter supports for PEP 692 [pylance-release#3868](https://github.com/microsoft/pylance-release/issues/3868)

Pylance's copy of Pyright has been updated from 1.1.293 to 1.1.294.

-   See Pyright's release notes for details: [1.1.294](https://github.com/microsoft/pyright/releases/tag/1.1.294).

## 2023.2.30 (15 February 2023) Release

Notable changes:

-   Release version that includes changes through version [2022.2.21](https://github.com/microsoft/pylance-release/blob/main/CHANGELOG.md#2023221-8-february-2023-prerelease) prerelease build.

## 2023.2.21 (8 February 2023) PreRelease

Notable changes:

-   Bug fix: Empty kw only dataclass has incorrect type hint for `__init__` signature [pylance-release#3916](https://github.com/microsoft/pylance-release/issues/3916)
-   Bug fix: Docstring of @property is not rendered correctly [pylance-release#3888](https://github.com/microsoft/pylance-release/issues/3888)

Pylance's copy of Pyright has been updated from 1.1.292 to 1.1.293.

-   See Pyright's release notes for details: [1.1.293](https://github.com/microsoft/pyright/releases/tag/1.1.293).

## 2023.2.20 (8 February 2023) Release

Notable changes:

-   Release version that includes changes through version [2022.2.13](https://github.com/microsoft/pylance-release/blob/main/CHANGELOG.md#2023213-6-february-2023-prerelease) prerelease build.

## 2023.2.13 (6 February 2023) PreRelease

Notable changes:

-   Bug fix: Crash with multi-root workspace (pre-release) [pylance-release#3907](https://github.com/microsoft/pylance-release/issues/3907)

## 2023.2.12 (2 February 2023) PreRelease

Notable changes:

-   Bug fix: Performance regression with 2023.2.11 Pre-Release [pylance-release#3901](https://github.com/microsoft/pylance-release/issues/3901)
-   Bug fix: VS Code + Pylance does not find venv-installed modules while venv is activated [pylance-release#3881](https://github.com/microsoft/pylance-release/issues/3881)
-   Enhancement: Pylance does not provide source actions for removing unused imports or sorting imports inside Jupyter Notebooks [pylance-release#3175](https://github.com/microsoft/pylance-release/issues/3175)

## 2023.2.11 (1 February 2023) PreRelease

Notable changes:

-   Bug fix: Don't show `__future__` options in auto-import quick action [pylance-release#3882](https://github.com/microsoft/pylance-release/issues/3882)
-   Bug fix: Syntax highlighting stop working after loading certain python files [pylance-release#3886](https://github.com/microsoft/pylance-release/issues/3886)
-   Bug fix: No automatic parens with class types [pylance-release#3870](https://github.com/microsoft/pylance-release/issues/3870)
-   Enhancement: semantic highlighting of cached_property [pylance-release#3742](https://github.com/microsoft/pylance-release/issues/3742)
-   Enhancement: Improve pytest completions and goto def [pylance-release#3727](https://github.com/microsoft/pylance-release/issues/3727)
-   Bug fix: `#region` nesting doesn't recognise last `#endregion` if there's no code after it at the end of the file on a non-"root" indent level [pylance-release#3290](https://github.com/microsoft/pylance-release/issues/3290)
-   Bug fix: Commented code at the end of a method doesn't collapse with method [pylance-release#2321](https://github.com/microsoft/pylance-release/issues/2321)

Pylance's copy of Pyright has been updated from 1.1.291 to 1.1.292.

-   See Pyright's release notes for details: [1.1.292](https://github.com/microsoft/pyright/releases/tag/1.1.292).

-   Unreleased in Pyright, but included in Pylance:
    -   Bug Fix: Fixed a few typos in the pyright documentation.
    -   Bug Fix: Fixed a bug that resulted in incorrect type evaluation when accessing instance methods directly from a `None` instance
    -   Bug Fix: Fixed a regression that resulted in a crash when resolving overloads with different numbers of parameters and with with arguments that evaluate to `Any`

## 2023.2.10 (1 February 2023) Release

-   Release version that rolls up changes from the [2022.1.41](https://github.com/microsoft/pylance-release/blob/main/CHANGELOG.md#2023141-25-january-2023-prerelease) prerelease build.

## 2023.1.41 (25 January 2023) PreRelease

Notable changes:

-   Bug fix: Request textDocument/foldingRange failed. [pylance-release#3847](https://github.com/microsoft/pylance-release/issues/3847)
-   Bug fix: Bad code insertion when typing Callable params as ellipsis [pylance-release#3841](https://github.com/microsoft/pylance-release/issues/3841)
-   Enhancement: Add more fine-grained code action kinds for `refactor.extract` [pylance-release#3803](https://github.com/microsoft/pylance-release/issues/3803)

Pylance's copy of Pyright has been updated from 1.1.290 to 1.1.291.

-   See Pyright's release notes for details: [1.1.291](https://github.com/microsoft/pyright/releases/tag/1.1.291).

## 2023.1.40 (25 January 2023) Release

-   Release version that rolls up changes from the [2022.1.31](https://github.com/microsoft/pylance-release/blob/main/CHANGELOG.md#2023131-18-january-2023-prerelease) prerelease build.

## 2023.1.31 (18 January 2023) PreRelease

Notable changes:

-   Bug fix: Overly aggressive automatic indent on deeply nested list in a `@pytest.mark.parametrize()` call [pylance-release#3839](https://github.com/microsoft/pylance-release/issues/3839)
-   Bug fix: No brackets autocompletion with python.analysis.completeFunctionParens set to true when python.languageServer is set to Pylance [pylance-release#3831](https://github.com/microsoft/pylance-release/issues/3831)
-   Bug fix: PYTHONPATH isn't expanded like how python handles it [pylance-release#3823](https://github.com/microsoft/pylance-release/issues/3823)
-   Bug fix: Django utils not found in auto import [pylance-release#3815](https://github.com/microsoft/pylance-release/issues/3815)
-   Bug fix: `extraPaths` starting with `~/` on Linux are considered relative [pylance-release#3730](https://github.com/microsoft/pylance-release/issues/3730)
-   Bug fix: Exclude map files from extension bundle [pylance-release#3647](https://github.com/microsoft/pylance-release/issues/3647)
-   Bug fix: Exclude platform specific bits from extension bundle [pylance-release#3646](https://github.com/microsoft/pylance-release/issues/3646)

Pylance's copy of Pyright has been updated from 1.1.288 to 1.1.290.

-   See Pyright's release notes for details: [1.1.289](https://github.com/microsoft/pyright/releases/tag/1.1.289), [1.1.290](https://github.com/microsoft/pyright/releases/tag/1.1.290).

-   Unreleased in Pyright, but included in Pylance:
    -   Bug Fix: Fixed a bug in the constraint solver that led to unsolved type variables in the case where a `lambda x:x` was passed to a `Callable[[T], S]`.
    -   Bug Fix: Fixed a bug that could lead to infinite type evaluation time when inferring the type of a tuple in a loop.
    -   Bug Fix: When converting a class into a callable (by combining its **new** and `__init__` methods), capture the docstring of the constructor or class. This preserves docstrings when using a class decorator.

## 2023.1.30 (18 January 2023) Release

-   Release version that rolls up changes from the [2022.1.21](https://github.com/microsoft/pylance-release/blob/main/CHANGELOG.md#2023121-11-january-2023-prerelease) prerelease build.

## 2023.1.21 (11 January 2023) PreRelease

Notable changes:

-   Bug fix: (Python) "Find All References" on any `__init__` shows every constructor for every class [pylance-release#3802](https://github.com/microsoft/pylance-release/issues/3802)
-   Bug fix: Auto-indent behavior as before / jumping to beginning of line [pylance-release#3781](https://github.com/microsoft/pylance-release/issues/3781)
-   Bug fix: No import suggestions for multi-root workspace with editable installs [pylance-release#3732](https://github.com/microsoft/pylance-release/issues/3732)

Pylance's copy of Pyright has been updated from 1.1.287 to 1.1.288.

-   See Pyright's release notes for details: [1.1.288](https://github.com/microsoft/pyright/releases/tag/1.1.288).

## 2023.1.20 (11 January 2023) Release

-   Release version that rolls up changes from the [2022.1.11](https://github.com/microsoft/pylance-release/blob/main/CHANGELOG.md#2023111-4-january-2023-prerelease) prerelease build.

## 2023.1.11 (4 January 2023) PreRelease

Notable changes:

-   Bug fix: Any comment that contains the word "region" triggers an error "#region is missing corresponding #endregion" [pylance-release#3765](https://github.com/microsoft/pylance-release/issues/3765)
-   Bug fix: Pyright parser causes tests failures [pylance-release#3761](https://github.com/microsoft/pylance-release/issues/3761)
-   Bug fix: Provide doc string for module in "import statement" completion [pylance-release#3721](https://github.com/microsoft/pylance-release/issues/3721)
-   Bug fix: Python intellisense is very slow [pylance-release#3668](https://github.com/microsoft/pylance-release/issues/3668)
-   Bug fix: option to exclude some auto-import options [pylance-release#3466](https://github.com/microsoft/pylance-release/issues/3466)

Pylance's copy of Pyright has been updated from 1.1.283 to 1.1.287.

-   See Pyright's release notes for details: [1.1.287](https://github.com/microsoft/pyright/releases/tag/1.1.287), [1.1.286](https://github.com/microsoft/pyright/releases/tag/1.1.286), [1.1.285](https://github.com/microsoft/pyright/releases/tag/1.1.285), [1.1.284](https://github.com/microsoft/pyright/releases/tag/1.1.284).

## 2023.1.10 (4 January 2023) Release

-   Release version that rolls up changes from the [2022.12.21](https://github.com/microsoft/pylance-release/blob/main/CHANGELOG.md#20221221-7-december-2022-prerelease) prerelease build.

## 2022.12.21 (7 December 2022) PreRelease

Notable changes:

-   Bug fix: Incorrect ShadowedImports warning on relative '.' import [pylance-release#3725](https://github.com/microsoft/pylance-release/issues/3725)
-   Bug fix: `source.unusedImports` is very slow and adds unnecessary whitespace [pylance-release#3715](https://github.com/microsoft/pylance-release/issues/3715)
-   Bug fix: Bad autocomplete when typing an open square bracket [pylance-release#3651](https://github.com/microsoft/pylance-release/issues/3651)
-   Bug fix: Module docstrings have inconsistent behaviour on hover [pylance-release#3636](https://github.com/microsoft/pylance-release/issues/3636)

## 2022.12.20 (7 December 2022) Release

-   Release version that rolls up changes from the [2022.12.11](https://github.com/microsoft/pylance-release/blob/main/CHANGELOG.md#20221211-1-december-2022-prerelease) prerelease build.

## 2022.12.11 (1 December 2022) PreRelease

Notable changes:

-   Bug fix: google.cloud namespace package imports fail as of 1.1.282 [pyright#4255](https://github.com/microsoft/pyright/issues/4255)
-   Bug fix: Option to set python.analysis.packageIndexDepths depth globally [pylance-release#3678](https://github.com/microsoft/pylance-release/issues/3678)

## 2022.11.41 (30 November 2022) PreRelease

Notable changes:

-   Enhancement: Dict Key Literal Autocompletion does not work with Attributes [pylance-release#3687](https://github.com/microsoft/pylance-release/issues/3687)
-   Bug fix: Auto-indent fails to break out of nested context [pylance-release#3686](https://github.com/microsoft/pylance-release/issues/3686)
-   Bug fix: Incorrectly Flagged child dataclass "Fields without default values cannot appear after fields with default values" [pylance-release#3676](https://github.com/microsoft/pylance-release/issues/3676)
-   Enhancement: Feature Request: Auto import should suggest all symbols in your project [pylance-release#3670](https://github.com/microsoft/pylance-release/issues/3670)
-   Bug fix: Semantic highlighting broken [pylance-release#3667](https://github.com/microsoft/pylance-release/issues/3667)
-   Enhancement: Flag indentation error without invalidating rest of file [pylance-release#3656](https://github.com/microsoft/pylance-release/issues/3656)
-   Bug fix: `TypeAlias` forward reference results in `Unknown` [pylance-release#3654](https://github.com/microsoft/pylance-release/issues/3654)
-   Bug fix: Linting disappeares when using multiple folders in workspace [pylance-release#3652](https://github.com/microsoft/pylance-release/issues/3652)
-   Bug fix: Massive performance issues for all Pylance features in some projects [pylance-release#3632](https://github.com/microsoft/pylance-release/issues/3632)
-   Enhancement: Inappropriate type error with docstrings [pylance-release#3612](https://github.com/microsoft/pylance-release/issues/3612)
-   Bug fix: How to prevent autocomplete of type hints [pylance-release#3599](https://github.com/microsoft/pylance-release/issues/3599)
-   Bug fix: RPyC Python module description looks strange [pylance-release#3549](https://github.com/microsoft/pylance-release/issues/3549)
-   Bug fix: `Add "# type: ignore" to suppress warning` places comment in wrong place [pylance-release#3544](https://github.com/microsoft/pylance-release/issues/3544)
-   Bug fix: Bug template url gives 404 message [pylance-release#3497](https://github.com/microsoft/pylance-release/issues/3497)
-   Bug fix: Bug on Pylance 2022.9.40 (released Sept 28, 2022) [pylance-release#3401](https://github.com/microsoft/pylance-release/issues/3401)
-   Enhancement: Emit warning for unmatched `#region`/`#endregion` [pylance-release#3308](https://github.com/microsoft/pylance-release/issues/3308)
-   Bug fix: lsp notebooks and jupyter.runStartupCommands [pylance-release#3219](https://github.com/microsoft/pylance-release/issues/3219)

## 2022.11.40 (30 November 2022) Release

-   Release version that rolls up changes from the [2022.11.32](https://github.com/microsoft/pylance-release/blob/main/CHANGELOG.md#20221132-16-november-2022-prerelease) prerelease build.

## 2022.11.32 (16 November 2022) PreRelease

Notable changes:

-   Bug fix: Don't treat empty open file as closed file.

## 2022.11.31 (16 November 2022) PreRelease

Notable changes:

-   Enhancement: Support for hint in inline `if` statement [pylance-release#3635](https://github.com/microsoft/pylance-release/issues/3635)
-   Bug fix: Update Pylance details displayed in VS Code [pylance-release#3626](https://github.com/microsoft/pylance-release/issues/3626)
-   Bug fix: Ensure folded function names are visible in Visual Studio [pylance-release#3580](https://github.com/microsoft/pylance-release/issues/3580)
-   Bug fix: Last expression in notebook cell should not be marked as unused [pylance-release#3282](https://github.com/microsoft/pylance-release/issues/3282)
-   Bug fix: Second declarations of from imports are marked as not defined [pylance-release#3218](https://github.com/microsoft/pylance-release/issues/3218)
-   Bug fix: Fix all can be customized and support pyright ignore on unused code [pylance-release#3144](https://github.com/microsoft/pylance-release/issues/3144)

Pylance's copy of Pyright has been updated from 1.1.279 to 1.1.280.

-   See Pyright's release notes for details: [1.1.280](https://github.com/microsoft/pyright/releases/tag/1.1.280).

## 2022.11.30 (16 November 2022) Release

-   Release version that rolls up changes from the [2022.11.21](https://github.com/microsoft/pylance-release/blob/main/CHANGELOG.md#20221121-9-november-2022-prerelease) prerelease build.

## 2022.11.21 (9 November 2022) PreRelease

Notable changes:

-   Bug fix: Fix Diagnostic links to jump straight into Pyright's documentation [pylance-release#3589](https://github.com/microsoft/pylance-release/issues/3589)
-   Bug fix: Parameters for a TypedDict don't show on hover [pylance-release#3569](https://github.com/microsoft/pylance-release/issues/3569)
-   Bug fix: Diagnostics in a notebook are not removed when changing language [pylance-release#3555](https://github.com/microsoft/pylance-release/issues/3555)
-   Bug fix: Parmeter hints not working with a child class attribute [pylance-release#3512](https://github.com/microsoft/pylance-release/issues/3512)
-   Bug fix: Rename fails in untitled notebook or untitled python file [pylance-release#3276](https://github.com/microsoft/pylance-release/issues/3276)
-   Bug fix: UNC paths are not parsed correctly [pylance-release#2891](https://github.com/microsoft/pylance-release/issues/2891)

Pylance's copy of Pyright has been updated from 1.1.278 to 1.1.279.

-   See Pyright's release notes for details: [1.1.279](https://github.com/microsoft/pyright/releases/tag/1.1.279).

## 2022.11.20 (9 November 2022) Release

-   Release version that rolls up changes from the [2022.11.11](https://github.com/microsoft/pylance-release/blob/main/CHANGELOG.md#20221111-2-november-2022-prerelease) prerelease build.

## 2022.11.11 (2 November 2022) PreRelease

Notable changes:

-   Bug fix: fix django CharField signature mismatch base class Field's init vs CharField's new function [pylance-release#3431](https://github.com/microsoft/pylance-release/issues/3431)
-   Bug fix: Fix parens for extract [pylance-release#1768](https://github.com/microsoft/pylance-release/issues/1768)
-   Bug fix: Fix type alias doc strings [pylance-release#3402](https://github.com/microsoft/pylance-release/issues/3402)
-   Bug fix: Fix crash when indexing is enabled. [pylance-release#3510](https://github.com/microsoft/pylance-release/issues/3510)

Pylance's copy of Pyright has been updated from 1.1.277 to 1.1.278.

-   See Pyright's release notes for details: [1.1.278](https://github.com/microsoft/pyright/releases/tag/1.1.278).

## 2022.11.10 (1 November 2022) Release

-   Release version that rolls up changes from the [2022.10.41](https://github.com/microsoft/pylance-release/blob/main/CHANGELOG.md#20221041-26-october-2022-prerelease) prerelease build.

## 2022.10.41 (26 October 2022) PreRelease

Notable changes:

-   Bug Fix: Fixed source mapper perf issue. ([pylance-release#3513](https://github.com/microsoft/pylance-release/issues/3513))
-   Bug Fix: Fixed crash on notebook cell reordering. ([pylance-release#3433](https://github.com/microsoft/pylance-release/issues/3433))
-   Enhancement: Changed auto import default to off. ([pylance-release#3467](https://github.com/microsoft/pylance-release/issues/3467))
-   Enhancement: Updated pandas stubs.
-   Enhancement: Updated typeshed.

Pylance's copy of Pyright has been updated from 1.1.276 to 1.1.277.

-   See Pyright's release notes for details: [1.1.277](https://github.com/microsoft/pyright/releases/tag/1.1.277).

## 2022.10.40 (26 October 2022) Release

-   Release version that rolls up changes from the [2022.10.31](https://github.com/microsoft/pylance-release/blob/main/CHANGELOG.md#20221021-19-october-2022-prerelease) prerelease build.

## 2022.10.31 (19 October 2022) PreRelease

Notable changes:

-   Bug Fix: Fixed a crash due to notebook cell reordering. ([pylance-release#3469](https://github.com/microsoft/pylance-release/issues/3469))
-   Bug Fix: Don't disable type checking mode for notebooks that don't exist on disk. ([pylance-release#3412](https://github.com/microsoft/pylance-release/issues/3412))
-   Enhancement: Improved smart selection behavior to include argument lists. ([pylance-release#3301](https://github.com/microsoft/pylance-release/issues/3301))
-   Enhancement: Improved doc string formatter to handle cv2 style doc string better. ([pylance-release#2945](https://github.com/microsoft/pylance-release/issues/2945))
-   Enhancement: Updated pandas stubs

Pylance's copy of Pyright has been updated from 1.1.275 to 1.1.276.

-   See Pyright's release notes for details: [1.1.276](https://github.com/microsoft/pyright/releases/tag/1.1.276).

## 2022.10.30 (19 October 2022) Release

-   Release version that rolls up changes from the [2022.10.21](https://github.com/microsoft/pylance-release/blob/main/CHANGELOG.md#20221021-12-october-2022-prerelease) prerelease build.

## 2022.10.21 (12 October 2022) PreRelease

Notable changes:

-   Bug Fix: Fixed a crash due to LSP type mismatch. ([pylance-release#3453](https://github.com/microsoft/pylance-release/issues/3453))
-   Bug Fix: Fixed behavior of `__init__` parameter synthesis when `dataclass_transform` is applied to a base class. ([pylance-release#3304](https://github.com/microsoft/pylance-release/issues/3304))
-   Enhancement: Improved `go to definition` behavior when multiple `pyi` are used for 1 `py` file. ([pylance-release#3227](https://github.com/microsoft/pylance-release/issues/3227))
-   Enhancement: Updated pandas stubs
-   Enhancement: Updated matplotlib stubs
-   Enhancement: New setting `python.analysis.packageIndexDepths` is added. User can use the setting to control indexing behavior.

Pylance's copy of Pyright has been updated from 1.1.274 to 1.1.275.

-   See Pyright's release notes for details: [1.1.275](https://github.com/microsoft/pyright/releases/tag/1.1.275).

## 2022.10.20 (12 October 2022) Release

-   Release version that rolls up changes from the [2022.10.11](https://github.com/microsoft/pylance-release/blob/main/CHANGELOG.md#20221011-5-october-2022-prerelease) prerelease build.

## 2022.10.11 (5 October 2022) PreRelease

Notable changes:

-   Enhancement: Handles cache better with multi root workspaces. ([pylance-release#3408](https://github.com/microsoft/pylance-release/issues/3408))
-   Bug Fix: Properly propagates future imports between notebook cells. ([pylance-release#3376](https://github.com/microsoft/pylance-release/issues/3376))
-   Enhancement: Improved parse tree recovery for missing statements. ([pylance-release#3319](https://github.com/microsoft/pylance-release/issues/3319))
-   Enhancement: Updated pandas stubs

Pylance's copy of Pyright has been updated from 1.1.273 to 1.1.274.

-   See Pyright's release notes for details: [1.1.274](https://github.com/microsoft/pyright/releases/tag/1.1.274).

## 2022.10.10 (5 October 2022) Release

-   Release version that rolls up changes from the [2022.9.41](https://github.com/microsoft/pylance-release/blob/main/CHANGELOG.md#2022941-28-september-2022-prerelease) prerelease build.

## 2022.9.41 (28 September 2022) PreRelease

Notable changes:

-   Enhancement: Added UX to control typeCheckingMode within language status button on status bar.
-   Bug Fix: The inferred argument type is confusing in subclass of logging.FileHandler ([pylance-release#3381](https://github.com/microsoft/pylance-release/issues/3381))

Pylance's copy of Pyright has been updated from 1.1.272 to 1.1.273.

-   See Pyright's release notes for details: [1.1.273](https://github.com/microsoft/pyright/releases/tag/1.1.273).

## 2022.9.40 (26 September 2022) Release

-   Release version that rolls up changes from the [2022.9.31](https://github.com/microsoft/pylance-release/blob/main/CHANGELOG.md#2022931-21-september-2022-prerelease) prerelease build.

## 2022.9.31 (21 September 2022) PreRelease

Notable changes:

-   Enhancement: Don't show diagnostics within IPython cell magics ([pylance-release#3327](https://github.com/microsoft/pylance-release/issues/3327))
-   Enhancement: Extended support for method override completions that use member access expression forms in a parameter's default value expression ([pylance-release#3374](https://github.com/microsoft/pylance-release/issues/3374))
-   Enhancement: Updated pandas stubs
-   Bug Fix: Default includes and excludes weren't being used if a `pyproject.toml` file was present ([pylance-release#3348](https://github.com/microsoft/pylance-release/issues/3348))
-   Bug Fix: Replaced django-stubs with a more pyright friendly version from ([sbdchd/django-types](https://github.com/sbdchd/django-types)) ([pylance-release#3359](https://github.com/microsoft/pylance-release/issues/3359))
-   Bug Fix: Inlay hint of bigInt incorrectly displaying int ([pylance-release#3355](https://github.com/microsoft/pylance-release/issues/3355))
-   Bug Fix: Display InlayHints only on variables that haven't already been annotated ([pylance-release#3325](https://github.com/microsoft/pylance-release/issues/3325))

Pylance's copy of Pyright has been updated from 1.1.271 to 1.1.272.

-   See Pyright's release notes for details: [1.1.272](https://github.com/microsoft/pyright/releases/tag/1.1.272).

-   Unreleased in Pyright, but included in Pylance:
    -   Bug Fix: False negative for calling positional-only argument by name

## 2022.9.30 (21 September 2022) Release

-   Release version that rolls up changes from the [2022.9.21](https://github.com/microsoft/pylance-release/blob/main/CHANGELOG.md#2022921-14-september-2022-prerelease) prerelease build.

## 2022.9.21 (14 September 2022) PreRelease

Notable changes:

-   Bug Fix: Using `Concatenate` and `ParamSpec` leads to skipped parameter in signature help ([pylance-release#3275](https://github.com/microsoft/pylance-release/issues/3275))
-   Bug Fix: Unexpected `reportMissingImports` in notebook for local package ([pylance-release#3208](https://github.com/microsoft/pylance-release/issues/3208))
-   Experiment: New auto-indent approach using `formatOnType`. We'll be enabling this for a percentage of prerelease users in the near future ([pylance-release#1613](https://github.com/microsoft/pylance-release/issues/1613))

Pylance's copy of Pyright has been updated from 1.1.270 to 1.1.271.

-   See Pyright's release notes for details: [1.1.271](https://github.com/microsoft/pyright/releases/tag/1.1.271).

## 2022.9.20 (14 September 2022) Release

-   Release version that rolls up changes from the [2022.9.11](https://github.com/microsoft/pylance-release/blob/main/CHANGELOG.md#2022911-7-september-2022-prerelease) prerelease build.

## 2022.9.11 (7 September 2022) PreRelease

Notable changes:

-   Enhancement: Include, exclude, and ignore paths can now be provided via settings in VS Code: `python.analysis.include`, `python.analysis.exclude`, `python.analysis.ignore` ([pylance-release#3261](https://github.com/microsoft/pylance-release/issues/3261), [pylance-release#3266](https://github.com/microsoft/pylance-release/issues/3266))
-   Enhancement: Show names of empty modules in auto completion list ([pylance-release#3293](https://github.com/microsoft/pylance-release/issues/3293), [pylance-release#3289](https://github.com/microsoft/pylance-release/issues/3289))
-   Enhancement: Updated bundled typeshed and pandas stubs
-   Bug Fix: "Remove all unused imports" code action now only removes top level imports and "Remove unused import" code action now removes leading whitespace ([pylance-release#3181](https://github.com/microsoft/pylance-release/issues/3181))
-   Bug Fix: Don't convert imports to relative format in user files that are within `extraPaths` ([pylance-release#3194](https://github.com/microsoft/pylance-release/issues/3194))
-   Bug Fix: Fixed availability of refactoring commands ([pylance-release#3246](https://github.com/microsoft/pylance-release/issues/3246))
-   Bug Fix: Fixed ignoring of IPython magics that appear after a dedent ([pylance-release#3251](https://github.com/microsoft/pylance-release/issues/3251))
-   Bug Fix: Fixed importing of `style` and `Axes` in matplotlib stubs ([pylance-release#3273](https://github.com/microsoft/pylance-release/issues/3273))
-   Bug Fix: Logging of file system exceptions was excessively verbose ([pylance-release#3291](https://github.com/microsoft/pylance-release/issues/3291))

Pylance's copy of Pyright has been updated from 1.1.269 to 1.1.270.

-   See Pyright's release notes for details: [1.1.270](https://github.com/microsoft/pyright/releases/tag/1.1.270).

## 2022.9.10 (7 September 2022) Release

-   Release version that rolls up changes from the [2022.8.51](https://github.com/microsoft/pylance-release/blob/main/CHANGELOG.md#2022851-31-august-2022-prerelease) prerelease build.

## 2022.8.51 (31 August 2022) PreRelease

Notable changes:

-   Enhancement: Updated bundled pandas stubs.
-   Bug Fix: Pylance erroneously marks async in async for as invalid in Jupyter notebook ([pylance-release#3205](https://github.com/microsoft/pylance-release/issues/3205))
-   Bug Fix: Ignoring \*.ipynb files does not work ([pylance-release#2135](https://github.com/microsoft/pylance-release/issues/2135))
-   Bug Fix: Pylance experiment doesn't provide semantic colorization without scrolling [pylance-release#2837](https://github.com/microsoft/pylance-release/issues/2837), [pylance-release#2897](https://github.com/microsoft/pylance-release/issues/2897).

Pylance's copy of Pyright has been updated from 1.1.268 to 1.1.269.

-   See Pyright's release notes for details: [1.1.269](https://github.com/microsoft/pyright/releases/tag/1.1.269).

## 2022.8.50 (31 August 2022) Release

-   Release version that rolls up changes from the [2022.8.41](https://github.com/microsoft/pylance-release/blob/main/CHANGELOG.md#2022841-24-august-2022-prerelease) prerelease build.

## 2022.8.41 (24 August 2022) PreRelease

Notable changes:

-   Enhancement: Updated matplotlib type stubs
-   Bug Fix: Mismatch between `__init__` arg name and matching attribute results in InternalError in 3.10 pattern matching ([pylance-release#3197](https://github.com/microsoft/pylance-release/issues/3197))
-   Bug Fix: Code folding issue with imports ([pylance-release#3159](https://github.com/microsoft/pylance-release/issues/3159))
-   Bug Fix: No folding of parenth_form expressions without commas [pylance-release#3085](https://github.com/microsoft/pylance-release/issues/3085)

Pylance's copy of Pyright has been updated to 1.1.268.

-   See Pyright's release notes for details: [1.1.268](https://github.com/microsoft/pyright/releases/tag/1.1.268).

## 2022.8.40 (24 August 2022) Release

-   Release version that rolls up changes from the [2022.8.31](https://github.com/microsoft/pylance-release/blob/main/CHANGELOG.md#2022831-17-august-2022-prerelease) prerelease build.

## 2022.8.31 (17 August 2022) PreRelease

Notable changes:

-   Bug Fix: Importing .py file in same directory as notebook ([pylance-release#3017](https://github.com/microsoft/pylance-release/issues/3017))
-   Bug Fix: Fixed bug in parser that resulted in crash when a soft keyword was used as a class pattern keyword argument name [pylance-release#3197](https://github.com/microsoft/pylance-release/issues/3197).

Pylance's copy of Pyright has been updated to 1.1.267.

-   See Pyright's release notes for details: [1.1.267](https://github.com/microsoft/pyright/releases/tag/1.1.267).

## 2022.8.30 (17 August 2022) Release

-   Release version that rolls up changes from the [2022.8.21](https://github.com/microsoft/pylance-release/blob/main/CHANGELOG.md#2022821-10-august-2022-prerelease) prerelease build.

## 2022.8.21 (10 August 2022) PreRelease

Notable changes:

-   Bug Fix: Symbol renaming in Jupyter notebooks only works in a single cell ([pylance-release#3061](https://github.com/microsoft/pylance-release/issues/3061))

Pylance's copy of Pyright has been updated to 1.1.266.

-   See Pyright's release notes for details: [1.1.266](https://github.com/microsoft/pyright/releases/tag/1.1.266).

-   Unreleased in Pyright, but included in Pylance:
    -   Bug Fix: Fixed bug that caused error to be suppressed when calling `assert_never` with bad arguments (incorrect number, etc).
    -   Enhancement: Added support for dictionary expansion of a TypedDict within a dictionary literal expression.

## 2022.8.20 (10 August 2022) Release

-   Release version that rolls up changes from the [2022.8.11](https://github.com/microsoft/pylance-release/blob/main/CHANGELOG.md#2022811-3-august-2022) to the [2022.8.12](https://github.com/microsoft/pylance-release/blob/main/CHANGELOG.md#2022812-8-august-2022) prerelease build.

## 2022.8.12 (8 August 2022)

Notable changes:

-   Bug Fix: Improved doc string support on function/callable assigned to a variable.
    ([pylance-release#3135](https://github.com/microsoft/pylance-release/issues/3135))
-   Bug Fix: Fixed crash on untitled.ipynb file.
    ([pylance-release#3126](https://github.com/microsoft/pylance-release/issues/3126))
-   Bug Fix: Fixed side by side file import bug on notebook.
    ([pylance-release#3017](https://github.com/microsoft/pylance-release/issues/3017))
-   Enhancement: Updated bundled typeshed.

Pylance's copy of Pyright has been updated from 1.1.265 to 1.1.266.

-   See Pyright's release notes for details: [1.1.266](https://github.com/microsoft/pyright/releases/tag/1.1.266).

## 2022.8.11 (3 August 2022)

Notable changes:

-   Enhancement: Auto/add imports now supports new import format options (relative, absolute)
-   Bug Fix: Remove double click to insert type hint on TypeVars, ParamSpec and typeAlias assigments

Pylance's copy of Pyright has been updated from 1.1.264 to 1.1.265.

-   See Pyright's release notes for details: [1.1.265](https://github.com/microsoft/pyright/releases/tag/1.1.265).

-   Unreleased in Pyright, but included in Pylance:
    -   Bug Fix: Fixed a bug that caused incorrect type evaluation because of stale module paths that are cached for specific source files. Module paths are dependent on the list of configured import resolution paths, so when the import resolution paths change, we may need to recompute the module path for a source file.
    -   Bug Fix: Fixed a bug that caused a false positive error when using a list comprehension within a method that is overloaded to accept either a `LiteralString` or a `str`. The incorrect overload was chosen in some cases, picking the `LiteralString` variant rather than the `str` variant even though `LiteralString` variant generated type errors.

## 2022.8.10 (3 August 2022)

-   Release version that rolls up changes from the [2022.7.41](https://github.com/microsoft/pylance-release/blob/main/CHANGELOG.md#2022741-20-july-2022) to the [2022.7.44](https://github.com/microsoft/pylance-release/blob/main/CHANGELOG.md#2022744-31-july-2022) prerelease build.

## 2022.7.44 (31 July 2022)

Notable changes:

-   Bug Fix: Removed `auto` option from import format.

## 2022.7.43 (28 July 2022)

Notable changes:

-   Bug Fix: Fixed the handling of library module under workspace root in toggle import format.

## 2022.7.42 (27 July 2022)

Notable changes:

-   Bug Fix: Improved inlay type hints code gen on double click.
    ([pylance-release#3095](https://github.com/microsoft/pylance-release/issues/3095))
-   Bug Fix: Provided name for all source code actions.
    ([pylance-release#3091](https://github.com/microsoft/pylance-release/issues/3091))
-   Bug Fix: Improved magic command handling in interactive window.
    ([pylance-release#2894](https://github.com/microsoft/pylance-release/issues/2894))

Pylance's copy of Pyright has been updated from 1.1.262 to 1.1.264.

-   See Pyright's release notes for details: [1.1.263](https://github.com/microsoft/pyright/releases/tag/1.1.263), [1.1.264](https://github.com/microsoft/pyright/releases/tag/1.1.264).

-   Issues fixed:
    -   Bug Fix: Incorrect type analysis in loop.
        ([pylance-release#3077](https://github.com/microsoft/pylance-release/issues/3077))

## 2022.7.41 (20 July 2022)

Notable changes:

-   Bug Fix: Improved virtual workspace handling.
    ([pylance-release#2978](https://github.com/microsoft/pylance-release/issues/2978))
-   Bug Fix: Improved extract method code generation around expression.
    ([pylance-release#2906](https://github.com/microsoft/pylance-release/issues/2906))
-   Enhancement: Added new capability to Inlay hint that will insert the type when double clicked.
    ([pylance-release#2970](https://github.com/microsoft/pylance-release/issues/2970))
-   Enhancement: Added new code action `remove all unused imports` that also supports `Fix all`.
-   Enhancement: Updated bundled pandas stubs.
-   Enhancement: Updated bundled typeshed.

Pylance's copy of Pyright has been updated from 1.1.260 to 1.1.262.

-   See Pyright's release notes for details: [1.1.261](https://github.com/microsoft/pyright/releases/tag/1.1.261), [1.1.262](https://github.com/microsoft/pyright/releases/tag/1.1.262).

-   Issues fixed:
    -   Performance: Improved type analysis performance.
        ([pylance-release#2881](https://github.com/microsoft/pylance-release/issues/2881))

## 2022.7.40 (20 July 2022)

-   Release version that rolls up changes from the [2022.7.31](https://github.com/microsoft/pylance-release/blob/main/CHANGELOG.md#2022731-13-july-2022) prerelease build.

## 2022.7.31 (13 July 2022)

Notable changes:

-   Bug Fix: Installing py.typed library will disable bundled partial stubs.
-   Enhancement: Provide hidden option to disable library file watching
    ([pylance-release#3001](https://github.com/microsoft/pylance-release/issues/3001))
-   Enhancement: Support extra commit characters ("." and "(") in completion when applicable.
    ([pylance-release#2946](https://github.com/microsoft/pylance-release/issues/2946))
-   Enhancement: Updated bundled pandas stubs.
-   Enhancement: Updated typeshed stubs to the latest version, which eliminates support for Python 3.6.

Pylance's copy of Pyright has been updated from 1.1.257 to 1.1.260.

-   See Pyright's release notes for details: [1.1.258](https://github.com/microsoft/pyright/releases/tag/1.1.258), [1.1.259](https://github.com/microsoft/pyright/releases/tag/1.1.259), [1.1.260](https://github.com/microsoft/pyright/releases/tag/1.1.260).

-   Issues fixed:
    -   Bug Fix: Fixed a bug that resulted in incorrect isinstance type narrowing when one or more of the filter classes was decorated with a class decorator.
        ([pylance-release#3033](https://github.com/microsoft/pylance-release/issues/3033))
    -   Performance: Added performance optimization for a special case that can occur in code without type annotations. It affects "pseudo-generic" classes that are parameterized recursively.
        ([pylance-release#2983](https://github.com/microsoft/pylance-release/issues/2983))

## 2022.7.30 (13 July 2022)

-   Release version that rolls up changes from the [2022.7.21](https://github.com/microsoft/pylance-release/blob/main/CHANGELOG.md#2022721-6-july-2022) prerelease build.

## 2022.7.21 (6 July 2022)

Notable changes:

-   Bug Fix: Don't report unused imports/variables in notebooks when using the LSP notebooks experiment.
    ([pylance-release#2986](https://github.com/microsoft/pylance-release/issues/2986))
-   Bug Fix: Handle signature help better on nested calls.
    ([pylance-release#1990](https://github.com/microsoft/pylance-release/issues/1990))
-   Enhancement: Improved semantic token provider performance.
-   Enhancement: Updated bundled pandas stubs.

Pylance's copy of Pyright has been updated from 1.1.256 to 1.1.257.

-   Unreleased in Pyright, but included in Pylance:
    -   Fixed a bug that resulted in incorrect type narrowing when using an `in` expression and the LHS operand is of type `type`. This situation requires some special casing.
    -   Fixed a bug in the handling of generic type aliases that are parameterized by ParamSpecs in the case where an explicit type argument is not provided. The type argument should default to `...` in this case.
    -   Fixed bug in the expression printer. It was not properly handling a minimal slice (`:`).
    -   Added optimization for slice expression evaluation. It can be skipped in cases where the we are speculatively evaluating the type.
    -   Implemented optimization for type evaluation for index expressions. In cases where there are multiple subexpressions separated by commas, we can skip the check for the `__index__` magic method.
    -   Fixed a bug that resulted in incorrect isinstance type narrowing when one or more of the filter classes was decorated with a class decorator.
    -   Added support for context managers whose **exit** method is declared to return a falsy return type other than `None`.
-   See Pyright's release notes for details: [1.1.257](https://github.com/microsoft/pyright/releases/tag/1.1.257).

-   Issues fixed:
    -   Bug Fix: Fixed a bug in type narrowing which caused pyright to report "code is unreachable"
        ([pylance-release#2992](https://github.com/microsoft/pylance-release/issues/2992))
    -   Bug Fix: Fixed a bug that caused incorrect diagnostics to be reported.
        ([pylance-release#2989](https://github.com/microsoft/pylance-release/issues/2989))
    -   Bug Fix: Don't report assert_type diagnostics when type checking mode is off.
        ([pylance-release#2982](https://github.com/microsoft/pylance-release/issues/2982))

## 2022.7.20 (6 July 2022)

-   Release version that rolls up changes from the [2022.6.31](https://github.com/microsoft/pylance-release/blob/main/CHANGELOG.md#2022631-29-june-2022) to [2022.7.11](https://github.com/microsoft/pylance-release/blob/main/CHANGELOG.md#2022711-1-july-2022) prerelease builds.

## 2022.7.11 (1 July 2022)

Notable changes:

-   Bug Fix: Method overriding template is auto inserted before opening parentheses.
    ([pylance-release#2987](https://github.com/microsoft/pylance-release/issues/2987)))

## 2022.6.31 (29 June 2022)

Notable changes:

-   Bug Fix: Period and open paren should insert currently selected IntelliSense completion
    ([pylance-release#2946](https://github.com/microsoft/pylance-release/issues/2946))
-   Bug Fix: Pylance/pyright is not running in IPythonMode
    ([pylance-release#2963](https://github.com/microsoft/pylance-release/issues/2963))

Pylance's copy of Pyright has been updated from 1.1.255 to 1.1.256.

-   See Pyright's release notes for details: [1.1.256](https://github.com/microsoft/pyright/releases/tag/1.1.256).

## 2022.6.30 (22 June 2022)

Notable changes:

-   Enhancement: Added support for inlay hints on function return and variable declarations.
    ```json
    "python.analysis.inlayHints.variableTypes": true
    "python.analysis.inlayHints.functionReturnTypes": true
    ```
    ([pylance-release#2643](https://github.com/microsoft/pylance-release/discussions/2643))
-   Bug Fix: Error message persists for package imports
    ([pylance-release#2246](https://github.com/microsoft/pylance-release/issues/2246))
-   Bug Fix: Extension is watching files outside of the workspace
    ([pylance-release#2914](https://github.com/microsoft/pylance-release/issues/2914))

Pylance's copy of Pyright has been updated from 1.1.254 to 1.1.255.

-   See Pyright's release notes for details: [1.1.255](https://github.com/microsoft/pyright/releases/tag/1.1.255).

-   Issues fixed:
    -   Bug Fix: exported name not exposed from workspace package even though listed in `__all__`
        ([pylance-release#2150](https://github.com/microsoft/pylance-release/issues/2150))
    -   Bug Fix: Docstring missing on `@overload` methods (but not plain functions)
        ([pylance-release#2948](https://github.com/microsoft/pylance-release/issues/2948))

## 2022.6.20 (15 June 2022)

Notable changes:

-   Enhancement: Added new configuration setting called "defineConstant". It allows a configuration to specify one or more identifiers that should be assigned by pyright's binder to be constant anywhere they appear. Values can be boolean (true or false) or a string. If an identifier of this value is used within a conditional statement (like `if not DEBUG:`) it will affect pyright's reachability analysis for the guarded code blocks.
-   Enhancement: Added support for new reportTypeCommentUsage diagnostic check. It flags the usage of # type: xxx comments for functions and variables. These are still supported for backward compatibility, but they are increasingly irrelevant and will likely be deprecated in the next few years.

Pylance's copy of Pyright has been updated from 1.1.253 to 1.1.254.

-   See Pyright's release notes for details: [1.1.254](https://github.com/microsoft/pyright/releases/tag/1.1.254).

## 2022.6.10 (8 June 2022)

Notable changes:

-   Enhancment: Changed our version numbering scheme so we can support VS Code's [pre-release extensions feature](https://code.visualstudio.com/updates/v1_63#_pre-release-extensions). Stable versions going forward will be YYYY.MM.X0 and prerelease versions will be YYYY.MM.X1, where X starts at 1 each month and increments. Stable and prerelease versions released on the same day will have the same value for X.
-   Enhancement: Show module paths in auto-import list
    ([pylance-release#2885](https://github.com/microsoft/pylance-release/issues/2885))
-   Bug Fix: "request cancelled" errors when using Pylance on vscode.dev
    ([pylance-release#2743](https://github.com/microsoft/pylance-release/issues/2743))
-   Bug Fix: Fix file watcher behavior with ZIP files
    ([pylance-release#2890](https://github.com/microsoft/pylance-release/issues/2890))

Pylance's copy of Pyright has been updated from 1.1.251 to 1.1.253.

-   See Pyright's release notes for details: [1.1.252](https://github.com/microsoft/pyright/releases/tag/1.1.252), [1.1.253](https://github.com/microsoft/pyright/releases/tag/1.1.253).

-   Issues fixed:
    -   Bug Fix: Stack overflow during symbol rename
        ([pylance-release#2550](https://github.com/microsoft/pylance-release/issues/2550))

## 2022.6.0 (1 June 2022)

Pylance's copy of Pyright has been updated from 1.1.249 to 1.1.251.

-   See Pyright's release notes for details: [1.1.249](https://github.com/microsoft/pyright/releases/tag/1.1.249), [1.1.251](https://github.com/microsoft/pyright/releases/tag/1.1.251).

-   Issues fixed:
    -   Bug Fix: Object of type "None" cannot be called
        ([pylance-release#2871](https://github.com/microsoft/pylance-release/issues/2871))
    -   Bug Fix: No keys hints for TypedDict when it is in union
        ([pylance-release#2860](https://github.com/microsoft/pylance-release/issues/2860))
    -   Bug Fix: Bool are int
        ([pylance-release#2865](https://github.com/microsoft/pylance-release/issues/2865))

## 2022.5.3 (25 May 2022)

Notable changes:

-   Experimental Feature: Treat each Jupyter notebook cell as a separate document rather than concatenating the cells together into a single document. Has the potential to fix a lot of Pylance notebook behaviors. Can be enabled by setting `"python.pylanceLspNotebooksEnabled": true`.
-   Bug Fix: Multiline tuples don't fold
    ([pylance-release#2779](https://github.com/microsoft/pylance-release/issues/2779))
-   Bug Fix: Report Issue command fails if Pylance has not been activated
    ([pylance-release#2791](https://github.com/microsoft/pylance-release/issues/2791))

Pylance's copy of Pyright has been updated from 1.1.247 to 1.1.249.

-   See Pyright's release notes for details: [1.1.248](https://github.com/microsoft/pyright/releases/tag/1.1.248), [1.1.249](https://github.com/microsoft/pyright/releases/tag/1.1.249).

-   Issues fixed:
    -   Enhancement: Improved parser recovery for member access expressions that are missing the member name
        ([pylance-release#2836](https://github.com/microsoft/pylance-release/issues/2836))
    -   Bug Fix: Incorrect type evaluation for a property access within a class when that property's getter has a generic return type
        ([pylance-release#2841](https://github.com/microsoft/pylance-release/issues/2841))

## 2022.5.2 (18 May 2022)

Notable changes:

-   Bug Fix: Jupyter notebooks hang
    ([pylance-release#2783](https://github.com/microsoft/pylance-release/issues/2783))

Pylance's copy of Pyright has been updated from 1.1.246 to 1.1.247.

-   See Pyright's release notes for details: [1.1.247](https://github.com/microsoft/pyright/releases/tag/1.1.247).

-   Issues fixed:
    -   Enhancement: Improved handling of context managers that swallow exceptions
        ([pylance-release#982](https://github.com/microsoft/pylance-release/issues/982),
        [pylance-release#2081](https://github.com/microsoft/pylance-release/issues/2081))

## 2022.5.1 (11 May 2022)

Notable changes:

-   Bug Fix: TypedDict attribute suggestions don't recognise f-string quote type
    ([pylance-release#1919](https://github.com/microsoft/pylance-release/issues/1919))
-   Bug Fix: Auto complete for attributes form CBV in Django not working
    ([pylance-release#2059](https://github.com/microsoft/pylance-release/issues/2059))
-   Bug Fix: Always require restart when installing new package and cannot find python interpreter ([pylance-release#2505](https://github.com/microsoft/pylance-release/issues/2505))

Pylance's copy of Pyright has been updated from 1.1.244 to 1.1.246.

-   See pyright's release notes for details: [1.1.246](https://github.com/microsoft/pyright/releases/tag/1.1.246), [1.1.245](https://github.com/microsoft/pyright/releases/tag/1.1.245).

-   Issues fixed:
    -   Bug Fix: Functions in class cannot be analyzed under some circumstances ([pylance-release#2745](https://github.com/microsoft/pylance-release/issues/2745))
    -   Bug Fix: False positive with type variable seemingly not being bound correctly when return type is inferred ([pylance-release#2785](https://github.com/microsoft/pylance-release/issues/2785))
    -   Bug Fix: Value dependent typing signature with self-defined generic types incorrectly handled ([pylance-release#2784](https://github.com/microsoft/pylance-release/issues/2784))
    -   Bug Fix: Type of "globals" is unknown when module named as globals ([pylance-release#2793](https://github.com/microsoft/pylance-release/issues/2793))

## 2022.5.0-pre.1 (4 May 2022)

We're only shipping to insiders this week. This release includes a change in Pyright's code flow analysis of `NoReturn` calls. When a similar change was attempted in Pylance 2022.2.1 it caused perf issues and was reverted. Pyright has improved its `NoReturn` handling and we're giving it another shot, but we're limiting the exposure to insiders users for now.

Notable changes:

-   Enhancement: Show completion suggestions for overriding inherited class variables
    ([pylance-release#2059](https://github.com/microsoft/pylance-release/issues/2059))
-   Enhancement: Updated typeshed stubs to latest.

Pylance's copy of Pyright has been updated from 1.1.240 to 1.1.244.

-   See pyright's release notes for details: [1.1.241](https://github.com/microsoft/pyright/releases/tag/1.1.241), [1.1.242](https://github.com/microsoft/pyright/releases/tag/1.1.242), [1.1.243](https://github.com/microsoft/pyright/releases/tag/1.1.243), and [1.1.244](https://github.com/microsoft/pyright/releases/tag/1.1.244).

-   Issues fixed:
    -   Bug Fix: Improved detection of NoReturn calls within code flow graph.
    -   Bug Fix: Fixed bug that led to inconsistent type evaluation results when the code flow engine determined that an expression was unreachable.
        ([pylance-release#2745](https://github.com/microsoft/pylance-release/issues/2745))
    -   Bug Fix: Fixed bug that incorrectly inferred the type for an exception group when using a Python 3.11 `except*` statement.
        ([pylance-release#2762](https://github.com/microsoft/pylance-release/issues/2762))

## 2022.4.3 (27 April 2022)

Pylance's copy of Pyright has been updated from 1.1.239 to 1.1.240.

-   Unreleased in Pyright, but included in Pylance:
    -   Fixed regression in "reportUnnecessaryComparison" diagnostic check that resulted in false positives when the LHS or RHS evaluated to `Never`.
-   See pyright's release notes for details: [1.1.240](https://github.com/microsoft/pyright/releases/tag/1.1.240)

-   Issues fixed:
    -   Bug Fix: Fixed bug on tuple assignment inside of loop. ([pylance-release#2731](https://github.com/microsoft/pylance-release/issues/2731))

## 2022.4.2 (20 April 2022)

Notable changes:

-   Enhancement: Improvement on supporting doc comment for builtin modules.
    ([pylance-release#1938](https://github.com/microsoft/pylance-release/issues/1938))
-   Enhancement: Updated typeshed stubs to latest.

In addition, Pylance's copy of Pyright has been updated from 1.1.237 to 1.1.239.

-   See pyright's release notes for details: [1.1.238](https://github.com/microsoft/pyright/releases/tag/1.1.238) and [1.1.239](https://github.com/microsoft/pyright/releases/tag/1.1.239)

-   Issues fixed:
    -   Bug Fix: Fixed bug that resulted in an infinite loop when a reference to a generic function was passed to itself as an argument. ([pylance-release#2686](https://github.com/microsoft/pylance-release/issues/2686))

## 2022.4.1 (13 April 2022)

Notable changes:

-   Enhancement: Renaming a method will rename all overridden methods as well.
    ([pylance-release#813](https://github.com/microsoft/pylance-release/issues/813))
-   Bug Fix: pandas stub updated to remove Unknown type argument.
    ([pylance-release#1968](https://github.com/microsoft/pylance-release/issues/1968))
-   Enhancement: Named argument in call context will show up at the top in completion.

In addition, Pylance's copy of Pyright has been updated from 1.1.235 to 1.1.237.

-   Unreleased in Pyright, but included in Pylance:
    -   Fixed a bug that generated a false positive when importing from a "py.typed" namespace package. This change also loosens the requirements for a "py.typed" file to be in each of the submodules within a namespace package; a single "py.typed" within the top-level namespace directory is also now supported.
    -   Improved error message for protocol mismatch due to invariance of mutable attributes.
-   See pyright's release notes for details: [1.1.236](https://github.com/microsoft/pyright/releases/tag/1.1.236) and [1.1.237](https://github.com/microsoft/pyright/releases/tag/1.1.237)

-   Issues fixed:
    -   Enhancement: Better handling on namespace packages ([pylance-release#2562](https://github.com/microsoft/pylance-release/issues/2562))
    -   Bug Fix: Incorrect type inference in loops ([pylance-release#2552](https://github.com/microsoft/pylance-release/issues/2552))
    -   Bug Fix: False positive reportOptionalMemberAccess ([pylance-release#2549](https://github.com/microsoft/pylance-release/issues/2549))
    -   Performance: Improvement on analyzing "while True" loop ([pylance-release#2540](https://github.com/microsoft/pylance-release/issues/2540))

## 2022.4.0 (6 April 2022)

Notable changes:

-   Enhancement: Improved completions for native modules with matching stub files.
    ([pylance-release#2533](https://github.com/microsoft/pylance-release/issues/2533))
-   Bug Fix: Fixed docstring lookup for typeshed stubbed packages.
    ([pylance-release#2472](https://github.com/microsoft/pylance-release/issues/2472))
-   Enhancement: The stubs for pandas and django have been updated.

In addition, Pylance's copy of Pyright has been updated from 1.1.234 to 1.1.235 including the following changes:

-   [1.1.235](https://github.com/microsoft/pyright/releases/tag/1.1.235)
    -   Performance: Fixed a performance regression that manifested when analyzing a large dictionary literal statement with a declared type.
    -   Enhancement: (Contributed by Robert Craigie) Show TypedDict key type and docstring on hover.
    -   Behavior Change: Updated logic for `dataclass_transform` to handle recent clarification in PEP 681 for cases where one or more overloads are decorated with `dataclass_transform`.
    -   Enhancement: (Contributed by Kevin Coffey) Added support for type guard based on `a.b is None` or `a.b is not None` patterns where `b` is a member variable that distinguishes two different classes.
    -   Enhancement: (Contributed by Robert Craigie) Add support for going to definition for TypedDict keys.
    -   Behavior Change: Changed hover provider to display `(property)` rather than `(method)` if the field is decorated with a descriptor object.
        ([pylance-release#2508](https://github.com/microsoft/pylance-release/issues/2508))
    -   Enhancement: Changed logic for hover and completion providers to support docstrings for general descriptors rather than just properties.
    -   Enhancement: Made synthesized `get` method in `TypedDict` classes a bit smarter. If a field is required, the default parameter's argument (or `None` if no default argument is provided) is ignored because the type will always come from the required field. If the `TypedDict` class is marked `@final`, any literal key name that is not part of the class will always return the type of the default argument (or `None` if no default argument is provided).
    -   Bug Fix: Fixed bug that could theoretically account for some of the remaining stack overflows that we're seeing in the pylance telemetry.
    -   Bug Fix: Fixed bug in the package type verifier where it incorrectly flagged an assignment to a descriptor member within a child class as an ambiguous override of that member.
    -   Bug Fix: Changed the way pyright detects high memory usage and decides to empty its internal type cache.
    -   Performance: Added perf enhancement to improve analysis times for complex unannotated code. Lowered complexity threshold for call-site return type inference and skipped argument expression evaluation for call expression when base call expression type is unknown.
    -   Performance: More performance optimizations for complex unannotated functions. Don't evaluate argument or subscript expressions if base type of call expression or index expression is incomplete.
    -   Enhancement: Updated typeshed stubs to latest.

## 2022.3.4 (30 March 2022)

Notable changes:

-   Enhancement: Improved `Rename Symbol` to handle imports.
    ([pylance-release#1175](https://github.com/microsoft/pylance-release/issues/1175))
-   Bug Fix: Fixed conda temp.txt files causing analysis unneeded refresh.
-   Bug Fix: Ignore var decl in completions
    ([pylance-release#2189](https://github.com/microsoft/pylance-release/issues/2189))

In addition, Pylance's copy of Pyright has been updated from 1.1.232 to 1.1.234 including the following changes:

-   [1.1.234](https://github.com/microsoft/pyright/releases/tag/1.1.234)
    -   Performance: Fixed bug that resulted in long analysis times when using call-site type inference for very complex functions that have no parameter annotations.
    -   Behavior Change: Removed support for `transform_descriptor_types` parameter in `dataclass_transform`, a feature that was determined to be not necessary. Added support on normal dataclass handling for field types that are custom descriptor objects.
    -   Bug Fix: Fixed bug in logic that determines whether to empty the in-memory type cache if it has the potential to overflow the heap.
    -   Enhancement: Improved printing of string nodes in error and log messages. If the string node is long, it is truncated to 32 characters.
    -   Enhancement: Improved textual form of string literal types. If the string literal is very long (>50 characters), it is truncated.
    -   Bug Fix: Fixed recent regression that caused the "--verifytypes" feature to incorrectly report that the "self" parameter of a `@property` method as unannotated.
    -   Performance: Removed older mechanism for tracking "incomplete types" — those that have been partially evaluated within a code flow loop. The older mechanism is no longer needed. Removing this is a big performance win in some (typically more complex) pieces of code.
    -   Performance: Fixed performance issue that caused long analysis times in some complex unannotated functions when attempting to infer whether the function was a NoReturn return type.
    -   Performance: Improved performance of code flow "reachability" analysis.
    -   Enhancement: Updated typeshed stubs to the latest version.
    -   Bug Fix: Fixed false positive error in "unreachable exception" detection code when the exception was typed as `Type[Exception]`.
    -   Enhancement: Contributed by Kevin Coffey - Extended `a[I] is None` type narrowing logic to handle subtypes of Tuple including NamedTuple.
-   [1.1.233](https://github.com/microsoft/pyright/releases/tag/1.1.233)
    -   Behavior Change: When hovering over the LHS of an augmented assignment (e.g. the `a` within `a += x`), reveal the type of the symbol _after_ the operation rather than _before_.
    -   Enhancement: Updated the `reportUnusedExpression` check to also report diagnostics for a simple name expression as a standalone statement.
    -   Bug Fix (from pylance): Fixed several bugs related to "Rename Symbol" command and improved performance in some cases.
    -   Bug Fix: Fixed crashing bug due to stack overflow when traversing the code flow graph.
    -   Behavior Change: Modified algorithm for calculating the complexity of a function's code flow. If the complexity exceeds a certain threshold, pyright will not attempt to analyze the code.
    -   Bug Fix: Fixed a bug that resulted in incorrect import resolution when the import referenced an empty directory within the stubspath. It should continue searching for imports in other locations in this case.
    -   Bug Fix: Fixed regression that caused false positive error when protocol match involved a property that returned a type that was generic.
    -   Bug Fix: Fixed bug that resulted in a false negative when assigning an invariant type var was specialized with a protocol type.
    -   Bug Fix: Fixed several bugs relating to type evaluation within loops. This is a significant change to the code flow engine logic.
        ([pylance-release#2983](https://github.com/microsoft/pylance-release/issues/2983))

## 2022.3.3 (23 March 2022)

Notable changes:

-   Enhancement: Added support for `prepare rename`. This will let users know when `rename` is not allowed.
    ([pylance-release#1360](https://github.com/microsoft/pylance-release/issues/1360))
    ([pylance-release#2457](https://github.com/microsoft/pylance-release/issues/2457))
-   Enhancement: Improved `reportMissingSourceModule` to work for all different import cases.
    ([pylance-release#2158](https://github.com/microsoft/pylance-release/issues/2158))
-   Enhancement: Improved property completions.
-   Enhancement: The bundled stubs for django have been updated.

In addition, Pylance's copy of Pyright has been updated from 1.1.230 to 1.1.232 including the following changes:

-   [1.1.232](https://github.com/microsoft/pyright/releases/tag/1.1.232)
    -   Enhancement: Improved diagnostic messages for overload implementation mismatch.
    -   Bug Fix: Fixed bug that resulted in false negative when assigning one function to another and the dest contains named positional arguments that have no corresponding positional slot in the dest and the dest does not contain a \*\*kwargs.
        ([pylance-release#2497](https://github.com/microsoft/pylance-release/issues/2497))
    -   Bug Fix: Modified the special-case logic for `property` so it exposes methods and attributes provided by `object`.
    -   Bug Fix: Improved the `reportIncompatibleMethodOverride` check to report a diagnostic if the base method provides a default argument value for a parameter but the override does not.
    -   Behavior Change: Lowered cyclical code complexity threshold for code flow analysis in an attempt to reduce stack overflow crashes.
    -   Bug Fix: Fixed a false positive error relating to `__slots__` when using a descriptor object that was assigned to a class variable in a base class.
    -   Enhancement: Updated typeshed stubs to the latest version.
    -   Enhancement: Added support for new `assert_type` call, which is being added to Python 3.11 and typing_extensions.
    -   Bug Fix: Fixed false positive error that occurs when assigning a class variable with a type annotation an expression that involves the name of the class variable symbol.
    -   Bug Fix: Improved modeling of property class so its `fget`, `fset`, `fdel`, `__get__`, `__set__` and `__delete__` methods are updated properly when adding a setter or deleter.
    -   Bug Fix: Fixed bug that resulted in false positive when overriding a method with position-only parameters when the base uses the old-style mechanism and the override uses the new-style `/` separator or vice versa.
-   [1.1.231](https://github.com/microsoft/pyright/releases/tag/1.1.231)
    -   Behavior Change: Moved a couple of type-related diagnostics under the reportGeneralTypeIssues diagnostic rule rather than reporting them unconditionally.
    -   Bug Fix: Fixed false negative for the reportIncompatibleMethodOverride diagnostic check. It was not detecting the case where the base method used keyword parameters but the override method used position-only parameters.
    -   Bug Fix: Fixed bug that resulted in a false positive error when matching a module against a specialized generic protocol class.
    -   Bug Fix: Fixed a bug that resulted in misleading output when printing the type of a generic alias that includes a generic function parameterized by a ParamSpec and is later specialized.
    -   Bug Fix: Fixed bug that resulted in incorrect type evaluation when a generic type alias parameterized with a ParamSpec was specialized multiple times.
    -   Bug Fix: Fixed bug in "--verifytypes" feature. It was ignoring a missing parameter annotation for the first parameter in a non-method function.
    -   Bug Fix: Fixed a bug that resulted in a false positive error when a generic callback protocol was passed as an argument to another generic callback protocol.

## 2022.3.2 (16 March 2022)

Notable changes:

-   Enhancement: Updated Pandas stubs
-   Bug Fix: Removed duplicate SQLAlchemy stubs due to them now being in typeshed.
-   Enhancement: Allow auto import customization
    ([pylance-release#2312](https://github.com/microsoft/pylance-release/issues/2312))
-   Enhancement: Allow `Rename` on excluded files
    ([pylance-release#2468](https://github.com/microsoft/pylance-release/issues/2468))

In addition, Pylance's copy of Pyright has been updated from 1.1.228 to 1.1.230 including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Behavior Change: Moved a couple of type-related diagnostics under the reportGeneralTypeIssues diagnostic rule rather than reporting them unconditionally.
        ([pylance-release#2482](https://github.com/microsoft/pylance-release/issues/2482))
    -   Bug Fix: Fixed false negative for the reportIncompatibleMethodOverride diagnostic check. It was not detecting the case where the base method used keyword parameters but
        the override method used position-only parameters.
-   [1.1.230](https://github.com/microsoft/pyright/releases/tag/1.1.230)
    -   Bug Fix: Fixed a bug that resulted in a false positive "reportMissingParameterType" error when using an old-style double underscore parameter name to indicate position-only parameter.
    -   Bug Fix: Handled the special case where an `Any` expression is bound to a ParamSpec giving it default parameters.
    -   Bug Fix: Fixed bug that resulted in a false positive error when using a dictionary unpack operator `**` with an instance of a class that satisfied the `SupportsKeysAndGetItem` protocol but did not directly derive from `Mapping`.
    -   Enhancement: Added new diagnostic check `reportUnusedExpression` to catch bugs like `a == 4` when `a = 4` was intended.
    -   Enhancement: Added special-case logic for a Type[T] (where T is an unbound TypeVar) that is instantiated through a call to its constructor. It should evaluate to T rather than Any.
    -   Bug Fix: Fixed bug in pattern exhaustive match logic that failed to detect exhaustive match when the subject expression was a unnarrowable expression form.
        ([pylance-release#2475](https://github.com/microsoft/pylance-release/issues/2475))
    -   Bug Fix: Improved the heuristics in the alias resolution logic to prefer declarations that are in non-exception paths even if the exception path has a typed decl and the non-exception decl must be inferred.
        ([pylance-release#2476](https://github.com/microsoft/pylance-release/issues/2476))
    -   Bug Fix: Fixed two bugs that generated false positive errors when using PEP 604 union syntax in an implicit type alias. The first bug affected the case where the union started with `None`. The second affected the case where a TypeVar was included in the union.
    -   Enhancement: Updated typeshed stubs to the latest.
    -   Bug Fix: Fixed bug that resulted in false positive reportIncompatibleVariableOverride error when one base class defined a symbol as a property and another base class defined a symbol as Any.
    -   Enhancement: Added support for the use of `Concatenate` as a type argument for a generic type alias that accepts a ParamSpec.
-   [1.1.229](https://github.com/microsoft/pyright/releases/tag/1.1.229)
    -   Bug Fix: Fixed a bug that caused semantic highlighting to sometimes skip information for certain tokens involved in member access expressions.
    -   Enhancement: Added checks for incompatible variable types for same-named instance or class variables in two base classes.
    -   Enhancement: Updated typeshed stubs to the latest version.
    -   Bug Fix: Fixed a bug that led to misleading type error messages and hover text when a type with an associated generic type alias was specialized. The underlying generic type was properly specialized, but the type alias itself appeared to be unspecialized still. Since the type alias is displayed in error messages and hover text, this was confusing.
    -   Bug Fix: Fixed a bug where classes that derive from `Any` are not allowed to be assigned to a TypeVar. This resulted in a false positive error when returning `NotImplemented` in a function that is annotated to return a TypeVar.
    -   Bug Fix: Fixed a bug that resulted in a false positive error "variable not in slots" when a value was assigned to a class variable that is a descriptor.
    -   Bug Fix: Fixed a bug in the `__post_init__` validation logic that resulted in a false positive when a dataclass with an `InitVar` derives from another dataclass with an `InitVar`.
    -   Enhancement: Added support for per-line suppression of diagnostics using `# pyright: ignore` comment. This also supports rule-specific suppression using a list of diagnostic rules, as in `# pyright: ignore [reportGeneralTypeIssues]`.
    -   Bug Fix: Fixed a bug in the reportUnnecessaryComparison diagnostic rule that resulted in false negatives when one of the two operands included a `None` in the type.
    -   Bug Fix: Fixed a bug that resulted in a false positive error when testing type compatibility of an invariant type argument that consists of a union of types, some of which are subtypes of each other.

## 2022.3.1 (9 March 2022)

Notable changes:

-   Enhancement: The bundled native module stubs for sklearn, scipy, and pandas have been updated.

In addition, Pylance's copy of Pyright has been updated from 1.1.226 to 1.1.228 including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Bug Fix: Improved solution to stack overflow and fixed another potential theoretical source based on code review.
-   [1.1.228](https://github.com/microsoft/pyright/releases/tag/1.1.228)
    -   Bug Fix: Improved "reportUnnecessaryComparison" diagnostic check so it catches more cases.
    -   Performance: Fixed performance bug that was causing a significant slowdown when evaluating highly nested call expressions especially when there are argument errors in the innermost expressions.
        ([pylance-release#2366](https://github.com/microsoft/pylance-release/issues/2366))
    -   Enhancement: Extended support for narrowing of index expressions to include those with negative subscripts, such as `a[-1]`. This is supported for all supported type guard patterns.
    -   Bug Fix: Fixed bug that resulted in a false positive error when using `typing.Self` in an inner function defined within an outer method.
    -   Enhancement: Added negative type narrowing support for sequence patterns in match statements.
    -   Bug Fix: Fixed a bug in negative type narrowing for class patterns in match statements when the class in the class pattern is one of the designated "special built-in classes" specified in PEP 634 and a class argument is specified.
    -   Bug Fix: Fixed a bug that resulted in incorrect TypeVar resolution when the TypeVar was used in a `Type[T]` type expression, was constrained, and two of the constraints overlapped in type.
    -   Bug Fix: Fixed an edge case in the code flow engine that theoretically could result in incorrect type evaluation.
    -   Bug Fix: Fixed a bug in the code flow engine that resulted in inconsistent type evaluation depending on order of evaluation in some cases where a variable is modified in a loop.
        ([pylance-release#2324](https://github.com/microsoft/pylance-release/issues/2324))
    -   Bug Fix: Fixed bug that resulted in a stack overflow when evaluating unions with large numbers of subtypes.
-   [1.1.227](https://github.com/microsoft/pyright/releases/tag/1.1.227)
    -   Enhancement: Extended conditional types to function and constructor calls where one or more arguments is a conditional type.
    -   Bug Fix: Fixed a bug that resulted in incorrect type inference when assigning `()` to a variable with an explicit type declaration of `tuple[()]`.
    -   Bug Fix: Fixed bug that results in incorrect type evaluation when an `if` statement is not paired with an `else` and the condition expression uses a `not` paired with an `and` or `or`.
    -   Bug Fix: Fixed bug that caused a class that derives from `NamedTuple` to not conform to the `Hashable` protocol.
    -   Behavior Change: Changed override detection to always use an overload implementation if present.
        ([pylance-release#2430](https://github.com/microsoft/pylance-release/issues/2430))
    -   Behavior Change: Fixed bug that caused symbols in unreachable code to be ignored in "Rename Symbol" and "Find all References" operations.
        ([pylance-release#2431](https://github.com/microsoft/pylance-release/issues/2431))
    -   Bug Fix: Fixed bug that resulted in a false positive when `cls` was used as an argument to a dynamic `type` creation call.
    -   Enhancement: Improved error message for overload that doesn't match its implementation.
    -   Bug Fix: Added code to avoid an attempt to analyze a function if its code flow complexity is too high. This reduces the likelihood of a stack overflow within the type evaluator. If a function or module is too complex, a diagnostic is now emitted to tell the developer that full analysis is suspended for that execution scope.
    -   Bug Fix: Improved reportIncompatibleMethodOverride diagnostic check, including fixes for a few false positives and false negatives and improvements to diagnostic messages.

## 2022.3.0 (3 March 2022)

Notable changes:

-   Enhancement: Django and SQLAlchemy stubs have been updated to their latest versions.
-   Enhancement: Pandas stubs updated.

In addition, Pylance's copy of Pyright has been updated from 1.1.225 to 1.1.226 including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Bug Fix: Extended conditional types to function and constructor calls where one or more arguments is a conditional type.
-   [1.1.226](https://github.com/microsoft/pyright/releases/tag/1.1.226)
    -   Bug Fix: Improved parser to detect extremely deep chains of call expressions that can crash the type evaluator.
    -   Bug Fix: Fixed bug that resulted in false positive error when detecting overlapping method overloads when the overloads use a class-scoped TypeVar.
    -   Bug Fix: Fixed a bug that resulted in a false positive error when validating type compatibility between two functions with nested Concatenate and ParamSpec usage.
    -   Bug Fix: Fixed a bug in the code flow graph relating to "with" statements that are nested within a "try" statement when the context manager does not swallow exceptions but instead forwards them to the outer except clause.
    -   Enhancement: Improved error message for binary and unary operations when an expected type (bidirectional inference) is present.
    -   Bug Fix: Fixed a performance issue that caused long analysis times for some code flow graphs that involve deeply nested loops and many interdependent variables.
    -   Bug Fix: Fixed a bug that resulted in a false positive error when assigning a value of type `type | Any` to type `type[T]`.
    -   Bug Fix: Fixed a bug that resulted in false positive errors when assigning a value to class variable that contains a generic descriptor object.
    -   Enhancement: Improved the error message for a call expression where a keyword argument and a positional argument target the same parameter.
    -   Enhancement: Updated typeshed stubs to the latest version.
-   [1.1.225](https://github.com/microsoft/pyright/releases/tag/1.1.225)
    -   Bug Fix: Added missing checks for an attempt to modify a variable that has been marked "Final" using a means other than a simple assignment statement. This includes augmented assignments, tuple assignments, for statements, with statements, assignment expressions, etc.
    -   Behavior Change: Modified parameter type inference logic to not infer a parameter's type based on the default argument value if the value is a tuple, list, set or dict.
    -   Enhancement: Improved type evaluation of `type(x)` to handle the case where `x` is a union type.
    -   Bug Fix: Fixed bug that caused false negative when a class defined a `__getattr__` method but no `__getitem__` method and a subscript expression was used with a class instance.
    -   Bug Fix: Fixed a bug in the logic that determines whether a class that derives from a protocol implements all of the functions and variables within that protocol. It wasn't considering mix-in classes.
    -   Bug Fix: Fixed regression in "finally" type analysis that allowed type violation errors to go unreported in finally clauses.
    -   Behavior Change: Changed the behavior of type evaluator when it encounters an unannotated symbol within a "py.typed" source file. Previously, it did not fall back on type inference and instead evaluated the type as "Unknown". It now falls back on type inference but internally marks the type as "ambiguous". Added logic to detect "likely ambiguous inferences".
    -   Behavior Change: Updated package type verifier to differentiate between "unknown" and "ambiguous" types.
    -   Bug Fix: Fixed a bug in type evaluator that resulted in a crash when a function signature contains a "\*\*" parameter with no name.
    -   Bug Fix: Fixed a bug that resulted in a crash due to infinite recursion.
    -   Bug Fix: Enhanced parser to detect extremely deep parse trees created from index or member access expressions. The parser now emits an error rather than allowing the type evaluator to crash (with a stack overflow) in such situations.
    -   Enhancement: Updated typeshed stubs to the latest.

## 2022.2.4 (23 February 2022)

Notable changes:

-   Enhancement: Several improvements in Pandas stubs (Thanks to @Dr-Irv and @sjdemartini)
-   Behavior Change: Changed `strictParameterNoneValue` to default to true rather than false. This reflects the updated guidance in PEP 484, which indicates that type checkers should not assume that a default argument of `None` should imply an `Optional` type.

In addition, Pylance's copy of Pyright has been updated from 1.1.222 to 1.1.224 including the following changes:

-   [1.1.224](https://github.com/microsoft/pyright/releases/tag/1.1.224)
    -   Bug Fix: Improved NoReturn return call inference when the callable type evaluates to a partial Any or Unknown.
    -   Bug Fix: Improved heuristics related to NoReturn detection when dealing with certain libraries that attempt to import another package within a `try` statement but provide a "dummy implementation" in an `except` clause. In this situation, we should use the declaration within the `try` block and ignore the one in the `except` clause. ([pylance-release#2402](https://github.com/microsoft/pylance-release/issues/2402))
    -   Bug Fix: Fixed buggy assert in type evaluator that resulted in some crashes.
    -   Behavior Change: Changed `strictParameterNoneValue` to default to true rather than false. This reflects the updated guidance in PEP 484, which indicates that type checkers should not assume that a default argument of `None` should imply an `Optional` type.
    -   Enhancement: If CLI version of pyright is run without providing arguments to certain commands, a failure is detected and reported. Thanks to Martin Fischer for this contribution.
    -   Bug Fix: Fixed performance regression due to a recent change in the code flow engine when attempting to evaluate whether call is a NoReturn.
    -   Enhancement: Added support for parameter type inference based on annotated base class method signatures and on default argument expressions.
    -   Bug Fix: Fixed recent regression that caused unnecessary reanalysis when closing a file when using pyright as an LSP. The regression also sometimes resulted in unexpected errors from reanalyzed files including diagnostics about unaccessed variables.
-   [1.1.223](https://github.com/microsoft/pyright/releases/tag/1.1.223)
    -   Bug Fix: Fixed a bug in negative type narrowing logic for value patterns in `match` statement.
    -   Behavior Change: Removed provisional support for PEP 677 (Alternate Call Syntax) because the proposal was rejected by the Python steering council.
    -   Bug Fix: Fixed a bug that led to incorrect type evaluation in the "implied else" code flow path.
    -   Bug Fix: Improved support for functions or methods that return a context manager that swallow exceptions, such as `pytest.raises`.
    -   Behavior Change: Modified `reportIncompatibleVariableOverride` check to permit a ClassVar in the base class to be overridden by a compatible class declaration in a child class.
    -   Bug Fix: Fixed a bug in the type evaluator that led to false positives when assigning a function type to another function type and the source contained parameters annotated with literal types and the dest contained corresponding parameters annotated with TypeVars.
    -   Bug Fix: Fixed bug in the handling of wildcard imports. If the target module doesn't contain a dunder all definition, the resulting imported symbol list should exclude names that start with a single underscore.
    -   Bug Fix: Fixed bug that resulted in a false positive error when using a TypeVarTuple in a `classmethod`.
    -   Behavior Change: Changed heap overflow detection to use a dynamic value based on available memory rather than a hard-coded size. For the pyright VS Code extension, changed the default "max heap size" from 1.7GB to 3.0GB on 32-bit systems. On 64-bit systems, this value appears to already be a higher value (4GB), and it doesn't appear to get overridden by the lower number.

## 2022.2.3 (16 February 2022)

Notable changes:

-   Bug Fix: Pandas stubs fixes.

In addition, Pylance's copy of Pyright has been updated from 1.1.220 to 1.1.222 including the following changes:

-   [1.1.222](https://github.com/microsoft/pyright/releases/tag/1.1.222)
    -   Bug Fix: Fixed bug that resulted in false positive when using a recursive type alias with a generic dataclass constructor.
    -   Bug Fix: Fixed a bug that results in a false negative when handling a function parameter that is annotated with a function-scoped TypeVar and has a default argument value.
    -   Behavior Change: Changed the handling of `reveal_type` so it participates in bidirectional type inference when used within a larger expression.
    -   Bug Fix: Fixed long-standing bug in logic that applies config file settings for diagnostic rule severity levels. The bug caused all settings overrides to be ignored if a pyrightconfig.json file was present. The new logic applies the default values, then the settings overrides, then the pyrightconfig.json file values. The change also simplifies the code, which was getting a bit unmaintainable.
    -   Enhancement: Extended `dataclass_transform` to support `transform_descriptor_types` parameter.
    -   Enhancement: Added support for an unpacked TypedDict as a type annotation for a `*kwargs` parameter.
    -   Bug Fix: Improved the `type(x) is y` type narrowing logic to handle the case where `y` is a TypeVar or Self type.
    -   Bug Fix: Fixed bug in match statement type narrowing. It wasn't properly handling the negative type narrowing case for class patterns when the subject expression was a bound TypeVar or Self type.
    -   Bug Fix: Fixed a bug related to the `__eq__` method (and other order methods) that are synthesized for a dataclass. The parameter name was incorrect. It should be `other`.
    -   Bug Fix: Added support for NFKC normalization of identifiers as specified in the Python lexical specification.
-   [1.1.221](https://github.com/microsoft/pyright/releases/tag/1.1.221)
    -   Behavior Change (from Pylance): Auto-exclude any folder under workspace starting with a period.
    -   Bug Fix: Fixed a bug in type narrowing for `match` statement. It was not properly handling `None` literal patterns when narrowing in the negative case.
    -   Bug Fix: Fixed bug that leads to a false positive error when using a class whose constructor doesn't contain any type annotations. Pyright treats such classes as though they are generic to help with inference of instance variables initialized in the constructor, but it shouldn't enforce the variance of the under-the-cover type variables.
    -   Bug Fix: Fixed bug that resulted in a false positive when evaluating certain list comprehensions where the subexpressions had interdependencies.
    -   Bug Fix: Fixed bug that resulted in a false positive error when evaluating type compatibility between two callables that included an `*args` parameter plus a set of keyword-only parameters. ([pylance-release#2370](https://github.com/microsoft/pylance-release/issues/2370))
    -   Enhancement: Updated typeshed stubs to the latest version.
    -   Enhancement: Added support for PEP 675 (arbitrary literal strings).
    -   Bug Fix: Added support for multiple unpack operators in a tuple list without parentheses when used in the RHS of a for statement. This was a grammar change introduced in Python 3.9. ([pylance-release#2371](https://github.com/microsoft/pylance-release/issues/2371))
    -   Enhancement: Improved completions for class member access when the member variable in a child class is unannotated but a parent class provides an annotation. In this case, we should use the type information from the annotated symbol.
    -   Behavior Change: Changed the behavior of the package type verifier so it does not flag unannotated class or instance variables if a parent class provides a type annotation for a variable of the same name. The type is inherited in this case. Also updated the library guidance to reflect this change.
    -   Bug Fix: Fixed bug that resulted in an incorrect type evaluation when handling a `namedtuple` call with a second parameter that is dynamic (not statically known).
    -   Enhancement: Improved support for `namedtuple` when the second argument is a tuple of string literals. It's more common to pass a list of string literals, but tuples should work as well.
    -   Bug Fix: Reverted a recent bug fix that caused significant performance degradations and crashes under some circumstances. ([pylance-release#2373](https://github.com/microsoft/pylance-release/issues/2373), [pylance-release#2387](https://github.com/microsoft/pylance-release/issues/2387), [pylance-release#2391](https://github.com/microsoft/pylance-release/issues/2391))
    -   Enhancement: Added special-case check for new callable syntax used within a quoted annotation passed as a bound or constraint argument to a TypeVar constructor.
    -   Bug Fix: Improved symbol resolution of module imports within the code flow engine when determining whether a context manager swallows exceptions or a callable returns NoReturn.
    -   Performance: Mitigated performance issue that results when doing a type compatibility check between two distinct recursive type aliases.
    -   Bug Fix: Fixed incorrect type evaluation when evaluating a constructor call with bidirectional type inference when the expected type is generic.
    -   Bug Fix: Fixed bug that resulted in incorrect type evaluation when a generic class with constrained type parameters was explicitly specialized with a subclass of one of the constrained types.

## 2022.2.2 (11 February 2022)

This release was not published.

## 2022.2.1 (9 February 2022)

Notable changes:

-   Performance: Only index workspaces that have open files. ([pylance-release#2270](https://github.com/microsoft/pylance-release/issues/2270))
-   Performance: Exclude folders whose names start with "." from indexing.
-   Performance: Delay indexing of libraries until 10 minutes after last edit.
-   Performance: Added partial seaborn stub.
-   Performance: Added colors API to matplotlib stub.

In addition, Pylance's copy of Pyright has been updated from 1.1.217 to 1.1.220 including the following changes:

-   [1.1.220](https://github.com/microsoft/pyright/releases/tag/1.1.220)
    -   Behavior Change: Changed the type narrowing logic for truthy and falsy conditions to exempt protocol classes.
    -   Bug Fix: Fixed bug that resulted in incorrect type evaluation of an `or` binary operator when the same expression was used in the LHS and RHS and was always truthy.
    -   Bug Fix: Fixed bug that resulted in the incorrect evaluation of a type resulting from a call to a constructor for an explicitly-specialized generic class in the case where that class implements neither a `__new__` nor an `__init__` method.
    -   Enhancement: Improved error message for descriptor and property setters.
    -   Bug Fix: Fixed a bug in PEP 646 unpacked tuple support where `*args` could not be annotated with `*tuple` type.
    -   Bug Fix: Fixed a false negative in the handling of dataclasses that contain fields with default orders before fields without default values in the case where an `__init__` is already defined on the class.
    -   Bug Fix: Fixed bug that results in false positive error when using a PEP 677 callable arrow syntax within a quoted type on Python 3.10 or older.
    -   Bug Fix: Fixed a bug in the code that prints types to text. It was not properly handling the case where a callable contains a synthesized \*args parameter with a type that isn't unpacked.
    -   Bug Fix: Fixed false negative where type annotations beginning with "\*" were not properly flagged as a syntax error.
    -   Improved support for matching of TypeVarTuple when used with \*args parameter.
    -   Bug Fix: Added missing check for a TypeVarTuple value that is not unpacked when passed as an argument.
-   [1.1.219](https://github.com/microsoft/pyright/releases/tag/1.1.219)
    -   Enhancement: Updated typeshed stubs to latest version.
    -   Bug Fix: Fixed a bug that results in a false positive error when using a `Self` return type for an `__aenter__` method.
    -   Bug Fix: Fixed false positive error when `P.args` or `P.kwargs` parameter type annotation is wrapped in `Annotated`.
    -   Bug Fix: Fixed bug that caused false negative when evaluating a recursive type alias involving a tuple.
    -   Bug Fix: Fixed a bug in the bidirectional type inference logic for list, set and dictionary expressions when that affected certain cases where the expected type contained a union.
    -   Bug Fix: Fixed bug that resulted in false negative when using a recursive type alias with dictionary, list or set expressions.
    -   Bug Fix: Fixed bug that resulted in the inappropriate generation of an Unknown type (and therefore false positive errors in strict mode) when using bidirectional type inference with a function that accepts a generic callable parameter.
    -   Bug Fix: Improved detection of NoReturn calls within code flow graph. In particular, the code now handles the case where the LHS of the call expression is a member access expression and the LHS of that expression is a local variable whose type needs to be inferred.
    -   Enhancement: Added better error handling and reporting for dataclass_transform.
    -   Bug Fix: Fixed bug that caused crash when handling bigint literal values.
    -   Bug Fix: Added missing check for a dataclass field that is declared with a default value in a base class but then overridden with one that doesn't include a default value in a child class. At runtime, it still acts as though it has a default value, which is inherited from the base class.
    -   Bug Fix: Fixed bug that prevented the "--verifytypes" feature from working with namespace packages.
    -   Bug Fix: Added missing check for improper use of `Unpack` when used in some contexts.
-   [1.1.218](https://github.com/microsoft/pyright/releases/tag/1.1.218)
    -   Enhancement: Allow "--watch" to be used in conjunction with "--outputjson" command-line options.
    -   Enhancement: Added support for bidirectional type inference for `yield` statements. The expected type is based on the first type argument in a `Generator` or `AsyncGenerator` return type annotation.
    -   Enhancement: Added the ability to add new symbols to `builtins` by simply adding a type stub file named `__builtins__.pyi` locally. ([pylance-release#1383](https://github.com/microsoft/pylance-release/issues/1383)), ([pylance-release#2103](https://github.com/microsoft/pylance-release/issues/2103))
    -   Bug Fix: Fixed a bug that led to a false positive error when handling bidirectional type inference for tuple expressions when the expected type was a union that contained multiple tuple subtypes.
    -   Bug Fix: Fixed a bug that resulted in a false negative when a list comprehension was used within a class body and referenced a class-scoped variable in a subexpression other than the first iterable. This also fixes a similar bug where a lambda was used within a class body and referenced a class-scoped variable in its return expression. These now property generate errors, reflecting the runtime behavior.
    -   Bug Fix: Fixed a bug that resulted in incorrect type inference for positional parameters used in class patterns if the corresponding class was defined in a "py.typed" library and it defined a `__match_args__` symbol with no annotation. ([pylance-release#2327](https://github.com/microsoft/pylance-release/issues/2327))
    -   Bug Fix: Fixed bug in stub generator that caused it to omit import statements with multi-part names (e.g. `import a.b.c`) even though there was a reference within the generated stub to the imported module.
    -   Enhancement: Extended type narrowing for class pattern matching so it supports narrowing in the negative case when arguments are present and when the pattern class is generic.
    -   Bug Fix: Fixed a bug that resulted in a false negative when a `*args` parameter was used in conjunction with a `*` keyword-only separator parameter. This generates a syntax error at runtime.
    -   Bug Fix: Fixed a false positive error when `TypeGuard` was used without a type argument in a runtime manner (outside of a type annotation).
    -   Bug Fix: Fixed recent regression that results in false positive errors detected in the `reportUnknownParameterType` diagnostic check when the function includes a parameter with a double underscore name indicating that it's positional-only.
    -   Enhancement: Improved signature help and hover text for synthesized `__init__` dataclass method when a parameter uses a field descriptor with a default value.

## 2022.2.0 (2 February 2022)

Notable changes:

-   Enhancement: Improve perf when python.analysis.indexing is on by only re-indexing user files that are directly changed. ([pylance-release#1368](https://github.com/microsoft/pylance-release/issues/1368))
-   Bug Fix: Fixed Pandas stubs to allow passing `NamedAgg` to `aggregate` and `agg`. ([pylance-release#2180](https://github.com/microsoft/pylance-release/issues/2180))

In addition, Pylance's copy of Pyright has been updated from 1.1.215 to 1.1.217 including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Enhancement: Added support for bidirectional type inference for `yield` statements.
    -   Enhancement: Allow `--watch` to be used in conjunction with `--outputjson` command-line options.
-   [1.1.217](https://github.com/microsoft/pyright/releases/tag/1.1.217)
    -   Bug Fix: Fixed a bug that resulted in a false positive error when passing an `*args` argument typed as an unpacked TypeVarTuple to a function that includes an unpacked TypeVarTuple parameter.
    -   Enhancement: Added special-case bidirectional type inference for the right operand of the "|" and "|=" operators (with an expected type based on the left operand). This supports the case where the left operand is a TypedDict and the right operand is a dict expression that conforms to the TypedDict type. ([pylance-release#2300](https://github.com/microsoft/pylance-release/issues/2300))
    -   Bug Fix: Fixed a bug in the reportIncompatibleMethodOverride check that resulted in false positive errors when both the base class and child methods have overloads but the base class does not have an - implementation and the child class does.
    -   Enhancement: Updated typeshed stubs to the latest version.
    -   Bug Fix: Fixed a bug that results in false positive errors when a `ClassVar` type declaration appears within an `Annotated`.
    -   Bug Fix: Added special-case handling of `Generic` base types to match the (undocumented) runtime behavior. Without this special-case handling, pyright reports that "a consistent method ordering cannot be found" in some cases where the runtime does not.
    -   Bug Fix: Fixed bug that is leading to some crashes that appear in the telemetry.
    -   Bug Fix: Added recursion detection for wildcard import lookups during code flow.
    -   Bug Fix: Fixed a bug that caused a type alias of `Any` to be evaluated as `Unknown` if defined within a py.typed library.
    -   Performance: Improved performance when analyzing types that involve some forms of recursive type aliases.
    -   Enhancement: Added support for typing_extensions.Never and typing.Never type and unified the underlying handling of Never and NoReturn, which are synonyms.
    -   Enhancement: Improved type stub generation code to emit definitions for TypeVar, TypeVarTuple, ParamSpec and NewType.
    -   Behavior Change: Changed heuristics for matching two union types when the destination union includes a combination of concrete types and one or more type variables. This case involves some heuristics in the constraint solver because multiple solutions are possible.
    -   Bug Fix: Fixed a bug that resulted in a false positive when assigning to a field in a dataclass that is annotated with a Callable type.
-   [1.1.216](https://github.com/microsoft/pyright/releases/tag/1.1.216)
    -   Bug Fix: Fixed recent regression that resulted in a crash (stack overflow) in the code flow engine.
    -   Bug Fix: Fixed a bug that resulted in unknown types in member access expressions to go unreported with `reportUnknownMemberType` was enabled. This occurred when the member access expression was located within a subscript of an index expression.
    -   Performance: Changed the logic that infers a NoReturn type to avoid inferring symbol types. This was causing a bunch of extra work to be performed in complex unannotated code bases like sklearn.
    -   Performance: Fixed performance issue in parser for deeply-nested parenthesized expressions. ([pylance-release#2299](https://github.com/microsoft/pylance-release/issues/2299))
    -   Bug Fix: Fixed bug in callable type compatibility logic. It was not properly handling some edge cases where a keyword parameter in the source and destination had an incompatible type if one or both of the types were specialized.
    -   Bug Fix: Fixed a bug that resulted in false positives when specializing a callback protocol with a TypeVarTuple when the callback protocol also contained one or more keyword parameters that were generic.
    -   Bug Fix: Fixed a bug in the protocol invariance checking logic. It wasn't properly handling protocols that used a TypeVarTuple as a type parameter that wasn't last (right-most) in the type parameter list.
    -   Behavior Change: Changed import resolution order to more closely match PEP 561. Typeshed stdlib type stubs are now resolved later in the import resolution process, after all local modules and modules within the python environment.

## 2022.1.5 (27 January 2022)

Notable changes:

-   Behavior Change: Changed folding of classes and functions to fold at the line containing the function or class name.
-   Enhancement: Updated to requied node 14 and vscode 1.63.1
-   Enhancement: Added new diagnostic check "reportMatchNotExhaustive" which reports cases where a `match` statement doesn't exhaustively cover all cases.
-   Enhancement: Added option to disable "Go to symbol in workspace"
    ([pylance-release#2236](https://github.com/microsoft/pylance-release/issues/2236))

In addition, Pylance's copy of Pyright has been updated from 1.1.213 to 1.1.215 including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Enhancement: Changed the logic that infers a NoReturn type to avoid inferring symbol types. This was causing a bunch of extra work to be performed in complex unannotated code bases like sklearn.
    -   Enhancement: Updated type inference documentation to eliminate a statement that was leading to some confusion.
    -   Bug Fix: Fixed a bug that resulted in unknown types in member access expressions to go unreported with `reportUnknownMemberType` was enabled. This occurred when the member access expression was located within a subscript of an index expression.
    -   Bug Fix: Fixed recent regression that resulted in a crash (stack overflow) in the code flow engine.
-   [1.1.215](https://github.com/microsoft/pyright/releases/tag/1.1.215)
    -   Bug Fix: Fixed bug that resulted in crash when extremely large integer literals are encountered.
        ([pylance-release#2279](https://github.com/microsoft/pylance-release/issues/2279))
    -   Bug Fix: Fixed bug that caused "extraPaths" specified for individual execution environment to be combined for all execution environments if a default "extraPaths" was also specified in the same config file.
    -   Bug Fix: Fixed handling of `NoReturn` type, which should act like `Never` in that both are considered "bottom types" and are assignable to any other type.
    -   Enhancement: Updated typeshed stubs to the latest.
    -   Enhancement: Added new diagnostic check "reportMatchNotExhaustive" which reports cases where a `match` statement doesn't exhaustively cover all cases.
    -   Enhancement: Added support for unpack operator for tuples used within type arguments. Support for this new syntax will appear in Python 3.11.
    -   Bug Fix: Added code in parser to detect obscenely deep parse subtrees containing binary and unary operations. These were sometimes leading to crashes in the binder and type evaluator. The parser now replaces them with error parse nodes and reports an error to the user.
    -   Bug Fix: Added recursion check in type guard logic to address stack overflow issue seen in telemetry.
    -   Bug Fix: Fixed bug that produces a false positive when attempting to assign a value of type `Type[NoneType]` to `Type[None]`. These are equivalent, so the assignment should be allowed.
    -   Enhancement: Enhanced parser to detect and report a runtime error that occurs when using a generator expression without surrounding parens as an argument within a call expression when more than one argument or a trailing comma is present.
    -   Bug Fix: Fixed a bug that resulted in a false positive when a member access expression targeted an attribute that was returned by a `__getattr__` method that returns a descriptor object. The old logic was binding the descriptor to the object, but that's inconsistent with the way things work at runtime.
        ([pylance-release#2282](https://github.com/microsoft/pylance-release/issues/2282))
    -   Enhancement: Improved analysis of `finally` block and the code that comes after the `finally` block so type narrowing performed within the `finally` block in the fall-through case is preserved.
    -   Enhancement: Added support for `Final` and `ClassVar` annotations embedded within `Annotated`. Runtime support has recently been added for this case.
    -   Enhancement: Added support for `InitVar` that is wrapped in `Annotated`. Support is being added for this in the runtime.
    -   Enhancement: Added special-case handling for methods declared as returning a `Generator`, `AsyncGenerator` or `AwaitableGenerator` that do not contain a yield statement. This special case applies only to methods declared in stub files, an abstract method, or a protocol definition with no code.
        ([pylance-release#2287](https://github.com/microsoft/pylance-release/issues/2287))
    -   Bug Fix: Improved support for custom subclasses of the builtin `property` class. Previously, the special-case handling in place for `property` were not handling these custom subclasses well, and this resulted in several false positive errors and incorrect type evaluations.
-   [1.1.214](https://github.com/microsoft/pyright/releases/tag/1.1.214)
    -   A regression was introduced in the 1.1.213 release that has the potential of impacting many pyright users, so I decided to do a quick update.
    -   Bug Fix: Reverted change from previous release that caused incorrect type evaluations and false positive errors in certain situations involving bidirectional type inference with call expressions.
    -   Enhancement: Updated typeshed stubs to latest.
-   [1.1.213](https://github.com/microsoft/pyright/releases/tag/1.1.213)
    -   Behavior Change: For not-required TypedDict fields, added a second synthesized overload for the two-parameter form of `get` that specifies the type of the second parameter is the same type as the field value. The other overload allows this second parameter to be of a different type.
    -   Bug Fix: Fixed bug that resulted in a false positive when accessing a field in a base class that provides a `__getattr__` method and is use in conjunction with another base class.
    -   Bug Fix: Fixed bug that resulted in crash due to infinite recursion.
    -   Bug Fix: Fixed a bug in the logic that detects duplicate enum members that resulted in a false positive when an enum class has other instance variables that are not enum members.
    -   Bug Fix: Added special-case handling for instance variables in a dataclass that are marked `Final`. Previously, these were flagged as an error because there was no explicit value assigned to them, but the synthesized `__init__` method implicitly initializes them.
    -   Enhancement: Added check for a class that derives from a protocol class where the protocol declares a method with an empty implementation, and the subclass doesn't provide a concrete implementation of the same-named method.
    -   Bug Fix: Fixed a bug that resulted in a false positive type evaluation error when using bidirectional type analysis for a call expression and the return type of the call contained a union of a TypeVar and another type and the expected type contained a union with at least one literal type.
    -   Bug Fix: Fixed bug that resulted in confusing error message when dataclass field was annotated with `Self` and then the class was subclassed.
    -   Enhancement: Improved the logic that handles instantiation of a custom metaclass when the name of the new class is passed as a string literal to the metaclass constructor.
    -   Enhancement: Improved the bidirectional type inference logic for lambdas to handle the case where one or more of the matching parameter types was a TypeVar.
    -   Bug Fix: Fixed a bug in the parser that resulted in a false negative when using an assignment expression (walrus operator) in the `if` clause of a list comprehension with no surrounding parentheses.
    -   Enhancement: Added support for bidirectional type inference when an `await` operator is used in an expression.
    -   Bug Fix: Fixed a bug in the logic that handles classes that are constructed from custom metaclasses.
    -   Enhancement: Added provisional support for the proposed "typing.reveal_type" call.

## 2022.1.3 (21 January 2022)

Notable changes:

-   Enhancement: Add folding for f-strings, dicts, and #regions.
-   Enhancement: Adding `"python.analysis.indexing"` to the config. Index installed third party libraries and user files for language features such as auto-import, add import, workspace symbols, etc.
    ([pylance-release#291](https://github.com/microsoft/pylance-release/issues/291))
    ([pylance-release#1288](https://github.com/microsoft/pylance-release/issues/1288))
    ([pylance-release#2261](https://github.com/microsoft/pylance-release/issues/2261))
-   Enhancement: Better support for docstrings on overload functions. example numpy.random.choice
    ([pylance-release#2243](https://github.com/microsoft/pylance-release/issues/2243))
-   Enhancement: Import completions no longer show builtin symbols
-   Enhancement: Implemented a new diagnostic check "reportMissingSuperCall" that checks for `__init__`, `__init_subclass__`, `__enter__` and `__exit__` methods that fail to call through to their parent classes' methods of the same name. This is a common source of bugs. The check is disabled by default. We may eventually enable it by default in strict mode, but we want to get feedback before doing so.

In addition, Pylance's copy of Pyright has been updated from 1.1.209 to 1.1.212 including the following changes:

-   Unreleased in Pyright, but included in Pylance:

    -   Bug Fix: Fixed bug that resulted in crash due to infinite recursion.
    -   Bug Fix: Fixed bug that resulted in a false positive when accessing a field in a base class that provides a `__getattr__` method and is use in conjunction with another base class.
        main
    -   Enhancement: For not-required TypedDict fields, added a second synthesized overload for the two-parameter form of `get` that specifies the type of the second parameter is the same type as the field value. The other overload allows this second parameter to be of a different type.
    -   Enhancement: Updated documentation to cover the new # pyright: basic comment.

-   [1.1.212](https://github.com/microsoft/pyright/releases/tag/1.1.212)
    -   Bug Fix: Fixed bug that resulted in false positive when one or more sources of types in TypeVar solving was unknown.
    -   Bug Fix: Fixed bug that resulted in a crash if a `TypedDict` class was derived from another `TypedDict` class and the base class had zero fields defined.
    -   Enhancement: Added support for `# pyright: basic` comment to enable basic type checking in a file.
    -   Bug Fix: Fixed a bug that resulted in a false positive error when determining whether method overrides for a multi-inheritance chain are compatible.
    -   Bug Fix: Fixed bug that resulted in a false positive when using bidirectional inference with a constructor with complex set of covariant, invariant, and contravariant type parameters.
    -   Enhancement: Improved logic for `type(x) is y` type narrowing pattern so it handles the case where `x` is `Any`.
        ([pylance-release#2896](https://github.com/microsoft/pylance-release/issues/2896))
-   [1.1.211](https://github.com/microsoft/pyright/releases/tag/1.1.211)
    -   Enhancement: Added support for very large integer literals (both in the tokenizer/parser and in the type system for Literals).
    -   Bug Fix: Fixed bug where call to async function that returns `NoReturn` was treated as a "no-return" function even though it wasn't awaited.
    -   Enhancement: Added check for class or instance variables that are declared but not assigned in a protocol class and not assigned in a concrete class that explicitly derives from the protocol class.
    -   Bug Fix: Fixed bug in type narrowing logic for `isinstance` calls where the input value includes a `Callable` and the class list includes a class that is not a runtime-checkable protocol class. In this case, the `Callable` should not be removed in the negative ("else") case even if the class defines a compatible `__call__` method.
    -   Bug Fix: Fixed bug that resulted in a false positive error when assigning a value to a TypedDict with not-required keys when that key had previously been assigned a literal value that narrowed the type.
    -   Behavior Change: Reverted recent change to TypedDict where the single-argument form of `get` was removed for not-required fields. This caused problems because there is a fallback overload that accepted this case still.
    -   Behavior Change: Changed `reportUnknownArgumentType` diagnostic check to be suppressed if the argument is an empty list or dict that comes from a `[]` or `{}` expression. While these types do technically contain `Unknown` type arguments, they are not unsafe, so reporting a diagnostic here is just noise.
    -   Behavior Change: Changed the implementation of `reveal_type` so it no longer returns a literal string type but now accepts optional keyword arguments `expected_text` and `expected_type`. The return type of `reveal_type` is now the same as the type of the first argument, making it consistent with mypy's implementation of `reveal_type`.
    -   Enhancement: Modified error messages for Required and NotRequired for clarity.
    -   Bug Fix: Fixed bug in parser that resulted in a false negative error when using an assignment expression within a subscript. This is allowed in the grammar as of Python 3.10.
    -   Enhancement: Updated typeshed stubs to the latest.
    -   Bug Fix: Fixed internal crash caused by infinite recursion.
    -   Bug Fix: Fixed bug that caused a crash in functools.partial special-case logic.
    -   Bug Fix: Fixed bug in type evaluation of index expressions that involve a recursive type alias in the subscript. Also improved text version of expanded types that include recursive type aliases.
-   [1.1.210](https://github.com/microsoft/pyright/releases/tag/1.1.210)
    -   Behavior Change: Removed support for two-argument form of `TypeGuard` including support for "type asserts". The feedback on this idea was relatively negative.
    -   Enhancement: Added provisional support for a proposed `StrictTypeGuard` feature. For details, refer to [this discussion](https://github.com/python/typing/discussions/1013).
    -   Enhancement: Added support for old-style (pre-await) coroutines.
    -   Bug Fix: Fixed a bug that resulted in a false positive in cases involving bidirectional type inference with an expected callable type where one or more of the parameter types was a tuple with non-literal element types and the provided argument was a tuple with a literal value.
    -   Bug Fix: Improved limit check for literal math.
    -   Enhancement: Updated typeshed stubs to the latest.
    -   Bug Fix: Fixed bug that results in false positive when using a `super().__init__` call within a metaclass `__init__` method.
    -   Bug Fix: Fixed bug that results in a false positive error when using `yield` within the outermost iterator of a list comprehension.
    -   Bug Fix: Fixed a bug that resulted in a false positive when importing `OrderedDict` from `typing_extensions`. Added a mechanism for loading typeshed modules on demand within the type evaluator, - Enhancement: Added improved checks for size mismatches when unpacking known-length iterables into a list target (like `[a, b] = (1, 2, 3)`).
    -   Behavior Change: Changed the `setdefault` method generated for TypedDict classes so it accepts only literal key values. Fixed a bug in the `get` method generated for TypedDict classes so it accepts arbitrary values for the default value parameter.
        ([pylance-release#2256](https://github.com/microsoft/pylance-release/issues/2256))
    -   Bug Fix: Fixed bug that resulted in incorrect type evaluation when using a generic type alias that consists of a union of multiple type variables that are filled with the same type when the type alias is specialized.
    -   Behavior Change: Modified the `reportMissingSuperCall` diagnostic based on feedback. It now emits an error for classes that include an `__init__` and don't call through to `super().__init__` even if that class derives from `object`, unless it's marked `@final`.
-   [1.1.209](https://github.com/microsoft/pyright/releases/tag/1.1.209)
    -   Enhancement: Added support for "literal math" for certain unary and binary operations where the operands are all the same literal class types (str, bytes, int, or bool). For example, `Literal[0, 1]` + `Literal[1, 2]` results in type `Literal1, 2, 3]`.
    -   Enhancement: Implemented a new diagnostic check "reportMissingSuperCall" that checks for `__init__`, `__init_subclass__`, `__enter__` and `__exit__` methods that fail to call through to their parent classes' methods of the same name. This is a common source of bugs. The check is disabled by default. We may eventually enable it by default in strict mode, but we want to get feedback before doing so.
    -   Behavior Change: Changed text output of CLI version to use the word "information" rather than "info" for consistency with JSON output.
    -   Bug Fix: Fixed bug that resulted in a crash if `Self` was used in a type argument within a method decorator.
    -   Behavior Change: Changed behavior to allow `Self` to appear within a `ClassVar` type.
    -   Bug Fix: Fixed bug that resulted in an incorrect type evaluation when `Self` was used as a return type annotation for a property or class property.

## 2022.1.1 (12 January 2022)

Notable changes:

-   Enhancement: Added LSP support for code folding ranges
    ([vscode-codebasics-folding](https://code.visualstudio.com/docs/editor/codebasics#_folding))
-   Enhancement: Added support for USERNAME and VIRTUAL_ENV shell variables in vscode settings.
    ([pylance-release#2221](https://github.com/microsoft/pylance-release/issues/2221))
-   Enhancement: Improved completion provider suggestions for static members.
    ([pylance-release#1318](https://github.com/microsoft/pylance-release/issues/1318))
-   Enhancement: "add import" suggestions now suggest exact matches with higher priority.
    ([pylance-release#297](https://github.com/microsoft/pylance-release/issues/297))
-   Enhancement: Improved override function completions around positional and keyword only parameters.
    ([pylance-release#711](https://github.com/microsoft/pylance-release/issues/711))
-   Behavior Change: Always enable stdlib indexing if possible. This will allow users to use 'auto import' and 'add import' in open single file mode.
    ([pylance-release#1765](https://github.com/microsoft/pylance-release/issues/1765))
-   Bug Fix: Pylance is not working on vscode.dev/github.dev.
    ([pylance-release#2235](https://github.com/microsoft/pylance-release/issues/2235))

In addition, Pylance's copy of Pyright has been updated from 1.1.205 to 1.1.208 including the following changes:

-   [1.1.208](https://github.com/microsoft/pyright/releases/tag/1.1.208)
    -   Enhancement (from pylance): Added support for USERNAME and VIRTUAL_ENV shell variables in ".env" file.
    -   Enhancement (from pylance): Improved completion provider suggestions for static members.
    -   Bug Fix: Reverted check for base classes that use variables. It was too disruptive, so another approach is needed.
-   [1.1.207](https://github.com/microsoft/pyright/releases/tag/1.1.207)
    -   Bug Fix: Fixed bug that results in false positive error when a function signature captured by a ParamSpec includes an \*args or \*\*kwargs parameter.
    -   Bug Fix: Fixed bug that resulted in false positive error and unclear error message with the reportIncompatibleMethodOverride check.
    -   Behavior Change: Changed type analysis of `def` statements to insert implicit `/` parameter (a position-only parameter separator) when one or more parameter names start with double underscores.
    -   Bug Fix: Fixed a bug that resulted in no error being emitted when an `await` keyword was used with a `Generator` object.
    -   Bug Fix: Fixed bug that resulted in false positive error when accessing a staticmethod or classmethod from a protocol class.
    -   Bug Fix: Fixed bug that prevented a file-level override of `reportUnnecessaryTypeIgnoreComment` from working correctly.
    -   Bug Fix: Fixed bug that resulted in a false positive error when adding a 'staticmethod' or 'classmethod' decorator to an already-decorated method.
    -   Enhancement: Updated typeshed stubs to latest.
    -   Enhancement: Improved check for index values for tuples to handle unions of tuples.
    -   Enhancement: Added new diagnostic check `reportInconsistentConstructor` that checks for inconsistent input signatures between `__new__` and `__init__` methods.
    -   Bug Fix: Added a check for base classes specified in a class declaration that is not a concrete class but instead a variable (dynamic) type.
-   [1.1.206](https://github.com/microsoft/pyright/releases/tag/1.1.206)
    -   Bug Fix: Fixed a bug in the logic that determines whether a call expression is a "NoReturn". In particular, the logic wasn't handling the case where the call was to the constructor of a class that had a custom metaclass that defined a `__call__` method.
        ([pylance-release#2224](https://github.com/microsoft/pylance-release/issues/2224))
    -   Bug Fix: Fixed regression that caused a false positive error when attempting to invoke constructor for a class derived from `ctypes.Structure`. This class uses a custom metaclass with a custom `__getattr__` method.
    -   Bug Fix: Updated heuristics in type variable constraint solver to better handle literals in the case where bidirectional type inference is being used.
    -   Enhancement: Updated `dataclass_transform` support so it applies to both metaclasses and base classes to conform to the latest version of the specification.
    -   Bug Fix: Fixed bug that resulted in false positive errors when dealing with protocol classes that referred to themselves internally.
    -   Bug Fix: Fixed bug in `reportIncompatibleMethodOverride` diagnostic check where it omitted an error if an overridden method had a decorator applied.
    -   Bug Fix: Fixed a bug in the type evaluation of the two-argument for of `super()` when the second argument is a class instance and the call is made from within a class or static method.
        ([pylance-release#2230](https://github.com/microsoft/pylance-release/issues/2230))
    -   Behavior Change: Added implied position-only parameter separator for `Concatenate` operator.
    -   Enhancement: Added new diagnostic check `reportUnnecessaryTypeIgnoreComment` that emits a diagnostic when a `# type: ignore` comment has no effect.
    -   Bug Fix: Fixed several bugs in type var constraint solver related to functions that have parameters that are callable that have parameters that are callable.
-   [1.1.205](https://github.com/microsoft/pyright/releases/tag/1.1.205)
    -   Enhancement: Improved type narrowing for `x.y == L` pattern to also support `x.y is L` if `L` is a `bool` or enum literal.
    -   Bug Fix: Fixed regression that resulted in a false positive error when assigning an empty tuple to a declared type that involved an unbounded tuple.
    -   Bug Fix: Fixed bug that causes a crash due to infinite recursion.
    -   Bug Fix: Fixed recent regression that resulted in a crash when using a zero-length tuple as a function argument.
    -   Bug Fix: Fixed bug that resulted in the first parameter of a local function declared within a method to be interpreted as a "self" parameter.
    -   Bug Fix: Fixed bug that resulted in a false positive when using a decorator that applies to a method and provides a type for the parameter corresponding to "self".
    -   Bug Fix: Fixed bug in tokenizer that resulted in a missing error when the first statement in a source file is preceded by whitespace.
    -   Enhancement: Updated typeshed stubs to latest.
    -   Bug Fix: Fixed bug that resulted in false positive error when a ParamSpec was bound to a generic function with some unresolved TypeVars.
    -   Behavior Change: Changed behavior of type alias declarations that use a generic class or alias in the RHS without any subscripts or unions. These are treated as unspecialized aliases, whereas they were previously specialized with `Any` type arguments.

## 2022.1.0 (5 January 2022)

Notable changes:

-   Enhancement: Improved untitled file support

In addition, Pylance's copy of Pyright has been updated from 1.1.196 to 1.1.204 including the following changes:

-   [1.1.204](https://github.com/microsoft/pyright/releases/tag/1.1.204)
    -   Behavior Change: Added special-cased handling for `__slots__` and `__class_getitem__` in protocol matching logic.
    -   Enhancement: Improved bidirectional type inference for lambdas with default argument values.
    -   Enhancement: Improved heuristics for when constraint solver should prefer literals over non-literals when solving a TypeVar in the case of bidirectional inference when assigning to a callable type.
    -   Enhancement: Added support for unpacking of tuples in type annotations (part of PEP 646).
    -   Bug Fix: Fixed bug that resulted in false positive error when a `Literal` was used within a Python-2 style type annotation comment.
    -   Enhancement: Updated typeshed stubs to the latest.
    -   Bug Fix: Fixed bug in "x is None" type guard logic. It wasn't preserving conditional types if x was a TypeVar.
    -   Bug Fix: Fixed bug that resulted in false positive error when a constrained TypeVar was checked against a particular constraint in an `isinstance` type guard.
    -   Bug Fix: Fixed a bug in the logic for assignment-based type narrowing that resulted in the wrong narrowed type if the declared type of the destination expression contained a union and the source contained a TypeVar.
-   [1.1.203](https://github.com/microsoft/pyright/releases/tag/1.1.203)
    -   Happy New Year everyone!
    -   Bug Fix: Fixed false positive error when `Optional` is used outside of a type annotation with no type arguments.
    -   Enhancement: Added provisional support for "asserting type guard functions", those that return a type of `TypeGuard[X, NoReturn]`.
    -   Enhancement: Added support for type narrowing in pattern classes based on the absence of an attribute (or a pattern mismatch of an attribute) if the class in question is marked `@final`.
    -   Behavior Change: Changed the behavior for wildcard imports when the target module defines `__all__` in a way that pyright cannot understand. Previously, the wildcard import didn't import any symbols in this case. Now, it imports all symbols from the target module.
    -   Enhancement: Added support for undocumented behavior of functools.partial whereby it allows keyword parameters to be overridden by the caller even though they are already supplied in the `partial` decorator.
    -   Behavior Change: Changed the reportImplicitStringConcatenation diagnostic check to not flag concatenated strings if they are contained within enclosing parentheses.
    -   Bug Fix: Fixed bug that caused `__hash__` function not to be synthesized for frozen pydantic models when using `dataclass_transform`.
    -   Enhancement: Enhanced the "aliased conditional" type narrowing capability to accommodate multiple assignments of the variable used within the aliased conditional as long as the variable isn't reassigned between the the aliased conditional assignment and the conditional check that uses the aliased value.
    -   Enhancement: Added support for `bool(x)` type guard.
    -   Bug Fix: Fixed several bugs that prevented type narrowing to work correctly when conditional expression included an assignment expression.
    -   Enhancement: Added check for member access expressions that access a member of a protocol class directly from the class. In this case, the member must be declared as a ClassVar.
    -   Enhancement: Improved "x in y" type narrowing logic to better handle literal types in the iterable value y.
    -   Behavior Change: Adjusted heuristics for assignment-based type narrowing. If the RHS type contains an unsolved TypeVar and the LHS (declared) type is concrete, do not apply type narrowing in this case.
    -   Bug Fix: Fixed bug that resulted in unreported type violation (false negative) when an inner function with a ParamSpec used a concatenated parameter but the outer function's return type did not.
    -   Enhancement: Added support for new type narrowing pattern: `len(x) == L` and `len(x) != L` where `x` is a tuple or union of tuples and `L` is a literal integer value.
-   [1.1.202](https://github.com/microsoft/pyright/releases/tag/1.1.202)
    -   Enhancement: Added check for class patterns for special builtin types (like int, float, etc.). These class patterns accept at most a single sub-pattern as an argument, and it must be positional.
    -   Bug Fix: Fixed type compatibility bug that allowed `Literal[1]` to be assignable to `type` when it should not be.
    -   Bug Fix: Fixed bug that caused "unnecessary isinstance" check to emit a false positive diagnostic when second argument was `Literal[1]`.
    -   Enhancement: Improved heuristics for determining preferred TypeVar match when matching against a union that includes a TypeVar.
    -   Enhancement: Added provisional support for two-argument form of TypeGuard to support negative narrowing cases.
    -   Bug Fix: Fixed bug in hover provider that caused docstrings not to appear for callable types that were generated from a callable with a ParamSpec.
    -   Bug Fix: Fixed a bug that resulted in a missing type error when a generic function returned a Callable type that used a TypeVar in its parameter types.
    -   Bug Fix: Fixed regression that resulted in a crash under certain circumstances where a `finally` clause was used in a generic function that used constrained TypeVars.
-   [1.1.201](https://github.com/microsoft/pyright/releases/tag/1.1.201)
    -   Enhancement: Added code to detect except clauses that are unreachable because their exception types are already handled by previous except clauses.
    -   Enhancement: Added type validation for custom metaclass keyword parameters specified in the metaclass's `__new__` method.
    -   Enhancement: Added type validation logic for dataclass `__post_init__` method.
    -   Bug Fix: Fixed bug that results in false positive error when class declaration arguments are evaluated out of order.
    -   Enhancement: Updated typeshed stubs to the latest version.
    -   Enhancement: Added support for `Required` and `NotRequired` type annotations in alternative syntax form of TypedDict.
    -   Behavior Change: Changed overload implementation consistency check so it doesn't require the implementation to include a `NoReturn` if one of the overload signatures returns a `NoReturn`.
    -   Bug Fix: Fixed a bug that resulted in a false positive in the overlapping overload check, specifically when a later overload used a type variable in a parameter annotation.
    -   Enhancement: Added type checking support for functools.total_ordering.
-   [1.1.200](https://github.com/microsoft/pyright/releases/tag/1.1.200)
    -   "The Christmas Edition"
    -   Enhancement: Added type checking support for functools.partial. This advanced support does not work with overloads or argument lists that include list or dictionary unpack operators.
    -   Bug Fix: Fixed a bug that resulted in a ParamSpec used within a generic function from becoming `Unknown` in some circumstances.
    -   Bug Fix: Fixed a bug that resulted in an incorrect specialized return type in certain cases involving ParamSpecs.
    -   Bug Fix: Fixed bug that can result in incorrect type evaluations when a keyword argument name is evaluated first when hovering over it.
    -   Behavior Change: Added special-case handling to accommodate assignment of a method that differs only in the Self parameter.
    -   Enhancement: Added logic to preserve function doc strings for a ParamSpec when it captures the signature of a function with a doc string. This is useful for decorators.
-   [1.1.199](https://github.com/microsoft/pyright/releases/tag/1.1.199)
    -   Bug Fix: Fixed bug that resulted in false positive error when class constructor is invoked with more than one argument and the class's metaclass has a custom `__call__` method.
    -   Enhancement: Updated typeshed stubs to the latest version.
    -   Bug Fix: Fixed recent regression that resulted in false positive when assigning a `Type[Proto]` to `Type[Proto]`.
    -   Enhancement: Added type checking for class constructor calls when the class has a metaclass with a custom `__call__` method.
    -   Bug Fix: Fixed a bug that resulted in an incorrect type inference when assigning to a list that includes an unpacked target variable.
    -   Enhancement: Improved handling of call expressions that have a `NoReturn` type. In particular, the logic now handles constructors, `__call__` methods, inferred symbol types, and symbol import chains.
    -   Bug Fix: Fixed bug that resulted in infinite recursion in certain cases when an aliased conditional expression was used.
    -   Bug Fix: Fixed bug in type evaluator that masked certain type errors when assigning a concrete type to a class TypeVar type.
    -   Bug Fix: Fixed bug that caused false positive when passing a generic function callback as an argument to another generic function.
-   [1.1.198](https://github.com/microsoft/pyright/releases/tag/1.1.198)
    -   Enhancement: Added support for exception group syntax introduced in PEP 654.
    -   Bug Fix: Fixed bug that resulted in false positive errors when using a TypeVar within the new callable syntax within a function declaration.
    -   Enhancement: Added missing check mandated by PEP 544, which disallows an assignment of a class type to a Type[Proto] if the class type is a protocol itself.
    -   Enhancement: Added support for class types that satisfy protocols. This is specifically allowed in PEP 544 in the section titled "Type[] and class objects vs protocols".
    -   Enhancement: Added support for assigning a param spec to a `...` signature, since the latter is the `Any` equivalent for ParamSpecs.
    -   Behavior Change: Changed type logic to allow `type` to be assigned to `Type[T]`. In this case, `type` is treated the same as `Type[Any]`, so `T` receives a value of `Any`.
    -   Enhancement: Added support for `__getattr__` and `__getattribute__` overloads that are typed with a literal str representing the attribute name.
    -   Bug Fix: Fixed bug in handling of callable syntax when a TypeVar, ParamSpec or TypeVarTuple was used outside of an appropriate scope. No error was emitted in this case.
    -   Bug Fix: Fixed a bug in the handling of the new callable syntax when it's used with an "async" keyword. The resulting return type should be `Awaitable` rather than `Coroutine`.
    -   Behavior Change: Changed the behavior of the new callable syntax to not accept `...` with other parameters. After further discussion on the typing-sig, the consensus is that supporting this will cause confusion.
    -   Bug Fix: Fixed a false negative (missing) error when a method within a generic class was annotated to return a generic type of itself.
    -   Enhancement: Added logic to handle the case where a declared return type of a function includes a constrained TypeVar and a return statement is guarded by a conditional check that guarantees that the constraint is met on that code path.
    -   Enhancement: Improved error message (and reduced cascading errors) for the case where a variable is incorrectly used as the LHS of a subscript expression within a type annotation.
-   [1.1.197](https://github.com/microsoft/pyright/releases/tag/1.1.197)
    -   Bug Fix: Fixed bug in type narrowing code for literal enums. It wasn't correctly handling the edge case where the enum class has no enumerated members.
    -   Bug Fix: Fixed bug in type narrowing logic for comparisons to literals that involve enums declared in a type stub. It was incorrectly narrowing the type to `Never` in the negative (else) case.
    -   Bug Fix: Fixed bug in type evaluator that resulted in incomplete (Unknown) types when variable types depend on each other within a loop and one of the expressions involves an unpack operator.
    -   Bug Fix: Fixed bug in protocol TypeVar variance validation. Thanks to @Azureblade3808 for this contribution.
    -   Enhancement: Added support for ellipsis type argument for a generic alias that uses a ParamSpec.
    -   Bug Fix: Fixed bug that caused false positives when assigning a function to a generic class or callback protocol that is parameterized with a ParamSpec that is specialized using an ellipsis.
    -   Bug Fix: Fixed several bugs where `Type[None]` was incorrectly treated as compatible with `None` and vice versa.
    -   Bug Fix: Fixed bug that resulted in a false positive error when `Required` or `NotRequired` special forms were used with no type arguments in contexts where they are used as runtime class names rather than type annotations.
    -   Behavior Change: Changed text representation of callables to more closely match the syntax introduced in PEP 677 including the use of "..." to represent "any parameters" and "\*\*P" to represent a ParamSpec.
    -   Bug Fix: Fixed error in pyrightconfig JSON schema, which duplicated a couple of IDs.
    -   Bug Fix: Fixed bug that caused crash in type analyzer when a TypeVar of the same name was declared twice in the same scope with constraints in one case and without in the other.
    -   Enhancement: Added support for draft PEP 677: callable type syntax.
-   [1.1.196](https://github.com/microsoft/pyright/releases/tag/1.1.196)
    -   Enhancement: Added support for Python 3.11 StrEnum.
    -   Behavior Change: Modified behavior for assignment-based type narrowing when the target of the assignment references an "asymmetric" descriptor or property, one where the setter accepts a different value type than the getter returns. When this is detected, assignment-based type narrowing is no longer applied.
    -   Behavior Change: Changed class pattern matching behavior to support narrowing of `Any` or `Unknown`, exempting this case from the general "never narrow Any" rule.
    -   Behavior Change: Modified behavior of overload matching when unpacked argument is present and the unpacked iterator is a type that doesn't provide any length information. In this case, overload matching will prefer an overload that includes a `*args` parameter rather than individual positional parameters.
    -   Enhancement: Added check for a module used as a type annotation, which is not permitted.
    -   Enhancement: Improved `isinstance` type narrowing logic to retain type arguments in cases where the corresponding type parameter is bound or constrained.
    -   Bug Fix: Fixed bug that resulted in a false positive error indicating that an overload isn't compatible with its implementation when the overload includes a callable parameter with a type variable as a parameter.
    -   Bug Fix: Fixed a bug in type evaluation of a `Final` class variable that has no explicit type but is assigned a literal value.
    -   Bug Fix: Fixed a bug that resulted in incorrect type evaluations when a generic class using a ParamSpec was explicitly specialized using a `Concatenate` in the type argument, as in `A[Concatenate[int, P]]`.
    -   Bug Fix: Fixed a bug that resulted in incorrect type resolution when evaluating mutually-dependent variables within a loop where one of the expressions involved a call to a constructor with an unpacked argument.
    -   Bug Fix: Fixed false positive error with reportUnnecessaryIsInstance diagnostic check with the provided class is dynamic.

## 2021.12.2 (13 December 2021)

Notable changes:

-   Bug Fix: Fixed false positive when using a generic type alias that refers to a class with a `__getitem__` method.
    ([pylance-release#2161](https://github.com/microsoft/pylance-release/issues/2161))
    ([pylance-release#2169](https://github.com/microsoft/pylance-release/issues/2169))

In addition, Pylance's copy of Pyright has been updated from 1.1.194 to 1.1.195 including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Behavior Change: Changed class pattern matching behavior to support narrowing of Any or `Unknown`, exempting this case from the general "never narrow Any" rule.
    -   Behavior Change: Modified behavior for assignment-based type narrowing when the target of the assignment references an "asymmetric" descriptor or property, one where the setter accepts a different value type than the getter returns. When this is detected, assignment-based type narrowing is no longer applied.
    -   Enhancement: Added support for Python 3.11 StrEnum.
-   [1.1.195](https://github.com/microsoft/pyright/releases/tag/1.1.195)
    -   Bug Fix: Fixed bug in handling of `__slots__`. Entries listed in `__slots__` apply only to instance variables, not to class variables.
    -   Bug Fix: Fixed false positive error with reportUnnecessaryComparison diagnostic rule when one of the two operands is `type` or `Type[Any]` and the other is a class.
    -   Bug Fix: Fixed false positive when using a generic type alias that refers to a class with a `__getitem__` method.
        ([pylance-release#2161](https://github.com/microsoft/pylance-release/issues/2161))
        ([pylance-release#2169](https://github.com/microsoft/pylance-release/issues/2169))
    -   Enhancement: Implemented support for type guards that based on "aliased conditional expressions". For details and examples, refer to https://github.com/microsoft/pyright/blob/main/docs/type-concepts.md#aliased-conditional-expression.
    -   Bug Fix: Fixed a bug that caused a false positive error under certain circumstances where a function return type annotation referred to a forward-declared symbol and `from __future__ import annotations` was in effect.
        ([pylance-release#2157](https://github.com/microsoft/pylance-release/issues/2157))
    -   Enhancement: Added error for an attempt to call a module, which generates an exception at runtime.
    -   Bug Fix: Fixed bug related to ParamSpec specialization when the signature has zero parameters.
    -   Behavior Change: Changed type completeness report (the "--verifytypes" feature) to exempt symbols that derive from "**slots**" entries.
    -   Enhancement: Improved `isinstance` type narrowing when the original type is a generic class with a TypeVar as a type argument and the second argument to `isinstance` is a generic subclass of the original type. The type argument is now properly retained.

## 2021.12.1 (9 December 2021)

Notable changes:

-   Pylance now supports smart selection (shift + alt + rightArrow/leftArrow)
-   Pylance's copy of typeshed has been updated.
-   The bundled stubs for django have been updated.

In addition, Pylance's copy of Pyright has been updated from 1.1.192 to 1.1.194 including the following changes:

-   [1.1.194](https://github.com/microsoft/pyright/releases/tag/1.1.194)
    -   Bug Fix: Fixed inconsistency in definition provider where it would sometimes fail to go to a declaration if the symbol was not re-exported from a type stub or "py.typed" module.
    -   Enhancement: Added support for explicit specialization of generic type aliases that include a ParamSpec.
    -   Bug Fix: Fixed bug that resulted in the import resolution paths retrieved from the currently-selected Python interpreter to omit the working directory if it happens to be in the "sys.path" list.
    -   Bug Fix: Fixed bug in specialization of callable type where the return type includes the expansion (unpacking) of a variadic type variable.
    -   Enhancement: Improved handling of `x in y` type guard to handle the case where `y` is a tuple.
    -   Bug Fix: Fixed a bug that caused type narrowing to fail in certain cases when the "X in Y" type guard pattern was used.
    -   Bug Fix: Fixed bug that resulted in false positive when a variable was modified in a loop that employed conditional type narrowing and was also used as a member access expression.
    -   Bug Fix: Fixed a bug whereby an explicit TypeAlias definition that includes a generic type with no explicit type arguments was not assuming `Unknown` for those type arguments. For example, `A: TypeAlias = list` should assume that `A` is equivalent to `list[Unknown]`.
    -   Enhancement: Added a missing diagnostic for an attempt to specialize a class that has already been specialized. This can occur in the case of a type alias, such as `A = list[int], A[int]`.
    -   Enhancement: Added code to support `__qualname__` in class definitions.
    -   Bug Fix: PEP 484 indicates that `Type[Any]` should be interpreted as equivalent to `type`, but the previous code was treating it as `Any`.
    -   Enhancement: Added error check for the use of a generic class as a metaclass.
    -   Bug Fix: Fixed a bug that resulted in a false positive error when a dictionary literal was passed to a constructor of a generic subclass of dict.
-   [1.1.193](https://github.com/microsoft/pyright/releases/tag/1.1.193)
    -   Bug Fix: Fixed incorrect type evaluation for symbols that are modified within a context manager block that is nested within a try/except statement.
    -   Enhancement: Updated to the latest typeshed stubs. Note that type stubs for several third-party packages were recently removed from typeshed: click, flask, jinja2, markupsafe, werkzeug.
    -   Bug Fix: Fixed bug that resulted in "unknown" type evaluation for variables assigned in a loop using a tuple assignment pattern.
        ([pylance-release#2140](https://github.com/microsoft/pylance-release/issues/2140))
    -   Bug Fix: Fixed bug in TypeVar solver where Self type was being incorrectly replaced with its concrete form in some cases.
    -   Bug Fix: Fixed bug that resulted in TypeVar not being solved in some circumstances involving recursive types.
    -   Bug Fix: Fixed a bug in the handling of generic classes whose implementation includes another instantiation of itself using the original type parameters as type arguments for the nested instantiation.
    -   Bug Fix: Fixed a bug in the handling of generic classes whose implementation includes another instantiation of itself using the original type parameters as type arguments for the nested instantiation.
    -   Enhancement: Enhanced reportIncompatibleMethodOverride diagnostic check to also detect incompatible methods defined by two classes that are used as base classes in a multiple-inheritance derived class.
-   [1.1.192](https://github.com/microsoft/pyright/releases/tag/1.1.192)
    -   Enhancement: Sped up "find reference" by performing a quick text search for the reference symbol and avoiding additional work for that file if there is no chance of finding a reference within it.
    -   Bug Fix: Fixed misleading error message involving a type mismatch within the TypeVar constraint solver. The source and destination types were reversed.
    -   Bug Fix: Fixed a bug in ternary expression type evaluation that resulted in a false positive error. It was not properly handling the case where the condition was statically determined to be false or true.
    -   Enhancement: Improved error message for unknown or partially-unknown type arguments in package type verifier.
    -   Bug Fix: Added missing check in package type verifier for generic type aliases with missing type arguments.
    -   Bug Fix: Fixed bug that resulted in false positive error when a `__new__` method has its own type variables that are not scoped to its corresponding class.
    -   Bug Fix: Changed behavior of symbol resolution involving a quoted (forward-declared) type annotation that references a symbol in the global (module) or builtins namespaces. The previous implementation didn't match the runtime behavior of `typing.get_type_hints`.
    -   Bug Fix: Improved heuristics that are intended to choose the simplest type when more than one solution is possible for a set of type variables.
    -   Enhancement: Added support for class-based definition of "NewType", which will appear in a new version of typeshed stubs soon.
    -   Bug Fix: Added missing check in function type compatibility checks for the case where the source type contains position-only parameters but the destination type does not.
    -   Bug Fix: Added support for synthesized `__hash__` method for dataclass and dataclass_transform.
    -   Bug Fix: Fixed bug that resulted in false positive parse error when using "/" parameter in type stub when pythonVersion was prior to Python 3.8.

## 2021.12.0 (2 December 2021)

Notable changes:

-   Pylance now supports Go to Type Definition.
-   Performance of Find All References and Rename Symbol has been improved for large workspaces.
    ([pylance-release#2109](https://github.com/microsoft/pylance-release/issues/2109))
-   Pylance's copy of typeshed has been updated.
-   The bundled stubs for django have been updated.

In addition, Pylance's copy of Pyright has been updated from 1.1.188 to 1.1.191 including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Enhancement: Improved heuristics that are intended to choose the simplest type when more than one solution is possible for a set of type variables.
    -   Bug Fix: Fixed regression introduced in previous check-in related to type stubs that use symbol names that overlap with builtins symbols.
    -   Behavior Change: Modified symbol resolution involving a quoted (forward-declared) type annotation that references a symbol in the global (module) or builtins namespaces. The previous implementation didn't match the runtime behavior of `typing.get_type_hints`.
    -   Bug Fix: Fixed bug that resulted in false positive error when a `__new__` method has its own type variables that are not scoped to its corresponding class.
    -   Enhancement: Updated command-line documentation for consistency.
-   [1.1.191](https://github.com/microsoft/pyright/releases/tag/1.1.191)
    -   Bug Fix: Fixed bug in synthesized `__match_args__` type for dataclass, which shouldn't include any keyword-only fields. Thanks to @HKGx for this contribution.
    -   Bug Fix: Added special-casing to suppress "partially unknown type" diagnostic within member access expressions when they are used to access non-specialized generic classes within an argument expression. There are legitimate uses of partially unknown types in this case (e.g. in "isinstance" calls).
    -   Behavior Change: Exempted class symbol `__weakref__` from type completeness check since its type is well defined by the Python spec.
    -   Behavior Change: Changed reportPropertyTypeMismatch to be disabled by default in all diagnostic modes.
    -   Bug Fix: Fixed a hole in the check for partially-unknown types. Generic type aliases that are not specialized or are partially specialized (i.e. only some type arguments are specified) should trigger this check.
    -   Bug Fix: Fixed bug that resulted in a false positive error when using class pattern matching with type variables.
    -   Bug Fix: Fixed bug in "--ignoreexternal" mode of "--verifytypes" feature. It was not properly flagging errors when the type was external (and known) but the type arguments were partially unknown.
    -   Enhancement: Enhanced truthy/falsy type narrowing pattern to handle classes that contain a `__bool__` method that always returns True or False.
    -   Enhancement: Changed parse error messages related to unclosed parentheses, braces and brackets so they are reported at the location of the starting token to better match the new Python 3.10 parse error reporting behavior.
        ([pylance-release#2118](https://github.com/microsoft/pylance-release/issues/2118))
-   [1.1.190](https://github.com/microsoft/pyright/releases/tag/1.1.190)
    -   Bug Fix: Fixed bug that caused false positive when evaluating type compatibility between two TypedDict types that are structurally the same but have different declarations. PEP 589 indicates that these should be treated as compatible types.
    -   Bug Fix: In the case where a type annotation is an illegal form (e.g. a variable or a function), the annotation should evaluate to an Unknown type.
    -   Enhancement: Added support for async functions that return `NoReturn` type.
    -   Bug Fix: Fixed bug that prevented error when a generator function returned an inappropriate type if that type was a subclass of `Iterable`.
        ([pylance-release#2127](https://github.com/microsoft/pylance-release/issues/2127))
    -   Bug Fix: Fixed bug that resulted in unreported Unknown type in strict mode when the type was evaluated as part of a call to an overloaded function in some circumstances.
    -   Enhancement: Updated typeshed stubs to the latest.
    -   Bug Fix: Improved check for inconsistent use of tabs and spaces to catch a previously-unreported case that generates runtime errors.
    -   Bug Fix: Added a type consistency check for TypedDicts which are otherwise compatible except that one is marked @final and the other is not.
    -   Behavior Change: Changed reportUnusedVariable diagnostic check to exempt variables whose names begin with an underscore.
    -   Behavior Change: Changed logic that determines whether a function should be exempt from return type consistency checks. If a function or method contains only a docstring but no `...`, it is no longer exempt (unless it is an `@overload`). ([pylance-release#2111](https://github.com/microsoft/pylance-release/issues/2111))
-   [1.1.189](https://github.com/microsoft/pyright/releases/tag/1.1.189)
    -   Bug Fix: Fixed regression relating to type inference for non-generic classes that have unannotated constructors (so-called "pseudo-generic classes").
    -   Bug Fix: Fixed crash that occurred when specializing a class with a TypeVarTuple and failing to provide a type argument for the TypeVarTuple type parameter.
    -   Bug Fix: Fixed recent regression in import resolver that caused a local import to no longer be preferred over an installed module by the same name.
    -   Bug Fix: Fixed bug that caused incorrect type evaluation of parameter with implied Optional type based on `None` default argument value when `strictParameterNoneValue` setting is false.
        ([pylance-release#2091](https://github.com/microsoft/pylance-release/issues/2091))
    -   Enhancement: Added checks for illegal forms of `Literal` type arguments.
    -   Bug Fix: Fixed false positive error when using a union type expression in an `isinstance` or `issubclass` call on Python 3.10.
    -   Bug Fix: Fixed bug in code flow engine that caused incorrect determination of node reachability in cases where an unannotated function recursively called itself.
    -   Bug Fix: Fixed a hole in the type checking logic for TypedDict classes. It was not properly handling the invariant case.
    -   Behavior Change: Made illegal assignment target checks unconditional so they are not gated by reportGeneralTypeIssues. These should be treated more like parse errors than type checking errors.
-   [1.1.188](https://github.com/microsoft/pyright/releases/tag/1.1.188)
    -   Bug Fix: Fixed issue that caused import resolution failures for certain submodules of `google.cloud`.
    -   Bug Fix: Fixed crash in completion provider.
    -   Bug Fix: Fixed bug in ParamSpec type evaluation that caused a false positive error when assigning a callable with a `Concatenate` to another `ParamSpec`.
    -   Bug Fix: Fixed bug in ParamSpec logic that resulted in false positive when a TypeVar was used as within a Concatenate expression.
    -   Bug Fix: Fixed bug in type evaluator that resulted in false positive error in strict mode. Type of call argument expression was incorrectly reported as partially unknown in some cases.
    -   Bug Fix: Fixed bug that resulted in a false positive when a tuple with known element types is used as an unpacked argument in a call to a function that uses position-only parameters.
        ([pylance-release#2083](https://github.com/microsoft/pylance-release/issues/2083))
    -   Bug Fix: Fixed type checking hole (false negative) in certain circumstances involving loop constructs and variables whose types are modified within these loops. This bug fix also has a positive performance impact when analyzing functions with complex code flow graphs.
        ([pylance-release#1979](https://github.com/microsoft/pylance-release/issues/1979))
    -   Bug Fix: Fixed issue that caused CLI version of pyright to use incorrect Python interpreter to discover the Python version when no "pythonVersion" configuration setting was supplied.
    -   Enhancement: Implemented diagnostic check for a `ClassVar` declaration that uses a type variable. PEP 526 explicitly states that this is not allowed.

## 2021.11.2 (17 November 2021)

Notable changes:

    -   Intellicode context now includes collections.
    -   Pylance's copy of typeshed has been updated.
    -   The bundled stubs have been updated.

In addition, Pylance's copy of Pyright has been updated from 1.1.186 to 1.1.187 including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Bug Fix: Fixed bug in type evaluator that resulted in false positive error in strict mode. Type of call argument expression was incorrectly reported as partially unknown in some cases.
    -   Bug Fix: Fixed style issue.
    -   Bug Fix: Fixed bug in ParamSpec logic that resulted in false positive when a TypeVar was used as within a Concatenate expression.
    -   Bug Fix: Fixed bug in ParamSpec type evaluation that caused a false positive error when assigning a callable with a `Concatenate` to another `ParamSpec`.
    -   Bug Fix: Fixed crash in completion provider.
    -   Bug Fix: Fixed issue that caused import resolution failures for certain submodules of `google.cloud`.
-   [1.1.187](https://github.com/microsoft/pyright/releases/tag/1.1.187)
    -   Bug Fix: Fixed false positive error when assigning type `T | Any` to type `T`.
        ([pylance-release#2054](https://github.com/microsoft/pylance-release/issues/2054))
    -   Behavior Change: Changed `Callable` special form to include a position-only marker at the end of the parameter list. Changed type printer to omit the `/` if it is unnecessary.
    -   Behavior Change: Modified the check for function declaration redefinitions to allow for same-signature overrides in cases where the declarations are not within the same statement suite (e.g. one in the "if" and the other in the "else" block).
    -   Bug Fix: Fixed missing diagnostic when a Self parameter was assigned to a `Concatenate[X, P]` where `X` is a type that is incompatible with `Self`.
    -   Bug Fix: Fixed bug that resulted in a false positive error when a specialized generic class with a `__call__` method uses a ParamSpec and is assigned to a `Callable` that is also parameterized with a ParamSpec.
    -   Enhancement: Updated typeshed stubs to the latest.
    -   Bug Fix: Fixed bug that resulted in hover text for symbols used within a default argument expression to sometimes be displayed as "Unknown".
        ([pylance-release#2064](https://github.com/microsoft/pylance-release/issues/2064))
    -   Bug Fix: Fixed regression in handling of callback protocols that define a `__name__` attribute, which is common to all functions.
    -   Behavior Change: Added support for upcoming change in typing.pyi in the way that the `NoReturn` symbol is declared.

## 2021.11.1 (10 November 2021)

Notable changes:

-   Bug fix: Fixed semantic token bug involving file opened and closed repeatedly in a short period times.

In addition, Pylance's copy of Pyright has been updated from 1.1.185 to 1.1.186 including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Bug Fix: Fixed missing diagnostic when a Self parameter was assigned to a `Concatenate[X, P]` where `X` is a type that is incompatible with `Self`.
    -   Enhancement: Modified the check for function declaration redefinitions to allow for same-signature overrides in cases where the declarations are not within the same statement suite (e.g. one in the "if" and the other in the "else" block).
    -   Enhancement: Changed isTypeSame function to handle functions whose signatures include position-only parameters. Also added support for inferred return types and eliminated the check for declaration parity. This allows two function types to be deemed the same even if they originate from different declarations.
    -   Enhancement: Changed Callable special form to include a position-only marker at the end of the parameter list. Changed type printer to omit the `/` if it is unnecessary.
    -   Bug Fix: Fixed false positive error when assigning type T | Any to type T. ([pylance-release#2054](https://github.com/microsoft/pylance-release/issues/2054))
-   [1.1.186](https://github.com/microsoft/pyright/releases/tag/1.1.186)
    -   Enhancement: Added checks for incorrect runtime usage of a UnionType object.
    -   Enhancement: Added more complete type checks involving the use of a default argument for a generic parameter in a constructor.
    -   Bug Fix: Fixed a bug that resulted in a false positive error when accessing members from a `type` instance or a `Type[T]`.
    -   Bug Fix: Fixed false positive error related to heuristics employed in bidirectional type inference for calls when the expected type comprises a union and the return type of the call is a union that includes Any and a type variable.
    -   Enhancement: Added support for `slots` parameter to dataclass, a new feature added in Python 3.10.
    -   Bug Fix: Fixed regression that caused a false positive error related to incorrect usage of a type variable within a type alias definition.
    -   Bug Fix: Fixed incorrect handling of client-initiated progress reporting for "onReferences" and "onExecuteCommand" handlers in language server.
-   [1.1.185](https://github.com/microsoft/pyright/releases/tag/1.1.185)
    -   Bug Fix: Fixed bug in completion provider where it was not properly handling binding to classes, which left parameter types unspecialized in some cases. It was already properly handling binding to objects (class instances), so this was a straightforward extension.
    -   Enhancement: Added support in completion provide for enum members. They are now properly identified as such and prioritized higher in the completion list than other non-member symbols. ([pylance-release#1977](https://github.com/microsoft/pylance-release/issues/1977))
    -   Enhancement: Improved readability of diagnostic message for type mismatch when assigning to a tuple expression. ([pylance-release#2020](https://github.com/microsoft/pylance-release/issues/2020))
    -   Bug Fix: Fixed a bug in the handling of `reveal_type` that caused hover text within the argument to be displayed as `Unknown` in some circumstances. ([pylance-release#2024](https://github.com/microsoft/pylance-release/issues/2024))
    -   Enhancement: Added special-case support for the `__self__` attribute of a bound method.
    -   Bug Fix: Fixed bug that resulted in stack overflow.
    -   Bug Fix: Fixed bug in stub generation code that resulted in an error if a stub was requested for a submodule in a package that includes an `__init__.py` file in the same directory as the submodule source file. ([pylance-release#2013](https://github.com/microsoft/pylance-release/issues/2013))
    -   Enhancement: Improved signature help for the constructor of classes that define a `__new__` method but no `__init__` method, such as the `zip` class. The previous logic was always preferring the `__init__`, which is supplied by the `object` class, which all classes derive from. ([pylance-release#1912](https://github.com/microsoft/pylance-release/issues/1912))
    -   Bug Fix: Fixed a bug that resulted in a false positive error when assigning one ParamSpec to another ParamSpec.
    -   Bug Fix: Fixed bug that resulted in false positive "reportUnknownMemberType" error when using a generic class within a class pattern.
    -   Bug Fix: Added missing diagnostic check for illegal type argument lists that include a ParamSpec when the type parameter list includes a ParamSpec.
    -   Enhancement: Added missing keyword "with" from completion provider. ([pylance-release#2042](https://github.com/microsoft/pylance-release/issues/2042))
    -   Bug Fix: Fixed bug in type promotion logic that resulted in false positive. It wasn't properly handling subclasses of promotable types (like 'int', which can be promoted to 'float').
    -   Enhancement: Improved bidirectional type inference for call expressions. The logic now handles the case where the return type of the callable is a generic type that is not an exact match for the expected type but is assignable to the expected type.
    -   Enhancement: Added support for explicit type aliases (PEP 613) within class scopes. A proposed amendment to PEP 613 will make this legal.
    -   Enhancement: Added check for a class-scoped generic type alias that uses a class-scoped TypeVar. This is now flagged as an error.

## 2021.11.0 (3 November 2021)

Notable changes:

-   Enum member values are now appear before other enum class members in completions.
    ([pylance-release#1977](https://github.com/microsoft/pylance-release/issues/1977))
-   Type mismatch errors involving tuples are now more descriptive.
    ([pylance-release#2020](https://github.com/microsoft/pylance-release/issues/2020))
-   Pylance's copy of typeshed has been updated.
-   The bundled stubs for django have been updated.

In addition, Pylance's copy of Pyright has been updated from 1.1.183 to 1.1.184 including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Enhancement: Improved signature help for the constructor of classes that define a `__new__` method but no `__init__` method, such as the `zip` class. The previous logic was always preferring the `__init__`, which is supplied by the `object` class, which all classes derive from. ([pylance-release#1912](https://github.com/microsoft/pylance-release/issues/1912))
    -   Bug Fix: Fixed bug in stub generation code that resulted in an error if a stub was requested for a submodule in a package that includes an `__init__.py` file in the same directory as the submodule source file. ([pylance-release#2013](https://github.com/microsoft/pylance-release/issues/2013))
    -   Bug Fix: Fixed overflow.
    -   Enhancement: Increased stack trace limit from default to 256 in pyright VS Code extension to facilitate debugging of stack overflow errors.
    -   Enhancement: Added special-case support for the **self** attribute of a bound method.
    -   Bug Fix: Fixed a bug in the handling of reveal_type that caused hover text within the argument to be displayed as `Unknown` in some circumstances. ([pylance-release#2024](https://github.com/microsoft/pylance-release/issues/2024))
    -   Enhancement: Improved readability of diagnostic message for type mismatch when assigning to a tuple expression. ([pylance-release#2020](https://github.com/microsoft/pylance-release/issues/2020))
    -   Enhancement: Added support in completion provide for enum members. They are now properly identified as such and prioritized higher in the completion list than other non-member symbols. ([pylance-release#1977](https://github.com/microsoft/pylance-release/issues/1977))
    -   Bug Fix: Fixed bug in completion provider where it was not properly handling binding to classes, which left parameter types unspecialized in some cases. It was already properly handling binding to objects (class instances), so this was a straightforward extension.
-   [1.1.184](https://github.com/microsoft/pyright/releases/tag/1.1.184)
    -   Bug Fix: Fixed false positive error when a class used within as a TypeVar `bound` argument is a "pseudo generic" class, one whose constructor is unannotated. ([pylance-release#2017](https://github.com/microsoft/pylance-release/issues/2017))
    -   Bug Fix: Changed type evaluator to elide `NoReturn` from union generated from `or` or `and` operator.
    -   Enhancement: Improved error handling for the `Generic` special form. Eliminated false positive error when `Generic` is used in certain legitimate ways within a function.
    -   Enhancement: Improved error messages for call expressions that involve overloaded functions. ([pylance-release#1982](https://github.com/microsoft/pylance-release/issues/1982))
    -   Enhancement: Implemented optimization that reduces analysis time and memory usage by generating a diagnostic message (which often involve converting types to a textual representation) only if the caller is interested in the diagnostic message.
    -   Enhancement: Added support for "Self" type documented in draft PEP: https://docs.google.com/document/d/1ujuSMXDmSIOJpiZyV7mvBEC8P-y55AgSzXcvhrZciuI/edit.
    -   Enhancement: Added support for trace logging of type evaluation from the command line when both `--stats` and `--verbose` are specified.
    -   Bug Fix: Fixed bug that resulted in the incorrect type evaluation when a property was defined on a metaclass and accessed through a class with that metaclass.
-   [1.1.183](https://github.com/microsoft/pyright/releases/tag/1.1.183)
    -   Bug Fix: Fixed bug in handling of the recently-added "--skipunannotated" command-line flag.
    -   Bug Fix: Fixed a recent regression that resulted in a false positive error when `Union` was used with no type arguments outside of a type annotation. [pylance-release#2014](https://github.com/microsoft/pylance-release/issues/2014))
    -   Enhancement: Extended support for bidirectional type inference for functions that have a generic return type and the "expected type" is a generic class with type arguments that include literal types.
    -   Enhancement: Expanded support for bidirectional type checking for function call expressions where the return type of the function includes a TypeVar that also appears within a function parameter and that parameter is a callable.
    -   Bug Fix: Fixed bug that resulted in incorrect type evaluation for a generic function that returns a specialized class that uses a `Concatenate` in one of the type arguments.
    -   Bug Fix: Fixed bug that caused the type of `super().__new__(cls)` to be evaluated incorrectly.
    -   Bug Fix: Changed type evaluator to elide `NoReturn` from union generated from ternary operator. ([pylance-release#2008](https://github.com/microsoft/pylance-release/issues/2008))
    -   Bug Fix: Fixed a bug that allowed a function to be assigned to a (non-protocol) class if that class defined a `__call__` method. This should be allowed only for protocol classes.
    -   Bug Fix: Fixed a bug that allowed a function to be assigned to a protocol class if it defined a `__call__` method but also defined additional methods or attributes. ([pylance-release#2006](https://github.com/microsoft/pylance-release/issues/2006))
    -   Behavior Change: Changed text representation of inferred type of `self` and `cls` parameters to `Self@ClassName`. This is more consistent with the emerging standard for an explicit `Self` type.

## 2021.10.3 (27 October 2021)

Notable changes:

-   Analysis performance has been improved for large and complicated functions, such as those in `scipy` and `sympy`.
    ([pylance-release#1964](https://github.com/microsoft/pylance-release/issues/1964))
-   Pylance's copy of typeshed has been updated.

In addition, Pylance's copy of Pyright has been updated from 1.1.181 to 1.1.182 including the following changes:

-   [1.1.182](https://github.com/microsoft/pyright/releases/tag/1.1.182)
    -   Enhancement: Implemented missing check for a write to a Final instance or class variable outside of the class implementation.
    -   Enhancement: Added missing check for an attempt to write to a named tuple attribute, which generates a runtime exception.
        ([pylance-release#1976](https://github.com/microsoft/pylance-release/issues/1976))
    -   Bug Fix: Fixed bug that resulted in a false positive when a function returned a callable type that included a parameter with a union type that included an unsolved type variable.
    -   Bug Fix: Improved handling of intersection types produced as part of `isinstance` or `issubclass` type narrowing when the source variable is a type variable. The creation of the intersection type was incorrectly eliminating the association with the type variable, so the narrowed type was no longer seen as compatible with the TypeVar.
    -   Enhancement: Added check for `Union` when only one type argument is provided and it is not an unpacked variadic type variable.
    -   Bug Fix: Fixed bug in "--ignoreexternal" option used with package type verification. It was not correctly ignoring all externally-imported symbols that had unknown or partially-unknown types.
    -   Enhancement: Updated typeshed stubs to latest.
    -   Bug Fix: Fixed false positive error when a constrained TypeVar T and Type[T] were both used in the same function signature.
-   [1.1.181](https://github.com/microsoft/pyright/releases/tag/1.1.181)
    -   Enhancement (from pylance): Improved completion suggestions when typing within a list expression.
    -   Enhancement: Updated typeshed stubs to the latest.
    -   Bug Fix: Fixed bug in type printing logic where it incorrectly displayed captured ParamSpec signature with "/" or "\*" parameters.
    -   Bug Fix: Fixed bug that caused false positive error when assigning one callback protocol to another when both protocols are generic and parameterized with a ParamSpec.
    -   Bug Fix (from pylance): Fixed regression with "--watch" option in command-line version of pyright.
    -   Behavior Change (from pylance): Increase max file size to 50 MB, matching VS Code.
    -   Enhancement: Improved logic for isinstance and issubclass type narrowing when the filter class's type arguments can be determined from the type arguments of the subject type.
    -   Enhancement: Improved type narrowing logic for class pattern matching when the matched class's type arguments can be determined from the type arguments of the subject type.
    -   Bug Fix: Fixed bug that resulted in an incorrect type evaluation for a binary operator that acts upon a bound TypeVar.
    -   Performance: Reduced the max number of nested call-site return type inference evaluations from 3 to 2. This can be extremely expensive in some code bases, such as with scipy, and it was leading to a poor user experience.
        ([pylance-release#1964](https://github.com/microsoft/pylance-release/issues/1964))
    -   Performance: Improved analyzer performance for code that contains thousands of statements with tens of thousands of call statements within a single function or module. This is found in some test modules within the sympy library.
    -   Enhancement: Added "--skipunannotated" option for command-line version of pyright. If specified, pyright skips type analysis of functions and methods that have no parameter or return type annotations. Return types of functions are also never inferred from the function implementation. This matches the default behavior of mypy and allows for more efficient analysis of complex code bases that are only partially annotated.

## 2021.10.2 (20 October 2021)

Notable changes:

-   A bug related to missing completions inside lists and tuples has been fixed.
    ([pylance-release#1302](https://github.com/microsoft/pylance-release/issues/1302))
-   The bundled stubs for django have been updated.

In addition, Pylance's copy of Pyright has been updated from 1.1.179 to 1.1.180 including the following changes:

-   [1.1.180](https://github.com/microsoft/pyright/releases/tag/1.1.180)
    -   Bug Fix: Fixed bug that resulted in a false positive error when a generic class used a specialized version of itself parameterized with one of its own type parameters.
    -   Bug Fix: Fixed recent regression where imported symbols that were ultimately resolved with a native library (e.g. a ".pyd" or ".so" file) were incorrectly resolved as a module rather than an Unknown type.
        ([pylance-release#2446](https://github.com/microsoft/pylance-release/issues/2446))
    -   Bug Fix: Fixed a type evaluation regression that caused type arguments to be incorrectly determined when calling a constructor and passing a callable that is generic.
    -   Enhancement: Added broader support for context managers in with statements which swallow exceptions. Thanks to Rik de Graaff for this contribution.
        ([pylance-release#1945](https://github.com/microsoft/pylance-release/issues/1945))
    -   Bug Fix: Added missing error condition for walrus operator used within a type annotation expression.
    -   Bug Fix: Fixed bug in pattern matching type evaluation where `bytearray` was matched against a sequence pattern even though PEP 634 explicitly excludes this case.
    -   Enhancement: Added support for sequence pattern match type narrowing when the subject type is a simple "object".
    -   Enhancement: Added support for type narrowing of enums when using pattern matching.
    -   Enhancement: Added error reporting for usage of type aliases within class pattern matching statements that generate runtime exceptions.
    -   Behavior Change: Changed the printed type of a ParamSpec signature to avoid the use of synthesized parameter names "\_\_p0", etc. Instead, the parameter names are omitted in the signature consistent with the emerging standard for the improved callable syntax.
    -   Enhancement: Added support for explicit specialization of generic classes that include a ParamSpec. This is defined in PEP 612 but was previously missing.
    -   Bug Fix: Fixed bug in check for generator return type. A diagnostic was meant to be generated if the declared return type was incorrect for a generator.
-   [1.1.179](https://github.com/microsoft/pyright/releases/tag/1.1.179)
    -   Enhancement: Added support for an unpacked tuple assignment within an instance method when the source of the assignment is the `self` parameter.
    -   Bug Fix: Fixed false positive error in protocol variance check (in the `reportInvalidTypeVarUse` diagnostic rule) when a protocol class used a ParamSpec.
    -   Bug Fix: Fixed bug that caused false positive errors when generic callback protocol class used a ParamSpec and a `__call__` method with only two parameters consisting of `P.args` and `P.kwargs`.
    -   Bug Fix: Fixed bug that resulted in a false positive error when using a generic callback protocol with a ParamSpec where the `__call__` method included a positional-only marker prior to the `P.args` and `P.kwargs` parameters.
    -   Bug Fix: Fixed a bug that results in false positive error when assigning a source union type to a destination union type.
    -   Bug Fix: Fixed an internal crash that was caused by infinite recursion.
    -   Bug Fix: Fixed bug in completion provider that resulted in inappropriate suggestions when typing arguments within a class declaration.
    -   Bug Fix: Changed type logic for sequence pattern matching to produce `list` rather than `tuple` for star subpatterns. This matches the runtime behavior in Python 3.10.
    -   Enhancement: Added support for name expressions in `with` statements where the name refers to a variable or parameter with a declared type that corresponds to a context manager class that swallows exceptions.
    -   Bug Fix: Fixed bug that resulted in a false positive error when a generic class used a specialized version of itself parameterized with one of its own type parameters.

## 2021.10.1 (14 October 2021)

Notable changes:

-   A bug in the import completion that prevented some absolute imports from being suggested has been fixed.
-   Variables named `match` no longer cause a parser error when used in a slice expression.
    ([pylance-release#1911](https://github.com/microsoft/pylance-release/issues/1911))
-   `TypedDict` completions now work correctly in `dict` literals with more than one key-value pair.
    ([pylance-release#1920](https://github.com/microsoft/pylance-release/issues/1920)
-   The bundled stubs for pandas, django and openpyxl have been updated.

In addition, Pylance's copy of Pyright has been updated from 1.1.176 to 1.1.178, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Enhancement: Added support for an unpacked tuple assignment within an instance method when the source of the assignment is the `self` parameter.
-   [1.1.178](https://github.com/microsoft/pyright/releases/tag/1.1.178)
    -   Bug Fix: Fixed false positive error that occurred when importing a symbol in a `from x import y` statement that referred to a chain of imports and was eventually resolved to a native library (e.g. ".pyd" or ". so" file).
    -   Bug Fix: Added missing check for type compatibility between callables where the destination type includes a default argument for a parameter but the source type does not.
    -   Bug Fix: Fixed bug that caused incorrect evaluation of inferred return type based on inferred type of unannotated "self" or "cls" parameter.
        ([pylance-release#1927](https://github.com/microsoft/pylance-release/issues/1927))
    -   Enhancement: Added support for "narrowing" of TypedDict instances on assignment when the TypedDict defines entries that are not required but are supplied.
        ([pylance-release#1926](https://github.com/microsoft/pylance-release/issues/1926))
    -   Behavior Change: Changed the interpretation of a property declared within a protocol class. It was previously interpreted only as a property (i.e. classes compatible with the protocol must implement a property of the same name). Compatible classes are now able to declare an attribute whose type is compatible with the property getter. Access to the property from the protocol class as a class variable is no longer allowed.
        ([pylance-release#1915](https://github.com/microsoft/pylance-release/issues/1915))
    -   Enhancement: Improved error message for improper use of a module as a type argument.
    -   Bug Fix: Fixed a bug in import resolution logic that resulted in incorrect resolution of a symbol in the presence of wildcard imports that allowed for multiple resolution paths, some of them cyclical. Pyright previously gave up when it detected a cycle rather than using a different (non-cyclical) resolution path.
    -   Bug Fix: Improved parser's detection of "match" as a soft keyword versus some other usage of a symbol named "match".
        ([pylance-release#1911](https://github.com/microsoft/pylance-release/issues/1911))
    -   Bug Fix: Fixed bug that resulted in a false negative when a TypedDict value was assigned to a protocol that included attributes that matched the TypedDict keys.
    -   Bug Fix: Fixed bug that resulted in false positive when a function is used in an `==` or `!=` binary expression.
    -   Bug Fix (from pylance): Fixed bug in import completions for parent directory resolution.
-   [1.1.177](https://github.com/microsoft/pyright/releases/tag/1.1.177)
    -   Bug Fix: Fixed bug in stub generation logic. It wasn't properly handling module paths with more than a single ".", such as "google.cloud.storage".
    -   Bug Fix: Fixed false positive error in certain cases where type variable was bound to a union.
    -   Enhancement: Implemented check for an attempt to subclass an Enum class that defines one or more enumerated values. This condition generates a runtime exception.
    -   Enhancement: Type aliases in the printed form of a union type are retained when aliased types are combined in a union.
    -   Bug Fix: Fixed bug in completion provider's handling of key completions for TypedDicts.
        ([pylance-release#1920](https://github.com/microsoft/pylance-release/issues/1920))
    -   Bug Fix: Fixed false positive type evaluation error when constrained TypeVar is assigned to a union that contains a compatible constrained TypeVar.
    -   Bug Fix: Added code to work around the circular definition found in the typeshed stub that defines the os.scandir function.
        ([pylance-release#1918](https://github.com/microsoft/pylance-release/issues/1918))
-   [1.1.176](https://github.com/microsoft/pyright/releases/tag/1.1.176)
    -   Enhancement: Exempted check for unsafe access to TypedDict key if it's within a context manager. It was previously exempted if included in a `try` block, but some prefer to use a context manager to catch exceptions.
    -   Behavior Change: Bumped pyright's default Python version from 3.9 to 3.10.
    -   Enhancement: Added support for "bare" `ClassVar` annotations.
    -   Enhancement: Updated to the latest version of typeshed stubs.
    -   Enhancement: Added new "--warnings" command-line option that generates an exit code of 1 if one or more warnings are emitted. By default, only errors generate an exit code of 1.
    -   Bug Fix: Fixed bug that resulted in a "unknown member of module" error if the member referred to a submodule that was imported privately from another module but that submodule was also explicitly imported. For example, if a module imports both `a` and `a.b` and then uses the symbol `a.b.c`.
    -   Enhancement: Added new diagnostic check "reportMissingParameterType" that checks for function and method input parameters that are missing a type annotation.
    -   Enhancement: Added support for new type guard pattern: `x[I] is None` and `x[I] is not None` where `x` is a tuple or union of tuples with known lengths and entry types and `I` is an integer.
    -   Enhancement: Enhanced the stub generation logic to emit `__all__ = ...` and `__all__ += ...` statements when they appear in the module scope and are not within a conditional (if/else) block.

## 2021.10.0 (6 October 2021)

Notable changes:

-   Return type inference is now skipped for high-complexity unannotated functions, which prevents hangs in `sympy`, `scipy`, and other unannotated libraries.
    ([pylance-release#946](https://github.com/microsoft/pylance-release/issues/946), [pylance-release#1890](https://github.com/microsoft/pylance-release/issues/1890), [pylance-release#1895](https://github.com/microsoft/pylance-release/issues/1895))
-   The bundled stubs for pandas have been updated.
-   Pylance's copy of typeshed has been updated.
    ([pylance-release#1909](https://github.com/microsoft/pylance-release/issues/1909))

In addition, Pylance's copy of Pyright has been updated from 1.1.173 to 1.1.175, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Enhancement: Updated typeshed stubs to the latest.
    -   Enhancement: Added support for "bare" ClassVar annotations.
    -   Enhancement: Bumped pyright's default Python version from 3.9 to 3.10.
    -   Behavior Change: Exempted check for unsafe access to TypedDict key if it's within a context manager. It was previously exempted if included in a `try` block, but some prefer to use a context manager to catch exceptions.
-   [1.1.175](https://github.com/microsoft/pyright/releases/tag/1.1.175)
    -   This is a "hot fix" release that addresses two regressions introduced in 1.1.174.
    -   Bug Fix: Reverted a change that broke the use of generic dataclass types.
    -   Bug Fix: Reverted a change that resulted in a false positive error when subclassing an Enum base class that defined no enumerated values.
-   [1.1.174](https://github.com/microsoft/pyright/releases/tag/1.1.174)
    -   Behavior Change: Modified import resolution logic to handle namespace stub packages. This case isn't explicitly covered by PEP 561, but there is a proposal to amend the PEP to clarify how to handle this case.
    -   Bug Fix: Fixed bug that resulted in a false negative when dealing with types that are conditioned on constrained or bound TypeVars.
    -   Bug Fix: Fixed bug that affected a missing type argument for a ParamSpec type parameter. It should be an Unknown type.
    -   Bug Fix: Fixed bug that resulted in an `Unknown` type appearing in a type evaluation for an unannotated variable that is modified in a loop.
    -   Enhancement: Added error reporting for an attempt to subclass an Enum class and a duplicate definition of enum members.
    -   Enhancement: Improved error reporting for index expressions used for non-generic classes.
    -   Enhancement: Fixed performance issue in stub generation code that caused stub generation to take longer than needed.
    -   Enhancement: Added performance improvement that skips return type inference for functions whose parameters are not annotated and have a "code flow complexity" beyond a certain threshold.
        ([pylance-release#946](https://github.com/microsoft/pylance-release/issues/946), [pylance-release#1890](https://github.com/microsoft/pylance-release/issues/1890), [pylance-release#1895](https://github.com/microsoft/pylance-release/issues/1895))
    -   Bug Fix: Fixed bug the resulted in a false positive when an overloaded function is passed as an argument to a function that accepts a callable parameter using generics.
    -   Bug Fix: Fixed a false positive error when a class with an overloaded constructor is passed as an argument to a callable parameter.
    -   Bug Fix: Fixed bug in type var matching logic that resulted in a false positive when using a generic class that conforms to a generic protocol and uses that protocol within its own method signatures.
        ([pylance-release#1807](https://github.com/microsoft/pylance-release/issues/1807))
-   [1.1.173](https://github.com/microsoft/pyright/releases/tag/1.1.173)
    -   Bug Fix: Fixed a false positive error with the new union syntax when the LHS expression is an Any or Unknown type.
    -   Enhancement: Updated typeshed stubs to the latest.
    -   Bug Fix: Fixed bug in ParamSpec specialization code that can occur when using a generic type alias with a ParamSpec.
    -   Bug Fix: Fixed false positive error when assigning a callable to a callback protocol that includes a ParamSpec.
    -   Bug Fix: Fixed bug that resulted in unbound variable condition not being reported if it was in a loop and was assigned conditionally.
    -   Bug Fix: Fixed bug relating to the use of an `Any` type argument corresponding to a ParamSpec type parameter.
        ([pylance-release#1892](https://github.com/microsoft/pylance-release/issues/1892))
    -   Bug Fix: Fixed a false positive error when using a generic descriptor class that is parameterized by the `self` or `cls` parameter of the class that allocates the descriptor.
    -   Enhancement: Added check for inappropriate use of a field annotated with `InitVar`.
    -   Bug Fix: Fixed bug that resulted in a false positive error when a protocol class used generic type parameters scoped to a method.

## 2021.9.4 (29 September 2021)

Notable changes:

-   Completion is now supported for TypedDict keys and values. Thanks to Robert Cragie for this contribution!
-   Variables captured by lambdas and functions are now narrowed when they are known to not be reassigned.
    ([pylance-release#261](https://github.com/microsoft/pylance-release/issues/261), [pylance-release#1016](https://github.com/microsoft/pylance-release/issues/1016))
-   Auto-imports no longer incorrectly add to `*` import lines.
    ([pylance-release#1679](https://github.com/microsoft/pylance-release/issues/1679))
-   The "Add Optional to Type Annotation" quick fix no longer fails to run.
    ([pylance-release#1873](https://github.com/microsoft/pylance-release/issues/1873))
-   Pylance's copy of typeshed has been updated.
    ([pylance-release#1872](https://github.com/microsoft/pylance-release/issues/1872))

In addition, Pylance's copy of Pyright has been updated from 1.1.170 to 1.1.172, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Bug Fix: Fixed a false positive error with the new union syntax when the LHS expression is an Any or Unknown type.
        ([pylance-release#1886](https://github.com/microsoft/pylance-release/issues/1886))
    -   Bug Fix: Fixed bug in ParamSpec specialization code that can occur when using a generic type alias with a ParamSpec.
    -   Bug Fix: Fixed false positive error when assigning a callable to a callback protocol that includes a ParamSpec.
-   [1.1.172](https://github.com/microsoft/pyright/releases/tag/1.1.172)
    -   Enhancement: Added completion suggestion support for TypedDict keys and values. Thanks to Robert Cragie for this contribution!
    -   Behavior Change: Changed behavior of reportInvalidTypeVarUse diagnostic check to flag bound type variables used as type arguments within return type annotations.
    -   Enhancement: Implemented code that applies type narrowing to local variables and parameters when they are captured by an inner-scoped lambda or function and the variable or parameter is not reassigned after the lambda or function along any code flow paths.
    -   Enhancement: Updated typeshed stubs to the latest.
    -   Bug Fix: Fixed a bug in ParamSpec handling that resulted in false positives when a callable type containing a ParamSpec was assigned to another callable type containing a ParamSpec.
    -   Enhancement (from pylance): Improved handling of type checking when files are opened in "single file" mode, rather than opening a project root directory.
    -   Enhancement (from pylance): Implemented heuristic for detecting import roots within a project. Previously, these all needed to be specified through "extraPaths" settings, but now pyright is smarter about locating these directories automatically.
    -   Bug Fix: Fixed false positive error when a generic class with a ParamSpec type parameter implements a descriptor protocol.
-   [1.1.171](https://github.com/microsoft/pyright/releases/tag/1.1.171)
    -   Bug Fix: Fixed bug in TypeVarTuple support that prevented the use of an unpacked TypeVarTuple within a type argument list for types other than Tuple or Union.
    -   Bug Fix: Fixed bug in synthesized `__new__` method for NamedTuple class that caused the constructor of subclasses of the NamedTuple to construct the base class.
    -   Bug Fix: Fixed bug where a class whose constructor is unannotated was allowed to have explicit generic type arguments.
    -   Behavior Change: Changed type evaluation behavior for protected instance variables (those that begin with a single underscore) and are assigned a literal value. Previously, the literal type was retained if the `reportPrivateUsage` was enabled. This caused various problems. It was a bad idea because type evaluations should not differ based on diagnostic reporting switches.
    -   Enhancement: Added logic to report a diagnostic if an instance variable is assigned only via an augmented assignment expression.
    -   Bug Fix (from pylance): Fixed bug in parser that resulted in incorrect text range for relative module names in import statements.
    -   Bug Fix: Improved inference of generator statements that involve `await` statements to conform to the runtime behavior of the CPython intepreter.
    -   Bug Fix: Fixed bug that caused inconsistent handling of dataclasses that use the `@dataclass` decorator and derive from abstract base classes.
    -   Bug Fix: Fixed bug that caused yield expression to be evaluated as "unknown" in some cases when it was contained within a loop.
    -   Bug Fix: Fixed bug that resulted in incorrect type evaluation for expressions within an `await` statement under some circumstances.
        ([pylance-release#1869](https://github.com/microsoft/pylance-release/issues/1869))
    -   Behavior Change: Changed code that converts types to textual representation to prepend a tilde ("~") character for the inferred type of a "self" or "cls" parameter.
    -   Enhancement: Updated typeshed stubs to the latest.

## 2021.9.3 (22 September 2021)

Notable changes:

-   A number of IntelliCode bugs have been fixed, including cases where starred entries would disappear when more code is typed.
    ([pylance-release#89](https://github.com/microsoft/pylance-release/issues/89))
-   Signature help should no longer trigger when typing a parenthesis in a string.
    ([pylance-release#1677](https://github.com/microsoft/pylance-release/issues/1677))
-   Pylance's copy of typeshed has been updated.

In addition, Pylance's copy of Pyright has been updated from 1.1.169 to 1.1.170, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Bug Fix: Fixed bug in TypeVarTuple support that prevented the use of an unpacked TypeVarTuple within a type argument list for types other than Tuple or Union.
    -   Bug Fix: Fixed bug in synthesized `__new__` method for NamedTuple class that caused the constructor of subclasses of the NamedTuple to construct the base class.
    -   Bug Fix: Fixed bug where a class whose constructor is unannotated was allowed to have explicit generic type arguments.
        ([pylance-release#1859](https://github.com/microsoft/pylance-release/issues/1859))
    -   Behavior Change: Changed type evaluation behavior for protected instance variables (those that begin with a single underscore) and are assigned a literal value. Previously, the literal type was retained if the `reportPrivateUsage` was enabled. This caused various problems. It was a bad idea because type evaluations should not differ based on diagnostic reporting switches.
    -   Enhancement: Added logic to report a diagnostic if an instance variable is assigned only via an augmented assignment expression.
        ([pylance-release#1858](https://github.com/microsoft/pylance-release/issues/1858))
-   [1.1.170](https://github.com/microsoft/pyright/releases/tag/1.1.170)
    -   Bug Fix (from Pylance): Handle unrooted execution environments (e.g., open file mode), preventing various crashes and oddities.
    -   Bug Fix (from Pylance): Generate default values in method overload signatures. Previously, we didn't include them, which generated the wrong signature.
    -   Bug Fix (from Pylance): Use attribute docstrings for type aliases in completion and hover.
    -   Bug Fix (from Pylance): Modify parser to change the range of parenthesized expressions to their contents. This improves the ranges returned in hovers, document highlight, etc.
    -   Bug Fix: Improved member access logic to more faithfully match the Python interpreter's behavior when the member is assigned through a class, that member is a class itself, and that class has a metaclass that implements a descriptor protocol. It appears that the interpreter does not call through to the metaclass's `__set__` method in this case, even though it does call its `__get__` method when the member is accessed in the same circumstance.
    -   Enhancement: Extended reportCallInDefaultInitializer diagnostic check to disallow list, set or dict expressions in default argument expression.
    -   Bug Fix: Improved `isinstance` and `issubclass` narrowing to handle open-ended tuples passed as the second argument.
    -   Bug Fix: Fixed false positive error when `namedtuple` constructor is called with a list of field names that includes dynamic (non-literal) expressions.
        ([pylance-release#1832](https://github.com/microsoft/pylance-release/issues/1832))
    -   Bug Fix: Fixed false positive error where an exception class (as opposed to an exception object) is used in a "from" clause in a "raise" statement.
    -   Enhancement: Added support for ParamSpec matching when used within a callback protocol. PEP 612 is unclear on whether this should be supported, by pyre (the reference implementation for the PEP) does support it.
    -   Bug Fix: Fixed false negative error in parser where it did not correctly detect a syntax error when a walrus operator was used in a ternary operator condition expression.
        ([pylance-release#1838](https://github.com/microsoft/pylance-release/issues/1838))
    -   Bug Fix: Fixed bug that resulted in false negative when bidirectional type inference involved an "expected type" of Any and the type being evaluated was a call expression that returned a generic object as a return value.
    -   Bug Fix: Fixed infinite recursion bug in hover provider when a symbol referred to both a locally-defined class and an imported symbol.
    -   Bug Fix: Fixed bug that resulted in false positive when using unpack operator with `self` when `self` refers to a named tuple or a tuple with known length.
    -   Behavior Change: Allow symbols that are not explicitly re-exported from a stub to be imported into another stub. This change is required to support recent updates to typeshed.
    -   Enhancement: Updated typeshed stubs to the latest.

## 2021.9.2 (16 September 2021)

Notable changes:

-   Method override completions now correctly include default parameters.
    ([pylance-release#869](https://github.com/microsoft/pylance-release/issues/869))
-   PEP 258 style attribute docstrings now work on type aliases.
    ([pylance-release#1815](https://github.com/microsoft/pylance-release/issues/1815))
-   Parenthesized expressions are now better handled in hover, document highlight, and semantic highlighting.
    ([pylance-release#591](https://github.com/microsoft/pylance-release/issues/591))
-   A number of errors and inconsistencies with unrooted environments (like open file mode) have been fixed.
    ([pylance-release#1586](https://github.com/microsoft/pylance-release/issues/1586))
-   The docstring for `os.path.splitext` is now correctly handled.
    ([pylance-release#1408](https://github.com/microsoft/pylance-release/issues/1408))
-   The bundled stubs for pandas have been updated.
-   Pylance's copy of typeshed has been updated.

In addition, Pylance's copy of Pyright has been updated from 1.1.166 to 1.1.169, including the following changes:

-   [1.1.169](https://github.com/microsoft/pyright/releases/tag/1.1.169)
    -   Bug Fix: Improved type narrowing logic for `a is b` pattern where `a` is `self` (or a bound TypeVar) and `b` is an enum literal.
    -   Bug Fix: Updated reportIncompatibleMethodOverride diagnostic check to special-case dict key names that overlap with method names in the `_TypedDict` class.
    -   Bug Fix: Improved handling of attribute accesses for classes that inherit from `Any` or an unknown class.
    -   Enhancement: Added optimization that reduces the time it takes to perform code flow analysis in the presence of if/elf/else statements, try statements, with statements, and ternary expressions.
    -   Bug Fix: Fixed bug that caused false positive when a bound TypeVar is bound to an instantiable class (e.g. `Type[X]`).
        ([pylance-release#1808](https://github.com/microsoft/pylance-release/issues/1808))
-   [1.1.168](https://github.com/microsoft/pyright/releases/tag/1.1.168)
    -   Bug Fix: Fixed inconsistency in the constraint solver with respect to literal types. They were being retained for most classes but not for tuples.
        ([pylance-release#1802](https://github.com/microsoft/pylance-release/issues/1802))
    -   Bug Fix: Fixed bug in parser that resulted in a false negative when a `for` keyword (in either a `for` statement or a list comprehension) was followed immediately by `in` keyword.
        ([pylance-release#1805](https://github.com/microsoft/pylance-release/issues/1805))
    -   Behavior Change: Enforce PEP 484 rules for symbols that are imported by a stub file but are not meant to be re-exported. These symbols are no longer resolved when accessed outside of the module, nor are they included in completion suggestions or other language service providers.
    -   Behavior Change: Modified logic for private symbols (whose names begin with an underscore) exported from a stub file or a py.typed source file; if the symbol is explicitly included in `__all__` it is not considered private.
    -   Enhancement: Added reportPrivateImportUsage diagnostic rule, which reports usage of a symbol from a py.typed library that is not intended to be re-exported by the library's author. The rule is on by default in basic type checking mode but can be disabled. Completion provider no longer offers these symbols as completion suggestions.
    -   Bug Fix: Fixed bug that resulted in incorrect type evaluation when co-dependent variables were assigned in a loop using tuple assignments (e.g. `a, b = b, a + 1`).
    -   Bug Fix: Improved `isinstance` and `issubclass` support to handle the case where the type of the second argument is a union where the subtypes includes both tuples of class types and non-tuples.
        ([pylance-release#1809](https://github.com/microsoft/pylance-release/issues/1809))
    -   Enhancement: Updated typeshed to latest version
-   [1.1.167](https://github.com/microsoft/pyright/releases/tag/1.1.167)
    -   Bug Fix: Fixed regression that caused a false positive error when an overload implementation annotates a parameter with a union that includes a type variable.
    -   Enhancement: Added support for type annotations that are enclosed in triple quotes.
    -   Bug Fix: Fixed false positive error when a class declaration inherits from `Protocol` and `Generic`.
    -   Bug Fix: Fixed bug that resulted in a missed error (false negative) when comparing an overload implementation with an overload signature that uses a generic return type.
    -   Enhancement: Added support for a `super()` call made within a class method or instance method where the `cls` or `self` parameter is explicitly annotated (e.g. with a bound type variable).
    -   Enhancement: Extended isinstance type narrowing logic to support `Callable`.
    -   Enhancement (contribution from Matt Hillsdon): Reduced cascading parser errors when a colon is omitted before an indented code block.
    -   Bug Fix: Fixed incorrect type evaluation for ternary, list and dictionary expressions in certain cases where the expression is within a loop.
    -   Bug Fix: Fixed bug in control flow engine that resulted in incomplete types in certain cases that involved loops and circular type dependencies.

## 2021.9.1 (8 September 2021)

Notable changes:

-   Docstrings are no longer inherited from builtins like `object`.
    ([pylance-release#653](https://github.com/microsoft/pylance-release/issues/653), [pylance-release#1047](https://github.com/microsoft/pylance-release/issues/1047), [pylance-release#1205](https://github.com/microsoft/pylance-release/issues/1205))
-   Builtin module variables (like `__file__` and `__package__`) are now correctly highlighted.
    ([pylance-release#964](https://github.com/microsoft/pylance-release/issues/964))

In addition, Pylance's copy of Pyright has been updated from 1.1.165 to 1.1.166, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Bug Fix: Fixed false positive error when a class declaration inherits from `Protocol` and `Generic`.
    -   Enhancement: Added support for type annotations that are enclosed in triple quotes.
    -   Bug Fix: Fixed regression that caused a false positive error when an overload implementation annotates a parameter with a union that includes a type variable.
    -   Bug Fix: Fixed bug that resulted in a missed error (false negative) when comparing an overload implementation with an overload signature that uses a generic return type.
        ([pylance-release#1778](https://github.com/microsoft/pylance-release/issues/1778))
    -   Enhancement: Added support for a super() call made within a class method or instance method where the `cls` or `self` parameter is explicitly annotated (e.g. with a bound type variable).
        ([pylance-release#1779](https://github.com/microsoft/pylance-release/issues/1779))
    -   Enhancement: Extended isinstance type narrowing logic to support `Callable`.
-   [1.1.166](https://github.com/microsoft/pyright/releases/tag/1.1.166)
    -   Bug Fix: Fixed a false positive error (and crash) when a walrus operator (assignment expression) is used within a list comprehension which is passed as an argument to a function decorator.
    -   Bug Fix: Fixed stack overflow crash in type analyzer.
        ([pylance-release#1751](https://github.com/microsoft/pylance-release/issues/1751))
    -   Bug Fix: Fixed incorrect evaluation of recursive type alias whose definition uses a `TypeAlias` annotation.
    -   Enhancement: Improved error messages for type argument count mismatch; they were referring to a "class", but sometimes they were used for type aliases as well.
    -   Bug Fix: Fixed bug that resulted in the incorrect specialization of a type alias that includes a ParamSpec.
    -   Bug Fix: Fixed bug in type verifier that resulted in incorrect reporting of an unknown type when a type alias was defined using a `TypeAlias` annotation.
    -   Enhancement: Extended dataclass_transform mechanism to support implicit `init` argument values for field descriptors.
    -   Bug Fix: Fixed false native that incorrectly allowed a union type to be assigned to a constrained TypeVar.
    -   Bug Fix: Improved handling of class properties (i.e. properties that have @classmethod applied to them). The `cls` parameter for the property method is now properly passed the class as an argument.
    -   Enhancement (contribution by Marc Mueller): Adjust auto-import sorting to better match isort.
    -   Bug Fix: Fixed bug in overlapping overload detection logic that resulted in false positives in some cases.
    -   Bug Fix: Fixed a bug that resulted in unsolved TypeVars in certain edge cases involving function type compatibility checks.
    -   Bug Fix: Improved handling of constrained type variables that use a union in one or more constraints.
    -   Bug Fix: Fixed bug that resulted in a false positive error when a call involves overloads and one or more of the arguments involves another call expression whose type is generic, and therefore influenced by bidirectional inference context.

## 2021.9.0 (1 September 2021)

Notable changes:

-   Docstrings for the `decimal` module are now supported.
    ([pylance-release#1350](https://github.com/microsoft/pylance-release/issues/1350))
-   The `None`, `True`, `False`, and `__debug__` builtin constants are now correctly colorized within quoted type annotations.
    ([pylance-release#1039](https://github.com/microsoft/pylance-release/issues/1039))
-   Completions for keywords that aren't available in the currently selected version of Python will no longer be offered.
    ([pylance-release#1724](https://github.com/microsoft/pylance-release/issues/1724))
-   Import completions will no longer include imports which will not resolve if accepted.
    ([pylance-release#1046](https://github.com/microsoft/pylance-release/issues/1046))
-   The bundled stubs for pandas have been updated.
-   Pylance's copy of typeshed has been updated.

In addition, Pylance's copy of Pyright has been updated from 1.1.163 to 1.1.165, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Bug Fix: Fixed a false positive error (and crash) when a walrus operator (assignment expression) is used within a list comprehension which is passed as an argument to a function decorator.
        ([pylance-release#1745](https://github.com/microsoft/pylance-release/issues/1745))
-   [1.1.165](https://github.com/microsoft/pyright/releases/tag/1.1.165)
    -   Bug Fix: Fixed false positive error due to incorrect type of the `__doc__` instance variable. It should be `str | None`, but it was hard-coded to be `str`.
    -   Bug Fix: Fixed a bug that resulted in a false positive type error when an instance variable's type depended on itself in a circular reference within a loop.
    -   Bug Fix: Fixed false positive error when a binary operation uses `None` on the LHS and the RHS is a type that accepts `None` to a reverse operator overload method.
    -   Bug Fix: Improved logic that determines whether a type is iterable. The old logic didn't support unions of iterable types.
    -   Bug Fix: Improved handling of call expressions to functions that return NoReturn.
    -   Bug Fix: Fixed bug in recently-added type check for inherited class variable type. The check was not properly specializing the base class type.
    -   Enhancement: Updated typeshed stubs to the latest version.
    -   Enhancement: Added performance optimization for code flow analysis within loops.
        ([pylance-release#1686](https://github.com/microsoft/pylance-release/issues/1686))
    -   Enhancement (from Pylance): Don't offer keywords as completion suggestions if they are not valid for the currently-selected version of Python.
    -   Enhancement: Added check for subscripted form of `asyncio.Task` when used in certain contexts prior to Python 3.9 that generate runtime exceptions.
-   [1.1.164](https://github.com/microsoft/pyright/releases/tag/1.1.164)
    -   Bug Fix: Fixed false positive error when assigning an `Any` value to a member of an object that has a `__set__` method.
    -   Enhancement: Eliminated confusing error message when nested argument expression contains a type error.
    -   Enhancement: Improved bidirectional inference logic for lambda expressions to better handle the situation where the "expected type" is a union that contains multiple callable types.
    -   Behavior Change: Suppressed the "obscured symbol" diagnostic check when the name of the symbol is `_`. This symbol is used in the single dispatch pattern documented in PEP 443.
    -   Bug Fix (from Pylance): Support eggs that are not in zip files but are instead in folders.
    -   Enhancement (from Pylance): Support pth file in extra paths.
    -   Bug Fix: Fixed false positive error when a constrained TypeVar is used as the second argument to an isinstance or subclass call.
        ([pylance-release#1730](https://github.com/microsoft/pylance-release/issues/1730))
    -   Bug Fix: Fixed false positive error that occurs when a `@final` class derives from an abstract base class that defines no abstract methods.
        ([pylance-release#1732](https://github.com/microsoft/pylance-release/issues/1732))
    -   Bug Fix: Fixed false positive error related to overload implementation checks when the return type of the implementation contains a Tuple annotation with a TypeVar as a type argument.
    -   Enhancement: Added special-case handling for `tuple[()]` type when determining the iterated type. In this case, it can be safely evaluated as `Never`.
        ([pylance-release#1736](https://github.com/microsoft/pylance-release/issues/1736))
    -   Enhancement: Improved error reporting for assignments to class variable assignments within a child class where the assigned value doesn't match the type of the same-named class variable declared in a parent class.
        ([pylance-release#1726](https://github.com/microsoft/pylance-release/issues/1726))

## 2021.8.3 (25 Aug 2021)

Notable changes:

-   A bug that prevented navigation to directory-based eggs has been fixed. ([pylance-release#1685](https://github.com/microsoft/pylance-release/issues/1685))
-   Corrupt eggs and zips will no longer cause a crash. ([pylance-release#1692](https://github.com/microsoft/pylance-release/issues/1692))
-   Triple quote auto-close has been disabled for multi-line selections. ([pylance-release#1716](https://github.com/microsoft/pylance-release/issues/1716))
-   The bundled stubs for django and pandas have been updated.
-   pth files in directories in extraPaths will now be processed for additional paths. ([pylance-release#1709](https://github.com/microsoft/pylance-release/issues/1709))
-   Pylance's copy of typeshed has been updated.

In addition, Pylance's copy of Pyright has been updated from 1.1.162 to 1.1.163, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Bug Fix: Fixed false positive error when assigning an Any value to a member of an object that has a `__set__` method.
    -   Enhancement: Eliminated confusing error message when nested argument expression contains a type error. ([pylance-release#1705](https://github.com/microsoft/pylance-release/issues/1705))
    -   Enhancement: Improved bidirectional inference logic for lambda expressions to better handle the situation where the "expected type" is a union that contains multiple callable types.
    -   Enhancement: Suppressed the "obscured symbol" diagnostic check when the name of the symbol is `_`. This symbol is used in the single dispatch pattern documented in PEP 443.
-   [1.1.163](https://github.com/microsoft/pyright/releases/tag/1.1.163)
    -   Bug Fix: Fixed false positive error relating to the use of a `*P.args` or `**P.kwargs` parameter as an iterable value (where `P` is a `ParamSpec`).
    -   Bug Fix: Fixed false positive error due to incomplete tracking of incomplete types during code flow evaluation.
    -   Bug Fix: Fixed bug with ParamSpec matching in the case where the matched function contains parameters with default values or `*args` / `**kwargs`;
    -   Bug Fix: Fixed false positive error that results when defining a property setter within an abstract base class and the property setter references a type that has a circular reference to the class.
    -   Bug Fix: Fixed a false positive error when handling *args and \*\*kwargs arguments when the function contains *P.args and \*\*P.kwargs parameters.
    -   Behavior Change (from Pylance): When inserting new auto-import symbol, sort by symbol type to match isort default behavior.
    -   Bug Fix: Fixed comparison operators so they use the proper opposite when looking for a type match. For example, the opposite of `__lt__` is `__ge__` rather than `__gt__`.
    -   Bug Fix: Fixed bug that caused inappropriate type narrowing if a comparison operator was used within an argument for a call expression which was, in turn, used within an `if` condition expression.
    -   Behavior Change: Changed the interpretation of a "callback protocol" to encompass protocols that include a `__call__` method in addition to other attributes.
    -   Bug Fix: Fixed false positive error related to `with` statements with an expression enclosed in single parentheses. ([pylance-release#1670](https://github.com/microsoft/pylance-release/issues/1670))
    -   Bug Fix: Fixed bug in type var matching when the a `cls` parameter is annotated with type `Type[T]` and `T` is bound to a protocol class.
    -   Bug Fix: Fixed bug that resulted in `# type: ignore` comments to be ignored in the event that we hit the heap high-water mark and emptied internal caches.
    -   Enhancement: Updated to latest version of typeshed stubs.

## 2021.8.2 (19 Aug 2021)

Notable changes:

-   Attribute doc strings are now supported in hover tooltips.
-   Diagnostics and other language features now work in untitled files and files manually marked as Python.
-   The "remove unused imports" code action now handles multiple statements on the same line properly. ([pylance-release#1547](https://github.com/microsoft/pylance-release/issues/1547))
-   Support for native modules stored in `dist-packages` has been improved, including `numpy` when installed globally on Debian-based Linux distributions.
-   Support for `cv2` has been improved. ([pylance-release#1339](https://github.com/microsoft/pylance-release/issues/1339)), ([pylance-release#1609](https://github.com/microsoft/pylance-release/issues/1609))

In addition, Pylance's copy of Pyright has been updated from 1.1.161 to 1.1.162, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Bug Fix: Fixed false positive error relating to the use of a `*P.args` or `**P.kwargs` parameter as an iterable value (where `P` is a `ParamSpec`).
    -   Bug Fix: Fixed false positive error due to incomplete tracking of incomplete types during code flow evaluation.
    -   Bug Fix: Fixed bug with ParamSpec matching in the case where the matched function contains parameters with default values or `*args` / `**kwargs`;
    -   Bug Fix: Fixed false positive error that results when defining a property setter within an abstract base class and the property setter references a type that has a circular reference to the class. ([pylance-release#1683](https://github.com/microsoft/pylance-release/issues/1683))
    -   Bug Fix: Fixed a false positive error when handling `*args` and `**kwargs` arguments when the function contains `*P.args` and `**P.kwargs` parameters.
    -   Bug Fix: Fixed comparison operators so they use the proper opposite when looking for a type match. For example, the opposite of `__lt__` is `__ge__` rather than `__gt__`.
    -   Bug Fix: Fixed bug that caused inappropriate type narrowing if a comparison operator was used within an argument for a call expression which was, in turn, used within an `if` condition expression.
    -   Enhancement: Sort imports by import symbol type when auto-imports are applied. ([pylance-release#1675](https://github.com/microsoft/pylance-release/issues/1675))
-   [1.1.162](https://github.com/microsoft/pyright/releases/tag/1.1.162)
    -   Enhancement: Added support for unpacking of objects that derive from known-length tuples. This includes named tuples.
    -   Enhancement: Improved match statement code flow logic to handle the case where a pattern is exhausted prior to the last case statement.
    -   Enhancement: Improved "implied else" code flow logic to handle nested "implied else" constructs.
    -   Bug Fix: Fixed regression that affected type narrowing of subscript expressions for TypedDict objects.
    -   Bug Fix: Fixed false positive error caused by inappropriate method binding for instance methods.
    -   Enhancement (from pylance): Added more support in completion provide for literal expressions.
    -   Bug Fix: Changed registration of language server to allow for URI types other than files. This allows pyright to be activated when an untitled file is identified as a python source file.
    -   Bug Fix: Fixed false positive error when assigning to a subscript expression where the base type is a TypedDict.
    -   Bug Fix: Fixed false positive error when "\*P.args" parameter (where P is a ParamSpec) is passed as an argument to another function that accepts "P.args".
    -   Bug Fix: Added support for member access expressions where the attribute contains a class whose metaclass implements a descriptor protocol.
    -   Bug Fix: Fixed crash due to infinite recursion when a protocol class included a property getter that returned an instance of the same protocol class. ([pylance-release#1671](https://github.com/microsoft/pylance-release/issues/1671))
    -   Enhancement: Improved the readability of error messages related to protocol type mismatches.
    -   Bug Fix (from pylance): Fixed diagnostics for source files that are not on disk (e.g. "untitled" new documents).
    -   Enhancement (from pylance): Added support for attribute docstrings in hover text.

## 2021.8.1 (11 Aug 2021)

Notable changes:

-   More literal completions are now supported. ([pylance-release#1497](https://github.com/microsoft/pylance-release/issues/1497))
-   The bundled pandas stubs have been updated.
-   Pylance's copy of typeshed has been updated.
-   Creating new file in open file mode no longer causes a hang.

In addition, Pylance's copy of Pyright has been updated from 1.1.159 to 1.1.161, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Bug Fix: Fixed false positive error caused by inappropriate method binding for instance methods.
    -   Bug Fix: Fixed regression that affected type narrowing of subscript expressions for TypedDict objects.
    -   Enhancement: Improved "implied else" code flow logic to handle nested "implied else" constructs.
    -   Enhancement: Improved match statement code flow logic to handle the case where a pattern is exhausted prior to the last case statement.
    -   Enhancement: Added support for unpacking of objects that derive from known-length tuples. This includes named tuples. ([pylance-release#1658](https://github.com/microsoft/pylance-release/issues/1658))
-   [1.1.161](https://github.com/microsoft/pyright/releases/tag/1.1.161)
    -   Bug Fix: Fixed bug in declaration provider that caused declaration not to be found when it referred to a metadata method.
    -   Bug Fix: Fixed bug that resulted in a false when evaluating nested lambdas (i.e. a lambda that returns a lambda).
    -   Enhancement: Added support for bidirectional type inference for assignment expressions where the LHS is an index expression that indexes into a TypedDict instance. ([pylance-release#1645](https://github.com/microsoft/pylance-release/issues/1645))
    -   Enhancement: Added support for new type narrowing pattern for discriminating among tuples. The pattern is `V[I] == L` or `V[I] != L` where `I` is an integer literal, `L` is another literal value, `V` is a tuple with a known length and a type at index `I` that is declared as a literal type.
    -   Enhancement: Improved logging for import failures. The previous code was printing the same log message for both stub and non-stub package resolution attempts which resulted in seemingly redundant messages.
    -   Enhancement: Added heuristic to allow proper inference of list expressions when used as the RHS operand in an expression of the form `my_list + [x]`.
    -   Bug Fix: Fixed a bug that was masking some error messages when multiple errors were reported for the same range and their message started with the same 25 characters.
    -   Enhancement: Changed method and attribute override compatibility checks to check for inappropriate overrides of all base classes in the multi-inheritance case. Previously, this check used MRO, so some override mismatches were left unreported if they were obscured by another base class. The change also affects `@final` checks. ([pylance-release#1495](https://github.com/microsoft/pylance-release/issues/1495))
    -   Enhancement: Added support for descriptor protocols defined on metaclasses.
    -   Bug Fix: Fixed a bug that caused methods in generic classes to be specialized twice when accessed through a member access expression.
    -   Bug Fix: Fixed false positive error when accessing `__name__` instance variable in a class that derives from `type`.
    -   Enhancement: Updated typeshed stubs to the latest version.
-   [1.1.160](https://github.com/microsoft/pyright/releases/tag/1.1.160)
    -   Enhancement: Updated the "type(x) is y" type narrowing logic to handle the negative case when the class type is "final".
    -   Bug Fix: Fixed bug that prevented "rename symbol" from working when in single-file mode. Rather than failing, it will now perform a rename only within a single file.
    -   Enhancement: Updated typeshed stubs to the latest version.
    -   Bug Fix: Fixed false positive that occurs when defining an abstract dataclass and one of its fields refers to the class itself in its type annotation.
    -   Bug Fix: Fixed bug in `x is None` type narrowing logic when `x` was typed as `object`.
    -   Bug Fix: Fixed bug that verified that a protocol class used within an isinstance call is runtime_checkable. It was skipping this check when the first argument to isinstance was an Any or Unknown type.
    -   Bug Fix: Fixed bug where a union of Literal[False] and Literal[True] were being coalesced into bool inappropriately in the case where they were conditional types that came from a constrained TypeVar.
    -   Bug Fix: Removed the assumption that all top-level modules in typeshed third-party stubs are unique. The typeshed folder structure allows multiple packages to have the same top-level module.
    -   Bug Fix: Fixed bug in the handling of generic recursive type aliases.
    -   Enhancement: Implemented support for new Python 3.10 dataclass features: `kw_only` parameter for `dataclass` and `field` and `KW_ONLY` separator. ([pylance-release#1626](https://github.com/microsoft/pylance-release/issues/1626))

## 2021.8.0 (4 Aug 2021)

Notable changes:

-   Performance of completions for huggingface/transformers has been improved by adding partial stubs. ([pylance-release#1258](https://github.com/microsoft/pylance-release/issues/1258))
-   Variable renaming now works in open file mode. ([pylance-release#1300](https://github.com/microsoft/pylance-release/issues/1300))
-   Pylance's copy of typeshed has been updated.

In addition, Pylance's copy of Pyright has been updated from 1.1.158 to 1.1.159, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Bug Fix: Fixed bug in x is None type narrowing logic when x was typed as `object`.
    -   Bug Fix: Fixed false positive that occurs when defining an abstract dataclass and one of its fields refers to the class itself in its type annotation.
    -   Enhancement: Updated typeshed stubs to the latest version.
    -   Bug Fix: Fixed bug that prevented "rename symbol" from working when in single file mode. Rather than failing, it will now perform a rename only within a single file. ([pylance-release#1300](https://github.com/microsoft/pylance-release/issues/1300))
    -   Enhancement: Updated the "type(x) is y" type narrowing logic to handle the negative case when the class type is "final".
-   [1.1.159](https://github.com/microsoft/pyright/releases/tag/1.1.159)
    -   Bug Fix: Fixed bug that could lead to an internal stack overflow when a generic value was used as an argument for a function or class decorator.
    -   Enhancement: Added support in literal comparison type narrowing to filter out comparisons to "None" in positive case.
    -   Bug Fix: Fixed bug in parser where it was too permissive in allowing keywords to be used as identifiers. The Python interpreter is less permissive, so pyright's parser should match.
    -   Bug Fix: Fixed several bugs that caused crashes (dereference of undefined variable) in certain circumstances.
    -   Enhancement: Added a new log error for the case where enumeration of files within the workspace is taking longer than 10 seconds.
    -   Bug Fix: Fixed bug in tokenizer which treated 'constructor' as a keyword.
    -   Bug Fix: Fixed bug in "type(x) is y" type narrowing logic to handle the case where x is an instance of a generic class.
    -   Enhancement: Added check for illegal trailing comma in "from x import y," statement. This generates a syntax error at runtime.
    -   Enhancement: Added check for illegal use of "Protocol" as a type argument.
    -   Enhancement: Implemented new check for a class that is decorated with `@final` but does not implement all abstract methods from abstract classes that it derives from.
    -   Enhancement: Added check for inappropriate use of `ClassVar` that will generate runtime exceptions.
    -   Enhancement: Added logic to enforce protocol mismatches if a member in the protocol is marked "Final" and the class is not (or vice versa).
    -   Behavior Change: Modified assignment type narrowing for index expressions so it applies only to built-in types. This eliminates incorrect type inference when using a class that has assymetric `__setitem__` and `__getitem__` methods.
    -   Enhancement: Fixed false positive error when `@property` is combined with `@functools.cache`.

## 2021.7.7 (28 July 2021)

This is a hotfix release, fixing a tokenizer bug that caused identifiers called "constructor" to be mishandled.
([pylance-release#1618](https://github.com/microsoft/pylance-release/issues/1618))

## 2021.7.6 (28 July 2021)

Notable changes:

-   PEP 258 style "attribute docstrings" are now supported.
    ([pylance-release#1576](https://github.com/microsoft/pylance-release/issues/1576))
-   Attribute assignments that use reserved keywords now correctly cause a parser error.
-   A number of bugs that caused crashes in certain circumstances have been fixed.
    ([pylance-release#1597](https://github.com/microsoft/pylance-release/issues/1597))
-   The bundled stubs for django and pandas have been updated.

In addition, Pylance's copy of Pyright has been updated from 1.1.157 to 1.1.158, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Enhancement: Added a new log error for the case where enumeration of files within the workspace is taking longer than 10 seconds.
    -   Bug Fix: Fixed several bugs that caused crashes (dereference of undefined variable) in certain circumstances.
    -   Bug Fix: Fixed bug in parser where it was too permissive in allowing keywords to be used as identifiers. The Python interpreter is less permissive, so pyright's parser should match.
    -   Enhancement: Added PEP 570 to the list of supported type features.
    -   Enhancement: Added support in literal comparison type narrowing to filter out comparisons to "None" in positive case.
    -   Bug Fix: Fixed bug that could lead to an internal stack overflow when a generic value was used as an argument for a function or class decorator.
        ([pylance-release#1597](https://github.com/microsoft/pylance-release/issues/1597))
-   [1.1.158](https://github.com/microsoft/pyright/releases/tag/1.1.158)
    -   Bug Fix: Fixed handling of generic type aliases with missing type arguments used in type annotations when the type alias itself is a member access expression.
    -   Enhancement: Added new diagnostic check (controlled by the existing "reportUnsupportedDunderAll" config switch) that reports an issue with a name specified in `__all__` if that symbol does not exist at the module level.
    -   Enhancement: Updated typeshed stubs to latest version.
    -   Enhancement: Added support for nested callables that use a ParamSpec at each level.
    -   Bug Fix: Fixed false positive error related to the use of the `Final` keyword when annotating attributes within a dataclass.
    -   Bug Fix: Fixed bug in TypeVar matching logic that allowed Type[T] to be matched against an instance of a type.
    -   Behavior Change: Changed type checking logic for functions to allow a function with a return result of `NoReturn` to match against any other return type.
    -   Bug Fix: Fixed false positive error in parser dealing with f-strings with string literals within the f-string expression that, in turn, have quotes within the string literal.
    -   Enhancement: Added support for "attribute docstrings" (defined in PEP 258) in completion provider.
        ([pylance-release#1576](https://github.com/microsoft/pylance-release/issues/1576))
    -   Bug Fix: Fixed bug in type analyzer related to a TypeVar with a bound type that is a union.

## 2021.7.5 (22 July 2021)

Notable changes:

-   Triple-quote closing now works correctly in LiveShare with multiple cursors.
    ([pylance-release#1583](https://github.com/microsoft/pylance-release/issues/1583))
-   A parser bug with f-strings containing nested strings has been fixed.
    ([pylance-release#1584](https://github.com/microsoft/pylance-release/issues/1584))
-   A new "reportUninitializedInstanceVariable" diagnostic check looks for instance variables that are not initialized in the class body or constructor.
-   The bundled stubs for django and pandas have been updated.
-   Pylance's copy of typeshed has been updated.

In addition, Pylance's copy of Pyright has been updated from 1.1.156 to 1.1.157, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Behavior Change: Changed type checking logic for functions to allow a function with a return result of `NoReturn` to match against any other return type.
    -   Bug Fix: Fixed false positive error in parser dealing with f-strings with string literals within the f-string expression that, in turn, have quotes within the string literal.
    -   Bug Fix: Fixed bug in TypeVar matching logic that allowed `Type[T]` to be matched against an instance of a type.
    -   Bug Fix: Fixed false positive error related to the use of the Final keyword when annotating attributes within a dataclass.
        ([pylance-release#1574](https://github.com/microsoft/pylance-release/issues/1574))
    -   Enhancement: Added support for nested callables that use a ParamSpec at each level.
    -   Enhancement: Updated typeshed stubs to latest version.
    -   Enhancement: Updated docs for reportUnsupportedDunderAll.
    -   Enhancement: Added new diagnostic check (controlled by the existing "reportUnsupportedDunderAll" config switch) that reports an issue with a name specified in `__all__` if that symbol does not exist at the module level.
    -   Bug Fix: Fixed handling of generic type aliases with missing type arguments used in type annotations when the type alias itself is a member access expression.
        ([pylance-release#1565](https://github.com/microsoft/pylance-release/issues/1565))
-   [1.1.157](https://github.com/microsoft/pyright/releases/tag/1.1.157)
    -   Bug Fix: Fixed false positive error when calling an object that has an `Any` in its inheritance chain.
    -   Enhancement: Improved support for `callable` type narrowing in cases where the type is a non-callable instance, but a subtype could be callable.
    -   Enhancement: Improved handling of `callable` type narrowing when the type involves a constrained type variable.
    -   Enhancement: Added support for ParamSpec's within a Protocol, which is supported in Python 3.10.
    -   Enhancement: Improved handling of `isinstance` type narrowing logic when the type being narrowed is a callable.
    -   Bug Fix: Fixed recent regression in type evaluator that occurs when a generic (non-specialized) type is assigned to another generic type and the type parameter(s) for the generic type are invariant.
    -   Bug Fix: Fixed bug that caused diagnostics from an open file not to be cleared after closing that file if it was not saved.
    -   Enhancement (from pylance): Improved completion suggestions for literals when used as dictionary keys.
    -   New Feature: Implemented "reportUninitializedInstanceVariable" diagnostic check that looks for instance variables that are not initialized in the class body or constructor.
    -   Bug Fix: Fixed false positive error due to bug in constraint solver related to the handling of `Type[T]` when `T` is a constrained type variable.
    -   Bug Fix: Fixed false positive error related to the use of a recursive type alias when `from __future__ import annotations` was in effect.
    -   Bug Fix: Fixed false negative related to augmented assignment expressions when operand was a union type and a subset of the union subtypes were not supported for the operation.

## 2021.7.4 (15 July 2021)

This is a hotfix release, fixing an error message that could appear when the "add to extraPaths" code action was used.

## 2021.7.3 (14 July 2021)

Notable changes:

-   Fixed bug that caused diagnostics from an open file not to be cleared after closing that file if it was not saved.
    ([pylance-release#1514](https://github.com/microsoft/pylance-release/issues/1514))
-   Fixed document highlight regression when selecting a class attribute.
    ([pylance-release#1500](https://github.com/microsoft/pylance-release/issues/1500))
-   Dictionary key completions now support non-string literals.
    ([pylance-release#1493](https://github.com/microsoft/pylance-release/issues/1493))
-   The bundled stubs for django and pandas have been updated.

In addition, Pylance's copy of Pyright has been updated from 1.1.155 to 1.1.156, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Bug Fix: Fixed bug that caused diagnostics from an open file not to be cleared after closing that file if it was not saved.
        ([pylance-release#1514](https://github.com/microsoft/pylance-release/issues/1514))
    -   Bug Fix: Fixed recent regression in type evaluator that occurs when a generic (non-specialized) type is assigned to another generic type and the type parameter(s) for the generic type are invariant.
        ([pylance-release#1526](https://github.com/microsoft/pylance-release/issues/1526))
    -   Enhancement: Improved handling of isinstance type narrowing logic when the type being narrowed is a callable
    -   Enhancement: Added support for ParamSpec's within a Protocol, which is supported in Python 3.10.
    -   Enhancement: Improved support for callable type narrowing in cases where the type is a non-callable instance, but a subtype could be callable.
    -   Bug Fix: Fixed false positive error when calling an object that has an Any in its inheritance chain.
-   [1.1.156](https://github.com/microsoft/pyright/releases/tag/1.1.156)
    -   Bug Fix: Fixed false positive error related to member access of optional type.
    -   Bug Fix: Fixed false positive error related to an escape sequence (backslash) used in an f-string format specifier.
    -   Bug Fix: Fixed false positive error with f-string format specifier that contains an expression within braces and also a colon specifier.
    -   Enhancement: Updated typeshed stubs to latest version.
    -   Bug Fix: Fixed false positive error when evaluating a subscript (index) operation with an index value that is a union type and an overloaded `__getitem__` method that requires union expansion.
    -   Enhancement: Added new check for a function overload that contains an implementation.
    -   Enhancement: Added special-case handling for addition of two tuples that have known lengths.
    -   Bug Fix: Fixed bug in check that detects improper variance for type variables used within generic protocols. Class or instance variables within a generic protocol must use invariant type variables.
    -   Enhancement: Improved heuristics for type matching when source and dest types are unions and invariance is being enforced — specifically in the case where the destination union type includes generic types.

## 2021.7.2 (7 July 2021)

This is a hotfix release, fixing a completion regression introduced in 2021.6.3.

## 2021.7.1 (6 July 2021)

Notable changes:

-   The bundled PIL stubs have been removed, as they have been merged into typeshed's Pillow stubs.

## 2021.7.0 (6 July 2021)

Notable changes:

-   An "add to extraPaths" quick fix for unresolved imports has been added, which suggests and adds potential paths `python.analysis.extraPaths`.
-   Support for the undocumented "mspythonconfig.json" config file name has been removed. This was previously available as an alternative to "pyrightconfig.json", but we've decided to standardize on the latter.

In addition, Pylance's copy of Pyright has been updated from 1.1.152 to 1.1.155, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Enhancement: Updated to the latest version of typeshed
    -   Bug Fix: Fixed false positive error with f-string format specifier that contains an expression within braces and also a colon specifier.
        ([pylance-release#1522](https://github.com/microsoft/pylance-release/issues/1522))
    -   Bug Fix: Fixed false positive error related to an escape sequence (backslash) used in an f-string format specifier.
    -   Bug Fix: Fixed false positive error related to member access of optional type.
-   [1.1.155](https://github.com/microsoft/pyright/releases/tag/1.1.155)
    -   Bug Fix: Fixed recent regression that resulted in false positive errors when a class declaration used both `Type[X]` and `X` in its specialization of base classes.
    -   Bug Fix: Fixed false positive error related to `isinstance` narrowing of a non-constrained TypeVar.
    -   Bug Fix: Changed encoding of literals in error messages to avoid including raw (unescaped) special characters in output.
    -   Behavior Change: Increased maximum source file size from 16MB to 32MB.
        ([pylance-release#1520](https://github.com/microsoft/pylance-release/issues/1520))
    -   Enhancement: Improved formatting of error messages that include expressions — specifically when the expression includes an empty dict ("{}").
    -   Bug Fix: Fixed false positive error for the case where a function with positional/keyword parameters is assigned to a callback protocol that accepts only keyword parameters.
    -   Enhancement: Added support for member access expressions for the `None` object.
    -   Enhancement: Added support for `isinstance` and `issubclass` type narrowing where the variable type and the test type have no apparent relationship. The type evaluator synthesizes a class that is a subclass of both types — effectively an "intersection" of the two.
        ([pylance-release#1499](https://github.com/microsoft/pylance-release/issues/1499))
    -   Behavior Change: Modified `reportUnnecessaryIsInstance` diagnostic to never report always-false conditions because the type checker no longer generates such conditions.
        ([pylance-release#1496](https://github.com/microsoft/pylance-release/issues/1496))
-   [1.1.154](https://github.com/microsoft/pyright/releases/tag/1.1.154)
    -   Removed support for undocumented "mspythonconfig.json" config file name. This was previously available as an alternative to "pyrightconfig.json", but we've decided to standardize on the latter.
    -   Bug Fix: Changed logic for "overload missing implementation" check to not require an implementation within a protocol class.
    -   Enhancement: Updated typeshed stubs to latest version.
    -   Bug Fix: Fixed confusing error message when file or directory is specified on command line but is excluded by the "exclude" section of the config file.
    -   Behavior Change: Exempt classes from `__slots__` check if they explicitly declare an empty slots. This is commonly used for mix-in classes that are compatible with slotted classes.
    -   Internal Change: This version of pyright includes a significant change within the type evaluator that simplifies the code and eliminates a major source of bugs related to the handling of `Type[X]` type annotations.
-   [1.1.153](https://github.com/microsoft/pyright/releases/tag/1.1.153)
    -   Bug Fix: Fixed type evaluation bug where `Callable` is used to annotate an input parameter, and the `Callable` return type is a union that contains a type variable and the type variable is used within a nested function.
    -   Bug Fix: Fixed bug in "isinstance" type narrowing logic and in the "unnecessary isinstance" diagnostic check when the type being narrowed is a runtime-checkable protocol instance.
    -   Bug Fix: Fixed bug in type evaluator that resulted in a false positive error when a `__getattr__` was supplied in a metaclass, and it returned a generic callable type.
        ([pylance-release#1481](https://github.com/microsoft/pylance-release/issues/1481))
    -   Enhancement: Added validation for assignment of instance variables that are not declared in `__slots__`.
    -   Enhancement: Added check for class variables that conflict with an instance variable declared in `__slots__` within a class.
    -   Behavior Change: When displaying overloaded functions in hover text, filter out the implementation signature.
        ([pylance-release#1498](https://github.com/microsoft/pylance-release/issues/1498))
    -   Bug Fix: Fixed bug in code flow engine that caused incorrect type evaluation of complex expression that appears multiple times within a function in contexts where `isinstance` type narrowing generates different types for the same expression.

## 2021.6.3 (23 June 2021)

Notable changes:

-   Absolute imports of local files are now supported in "open file" mode.
-   Extract method/variable will now also trigger a rename on the newly generated symbol.
-   Pylance will now auto-close triple quoted strings.
-   Dictionary key completions that contain non-alpha characters will now work correctly.
    ([pylance-release#1460](https://github.com/microsoft/pylance-release/issues/1460))
-   Completions on nested TypedDicts will now work correctly.
    ([pylance-release#1485](https://github.com/microsoft/pylance-release/issues/1485))
-   The bundled stubs for matplotlib, django, openpyxl, and pandas have been updated.

In addition, Pylance's copy of Pyright has been updated from 1.1.149 to 1.1.152, including the following changes:

-   [1.1.152](https://github.com/microsoft/pyright/releases/tag/1.1.152)
    -   Bug Fix: Fixed false positive error involved in the instantiation of `type(self)()` within an abstract class.
    -   Bug Fix: Fixed parser bug that caused completion provider to not work correctly when completing relative imports ending in a dot.
        ([pylance-release#1479](https://github.com/microsoft/pylance-release/issues/1479))
    -   Bug Fix: Fixed bug that led to false positive error related to dictionary unpacking when the argument type is a type variable.
        ([pylance-release#1463](https://github.com/microsoft/pylance-release/issues/1463))
    -   Bug Fix: Fixed false positive error when using `del` keyword with a tuple expression.
        ([pylance-release#1480](https://github.com/microsoft/pylance-release/issues/1480))
    -   Bug Fix: Fixed bug in completion provider where it was interpreting prior quotes incorrectly when completing a typed dictionary key, most easily reproducible when using nested typed dictionaries.([pylance-release#1485](https://github.com/microsoft/pylance-release/issues/1485))
    -   Bug Fix: Eliminated false positive error for `Final` when it doesn't include a type argument.
    -   Bug Fix: Fixed several possible causes of stack overflow crashes in the type evaluator.
        ([pylance-release#1464](https://github.com/microsoft/pylance-release/issues/1464))
    -   Bug Fix (from pylance): Fixed bug in completion provider related to dictionary key completions that contain non-alpha characters.
        ([pylance-release#1460](https://github.com/microsoft/pylance-release/issues/1460))
    -   Bug Fix: Fixed false positive error when `super()` was used in a static or class method and the target function in the base class had an annotated cls parameter.
        ([pylance-release#1488](https://github.com/microsoft/pylance-release/issues/1488))
-   [1.1.151](https://github.com/microsoft/pyright/releases/tag/1.1.151)
    -   Enhancement: Added support for metaclasses that support the `__getitem__`, `__setitem__` and `__delitem__` magic methods, allowing classes that derive from these metaclasses to be used in index expressions.
    -   Bug Fix: Fixed bug that caused dataclass usage to break in Python 3.6 and older when using the polyfill library.
    -   Enhancement: Added conditional type support for `__setitem__` so a value with a type defined by a constrained TypeVar can be assigned to an index expression.
    -   Bug Fix: Fixed bug that caused a crash in the tokenizer when encountering a string literal that is extremely long (>100K in length).
    -   Bug Fix: Fixed bug caused by a variable assignment with a list expression on the RHS that was interpreted temporarily as a type alias declaration. Added more sanity checking on the type of the assigned expression for type aliases.
    -   Bug Fix: Fixed type evaluation bug where `Callable` is used to annotate an input parameter, and the `Callable` return type is a union that contains a type variable.
    -   Bug Fix: Fixed bug in constraint solver relating to replacement of return type of the form T when matching was performed against Type[T].
    -   Enhancement: Added support for `__builtins__` module symbol symbol.
    -   Enhancement: Added support for type narrowing conditional expressions of the form `a is False`, `a is True`, `a is not False` and `a is not True`.
-   [1.1.150](https://github.com/microsoft/pyright/releases/tag/1.1.150)
    -   Enhancement: Avoid completion suggestions when typing an ellipsis. (Thanks to contribution from Marc Mueller.)
    -   Bug Fix: Fixed false positive errors relating to unions created from a `Type[T]` type.
        ([pylance-release#1468]https://github.com/microsoft/pylance-release/issues/1468))
    -   Bug Fix: Fixed bug that caused class docString not to appear in signature help when invoking constructor for classes with synthesized constructor methods (e.g. dataclass or namedtuple).
    -   Behavior Change: Changed `reportPrivateUsage` diagnostic check to suppress the check when method or attribute comes from a type stub file. It is presumably part of the public interface contract in this case and not a private or protected member.
        ([pylance-release#1478](https://github.com/microsoft/pylance-release/issues/1478))
    -   Enhancement: Added completion suggestion support for dictionary key names.
    -   Bug Fix: Fixed bug in type evaluator that resulted in incorrect type in certain cases when evaluating function with declared return type of `Type[T]`.
        ([pylance-release#1462](https://github.com/microsoft/pylance-release/issues/1462))
    -   Bug Fix: Fixed false positive error that occurred when evaluating a binary operation provided by a metaclass when the LHS or RHS type was a `Type[T]`.
    -   Behavior Change: In basic type checking mode, enabled the following diagnostic checks by default: reportOptionalSubscript, reportOptionalMemberAccess, reportOptionalCall, reportOptionalIterable, reportOptionalContextManager, and reportOptionalOperand.
    -   Bug Fix: Fixed crashing bug in document symbol provider when handling import statements.
    -   Bug Fix: Fixed type evaluation bug that affected the specialization of a generic type alias that includes a bound TypeVar.

## 2021.6.2 (16 June 2021)

Notable changes:

-   Pylance will now offer completions inside dictionary key context if that dictionary was defined in the current scope.
-   The bundled stubs now include partial stubs for sympy.
    ([pylance-release#1388](https://github.com/microsoft/pylance-release/issues/1388), [pylance-release#946](https://github.com/microsoft/pylance-release/issues/946))

In addition, Pylance's copy of Pyright has been updated from 1.1.148 to 1.1.149, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Behavior Change: Changed reportPrivateUsage diagnostic check to suppress the check when method or attribute comes from a type stub file. It is presumably part of the public interface contract in this case and not a private or protected member.
        ([pylance-release#1454](https://github.com/microsoft/pylance-release/issues/1454))
    -   Bug Fix: Fixed bug that caused class docString not to appear in signature help when invoking constructor for classes with synthesized constructor methods (e.g. dataclass or namedtuple).
        ([pylance-release#640](https://github.com/microsoft/pylance-release/issues/640))
    -   Bug Fix: Fixed false positive errors relating to unions created from a `Type[T]` type
        ([pylance-release#1422](https://github.com/microsoft/pylance-release/issues/1422))
    -   Enhancement: Return empty completionList for Ellipsis
-   [1.1.149](https://github.com/microsoft/pyright/releases/tag/1.1.149)
    -   Bug Fix (from pylance): Fixed crash that can occur when a library is installed in the form of a zip file, and that zip file is malformed.
        ([pylance-release#1421](https://github.com/microsoft/pylance-release/issues/1421))
    -   Bug Fix: Fixed bug that caused false positive error when using a generic type alias as a constructor call.
    -   Enhancement: Added check for illegal use of "async" keyword. The Python interpreter generates a syntax error if it is used outside of an async function.
    -   Enhancement: Tweaked heuristics in constraint solver for dealing with matching of TypeVar T for the type expression `Union[T, SomeClass[T]]`. There are two valid solutions if the argument is type `SomeClass-[X]`, but the "simpler" solution (`T = X`) should be preferred over the more complex (`T = SomeClass[X]`).
    -   Bug Fix: Fixed bug in type checker related to the use of a TypeVar or ParamSpec within an inner function when it is already bound to an outer function but used only within that outer function's return type a nnotation.
    -   Bug Fix: Added error handling for very large source files. This situation is now detected earlier so we don't attempt to load the file contents and crash the language server in the process.
        ([pylance-release#1426](https://github.com/microsoft/pylance-release/issues/1426))
    -   Behavior Change: Added logic to convert `Type[A | B]` into `Type[A] | Type[B]`, which avoids violating assumptions elsewhere in the type checker.
    -   Enhancement: Updated to the latest version of typeshed, which includes support for ParamSpec in contextlib's contextmanager function.
        ([pylance-release#516](https://github.com/microsoft/pylance-release/issues/516))
    -   Bug Fix: Fixed bug in type checker that occurred in some cases when a generic function returned `Type[T]`. In some cases where an input parameter also had an annotation of `Type[T]`, the "solved" type was wrapped in `Type` twice (e.g. `Type[Type[int]]`).
        ([pylance-release#1437](https://github.com/microsoft/pylance-release/issues/1437))
    -   Bug Fix: Fixed bug in type evaluator that occurred when calling a constructor of type `Type[T]` where `T` is a constrained TypeVar.
    -   Bug Fix: Fixed bug that resulted in an import being marked as unaccessed if it was accessed within a class declaration but was also redeclared within the class scope.

## 2021.6.1 (9 June 2021)

Notable changes:

-   Search paths returned by the Python interpreter are now normalized according to the case provided by the OS.
    ([pylance-release#1375](https://github.com/microsoft/pylance-release/issues/1375))
-   An error related to file watcher creation will no longer appear.
    ([pylance-release#1392](https://github.com/microsoft/pylance-release/issues/1392))
-   Pylance will no longer crash at startup when an invalid zip or egg file are present in the workspace.
    ([pylance-release#1397](https://github.com/microsoft/pylance-release/issues/1397))
-   Match/case statements will now be checked for exhaustiveness.
    ([pylance-release#1380](https://github.com/microsoft/pylance-release/issues/1380))

In addition, Pylance's copy of Pyright has been updated from 1.1.146 to 1.1.148, including the following changes:

-   [1.1.148](https://github.com/microsoft/pyright/releases/tag/1.1.148)
    -   Enhancement: Improved type narrowing of subject expression in a match statement when none of the case statements match the pattern and the code falls through the bottom of the match.
    -   Enhancement: Added support for pattern matching exhaustion detection in cases where there is not an explicit irrefutable pattern present.
        ([pylance-release#1380](https://github.com/microsoft/pylance-release/issues/1380))
    -   Bug Fix: Fixed recent regression that resulted in false positive errors when attempting to instantiate `tuple` or `type` directly.
    -   Enhancement: Improved type checking for classes that are assigned to `Callable` types. Previously, type incompatibilities were not reported if the `__init__` or `__new__` methods were overloaded within the class.
        ([pylance-release#1400](https://github.com/microsoft/pylance-release/issues/1400))
    -   Bug Fix: Fixed bug that caused parser error when handling a carriage return within a triple-quoted inner string within an outer triple-quoted f-string.
        ([pylance-release#1401](https://github.com/microsoft/pylance-release/issues/1401))
    -   Bug Fix: Fixed bug that resulted in false positive error when second argument to `NewType` call contained a `Type` object.
        ([pylance-release#1406](https://github.com/microsoft/pylance-release/issues/1406))
    -   Bug Fix: Fixed recent regression that resulted in a false positive error when instantiating a variable of type `Type[T]` where `T` was a protocol class.
    -   Bug Fix: Fixed bug in type printer that resulted in double parentheses around return type expressions when they involved unions.
    -   Bug Fix: Fixed bug that resulted in a false positive error when using generic `Type[T]` in a function parameter in overload validation.
        ([pylance-release#1407](https://github.com/microsoft/pylance-release/issues/1407))
    -   Bug Fix: Fixed bug in type checker relating to constrained type variables that combine non-union and union constraints.
        ([pylance-release#1412](https://github.com/microsoft/pylance-release/issues/1412))
    -   Bug Fix: Fixed bug in type checker when handling Final variables assigned at the class level. PEP 591 indicates that they should be treated as though they are annotated as ClassVar even though they are not.
    -   Bug Fix: Fixed a bug in the type checker relating to the use of a specialized generic class that is parameterized by a ParamSpec.
-   [1.1.147](https://github.com/microsoft/pyright/releases/tag/1.1.147)
    -   Enhancement: Added check for an attempt to instantiate a protocol class. This causes a runtime error.
    -   Behavior Change: Closed a hole in type narrowing for "in" operator when used with TypedDict. It can eliminate types from a union only if the type is marked final.
    -   Enhancement: Changed type printer to handle recursion differently — most notably when dealing with recursive type aliases. If it is asked to expand type aliases, it now expands only the first level of a given type alias, so if there's recursion, it will use the type alias name the second time it is encountered rather than continuing to expand it.
    -   Enhancement: Changed `reveal_type` and `reveal_locals` to expand type aliases in their output.
    -   Bug Fix: Fixed bug that resulted in incorrect type checking behavior when a type annotation involved a tuple with literal elements.
    -   Bug Fix: Fixed bug that affected the handling of a function decorator that uses ParamSpec when applied to a classmethod or staticmethod.
    -   Enhancement: Added diagnostic for an attempt to instantiate a special type like a Union, Callable, or Optional.
    -   Bug Fix: Improved support for generic functions that annotate a parameter and a return type with a union that includes a TypeVar. In such cases, the TypeVar may not be matched during constraint solving.
    -   Enhancement: Improved hover text for type variables and param specs by updating the label so they are not shown simply as type aliases.
    -   Enhancement: Updated to the latest typeshed stubs.

## 2021.6.0 (2 June 2021)

Notable changes:

-   Libraries installed via egg/zip files are now supported (including `transformers` installed via `conda`).
    ([pylance-release#1260](https://github.com/microsoft/pylance-release/issues/1260))
-   Unannotated decorators are now treated as no-ops, rather than using type inference and potentially obscuring the signature of the function they decorate.
-   Files that were referenced but unopened will no longer be mistakenly reanalyzed when opened.
-   Tables in docstrings are now better spaced.
-   The bundled stubs for django have been updated.
-   Pylance's copy of typeshed has been updated.

In addition, Pylance's copy of Pyright has been updated from 1.1.144 to 1.1.146, including the following changes:

-   [1.1.146](https://github.com/microsoft/pyright/releases/tag/1.1.146)
    -   Enhancement: Updated to the latest version of typeshed stubs.
    -   Behavior Change: Updated `reportIncompatibleVariableOverride` to avoid reporting an error when a class variable is reassigned a value in a base class without declaring its type.
    -   Bug Fix: Fixed false positive error indicating that a type alias is a variable. This results when a type alias refers to a union and that union is reformed when losing the original type alias.
    -   Enhancement: Added optimization for union creation where all subtypes are the same. This optimization commonly reduces the need to create new types during code flow operations. It also retains type alias info more faithfully.
    -   Enhancement: Added support for `__qualname__` and `__module__` attributes within a class body.
        ([pylance-release#1376](https://github.com/microsoft/pylance-release/issues/1376))
    -   Behavior Change: Changed call expression evaluation logic to not skip return type inference when there are errors detected during argument expression evaluation. This was previously added as an optimization, but it was leading to confusing results in some cases.
    -   Enhancement: Enhanced logic to detect unannotated decorator functions and treat them as no-ops rather than using return type inference, which often leads to incorrect and confusing results for decorators.
    -   Bug Fix: Fixed bug in pattern matching logic for class patterns where the class uses properties or descriptors for the targeted attributes.
    -   Enhancement (from pylance): Added support for libraries packages as zip/egg containers.
-   [1.1.145](https://github.com/microsoft/pyright/releases/tag/1.1.145)
    -   Bug Fix: Fixed bug that resulted in the incorrect type when bidirectional type inference (an "expected type") was used in conjunction with the `tuple()` constructor.
        ([pylance-release#1359](https://github.com/microsoft/pylance-release/issues/1359))
    -   Behavior Change: Changed logic to avoid reanalyzing a file when it is opened in the editor if we have already analyzed it and the file contents are the same as before.
    -   Bug Fix: Improved handling of call expressions where the call is a union and some of the subtypes return NoReturn and others do not.
    -   Behavior Change: Changed the logic that validates the assignment to instance variables that are marked `Final`. Previously, only one such assignment was allowed even if it was within an `__init__` method. It now allows an arbitrary number of assignments (conditional or otherwise) as long as they occur within an `__init__` method.
    -   Enhancement: Enhanced "reportIncompatibleVariableOverride" diagnostic check to detect the case where a base class declares a class variable and a child class tries to override it with an instance variable or vice versa.
    -   Bug Fix: Added logic to handle the case where a dataclass subclass overrides a member of its parent class with a ClassVar and another dataclass then subclasses from the child.
    -   Enhancement: Enhanced type stub generator so it doesn't emit "object" as base class, since that's implied in Python 3.x.
    -   Enhancement: Enhanced type stub generator to emit inferred function and method return types as comments.
    -   Behavior Change: Removed false positive error reported for a "bare" `raise` statement outside of an `except` clause.
        ([pylance-release#1365](https://github.com/microsoft/pylance-release/issues/1365))
    -   Bug Fix: Changed type variable constraint solver to preserve literal types when matching type arguments from other class types. In other cases, it typically "strips" the literal, widening the type to a str, int, etc. This change allows proper type evaluation in certain cases where a literal type is specified in a type annotation, such as with `Set[Literal["foo"]]`.
    -   Bug Fix: Fixed bug in code flow engine where it was sometimes evaluating the wrong type when cycles occurred in type dependencies.
        ([pylance-release#1356](https://github.com/microsoft/pylance-release/issues/1356))
    -   Bug Fix: Fixed bug that can result in a crash when indexing a file that includes a nested function or lambda that is used for type inference.
    -   Enhancement: Improved detection and reporting of illegal type alias recursion cases — e.g. when a possible type alias refers to a function that uses the type alias in parameter or return type annotations.
    -   Enhancement: Changed type printer to include a "\*" after a type if it is conditionally associated with a TypeVar constraint.
    -   Bug Fix: Augmented type checking logic for generator expressions to allow `await` keyword even though enclosing function isn't async. Also allowed generator expression to be evaluated as `AsyncGenerator` rather normal `Generator`.
        ([pylance-release#1348](https://github.com/microsoft/pylance-release/issues/1348))
    -   Enhancement: Changed the way conditional constraints are tracked in the type evaluator. This is a significant change that simplifies the logic and handles some cases that the old approach did not.

## 2021.5.4 (26 May 2021)

Notable changes:

-   Auto-import quick fixes now more closely match auto-import completions.
    ([pylance-release#1250](https://github.com/microsoft/pylance-release/issues/1250))
-   TypedDict support has been improved, supporting `**kwargs` unpacking checks and tagged union narrowing.
    ([pylance-release#374](https://github.com/microsoft/pylance-release/issues/374), [pylance-release#1328](https://github.com/microsoft/pylance-release/issues/1328), [pylance-release#1240](https://github.com/microsoft/pylance-release/issues/1240))
-   A bug that led to infinite recursion has been fixed.
    ([pylance-release#1315](https://github.com/microsoft/pylance-release/issues/1315))
-   Memory usage when indexing is enabled has been improved.
-   The bundled stubs for pandas have been updated.
-   The bundled stubs now include partial stubs for `gym`.

In addition, Pylance's copy of Pyright has been updated from 1.1.141 to 1.1.144, including the following changes:

-   [1.1.144](https://github.com/microsoft/pyright/releases/tag/1.1.144)
    -   Bug Fix: Changed CLI to not use process.exit() but instead return normally. The previous code sometimes resulted in truncated output.
    -   Enhancement: Added error for keyword-only parameter separator or position-only parameter separator appearing in a function signature after an "\*args" parameter. This will result in a runtime error.
        ([pylance-release#1341](https://github.com/microsoft/pylance-release/issues/1341))
    -   Enhancement: Improved error message for missing \*\*kwargs parameter when assigning one function to another.
    -   Bug Fix: Fixed bug in logic that converts a type into a text representation. It wasn't properly adding the scope for a ParamSpec in certain circumstances, so instead of outputting `P@scope`, it was outputting `P`.
    -   Bug Fix: Fixed bug in specialization of generic class that contains only one type variable that is a ParamSpec.
    -   Bug Fix: Fixed bugs that prevented ParamSpec annotations `P.args` and `P.kwargs` from working properly when the annotation was in quotes.
    -   Bug Fix: Fixed false positive error in check for inappropriate use of contravariant type var in return type annotation. It should not generate an error when the contravariant type var is part of a union.
    -   Enhancement: Improved error message consistency for for "cannot assign to None" condition.
-   [1.1.143](https://github.com/microsoft/pyright/releases/tag/1.1.143)
    -   Bug Fix: Added missing recursion check that resulted in stack overflow in type evaluator.
        ([pylance-release#1315](https://github.com/microsoft/pylance-release/issues/1315))
    -   Enhancement: Added support for unpacked dictionary argument in function calls when the unpacked expression is a TypedDict.
        ([pylance-release#374](https://github.com/microsoft/pylance-release/issues/374), [pylance-release#1328](https://github.com/microsoft/pylance-release/issues/1328))
    -   Enhancement: Improved error message for the case where positional-only parameters are used in a function and a caller does not provide enough arguments.
    -   Bug Fix: Improved logic for argument matching for call expressions where the call includes keyword-only parameters and the call expression includes an unpacked list argument.
        ([pylance-release#1319](https://github.com/microsoft/pylance-release/issues/1319))
    -   Bug Fix: Fixed bug in type evaluation of list comprehensions when literal types were involved. The literal types were being widened to their associated non-literal types.
    -   Enhancement: Improved `isinstance` type narrowing logic to accommodate the case where the first argument to `isinstance` is a module and the second argument is a runtime-checkable protocol class.
    -   Bug Fix: Fixed regression that caused false positive in the case where a `Callable` type was used that defined its own TypeVar scope and was later matched against a `self` parameter in an instance method.
    -   Enhancement: Enhanced "reportIncompatibleVariableOverride" diagnostic check so it applies to instance variables defined within a method (e.g. `self.var: str = ""`) in addition to class variables.
    -   Enhancement: Added type narrowing support for index expressions where the index value is a string literal.
    -   Enhancement: Added support for "tagged union" type narrowing when the conditional expression is of the form `x[K] == V` or `x[K] != V` where `x` is a union of TypedDict objects and `K` is a literal str key value that refers to a field with a literal type and `V` is a literal value.
        ([pylance-release#1240](https://github.com/microsoft/pylance-release/issues/1240))
-   [1.1.142](https://github.com/microsoft/pyright/releases/tag/1.1.142)
    -   Bug Fix: Fixed false negative (missing error) due to bug in dictionary expression bidirectional type inference logic when the expected type included a union.
    -   Enhancement: Added support for subscript expressions that contain slices when applied to tuples with known lengths.
    -   Bug Fix: Fixed false negative condition where a protocol class was treated as a callback protocol even though it included members other than `__call__`.
    -   Bug Fix: Fixed false positive error when a builtin symbol was used in a file but later redeclared within the module scope.
        ([pylance-release#1320](https://github.com/microsoft/pylance-release/issues/1320))
    -   Bug Fix: Fixed bug in "expression printer" which is used in some error messages. It was not properly preserving parentheses for binary operation expressions.
    -   Bug FIx: Fixed false positive error for "missing type arguments" that was surfaced when changes were made within typeshed's types.pyi stub.

## 2021.5.3 (19 May 2021)

Notable changes:

-   A number of CPU and memory improvements have been made, improving parsing, indexing, and overall performance.
-   Libraries which indicate that they are `py.typed` will now be correctly preferred over typeshed, following PEP 561. This allows the use of the types in well-typed libraries such as the newly-released Flask 2.0, PyJWT, and tornado, improving completions, hover, navigation, and the type checking experience.
    ([pylance-release#1197](https://github.com/microsoft/pylance-release/issues/1197))
-   Auto-imports now require the first character to match before fuzzy matching is applied, which reduces the number of unwanted completions and greatly improves performance when indexing is enabled.
-   Extract method now supports extracting comments.
    ([pylance-release#1262](https://github.com/microsoft/pylance-release/issues/1262))
-   Variable names using supplementary characters are now supported.
    ([pylance-release#1286](https://github.com/microsoft/pylance-release/issues/1286))
-   Tables in docstrings are now supported.
-   Incompatible type diagnostics will now fully qualify type names if the incompatible types have the same short name.
    ([pylance-release#1306](https://github.com/microsoft/pylance-release/issues/1306))
-   A bug which caused some imports from `pywin32` to not be resolved has been fixed.
    ([pylance-release#1423](https://github.com/microsoft/pylance-release/issues/1423))
-   Added stubs for pywin32, openpyxl.
    ([pylance-release#947](https://github.com/microsoft/pylance-release/issues/947), [pylance-release#1423](https://github.com/microsoft/pylance-release/issues/1423))
-   The bundled stubs for django and pandas have been updated.
-   File watcher events from `.git` directories will no longer trigger reanalysis.
    ([pylance-release#1282](https://github.com/microsoft/pylance-release/issues/1282))
-   The import resolver now supports typeshed's VERSIONS file, which indicates which versions of Python each standard library module is available.
-   Pylance's copy of typeshed has been updated.

In addition, Pylance's copy of Pyright has been updated from 1.1.137 to 1.1.141, including the following changes:

-   [1.1.141](https://github.com/microsoft/pyright/releases/tag/1.1.141)
    -   Enhancement: Improved "is None" and "is not None" type narrowing logic for constrained TypeVars that include `None` as one of the constraints.
    -   Enhancement: Improved error message for illegal character in token and surrogate character codes combinations that are not allowed in identifiers.
    -   Enhancement: Added support for more surrogate character ranges that I didn't realize existed when I added the initial support.
    -   Behavior change: Don't prefer py.typed libraries when the execution environment is typeshed.
    -   Bug Fix: Fixed bug in signature help provider where it was not properly handling a call with a type `Type[T]`.
    -   Bug Fix: Fixed bug in code that handles "super" call when a `cls` variable is passed as the first argument.
    -   Bug Fix: Changed the way the current parameter index is specified in signature help to better conform to LSP standard.
    -   Enhancement: Improved the "X is incompatible with Y" error message in the case where types X and Y have the same short name. In this case, the fully-qualified names will be used to provide clarity.
    -   Bug Fix: Fixed bug that resulted in false positive when generic type was used for iterable within a list comprehension.
    -   Bug Fix: Fixed bug that resulted in incorrect errors when using a TypeVar imported from another file and referenced using a member access expression (e.g. `typing.AnyStr`).
    -   Enhancement: Added support for `defaults` argument in `namedtuple` constructor, which marks the rightmost input parameters to the resulting named tuple as having default values.
    -   Behavior change (from pylance): Filter auto-imports more strictly to reduce the number of completions returned. Matches require at least the first character to match before fuzzy matching is applied.
    -   Enhancement (from pylance): Add support for tables in docstrings.
-   [1.1.140](https://github.com/microsoft/pyright/releases/tag/1.1.140)
    -   Bug Fix: Fixed bug that caused parameters in overloaded functions not to be marked as accessed, as was intended.
    -   Bug Fix: Fixed false negative when the same name was defined in both an outer and inner function and referenced in the inner function prior to being assigned.
    -   Enhancement: Added support for identifiers that contain Unicode characters that require two UTF16 character codes (surrogates). This allows identifiers to use characters in the Unicode blocks for Egyptian Hieroglyphs, Linear B Ideograms, Cuneiform, Phoenician, etc.
    -   Enhancement: Added new diagnostic rule "reportIncompleteStub", which reports a diagnostic for a module-level `__getattr__` function in a type stub, indicating that it's incomplete. This check was previously part of the "reportUnknownMemberType" diagnostic rule.
    -   Behavior Change: Disabled support for keyword arguments in subscript expressions because PEP 637 was rejected.
    -   Bug Fix: Fixed bug in the type specialization for ParamSpec when the return type contains no generics.
    -   Bug Fix: Changed TypeGuard behavior to evaluate the return type of a call expression that invokes a type guard function to be 'bool' rather than 'TypeGuard[T]'.
    -   Behavior Change: Changed TypeGuard behavior to allow a type guard function to be passed as a callback that expects the return type to be bool.
    -   Bug Fix: Removed explicit check for Python 3.10 when using ParamSpec. It's possible to use it with older versions of Python if importing from `typing_extensions`.
    -   Bug Fix: Fixed bug that caused a false positive error when applying a subscript operation on a TypeVar.
    -   Bug Fix: Fixed bug that resulted in a false positive error when the second argument to `isinstance` or `issubclass` was a union that included both a single type and a tuple of types.
        ([pylance-release#1294](https://github.com/microsoft/pylance-release/issues/1294))
    -   Enhancement: Updated typeshed stubs to the latest version.
    -   Enhancement: Added support in typeshed VERSIONS file for submodules.
-   [1.1.139](https://github.com/microsoft/pyright/releases/tag/1.1.139)
    -   Enhancement: Updated typeshed to the latest.
    -   Enhancement: Added support for typeshed VERSION file, which indicates which stdlib modules are available in each version of Python.
    -   Bug Fix: Fixed bug that resulted in symbols being inappropriately marked "unaccessed" when they were accessed within a keyword argument used within a class declaration.
        ([pylance-release#1272](https://github.com/microsoft/pylance-release/issues/1272))
    -   Bug Fix: Fixed false positive error when a dataclass declares an instance variable but a subclass redeclares a class variable of the same name.
    -   Bug Fix: Fixed type narrowing bug with 'isinstance' checks that involve protocol classes. The bug resulted in false positive errors with the reportUnnecessaryIsInstance check.
    -   Enhancement: Added support for callback protocols that use overloaded `__call__` methods.
        ([pylance-release#1276](https://github.com/microsoft/pylance-release/issues/1276))
    -   Enhancement (from pylance): Improved performance of tokenizer's handling of string literals.
    -   Bug Fix (from pylance): Ignore updates to ".git" file so they don't trigger reanalysis.
    -   Bug Fix: Fixed false positive error in check for overload implementation consistency when one of the overloaded methods in a generic class provides an explicit type annotation for "self" or "cls" but the implementation does not.
    -   Enhancement: Improved "is None" and "is not None" type narrowing logic to handle constrained TypeVar that includes None as one of the constraints.
    -   Bug Fix: Fixed false positive error when a `__getattr__` method is present. The previous logic was assuming that `__getattr__` could provide a magic method value (e.g. for `__add__`).
        ([pylance-release#1252](https://github.com/microsoft/pylance-release/issues/1252))
    -   Bug Fix: Prefer py.typed libraries over typeshed for consistency with PEP 561.
    -   Bug Fix: Improved validation for function calls where the function signature includes keyword arguments without default values that are not directly matched by keyword arguments but are matched by a **kwargs argument. In this situation, the type of the **kwargs values should be verified to be compatible with the type of the keyword parameters.
    -   Bug Fix: Fixed bug in lambda type evaluation for lambdas that use an \*args parameter. The parameter type was not being transformed into a tuple, as it should have been.
        ([pylance-release#1284](https://github.com/microsoft/pylance-release/issues/1284))
    -   Enhancement: Improved diagnostic message for constant redefinition to make it clear that the symbol is assumed to be constant because its name is uppercase.
-   [1.1.138](https://github.com/microsoft/pyright/releases/tag/1.1.138)
    -   Bug Fix: Fixed bug in handling special-case types in typing.pyi or typing_extensions.pyi. The RHS of the assignment was not being evaluated, so symbols referenced in the RHS were not be marked as accessed.
    -   Bug Fix: Changed special-case handling of "overload" definition in typying.pyi stub. New versions of this stub have changed the definition from an object to a function.
    -   Bug Fix: Fixed recent regression in handling of f-strings that are also raw.

## 2021.5.2 (13 May 2021)

Pylance has reached stable and is officially out of public preview! (https://aka.ms/announcing-pylance-stable)

## 2021.5.1 (6 May 2021)

This is a hotfix release, fixing raw format strings ([pylance-release#1241](https://github.com/microsoft/pylance-release/issues/1241)) and handling language server settings changes available in the next Python extension release.

## 2021.5.0 (5 May 2021)

Notable changes:

-   A number of CPU and memory improvements have been made, improving indexing, docstring conversion, and peak memory usage.
-   Pylance insiders will now be automatically enabled when Python insiders is enabled. This can be overridden by explicitly setting `pylance.insidersChannel`.
-   Docstring support for compiled standard library modules (such as `math`, `sys`, and `time`) now handles module docstrings.
-   The bundled stubs for pandas and PIL have been updated.
    ([pylance-release#556](https://github.com/microsoft/pylance-release/issues/556), [pylance-release#660](https://github.com/microsoft/pylance-release/issues/660), [pylance-release#769](https://github.com/microsoft/pylance-release/issues/769), [pylance-release#779](https://github.com/microsoft/pylance-release/issues/779))
-   The "report issue" command can now be run in any file, including Jupyter notebooks.
    ([pylance-release#1207](https://github.com/microsoft/pylance-release/issues/1207))
-   A number of crashes have been fixed.
    ([pylance-release#1211](https://github.com/microsoft/pylance-release/issues/1211), [pylance-release#1218](https://github.com/microsoft/pylance-release/issues/1218), [pylance-release#1219](https://github.com/microsoft/pylance-release/issues/1219))
-   Python 3.10's new `match` and `case` keywords will now be highligted as keywords when semantic tokenization is enabled.
    ([pylance-release#1215](https://github.com/microsoft/pylance-release/issues/1215))
-   Assignment expressions in the class scope are no longer incorrectly disallowed.
    ([pylance-release#1213](https://github.com/microsoft/pylance-release/issues/1213))
-   Completions are no longer incorrectly provided in the string portion of f-strings.
    ([pylance-release#1226](https://github.com/microsoft/pylance-release/issues/1226))
-   Pylance's copy of typeshed has been updated.
    ([pylance-release#1216](https://github.com/microsoft/pylance-release/issues/1216))

In addition, Pylance's copy of Pyright has been updated from 1.1.136 to 1.1.137, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Bug Fix: Fixed bug in handling special-case types in typing.pyi or typing_extensions.pyi. The RHS of the assignment was not being evaluated, so symbols referenced in the RHS were not be marked as accessed.
-   [1.1.137](https://github.com/microsoft/pyright/releases/tag/1.1.137)
    -   Bug Fix: Fixed bug in type inference of dictionary, list and set expressions when they contain classes or class instances that are apparently the same type but internally appear different because they are "pseudo-generic". Pseudo-generic classes are those that have no type annotations in the `__init__` method and are treated internally as generics to improve type inference.
    -   Bug Fix: Fixed bug that caused false positive error when assigning `Type[Any]` to `type`.
    -   Bug Fix: Fixed false positive error when assignment expression (i.e. walrus operator) is used within a class scope.
    -   Enhancement: Updated typeshed stubs to the latest.
    -   Behavior Change: When in "outputjson" mode, the CLI now output log information to stderr.
    -   Enhancement: Add match and case keywords to completion provider.
    -   Bug Fix: Fixed regression that caused runtime assertion (and crash) in some rare circumstances.
    -   Performance: Eliminated O(n\*m) behavior when testing type compatibility of a union with n subtypes and a union of m subtypes when those subtypes contain mostly literals.
    -   Performance: Moved checks for string literal errors (unsupported escape characters, etc.) from binder to checker for performance reasons.
    -   Performance: Improved performance of string token value unescape logic by handling the common cases (no format string and no escape characters) using a fast path.
    -   Bug Fix (from Pylance): Fixed bug in file watching logic for config files.
    -   Performance (from Pylance): Reduced work done during parsing and binding related to doc string handling.
    -   Enhancement (from Pylance): Improved document symbol provider symbol type information.
    -   Behavior Change: Removed PEP 563 (deferred type annotation) behavior as default for Python 3.10, since the PEP was deferred.
    -   Bug Fix: Fixed bug in completion provider that caused completions to be provided when pressing "." within the string literal portion of an f-string.
    -   Performance (from Pylance): Provided special-case code paths in parser and binder to speed up symbol indexing operations.

## 2021.4.3 (29 April 2021)

Notable changes:

-   The bundled native module stubs for sklearn, numpy, and pandas have been updated.
-   Markdown-style links in docstrings will now be passed through as-is to tooltips.
-   Docstrings for all compiled standard library modules (such as `math`, `sys`, and `time`) are now supported.
    ([pylance-release#465](https://github.com/microsoft/pylance-release/issues/465))
-   Docstrings in signature help tooltips will now show the same docstrings as completion and hover tooltips.
-   Overload matching has been changed to more closely match matching in other type checkers.
    ([pylance-release#549](https://github.com/microsoft/pylance-release/issues/549), [pylance-release#1111](https://github.com/microsoft/pylance-release/issues/1111))
-   A number of bugs that could cause potentially nondeterministic behavior when semantic highlighting is enabled have been fixed.
    ([pylance-release#1180](https://github.com/microsoft/pylance-release/issues/1180), [pylance-release#1181](https://github.com/microsoft/pylance-release/issues/1181))

In addition, Pylance's copy of Pyright has been updated from 1.1.133 to 1.1.136, including the following changes:

-   [1.1.136](https://github.com/microsoft/pyright/releases/tag/1.1.136)
    -   Bug Fix: Fixed bug in diagnostic check for contravariant type variables used in a return type annotation that resulted in a false negative.
        ([pylance-release#1190](https://github.com/microsoft/pylance-release/issues/1190))
    -   Enhancement: Added minimal support for `*` and `**` parameter annotations within function annotation comments.
        ([pylance-release#1191](https://github.com/microsoft/pylance-release/issues/1191))
    -   Behavior Change: Modified algorithm for invariant union type assignments to avoid n^2 behavior.
    -   Bug Fix: Fixed a false positive error that occurs when a class uses itself as a type argument for one of its base classes and that base class uses a bound type variable.
    -   Enhancement: Added logic to skip the normal `__new__` constructor evaluation if the class is created by a metaclass with a custom `__call__` method.
    -   Bug Fix: Fixed bug in TypedDict type narrowing (for containment of non-required fields) that resulted in a false positive error when a narrowed type was later used.
    -   Bug Fix: Fixed bug in type variable constraint solver that resulted in a confusing false positive error in circumstances involving contravariant type variables (e.g. when dealing with callback protocols) and a combination of `Type[T]` and `T` within the callback signature.
    -   Enhancement (from pylance): Improved formatting of doc strings in tool tips.
-   [1.1.135](https://github.com/microsoft/pyright/releases/tag/1.1.135)
    -   Behavior Change: Changed behavior of function overload evaluation to more closely match the behavior of other type checkers. Notably, if one or more argument have union types, they are expanded, and each combination of argument union subtypes can use different overloads.
    -   Bug Fix: Fixed bug that caused false positive error when assigning a function with no position-only marker to a function with a position-only marker.
        ([pylance-release#1187](https://github.com/microsoft/pylance-release/issues/1187))
    -   Enhancement: Added support for call arguments whose types are constrained type variables and must be constrained to a particular subtype during call evaluation because the LHS of the call imposes such constraints.
        ([pylance-release#1182](https://github.com/microsoft/pylance-release/issues/1182))
    -   Enhancement: Added support for special cases of class pattern matching as described in PEP 634.
    -   Enhancement: Added support for auto generation of `__match_args__` class variable for dataclass and named tuples.
    -   Enhancement: Added support for type narrowing of the subject expression within a "match" statement based on the matched pattern.
    -   Bug Fix: Fixed bug in type analyzer that resulted in a false positive error when a return type annotation included a generic class but omitted the type arguments.
-   [1.1.134](https://github.com/microsoft/pyright/releases/tag/1.1.134)
    -   Enhancement: Implemented first cut at generalized support for dataclass transforms.
    -   Behavior Change: Allow NoReturn return type annotation for `__init__` method.
    -   Bug Fix: Fixed bug in completion provider that resulted in no valid completion suggestions at the end of a "from x import a, " statement.
        ([pylance-release#673](https://github.com/microsoft/pylance-release/issues/673))
    -   Bug Fix: Fixed bug in type checker that led to a false positive when assigning a function to a callable type and the source contained unannotated parameters.
    -   Bug Fix: Fixed numerous bugs that result in occasional type evaluation errors, some of which appear to be somewhat non-deterministic.
        ([pylance-release#1180](https://github.com/microsoft/pylance-release/issues/1180), [pylance-release#1181](https://github.com/microsoft/pylance-release/issues/1181))
    -   Bug Fix: Fixed bug in type evaluator that caused incorrect type evaluation for annotated parameter types in some cases.
    -   Bug Fix: Fixed a bug in the type checker that resulted in a false positive error when using "|" (union) operator in parameter type annotations in some cases.
    -   Bug Fix: Changed binder logic for "from .a import x" statements in `__init__.py`. Implicit import of ".a" is performed only in cases where there is a single dot. For example, "from .a.b import x" does not implicitly import ".a.b".
        ([pylance-release#234](https://github.com/microsoft/pylance-release/issues/234))

## 2021.4.2 (21 April 2021)

Notable changes:

-   A number of CPU and memory improvements have been made, which should lead to faster initial startup, faster analysis, and lower peak memory usage.
-   A partial stub for scikit-learn has been included, which should fix many classes (such as `MinMaxScalar`).
    ([pylance-release#1139](https://github.com/microsoft/pylance-release/issues/1139))
-   A number of crashes have been fixed.
    ([pylance-release#1072](https://github.com/microsoft/pylance-release/issues/1072))
-   `self`/`cls`, parameters in abstract methods, parameters in `Protocol` definitions, and parameters in function overloads will no longer be marked as "not accessed" and grayed out.
    ([pylance-release#194](https://github.com/microsoft/pylance-release/issues/194))
-   The bundled matplotlib stubs have been updated.
-   Pylance's copy of typeshed has been updated. Stubs that are marked as Python 2 only are no longer included.
-   Interpreter paths are now correctly queried when the selected interpreter is PyPy.
-   Indexing has been re-enabled in the insiders build.

In addition, Pylance's copy of Pyright has been updated from 1.1.130 to 1.1.133, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Enhancement: Implemented first cut at generalized support for dataclass transforms.
-   [1.1.133](https://github.com/microsoft/pyright/releases/tag/1.1.133)
    -   Bug Fix: Fixed bug that resulted in a false positive error within type checker when a constrained TypeVar was used in a lambda callback.
    -   Bug Fix: Fixed bug in type variable constraint solver that resulted in false positive error in certain cases involving bidirectional type inference with unknown (or missing) type arguments.
        ([pylance-release#1168](https://github.com/microsoft/pylance-release/issues/1168))
    -   Enhancement: Reduced memory consumption of tokenizer for string literal tokens.
    -   Enhancement: Improved performance of type analyzer in cases where certain type checking diagnostic rules are disabled.
    -   Enhancement: Improved startup time of pyright by eliminating redundant calls to Python interpreter to retrieve import resolution paths.
    -   Behavior Change: Automatically mark parameters as accessed (so they don't appear as "grayed out") in the following circumstances: 1) it is a self parameter in an instance method, 2) it is a cls parameter in a class method, 3) it is a parameter in a method marked abstract, 4) it is a parameter in a method that is part of a protocol class, 5) it is a parameter in an overload signature.
        ([pylance-release#194](https://github.com/microsoft/pylance-release/issues/194))
    -   Bug Fix: Fixed incompatibility with pypy when retrieving import resolution paths from the configured Python interpreter.
    -   Enhancement: Added diagnostic for `__init__` method that does not have a return type of `None`.
    -   Enhancement: Configuration settings can now be stored in a pyproject.toml file. If both pyproject.toml and pyrightconfig.json are both present, the latter takes precedent.
-   [1.1.132](https://github.com/microsoft/pyright/releases/tag/1.1.132)
    -   Bug Fix: Fixed regression that caused incorrect reporting of "parameter name mismatch" errors for overrides of dundered methods.
-   [1.1.131](https://github.com/microsoft/pyright/releases/tag/1.1.131)
    -   Bug Fix: Changed logic that detects generator functions to accommodate yield statements that are provably unreachable in the code flow.
    -   Behavior Change: Changed dataclass logic to not enforce ordering of fields with defaults vs those without if `init=False` is specified.
    -   Enhancement: Extended method override check to include dundered methods (other than constructors).
    -   Bug Fix (from pylance): Removed duplicate "yield" suggestion in completion list.
    -   Enhancement (from pylance): Improved logic that maps type stubs to corresponding source files.
    -   Enhancement: Added support for implicit `__annotations__` symbol at the module level.
        ([pylance-release#1161](https://github.com/microsoft/pylance-release/issues/1161))
    -   Enhancement: Updated to the latest typeshed stubs. Removed third-party stubs for that were marked as Python 2 only (enum34, fb303, futures, ipaddress, kazoo, openssl-python, pathlib2, pymssql, Routes, scribe, tornado).
    -   Enhancement: Added support for `type(None)` within isinstance type narrowing.
    -   Bug Fix: When providing a completion suggestion for an async method override, an "await" operator is now added in the generated return expression.
    -   Bug Fix: Fixed false positive error in argument/parameter matching logic for function calls that occurs when a keyword argument targets a parameter that can be either positional or keyword and a spread operator is used in an earlier argument.
    -   Bug Fix: Fixed bug that resulted in false positive error when a constrained TypeVar type was passed through the "isinstance" type narrowing logic and then used as an operand in a binary operation.
        ([pylance-release#1165](https://github.com/microsoft/pylance-release/issues/1165))
    -   Bug Fix: Fixed several bugs that caused type checker crash in certain cases.

## 2021.4.1 (14 April 2021)

Notable changes:

-   Source mapping has been greatly improved. Notably, in more recent versions of numpy (1.20+), docstrings and navigation should work for many more symbols.
    ([pylance-release#855](https://github.com/microsoft/pylance-release/issues/855))
-   The `yield` keyword will no longer be duplicated in completions.
    ([pylance-release#1137](https://github.com/microsoft/pylance-release/issues/1137))

In addition, Pylance's copy of Pyright has been updated from 1.1.129 to 1.1.130, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Bug Fix: Changed logic that detects generator functions to accommodate yield statements that are provably unreachable in the code flow.
    -   Behavior Change: Changed dataclass logic to not enforce ordering of fields with defaults vs those without if `init=False` is specified.
    -   Enhancement: Extended method override check to include dundered methods (other than constructors).
-   [1.1.130](https://github.com/microsoft/pyright/releases/tag/1.1.130)
    -   Bug Fix: Fixed bug in type narrowing logic when the narrowed expression contained an assignment expression (walrus operator). It was not properly narrowing the target of the assignment expression.
    -   Bug Fix: Fixed bug in "isinstance" type narrowing support when the first argument is a type (e.g. a class or `Type[T]`) and the second argument is `type` (or a tuple that contains `type`).
    -   Bug Fix: Fixed bug in "isinstance" type narrowing logic where it didn't properly handle protocol classes that support runtime checking.
    -   Enhancement (from Pylance): Improved docstring formatting in hover text.
    -   Behavior Change: Suppressed "access to non-required key" diagnostic if the access is performed within a try block.
        ([pylance-release#1145](https://github.com/microsoft/pylance-release/issues/1145))
    -   Bug Fix: Fixed bug in 'callable' type narrowing logic. It wasn't properly handling type variables.
    -   Enhancement: Implemented new diagnostic rule "reportUnnecessaryComparison". It checks for "==" and "!=" comparisons where the LHS and RHS types have no overlap and the LHS has no `__eq__` overload. This new diagnostic rule is off by default in normal type checking mode but is on in strict mode.
    -   Bug Fix: Fixed false positive error that occurred when file started with "from typing import Collection". This was due to mishandling of a cyclical dependency in the typeshed classes.
    -   Enhancement: Improved bidirectional type inference for expressions that involve the pattern `[<list elements>] * <expression>`.
    -   Bug Fix: Fixed false positive error relating to the use of parentheses in "with" statement when using Python 3.9.
        ([pylance-release#999](https://github.com/microsoft/pylance-release/issues/999))
    -   Bug Fix: Fixed bug in type evaluation of async functions that are not generators but have a declared return type of AsyncGenerator. The actual return type needs to be wrapped in a Coroutine in this case.
        ([pylance-release#1140](https://github.com/microsoft/pylance-release/issues/1140))
    -   Bug Fix: Suppressed diagnostic check for `Subscript for class "X" will generate runtime exception` when it's used in a PEP 526-style variable type annotation. Apparently the exception occurs only when used in other contexts like parameter and return type annotations.

## 2021.4.0 (7 April 2021)

Notable changes:

-   `lxml.etree` (and other compiled modules) should no longer be mistakenly marked as unresolved in some cases.
    ([pylance-release#392](https://github.com/microsoft/pylance-release/issues/392))
-   A bug in a performance optimization for `__all__` involving `py.typed` libraries has been fixed. This issue manifested as auto-imports using an unwanted path (e.g. `fastapi.param_functions.Query` instead of `fastapi.Query`).
    ([pylance-release#774](https://github.com/microsoft/pylance-release/issues/774))
-   Signature help in broken code will now more correctly signatures and parameters.
    ([pylance-release#1128](https://github.com/microsoft/pylance-release/issues/1128))
-   A regression in namespace package handling has been fixed.
    ([pylance-release#1132](https://github.com/microsoft/pylance-release/issues/1132))
-   The default setting for indexing in the insiders build has been temporarily changed to `false` as we continue to analyze and improve its performance. It can still be manually enabled with `"python.analysis.indexing": true`.
-   The bundled matplotlib stubs have been updated.
-   Pylance's copy of typeshed has been updated.

In addition, Pylance's copy of Pyright has been updated from 1.1.127 to 1.1.129, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Bug Fix: Fixed bug in type narrowing logic when the narrowed expression contained an assignment expression (walrus operator). It was not properly narrowing the target of the assignment expression.
    -   Bug Fix: Fixed bug in "isinstance" type narrowing support when the first argument is a type (e.g. a class or `Type[T]`) and the second argument is `type` (or a tuple that contains `type`).
    -   Bug Fix: Fixed bug in "isinstance" type narrowing logic where it didn't properly handle protocol classes that support runtime checking.
-   [1.1.129](https://github.com/microsoft/pyright/releases/tag/1.1.129)
    -   Enhancement: Added configuration option "strictSetInference" which is analogous to "strictListInference" and "strictDictionaryInference" but specifically for set expressions.
    -   Enhancement: Tweaked heuristic in constraint solver to prefer types that have no "unknown" element to those that do.
    -   Enhancement: Improved the handling of TypeVar matching when the source and dest types are both unions, the types are being compared with invariant constraints, and the dest contains a TypeVar.
    -   Enhancement: Fixed misleading error message for "unsupported `__all__` operations".
    -   Enhancement: Improved error message for dataclass fields.
    -   Bug Fix: Fixed bug that caused inconsistent type evaluation for type annotations based on order of evaluation. It was triggered in some cases by the semantic highlighting feature.
        ([pylance-release#1121](https://github.com/microsoft/pylance-release/issues/1121))
    -   Bug Fix: Fixed bug in the function type compatibility logic. If the source has a `*args` or `**kwargs` parameter but the dest does not, the function should still be assignable.
    -   Behavior Change: Changed the logic that searches for a config file. It currently searches from the current working directory all the way up the folder hierarchy. This makes sense only for a command-line tool, not for a language server. The latter already knows the project root, and we should look only in that directory for a config file.
    -   Bug Fix: Fixed bug in signature help provider where its heuristics were causing it to return a bad response when the insertion point was immediately after a comma and a call expression preceded the comma.
        ([pylance-release#1128](https://github.com/microsoft/pylance-release/issues/1128))
    -   Bug Fix: Added support for an import edge case where a module's `__init__.py` file is apparently importing from itself but intends instead to import from one of its submodules.
    -   Bug Fix: Fixed bug in namespace import resolution. When there are multiple import search matches, the import resolver needs to take into account the individual symbols specified in the import statement.
        ([pylance-release#1132](https://github.com/microsoft/pylance-release/issues/1132))
    -   Bug Fix: Fixed a bug whereby call expressions within a type annotation were flagged as errors but not evaluated, which meant that symbols referenced within them were not marked as accessed.
    -   Enhancement: Updated typeshed stubs to the latest.
-   [1.1.128](https://github.com/microsoft/pyright/releases/tag/1.1.128)
    -   Bug Fix: Fixed bug in argument-matching code that produced false positive errors when a keyword argument corresponded to a positional-only argument name but should have been matched to a \*\*kwargs parameter instead.
        ([pylance-release#1109](https://github.com/microsoft/pylance-release/issues/1109))
    -   Bug Fix: Fixed bug in bidirectional type inference logic for list and dict expressions when expected type included a type varaible.
    -   Bug Fix: Disabled the "self" annotation checks for overloaded methods because the self annotation can be used as a legitimate filter for overloads.
    -   Enhancement: Improved bidirectional type inference for set expressions so it better handles unions in expected type.
    -   Bug Fix: Improved TypeVar constraint solver so it provides a better solution when a TypeVar is constrained first by a contravariant wide bound in a first argument and then a subsequent argument relies on bidirectional type inference with a covariant or invariant use of the same TypeVar.
    -   Bug Fix: Fixed bug that caused a crash in the type checker when a protocol class inherited from a generic non-protocol class.
    -   Enhancement: Added check for a class that inherits from Generic to ensure that all type variables are included in the Generic subscript list.
    -   Bug Fix: Fixed regression in handling expressions of the form `[x] * y`. Some previously-added special-case code to handle the `[None] * n` case was too general.
    -   Enhancement: Changed printed types to fully expand type aliases in error messages where that additional detail is needed — namely, for "partially unknown" messages. This makes for verbose types, but without the expansion, it can be very difficult to determine which part of the type is unknown.
    -   Bug Fix: Fixed false positive error in type compatibility check where the destination type is `Type[Any]` and the source type is `Type[x]` where x is anything (including `Any`).
    -   Enhancement: Added exemption to the overlapping overload check for the `__get__` method. Other type checkers (namely mypy) exempt this method also.

## 2021.3.4 (31 March 2021)

Notable changes:

-   Broken symlinks in the workspace should no longer cause crashes.
    ([pylance-release#1102](https://github.com/microsoft/pylance-release/issues/1102))
-   Completion performance when IntelliCode is enabled has been improved.
-   The bundled matplotlib stubs have been updated.
-   Method override completions while editing a stub will no longer include `super()` calls, and instead add the correct `...` body.
-   Auto-import completions and quick fixes will now more correctly handle import blocks that have been split onto multiple lines.
    ([pylance-release#1097](https://github.com/microsoft/pylance-release/issues/1097))

In addition, Pylance's copy of Pyright has been updated from 1.1.125 to 1.1.127, including the following changes:

-   [1.1.127](https://github.com/microsoft/pyright/releases/tag/1.1.127)
    -   Bug Fix: Fixed bug in type evaluator that resulted in suppressed errors and evaluations when the evaluation of a lambda expression resulted in some form of recursion (e.g. it references a symbol that depends on the return result of the lambda).
        ([pylance-release#1096](https://github.com/microsoft/pylance-release/issues/1096))
    -   Enhancement: Added "reportTypedDictNotRequiredAccess" diagnostic rule and split out diagnostics that pertain specifically to unguarded accesses to non-required TypedDict keys.
    -   Bug Fix: Changed type of `__path__` variable in module from `List[str]` to `Iterable[str]`.
        ([pylance-release#1098](https://github.com/microsoft/pylance-release/issues/1098))
    -   Bug Fix: Fixed bug that resulted in a runtime crash within the type checker when a protocol class inherits from another protocol class that is not generic (like "Sized").
        ([pylance-release#1101](https://github.com/microsoft/pylance-release/issues/1101))
    -   Enhancement: Added better heuristics to auto-complete insertion logic so it honors single-symbol-per-line and multi-symbol-per-line formats of "from x import a" statements.
        ([pylance-release#1097](https://github.com/microsoft/pylance-release/issues/1097))
    -   Enhancement: Implemented a new check to validate that annotated types for "self" and "cls" parameters are supertypes of their containing classes.
    -   Bug Fix (from pylance): Fixed bug that resulted in crashes when a broken symlink was encountered.
        ([pylance-release#1102](https://github.com/microsoft/pylance-release/issues/1102))
    -   Bug Fix: Fixed recent regression that resulted in false positives when checking the type of a "self" parameter within a metaclass when the type annotation was of the form `Type[T]`.
    -   Enhancement: Added minimal support for "@no_type_check" decorator. It does not suppress errors, but it doesn't generate an error itself.
    -   Enhancement: Added support for PEP 612 ParamSpecs to be used as type parameters for generic classes and generic type aliases. Previously, they were allowed only in the specialization of `Callable`.
    -   Enhancement: Added out-of-bounds access check for index operations where the indexed type is a tuple object with known length and the index value is a negative integer literal value.
    -   Bug Fix: Fixed bugs in the handling of PEP 487 `__init_subclass__`. The logic was using the `__init_subclass__` defined in the class itself rather than its base classes.
    -   Enhancement: Added special-case handling for generic functions that return a `Callable` with generic parameters. The change allows for callers to pass type variables to the function and then have the resulting `Callable` provide a TypeVar scope for those variables.
    -   Bug Fix (from pylance): Fixed bugs relating to partial type stub packages.
-   [1.1.126](https://github.com/microsoft/pyright/releases/tag/1.1.126)
    -   Bug Fix: Fixed bug that affected the use of the `tuple` constructor. It was not properly updating the variadic type arguments. This resulted in false negatives for the resulting type.
        ([pylance-release#1085](https://github.com/microsoft/pylance-release/issues/1085))
    -   Bug Fix: Fixed bug that resulted in false negatives because diagnostics generated while analyzing a constructor call were suppressed.
        ([pylance-release#1087](https://github.com/microsoft/pylance-release/issues/1087), [pylance-release#1088](https://github.com/microsoft/pylance-release/issues/1088), [pylance-release#1104](https://github.com/microsoft/pylance-release/issues/1104))
    -   Enhancement: Improved stub generator to print "x = ..." rather than include the RHS expression if `x` is not a type alias.
    -   Enhancement: Added special-case handling for assignments of the form `x: List[A] = [a] * y` (the multiply operator on a list). This specific idiom is commonly used to initialize a list with None values.
    -   Performance: Added perf improvements that help when dealing with unions that contain many tuples. Improved TypeVar constraint solver to better handle the case where a type is widened to include hundreds of subtypes, thus grinding performance to a halt. This occurs in one of the modules in pytorch.
    -   Enhancement: Rewrote package type verifier based on feedback from users. Its error messages are now much clearer, it distinguishes between "exported symbols" and "other referenced symbols", it properly handles properties, and it omits warnings about missing docstrings by default (can be overridden with "--verbose" setting).
    -   Bug Fix: Fixed bug that resulted in incorrect type evaluation for a constructor call when the class's `__new__` method returns an instance of a different class.
        ([pylance-release#1092](https://github.com/microsoft/pylance-release/issues/1092))

## 2021.3.3 (24 March 2021)

Notable changes:

-   Recursive symlinks in the workspace should no longer cause a hang.
    ([pylance-release#1070](https://github.com/microsoft/pylance-release/issues/1070), [pylance-release#1078](https://github.com/microsoft/pylance-release/issues/1078))
-   An error about a missing "typings" folder will no longer appear at the default log level.
    ([pylance-release#1075](https://github.com/microsoft/pylance-release/issues/1075))
-   pygame stubs are no longer bundled. pygame 2.0 (released October 2020) and above include high-quality types.
    ([pylance-release#758](https://github.com/microsoft/pylance-release/issues/758))

In addition, Pylance's copy of Pyright has been updated from 1.1.122 to 1.1.125, including the following changes:

-   [1.1.125](https://github.com/microsoft/pyright/releases/tag/1.1.125)
    -   Bug Fix: Disabled the "always False comparison" check for expressions like "sys.platform == 'win32'" because they can vary depending on environment.
    -   Enhancement: Added error check for a class that attempts to derive from NamedTuple and other base classes. This is not supported and will generate runtime exceptions.
    -   Enhancement: Improved type checking for generators. Fixed several false negatives and false positives relating to "yield from" expressions.
    -   Enhancement: Changed special-case logic for `self` annotations used with `__init__` methods to accommodate new usages in typeshed stubs.
    -   Enhancement: Updated typeshed stubs to latest.
    -   Bug Fix: Fixed bug in TypeVar constraint solver that resulted in a false positive when using the built-in "filter" method with the "os.path.exists" callback.
    -   Bug Fix: Fixed bug where "comparison chaining" was not being appropriately applied to expressions that contained "is", "is not", "in" and "not in" operators in a chain (e.g. "1" in "1" == "1").
    -   Enhancement: Added smarter handling of empty lists (`[]`) and dicts (`{}`). Previously, these were inferred to have types `list[Unknown]` and `dict[Unknown, Unknown]`, respectively. They are now provided with a known type if the variable is assigned a known list or dict type along another code path.
    -   Bug Fix (from pylance): Made hover text, signature help, and completion suggestions show function docstring using same code.
    -   Bug Fix (from pylance): Fixed issue with partial stub files in cases where a stub file is found but no corresponding source (.py) file is found.
-   [1.1.124](https://github.com/microsoft/pyright/releases/tag/1.1.124)
    -   Bug Fix: Fixed bug where a keyword parameter with a generic type (a TypeVar) and a default value of "..." caused the TypeVar to be assigned a value of "Any".
    -   Bug Fix: Fixed recent regression that caused certain diagnostics to be suppressed when calling a constructor with an expected type.
    -   Enhancement: Added missing check indicated in PEP 589 for TypedDict fields that override a parent class field by the same name with a different type.
    -   Bug Fix: Added support for TypeVar where the bound or constrained types are literals.
    -   Enhancement: Updated typeshed stubs.
    -   Bug Fix: Fixed bug that resulted in false negatives when a generic class was used within a subscript (e.g. within the type argument of another type) and no type arguments were specified for the generic class. This also resulted in such types not properly getting default values. For example, in the expression `Union[int, Callable]`, the `Callable` was not being interpreted as `Callable[..., Unknown]`.
    -   Enhancement: Improved error message for partially-unknown lambda type.
    -   Bug Fix: Fixed a bug in the logic for inferring the type of list expressions when the expected type is "object".
    -   Bug Fix: Improved handling of bidirectional inference for call expressions when the expected type contains a union of literals and the function returns a generic type.
    -   Enhancement: Added new check for a common source of bugs where an equals operator within an if statement compares two values whose literal types do not overlap and will therefore never evaluate to True.
-   [1.1.123](https://github.com/microsoft/pyright/releases/tag/1.1.123)
    -   Bug Fix: Fixed bug in handling of "Final" type annotation with no specified type argument (e.g. "x: Final = 4").
    -   Enhancement: Added support for inferring type of subscripted tuple when subscript is a negative integer literal.
    -   Bug Fix: Fixed recent regression where `super(A, self).x` did not return an unknown type if class `A` had a class in its MRO that had an unknown type.
    -   Bug Fix: Fixed false positive error due to constraint solver's handling of a TypeVar used within a Callable parameter that is matched to a function parameter annotated with another TypeVar.
    -   Enhancement: Improved handling of literals within constraint solver when used with bidirectional type inference.
    -   Bug Fix: Fixed bug that caused false positive error when a generic call expression was used for an argument to an overloaded function and TypeVar matching errors were reported.
        ([pylance-release#1063](https://github.com/microsoft/pylance-release/issues/1063))
    -   Enhancement: Deferred resolution of metaclass during class type resolution to improve compatibility with code generated by mypy-protobuf, which contains cyclical dependencies.
    -   Bug Fix: Fixed bug in declaration provider that caused declaration of class variables to not be resolved correctly when accessed via a `cls` parameter in a class method.
        ([pylance-release#1064](https://github.com/microsoft/pylance-release/issues/1064))
    -   Bug Fix: Fixed bug in symbol resolution when a local class mirrors the name of a class in typing (e.g. `List`) but is not imported from typing and is used in a context where it is forward declared without quotes.
    -   Bug Fix (from pylance): Avoid recursing infinitely when searching for source files when there is a cyclical symlink present.
    -   Bug Fix: Fixed type inference for "yield" expressions. The previous code was using the same logic for "yield" and "yield from".
    -   Enhancement: Added check to determine if type variables in generic protocols use the appropriate variance.
    -   Performance Improvement: Limited "implied else type narrowing" to expressions that have declared types. It's too expensive to infer types.

## 2021.3.2 (17 March 2021)

Notable changes:

-   Completions for class property overrides are now supported.
    ([pylance-release#1054](https://github.com/microsoft/pylance-release/issues/1054))
-   Editable installs are now supported.
    ([pylance-release#78](https://github.com/microsoft/pylance-release/issues/78))
-   Module members appearing in `__all__` are now always suggested in auto-imports, regardless of their name.
    ([pylance-release#703](https://github.com/microsoft/pylance-release/issues/703))
-   Completions offered within stub files will now correctly show symbols available in the current file, rather than only the stub's "externally visible" symbols.
    ([pylance-release#685](https://github.com/microsoft/pylance-release/issues/685))
-   A bug in symlink support (introduced in the previous release) has been fixed. Some code paths were not correctly handling symlinked directories.
    ([pylance-release#1031](https://github.com/microsoft/pylance-release/issues/1031))
-   Imports of the form `from . import X` now work correctly in non-`__init__.py` files.
    ([pylance-release#1050](https://github.com/microsoft/pylance-release/issues/1050))
-   Analysis performance has been improved some code patterns with many inferred variables and deeply nested loops.
    ([pylance-release#1049](https://github.com/microsoft/pylance-release/issues/1049))
-   Python 3.10 `match` support has been updated to support unparenthesized pattern subject lists.
    ([pylance-release#1044](https://github.com/microsoft/pylance-release/issues/1044))
-   Type aliases can now be defined within the class scope.
    ([pylance-release#1043](https://github.com/microsoft/pylance-release/issues/1043))
-   The bundled Django, matplotlib, and pandas stubs have been updated to fix several bugs and missing members.
    ([pylance-release#780](https://github.com/microsoft/pylance-release/issues/780), [pylance-release#792](https://github.com/microsoft/pylance-release/issues/792), [pylance-release#850](https://github.com/microsoft/pylance-release/issues/850), [pylance-release#1037](https://github.com/microsoft/pylance-release/issues/1037))
-   When indexing is enabled (`"python.analysis.indexing": true`), auto-import quick fixes will now include results from user code. This was disabled in the previous release; completions from indexed user code are still not offered.
    ([pylance-release#1055](https://github.com/microsoft/pylance-release/issues/1055))
-   Pylance no longer needs to copy files at startup for cross-platform support, which should improve startup time.
-   The hover tooltip now separates the type from the docstring with a horizontal line, matching the completion tooltip.
-   Stubs for `scipy`'s compiled modules are now included, which should improve performance and completion quality.
-   Pylance's copy of typeshed has been updated.

In addition, Pylance's copy of Pyright has been updated from 1.1.120 to 1.1.122, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Bug Fix: Fixed bug in handling of "Final" type annotation with no specified type argument (e.g. "x: Final = 4").
    -   Enhancement: Added support for inferring type of subscripted tuple when subscript is a negative integer literal.
    -   Bug Fix: Fixed recent regression where `super(A, self).x` did not return an unknown type if class `A` had a class in its MRO that had an unknown type.
    -   Bug Fix: Allow lowercase `tuple` type to be subscripted in versions of Python prior to 3.9 if it is within a quoted annotation.
        ([pylance-release#1056](https://github.com/microsoft/pylance-release/issues/1056))
-   [1.1.122](https://github.com/microsoft/pyright/releases/tag/1.1.122)
    -   Bug Fix: Fixed false positive error in constructor method with an input parameter annotated with a class-scoped TypeVar and with a default value.
    -   Enhancement: Improved performance of type analysis for certain code patterns that involve inferred types of variables that are used in deeply nested loops and chains of updates. In one such example, this change reduced the analysis time from ~17000ms to ~200ms.
    -   Bug Fix: Fixed bug in the handling of the `owner` parameter for the `__get__` method in a descriptor class. The type evaluator was using an `Any` type rather than the proper class type in this case.
    -   Bug Fix: Updated TypeVar constraint solver so it tracks a "narrow bound" and "wide bound" for each TypeVar as they are being solved. This fixes several subtle bugs.
    -   Enhancement: Updated typeshed stubs to the latest.
    -   Behavior Change: Added new top-level "extraPaths" config option for pythonconfig.json that specifies the default extraPaths to use when no execution environments apply to a file. Changed settings logic to use the new default extraPaths mechanism for the "python.analysis.extraPaths" setting.
        ([pylance-release#1053](https://github.com/microsoft/pylance-release/issues/1053))
    -   Bug Fix: Fixed bug related to the handling of `from . import X` statement located in a file other than `__init__.py`. When used outside of an `__init__.py` file, this import looks for the `__init__.py` and imports the requested symbol `X` from it rather than looking for a submodule `X`.
        ([pylance-release#1050](https://github.com/microsoft/pylance-release/issues/1050))
    -   Enhancement: Improved completion provider's handling of method overrides so it properly handles properties.
        ([pylance-release#1054](https://github.com/microsoft/pylance-release/issues/1054))
    -   Enhancement (from pylance): Add lowercased items from `__all__` in auto-imports.
    -   Bug Fix: Fixed bug in constraint solver that occurs when a constrained TypeVar is used in conjunction with a protocol that has a contravariant TypeVar.
-   [1.1.121](https://github.com/microsoft/pyright/releases/tag/1.1.121)
    -   Bug Fix: Fixed a bug that generated a false positive error when a function (or other callable) was assigned to a Hashable protocol.
    -   Enhancement (from pylance): Made auto-imports lazy for better completion suggestion performance.
    -   Enhancement (from pylance): Improved readability of hover text for functions and methods with overloaded signatures.
    -   Bug Fix: Fixed false positive error when using an instance or class variable defined within a Protocol class within a method in that same class. The previous logic was based on a misinterpretation of a sentence in PEP 544.
    -   Bug Fix: Fixed false positive error in type checker when dealing with two types that are both unions and both contain constrained type variables.
    -   Bug Fix: Fixed improper handling of symlinks used in editable installs. This affected auto-import functionality.
    -   Bug Fix: Fixed recent regression that caused crash in hover provider.
    -   Bug Fix (from pylance): Fixed issue that caused editable installs to require a restart of the language server before their effects were visible.
    -   Bug Fix: Fixed false positive error during TypeVar constraint solving in the case where the same TypeVar is used in both the form T and `Type[T]` in the same signature.
    -   Enhancement: Improved support for enums. The Python spec indicates that attributes that start and end with an underscore are not treated as enum members, nor are attributes that are assigned a descriptor object.
    -   Enhancement: Added support for inferring the "value" and "name" fields of an enum.
    -   Bug Fix: Added support for unparenthesized pattern subject lists in match statement.
        ([pylance-release#1044](https://github.com/microsoft/pylance-release/issues/1044))
    -   Bug Fix: Fixed false positive error related to a type alias declared within a class.
        ([pylance-release#1043](https://github.com/microsoft/pylance-release/issues/1043))

## 2021.3.1 (10 March 2021)

Notable changes:

-   Import resolution performance has been improved, which significantly reduces overall analysis times (30% in some projects).
-   Hover tooltips for overloaded functions will now place each overload on its own line. This matches the existing completion tooltip. Additionally, signatures which may appear too wide in a tooltip are now separated by extra newlines to visually distinguish them.
    ([pylance-release#612](https://github.com/microsoft/pylance-release/issues/612))
-   `if`/`elif` chains without `else` clauses can now completely narrow variables. For example, it's possible to verify that an enum value has been exhaustively checked against all possible values without a "default" case. This feature is only active in annotated functions.
-   Symlinks are now generally supported.
    ([pylance-release#131](https://github.com/microsoft/pylance-release/issues/131))
-   Angle brackets in docstring inline code blocks are no longer incorrectly escaped.
    ([pylance-release#816](https://github.com/microsoft/pylance-release/issues/816))
-   PEP 464 support (variadic generics) has been updated to match the current state of the PEP. This PEP is not yet accepted, but is targeting Python 3.10.
-   TypedDict support has been updated to allow for narrowing dict members. For example, checking `if "a" in d` will now recognize `d["a"]` as a safe operation.
-   When indexing is enabled (`"python.analysis.indexing": true`), auto-import completions will no longer include indexer results from user code (as this negatively impacted performance); only auto-imports in code referenced from currently open files will be offered. We are looking for feedback about the indexing feature; please file an issue if you have enabled indexing and this affects your workflow.
-   Pylance's copy of typeshed has been updated.

In addition, Pylance's copy of Pyright has been updated from 1.1.117 to 1.1.120, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Bug Fix: Fixed a bug that generated a false positive error when a function (or other callable) was assigned to a Hashable protocol.
        ([pylance-release#1027](https://github.com/microsoft/pylance-release/issues/1027))
-   [1.1.120](https://github.com/microsoft/pyright/releases/tag/1.1.120)
    -   Bug Fix: Fixed type evaluation bug that resulted in the incorrect inference of an exception type within an "except X as Y" clause when the expression X was a bound TypeVar.
    -   Enhancement: Improved detection and error reporting for class definitions that depend on themselves (illegal cyclical dependency). Previously, pyright failed in ways that were difficult to diagnose.
    -   Enhancement: Added support for symbolic links in import resolver both for resolution of ".pth" files and for imports themselves.
    -   Behavior Change: Removed support for "venv" entry in execution environments since this never really worked. Clarified in documentation that import resolution within an execution environment is not transitive.
    -   Bug Fix: Fixed bug in completion provider that caused class variables not be included as suggestions as members for the "cls" parameter in a class method.
        ([pylance-release#1026](https://github.com/microsoft/pylance-release/issues/1026))
    -   Enhancement: Added error check for access to non-required fields in a TypedDict using a subscript with a literal string field name. Added support for "narrowing" of a TypedDict class based on guard expression of the form "S in D" where S is a string literal name of a non-required field. Improved the synthesized "get" method on a TypedDict for non-required fields; it now returns an `Optional[T]` (where T is the defined type for that field) rather than just T.
    -   Enhancement: Updated to the latest typeshed stubs.
    -   Enhancement: Added error check for a "yield" or "yield from" statement used within a list comprehension. This generates a runtime syntax error.
-   [1.1.119](https://github.com/microsoft/pyright/releases/tag/1.1.119)
    -   Bug Fix: Fixed bug in type evaluator that caused some diagnostics to be suppressed unintentionally and in a non-deterministic manner (based on the order in which types were evaluated).
    -   Enhancement: Added a heuristic to disable the "implied else" analysis if the code is within a function that has no input parameter annotations. This mitigates the performance overhead of "implied else narrowing".
    -   Enhancement: When a function decorator is applied and the decorator returns a function that has no docstring, copy the docstring from the decorated function.
    -   Enhancement: Changed inference logic for constructors to allow synthesized type for `cls` to retain its generic form when instantiated, so the expression `cls()` will remain generic.
    -   Bug Fix: Fixed false positive "metaclass conflict" error that occurs when the metaclass has an unknown class type in its class hierarchy.
    -   Bug Fix: Fixed bug in type evaluator when dealing with a bound TypeVar. The constraint solver wasn't properly handling the `Type[T]` statement in all cases.
    -   Bug Fix: Fixed recent regression in CLI where partial stub packages were not applied correctly.
    -   Enhancement: Eliminate duplicate python search paths, eliminating the need to search the same path more than once on every import resolution.
    -   Bug Fix: Fixed crash in logic that handles partial type stub merging. The crash occurs when a search path points to a file (e.g. a zip file) rather than a directory.
        ([pylance-release#1021](https://github.com/microsoft/pylance-release/issues/1021))
    -   Enhancement: Added support in PEP 646 when the unpacked TypeVarTuple is not at the end of the type parameter list. This allows for suffixing when matching type arguments against type parameters and when matching TypeVarTuple parameters in a Callable.
    -   Enhancement: Added better error reporting for reveal_type and reveal_locals calls.
    -   Enhancement: Added file system caching to import resolver for performance reasons.
    -   Bug Fix: Fixed bug in type-printing logic for tuples. When typeCheckingMode is "off", type arguments are supposed to be displayed if they are not all "Any" or "Unknown", but they were omitted always.
    -   Bug Fix: Fixed bug that caused type evaluation behavior that depends on (including, possibly, false positive errors) when evaluating subexpressions within a case statement.
    -   Enhancement (from Pylance): Fix HTML escaping in code blocks.
        ([pylance-release#816](https://github.com/microsoft/pylance-release/issues/816))
    -   Behavior Change: Exempt ParamSpec from "single use of TypeVar within function signature" check.
    -   Enhancement: Improved error reporting for ParamSpec misuse.
-   [1.1.118](https://github.com/microsoft/pyright/releases/tag/1.1.118)
    -   Bug Fix: Fixed bug in logic that verifies exception type in "raise" statement. It was not properly handling generic types that were bound to BaseException.
    -   New Feature: Add --ignoreexternal CLI flag for use with --verifytypes feature. (Contribution by Vlad Emelianov)
    -   Enhancement: The --verifytypes output now includes file paths in the report. (Contribution by Vlad Emelianov)
    -   Bug FIx: Fixed crash that occurred when a function was declared within a local scope but when the function's symbol was previous declared "global" or "nonlocal" within that scope.
    -   Enhancement (from Pylance): Method and class docstrings now inherit from parent classes if docstrings are missing in child class.
    -   Enhancement (from Pylance): Improved support for partial stubs (where py.typed file includes "partial" as per PEP 561).
    -   Bug Fix: Fixed bug that caused incorrect type evaluation for member access expressions when the member was a descriptor object and the base type was a variable containing a reference to the class.
    -   Bug Fix: Fixed bug in document symbol provider that caused incorrect range to be returned for classes and functions.
        ([pylance-release#1010](https://github.com/microsoft/pylance-release/issues/1010))
    -   Enhancement: Improved tracking of incomplete types (those that have not yet been fully established because of recursive type dependencies within the code flow graph).
    -   New Feature: Added logic for if/elif chains that contain no else clause but completely narrow one or more variables.
    -   Behavior Change: Changed behavior of TypeVar constraint solver to eliminate literal types (widening them to their associated type) when solving for TypeVars, unless a literal type was explicitly provided (e.g. using explicit specialization like `List[Literal[1, 2, 3]]`).
    -   Behavior Change: Changed reportOverlappingOverload to be an error in strict mode.
    -   Bug Fix: Fixed bug in logic that determines whether one callable type can be assigned to another. It wasn't taking into account the positional-only parameter separator (`/`).
        ([pylance-release#1017](https://github.com/microsoft/pylance-release/issues/1017))
    -   Bug Fix: Fixed a bug in conditional type narrowing that narrows based on descriminated member variable types. It was being over aggressive in narrowing in the negative ("else") case when the type of the member was a union of literal types.
    -   Bug Fix: Fixed false positive error that occurred when setting or deleting the member of an object where that member's type is defined by a parent class and is generic but is specialized by a child class.

## 2021.3.0 (3 March 2021)

Notable changes:

-   Method docstrings are now inherited from parent classes.
    ([pylance-release#550](https://github.com/microsoft/pylance-release/issues/550), [pylance-release#877](https://github.com/microsoft/pylance-release/issues/877))
-   The matplotlib and PIL stubs have been updated to be more complete and correct.
    ([pylance-release#73](https://github.com/microsoft/pylance-release/issues/73), [pylance-release#420](https://github.com/microsoft/pylance-release/issues/420), [pylance-release#462](https://github.com/microsoft/pylance-release/issues/462), [pylance-release#716](https://github.com/microsoft/pylance-release/issues/716), [pylance-release#994](https://github.com/microsoft/pylance-release/issues/994))
-   Parentheses in `with` statements will no longer be flagged as invalid.
    ([pylance-release#999](https://github.com/microsoft/pylance-release/issues/999))
-   A case where the same auto-import may be suggested more than once has been fixed.
-   Files ending in `.git` will now be ignored in file watcher events. These files are created by some tools and cause reanalysis on change.
-   Partial stub packages (defined in PEP 561) are now supported.
-   Pylance's copy of typeshed has been updated.

In addition, Pylance's copy of Pyright has been updated from 1.1.114 to 1.1.117, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Bug Fix: Fixed crash that occurred when a function was declared within a local scope but when the function's symbol was previous declared "global" or "nonlocal" within that scope.
    -   Bug Fix: Fixed bug in logic that verifies exception type in "raise" statement. It was not properly handling generic types that were bound to BaseException.
        ([pylance-release#1003](https://github.com/microsoft/pylance-release/issues/1003))
-   [1.1.117](https://github.com/microsoft/pyright/releases/tag/1.1.117)
    -   Enhancement: Extended check that detects redeclared functions and methods to also report redeclared properties within a class.
    -   Bug Fix: Fixed crash in parser that occurs when malformed index expression is parsed.
    -   Enhancement: Improved error message for certain type incompatibilities.
    -   Bug Fix: Fixed bug in logic that determines whether a function type is assignable to another function type. It was not properly handling the case where the destination had a \*\*kwargs parameter and the source had an unmatched keyword parameter.
    -   Enhancement: Added new check to ensure that the type signature of a function with overloads is the superset of all of its overload signatures.
    -   Enhancement: Improved consistency of error messages by standardizing on "incompatible" rather than "not compatible".
    -   Bug Fix: Fixed bug in handling of `type(x)` call that resulted in false positive errors.
    -   Behavior Change: Changed the logic that determines whether a variable assignment is an implicit type alias definition. If there is an explicit type annotation (other than the use of the PEP 612 TypeAlias), it is no longer considered a type alias. This is consistent with the rules mypy uses.
    -   Bug Fix: Fixed a bug in the logic for inferring "cls" parameter that resulted in incorrect type evaluations.
    -   Enhancement: Added check to detect inappropriate use of variables (that are not type aliases) within type annotations.
    -   Bug Fix: Fixed bug in type compatibility logic that permitted a type of `Type[Any]` to be assigned to type `None`.
    -   New Feature: Implemented support for PEP 655: Marking individual TypedDict items as required or potentially-missing. This PEP is still under development, so the spec could change.
-   [1.1.116](https://github.com/microsoft/pyright/releases/tag/1.1.116)
    -   Enhancement: Improved type inference logic for tuple expressions that contain unpacked tuples.
        ([pylance-release#991](https://github.com/microsoft/pylance-release/issues/991))
    -   Bug Fix: Fixed bug that resulted in unknown types within stubs when a forward reference was made within a type alias definition.
    -   Bug Fix: Fixed bug in bidirectional type inference logic for unpack operator.
    -   Bug Fix: Fixed bug in assignment type narrowing for index expressions. The narrowed type was always evaluated as "None" rather than the assigned type.
        ([pylance-release#992](https://github.com/microsoft/pylance-release/issues/992))
    -   Bug Fix: Fixed bug in assignment type narrowing that was triggered when the RHS and LHS were both union types and the RHS contained an `Any`.
        ([pylance-release#993](https://github.com/microsoft/pylance-release/issues/993))
    -   Enhancement: Added diagnostic check for a call expression that appears within a type annotation. This was previously not flagged as an error.
    -   Bug Fix: Fixed false negative bug in the "reportOverlappingOverload" diagnostic check. It was not correctly detecting overlapping overloads when one of the parameters in the earlier overload was annotated with at TypeVar.
    -   Bug Fix: Fixed bug in logic that compares the type compatibility of two functions. In particular, if the source function contains a keyword argument and the dest function does not contain a keyword argument of the same name bug contains a \*\*kwargs, the types must match.
    -   Enhancement: Added support for overloaded `__init__` method that annotates the `self` parameter with a generic version of the class being constructed.
    -   Behavior Change: Added a few exemptions for the reportInvalidTypeVarUse check. In particular, constrained TypeVars, bound TypeVars used as type arguments, and any TypeVar used as a type argument to a generic type alias are exempt from this check. There are legitimate uses for all of these cases.
    -   Bug Fix: Fixed recent regression in type assignment check logic that broke certain cases where the destination and source were both unions that contained type variables.
    -   Behavior Change: Changed behavior when evaluating type of symbol within type stubs. Previously forward references were allowed only for class types. Now, forward references are allowed (and no code flow analysis is employed) for all symbols. The new behavior is consistent with mypy's.
    -   Enhancement: Added new diagnostic check for an overloaded function without an implementation within a source (.py) file. Fixed a bug in the diagnostic check for a single overload when an implementation is present.
    -   Bug Fix: Fixed bug in the parsing of "with" statements where the "with item" starts with an open parenthesis.
    -   Enhancement: Added "collections.defaultdict" to the list of classes that does not support runtime subscripting in versions of Python prior to 3.9.
        ([pylance-release#1001](https://github.com/microsoft/pylance-release/issues/1001))
    -   Behavior Change: Changed behavior of type inference for empty list (`[]`) and empty dict (`{}`) expressions. They were previously inferred to be `List[Any]` and `Dict[Any, Any]`, but they are now inferred as `List[Unknown]` and `Dict[Unknown, Unknown]`. This affects strict mode type checking, where partially-unknown types are reported as errors. This change may require some explicit type annotations within strictly-typed code.
-   [1.1.115](https://github.com/microsoft/pyright/releases/tag/1.1.115)
    -   Bug Fix: Fixed false positive bug where "class not runtime subscriptable" error was reported even if in a type stub.
    -   New Feature: Implemented command-line switches for pythonplatform and pythonversion. These are overridden by pyrightconfig.json settings.
    -   New Feature: Added support for comments and trailing comments within pyrightconfig.json.
    -   Enhancement: Updated to latest typeshed stubs.
    -   Enhancement (from Pylance): Improve auto-import performance.
    -   Enhancement (from Pylance): Added extra perf tracking.
    -   Bug Fix: Fixed false positive error that incorrectly complained about the use of `Annotated` as a class with no type arguments.
    -   Bug Fix: Fixed false positive error when using bidirectional inference of dictionary expression where the expected type key and/or value types contain literals.
    -   Bug Fix: Fixed bug that resulted in wildcard imports (i.e. imports the form `from x import *`) to import symbols from the target that were not meant to be externally visible. This bug occurred only when the imported module had no `__all__` symbol defined.
    -   Bug Fix: Fixed bug in validation of constrained types in TypeVars. Subtypes of constrained types should be allowed.

## 2021.2.4 (24 February 2021)

Notable changes:

-   The mapping of stub files to source files has been greatly improved. Go-to-definition and doc strings should now work for a much wider range of code.
    ([pylance-release#809](https://github.com/microsoft/pylance-release/issues/809), [pylance-release#949](https://github.com/microsoft/pylance-release/issues/949))
-   Index expression type narrowing is now supported. For example, a check like `if some_tuple[1] is not None` will cause future uses of `some_tuple[1]` to not be `None`, without needing to narrow a temporary variable.
-   Auto-import completion performance has been improved.
-   Pylance's copy of typeshed has been updated.

In addition, Pylance's copy of Pyright has been updated from 1.1.112 to 1.1.114, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Bug Fix: Fixed false positive bug where "class not runtime subscriptable" error was reported even if in a type stub.
    -   Enhancement: Implemented command-line switches for pythonplatform and pythonversion. These are overridden by pyrightconfig.json settings.
    -   Enhancement: Added support for comments and trailing comments within pyrightconfig.
    -   Enhancement: Updated to latest typeshed stubs.
    -   Bug Fix: Fixed false positive error that incorrectly complained about the use of `Annotated` as a class with no type arguments.
    -   Bug Fix: Fixed false positive error when using bidirectional inference of dictionary expression where the expected type key and/or value types contain literals.
-   [1.1.114](https://github.com/microsoft/pyright/releases/tag/1.1.114)
    -   Enhancement: Improve source mapper (the code that maps symbols found in stub files to the corresponding code in ".py" files) to handle more cases.
    -   Enhancement: Added diagnostic error for try statement that has no except or finally statement.
    -   New Feature: Added "reportOverlappingOverload" diagnostic rule, splitting out a few checks that were previously in the "reportGeneralTypeIssue" rule. This allows for finer-grained control over these overload checks.
    -   Behavior Change: Added a few additional names that can be used for "cls" parameter without triggering diagnostic. These variants are reasonable and are used within some typeshed stubs.
    -   Enhancement: Added TypeVarTuple definition to typings.pyi stub.
    -   Enhancement: Updated TypeVarTuple logic to detect and report an error when a tuple of unknown length is bound to an unpacked TypeVarTuple. This is illegal according to the latest version of PEP 646.
    -   Enhancement: Special-cased the `__init_subclass__` method in the completion provider so it is offered as a suggestion even though there is no @classmethod decorator present. This symbol is unfortunately inconsistent from all other class methods in that it doesn't require a @classmethod decorator for some reason.
        ([pylance-release#972](https://github.com/microsoft/pylance-release/issues/972))
    -   Behavior Change: Changed logic for attributes marked `ClassVar` to allow writes from an instance of the class as long as the type of the attribute is a descriptor object.
    -   Bug Fix: Fixed a hole in type comparison logic for TypeVars that could have theoretically resulted in incorrect aliasing of types.
    -   Bug Fix: Fixed bug that caused false positive when import statement targeted a symbol that had a nonlocal or global name binding.
        ([pylance-release#977](https://github.com/microsoft/pylance-release/issues/977))
    -   Behavior Change: Enhanced method override compatibility logic to allow instance and class methods to pass generic bound types for `self` and `cls`.
    -   New Feature: Added support for ".pth" files (often used for editable installs) when using the "venv" configuration option in pythonconfig.json.
    -   Bug Fix: Fixed bug whereby import symbol “A” in the statement “from . import A” was not considered a public symbol in a py.typed source file, but it should be.
    -   Enhancement: Improved handling of enum classes. If such a class is defined in a ".py" file, variables defined in the class with type annotations but no assignment are now considered instance variables within each enum instance, whereas variables assigned within the enum class are assumed to be members of the enumeration. This is consistent with the way the EnumMeta metaclass works. In stub files, type annotations without assignments are still assumed to be members of the enumeration, since that's the convention used in typeshed and other stubs.
    -   Enhancement: Added check for parameter names when comparing functions. Parameter names that do not begin with an underscore must match in name. This also affects method override checks and protocol matching checks.
    -   Bug Fix: Fix potential infinite recursion in source mapping, crash in doc strings
-   [1.1.113](https://github.com/microsoft/pyright/releases/tag/1.1.113)
    -   Bug Fixes: Improved support for PEP 634 (Structured Pattern Matching):
        -   Improved negative-case type narrowing for capture patterns. Because capture patterns capture anything, the remaining type is "Never".
        -   Improved type narrowing for mapping patterns used in structural pattern matching when the subject expression type contains a typed dictionary.
        -   Added code to detect and report cases where irrefutable patterns are used within an "or" pattern and are not the last entry.
        -   Added logic to verify that all "or" subpatterns target the same names as specified in PEP 634.
        -   Added code to detect the case where a case statement without a guard expression uses an irrefutable pattern but is not the final case statement. This is disallowed according to PEP 634.
        -   Fixed bug in parser that resulted in incorrect text ranges for parenthetical patterns.
    -   Bug Fix: Improved performance for completion suggestions, especially when large numbers of suggestions are returned.
    -   Enhancement: Updated typeshed stubs to the latest.
    -   Enhancement: Enabled postponed type annotation evaluation by default for Python 3.10.
    -   Bug Fix: Fixed bug that caused a false positive when a bound TypeVar was used to access a class method that was annotated with a bound TypeVar for the "cls" parameter.
    -   Bug Fix: Fixed bug that caused index expressions to be printed incorrectly when they appeared in error messages.
    -   Enhancement: Added type narrowing support for index expressions that use a numeric (integral) literal subscript value.
    -   Enhancement: Improved the logic that determines whether a call expression within the code flow graph is a "NoReturn" call. It now provides better handling of unions when evaluating the call type.
        ([pylance-release#967](https://github.com/microsoft/pylance-release/issues/967))
    -   Enhancement: Added support for parenthesized list of context managers in "with" statement for Python 3.10.
    -   Bug Fix: Fixed bug that prevented the use of a generic type alias defined using a PEP 593-style "Annotated" with a bare TypeVar.

## 2021.2.3 (17 February 2021)

Notable changes:

-   PEP 634 ("match") is now supported, including parser and type checking support. This feature will be available in Python 3.10.
-   Completion performance has been improved when the completion list contains a large number of items, which is common when indexing is enabled (`"python.analysis.indexing": true`) and many auto-imports are suggested.
-   Indexing has been re-enabled in the insiders build.
-   The bundled Django stubs have been updated to their latest version.

In addition, Pylance's copy of Pyright has been updated from 1.1.109 to 1.1.112, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Enhancement: Improved type narrowing for mapping patterns used in structural pattern matching when the subject expression type contains a typed dictionary.
    -   Enhancement: Improved negative-case type narrowing for capture patterns. Because capture patterns capture anything, the remaining type is "Never"
-   [1.1.112](https://github.com/microsoft/pyright/releases/tag/1.1.112)
    -   Bug Fix: Fixed false negative when PEP 585 type is used in a type alias or other cases where postponed evaluation is not possible.
        ([pylance-release#953](https://github.com/microsoft/pylance-release/issues/953))
    -   Bug Fix: Fixed regression that resulted in error when "match" is used in expressions but is mistaken for a pattern-matching statement.
    -   Bug Fix: Fixed schema for "python.analysis.logLevel" setting. The default value was specified incorrectly. Thanks to Rafał Chłodnicki for this fix.
    -   Bug Fix: Fixed a bug that caused a false positive when a TypeVar is bound to a generic protocol class.
    -   Bug Fix: Fixed a bug that caused a false positive when a boolean operator was applied to a type variable and the corresponding magic method used an explicit type annotation for the "self" parameter.
    -   Enhancement: Added a new diagnostic check for out-of-range indexes for tuples that have known lengths.
    -   Enhancement: Added limited support for negative type narrowing in pattern matching. For example, if the type of the subject expression is bool and the matching pattern is `False | x`, the type of `x` will be inferred to be `True`.
    -   Bug Fix: Fixed bug that affected generic type aliases that contained Callable types that are parameterized by a type variable.
    -   Enhancement: Extended abstract method checks to Protocol classes even though they don't explicitly derive from ABCMeta.
    -   Bug Fix: Fixed bug in type narrowing for class patterns in "case" statements.
-   [1.1.111](https://github.com/microsoft/pyright/releases/tag/1.1.111)
    -   New Feature: Implemented PEP 634 support for structural pattern matching. This new PEP was just accepted, and the functionality will appear in the next alpha release of Python 3.10.
    -   Bug Fix: Fixed bug that caused a false positive error when declaring a class within a local scope when the symbol is nonlocal or global.
        ([pylance-release#950](https://github.com/microsoft/pylance-release/issues/950))
    -   Enhancement: Improved handling of unpacked arguments when the type is a union of known-length tuples.
-   [1.1.110](https://github.com/microsoft/pyright/releases/tag/1.1.110)
    -   Bug Fix: Fixed a bug in isinstance type narrowing logic where the type of the second argument to isinstance is type `Type[T]` and the first argument is a union of types that includes type `T`.
    -   Enhancement: Expanded reportUnusedCallResult diagnostic check to also check for expressions of the form `await <call expression>`.
    -   Bug Fix (from Pylance): Changed language server to set the working directory before attempting to execute script to retrieve sys.paths.
    -   Behavior Change (from Pylance): Separated behavior of "go to definition" and "got to declaration". The former tries to take you to the source, whereas the latter takes you to the stub file.
    -   Bug Fix: Changed binding logic to not assume that an assignment to a simple name can generate an exception. This fixes a reported false positive error in a type narrowing case.
    -   Enhancement: Added proper error check for the use of an unpack operator (\*) when used outside of a tuple.
    -   Bug Fix: Avoid generating a diagnostic for reporUnknownMemberType if the member access expression is used as a call argument and is a generic class that is missing type arguments. This case was already special-cased for reportUnknownArgumentType to handle common cases like `isinstance(x, list)`, but it was resulting in errors for `isinstance(x, re.Pattern)`.
    -   Bug Fix: Fixed a hole in the detection of unspecified type arguments for the Tuple and tuple classes.
    -   Enhancement: Added support for generic classes that are parameterized by ParamSpecs, as allowed in PEP 612.

## 2021.2.2 (11 February 2021)

This is a hotfix release, reverting a change in 2021.2.1 which was intended to fix file watching for non-workspace folders, but instead led to "too many files open" messages on macOS.
([pylance-release#936](https://github.com/microsoft/pylance-release/issues/936))

## 2021.2.1 (10 February 2021)

Notable changes:

-   Go-to-definition now brings you to source files (e.g. `.py` files), and a new "go-to-declaration" option brings you to stub files (`.pyi`). If either would otherwise return no result, Pylance will bring you to whichever files are available.
    ([pylance-release#65](https://github.com/microsoft/pylance-release/issues/65))
-   Pylance now correctly handles file change events outside of the workspace, triggering reanalysis on actions such as `pip install`. Environments stored in the workspace were not affected by this bug.
    ([pylance-release#923](https://github.com/microsoft/pylance-release/issues/923))
-   Some potentially nondeterministic behavior in `NoReturn` inference has been fixed, which could potentially lead to code being greyed out as unreachable.
    ([pylance-release#248](https://github.com/microsoft/pylance-release/issues/248))
-   A bug that could lead to execution of `json.py` in the workspace root and invalid entries in `sys.path` has been fixed. Thanks to [David Dworken](https://daviddworken.com) for reporting this issue.
-   The bundled Django and SQLAlchemy stubs have been updated to their latest versions.

In addition, Pylance's copy of Pyright has been updated from 1.1.108 to 1.1.109, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Behavior Change: Expanded reportUnusedCallResult diagnostic check to also check for expressions of the form `await <call expression>`.
    -   Bug Fix: Fixed a bug in isinstance type narrowing logic where the type of the second argument to isinstance is type `Type[T]` and the first argument is a union of types that includes type `T`.
-   [1.1.109](https://github.com/microsoft/pyright/releases/tag/1.1.109)
    -   Enhancement: Added some performance optimizations to handle cases where there are many overloads for a function (>100). Previous code hit n^2 analysis times where n is number of overloads.
    -   Enhancement: Added perf optimization that avoids reallocation of special form classes (like Protocol and Literal) every time they're used. Since instance of the type is now cached and reused.
    -   Enhancement (from Pylance): Improved formatting of docstrings in hover text, completion suggestions, and signature help.
    -   Enhancement (from Pylance): Added better performance metrics.
    -   Bug Fix (from Pylance): Improved logic to ignore temp files created by code formatters like black.
    -   Bug Fix: Fixed "possibly unbound" false positive error in try/except/else/finally statement in the special case where a "bare except" clause is used.
        ([pylance-release#913](https://github.com/microsoft/pylance-release/issues/913))
    -   Bug Fix: Replaced logic that detects whether a function's inferred type is "NoReturn" — and specifically whether its implementation is a "raise NotImplementedError". The old logic depended results that varied depending on the order in which types were evaluated and was therefore nondeterministic.
        ([pylance-release#248](https://github.com/microsoft/pylance-release/issues/248))
    -   Bug Fix: Fixed false negative where type expressions used as arguments to TypedDict or NamedTuple constructors are not correctly checked for incompatibility with older versions of Python when they contain `|` or use PEP 585 types.
        ([pylance-release#918](https://github.com/microsoft/pylance-release/issues/918))
    -   Behavior Change: Changed PEP 585 violations (e.g. using `list[int]` rather than `List[int]`) to be unconditional errors rather than diagnostics controlled by reportGeneralTypeIssues diagnostic rule. That way, they appear even when type checking is disabled.
        ([pylance-release#916](https://github.com/microsoft/pylance-release/issues/916), [pylance-release#917](https://github.com/microsoft/pylance-release/issues/917))
    -   Bug Fix: Reverted recent change in for/else statement logic because it introduced a regression.
    -   Behavior Change: Changed the `reportUnboundVariable` default severity from "warning" to "none" when typeCheckingMode is "off". There were too many complaints of false positives from users who have no interest in type checking.
        ([pylance-release#919](https://github.com/microsoft/pylance-release/issues/919))
    -   Enhancement: When a redundant form of a from .. import statement is used (e.g. `from x import foo as foo`), always mark the imported symbol as accessed because it is assumed that it is being re-exported.
    -   Bug Fix: Fixed bug that caused incorrect type evaluation when a return type in a generic function used a Callable with Concatenate and a ParamSpec.
    -   Bug Fix: Fixed bug in code that prints types (e.g. in error messages and hover text) that resulted in duplicate types in a union when typeCheckingMode was "off".
        ([pylance-release#920](https://github.com/microsoft/pylance-release/issues/920))
    -   Enhancement: Updated code that prints function types (e.g. for error messages and hover text) to include unioned return types in parentheses to distinguish between `() -> (int | str)` and `() -> int | str`.
    -   Bug Fix: Fixed formatting of usage text in CLI. Fix contributed by @fannheyward.
    -   Bug Fix: Fixed bug that caused problems when the type `ellipsis` was used in a type stub instead of `...`.
        ([pylance-release#925](https://github.com/microsoft/pylance-release/issues/925))
    -   Bug Fix: Fixed recent regression in handling of isinstance second parameter.

## 2021.2.0 (3 February 2021)

Notable changes:

-   Docstring formatting has been greatly improved, and now better supports indented regions (such as parameter blocks in numpy/pandas docs), nested lists (such as those in argparse), and epydoc (used in OpenCV).
    ([pylance-release#41](https://github.com/microsoft/pylance-release/issues/41), [pylance-release#48](https://github.com/microsoft/pylance-release/issues/48), [pylance-release#83](https://github.com/microsoft/pylance-release/issues/83), [pylance-release#601](https://github.com/microsoft/pylance-release/issues/601), [pylance-release#696](https://github.com/microsoft/pylance-release/issues/696))
-   The creation and deletion of temporary files should no longer trigger reanalysis.
    ([pylance-release#905](https://github.com/microsoft/pylance-release/issues/905))
-   A regression that affected pkgutil-style namespace packages has been fixed.
    ([pylance-release#892](https://github.com/microsoft/pylance-release/issues/892))
-   Pylance now supports PEP 637 (indexing with keyword arguments) and PEP 646 (variadic generics). These PEPs are still in the draft phase (targeting Python 3.10) and may change before being finalized.
-   Pylance's copy of typeshed has been updated, including support for its new directory layout.

In addition, Pylance's copy of Pyright has been updated from 1.1.106 to 1.1.108, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Enhancement: Added perf optimization that avoids reallocation of special form classes (like Protocol and Literal) every time they're used. Since instance of the type is now cached and reused.
    -   Enhancement: Added some performance optimizations to handle cases where there are many overloads for a function (>100). Previous code hit n^2 analysis times where n is number of overloads.
-   [1.1.108](https://github.com/microsoft/pyright/releases/tag/1.1.108)
    -   Behavior change: Changed type inference logic for binary expressions of the form `x or []` so `[]` uses the type of `x` to inform its type.
    -   Bug Fix: Fixed bug in the way a specialized variadic type alias is printed (for error messages, hover text, etc.).
    -   Enhancement: Added support for subscript index lists that contain a trailing comma (e.g. `a[0,]`). The subscript in this case is a tuple and is not valid for most objects, so it should generate an error.
    -   Enhancement: Improved parse error recovery for empty subscripts (e.g. `a[]`). Started to add support for PEP 637.
    -   Enhancement: Improved consistency of error messages.
    -   New Feature: Added support for PEP 637 (keyword and unpacked arguments in subscripts). This PEP is still in the draft phase and may change before being finalized.
    -   New Feature: Added a way for the "verifytypes" feature to ignore partially-unknown types imported from external packages. To use this feature, append a "!" to the end of the package name provided after the "--verifytypes" option.
-   [1.1.107](https://github.com/microsoft/pyright/releases/tag/1.1.107)
    -   Bug Fix: Fixed cyclical type resolution with TypeVar.
    -   Behavior Change: Updated typeshed stubs to new directory layout.
    -   Bug Fix: Fixed false positive error in try/except/finally statement. Call expressions are now assumed to possibly result in raised exceptions, and finally clauses are assumed to be exception targets.
    -   Bug Fix: Fixed regression in import resolution where the first portion of the import path matches multiple namespace packages.
        ([pylance-release#892](https://github.com/microsoft/pylance-release/issues/892))
    -   New Feature: Added initial support for PEP 646 (variadic type variables). This PEP is still in the draft stage and is likely to change before it is ratified.
    -   Enhancement: Added check for duplicate keyword arguments that map to \*\*kwargs parameter.
    -   Enhancement: Added support for class properties, which are now supported in Python 3.9.
    -   Behavior: Eliminated false positive errors for unbound variables that are targets of a for loop iterator and used after the for loop. This change can result in some false negatives.
        ([pylance-release#496](https://github.com/microsoft/pylance-release/issues/496))

## 2021.1.3 (27 January 2021)

Notable changes:

-   Deleting an entire folder in the workspace will now correctly retrigger analysis.
-   Analysis performance has been improved in the case of deeply nested expressions with calls to overloaded functions.
-   Import resolution should now pick the correct module when both a namespace module and a traditional module have the same name in the search paths.
    ([pylance-release#859](https://github.com/microsoft/pylance-release/issues/859))
-   The variable override compatibility check will now correclty ignore private class members.
    ([pylance-release#863](https://github.com/microsoft/pylance-release/issues/863))
-   A number of crashes and analysis bugs have been fixed.
-   The default setting for indexing in the insiders build has been temporarily changed to `false` to pin down potential performance regressions in the feature. It can still be manually enabled with `"python.analysis.indexing": true`.

In addition, Pylance's copy of Pyright has been updated from 1.1.103 to 1.1.106, including the following changes:

-   [1.1.106](https://github.com/microsoft/pyright/releases/tag/1.1.106)
    -   Bug Fix: Added missing check for empty f-string expression.
    -   Bug Fix: Fixed a bug that resulted in incorrect bidirectional type inference when the source was a call to a constructor and the destination (expected) type was a recursive type alias that includes a union with only some subtypes that match the constructed type.
        ([pylance-release#721](https://github.com/microsoft/pylance-release/issues/721))
    -   Bug Fix: Fixed two issues in the import resolution logic. First, it was returning a namespace module if it found one in the workspace path or extraPaths even if a traditional (non-namespace) module satisfied the import from the sys.path. The interpreter searches all paths and always prefers a traditional module if it can find it. Second, it was resolving a namespace module if a traditional module only partially resolved the import path. The real interpreter always prefers a traditional module even if it partially resolves the path (in which case the full import fails).
        ([pylance-release#859](https://github.com/microsoft/pylance-release/issues/859))
    -   Behavior Change: When too few type arguments are provided for a generic class specialization, this diagnostic is now handled via reportGeneralTypeIssues rather than reportMissingTypeArgument. The latter is reserved for cases where type arguments are omitted completely.
    -   Enhancement: Improved type narrowing logic for isinstance and issubclass so they better handle the case where the class passed in the second argument is a type variable.
-   [1.1.105](https://github.com/microsoft/pyright/releases/tag/1.1.105)
    -   Enhancement: Added missing check for \*\* used in argument expressions. The expression after the \*\* must be a mapping with str keys.
    -   Enhancement: Added missing check for a name-only parameter appearing in a signature after a "\*args: P.args" ParamSpec parameter.
    -   Enhancement: Improved error message for non-keyword parameter that follows a "\*" parameter.
    -   Enhancement: Added missing check for positional argument count when a simple positional argument appears after a \*args argument.
    -   Enhancement: Added missing checks for illegal usage of positional parameters when calling a function defined with ParamSpec and Concatenate.
    -   Enhancement: Added missing check for use of keyword arguments in a call to an inner function that uses P.args and P.kwargs defined by a ParamSpec.
    -   Bug Fix: Fixed false positive warning relating to single use of a type variable within a signature when that type variable is a ParamSpec, and it is also referenced in "P.args" or "P.kwargs" annotations.
    -   Enhancement: Added missing PEP 612 support for functions that take a parameter with a callable type that includes a ParamSpec as well as \*args: P.args and \*\*kwargs: P.kwargs parameters.
    -   Bug Fix: Fixed false positive error related to use of "ClassVar" when it is used in a member access expression like "typing.ClassVar".
        ([pylance-release#876](https://github.com/microsoft/pylance-release/issues/876))
    -   Enhancement: Improved performance for deeply nested expressions that involve calls to overloaded functions.
    -   Bug Fix: Fixed crash when "()" is used as a type argument for a class that doesn't accept variadic type parameters.
-   [1.1.104](https://github.com/microsoft/pyright/releases/tag/1.1.104)
    -   Bug Fix: Fixed bug in import resolver where a namespace package was chosen over a traditional package if the former had a shorter name.
    -   Enhancement: Added support for `__call__` method overloads when assigning a callable object to a callable type.
    -   Enhancement: Added error for a subscripted type annotation that involves a quoted expression in the LHS of the subscript. This generates runtime errors.
    -   Enhancement: Enhanced reportIncompatibleMethodOverride diagnostic check to support overrides that have `*args` and `**kwargs` parameters.
    -   Enhancement: Improved completion suggestions to better handle super calls in base class methods.
    -   Bug Fix: Fixed bug that affected the case where a class variable has a declared type in a base class, and a subclass assigns a value to that class variable but doesn't (re)declare its type. In this case, the type of the expression assigned within the base class should use the expected type declared in the base class for type inference.
        ([pylance-release#861](https://github.com/microsoft/pylance-release/issues/861))
    -   Enhancement: Added missing error logic to handle the case where a type variable is used in the LHS of a member access expression. This isn't supported currently in the Python type system.
    -   Enhancement: Improved error checking and reporting for NewType (for unions, literals, callables, protocol classes, and type variables).
    -   Enhancement: Added error check for an attempt to instantiate a literal (`Literal[1]()`).
    -   Bug Fix: Fixed bug in TypeVar constraint solving logic. If an "Any" or "Unknown" type is being assigned to a constrained TypeVar, it should result in "Any" or "Unknown" rather than the first constrained type.
    -   Enhancement: Added check for multiple functions declared within the same scope that have the same name, with the final one overwriting the earlier ones. This check is suppressed for overloaded functions and property setters/deleters.
        ([pylance-release#865](https://github.com/microsoft/pylance-release/issues/865))
    -   Enhancement: Improved the reportIncompatibleVariableOverride diagnostic check so it ignores symbols with private names (i.e. start with double underscores).
        ([pylance-release#863](https://github.com/microsoft/pylance-release/issues/863))
    -   Bug Fix: Changed hover text to use the last declaration of a symbol rather than the first declaration to determine which type category text (e.g. "(module)" or "(class)") in the hover text.
        ([pylance-release#867](https://github.com/microsoft/pylance-release/issues/867))
    -   Bug Fix: Fixed bug that caused error when invoking the definition provider on an unresolved module import.
    -   Bug Fix: Fixed bug in logic that infers symbol types that resulted in "unbound" types to be reported incorrectly in certain rare circumstances.
        ([pylance-release#864](https://github.com/microsoft/pylance-release/issues/864))
    -   Bug Fix: Fixed a crash in the "--verifytypes" feature of the CLI.
    -   Bug Fix: Fixed bug in file watching logic so it properly handles cases where an entire folder is deleted.

## 2021.1.2 (20 January 2021)

Notable changes:

-   Completions for method overrides in classes without a parent class will no longer generate unnecessary `super()` calls.
-   Signature help tooltips will now work when the closing parenthesis is missing.
-   Code in `context.surpress` blocks should no longer be unintentionally grayed out in some cases.
    ([pylance-release#494](https://github.com/microsoft/pylance-release/issues/494))
-   Methods prefixed with a single underscore are now correctly checked for incompatible overrides.
    ([pylance-release#843](https://github.com/microsoft/pylance-release/issues/843))
-   An internal error related to NewType when used with Protocols has been fixed.
    ([pylance-release#825](https://github.com/microsoft/pylance-release/issues/825))
-   `@final` and `Final` checks will now ignore private class members and no longer ignore members prefixed with a single underscore when checking for redeclarations.
    ([pylance-release#725](https://github.com/microsoft/pylance-release/issues/725))

In addition, Pylance's copy of Pyright has been updated from 1.1.101 to 1.1.103, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Bug Fix: Fixed bug in import resolver where a namespace package was chosen over a traditional package if the former had a shorter name.
        ([pylance-release#853](https://github.com/microsoft/pylance-release/issues/853))
    -   Enhancement: Added support for `__call__` method overloads when assigning a callable object to a callable type.
    -   Enhancement: Added error for a subscripted type annotation that involves a quoted expression in the LHS of the subscript. This generates runtime errors.
    -   Enhancement: Enhanced reportIncompatibleMethodOverride diagnostic check to support overrides that have `*args` and `**kwargs` parameters.
    -   Behavior Change: Changed error message about quoted type annotations with non-quoted subscripts to be conditional based on stubs and Python version. This will be supported at runtime in Python 3.10.
-   [1.1.103](https://github.com/microsoft/pyright/releases/tag/1.1.103)
    -   Bug Fix: Suppressed "symbol is unbound" error when used in a `del` statement, since this is legal.
    -   Enhancement: Enhanced --verifytypes command so it can now accept a module path within a package. Type analysis is limited to the specified module and its submodules.
    -   Bug Fix: Fixed bug that caused "--verifytypes" feature to report missing return type annotations for all property getters within a class if only one of them was missing a return type annotation.
    -   Enhancement: Added missing error logic to handle the case where a type variable is subscripted in a type expression. This isn't supported currently in the Python type system.
    -   Enhancement: Improved signature help in case where right parenthesis is missing.
    -   Enhancement: Added error for incorrect use of list expression for type arguments.
-   [1.1.102](https://github.com/microsoft/pyright/releases/tag/1.1.102)
    -   Enhancement: Added error for Callable that is missing a return type.
    -   Behavior Change: Changed type analysis behavior when reportGeneralTypeIssues diagnostic rule is disabled and an incompatible type is assigned to a variable. Previously, the assigned type was retained in this case, but now the declared type is assumed (as it is when reportGeneralTypeIssues is enabled).
    -   Enhancement: Added support for completion suggestions within subscript for typed dict attribute names.
    -   Behavior Change: Change string literals to use "constant" type when displayed in completion suggestion lists.
    -   Behavior Change: Changed logic for detecting overrides of Final member variables by subclasses. Symbols with double underscores are now exempt from this check, since they are considered private and are name-mangled.
        ([pylance-release#725](https://github.com/microsoft/pylance-release/issues/725))
    -   Bug Fix: Fixed bug in logic that detects overrides of @final methods. The logic was not handling the case where a private (single underscore) method was marked final.
        ([pylance-release#725](https://github.com/microsoft/pylance-release/issues/725))
    -   Enhancement: Updated typeshed stubs to latest.
    -   Bug Fix: Fixed regression in code that handles context managers that suppress exceptions.
        ([pylance-release#494](https://github.com/microsoft/pylance-release/issues/494))
    -   Bug Fix: Fixed bug that resulted in infinite recursion (and an internal error) when NewType was used with a protocol class.
        ([pylance-release#825](https://github.com/microsoft/pylance-release/issues/825))
    -   Bug Fix: Fixed reportIncompatibleMethodOverride diagnostic check so it doesn't ignore incompatible protected methods (those whose names start with a single underscore).
        ([pylance-release#843](https://github.com/microsoft/pylance-release/issues/843))
    -   Enhancement: Added support for "reveal_locals()" call to reveal all of the symbols within the current scope.
    -   Bug Fix: Fixed internal error resulting from an assignment expression located within a list comprehension scope which is contained within a class scope.
    -   Enhancement: Augmented type completeness JSON output to include alternate public names of exported symbols. For example, if a symbol "foo" is declared in module "a.b.c" and is also re-exported from "a", then the main name of the symbol is "a.b.c.foo", but it has an alternate name of "a.foo".
    -   Enhancement: Improved "partially unknown type" error messages within type completeness report.

## 2021.1.1 (13 January 2021)

Notable changes:

-   The new "report issue" VS Code command can automatically fill out a new GitHub issue template for simpler bug reporting.
    ([pylance-release#762](https://github.com/microsoft/pylance-release/issues/762))
-   The PYTHONPATH environment variable is now supported. This requires a recent insiders build of the Python extension (or the yet-to-be-released January version).
    ([pylance-release#275](https://github.com/microsoft/pylance-release/issues/275))
-   Variables that are annotated but assigned a value of the wrong type will now use the annotated type rather than using the incorrect type (while in the "off" type checking mode, Pylance's default).
    ([pylance-release#822](https://github.com/microsoft/pylance-release/issues/822))
-   A number of crashes and performance issues have been fixed.
    ([pylance-release#825](https://github.com/microsoft/pylance-release/issues/825))
-   `TypedDict` keys are now suggested in index expression completions.
    ([pylance-release#827](https://github.com/microsoft/pylance-release/issues/827))
-   The semantic token types for class members and methods have been changed to `property` and `method` respectively, for consistency with the LSP spec and other languages in VS Code.
-   Type stubs for SQLAlchemy are now bundled, improving completions, type checking, and other features.
-   The bundled Django stubs have been updated to the latest version.

In addition, Pylance's copy of Pyright has been updated from 1.1.99 to 1.1.101, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Enhancement: Added error for Callable that is missing a return type.
    -   Behavior Change: Changed type analysis behavior when reportGeneralTypeIssues diagnostic rule is disabled and an incompatible type is assigned to a variable. Previously, the assigned type was retained in this case, but now the declared type is assumed (as it is when reportGeneralTypeIssues is enabled).
        ([pylance-release#822](https://github.com/microsoft/pylance-release/issues/822))
    -   Enhancement: Added support for completion suggestions within subscript for typed dict attribute names.
-   [1.1.101](https://github.com/microsoft/pyright/releases/tag/1.1.101)
    -   Bug Fix: Fixed false negative for "reportUnknownParameterType" diagnostic rule when all function parameters were unannotated.
    -   Bug Fix: Fixed a couple of issues with TypeGuard. Previously, `TypeGuard` was implemented as an alias to `bool` which meant that `bool` was assignable to `TypeGuard` in all circumstances. Now it is special-cased to be assignable only in return statements.
    -   Bug Fix: Fixed bug that caused definition provider to not fully resolve a submodule symbol in certain cases.
    -   Enhancement: Added support for aliases of imported module "sys" when evaluating "sys.platform" and "sys.version".
    -   Behavior Change: Suppressed "Covariant type variable cannot be used in parameter type" diagnostic in the case of an `__init__` method to match mypy behavior.
    -   Bug Fix: Fixed regression that broke type inference for packages with no "py.typed" file and no stubs when "useLibraryCodeForTypes" was enabled.
-   [1.1.100](https://github.com/microsoft/pyright/releases/tag/1.1.100)
    -   Bug Fix: Fixed bug that caused "Type" with no type argument not to be flagged as an error.
    -   Enhancement: Changed pythonPlatform to accept a value of "All" in which case no particular platform will be used over the others.
    -   Bug Fix: Fixed bug that caused improper error when using "self" in a "raise ... from self" statement.
    -   Bug Fix: Fixed bug that caused false negative when using a generic type alias with no type arguments.
    -   Bug Fix: Added cache for logic that determines whether a context manager swallows exceptions (and hence acts like a try/except statement). This cache not only improves performance of code flow walks but also prevents infinite recursion in rare cases.
    -   Behavior Change: Improved handling of unannotated decorator functions. If the decorator returns a function that accepts only \*args and \*\*kwargs (which is common), the type checker now assumes that the decorated function or method's signature is unmodified by the decorator. This preserves the original signature and docstring.
        ([pylance-release#125](https://github.com/microsoft/pylance-release/issues/125))
    -   Bug Fix: Fixed bug that caused types within a "finally" clause to be evaluated incorrectly in situations where the "try" and all "except" and "else" clauses returned, raised, or broke.
    -   Enhancement: Changed error messages that refer to "named" parameters and arguments to "keyword", which is more standard for Python.
    -   Bug Fix: Fixed bug in declaration provider where the declaration of a member wasn't properly resolved when the LHS of the member access was a call to a function that returns a `Type[X]`.
        ([pylance-release#821](https://github.com/microsoft/pylance-release/issues/821))
    -   Bug Fix: Fixed bug that manifest as a problem with enums but was actually a problem in handling the circular dependency between "type" and "object" classes (since "type" is an object and "object" is a type).
    -   Bug Fix: Fixed bug that caused incorrect type evaluation when a class was assigned to a generic protocol that was satisfied by the class's metaclass if the class also derived from a base class that also satisfied the same protocol.
    -   Enhancement: Added code to test for missing annotation in `Annotated`.
    -   Bug Fix: Fixed false negative where a union type was assigned to a constrained type variable. An error should be generated in this situation.
    -   Enhancement: Added additional validation for TypeVar scoping. If an outer class defines the scope for a type var, functions and variables within an inner class cannot use a TypeVar of the same name.
    -   Bug Fix: Improved handling of "py.typed" for namespace packages and packages with submodules.
    -   Enhancement: Added support for `__index__` magic method when used with `__getitem__` or `__setitem__` magic methods.
    -   Enhancement: Added support for matching modules against protocols as specified by PEP 544.
    -   Bug Fix: Fix for missing docs in completion list due to only checking the setter for docs because its definition comes after the getter.

## 2021.1.0 (6 January 2021)

Notable changes:

-   Python files which do not have a `.py` or `.pyi` file extension are now supported.
    ([pylance-release#739](https://github.com/microsoft/pylance-release/issues/739), [pylance-release#803](https://github.com/microsoft/pylance-release/issues/803), [pylance-release#810](https://github.com/microsoft/pylance-release/issues/810))
-   Analysis performance has been improved in cases of deeply nested expressions.
    ([pylance-release#590](https://github.com/microsoft/pylance-release/issues/590), [pylance-release#767](https://github.com/microsoft/pylance-release/issues/767))
-   Numerous type checking error messages have been improved, including for `TypedDict`, type variable scoping, yields, and `ParamSpec` with overloads.
-   Two diagnostics have been added, `reportInvalidTypeVarUse` and `reportUnusedCoroutine`.
-   Pylance's copy of typeshed has been updated.

In addition, Pylance's copy of Pyright has been updated from 1.1.94 to 1.1.99, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Bug Fix: Fixed bug that caused "Type" with no type argument not to be flagged as an error.
    -   Enhancement: Changed pythonPlatform to accept a value of "All" in which case no particular platform will be used over the others.
        ([pylance-release#794](https://github.com/microsoft/pylance-release/issues/794))
    -   Bug Fix: Fixed bug that caused improper error when using "self" in a "raise ... from self" statement.
        ([pylance-release#806](https://github.com/microsoft/pylance-release/issues/806))
    -   Bug Fix: Fixed bug that caused false negative when using a generic type alias with no type arguments.
-   [1.1.99](https://github.com/microsoft/pyright/releases/tag/1.1.99)
    -   Enhancement: Improved error messages for expected TypeDicts. (Contribution from Sam Abey.)
    -   Bug Fix: Fixed bug where an \*args or \*\*kwargs parameter could be specified by name in a function call.
    -   Behavior Change: Changed behavior of kwargs parameter that has a generic (TypeVar) type annotation. Literals are now stripped in this case before assigning to the TypeVar.
    -   Enhancement: Improved mechanism for overloaded `__init__` method that uses `self` parameter annotation to specify the result of a constructor. The new mechanism supports generic type arguments within the `self` annotation.
    -   Bug Fix: Fixed bug that caused sporadic errors when modifying the builtins.pyi stub file.
    -   Bug Fix: Fixed bug with overlapping overload detection. It was reporting an incorrect overlap when a different TypeVar (bound vs unbound) was used in two overloads.
    -   Bug Fix: Fixed another false positive error related to overlapping overload methods with a TypeVar in a parameter annotation.
    -   Bug Fix: Fixed bug that caused internal stack overflow when attempting to assign a class to a protocol that refers to itself.
    -   Enhancement: Improved support for protocol matching for protocols that include properties. Getter, setter and deleter methods are now individually checked for presence and type compatibility, and generics are now supported.
    -   Enhancement: Updated to latest typeshed stubs.
-   [1.1.98](https://github.com/microsoft/pyright/releases/tag/1.1.98)
    -   New Feature: Added new diagnostic rule "reportUnusedCoroutine" that reports an error if the result returned by an async function is not consumed (awaited, assigned to a variable, etc.). This detects and reports a common error when using async coroutines.
    -   Enhancement: Improved error messages for invalid type annotation syntax usage.
    -   Enhancement: Updated to the latest typeshed stubs.
    -   Bug Fix: Fixed recent regression in error message for bound TypeVars that resulted in a confusing message.
    -   Bug Fix: Fixed bug in error messages for parameter type incompatibility; reported parameter number off by one leading to confusing message.
    -   Bug Fix: Fixed bug in type compatibility logic when the destination was a metaclass instance and the dest was a class that derived from that metaclass.
    -   Bug Fix: Fixed bug that caused failure in protocol type matching when the protocol contained a method with an annotated "self" parameter.
    -   Behavior Change: If a class derives from a protocol class explicitly, individual members are no longer type-checked. This improves performance of type evaluation in some cases.
    -   Bug Fix: Fixed bug whereby the presence of a `__getattr__` method on a class with no `__init__` method generated an incorrect error when instantiating the class.
    -   Enhancement: Implemented complete support for module-level `__getattr__` functions as described in PEP 562.
    -   Behavior Change: Eliminated restriction that prevented the analysis of text files that don't end in ".py" or ".pyi".
        ([pylance-release#739](https://github.com/microsoft/pylance-release/issues/739), [pylance-release#803](https://github.com/microsoft/pylance-release/issues/803), [pylance-release#810](https://github.com/microsoft/pylance-release/issues/810))
-   [1.1.97](https://github.com/microsoft/pyright/releases/tag/1.1.97)
    -   Enhancement: Improved type analysis performance in cases where an expression contains deeply-nested expressions that involve calls to overloaded functions or bidirectional type inference.
    -   Bug Fix: Fixed bug in ParamSpec logic that affected the case where a generic function with specialized parameters was matched to the ParamSpec.
    -   Bug Fix: Fixed bug where a union with a NoReturn subtype could have been generated when evaluating a union of iterable types.
    -   Enhancement: Improved type narrowing logic for "a is b" narrowing in the case where b is a union that contains both literal and non-literal subtypes.
    -   Enhancement: Added error condition for the situation where an overloaded function is used in conjunction with a ParamSpec.
    -   Bug Fix: Fixed bug that resulted in a false negative error when performing type assignment checks for functions that contain unspecialized type variables.
    -   Enhancement: Improved error messages that include type variables. The scope that defines the type variable is now included. This avoids confusing and seemingly-contradictory error messages like "type \_T cannot be assigned to type \_T".
    -   Bug Fix: Fixed bug that caused type evaluator to generate different results if someone hovered over the name of a type variable within an index expression before the entire source file was analyzed.
-   [1.1.96](https://github.com/microsoft/pyright/releases/tag/1.1.96)
    -   Enhancement: Updated typeshed stubs to the latest.
    -   Behavior Change: Switched to LSP-native progress reporting rather than using custom progress reporting messages.
    -   New Feature: Added a new diagnostic rule called "reportInvalidTypeVarUse" that flags errors when TypeVars are used incorrectly. In particular, it flags the use of a single instance of a TypeVar within a generic function signature.
    -   Bug Fix: Fixed assertion (and associated crash) that results when an LS client asks the language server to open a non-Python file (i.e. one whose file name doesn't have a ".py" or ".pyi" extension). The server now ignores such requests rather than crashing.
    -   Enhancement: Enhanced ParamSpec mechanism to support parameters that have default values.
    -   Bug Fix: Fixed issue with variable expansion for environment variables used within settings.
    -   Enhancement: Improved error message for yield type mismatch.
    -   Performance Improvement: Added a heuristic to skip call-site return type inference if the number of arguments is above a threshold (6). This avoids long analysis times for complex unannotated functions.
        ([pylance-release#729](https://github.com/microsoft/pylance-release/issues/729))
    -   Bug Fix: Fixed bug in error message for tuple size mismatches in the case where the source tuple has indeterminate length and the dest has a specified length.
    -   Bug Fix: Fixed incorrect assertion (which manifests as a runtime crash) when assigning to a type that is a generic class with no specified type arguments.
    -   Enhancement: Added new error for a protocol class that derives from a non-protocol base class.
    -   Behavior Change: Changed the logic for `Type` vs `type` such that `Type` (the capitalized form) is always used in cases where there is a type argument (such as `Type[int]` or `type[str]` and `type` is used in cases where the non-generic class `type` is intended. This allows `type` to be used in `isinstance` type narrowing.
    -   Bug Fix: Fixed bug in function assignment logic in the case where the destination function has name-only parameters and the source has positional parameters that match those name-only parameters.
    -   Behavior Change: Changed heuristic for when a decorator should be ignored for purposes of type checking. It was previously ignored if the application of the decorator resulted in an "Unknown" type. The new heuristic also ignores the application of the decorator if the resulting type is a union that includes an Unknown subtype. This situation occurs frequently with unannotated decorators where part of the result can be inferred but part cannot.
        ([pylance-release#728](https://github.com/microsoft/pylance-release/issues/728))
    -   Bug Fix: Fixed bug that caused incorrect type evaluation when a relative import referenced a submodule with the same name as a symbol that was imported from that submodule if that submodule was later imported again within the same file (e.g. `from .foo import foo, from .foo import bar`).
        ([pylance-release#750](https://github.com/microsoft/pylance-release/issues/750))
    -   Enhancement: Added support for protocol callable types when performing bidirectional type inference for lambda expressions.
        ([pylance-release#754](https://github.com/microsoft/pylance-release/issues/754))
    -   Enhancement: Improved "isinstance" narrowing to better handle the case where the narrowed expression is a constrained TypeVar. It now preserves the constraint so the value can be assigned back to the TypeVar type.
    -   Bug Fix: Fixed bug in "is None" and "is not None" type narrowing logic when dealing with recursive type aliases.
-   [1.1.95](https://github.com/microsoft/pyright/releases/tag/1.1.95)
    -   Behavior Change: Changed encoding of diagnostics reported through the LSP interface. The diagnostic rule (if applicable) is now reported in the "code" field, and a URL points to general documentation for diagnostic rules.
    -   Enhancement: Added support for type arg lists specified in a tuple expression (like `Dict[(str, str)]`) which is a legal way of writing type annotations.
    -   Bug Fix: Fixed infinite recursion due to a `__call__` method that returns an instance of the class that is being called.
    -   Bug Fix: Fixed bug that caused completion suggestions not to work for member accesses when the LHS of the expression was a type specified in the form `Type[X]`.
    -   Bug Fix: Fixed bug that resulted in an attempt to parse and bind a native library (binary file) resulting in long latencies and out-of-memory errors.
    -   Enhancement: Improved error message for unknown named parameters for TypeVar constructor.
    -   Bug Fix: Fixed recent regression that causes a crash in certain circumstances when binding a method to an object or class in cases where that method doesn't have a "self" parameter but instead just has `*args` and `**kwargs` parameters.
    -   Bug Fix: Fixed bug that resulted in incorrect reporting of unreported variables or parameters when they are accessed within argument expressions in cases where an error is detected when analyzing a call expression.
    -   Enhancement: Expand ${env:HOME} in settings. Thanks to @ashb for the contribution.
    -   Bug Fix: Fixed bug that generated incorrect errors when a callable type included another callable type as an input parameter and the second callable type had generic parameter types.
    -   Bug Fix: Fixed bug that caused a false negative when a default parameter value was assigned to a parameter with a generic type annotation.
    -   Bug Fix: Fixed bug that caused incorrect error to be reported when applying logical operators ("|", "&" or not) to enum.Flag literals.
        ([pylance-release#726](https://github.com/microsoft/pylance-release/issues/726))

## 2020.12.2 (11 December 2020)

Notable changes:

-   Extract method and variable refactorings are now enabled for all users.
-   Binary files will no longer be mistakenly loaded as source code.
    ([pylance-release#706](https://github.com/microsoft/pylance-release/issues/706))
-   Various crashes and stack overflows have been fixed.
    ([pylance-release#709](https://github.com/microsoft/pylance-release/issues/709), [pylance-release#717](https://github.com/microsoft/pylance-release/issues/717))

In addition, Pylance's copy of Pyright has been updated, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Behavior Change: Changed encoding of diagnostics reported through the LSP interface.
    -   Enhancement: Added support for type arg lists specified in a tuple expression (like `Dict[(str, str)]`) which is a legal way of writing type annotations.
    -   Bug Fix: Fixed infinite recursion due to a `__call__` method that returns an instance of the class that is being called.
        ([pylance-release#709](https://github.com/microsoft/pylance-release/issues/709))
    -   Bug Fix: Fixed bug that caused completion suggestions not to work for member accesses when the LHS of the expression was a type specified in the form `Type[X]`.
        ([pylance-release#714](https://github.com/microsoft/pylance-release/issues/714))
    -   Bug Fix: Fixed bug that resulted in an attempt to parse and bind a native library (binary file) resulting in long latencies and out-of-memory errors.
        ([pylance-release#706](https://github.com/microsoft/pylance-release/issues/706))
    -   Bug Fix: Fixed recent regression that causes a crash in certain circumstances when binding a method to an object or class in cases where that method doesn't have a "self" parameter but instead just has `*args` and `**kwargs` parameters.
        ([pylance-release#717](https://github.com/microsoft/pylance-release/issues/717))
    -   Bug Fix: Fixed bug that resulted in incorrect reporting of unreported variables or parameters when they are accessed within argument expressions in cases where an error is detected when analyzing a call expression.
        ([pylance-release#719](https://github.com/microsoft/pylance-release/issues/719))

## 2020.12.1 (9 December 2020)

Notable changes:

-   Context managers that may suppress exceptions (such as `contextlib.suppress`) will no longer mark code after the `with` block as unreachable.
    ([pylance-release#494](https://github.com/microsoft/pylance-release/issues/494))
-   Various stack overflows have been fixed.
    ([pylance-release#701](https://github.com/microsoft/pylance-release/issues/701))
-   Stack traces in error messages should now provide more detailed information, aiding in issue reporting for internal errors and crashes.

In addition, Pylance's copy of Pyright has been updated from 1.1.91 to 1.1.94, including the following changes:

-   [1.1.94](https://github.com/microsoft/pyright/releases/tag/1.1.94)
    -   Bug Fix: Fixed potential source of infinite recursion in type evaluator.
    -   Behavior Change: Changed behavior of tuples to strip literals when converting the variadic list of type arguments into a single "effective" type argument. This means the expression `list((1,))` will now be evaluated as type `list[int]` rather than `list[Literal[1]]`.
        ([pylance-release#697](https://github.com/microsoft/pylance-release/issues/697))
    -   Bug Fix: Fixed bug in parser that generated an inappropriate syntax error when an annotated variable assignment included a star test list on the RHS with an unpack operator.
        ([pylance-release#700](https://github.com/microsoft/pylance-release/issues/700))
    -   Enhancement: Added support for context managers that are designed to suppress exceptions.
    -   Bug Fix: Fix infinite recursion in logic that maps pyi files to py files.
    -   Enhancement: Improved source maps for better stack traces, useful for bug reports.
-   [1.1.93](https://github.com/microsoft/pyright/releases/tag/1.1.93)
    -   Enhancement: Added support for TypeVar objects that are used outside of type annotations.
    -   Bug Fix: Fixed bug that caused incorrect error when performing binary operations (arithmetics, comparisons, etc.) on classes that define corresponding magic methods that are instance methods. When performing the operation on the class, the magic methods in the metaclass should be used instead.
        ([pylance-release#705](https://github.com/microsoft/pylance-release/issues/705))
    -   Enhancement: Added support for frozen dataclasses. Errors are now reported if a frozen dataclass inherits from a non-frozen dataclass and if an attempt is made to set the member of a frozen dataclass.
    -   Bug Fix: Added support for "bytes" type promotions for bytearray and memoryview.
        ([pylance-release#692](https://github.com/microsoft/pylance-release/issues/692))
    -   Bug Fix: Added support for static methods and class methods that are invoked on non-specialized generic classes where the arguments to the method provide sufficient context to fill in the missing class-level type arguments.
    -   Behavior Change: Changed reportWildcardImportFromLibrary diagnostic rule so it doesn't apply to type stub files.
    -   Bug Fix: Fixed bug that resulted in incorrect error when attempting to assign a constrained TypeVar to a union type that satisfied all of the constrained types.
    -   Bug Fix: Added support for binary operator magic methods that operate on constrained TypeVars.
    -   Bug Fix: Fixed the logic that determines whether a type can be assigned to another type when invariance rules are in effect - in particular when the destination is a union. Previously, the unions needed to match exactly. The new logic takes into account whether the destination union contains subtypes that are subclasses of each other.
    -   Bug Fix: Fixed bug where None and Callable types could be assigned to "object" even when invariant rules were in effect. This allowed `List[None]` to be assigned to `List[object]`.
-   [1.1.92](https://github.com/microsoft/pyright/releases/tag/1.1.92)
    -   Bug Fix: Fixed bug in parser that resulted in the opening parenthesis ("(") in a parenthesized expression or tuple not being included in the parse node range.
    -   Bug Fix: Fixed bug that could result in "unaccessed variable" error for variables that were referenced in argument expressions if there were other errors related to the call expression.
    -   Bug Fix: Fixed bug in logic dealing with comment-style function annotations that resulted in spurious errors if "self" was used within an instance method that was so annotated.
    -   Bug Fix: Fixed bug that caused errors when a hierarchy of dataclass classes used generic types for one or more dataclass members.
    -   Bug Fix: Fixed bug in type checker where it allowed invariant type parameters to violate invariance if the destination was an "object" instance.
    -   Bug Fix: Fixed off-by-one error in fstring parsing with debug variables that resulted in errors if the "=" was not preceded by a space.
        ([pylance-release#686](https://github.com/microsoft/pylance-release/issues/686))
    -   Bug Fix: Fixed bug in logic that validates the assignment of a callable type to a generic callable when one of the parameters is another callable.
    -   Bug Fix: Fixed bug that affected generic type aliases that included callable types.
    -   Bug Fix: Fixed bug in bidirectional type inference logic when RHS includes call that returns a generic type. The old logic was prepopulating the type associated with that TypeVar but prevented the type from being further narrowed. This resulted in incorrect errors with argument expressions in some cases.
    -   Enhancement: Added PEP 604 support for unions passed as the second argument to isinstance and issubclass.
    -   Enhancement: Improved error messages for binary operations that involve a TypeVar for one of the operands.
    -   Enhancement: Updated the reportMissingTypeArgument diagnostic check to apply to bound types in TypeVar declarations.

## 2020.12.0 (2 December 2020)

Notable changes:

-   Extract method and extract variable code actions are available for preview in Pylance insiders (`"pylance.insidersChannel": "daily"`).
-   Completion suggestions are now matched more fuzzily. For example, typing `lx` will match a completion for `logical_xor`, even though it does not contain the substring `lx`.
    ([pylance-release#608](https://github.com/microsoft/pylance-release/issues/608))
-   Auto-imports (both completions and quick fixes) will now make use of existing imports when possible. For example, an auto-import completion for `array` when `import numpy as np` is present will now complete to `np.array`, rather than adding `from numpy import array`.
-   Auto-imports will now correctly insert a new import rather than reusing an import statement from a submodule.
    ([pylance-release#646](https://github.com/microsoft/pylance-release/issues/646))
-   Method override completions will now generate a `super()` call.
    ([pylance-release#668](https://github.com/microsoft/pylance-release/issues/668))
-   Completions for overridden methods will now show the correct signature.
-   VS Code's "word based suggestions" (`editor.wordBasedSuggestion`) are now disabled by default in Python files to mitigate poor completions when Pylance specifies no completions are available.
    ([pylance-release#604](https://github.com/microsoft/pylance-release/issues/604))
-   Pylance's copy of typeshed has been updated.

In addition, Pylance's copy of Pyright has been updated from 1.1.86 to 1.1.91, including the following changes:

-   [1.1.91](https://github.com/microsoft/pyright/releases/tag/1.1.91)
    -   Enhancement: Updated to the latest typeshed stubs.
    -   Bug Fix: Fixed bug in fstring parser that generated "unexpected token at end of string" errors if fstring debug (introduced in Python 3.8) was used in conjunction with string-formatting syntax and there was no space between the "=" and the ":".
    -   Bug Fix: Fixed bug that caused a spurious error when defining a property setter when the property getter had no declared return type.
    -   Bug Fix: Fixed bug in isinstance narrowing logic where it didn't properly preserve a TypeVar in the negative ("else") case.
    -   Bug Fix: Fixed bug in type narrowing logic for member access expressions like "a.b.c". A narrowed type needs to be abandoned if any part of the expression is reassigned (e.g. `a.b = <expression>`).
    -   Bug Fix: Fixed bug that resulted a "Never" type appearing as a type argument in an inferred function return type. "Never" should never be used as a type argument. It is now replaced by "Unknown" if it ever does appear.
    -   Bug Fix: (from pylance): Fixed completion case where the completion item said one method, but hover said another once inserted.
    -   Bug Fix: (from pylance): Reuse existing imports for auto-imports (e.g. if `import os.path` is present, `join` will use `os.path.join`).
-   [1.1.90](https://github.com/microsoft/pyright/releases/tag/1.1.90)
    -   Enhancement: Added support for type() call when argument contains a generic class instance.
    -   Enhancement: Improved reportIncompatibleMethodOverride diagnostic check for property overrides. It now checks for missing fget, fset, fdel methods and the overridden method types for each of these.
    -   Enhancement: Added special-case handling of overloaded `__init__` methods where the `self` parameter contains an annotation with a specialized version of the class. This is used in some typeshed stubs to influence the constructed object type when no additional information is available.
    -   Bug Fix: Fixed bug in parser that resulted in incorrect errors when an unpack operator was used within an f-string expression.
    -   Bug Fix: Fixed bug that resulted in incorrect errors when matching synthesized "cls" parameter type. This bug generally affected all TypeVars that were bound to a Type.
    -   Enhancement: Improved type checking support for constrained TypeVars within function and class bodies. This was a significant change, so there's some risk of regressions or new false-positive errors. Please report any bugs you see.
-   [1.1.89](https://github.com/microsoft/pyright/releases/tag/1.1.89)
    -   New Feature: Added support for new reportUnsupportedDunderAll diagnostic rule. It checks for unsupported manipulations of `__all__`.
    -   New Feature: Implemented new diagnostic rule reportUnusedCallResult that checks whether a call expression's results are consumed. If the results are None or Any, no diagnostic is produced.
    -   Enhancement: Added support for isinstance and issubclass type narrowing when "cls" or "self" parameters are used in the second argument
    -   Bug Fix: Fixed recent regression with TypeGuard type that caused spurious error when a bool value was return from a user-defined type guard function.
    -   Bug Fix: Fixed bug in reportIncompatibleMethodOverride diagnostic check where it incorrectly reported an error if a derived class used overload functions on an overridden method.
    -   Bug Fix: Fixed bug that caused incorrect binding when invoking a class method through an instance.
    -   Bug Fix: Fixed handling of recursive type annotations for variables (e.g. "int: int"). In some specific situations this is allowed if the annotation refers to a symbol in an outer scope.
    -   Bug Fix: Fixed several bugs related to constructor type inference when the expected type contained generic types with type arguments that contained type variables defined in a context outside of the constructor's call site.
-   [1.1.88](https://github.com/microsoft/pyright/releases/tag/1.1.88)
    -   Enhancement: This release includes a major update to TypeVar code. The type checker is now much more strict about how TypeVars are treated when analyzing the bodies of generic functions or methods within generic classes.
    -   Bug Fix: Fixed bug in synthesis of comparison operators in dataclass. By default, these methods should not be synthesized unless `order=True` is passed to the `@dataclass` decorator.
    -   Bug Fix: Fixed bug that caused incorrect specialization of a TypeVar when used in a descriptor class with a `__set__` method.
    -   Bug Fix: Fixed incorrectly handling of generic type alias that is defined in terms of other generic type aliases.
        ([pylance-release#636](https://github.com/microsoft/pylance-release/issues/636))
    -   Bug Fix: Fixed bug that caused incorrect overload to be selected in cases where a named argument was used.
    -   Enhancement: Improved signature help for calls to namedtuple constructor.
        ([pylance-release#630](https://github.com/microsoft/pylance-release/issues/630))
    -   Bug Fix: Added support for a generic method whose "self" parameter is annotated with a bound TypeVar and is then invoked using another bound TypeVar.
    -   Bug Fix: Improved error reporting for assignments to protocols.
    -   Enhancement: Added support for the instantiation of a class via a constructor when the type of the class is specified as a TypeVar.
    -   Bug Fix: Fixed inappropriate error in strict mode when a named argument for a call expression begins with an underscore.
    -   Bug Fix: Fixed bug that results in an incorrect type when a call to a function returns a generic type and the result is assigned to a variable with a declared type that includes a union.
-   [1.1.87](https://github.com/microsoft/pyright/releases/tag/1.1.87)
    -   Bug Fix: Fixed bug with type annotations that use a TypeVar with the new union syntax.
    -   Behavior Change: Removed special-case code that eliminates a NoReturn from an async function.
    -   Behavior Change: Changed behavior of NoReturn when it appears within unions. Previously, it was always filtered out of unions. It is now filtered out only in the inferred return type of a function. This allows NoReturn to be used in unions in other legitimate cases.
    -   Bug Fix: Fixed bug that resulted in a false negative when a callable type with a kwargs parameter was assigned to a callable type without a kwargs or with a kwargs of a different type.
    -   Enhancement (from Pylance): Changed fuzzy text matching algorithm for completion suggestions.
    -   Bug Fix: Fixed bug whereby an assignment was not flagged as an error if the target type contains a type var and the source is concrete. This change generally makes the core type checker more strict about the use of type variables.
    -   Enhancement: Added support for "eq" and "order" parameters in dataclass decorator as defined in PEP 557.
    -   New Feature: Added new diagnostic rule "reportFunctionMemberAccess" that reports an attempt to access, set or delete non-standard attributes of function objects.

## 2020.11.2 (18 November 2020)

Notable changes:

-   Pylance now includes generated stubs for select compiled modules in `numpy`, `cv2`, and `lxml`. This should greatly improve usability when working with these libraries.
    ([pylance-release#138](https://github.com/microsoft/pylance-release/issues/138), [pylance-release#150](https://github.com/microsoft/pylance-release/issues/150), [pylance-release#392](https://github.com/microsoft/pylance-release/issues/392))
-   Pylance now offers an insiders program, which provides access to prerelease builds and features. Setting `"pylance.insidersChannel": "daily"` will check daily for updates.
-   `__future__` is now properly suggested as an import.
    ([pylance-release#539](https://github.com/microsoft/pylance-release/issues/539))
-   Type aliases are now properly expanded in completion tooltips.
    ([pylance-release#562](https://github.com/microsoft/pylance-release/issues/562))

In addition, Pylance's copy of Pyright has been updated from 1.1.85 to 1.1.86, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Bug Fix: Fixed bug with type annotations that use a TypeVar with the new union syntax.
    -   Behavior Change: Removed special-case code that eliminates a NoReturn from an async function.
    -   Behavior Change: Changed behavior of NoReturn when it appears within unions. Previously, it was always filtered out of unions. It is now filtered out only in the inferred return type of a function. This allows NoReturn to be used in unions in other legitimate cases.
    -   Bug Fix: Fixed bug that resulted in a false negative when a callable type with a kwargs parameter was assigned to a callable type without a kwargs or with a kwargs of a different type.
-   [1.1.86](https://github.com/microsoft/pyright/releases/tag/1.1.86)
    -   Enhancement (from Pylance): Improvements to completion provider and signature help provider.
    -   Bug Fix: Allow `TypeAlias` to be used prior to Python 3.10 if imported from typing_extensions.
    -   Enhancement: Added special-case handling for magic method `__class_getitem__`, which is implicitly a classmethod.
    -   Enhancement: Added support for classes that include the `__class_getitem__` magic method to provide custom behaviors for subscripting.
    -   Enhancement: Support detecting multiple site-packages directories in venvs. [Contribution by Truls Asheim]
    -   Bug Fix: Fixed bug that caused incorrect type errors when dealing with magic methods on the tuple class.
    -   Bug Fix: Fixed a confusing diagnostic message relating to incorrect method override.
    -   Enhancement: Enforced that TypeVars being solved for in a TypeVar map match the expected scope.
    -   Bug Fix: Fixed bug in synthesized `setdefault` method on TypedDict for required entries, which never use the default value.
    -   Bug Fix: Fixed bug that resulted in an inappropriate error when a kwarg parameter was typed with a class-defined TypeVar (e.g. `**kwargs: _VT`).
    -   Bug Fix: Made the check less strict for the use of covariant type vars within a function input parameter annotation. In particular, unions that contain covariant type vars are now permitted.
    -   Enhancement: Add `__future__` module as import suggestion. [Contribution by cdce8p]
        ([pylance-release#539](https://github.com/microsoft/pylance-release/issues/539))
    -   Bug Fix: Fixed bug that caused the issubtype type narrowing logic to fail when used with a bound TypeVar T in combination with `Type[T]`.
    -   Bug Fix: Don't add suggestions for 'with Y as [ ]'. [Contribution by cdce8p]
    -   Enhancement: Type aliases are now expanded in completion provider text in the same way as the hover text. [Contribution by cdce8p]
        ([pylance-release#562](https://github.com/microsoft/pylance-release/issues/562))
    -   Enhancement: Improve handling of type aliases for auto-import. [Contribution by cdce8p]
        ([pylance-release#606](https://github.com/microsoft/pylance-release/issues/606))

## 2020.11.1 (11 November 2020)

Notable changes:

-   Completions will no longer be offered in contexts where a new name is being typed, including class names, function names, parameter names, and import alias names. This also has the effect of hiding undesirable auto-import completions for test fixtures.
    ([pylance-release#163](https://github.com/microsoft/pylance-release/issues/163))
-   Completions will no longer incorrectly be offered inside of string literals.
    ([pylance-release#383](https://github.com/microsoft/pylance-release/issues/383))
-   Docstring formatting in signature help tooltips will now match hover and completion tooltips.
    ([pylance-release#566](https://github.com/microsoft/pylance-release/issues/566))
-   Tokens that come from the builtins now have a "builtin" semantic modifier for theming.
    ([pylance-release#561](https://github.com/microsoft/pylance-release/issues/561))
-   The "make Pylance your default language server" prompt will now hide permanently if "no" is selected.
    ([pylance-release#568](https://github.com/microsoft/pylance-release/issues/568))
-   The pandas stubs have been updated.
    ([pylance-release#576](https://github.com/microsoft/pylance-release/issues/576))
-   Pylance's copy of typeshed has been updated.

In addition, Pylance's copy of Pyright has been updated from 1.1.83 to 1.1.85, including the following changes:

-   [1.1.85](https://github.com/microsoft/pyright/releases/tag/1.1.85)
    -   Behavior Change: Changed diagnostic about first argument to `super` call to be part of the reportGeneralTypeIssues diagnostic rule so it is suppressed when type checking mode is set to "off".
        ([pylance-release#589](https://github.com/microsoft/pylance-release/issues/589))
    -   Bug Fix: Fixed bug that caused code within finally clause to be marked as unreachable if there was no except clause and the code within the try block always raised an exception.
        ([pylance-release#592](https://github.com/microsoft/pylance-release/issues/592))
    -   Bug Fix: Fixed bugs in ParamSpec logic. It was not properly handling the case where the target callable type contained keyword-only or positional-only parameter separators.
    -   Bug Fix: Added support for `tuple` and `type` subscripts when `__future__` annotations is defined.
    -   Bug Fix: Fixed bug that caused improper errors when using new-style union syntax with `from __future__ import annotations`.
    -   Bug Fix: Worked around a reported bug in node 14+ on Linux where calls to fs.watch throw an exception when creating a recursive file watcher. The workaround is to catch the exception and proceed without a file watcher in place.
    -   Enhancement: Updated typeshed stubs to the latest.
-   [1.1.84](https://github.com/microsoft/pyright/releases/tag/1.1.84)
    -   Bug Fix: Fixed parser crash when an f-string contained an empty expression.
    -   Bug Fix: Fixed bug that caused diagnostics with "information" severity to be reported as "warnings" in the CLI version of pyright.
    -   Bug Fix: Fixed recent regression in handling type evaluations for "and" and "or" operators. Short-circuiting evaluation was not handled correctly in some cases.
    -   Bug Fix: Fixed bug in parser that caused expressions within f-strings to be handled incorrectly if they contained syntax errors.
    -   Bug Fix: Fixed bug in parsing of annotated variable assignments. It was not allowing yield expressions on the right-hand side.
    -   Enhancement: Added special-case logic to handle `isinstance` call when the first argument is a TypedDict and the second argument is a `dict` class. A TypedDict does not derive from `dict` from the perspective of type checking, but at runtime, `isinstance` returns True. This affects both type narrowing logic and checks for unnecessary `isinstance` calls.
    -   Bug Fix: Fixed bug in type narrowing logic for expressions of the form "type(x) is y" or "type(x) is not y". The logic was incorrectly narrowing the type in the negative ("else") case. And in the positive case, it was not properly handling cases where x was a subclass of y.
        ([pylance-release#572](https://github.com/microsoft/pylance-release/issues/572))
    -   Bug Fix: Fixed bug that caused completion suggestions to be presented when typing a period within a comment on the first line of the file.
    -   Enhancement: Improved signature help for data classes where default values are specified.
        ([pylance-release#585](https://github.com/microsoft/pylance-release/issues/585))
    -   Bug Fix: Fixed bug in NamedTuple logic that caused spurious errors when attempting to assign a NamedTuple to a Tuple with a compatible set of type arguments.

## 2020.11.0 (4 November 2020)

Notable changes:

-   Common module aliases (such as `np`, `pd`, `plt`) are now available as completions, in addition to being suggested in quick fixes.
-   Completions on lines containing the character `#` will now work correctly.
    ([pylance-release#461](https://github.com/microsoft/pylance-release/issues/461))
-   Completions for functions in import statements will no longer incorrectly add parentheses when `completeFunctionParens` is enabled.
    ([pylance-release#320](https://github.com/microsoft/pylance-release/issues/320))
-   The bundled Django stubs have been updated to the latest version.
    ([pylance-release#212](https://github.com/microsoft/pylance-release/issues/212))
-   Empty f-string expressions are now parsed correctly.

In addition, Pylance's copy of Pyright has been updated from 1.1.82 to 1.1.83, including the following changes:

-   [1.1.83](https://github.com/microsoft/pyright/releases/tag/1.1.83)
    -   Bug Fix: Fixed bug in perf optimization for set, list, and dictionary type inference. The old code was failing to evaluate expressions associated with entries beyond 64, which meant that tokens were not classified correctly and type errors in these expressions were not reported.
    -   Bug Fix: Do not report errors for union alternative syntax (PEP 604) if evaluation of type annotation is postponed (either in a quote or via PEP 563).
    -   Bug Fix: Fixed bug that caused spurious errors when evaluating type annotations within certain circumstances.
        ([pylance-release#513](https://github.com/microsoft/pylance-release/issues/513))
    -   Bug Fix: Fixed bug that sporadically caused incorrect and confusing type errors such as "list is incompatible with List".
        ([pylance-release#521](https://github.com/microsoft/pylance-release/issues/521))
    -   Bug Fix: PEP 585 says that it should be possible to use `type` in place of `Type` within type annotations. Previously, this generated an error.
    -   Behavior Change: Changed re-export logic for type stub and py.typed modules to honor the clarification that was recently added to PEP 484. Previously, any import that used an "as" clause was considered to be re-exported. Now, symbols are re-exported only if the "as" clause is redundant (i.e. it is of the form `import A as A` or `from A import X as X`).
    -   Bug Fix: Fixed inconsistency in handling of imported symbols that have multiple untyped declarations within the target module. The inconsistency was between the two cases `import x, x.y` and `from x import y`. In the latter case the type resolution logic considered only the last symbol declaration in the target module, but in the former case it was considering all declarations and returning the union of all types.
        ([pylance-release#545](https://github.com/microsoft/pylance-release/issues/545))
    -   Bug Fix: Fixed bug in f-string parsing. It was generating an error for comma-separate list of expressions, which is legal.
        ([pylance-release#551](https://github.com/microsoft/pylance-release/issues/551))
    -   Bug Fix: Fixed inconsistency in type narrowing for `isinstance` and `issubclass` calls. Previously, the narrowing logic used the target class(es) if the source expression was of type Any but did not do the same when the source expression was a union type that included Any but all other subtypes were eliminated.
        ([pylance-release#557](https://github.com/microsoft/pylance-release/issues/557))
    -   Bug Fix: Added logic for `or` and `and` operators to handle the case where the left-hand operand is always falsy (in the case of `or`) or always truthy (in the case of `and`).

## 2020.10.3 (28 October 2020)

Notable changes:

-   Performance while in the "off" type checking mode has been improved (the default for Pylance).
-   A performance regression related to the experimental `TypeGuard` type has been fixed, which should further improve overall performance.
-   The bundled Django stubs have been updated to the latest version.
    ([pylance-release#536](https://github.com/microsoft/pylance-release/issues/536))

In addition, Pylance's copy of Pyright has been updated from 1.1.81 to 1.1.82, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Bug Fix: Do not report errors for union alternative syntax (PEP 604) if evaluation of type annotation is postponed (either in a quote or via PEP 563).
        ([pylance-release#513](https://github.com/microsoft/pylance-release/issues/513))
    -   Bug Fix: Fixed bug in perf optimization for set, list, and dictionary type inference. The old code was failing to evaluate expressions associated with entries beyond 64, which meant that tokens were not classified correctly and type errors in these expressions were not reported.
        ([pylance-release#518](https://github.com/microsoft/pylance-release/issues/518))
-   [1.1.82](https://github.com/microsoft/pyright/releases/tag/1.1.82)
    -   Bug Fix: Fixed internal error that occurs when the type evaluator encounters a circular dependency between a class decorator and the class that it decorates.
    -   Bug Fix: Fixed bug in protocol matching logic that results in incorrect errors indicating a function type mismatch.
    -   Perf Improvement: Conditionalized the logic for the reportPropertyTypeMismatch diagnostic check. It's somewhat expensive, so don't bother executing it if it's disabled.
    -   Perf Improvement: Fixed performance regression introduced along with user-defined type guards.
    -   Enhancement: Added support for reverse logical operators (`__ror__`, `__rand__`, etc.).
    -   Bug Fix: Added code to handle the case where a class has a custom metaclass that handles logical or (the `__or__` method). Previous to this change, use of an `|` operator with classes was assumed to be a misuse of PEP 614 in Python versions prior to 3.10.
        ([pylance-release#513](https://github.com/microsoft/pylance-release/issues/513))
    -   Bug Fix: Fixed bug that resulted in an incorrect error when a list comprehension expression was used within a lambda and the expression referenced one or more of the lambda parameters.
        ([pylance-release#520](https://github.com/microsoft/pylance-release/issues/520))
    -   Bug Fix: Fixed bug that caused incorrect error to be reported for names referenced in global and nonlocal statements when those names were not declared in the outer scope.
        ([pylance-release#526](https://github.com/microsoft/pylance-release/issues/526))
        Bug Fix: Fixed bug that resulted in incorrect error when second argument of isinstance was a "type" or "Type" object.

## 2020.10.2 (21 October 2020)

Notable changes:

-   Incremental text changes are now supported, which should improve performance when editing large files.
-   Invalid diagnostics should no longer appear when semantic highlighting is enabled.
    ([pylance-release#491](https://github.com/microsoft/pylance-release/issues/491))

In addition, Pylance's copy of Pyright has been updated from 1.1.79 to 1.1.81, including the following changes:

-   [1.1.81](https://github.com/microsoft/pyright/releases/tag/1.1.81)
    -   Bug Fix: Fixed bug in parser that caused incorrect errors in chains of comparison or "in"/"not in" operators. The expression "a == b == c" should be parsed as "a == (b == c)", but the code was previously parsing it as "(a == b) == c". This didn't matter in most cases, but it does when the types of a, b and c differ.
        ([pylance-release#506](https://github.com/microsoft/pylance-release/issues/506))
    -   Bug Fix: Fixed bug that resulted in incorrect errors when an instance variable with no type declaration was assigned an enum value. It was assumed to be of that literal enum value type rather than the wider enum type.
    -   Bug Fix: Fixed bug that resulted in false positive error when a class derived from another class that was instantiated from a custom metaclass.
        ([pylance-release#507](https://github.com/microsoft/pylance-release/issues/507))
    -   Bug Fix: Fixed bug that caused type errors when internal type cache was cleared. The code previously used parse node IDs to distinguish between types that are not created via class declarations (NamedTuple, type, NewType, etc.). Since node IDs change when a file is reparsed (due to a change), these IDs cannot be relied upon for type comparisons.
    -   Enhancement: Added support for "typing" module aliases when checking for TYPE_CHECKING symbol in static boolean expressions.
-   [1.1.80](https://github.com/microsoft/pyright/releases/tag/1.1.80)
    -   Bug Fix: Fixed bug that caused an incorrect error when `self.__class__` was used as the second argument to an `isinstance` call.
    -   Bug Fix: Changed logic for function return type inference so "unbound" type is never propagated to callers. This eliminates incorrect and confusing errors.
    -   Bug Fix: Fixed bug in type stub generator. It was not properly handling annotated variables (either those with PEP 593 annotations or older-style type comment annotations).
        ([pylance-release#490](https://github.com/microsoft/pylance-release/issues/490))
    -   Bug Fix: Fixed bug in completion provider that caused submodules within a namespace module not to be suggested within a "from x import y" statement.
        ([pylance-release#359](https://github.com/microsoft/pylance-release/issues/359))
    -   Bug Fix: Fixed misleading error message within "from x import y" statement where x was a namespace package and y was not found. The error was being reported as an "unresolved import x" rather than "unknown symbol y".
    -   Bug Fix: Fixed bug in type evaluator that caused spurious errors related to variables used within "for" and "if" statements within a comprehension.
    -   Bug Fix: Fixed bug that caused incorrect error to be reported when a recursive type alias was used in certain circumstances.
    -   Enhancement: Improved type inference for tuples in circumstances where literals are used within a tuple expression and when tuple expressions are assigned to an expected type that is not a tuple but is a compatible type (such as Iterable).
        ([pylance-release#487](https://github.com/microsoft/pylance-release/issues/487))
    -   Bug Fix: Fixed bug that resulted in incorrect error about TypeVar being used incorrectly. The specific condition was when it was referenced within a method within a generic class and one of the method's parameters also referenced the same TypeVar.
    -   Bug Fix: Fixed bug where declared variable with literal types in type arguments were being stripped of those literals when the variable was exported from a module.
    -   Bug Fix: Fixed bug that caused duplicate error messages involving certain TypeVar assignments.
    -   Enhancement: Added diagnostic check for dictionary unpack operator (\*\*) if the operand is not a mapping object.
    -   Enhancement (from Pylance): Added support for increment text changes in language server interface. This will theoretically improve performance for edits in large source files.

## 2020.10.1 (14 October 2020)

Notable changes:

-   The `pandas` stubs have been further improved.
    ([pylance-release#457](https://github.com/microsoft/pylance-release/issues/457))
-   Semantic tokens will now be refreshed on settings change.
-   Completions for function parameters will no longer incorrectly appear outside call parenthesis.

In addition, Pylance's copy of Pyright has been updated from 1.1.78 to 1.1.79, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Bug Fix: Fixed bug that caused an incorrect error when `self.__class__` was used as the second argument to an `isinstance` call.
    -   Bug Fix: Changed logic for function return type inference so "unbound" type is never propagated to callers. This eliminates incorrect and confusing errors.
        ([pylance-release#488](https://github.com/microsoft/pylance-release/issues/488))
-   [1.1.79](https://github.com/microsoft/pyright/releases/tag/1.1.79)
    -   Bug Fix: Fixed the handling of backslashes within an f-string that is also raw.
    -   Enhancement: Added streaming support for "find all references" so updates appear incrementally.
    -   Enhancement: Improved some internal type transforms to preserve type alias information where possible. This helps types be more readable in hover text and error messages.
    -   Bug Fix: Fixed bug that caused identifiers with non-ASCII characters to sometimes be handled incorrectly.
        ([pylance-release#466](https://github.com/microsoft/pylance-release/issues/466))
    -   Bug Fix: Fixed bug that resulted in an incorrect "unbound variable" error when the variable was used in an assignment expression within an if/else conditional expression.
        ([pylance-release#468](https://github.com/microsoft/pylance-release/issues/468))
    -   Bug Fix: Fixed bug where implementation of an overloaded function was included in the list of overloads leading to incorrect signature suggestions and false positives for various overload diagnostic checks.
    -   Enhancement: Updated typeshed to latest.
    -   Bug Fix: Added missing descriptor for "python.analysis.extraPaths" in Pyright VS Code extension. This caused VS Code to indicate that this setting wasn't known.
    -   Bug Fix: Fixed bugs in import resolver when a project contains multiple namespace packages with the same name.
        ([pylance-release#471](https://github.com/microsoft/pylance-release/issues/471))
    -   Bug Fix: Fixed bug that resulted in "unknown" parameter type when assigning a lambda to a variable with a declared Callable type.
    -   Bug Fix: Fixed issue with call signature arguments.
    -   Enhancement: Added support for plain text doc strings.
    -   Bug Fix: Fixed bug that caused a type variable to be "unknown" in some cases where a generic class type was used without providing explicit type arguments.
    -   Bug Fix: Fixed handling of "Annotated" type introduced in PEP 593. Wasn't properly handling string literals in type arguments.
        ([pylance-release#479](https://github.com/microsoft/pylance-release/issues/479))

## 2020.10.0 (7 October 2020)

Notable changes:

-   Indexing performance has been improved. The indexer is still disabled by default, but we'd appreciate feedback about its behavior. Indexing can be enabled by setting `"python.analysis.indexing": true`.
-   The `pandas` stubs have been further improved.
    ([pylance-release#426](https://github.com/microsoft/pylance-release/issues/426), [pylance-release#427](https://github.com/microsoft/pylance-release/issues/427), [pylance-release#428](https://github.com/microsoft/pylance-release/issues/428), [pylance-release#436](https://github.com/microsoft/pylance-release/issues/436), [pylance-release#444](https://github.com/microsoft/pylance-release/issues/444), [pylance-release#448](https://github.com/microsoft/pylance-release/issues/448), [pylance-release#449](https://github.com/microsoft/pylance-release/issues/449), [pylance-release#457](https://github.com/microsoft/pylance-release/issues/457))
-   Semantic token scopes for some type hints have been fixed.
    ([pylance-release#459](https://github.com/microsoft/pylance-release/issues/459))
-   Type aliases should now be more consistently used in tooltips.
    ([pylance-release#301](https://github.com/microsoft/pylance-release/issues/301))
-   Python 3.9's more permissive decorator syntax is now supported.
-   Recursive type aliases are now supported.
-   Experimental support for a new proposed `typing` extension "TypeGuard" has been added. This extension allows for the creation of user-defined type guards.

In addition, Pylance's copy of Pyright has been updated from 1.1.75 to 1.1.78, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Bug Fix: Fixed the handling of backslashes within an f-string that is also raw.
    -   Enhancement: Improved some internal type transforms to preserve type alias information where possible. This helps types be more readable in hover text and error messages.
        ([pylance-release#301](https://github.com/microsoft/pylance-release/issues/301))
-   [1.1.78](https://github.com/microsoft/pyright/releases/tag/1.1.78)
    -   Bug Fix: Fixed regression were diagnostics reported for constructor argument expressions were being suppressed.
    -   Bug Fix: Fixed bug that was causing "self is unknown type" errors in strict mode for "self" parameters used within a protocol class.
        ([pylance-release#458](https://github.com/microsoft/pylance-release/issues/458))
    -   Enhancement: Added support for arbitrary expressions in decorators for Python 3.9 and newer as specified in PEP 614.
    -   Enhancement: Implemented provisional "TypeGuard" functionality that allows for user-defined type guard functions. This must still go through a spec'ing and ratification process before it is finalized. Until then, details could change.
    -   Enhancement: Added diagnostic messages for incorrect use of contravariant type variable as a method return type or a covariant type variable as a method parameter.
    -   Bug Fix: Added missing comparison operator methods (`__eq__`, `__lt__`, etc.) for dataclass.
-   [1.1.77](https://github.com/microsoft/pyright/releases/tag/1.1.77)
    -   Bug Fix: Fixed bug where float and complex values were being inferred as Literal types when PEP 586 clearly states that complex and float values are not supported for Literal.
    -   Bug Fix: Fixed spurious "variable is unbound" error when symbol was used in a compound conditional expression where the first part of the expression was statically determined to short-circuit the evaluation (e.g. `if False and name:`).
        ([pylance-release#452](https://github.com/microsoft/pylance-release/issues/452))
    -   Bug Fix: Fixed regression relating to bidirectional type inference used for constructor calls.
    -   Bug Fix: Fixed bug that caused an internal error (stack overflow) when analyzing types of symbols that mutually depend upon each other and are potentially (but turn out not to be) type aliases.
    -   Bug Fix: Improved handling of constrained type variables where one of the constraints is a narrower version of another.
        ([pylance-release#453](https://github.com/microsoft/pylance-release/issues/453))
    -   Bug Fix: Eliminated spurious "cannot instantiate abstract class" error when the value being instantiated is typed as `Type[X]`. Even though `X` is abstract, this shouldn't generate an error because `Type[X]` means "any subclass of `X`".
    -   Bug Fix: Fixed handling of bidirectional type inference when source is an expression involving an "and" or "or" binary operator.
    -   Enhancement: Changed type printing logic to include the name of a module for module types for clarity. Rather than 'Module', it now prints 'Module("&lt;name&gt;")'. This string is used in hover text and diagnostic messages.
    -   Bug Fix: Fixed bug in hover provider where it incorrectly labeled variables as "type alias" if they are instantiated from a type alias.
    -   Bug Fix: Fixed bug that caused type narrowing for assignments not to be applied when the source of the assignment was a call to a constructor.
    -   Enhancement: Improved type narrowing for assignments when destination is declared with one or more "Any" type arguments.
    -   Enhancement: Improved bidirectional type inference for list and dict types when destination type is a union that contains one or more specialized list or dict types.
    -   Enhancement: Improved support for generic recursive type aliases. Improved bidirectional type inference for list and dict types when destination type is a wider protocol type (like Iterable, Mapping, Sequence, etc.).
    -   Bug Fix: Added escapes in docstring markdown converter for "<" and ">" characters so they are not interpreted as an HTML tag by the markdown renderer.
-   [1.1.76](https://github.com/microsoft/pyright/releases/tag/1.1.76)
    -   Bug Fix: Fixed spurious error when "Literal" was used with a dynamic type argument in a place where a type annotation wasn't expected.
    -   Enhancement: Improved type verification report for readability.
    -   Bug Fix: Fixed bug where Enum constructor was not handling some variations of parameter types.
    -   Bug Fix: Fix handling of pythonPath setting when it is unset.
    -   Enhancement: Improved logging for import search paths.
    -   Enhancement: Improved experience for auto-import completions by including "Auto-import" in details.
    -   Enhancement: Added optimizations in type validator to avoid checking built-in classes.
    -   Enhancement: Added checks in type validator for metaclasses.
    -   Bug Fix: Improved handling of bidirectional type inference when RHS of assignment is a constructor.
    -   Bug Fix: Added support for `__all__` assignments that include a type annotation. Added support for the `__all__ += <module>.__all__` idiom for mutating the `__all__` value. This idiom is used by numpy.
    -   Bug Fix: Fixed bug that caused symbols referenced by `__all__` not to be marked as accessed in some cases.
        ([pylance-release#446](https://github.com/microsoft/pylance-release/issues/446))
    -   Enhancement: Added diagnostic check for static and class methods used for property getters, setters and deleters.

## 2020.9.8 (2 October 2020)

This is a hotfix release, fixing a regression in 2020.9.7 that caused some `numpy` members (such as `numpy.nan`) to be missing.

## 2020.9.7 (30 September 2020)

Notable changes:

-   The `pandas` stubs have been further improved.
    ([pylance-release#386](https://github.com/microsoft/pylance-release/issues/386), [pylance-release#399](https://github.com/microsoft/pylance-release/issues/399), [pylance-release#405](https://github.com/microsoft/pylance-release/issues/405), [pylance-release#411](https://github.com/microsoft/pylance-release/issues/411), [pylance-release#412](https://github.com/microsoft/pylance-release/issues/412))
-   Imports of the form `from X import Y as Z` and dead code blocks will no longer have spurious errors with semantic highlighting enabled.
    ([pylance-release#376](https://github.com/microsoft/pylance-release/issues/376), [pylance-release#401](https://github.com/microsoft/pylance-release/issues/406))
-   Decorators and declarations now have additional semantic token modifiers for further customization.
    ([pylance-release#401](https://github.com/microsoft/pylance-release/issues/401))
-   Temporary folder creation on multi-user shared systems has been fixed.
    ([pylance-release#421](https://github.com/microsoft/pylance-release/issues/421))
-   Auto-import completions will now show "Auto-import" in the completion list when the tooltip hasn't been expanded.
-   Fixed a regression in the configuration of some paths, which may have prevented the correct python interpreter from being selected.

In addition, Pylance's copy of Pyright has been updated from 1.1.74 to 1.1.75, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Bug Fix: Fixed bug where Enum constructor was not handling some variations of parameter types.
    -   Bug Fix: Fixed spurious error when "Literal" was used with a dynamic type argument in a place where a type annotation wasn't expected.
-   [1.1.75](https://github.com/microsoft/pyright/releases/tag/1.1.75)
    -   Bug Fix: Fixed bug that caused some source files that were part of a "py.typed" package to not be identified as such. This meant that the special rules for "py.typed" exports were not being applied in those cases.
    -   Enhancement: Updated typeshed stubs to the latest.
    -   Behavior Change: Added special-case handling of values within enum classes in a py.typed package. They should be treated as constants and not require type annotations.
    -   Behavior Change: Improved detection of implicit type aliases.
    -   Bug Fix: Fixed bug that caused incorrect error in case where bidirectional type inference was used with a list expression and the expected type was an empty protocol.
        ([pylance-release#409](https://github.com/microsoft/pylance-release/issues/409))
    -   Bug Fix: Fixed a bug where spurious errors were generated when using an unannotated "self" as an argument to a constructor in a generic class.
        ([pylance-release#423](https://github.com/microsoft/pylance-release/issues/423))
    -   Enhancement: Added type narrowing for expressions of the form `<string> in X` and `<string> not in X` where X is a union of TypedDict instances.
    -   Bug Fix: Fixed several bugs related to recursive type aliases. The hover text was sometimes incorrect, type narrowing for "isinstance" was broken in some cases, and the reportUnnecessaryIsInstance rule was reporting incorrect errors.
    -   Bug Fix: Fixed bug in code that prints function types that contain a "named-parameter separator" (`_`). It was emitting an extra slash (`_/`).
    -   Enhancement: Added check for position-only argument separator ("/") appearing as the first parameter in a parameter list. This is a syntax error.
    -   Bug Fix: Fixed incorrect handling of global name bindings when a same-named nonlocal name was present.
        ([pylance-release#429](https://github.com/microsoft/pylance-release/issues/429))
    -   Enhancement: Expanded support for idioms used in libraries to define `__all__`. Tuples are now supported, as are calls to `expand`, `append` and `remove`.
    -   Bug Fix: Fixed bug with synthesized `__set__` and `__del__` property methods. The wrong parameter types were being specified for the 'self' and 'obj' parameters.
    -   Bug Fix: Fixed bug in diagnostics reporting logic that caused stack overflow in some rare cases.
    -   Bug Fix: Fixed bug in `callable` type narrowing logic where the union of the type includes `None`.
    -   Bug Fix: Improved handling of bidirectional type inference for constructor calls on generic types. In particular, the new logic better handles the case where the expected type is a union.
    -   Bug Fix: Fixed bug in type inference for generator types. It was not properly adding the three type arguments for Generator in the inferred return type.
        ([pylance-release#431](https://github.com/microsoft/pylance-release/issues/431))
    -   Behavior Change: Implemented new rules for reexports within a py.typed module. ".py" files now follow PEP 484 rules with an override based on `__all__`.
    -   New Feature: Implemented new "verifytypes" command-line option that analyzes a py.typed package and reports missing or partially-unknown types.
    -   Enhancement: Added limiter for list type inference to clip the number of unique subtypes and avoid poor performance in some cases.

## 2020.9.6 (23 September 2020)

Notable changes:

-   Docstrings for the builtins are now supported. You should now see docstrings in tooltips for functions like `print`, `range`, `open`, `str.split`, types like `int`, `float`, `str`, `Exception`, and more.
    ([pylance-release#49](https://github.com/microsoft/pylance-release/issues/49))
-   Semantic highlighting has been expanded to provide more token types and modifiers. Special tokens such as `self` and `cls`, constants, dunder methods, and type hints in comment will be styled similarly to VS Code's built-in regex-based highlighting.
    ([pylance-release#323](https://github.com/microsoft/pylance-release/issues/323), [pylance-release#335](https://github.com/microsoft/pylance-release/issues/335))
-   String literals are no longer highlighted when hovered or containing a cursor.
    ([pylance-release#172](https://github.com/microsoft/pylance-release/issues/172))
-   Relative paths provided settings like `extraPaths` and `stubPath` will now correctly be resolved relative to the workspace.
    ([pylance-release#326](https://github.com/microsoft/pylance-release/issues/326))
-   When hovering on a class invocation and the `__init__` method does not have a docstring, the class's docstring will be displayed instead.
    ([pylance-release#316](https://github.com/microsoft/pylance-release/issues/316))
-   The `pandas` stubs have been further improved.
    ([pylance-release#385](https://github.com/microsoft/pylance-release/issues/385), [pylance-release#387](https://github.com/microsoft/pylance-release/issues/387), [pylance-release#389](https://github.com/microsoft/pylance-release/issues/389), [pylance-release#390](https://github.com/microsoft/pylance-release/issues/390), [pylance-release#391](https://github.com/microsoft/pylance-release/issues/391), [pylance-release#393](https://github.com/microsoft/pylance-release/issues/393))

In addition, Pylance's copy of Pyright has been updated from 1.1.72 to 1.1.74, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Fixed bug that caused some source files that were part of a "py.typed" package to not be identified as such. This meant that the special rules for "py.typed" exports were not being applied in those cases.
-   [1.1.74](https://github.com/microsoft/pyright/releases/tag/1.1.74)
    -   Bug Fix: Fixed bug that caused some type aliases defined in ".py" files within a py.typed package to be treated as unknown.
    -   Bug Fix: Fixed bug relating to member access expressions used in the LHS of an assignment where the inferred type of the member is an object that does not provide a `__set__` method. This should generate an error, and it was not.
    -   Bug Fix: Fixed bug in completion provider that sometimes resulted in detailed completion information not to be displayed. The provider was making use of an internal "symbol ID" to resolve symbol information lazily when the item was selected from the completion menu, but the symbol ID was not guaranteed to be the same from one call to the next.
        ([pylance-release#382](https://github.com/microsoft/pylance-release/issues/382))
    -   Bug Fix: Fixed a bug where an overloaded function could not be assigned to the type 'object' without generating an error. This should be allowed.
    -   Bug Fix: Fixed bug with the invocation of the `__get__` method. It was not being bound to the correct object when called, resulting in incorrect type variable resolution if the "self" parameter was annotated with a TypeVar.
    -   Behavior Change: Eliminated string literal highlighting within document highlight provider. We received significant user feedback that this was not desirable.
        ([pylance-release#172](https://github.com/microsoft/pylance-release/issues/172))
    -   Bug Fix: Fixed bug in handling the two-argument form of "super". The type evaluator was not properly honoring the second argument, which specifies the class or object that should be use for binding.
        ([pylance-release#395](https://github.com/microsoft/pylance-release/issues/395))
    -   Performance Improvement: Changed the logic that infers the type of a list, set, or dict to look at only the first 64 entries. There were cases where thousands of entries were provided in list and dict statements, and this resulted in very poor performance. In practice, looking at the first 64 entries as part of the inference heuristic is sufficient.
    -   Bug Fix: Fixed bug that caused a enums to be incorrectly reported as "not iterable" in cases where a generic `Type[Enum]` was used.
    -   Bug Fix: Fixed bug where type aliases that referred to literals would have those literal values stripped if the type alias was declared within a class.
    -   Bug Fix: Made the printing of literal types more consistent within error messages and hover text. If the type is an literal type (as opposed to a literal instance), it is now consistently printed as `Type[Literal[...]]`.
    -   Bug Fix: Fixed bug in the handling of overloaded magic methods associated with arithmetic operators. If no overload was found in the primary method (e.g. `__add__`), it was not properly falling back on the reverse method (e.g. `__radd__`).
    -   Bug Fix: Fixed bug that caused the type checker to indicate that None was not compatible with the Hashable protocol.
    -   Enhancement: Improved support for constrained TypeVars. The list of constrained types is now honored when providing completion suggestions and when narrowing types for isinstance/issubclass calls.
    -   Enhancement: Improved type checking for binary operations. Previously, if the right-hand operand was a union and at least one subtype was supported, no error was reported. The new implementation verifies that all subtypes are supported and emits an error if not.
    -   Bug Fix: Fixed bug that reported incorrect error when attempting to index a symbol whose type was annotated with `Type[enum]`.
    -   Enhancement: Improved reporting of errors for call expressions, especially in the case where the call type is a union and one or more subtypes are not callable.
    -   Bug Fix: Fixed a bug in the handling of wildcard imports when a dunder all symbol is present in the target and the dunder all array refers to an implicitly-imported submodule.
        ([pylance-release#402](https://github.com/microsoft/pylance-release/issues/402))
-   [1.1.73](https://github.com/microsoft/pyright/releases/tag/1.1.73)
    -   Behavior Change: Changed reveal_type to return a string literal that represents the printed version of the type.
    -   Behavior Change: Changed reveal_type to use an information diagnostic severity rather than warning. Added support in CLI for information diagnostic severity. These were previously dropped.
    -   Bug Fix: Tweaked the logic for py.typed type inference. Assignments that are type aliases should never be ignored in a py.typed package if they are defined in a pyi file.
    -   Bug Fix: Fixed bug in the parser relating to assignment expressions. It was not allowing for ternary expressions in the RHS.
        ([pylance-release#381](https://github.com/microsoft/pylance-release/issues/381))
    -   Bug Fix: Fixed a bug that caused an incorrect error to be reported when a callable type was assigned to an 'object'. This should be allowed.
    -   Bug Fix: Fixed bug in the completion provider where it was not properly handling object references through "self".
    -   Bug Fix: Fixed bug in the type checker with respect to member accesses where the LHS is a class and the RHS is a property. This should evaluate to a property object.

## 2020.9.5 (16 September 2020)

Notable changes:

-   The `pandas` stubs have been further improved.
    ([pylance-release#302](https://github.com/microsoft/pylance-release/issues/302), [pylance-release#303](https://github.com/microsoft/pylance-release/issues/303), [pylance-release#337](https://github.com/microsoft/pylance-release/issues/337))

In addition, Pylance's copy of Pyright has been updated from 1.1.70 to 1.1.72, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Bug Fix: Tweaked the logic for py.typed type inference. Assignments that are type aliases should never be ignored in a py.typed package if they are defined in a pyi file.
    -   Behavior Change: Changed reveal_type to use an information diagnostic severity rather than warning. Added support in CLI for information diagnostic severity. These were previously dropped.
    -   Behavior Change: Changed reveal_type to return a string literal that represents the printed version of the type.
-   [1.1.72](https://github.com/microsoft/pyright/releases/tag/1.1.72)
    -   Bug Fix: Changed the type of `__path__` attribute for a module from `Iterable[str]` to `List[str]`.
    -   Bug Fix: Fixed a bug that caused a crash in the type checker in some rare cases when a function or class declaration was located within a block of code is unaccessible.
        ([pylance-release#369](https://github.com/microsoft/pylance-release/issues/369))
    -   Behavior Change: Changed python.analysis.logLevel to use "Information" rather than "Info" for consistency with Python extension.
    -   Bug Fix: Changed comment-style type annotations for functions to always allow forward declarations.
    -   Behavior Change: Added special-case logic for the `tuple` constructor. Rather than returning a type of `tuple[_T_co]`, it now returns a type of `tuple[_T_co, ...]`.
    -   Behavior Change: Changed behavior of type evaluator for modules within a "py.typed" package when "typeCheckingMode" is not "off". If it encounters an unannotated symbol, the type evaluator no longer attempts to infer its type. Instead, it returns an unknown type. When "typeCheckingMode" is "off" (the default value for Pylance), inference is still used.
    -   Enhancement: Improved reportMissingTypeArgument diagnostic rule to report cases where some type arguments are provided but some are missing. Previously, it detected only those cases where no type arguments were provided.
    -   Bug Fix: Fixed bug that caused incorrect error to be generated when a yield was used within a lambda.
        ([pylance-release#373](https://github.com/microsoft/pylance-release/issues/373))
-   [1.1.71](https://github.com/microsoft/pyright/releases/tag/1.1.71)
    -   Behavior Change: Added code to disable the Pyright extension when the Pylance extension is installed. The two extensions are not intended to work together.
    -   Bug Fix: Fixed bug in handling of specialized "tuple" class as defined in PEP 585.
    -   Behavior Change: Changed the behavior of the command-line version of pyright when file specs are passed on the command line. Previously, file specs couldn't be used in conjunction with a config file. Now a config file is used, but the specified file specs override the "include" section of the config file.
    -   Enhancement: Added validation of arguments passed to `__init_subclass__` method described in PEP 487.
    -   Enhancement: Added detection of duplicate base classes in a class declaration.
    -   Bug Fix: Fixed bug that generated incorrect "could not create consistent mro" error if one of the base classes was "Generic". The Python interpreter appears to special-case this class.
        ([pylance-release#361](https://github.com/microsoft/pylance-release/issues/361))
    -   New Feature: Added support for new "reportWildcardImportFromLibrary" diagnostic rule that checks for the use of wildcard imports from non-local modules. By default, it is reported as a warning, but in strict mode it is an error.
    -   Enhancement: Added code to synthesize custom overloaded "pop", "setdefault", and "\_\_delitem\_\_" methods for TypedDict classes.
    -   Enhancement: Added support for the direct instantiation of a metaclass rather than using the normal metaclass hook.
        ([pylance-release#360](https://github.com/microsoft/pylance-release/issues/360))

## 2020.9.4 (10 September 2020)

Notable changes:

-   Bug Fix: Addressing memory and cpu issues a number of users had by no longer indexing libraries and unopened files at startup. This will revert auto-import completions and workspace symbols performance to previous levels.
    ([pylance-release#321](https://github.com/microsoft/pylance-release/issues/321))

In addition, Pylance's copy of Pyright has been updated from 1.1.66 to 1.1.70, including the following changes:

-   [1.1.70](https://github.com/microsoft/pyright/releases/tag/1.1.70)
    -   Enhancement: Added support for PEP 585. Standard collection types defined in builtins can now be used like their typing counterparts. This includes "tuple", which needs special-case handling because its class definition in builtins.pyi indicates that it has a single type parameter, but it actually supports variadic parameters.
    -   Bug Fix: Added code to prevent heap overrun errors during parsing/binding, most notably during indexing operations.
    -   Bug Fix: Fixed bug that caused runtime crash if typeshed stubs couldn't be found or didn't define 'tuple'.
    -   Bug Fix: Improved interaction between recursive type aliases and bidirectional type inference for lists and dicts.
    -   Bug Fix: Improved type narrowing for assignments in cases where the destination of the assignment is declared as a union and the assigned type is a narrower form of one of the union elements. Previously, the narrowing logic didn't choose the narrowest type possible in this case.
    -   Enhancement: Added perf optimization for unions that contain hundreds or thousands of int literal values. This is similar to another recent optimization for str literal unions.
    -   From Pylance: Ensure that auto-import doesn't place import statement below usage.
-   [1.1.69](https://github.com/microsoft/pyright/releases/tag/1.1.69)
    -   Enhancement: Improved type analysis perf by about 5% and reduced memory usage slightly by not formatting and logging diagnostic messages in cases where they are suppressed (e.g. argument type mismatches when doing overload matching).
    -   Bug Fix: Fixed bug that affected dependency tracking of source files on platforms with case-insensitive file systems. In some cases, the case of paths differed, and the logic was treating these as separate files.
    -   Enhancement: Added diagnostics for type variables that are used improperly as defined in PEP 484: 1) conflicting type variables that are used in nested generic class declarations, and 2) type variables that are used within annotations outside of a context in which they have meaning.
    -   New Feature: Added support for "higher-order" type variables. You can now pass a generic function as an argument to another generic function, and the type var solver can solve the type variables for both at the same time.
    -   New Feature: Added support for recursive type aliases.
    -   Behavior Change: Updated the default Python version from 3.8 to 3.9. This is used only if it is not otherwise configured and there is no Python environment from which to determine the version.
    -   Enhancement: Added checks for usage of certain built-in types that are defined as generic in the typeshed stubs but generate runtime exceptions if subscripted on older versions of Python (prior to 3.9). Such types need to be enclosed in quotes when used in annotations.
-   [1.1.67](https://github.com/microsoft/pyright/releases/tag/1.1.67)
    -   Bug Fix: Fixed bug that caused the recently-added "discriminated field type narrowing" to be used in cases where it should not. This resulted in types being narrowed inappropriately when a field was typed as a union of literals.
    -   Behavior Change: Changed command-line version to not print any non-JSON output when "--outputjson" option is used.
    -   Behavior Change: Changed behavior when "useLibraryCodeForTypes" is set to "false". Previously, all ".py" library code was ignored in this case. Now, ".py" types are used for types if the package has an associated "py.typed" file as specified in PEP 561. Packages with no "py.typed" file will still be ignored if "useLibraryCodeForTypes" is "false".
    -   Bug Fix: Fixed a couple of bugs that resulted in the hover text incorrectly identifying a symbol as a "type alias".
    -   Behavior Change: Changed type inference logic to use "List", "Set", and "Dict" rather than "list", "set" and "dict" when inferring the type of a list, set or dict expression. These are aliases for the same underlying class, but the upper-case versions are more consistent with type annotations used within the code.
    -   Bug Fix: Fixed "NoReturn" inference logic for async functions. This logic was previously flagging the code after a call to such a function as unreachable.
    -   Enhancement: Improved parser to detect syntax errors involving unpack operator within a comprehension.
    -   Enhancement: Changed import resolution logic to allow binaries (e.g. ".so" files) to satisfy local imports (within the package), not just third-party imports (within site-packages).
    -   Enhancement: Extended bidirectional type inference (expected types) to list comprehensions.
    -   New Feature: Added new diagnostic rule "reportPropertyTypeMismatch" that verifies that the type of the input parameter to a property's setter is assignable to the return type of the getter.
    -   Bug Fix: Fixed bug that caused a crash in the type checker in cases where type arguments were not provided to a few special-case built-in classes.
    -   Bug Fix: Fixed a bug in the handling of generics that involve constrained TypeVars. The TypeVar matching logic was sometimes inappropriately specializing the type using the first constrained type.
    -   Bug Fix: Added special-case handling in type checker for callers who request the type of an expression that happens to be a name used in a call expression to designate a named parameter. This isn't really an expression, so the code wasn't handling it correctly, but callers (such as the hover provider and the new semantic token provider) were assuming that it was safe. This resulted in incorrect "X is not defined" diagnostics being logged.

## 2020.9.0 (3 September 2020)

Notable changes:

-   Pylance now supports semantic highlighting. In order to enable this feature, you must be using at least version 2020.8.106424 of the Python extension, as well as a VS Code theme which includes semantic colorization support (e.g., Dark+, Light+, One Dark Pro, others).
    ([pylance-release#220](https://github.com/microsoft/pylance-release/issues/220))
-   Pylance will now index libraries and unopened files at startup to provide auto-import completions even for variables that have not been fully analyzed. This index is also used to improve the performance of the workspace symbols search.
-   The auto-import completions offered should now more accurately reflect the "intended" import, rather than suggesting importing deeper modules. This helps improve the behavior in libraries that re-export symbols through other modules.
    ([pylance-release#222](https://github.com/microsoft/pylance-release/issues/222), [pylance-release#139](https://github.com/microsoft/pylance-release/issues/139), [pylance-release#28](https://github.com/microsoft/pylance-release/issues/28), [pylance-release#97](https://github.com/microsoft/pylance-release/issues/97))
-   The auto-import completion tooltip now more clearly states what will be added to your import block. For example, a completion for "join" will explicitly say `from os.path import join`, rather than just "Auto-import from os.path".
-   When the `completeFunctionParens` feature is enabled, the signature help will now open automatically, matching the behavior when the parentheses are user-written.
    ([pylance-release#273](https://github.com/microsoft/pylance-release/issues/273))
-   Pylance now includes schemas for `pyrightconfig.json`/`mspythonconfig.json`, which enables code completion and validation for these config files.
    ([pylance-release#40](https://github.com/microsoft/pylance-release/issues/40))
-   Methods which only raise `NotImplementedError` will now be treated as abstract and not be marked as not returning, preventing some child class functions from being spuriously marked as dead code. Explicitly declaring classes and methods as abstract is still strongly preferred as it allows the type checker to more accurately check child classes for correctness.
    ([pylance-release#248](https://github.com/microsoft/pylance-release/issues/248))
-   The default `stubPath` now correctly shows in the VS Code settings UI with its default "typings".
    ([pylance-release#285](https://github.com/microsoft/pylance-release/issues/285))

In addition, Pylance's copy of Pyright has been updated from 1.1.65 to 1.1.66, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Bug Fix: Fixed bug that caused the recently-added "discriminated field type narrowing" to be used in cases where it should not. This resulted in types being narrowed inappropriately when a field was typed as a union of literals.
-   [1.1.66](https://github.com/microsoft/pyright/releases/tag/1.1.66)
    -   Enhancement: Improved completion suggestion behavior when the insertion point is between an identifier and an empty index (e.g. "f[]") or in the presence of a missing right square bracket (e.g. "f.[").
    -   Behavior Change: Changed diagnostic related to type argument count to be controlled by the "reportGeneralTypeIssues" diagnostic rule. It was previously always emitted as an error.
    -   From Pylance: Fix progress reporter type, auto-import/symbol changes, worker thread updates, improve auto-import tooltips (#977)
    -   Enhancement: Updated typeshed stubs to the latest version.
        ([pylance-release#293](https://github.com/microsoft/pylance-release/issues/293))
    -   Bug Fix: Eliminated incorrect error when "super()" was used in a class where one or more parent classes were of an unknown type.
    -   Bug Fix: Changed the handling of old-style comment method annotations to accept an optional annotation for "self" and "cls" parameters.
    -   Bug Fix: Changed handling of dataclass classes that derive from a class whose type is unknown. The synthesized constructor now allows any parameter list in this case.
    -   Enhancement: Improved completion provider to distinguish properties from other methods.
        ([pylance-release#299](https://github.com/microsoft/pylance-release/issues/299))
    -   Behavior Change: Changed heuristics for function return type inference so methods that raise a NotImplementedError and have no other return path have an inferred return type of Unknown rather than NoReturn. Such methods should be marked as abstract, but frequently they are not.
    -   Behavior Change: Changed the behavior of the import resolution logic to fail an import resolution of a multi-part name (e.g. "a.b.c") if it can't be fully resolved. This could produce false positives in cases where third-party libraries are using dynamic tricks to manipulate their package namespace, but it will eliminate false negatives.
    -   Bug Fix: Suppress the use of "Unnecessary" diagnostic hints (used to display variables and code blocks in gray) if the LSP client claims not to support this tag.
    -   Enhancement: Added new "reportMissingTypeArgument" diagnostic rule and enabled it by default in "strict" mode. It generates a diagnostic when a generic class or generic type alias is used in an annotation with no type arguments provided.
    -   Bug Fix: Fixed handling of scopes for nested classes. The previous logic allowed an inner class to access variables defined in an outer class, which is not permitted.
    -   Enhancement: Added check for raise statements that take an exception class but the class constructor requires one or more arguments.
    -   Bug Fix: Fixed bug in tokenizer that cause line numbers to be off when an invalid token occurred at the end of a line.
    -   Bug Fix: Fixed a bug in the Pyright parser. It was not correctly following the Python grammar spec when parsing type annotations, so it generated syntax errors in some cases where that was inappropriate.
    -   Enhancement: Added a check and a general type diagnostic for metaclass conflicts.

## 2020.8.3 (28 August 2020)

Notable changes:

-   Overall memory usage has been improved; in many use cases, peak memory usage has been reduced by 10%.
-   Performance with large unions of `Literal` strings has been greatly improved.
-   Type aliases now show more consistently in tooltips.
-   The upcoming Python 3.10 `typing.TypeAlias` (PEP 613) is now supported.

In addition, Pylance's copy of Pyright has been updated from 1.1.64 to 1.1.65, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Bug Fix: Improved completion suggestion behavior when the insertion point is between an identifier and an empty index (e.g. "f[]") or in the presence of a missing right square bracket (e.g. "f.[")
        ([pylance-release#286](https://github.com/microsoft/pylance-release/issues/286))
    -   Behavior Change: Changed diagnostic related to type argument count to be controlled by the "reportGeneralTypeIssues" diagnostic rule. It was previously always emitted as an error.
        ([pylance-release#290](https://github.com/microsoft/pylance-release/issues/290))
-   [1.1.65](https://github.com/microsoft/pyright/releases/tag/1.1.65)
    -   Bug Fix: Fixed bug in command-line version that caused an error to be reported when "useLibraryCodeForTypes" or "verboseOutput" was specified in the pyrightconfig.json file.
    -   Enhancement: Added support for protocol matching where the protocol includes an overloaded method.
    -   Enhancement: Improved diagnostic messages for function type mismatches.
    -   Enhancement: Improved diagnostic messages for tuple matching and union assignments.
    -   Enhancement: Changed nested diagnostic messages to use non-breaking spaces so indentations are visible within the VS Code "Problems" panel.
    -   Bug Fix: Fixed bug in reportIncompatibleMethodOverride diagnostic check. The logic was checking for wider parameter types when it should have been checking for narrower.
    -   Bug Fix: Fixed bug in method override validation code. It wasn't applying partial specialization of the base class, resulting in inappropriate errors in some cases.
    -   Bug Fix: Fixed bug in the type evaluation of expressions with + or - operators and integer literal operands. These expressions should evaluate to a literal type, not an int.
        ([pylance-release#260](https://github.com/microsoft/pylance-release/issues/260))
    -   Bug Fix: Fixed bug in parsing of f-strings that contain \N escape and a Unicode character name that includes a hyphen.
        ([pylance-release#263](https://github.com/microsoft/pylance-release/issues/263))
    -   Bug Fix: Fixed bug in type evaluator that caused an incorrect error when a class decorator was used for a generic class.
    -   Bug Fix: (From Pylance) Fixed performance problem related to file change events triggered by reads from site-packages.
    -   Enhancement: Enabled support for PEP 613 (TypeAlias).
    -   Bug Fix: Fixed bug that caused type aliases to get expanded in some contexts when they shouldn't.
        ([pylance-release#265](https://github.com/microsoft/pylance-release/issues/265))
    -   Bug Fix: Fixed bug that caused "from .A import \*" to work incorrectly when the wildcard included symbol A.
        ([pylance-release#269](https://github.com/microsoft/pylance-release/issues/269))
    -   Enhancement: Added logic in completion provider to return class variables in base classes when the insertion point is in the context of a subclass body.
    -   Bug Fix: Fixed TypeAlias code to check for Python 3.10 rather than 3.9 since PEP 613 has been moved out to 3.10.
    -   Enhancement: Added performance optimization for TypedDict classes. Entries are now computed once and cached in the class type. This provides a big speed-up for TypeDict classes that have a large number of fields.
    -   Enhancement: Added performance optimization for union types that contain large numbers of string literals. The code for inserting new items into a union is O(n^2); this optimization makes it O(n) for string literal types.
    -   Bug Fix: Fixed bug that caused custom import aliases of "Final", "Literal" and "TypeAlias" to not work correctly.
    -   Bug Fix: Fixed bug that resulted in spurious errors when hovering over module names in import statements.
    -   Bug Fix: Fixed several bugs relating to symbols introduced into a class by its metaclass.
        ([pylance-release#154](https://github.com/microsoft/pylance-release/issues/154))
    -   Bug Fix: Fixed bug that caused type analyzer to crash when a nonlocal binding referred to a symbol that was not present in an outer scope and then was assigned to.

## 2020.8.2 (20 August 2020)

Notable changes:

-   The new `python.analysis.completeFunctionParens` option adds parenthesis to function and method completions. This option is disabled by default.
    ([pylance-release#37](https://github.com/microsoft/pylance-release/issues/37))
-   Workspace symbol searching will no longer search or return results from libraries or bundled type stubs, which greatly improves its performance.
    ([pylance-release#34](https://github.com/microsoft/pylance-release/issues/34), [pylance-release#228](https://github.com/microsoft/pylance-release/issues/228))
-   File watching support has been improved, leading to improved performance and lower peak memory consumption.
-   Settings from MPLS (for example `python.autoComplete.extraPaths` and `python.autoComplete.addBrackets`) will now be automatically ported to their updated names if present and Pylance is enabled.

In addition, Pylance's copy of Pyright has been updated from 1.1.62 to 1.1.64, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Bug Fix: Fixed bug in type evaluator that caused an incorrect error when a class decorator was used for a generic class.
    -   Bug Fix: Fixed bug in parsing of f-strings that contain \N escape and a Unicode character name that includes a hyphen.
        ([pylance-release#263](https://github.com/microsoft/pylance-release/issues/263))
    -   Behavior Change: Changed capitalization of the python.analysis.logLevel setting so it matches Pylance. The settings code in Pyright is case insensitive, but the JSON editor emits a warning if the case doesn't match.
    -   Bug Fix: Fixed bug in the type evaluation of expressions with + or - operators and integer literal operands. These expressions should evaluate to a literal type, not an int.
        ([pylance-release#260](https://github.com/microsoft/pylance-release/issues/260))
    -   Bug Fix: Fixed bug in method override validation code. It wasn't applying partial specialization of the base class, resulting in inappropriate errors in some cases.
    -   Bug Fix: Fixed bug in reportIncompatibleMethodOverride diagnostic check. The logic was checking for wider parameter types when it should have been checking for narrower.
    -   Enhancement: Changed nested diagnostic messages to use non-breaking spaces so indentations are visible within the VS Code "Problems" panel.
    -   Enhancement: Improved diagnostic messages for tuple matching and union assignments.
    -   Enhancement: Added support for protocol matching where the protocol includes an overloaded method.
    -   Bug Fix: Fixed bug in command-line version that caused an error to be reported when "useLibraryCodeForTypes" or "verboseOutput" was specified in the pyrightconfig.json file.
-   [1.1.64](https://github.com/microsoft/pyright/releases/tag/1.1.64)
    -   Bug Fix: Fixed regression that caused "isinstance(x, Callable)" to be flagged as an error when PEP 484 says that it's legal.
        ([pylance-release#247](https://github.com/microsoft/pylance-release/issues/247))
    -   Enhancement: Changed error messages related to "partially unknown" types to expand type aliases, which can obscure the unknown part of the type.
    -   Enhancement: Added support for narrowing types based on the pattern `A.B == <literal>` and `A.B != <literal>` when A has a union type and all members of the union have a field "B" with a declared literal type that discriminates one sub-type from another.
    -   Enhancement: Added bidirectional type inference for ternary expressions.
    -   Bug Fix: Fixed incorrect handling of member accesses when the accessed field had a type that was a union between two or more classes, some with special accessor methods (e.g. `__get__`) and some without.
    -   Enhancement: Improved type checking for assignments of callable types. Previously, certain edge cases were ignored.
    -   Enhancement: Added code to check for overlapping (obscured) overload functions.
    -   Bug Fix: Fixed bug that caused incorrect evaluation of type alias that refers to Literal types. The literal values were being stripped in some cases.
    -   Bug Fix: Fixed recent regression that caused type aliases that described literal types to be printed incorrectly in hover text and error messages.
    -   Enhancement: Added code to report overloads that overlap in an "unsafe" way — i.e. they can potentially accept the same arguments but return different (incompatible) types.
    -   Enhancement: Updated typeshed stubs to latest version.
    -   Bug Fix: Fixed bug in assignment checks between homogeneous multi-length tuples and fixed-size tuples.
-   [1.1.63](https://github.com/microsoft/pyright/releases/tag/1.1.63)
    -   Enhancement: Diagnostic rule severity overrides are now editable in the VS Code settings UI.
    -   Bug Fix: Fixed out-of-memory error that occurred during a workspace "find symbols" operation. We were not properly checking for the heap high watermark during this operation.
        ([pylance-release#254](https://github.com/microsoft/pylance-release/issues/254))
    -   Enhancement: Added support for special type "Counter" exported by typing module, which is an alias for collections.Counter.
    -   Bug Fix: Fixed bug in bidirectional type inference for dictionary statements. The logic was not allowing for dict subclass Mapping.
    -   Enhancement: Improved type checker's handling of "in" operator. It previously flagged an error if the right operand didn't support a `__contains__` method. It now properly checks for iterable types as well.
    -   Bug Fix: Fixed bug that caused incorrect evaluation of symbol types within a chain of assignments (e.g. "a = b = c = 4") in some cases.
    -   Enhancement: Enabled file watcher for libraries to detect changes in installed packages. This behavior is already standard for Pylance, but it was disabled for Pyright.
    -   Enhancement: Improved handling of Tuple type. The type checker now does a better job retaining the types of the individual elements within a Tuple or a class that derives from a Tuple.
    -   Enhancement: Improved support for NamedTuple classes and classed derived from NamedTuple. The type checker now retains types of individual elements when used with unpacking and indexing operators.
        ([pylance-release#251](https://github.com/microsoft/pylance-release/issues/251))
    -   Behavior Change: Changed "find workspace symbols" to return only symbols from within user code or opened files, not library files that are closed.
        ([pylance-release#34](https://github.com/microsoft/pylance-release/issues/34), [pylance-release#228](https://github.com/microsoft/pylance-release/issues/228))
    -   Bug Fix: Fixed recent regression that caused incorrect errors to be generated in sub files for certain call expressions.
        ([pylance-release#243](https://github.com/microsoft/pylance-release/issues/243))
    -   New Feature: Added support for Concatenate as described in latest version of PEP 612. Added ParamSpec and Concatenate to typing.pyi.

## 2020.8.1 (13 August 2020)

Notable changes:

-   The `pandas` stubs have been further improved.
    ([pylance-release#27](https://github.com/microsoft/pylance-release/issues/27), [pylance-release#90](https://github.com/microsoft/pylance-release/issues/90), [pylance-release#144](https://github.com/microsoft/pylance-release/issues/144), [pylance-release#148](https://github.com/microsoft/pylance-release/issues/148), [pylance-release#202](https://github.com/microsoft/pylance-release/issues/202))
-   The VS Code settings editor (both UI and JSON) now provides hints for `python.analysis.diagnosticSeverityOverrides`, listing all valid options, their values, and descriptions.
-   Old-style `# type` comments for function signature type annotations are now supported. This syntax is underspecified and not preferred, but is commonly used to provide compatibility with (the now end-of-life) Python 2, and may improve the usability of some libraries.

In addition, Pylance's copy of Pyright has been updated from 1.1.60 to 1.1.62, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Bug Fix: Fixed bug that caused incorrect evaluation of symbol types within a chain of assignments (e.g. "a = b = c = 4") in some cases.
    -   Enhancement: Improved type checker's handling of "in" operator. It previously flagged an error if the right operand didn't support a `__contains__` method. It now properly checks for iterable types as well.
    -   Bug Fix: Fixed bug in bidirectional type inference for dictionary statements. The logic was not allowing for dict subclass Mapping.
    -   Enhancement: Added support for special type "Counter" exported by typing module, which is an alias for collections.Counter.
        ([pylance-release#229](https://github.com/microsoft/pylance-release/issues/229))
    -   Bug Fix: Fixed out-of-memory error that occurred during a workspace "find symbols" operation. We were not properly checking for the heap high watermark during this operation.
        ([pylance-release#228](https://github.com/microsoft/pylance-release/issues/228))
-   [1.1.62](https://github.com/microsoft/pyright/releases/tag/1.1.62)
    -   Bug Fix: Fixed bug in the handling of unrecognized escape sequences within string literals.
        ([pylance-release#219](https://github.com/microsoft/pylance-release/issues/219))
    -   Bug Fix: Fixed bug related to a subtle interaction between bidirectional type inference of list expressions that contain literal values and TypeVar matching. The previous logic was incorrectly matching T in `List[T]` and the list contained a literal type. It should have stripped the literal if possible.
    -   Enhancement: Added diagnostic message for TypeVar with a single constraint type for consistency with mypy.
    -   Enhancement: Added support for member access completion suggestions when the LHS is a function or a None type.
        ([pylance-release#214](https://github.com/microsoft/pylance-release/issues/214))
    -   Behavior Change: Behavior change for type stub generator: don't emit `__all__` assignments or assignments to self.xxx in function bodies. These violate PEP 484 guidelines for type stubs.
    -   Enhancement: Added diagnostic check to reportInvalidStubStatement that flags parameter default value expressions that are not "..." in stub files.
    -   Bug Fix: Fixed bug that caused annotated types of vargs and kwargs parameters not to be printed in hover text.
    -   Enhancement: Implemented support for older-style function annotation type comments. I previously resisted adding this additional complexity, but we're seeing many libraries that still contain these annotations for backward compatibility with Python 2.
    -   Bug Fix: Fixed bug that caused a crash in the type analyzer when a protocol class referred to itself.
        ([pylance-release#225](https://github.com/microsoft/pylance-release/issues/225))
    -   Enhancement: Added support for "useLibraryCodeForTypes" option in config file. It overrides the client setting of the same name or the "--lib" command-line option.
    -   Bug Fix: Fixed several bugs in logging for config errors.
    -   Enhancement: Added logic to type checker to validate that the "self" or "cls" parameter with a specified type annotation is assignable when binding the method to an object or class.
    -   Enhancement: Improved type assignment diagnostic message. Added "(property)" designator to the end of a property type to differentiate it from a normal attribute.
    -   Enhancement: Added code to validate that method overloads are all abstract or not.
    -   Enhancement: Updated typeshed stubs to the latest.
-   [1.1.61](https://github.com/microsoft/pyright/releases/tag/1.1.61)
    -   Bug Fix: Fixed bug that caused symbols to be marked unaccessed if they were accessed by code that is not accessible (e.g. due to conditional execution based on the platform).
    -   Bug Fix: Updated PEP 604 and PEP 612 error message to refer to Python 3.10 instead of 3.9.
    -   Behavior Change: Changed logic that validates "self" or "cls" parameter names to ignore the check if the provided parameter name begins with an underscore, as is seen in several typeshed stub files.
    -   Bug Fix: Fixed bug in nested f-string parsing when f-string contains triple quotes that include single quotes.
        ([pylance-release#203](https://github.com/microsoft/pylance-release/issues/206))
    -   Bug Fix: Fixed handling of a class that is subclassed from both Enum and another class (like str).
    -   Enhancement: Added support for generic classes that refer to themselves as type arguments within their base class.
    -   Bug Fix: Improved error message for partially-unknown types that have a type alias.
    -   Bug Fix: Allow use of forward-declared classes as subclass in class declarations within type stub files.
    -   Bug Fix: Add special-case handling of `__class_getitem__` method, which acts as a class method even though it is not decorated as such.
    -   Bug Fix: Added missing validation of arguments to `type` call.
    -   Enhancement: Added `=` character to end of named parameter for completion suggestions within a call signature.
        ([pylance-release#209](https://github.com/microsoft/pylance-release/issues/209))
    -   Bug Fix: Added client capability check for signature information "labelOffsetSupport" for compatibility with clients that don't support this capability.
    -   Bug Fix: When adding completion suggestions to the list for expression completion, avoid adding duplicately-named symbols that appear in nested scopes.
        ([pylance-release#215](https://github.com/microsoft/pylance-release/issues/215))
    -   Bug Fix: Fixed bug related to calls of methods on a metaclass via classes that are constructed by that metaclass.
    -   Enhancement: Added check for single @overload function with no additional overloads.

## 2020.8.0 (5 August 2020)

-   Added `python.analysis.autoImportCompletions` setting (`true` by default), which allows auto-import completions to be disabled.
    ([pylance-release#64](https://github.com/microsoft/pylance-release/issues/64))
-   Fixed the "make Pylance your default language server" prompt when language server setting was previously set outside of the user settings.

In addition, Pylance's copy of Pyright has been updated from 1.1.58 to 1.1.60, including the following changes:

-   [1.1.60](https://github.com/microsoft/pyright/releases/tag/1.1.60)
    -   Bug Fix: Fixed a bug "aliased import with leading underscore produces private usage error".
    -   Bug Fix: Fixed a bug that caused the wrong diagnostic message string to be used when "Generic" is used with no type arguments.
    -   Enhancement: Added new diagnostic message for when "Generic" is used in contexts outside of a class definition statement.
    -   Bug Fix (from Pylance): Use `sys.version_info` to query interpreter version.
    -   Enhancement: Added heuristics to type var solver so it picks the "least complex" solution when considering the elements within a union.
    -   Enhancement: Updated typeshed stubs to the latest versions.
    -   Bug Fix: Fixed a bug that caused an error to be reported when a newline token was used within an f-string expression.
        ([pylance-release#200](https://github.com/microsoft/pylance-release/issues/200))
    -   Enhancement: Added new diagnostic rule "reportInvalidStubStatement" (on by default in strict mode, off otherwise) that reports diagnostics for statements that should not appear within a type stub file.
    -   Enhancement: Added diagnostic for a module-level `__getattr__` function defined in a type stub file when in strict mode.
    -   Bug Fix: Fixed bug that caused imports (and other symbols) to be reported as unaccessed if they were accessed from within code that was deemed to be unreachable (e.g. due to the current platform configuration).
    -   Behavior Change: Changed logic for reportUnusedClass and reportUnusedFunction diagnostic rules so they don't report private-named functions and classes within stub files.
    -   Bug Fix: The token "..." should mean an ellipsis object, not the ellipsis class, when used in a normal expression within a non-stub file.
    -   Enhancement (from Pylance): Add python.analysis.autoImportCompletions to control auto-import completions.
-   [1.1.59](https://github.com/microsoft/pyright/releases/tag/1.1.59)
    -   Bug Fix: Changed the inferred type of an async function to use `Coroutine` rather than `Awaitable` type. `Coroutine` is a subclass of `Awaitable` and is arguably more correct in this case.
        ([pylance-release#184](https://github.com/microsoft/pylance-release/issues/184))
    -   Bug Fix: Fixed a bug in the handling of position-only parameters with default values followed by named parameters or \*\*kwargs.
    -   Bug Fix: Fixed a bug where "yield from" argument was assumed to be an "Iterator", but it should really be an "Iterable".
    -   Bug Fix: Fixed bug where "from .A import A" statement caused symbol "A" to have an inferred type that was a union of a module and other type, even though the other type immediately overwrites the module.
        ([pylance-release#188](https://github.com/microsoft/pylance-release/issues/188))
    -   Behavior Change: Changed type stub generator to never generate parameter type annotations based purely on default value types since those can be incorrect or incomplete. Changed type stub generator to automatically add method return types for common magic methods whose return type is always the same.
    -   Behavior Change: Changed type stub generator to avoid emitting functions and methods that begin with an underscore.
    -   Enhancement: Changed type checker to flag unaccessed symbols within type stubs in some cases. It doesn't mark function parameters or variables as unaccessed, and it doesn't mark imports of the form "from x import y as z" or "import a as b" as unaccessed since those are intended to be re-exports.
    -   Enhancement: Changed type checker to treat "..." as an "Unknown" type when used as the RHS of an assignment statement such as "a = ...". This idiom appears sometimes within type stubs, and it should be treated as a missing (unknown) type so stub authors know that they need to fill in a type annotation.
    -   Enhancement: Improved the diagnostic message used to report parameter type mismatches when a parameter name isn't known.
    -   Bug Fix: Fixed a bug whereby a TypeVar in a source type could be conflated with a same-named TypeVar in a dest type when performing TypeVar matching.
    -   Bug Fix: On the Windows platform, avoid calling 'python3' to determine the import paths for the current interpreter. This command can sometimes display a dialog indicating that python isn't installed and can be downloaded from the store.

## 2020.7.4 (29 July 2020)

-   Fixed case where analysis progress spinner would not disappear after analysis was complete.
-   Improved active parameter bolding in signature help for functions with multiple overrides.

In addition, Pylance's copy of Pyright has been updated from 1.1.54 to 1.1.58, including the following changes:

-   [1.1.58](https://github.com/microsoft/pyright/releases/tag/1.1.58)
    -   Enhancement: Rework signature help to use new VS Code / LSP APIs. Function overrides and active parameters are handled much, much better.
    -   Enhancement: Added strict-mode check for declared return types in type stubs, which don't allow for return type inference.
    -   Bug Fix: Fixed bug in type checker that resulted in a crash when a function declaration referred to itself within its return type annotation.
        ([pylance-release#181](https://github.com/microsoft/pylance-release/issues/181))
    -   Bug Fix: Fixed bug that caused duplicate diagnostics to be reported for quoted type annotations in some cases.
    -   Bug Fix: Fixed bug that caused "find all references" and "replace symbol" to sometimes miss references to a symbol if they were within quoted type annotations or type comments.
    -   Bug Fix: Fixed bugs in a few of the "find all references" tests, which were not properly quoting a forward-declared symbol.
    -   Bug Fix: Fixed a bug that caused infinite recursion and a crash when printing the type of a function that refers to itself within its own return type annotation.
        ([pylance-release#181](https://github.com/microsoft/pylance-release/issues/181))
    -   Bug Fix: Fixed bug where an f-string expression generated an error if it ended in an equal sign followed by whitespace. The Python 3.8 spec doesn't indicate whether whitespace is allowed here, but clearly the interpreter accepts it.
        ([pylance-release#182](https://github.com/microsoft/pylance-release/issues/182))
    -   Bug Fix: Fixed bug in logic that handles chained comparisons (e.g. `a < b < c`). The code was not properly handling the case where the left expression was parenthesized (e.g. `(a < b) < c`).
    -   Enhancement: Improved bidirectional type inference in the case where the type and the expected type are generic but the expected type is a base class that has been specialized. For example, if the expected type is `Mapping[str, int]` and the type is a `dict`.
-   [1.1.57](https://github.com/microsoft/pyright/releases/tag/1.1.57)
    -   Bug Fix: Fixed bug that caused partial type stub creation (for subpackages of a top-level package) to be generated in the wrong directory.
    -   Change in Behavior: Changed logic within type evaluator to track differences between None and NoneType. Previously, they were treated interchangeably. This worked in most cases, but there are some edge cases where the difference is important.
    -   Change in Behavior: Changed logic that converts a type to text so it properly distinguishes between "None" and "NoneType". It previously always output "None".
    -   Enhancement: Added support for NoneType matching a type expression `Type[T]` during TypeVar matching.
    -   Bug Fix: Fixed the handling of class or instance variable declarations that redefine a same-named symbol in an outer scope but do not use a variable declaration statement within the class.
        ([pylance-release#175](https://github.com/microsoft/pylance-release/issues/175))
    -   Bug Fix: Updated type checker's logic for dealing with symbols that are declared in an inner scope and an outer scope but used within the inner scope prior to being redefined.
    -   Bug Fix: Fixed bug a homogeneous tuple of indeterminate length was indexed with a constant expression.
    -   Enhancement: Made the reportIncompatibleMethodOverride rule smarter. It now properly handles position-only parameters and allows a subclass to extend the signature of a method it is overriding as long as the parameters are \*varg, \*\*kwarg, or have default values.
        ([pylance-release#157](https://github.com/microsoft/pylance-release/issues/157))
    -   Enhancement: Augmented the reportIncompatibleMethodOverride diagnostic rule to check for cases where a non-function symbol within a subclass redefines a function symbol in a base class.
    -   New Feature: Added new diagnostic rule "reportIncompatibleVariableOverride" which is similar to "reportIncompatibleMethodOverride" except that it reports incompatible overrides of variables (non-methods).
-   [1.1.56](https://github.com/microsoft/pyright/releases/tag/1.1.56)
    -   Bug Fix: Fixed bug that caused the default python platform not to be specified if there was no config file and no python interpreter selected.
    -   Bug Fix: Fixed crash in type checker that occurs when removing NoReturn from a union and having no remaining types.
    -   Bug Fix: Fixed bug that caused `__name__` not to be flagged as an invalid attribute on a class instance.
        ([pylance-release#154](https://github.com/microsoft/pylance-release/issues/154))
    -   Bug Fix: Fixed bug that caused quoted type annotation (i.e. a forward reference) that contains type arguments to report an "unbound symbol".
    -   Enhancement: Improved CompletionItemKind for intrinsic class symbols like `__name__`, etc.
        ([pylance-release#154](https://github.com/microsoft/pylance-release/issues/154))
    -   Bug Fix: Fixed bug in parsing of unicode named character encodings within string literals when the encoding included capital letters.
        ([pylance-release#161](https://github.com/microsoft/pylance-release/issues/161))
    -   Bug Fix: Fixed bug whereby a non-function definition (such as an instance variable) within a subclass was not considered as having overridden an abstract method or property within a base class.
    -   Change in Behavior: Changed Never internal type to be assignable to any type. Previously, it was assignable to no type.
    -   Bug Fix: Fixed bug that caused a spurious error during TypeVar matching when the TypeVar is constrained and is initially matched against an Any or Unknown type but is later matched against a known type.
    -   Bug Fix: Fixed bug in dataclass logic that reported spurious error when initializing attribute with `field(init=False)`.
        ([pylance-release#162](https://github.com/microsoft/pylance-release/issues/162))
    -   Change in Behavior: Renamed ParameterSpecification to ParamSpec to reflect latest PEP 612 changes.
    -   Enhancement: Updated typeshed fallback stubs to latest version.
    -   Change in Behavior: Updated PEP 612 and 614 features to be dependent on 3.10 rather than 3.9.
    -   Bug Fix: Fixed bug that caused diagnostics to persist in files that are not part of the workspace even after they are closed.
    -   Bug Fix: Fixed bug that generated incorrect type checking error when type alias used a `Type[x]` type annotation.
-   [1.1.55](https://github.com/microsoft/pyright/releases/tag/1.1.55)
    -   Bug Fix: Changed logic for reportMissingModuleSource diagnostic rule so it isn't reported for stub files.
    -   Enhancement: Added support for typing.OrderedDict, which is a generic alias for collections.OrderedDict.
        ([pylance-release#151](https://github.com/microsoft/pylance-release/issues/151))
    -   Enhancement: Added support for new Python extension callback so Pyright extension is notified when pythonPath is modified.
    -   Bug Fix: Fixed bug in docstring trimming code that resulted in some docstrings (those consisting of two lines where the second line was empty) not appearing when hovering over functions.
    -   Bug Fix: Fixed bug in type checker that resulted in incorrect error when creating a generic type alias with a compatible TypeVar as one of the type arguments.
    -   Bug Fix: Fixed bug that caused value expressions for default parameter values in lambdas to be evaluated within the wrong scope resulting in errors if the lambda scope had a same-named symbol.
    -   Bug Fix: Fixed bugs in handling of wildcard imports. First, it was not properly handling the implicit introduction of symbol A in the statement `from .A import *`. Second, it was implicitly including submodules as part of the wildcard, and it shouldn't.
    -   Bug Fix: Fixed bug that resulted in incorrect error when using an unpack operator in an argument expression that corresponds to a \*varg parameter in the callee.
    -   Bug Fix: Fixed recent regression that caused `isinstance` check to emit a bad error when `self.__class__` was passed as a second argument.

## 2020.7.3 (21 July 2020)

-   Fixed typo in marketplace entry's readme.

In addition, Pylance's copy of Pyright has been updated from 1.1.53 to 1.1.54, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Enhancement: Changed logic for reportMissingModuleSource diagnostic rule so it isn't reported for stub files.
    -   Enhancement: Added support for typing.OrderedDict, which is a generic alias for collections.OrderedDict.
        ([pylance-release#151](https://github.com/microsoft/pylance-release/issues/151))
    -   Bug Fix: Fixed bug in docstring trimming code that resulted in some docstrings (those consisting of two lines where the second line was empty) not appearing when hovering over functions.
    -   Bug Fix: Fixed bug in type checker that resulted in incorrect error when creating a generic type alias with a compatible TypeVar as one of the type arguments.
    -   Bug Fix: Fixed bug that caused value expressions for default parameter values in lambdas to be evaluated within the wrong scope resulting in errors if the lambda scope had a same-named symbol.
-   [1.1.54](https://github.com/microsoft/pyright/releases/tag/1.1.54)
    -   Enhancement: Added json schema for mspythonconfig.json (in addition to pyrightconfig.json).
    -   Enhancement: Updated config file watcher logic so it can detect when a new config file is added to a workspace.
    -   Bug Fix: "Find all references" should not return references to a symbol within library code unless that library source file is currently open in the editor.
    -   Bug Fix: Fixed bug in type checker that caused a crash when analyzing an abstract class with a constructor that contained two or more parameters, all of which are unannotated.
        ([pylance-release#118](https://github.com/microsoft/pylance-release/issues/118))
    -   Bug Fix: Fixed pyrightconfig.json JSON schema to accept "information" as a valid diagnostic severity setting.
    -   Enhancement: Updated log levels for messages logged by the Pyright service. Some log levels were "info" but should have been "warning" or "error".
        ([pylance-release#120](https://github.com/microsoft/pylance-release/issues/120))
    -   Bug Fix: Fixed bug that caused incorrect type evaluation for \*args or \*\*kwargs parameters if no type annotation was present. This bug also affected completion suggestions for these parameters.
        ([pylance-release#119](https://github.com/microsoft/pylance-release/issues/119))
    -   Bug Fix: Fixed a bug that resulted in Pyright attempting to parse and analyze binaries (native libraries) like ".pyd" and ".so" files.
        ([pylance-release#124](https://github.com/microsoft/pylance-release/issues/124))
    -   Bug Fix: Fixed bug in argument/parameter matching when an unpack operator is used in the argument and the parameter is a \*varg type.
    -   Enhancement: Renamed setting "pyright.useLibraryCodeForTypes" to "python.analysis.useLibraryCodeForTypes" for compatibility with Pylance. The older setting name is still supported but will be removed in the future.
    -   Enhancement: Added code to handle the case where a class is assigned to a type described by a callable protocol object. In this case, the class constructor's signature should be compared against the `__call__` signature defined in the protocol.
    -   Bug Fix: Fixed bug in import resolver that caused imports that referred to local namespace packages not to resolve.
    -   Bug Fix: Fixed bug that caused enum names that were not uppercase to be handled incorrectly.
    -   Bug Fix: Fixed bug that caused incorrect type analysis when a package `__init__.py` imported and re-exported a symbol that matched the submodule it was being imported from, e.g. `from .foo import foo`.
    -   Bug Fix: Fixed bug in type analyzer where default value expressions for lambda parameters were not being evaluated. This meant that errors related to these expressions were not reported, and symbols referenced within them were marked as unreferenced.

## 2020.7.2 (15 July 2020)

-   Allow find all references to search libraries if invoked from non-user files.

In addition, Pylance's copy of Pyright has been updated from 1.1.51 to 1.1.53, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Bug Fix: Updated config file watcher logic so it can detect when a new config file is added to a workspace.
-   [1.1.53](https://github.com/microsoft/pyright/releases/tag/1.1.53)
    -   Bug Fix: Fixed bug in parser where it was emitting a spurious error about function return type annotations being a tuple when it was simply enclosed in parentheses.
    -   Bug Fix: Fixed a bug that caused completion suggestions not to work for the LHS of a member access expression (e.g. the "a" in "a.b").
    -   Bug Fix: Fixed diagnostic message for "partially unknown" types (used in strict mode). It was incorrectly using the "unknown" message rather than "partially unknown", which could lead to confusion.
    -   Enhancement: Changed type printing logic to emit "Unknown" annotations when in strict mode to make it clearer to the user which part of the type is unknown.
    -   Bug Fix: Fixed bug that caused extension to report empty diagnostics for all tracked files when unnecessary (in particular, when the diagnostic mode is set to openFilesOnly and the file is not open).
    -   Enhancement: Added partial support for mypy-supported variant of "# type: ignore" comment where specific error codes in square brackets after the "ignore". Pyright doesn't honor the specific error codes but now treats it as a normal # type: ignore" comment.
        ([pylance-release#108](https://github.com/microsoft/pylance-release/issues/108))
    -   Bug Fix: Fixed bug that caused the arguments of a call to remain unanalyzed if the LHS of the call was not callable. This resulted in omitted errors and spurious unreferenced symbols.
    -   Bug Fix: Changed diagnostic for second argument to "Enum" call to be dependent on the reportGenalTypeIssues diagnostic rule rather than unconditional.
    -   Bug Fix: Fixed recent regression relating to "isinstance" type narrowing when the type of the target is a constrained TypeVar.
    -   Bug Fix: Fixed bug in the handling of the NewType function introduced in PEP 484. The previous code was not synthesizing a constructor (`__init__` method) as specified in the PEP.
    -   Enhancement: Changed fallback mechanism for detecting the configured python interpreter to use the shell command "python3" first and then "python" if that fails. This is preferable on Linux and MacOS because "python" typically points to a Python 2.7 interpreter.
    -   Enhancement: Added parser error for relative imports of the form "import .abc". This is treated as a syntax error by the Python interpreter and should be flagged as such.
    -   Bug Fix: Fixed bug with "from . import a" form of import. Diagnostic was not logged when "a" could not be resolved.
-   [1.1.52](https://github.com/microsoft/pyright/releases/tag/1.1.52)
    -   Bug Fix: Fixed escaping of literal strings when printing Literal string types.
    -   Enhancement: Improved completion suggestions related to member access expressions (e.g. obj.method) by binding the method to the object when appropriate.
    -   Enhancement: When hovering over class name that is used in a constructor call, display the `__init__` method signature rather than the class.
    -   Bug Fix: Fixed recent regression in unreachable code reporting at the module level.
        ([pylance-release#107](https://github.com/microsoft/pylance-release/issues/107))
    -   Bug Fix: Removed error message for unexpected dynamic argument types to `type` initializer.
        ([pylance-release#114](https://github.com/microsoft/pylance-release/issues/114))
    -   Bug Fix: Fixed a bug in the code that validates an exception type in an "except" clause. It was not properly handling the case where the type of the exception was specified as a `Type[X]` object.
    -   Bug Fix: Reverted part of a previous change where constrained type vars were specialized as a union of the constrained types. Changed logic to use first constrained type only.
    -   Bug Fix: Fixed bug in logic that detects assignment compatibility for function types. It wasn't properly handling generic parameters, including synthesized TypeVar types used for "self" parameters.
    -   Bug Fix: Added diagnostic for TypeVar or generic class with type args being used as a second argument for isinstance or issubclass. These will raise a TypeError exception at runtime.
    -   Enhancement: Changed Pyright import resolution order to match that described in PEP 561. In particular, stubs in stubPath are now searched prior to user code, and third-party typeshed stubs are searched only after installed packages are searched for stub packages and inline stubs. There is one place where Pyright's import resolution still differs from a strict interpretation of PEP 561: it searches stdlib typeshed stubs first (unless typeshedPath is defined, in which case it searches there). This is more consistent with the way the Python interpreter resolves stdlib types.
    -   Bug Fix: Fixed bug in handling of constructor that uses a specialized class (e.g. `MyClass[int]()`). The previous code was inappropriate overriding the provided type arguments as part of bidirectional inference logic.
    -   Bug Fix: Fixed bug that caused spurious errors when assigning a specialized object/class to a variable whose type is a specialized base class of the specialized object/class.

## 2020.7.1 (10 July 2020)

-   Fixed background analysis thread, which prevented diagnostics (syntax checks, import warnings, etc) from working.
    ([pylance-release#86](https://github.com/microsoft/pylance-release/issues/86))
-   Fixed setting and survey banners blocking startup.

## 2020.7.0 (9 July 2020)

-   Hovers for class invocations will now show the `__init__` method's docstring.
-   Import organization has been disabled to prevent conflicts with the Python extension's import sorting.
    ([pylance-release#23](https://github.com/microsoft/pylance-release/issues/23))
-   Docstrings for bound methods will no longer show `self` in the signature.
-   Fixed multi-line string literals in tooltips.
-   IntelliCode now operates in environments without OpenMP.
-   The `pandas` stubs have been improved.
    ([pylance-release#13](https://github.com/microsoft/pylance-release/issues/13), [pylance-release#71](https://github.com/microsoft/pylance-release/issues/73), [pylance-release#73](https://github.com/microsoft/pylance-release/issues/71))
-   `pyplot.subplots`'s signature has been fixed.
    ([pylance-release#43](https://github.com/microsoft/pylance-release/issues/43))
-   The bundled copy of typeshed has been updated.
-   The overall startup time and responsiveness has been improved.

In addition, Pylance's copy of Pyright has been updated from 1.1.46 to 1.1.51, including the following changes:

-   Unreleased in Pyright, but included in Pylance:
    -   Bug Fix: Fixed recent regression in unreachable code reporting at the module level.
    -   Enhancement: Removed error message for unexpected dynamic argument types to `type` initializer.
-   [1.1.51](https://github.com/microsoft/pyright/releases/tag/1.1.51)
    -   New Feature: Added document highlight provider. When you click on a symbol in the editor, all other symbols within the same file that have the same name and have the same semantic meaning are also highlighted.
        ([pylance-release#42](https://github.com/microsoft/pylance-release/issues/42))
    -   Enhancement: If reportGeneralTypeIssues rule is disabled, don't replace assigned type with declared type because it will lead to additional errors that will confuse users.
        Enhancement: Added type narrowing support for "in" operator when RHS is a specialized list, set, frozenset, or deque.
    -   Enhancement: Added logic to validate that RHS operand used with "in" and "not in" operators support the `__contains__` magic method.
    -   Bug Fix: Fixed bug where "field" initialization of dataclass member didn't take into account "default" or "default_factory" parameters when determining whether the field had a default value.
    -   Bug Fix: Added code to deal with the special case where a method declared with a "def" statement is later overwritten with a callable instance variable.
    -   Bug Fix: Fixed bug whereby a TypeVar type was not treated the same when it was alone versus within a union leading to some subtle differences in error reporting. Also changed specialization of constrained TypeVars to be a union of constrained types rather than Unknown if the TypeVar is not used as a type argument.
    -   Bug Fix: Fixed bug in diagnostic message for constrained TypeVar type mismatch. The wrong type was being printed leading to confusing errors.
    -   Bug Fix: Fixed a bug that caused incorrect linearization of classes during MRO calculation.
    -   Bug Fix: Fixed bug in synthesized version of `get` method for `TypedDict` class. It should provide an overload that allows for any str key and return an "Unknown" type.
-   [1.1.50](https://github.com/microsoft/pyright/releases/tag/1.1.50)
    -   Bug Fix: Fixed regression in completion provider when retrieving suggestions for "self.". Added test to cover this case.
        ([pylance-release#53](https://github.com/microsoft/pylance-release/issues/53))
    -   Enhancement: Changed "x is not iterable" diagnostic to be part of the "reportGeneralTypeIssues" rule so it doesn't get reported if typeCheckingMode is "off".
        ([pylance-release#59](https://github.com/microsoft/pylance-release/issues/59))
    -   Bug Fix: Fixed bug that caused incorrect behavior when a symbol was imported multiple times in the same file.
    -   Bug Fix: Fixed bug that caused Callable instance variables to be treated as though they needed to be "bound" to the object at the time they were accessed. This resulted in spurious errors about parameter count because an implicit "self" parameter was assumed.
    -   Enhancement: Improved type analysis performance by 5-10% on typical code and by significantly more on certain code sequences that involve many if statements within a loop. This optimization uses code flow caching to determine when incomplete types (those that haven't been fully resolved) are potentially stale.
        ([pylance-release#57](https://github.com/microsoft/pylance-release/issues/57))
    -   Bug Fix: Fixed recent regression related to imports of the form "from .x import y" within an `__init__.py(i)` file.
    -   Enhancement: Changed type analyzer to use module-level `__getattr__` for types only if the file is a stub.
    -   Enhancement: Added code to prevent "variable possibly unbound" error from propagating to other variables. It should be reported only once.
    -   Enhancement: Switched "pyright.typeCheckingMode" to "python.analysis.typeCheckingMode" for compatibility with Pylance.
    -   Enhancement: Moved a few parameter-related diagnostics to the "reportGeneralTypeIssues" diagnostic rule rather than being unconditional errors.
        ([pylance-release#15](https://github.com/microsoft/pylance-release/issues/15), [pylance-release#39](https://github.com/microsoft/pylance-release/issues/39), [pylance-release#54](https://github.com/microsoft/pylance-release/issues/54))
    -   Bug Fix: Fixed bug that resulted in incorrect type inference for a member variable that is not assigned within a class but is assigned within an ancestor class.
    -   Enhancement: Added type narrowing support for "is" and "is not" operator where RHS is an enum literal value.
-   [1.1.49](https://github.com/microsoft/pyright/releases/tag/1.1.49)
    -   Bug Fix: Fixed bug that caused incorrect type to be determined for \*args and \*\*kwargs parameters in some contexts.
        ([pylance-release#20](https://github.com/microsoft/pylance-release/issues/20))
    -   Enhancement: Updated typeshed stubs to the latest versions from the typeshed repo.
    -   Bug Fix: Fixed bug in tokenizer where it was generating an error if escaped unicode characters (using the \N{name} escape) contained a space in the name.
        ([pylance-release#25](https://github.com/microsoft/pylance-release/issues/25))
    -   Enhancement: Improved parse recovery for statements that are supposed to end in a colon followed by a suite of other indented statements. Previously, a missing colon or expression error resulted in a cascade of additional errors.
        ([pylance-release#22](https://github.com/microsoft/pylance-release/issues/22))
    -   Enhancement: Improved error message for overloaded calls where no overload matches the provided arguments.
    -   Bug Fix: Fixed bug in unreachable code detection and reporting. The logic was previously split between the binder (which used proper code flow analysis) and the checker (which didn't use code flow analysis but had access to NoReturn - call information). The new code combines everything into the checker and uses both code flow analysis and NoReturn call info.
        ([pylance-release#31](https://github.com/microsoft/pylance-release/issues/31))
    -   Bug Fix: Added code to include a symbol in a module if the source file is an `__init__.py(i)` and a relative import of the form "from .x.y.z import X" is used. In this case, the symbol "x" should appear within the module's namespace.
    -   Bug Fix: Fixed bug in pyrightconfig schema. The defaults for several settings were using strings "true" and "false" rather than booleans true and false.
    -   Bug Fix: Fixed bug in parser that generated a spurious error when an unparenthesized assignment expression (walrus operator) was used as an argument. PEP 572 indicates that this should be allowed in cases where the argument is not named.
    -   Enhancement: Changed constructor type analysis logic to always specialize the instantiated instance.
    -   Bug Fix: Fixed bug in reportAssertAlwaysTrue diagnostic. It wasn't properly handling tuples of indeterminate length.
    -   Bug Fix: Fixed bug in import resolution that resulted in an unresolved import when a local folder was present with the same name as the imported third-party library.
    -   Bug Fix: Fixed bug that caused diagnostics for unopened files to remain in "problems" panel after switching diagnostic mode from "workspace" to "open files only".
    -   Bug Fix: Fixed bug in parsing of f-string expressions that contain nested braces.
        ([pylance-release#45](https://github.com/microsoft/pylance-release/issues/45))
    -   Bug Fix: Fixed bug in import resolver where it was not preferring regular package imports over namespace packages.
        ([pylance-release#52](https://github.com/microsoft/pylance-release/issues/52))
-   [1.1.48](https://github.com/microsoft/pyright/releases/tag/1.1.48)
    -   Enhancement: Added support for accessing metaclass members from class. This allows, for example, access to the `__members__` attribute of an Enum class.
    -   Enhancement: Added type completion support for class attributes provided by a metaclass.
    -   Bug Fix: Fixed bug that caused unbound variables to go unreported if they had type annotations.
    -   Bug Fix: Fixed bug in type narrowing logic for isinstance call. It wasn't properly handling bound TypeVar types. This includes synthesized bound TypeVars like those used for unannotated "self" and "cls" parameters.
    -   Bug Fix: Fixed bug that caused stand-alone expression statements (those that are not included in other statements) to go unchecked, resulting in symbols potentially unreferenced and type errors unreported.
    -   Bug Fix: Fixed bug where the use of unpack operator within a tuple not surrounded by parens within a return/yield statement incorrectly reported an error when used with Python <3.8.
    -   Bug Fix: Changed signature help provider to use the `__init__` method signature (if available) for class construction expressions. It previously used the `__new__` method signature by default.
    -   Enhancement: Unaccessed function parameters are now displayed as "grayed out" in VS Code. There was previously code in place to do this, but it contained a bug that went unnoticed.
-   [1.1.47](https://github.com/microsoft/pyright/releases/tag/1.1.47)
    -   Enhancement: Improved support for type aliases, especially those with generic parameters. Type alias names are now tracked and used within printed type names.
    -   Bug Fix: Fixed recent regression in CLI that resulted in unintended verbose logging output.
    -   Bug Fix: Added minimum node version to package.json to prevent installation of pyright CLI on incompatible versions of node.
    -   Enhancement: Added code to better handle the obsolete "<>" operator from Python 2 - including a better error message and better parse recovery.
    -   Enhancement: Added special-case handling of 'NoReturn' type to allow Never type to be assigned to it. This can be used to verify exhaustive type narrowing.
    -   Bug Fix: Added code to differentiate between Protocol symbol in typing.pyi versus typing_extensions.pyi. The latter can be used on older versions of Python.
    -   Enhancement: Changed activation events to remove glob path for pyrightconfig.json, which speeds up extension activation on large projects. Added support for mspythonconfig.json

## 2020.6.1 (30 June 2020)

Initial release!
