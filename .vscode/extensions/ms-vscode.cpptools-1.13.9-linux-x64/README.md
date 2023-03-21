# C/C++ for Visual Studio Code

#### [Repository](https://github.com/microsoft/vscode-cpptools)&nbsp;&nbsp;|&nbsp;&nbsp;[Issues](https://github.com/microsoft/vscode-cpptools/issues)&nbsp;&nbsp;|&nbsp;&nbsp;[Documentation](https://code.visualstudio.com/docs/languages/cpp)&nbsp;&nbsp;|&nbsp;&nbsp;[Code Samples](https://github.com/microsoft/vscode-cpptools/tree/main/Code%20Samples)

[![Badge](https://aka.ms/vsls-badge)](https://aka.ms/vsls)

The C/C++ extension adds language support for C/C++ to Visual Studio Code, including [editing (IntelliSense)](https://code.visualstudio.com/docs/cpp/cpp-ide) and [debugging](https://code.visualstudio.com/docs/cpp/cpp-debug) features.

## Pre-requisites
C++ is a compiled language meaning your program's source code must be translated (compiled) before it can be run on your computer. VS Code is first and foremost an editor, and relies on command-line tools to do much of the development workflow. The C/C++ extension **does not include a C++ compiler or debugger**. You will need to install these tools or use those already installed on your computer.
 * C++ compiler pre-installed
 * C++ debugger pre-installed

<br/>

Here is a list of compilers and architectures per platform officially supported by the extension. These are reflected by the available [IntelliSense modes](https://code.visualstudio.com/docs/cpp/configure-intellisense-crosscompilation#_intellisense-mode) from the extension's IntelliSense configuration. Note that support for other compilers may be limited.

Platform | Compilers | Architectures
:--- | :--- | :--- 
Windows | MSVC, Clang, GCC | x64, x86, arm64, arm
Linux | Clang, GCC | x64, x86, arm64, arm
macOS | Clang, GCC | x64, x86, arm64

For more information about installing the required tools or setting up the extension, please follow the tutorials below.
<br/>
<br/>

## Overview and tutorials
* [C/C++ extension overview](https://code.visualstudio.com/docs/languages/cpp)
* [Introductory Videos](https://code.visualstudio.com/docs/cpp/introvideos-cpp)

C/C++ extension tutorials per compiler and platform
* [Microsoft C++ compiler (MSVC) on Windows](https://code.visualstudio.com/docs/cpp/config-msvc)
* [GCC and Mingw-w64 on Windows](https://code.visualstudio.com/docs/cpp/config-mingw)
* [GCC on Windows Subsystem for Linux (WSL)](https://code.visualstudio.com/docs/cpp/config-wsl)
* [GCC on Linux](https://code.visualstudio.com/docs/cpp/config-linux)
* [Clang on macOS](https://code.visualstudio.com/docs/cpp/config-clang-mac)

## Quick links
* [Editing features (IntelliSense)](https://code.visualstudio.com/docs/cpp/cpp-ide)
* [IntelliSense configuration](https://code.visualstudio.com/docs/cpp/customize-default-settings-cpp)
* [Enhanced colorization](https://code.visualstudio.com/docs/cpp/colorization-cpp)
* [Debugging](https://code.visualstudio.com/docs/cpp/cpp-debug)
* [Debug configuration](https://code.visualstudio.com/docs/cpp/launch-json-reference)
* [Enable logging for IntelliSense or debugging](https://code.visualstudio.com/docs/cpp/enable-logging-cpp)

## Questions and feedback

**[FAQs](https://code.visualstudio.com/docs/cpp/faq-cpp)**
<br>
Check out the FAQs before filing a question.
<br>

**[Provide feedback](https://github.com/microsoft/vscode-cpptools/issues/new/choose)**
<br>
File questions, issues, or feature requests for the extension.
<br>

**[Known issues](https://github.com/Microsoft/vscode-cpptools/issues)**
<br>
If someone has already filed an issue that encompasses your feedback, please leave a 👍 or 👎 reaction on the issue to upvote or downvote it to help us prioritize the issue.
<br>

**[Quick survey](https://www.research.net/r/VBVV6C6)**
<br>
Let us know what you think of the extension by taking the quick survey.

## Contribution

Contributions are always welcome. Please see our [contributing guide](https://github.com/Microsoft/vscode-cpptools/blob/HEAD/CONTRIBUTING.md) for more details.

## Microsoft Open Source Code of Conduct

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact opencode@microsoft.com with any additional questions or comments.

## Data and telemetry

This extension collects usage data and sends it to Microsoft to help improve our products and services. Collection of telemetry is controlled via the same setting provided by Visual Studio Code: `"telemetry.enableTelemetry"`. Read our [privacy statement](https://privacy.microsoft.com/en-us/privacystatement) to learn more.
