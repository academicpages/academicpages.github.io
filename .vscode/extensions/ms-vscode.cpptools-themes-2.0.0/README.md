# C/C++ Extension UI Themes

[Semantic colorization was added to the C/C++ Extension in version 0.24.0](https://devblogs.microsoft.com/cppblog/visual-studio-code-c-c-extension-july-2019-update/). At the time, colorization in VS Code was purely syntactic/lexical and leveraged TextMate grammar to associate named 'scopes' with syntactic elements. Themes and settings can be used to associate colors with these scopes. Our original implementation of semantic colorization leveraged the same system of associating colors with named scopes. But, some tokens that can be colored by semantic colorization in C/C++ did not have existing analogs in VS Code's TextMate grammar. So, new named scopes are required. Because these scopes were new, existing themes did not include colors for them either.

We created C/C++ Extension UI Themes to closely match Visual Studio themes and include colors for many of the new scopes. The old themes from Visual Studio 2017 can be found alongside new themes that more closely resemble the Enhanced themes from more recent versions of Visual Studio.

VS Code has since provided an API for semantic colorization. The C/C++ Extension has transitioned from its own implementation to this new API. These themes now include colors for some of the new semantic token scopes.

## Example

Light Theme

![Light Theme 2019 example](https://github.com/Microsoft/vscode-cpptools/raw/HEAD/Themes/assets/light.png)

Dark Theme

![Dark Theme 2019 example](https://github.com/Microsoft/vscode-cpptools/raw/HEAD/Themes/assets/dark.png)

2017 Light Theme

![2017 Light Theme example](https://github.com/Microsoft/vscode-cpptools/raw/HEAD/Themes/assets/light2017.png)

2017 Dark Theme

![2017 Dark Theme example](https://github.com/Microsoft/vscode-cpptools/raw/HEAD/Themes/assets/dark2017.png)

## Contributing

This project welcomes contributions and suggestions. Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
