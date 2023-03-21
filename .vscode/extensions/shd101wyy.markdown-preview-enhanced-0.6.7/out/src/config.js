"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.MarkdownPreviewEnhancedConfig = void 0;
const vscode = require("vscode");
const path_resolver_1 = require("./utils/path-resolver");
class MarkdownPreviewEnhancedConfig {
    static getCurrentConfig() {
        return new MarkdownPreviewEnhancedConfig();
    }
    constructor() {
        const config = vscode.workspace.getConfiguration("markdown-preview-enhanced");
        this.configPath = (config.get("configPath") || "").trim();
        this.configPath = path_resolver_1.PathResolver.resolvePath(this.configPath);
        this.usePandocParser = config.get("usePandocParser");
        this.breakOnSingleNewLine = config.get("breakOnSingleNewLine");
        this.enableTypographer = config.get("enableTypographer");
        this.enableWikiLinkSyntax = config.get("enableWikiLinkSyntax");
        this.enableLinkify = config.get("enableLinkify");
        this.useGitHubStylePipedLink = config.get("useGitHubStylePipedLink");
        this.wikiLinkFileExtension = config.get("wikiLinkFileExtension");
        this.enableEmojiSyntax = config.get("enableEmojiSyntax");
        this.enableExtendedTableSyntax = config.get("enableExtendedTableSyntax");
        this.enableCriticMarkupSyntax = config.get("enableCriticMarkupSyntax");
        this.frontMatterRenderingOption = config.get("frontMatterRenderingOption");
        this.mermaidTheme = config.get("mermaidTheme");
        this.mathRenderingOption = config.get("mathRenderingOption");
        this.mathInlineDelimiters = config.get("mathInlineDelimiters");
        this.mathBlockDelimiters = config.get("mathBlockDelimiters");
        this.mathRenderingOnlineService = config.get("mathRenderingOnlineService");
        this.codeBlockTheme = config.get("codeBlockTheme");
        this.previewTheme = config.get("previewTheme");
        this.revealjsTheme = config.get("revealjsTheme");
        this.protocolsWhiteList = config.get("protocolsWhiteList");
        this.imageFolderPath = config.get("imageFolderPath");
        this.imageUploader = config.get("imageUploader");
        this.printBackground = config.get("printBackground");
        this.chromePath = config.get("chromePath");
        this.imageMagickPath = config.get("imageMagickPath");
        this.pandocPath = config.get("pandocPath");
        this.pandocMarkdownFlavor = config.get("pandocMarkdownFlavor");
        this.pandocArguments = config.get("pandocArguments");
        this.latexEngine = config.get("latexEngine");
        this.enableScriptExecution = config.get("enableScriptExecution");
        this.scrollSync = config.get("scrollSync");
        this.liveUpdate = config.get("liveUpdate");
        this.singlePreview = config.get("singlePreview");
        this.automaticallyShowPreviewOfMarkdownBeingEdited = config.get("automaticallyShowPreviewOfMarkdownBeingEdited");
        this.enableHTML5Embed = config.get("enableHTML5Embed");
        this.HTML5EmbedUseImageSyntax = config.get("HTML5EmbedUseImageSyntax");
        this.HTML5EmbedUseLinkSyntax = config.get("HTML5EmbedUseLinkSyntax");
        this.HTML5EmbedIsAllowedHttp = config.get("HTML5EmbedIsAllowedHttp");
        this.HTML5EmbedAudioAttributes = config.get("HTML5EmbedAudioAttributes");
        this.HTML5EmbedVideoAttributes = config.get("HTML5EmbedVideoAttributes");
        this.puppeteerWaitForTimeout = config.get("puppeteerWaitForTimeout");
        this.usePuppeteerCore = config.get("usePuppeteerCore");
        this.puppeteerArgs = config.get("puppeteerArgs");
        this.plantumlServer = config.get("plantumlServer");
        this.hideDefaultVSCodeMarkdownPreviewButtons = config.get("hideDefaultVSCodeMarkdownPreviewButtons");
    }
    isEqualTo(otherConfig) {
        const json1 = JSON.stringify(this);
        const json2 = JSON.stringify(otherConfig);
        return json1 === json2;
    }
}
exports.MarkdownPreviewEnhancedConfig = MarkdownPreviewEnhancedConfig;
//# sourceMappingURL=config.js.map