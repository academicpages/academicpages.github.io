/* --------------------------------------------------------------------------------------------
 * Copyright (c) Microsoft Corporation. All Rights Reserved.
 * See 'LICENSE' in the project root for license information.
 * ------------------------------------------------------------------------------------------ */
'use strict';
var elementId = {
    // Basic settings
    configName: "configName",
    configNameInvalid: "configNameInvalid",
    configSelection: "configSelection",
    addConfigDiv: "addConfigDiv",
    addConfigBtn: "addConfigBtn",
    addConfigInputDiv: "addConfigInputDiv",
    addConfigOk: "addConfigOk",
    addConfigCancel: "addConfigCancel",
    addConfigName: "addConfigName",
    compilerPath: "compilerPath",
    compilerPathInvalid: "compilerPathInvalid",
    knownCompilers: "knownCompilers",
    noCompilerPathsDetected: "noCompilerPathsDetected",
    compilerArgs: "compilerArgs",
    intelliSenseMode: "intelliSenseMode",
    intelliSenseModeInvalid: "intelliSenseModeInvalid",
    includePath: "includePath",
    includePathInvalid: "includePathInvalid",
    defines: "defines",
    cStandard: "cStandard",
    cppStandard: "cppStandard",
    // Advanced settings
    windowsSdkVersion: "windowsSdkVersion",
    macFrameworkPath: "macFrameworkPath",
    macFrameworkPathInvalid: "macFrameworkPathInvalid",
    compileCommands: "compileCommands",
    compileCommandsInvalid: "compileCommandsInvalid",
    configurationProvider: "configurationProvider",
    forcedInclude: "forcedInclude",
    forcedIncludeInvalid: "forcedIncludeInvalid",
    mergeConfigurations: "mergeConfigurations",
    dotConfig: "dotConfig",
    dotConfigInvalid: "dotConfigInvalid",
    // Browse properties
    browsePath: "browsePath",
    browsePathInvalid: "browsePathInvalid",
    limitSymbolsToIncludedHeaders: "limitSymbolsToIncludedHeaders",
    databaseFilename: "databaseFilename",
    databaseFilenameInvalid: "databaseFilenameInvalid",
    // Other
    showAdvanced: "showAdvanced",
    advancedSection: "advancedSection"
};
var SettingsApp = /** @class */ (function () {
    function SettingsApp() {
        this.updating = false;
        this.vsCodeApi = acquireVsCodeApi();
        window.addEventListener("keydown", this.onTabKeyDown.bind(this));
        window.addEventListener("message", this.onMessageReceived.bind(this));
        // Add event listeners to UI elements
        this.addEventsToConfigNameChanges();
        this.addEventsToInputValues();
        document.getElementById(elementId.knownCompilers).addEventListener("change", this.onKnownCompilerSelect.bind(this));
        // Set view state of advanced settings and add event
        var oldState = this.vsCodeApi.getState();
        var advancedShown = (oldState && oldState.advancedShown);
        document.getElementById(elementId.advancedSection).style.display = advancedShown ? "block" : "none";
        document.getElementById(elementId.showAdvanced).classList.toggle(advancedShown ? "collapse" : "expand", true);
        document.getElementById(elementId.showAdvanced).addEventListener("click", this.onShowAdvanced.bind(this));
        this.vsCodeApi.postMessage({
            command: "initialized"
        });
    }
    SettingsApp.prototype.addEventsToInputValues = function () {
        var _this = this;
        var elements = document.getElementsByName("inputValue");
        elements.forEach(function (el) {
            el.addEventListener("change", _this.onChanged.bind(_this, el.id));
        });
        // Special case for checkbox elements
        document.getElementById(elementId.limitSymbolsToIncludedHeaders).addEventListener("change", this.onChangedCheckbox.bind(this, elementId.limitSymbolsToIncludedHeaders));
        document.getElementById(elementId.mergeConfigurations).addEventListener("change", this.onChangedCheckbox.bind(this, elementId.mergeConfigurations));
    };
    SettingsApp.prototype.addEventsToConfigNameChanges = function () {
        document.getElementById(elementId.configName).addEventListener("change", this.onConfigNameChanged.bind(this));
        document.getElementById(elementId.configSelection).addEventListener("change", this.onConfigSelect.bind(this));
        document.getElementById(elementId.addConfigBtn).addEventListener("click", this.onAddConfigBtn.bind(this));
        document.getElementById(elementId.addConfigOk).addEventListener("click", this.OnAddConfigConfirm.bind(this, true));
        document.getElementById(elementId.addConfigCancel).addEventListener("click", this.OnAddConfigConfirm.bind(this, false));
    };
    SettingsApp.prototype.onTabKeyDown = function (e) {
        if (e.keyCode === 9) {
            document.body.classList.add("tabbing");
            window.removeEventListener("keydown", this.onTabKeyDown);
            window.addEventListener("mousedown", this.onMouseDown.bind(this));
        }
    };
    SettingsApp.prototype.onMouseDown = function () {
        document.body.classList.remove("tabbing");
        window.removeEventListener("mousedown", this.onMouseDown);
        window.addEventListener("keydown", this.onTabKeyDown.bind(this));
    };
    SettingsApp.prototype.onShowAdvanced = function () {
        var isShown = (document.getElementById(elementId.advancedSection).style.display === "block");
        document.getElementById(elementId.advancedSection).style.display = isShown ? "none" : "block";
        // Save view state
        this.vsCodeApi.setState({ advancedShown: !isShown });
        // Update chevron on button
        var element = document.getElementById(elementId.showAdvanced);
        element.classList.toggle("collapse");
        element.classList.toggle("expand");
    };
    SettingsApp.prototype.onAddConfigBtn = function () {
        this.showElement(elementId.addConfigDiv, false);
        this.showElement(elementId.addConfigInputDiv, true);
    };
    SettingsApp.prototype.OnAddConfigConfirm = function (request) {
        this.showElement(elementId.addConfigInputDiv, false);
        this.showElement(elementId.addConfigDiv, true);
        // If request is yes, send message to create new config
        if (request) {
            var el = document.getElementById(elementId.addConfigName);
            if (el.value !== undefined && el.value !== "") {
                this.vsCodeApi.postMessage({
                    command: "addConfig",
                    name: el.value
                });
                el.value = "";
            }
        }
    };
    SettingsApp.prototype.onConfigNameChanged = function () {
        if (this.updating) {
            return;
        }
        var configName = document.getElementById(elementId.configName);
        var list = document.getElementById(elementId.configSelection);
        if (configName.value === "") {
            document.getElementById(elementId.configName).value = list.options[list.selectedIndex].value;
            return;
        }
        // Update name on selection
        list.options[list.selectedIndex].value = configName.value;
        list.options[list.selectedIndex].text = configName.value;
        this.onChanged(elementId.configName);
    };
    SettingsApp.prototype.onConfigSelect = function () {
        if (this.updating) {
            return;
        }
        var el = document.getElementById(elementId.configSelection);
        document.getElementById(elementId.configName).value = el.value;
        this.vsCodeApi.postMessage({
            command: "configSelect",
            index: el.selectedIndex
        });
    };
    SettingsApp.prototype.onKnownCompilerSelect = function () {
        if (this.updating) {
            return;
        }
        var el = document.getElementById(elementId.knownCompilers);
        document.getElementById(elementId.compilerPath).value = el.value;
        this.onChanged(elementId.compilerPath);
        // Post message that this control was used for telemetry
        this.vsCodeApi.postMessage({
            command: "knownCompilerSelect"
        });
        // Reset selection to none
        el.value = "";
    };
    SettingsApp.prototype.onChangedCheckbox = function (id) {
        if (this.updating) {
            return;
        }
        var el = document.getElementById(id);
        this.vsCodeApi.postMessage({
            command: "change",
            key: id,
            value: el.checked
        });
    };
    SettingsApp.prototype.onChanged = function (id) {
        if (this.updating) {
            return;
        }
        var el = document.getElementById(id);
        this.vsCodeApi.postMessage({
            command: "change",
            key: id,
            value: el.value
        });
    };
    SettingsApp.prototype.onMessageReceived = function (e) {
        var message = e.data; // The json data that the extension sent
        switch (message.command) {
            case 'updateConfig':
                this.updateConfig(message.config);
                break;
            case 'updateErrors':
                this.updateErrors(message.errors);
                break;
            case 'setKnownCompilers':
                this.setKnownCompilers(message.compilers);
                break;
            case 'updateConfigSelection':
                this.updateConfigSelection(message);
                break;
        }
    };
    SettingsApp.prototype.updateConfig = function (config) {
        this.updating = true;
        try {
            var joinEntries = function (input) { return (input && input.length) ? input.join("\n") : ""; };
            // Basic settings
            document.getElementById(elementId.configName).value = config.name;
            document.getElementById(elementId.compilerPath).value = config.compilerPath ? config.compilerPath : "";
            document.getElementById(elementId.compilerArgs).value = joinEntries(config.compilerArgs);
            document.getElementById(elementId.intelliSenseMode).value = config.intelliSenseMode ? config.intelliSenseMode : "${default}";
            document.getElementById(elementId.includePath).value = joinEntries(config.includePath);
            document.getElementById(elementId.defines).value = joinEntries(config.defines);
            document.getElementById(elementId.cStandard).value = config.cStandard;
            document.getElementById(elementId.cppStandard).value = config.cppStandard;
            // Advanced settings
            document.getElementById(elementId.windowsSdkVersion).value = config.windowsSdkVersion ? config.windowsSdkVersion : "";
            document.getElementById(elementId.macFrameworkPath).value = joinEntries(config.macFrameworkPath);
            document.getElementById(elementId.compileCommands).value = config.compileCommands ? config.compileCommands : "";
            document.getElementById(elementId.mergeConfigurations).checked = config.mergeConfigurations;
            document.getElementById(elementId.configurationProvider).value = config.configurationProvider ? config.configurationProvider : "";
            document.getElementById(elementId.forcedInclude).value = joinEntries(config.forcedInclude);
            document.getElementById(elementId.dotConfig).value = config.dotConfig ? config.dotConfig : "";
            if (config.browse) {
                document.getElementById(elementId.browsePath).value = joinEntries(config.browse.path);
                document.getElementById(elementId.limitSymbolsToIncludedHeaders).checked =
                    (config.browse.limitSymbolsToIncludedHeaders && config.browse.limitSymbolsToIncludedHeaders);
                document.getElementById(elementId.databaseFilename).value = config.browse.databaseFilename ? config.browse.databaseFilename : "";
            }
            else {
                document.getElementById(elementId.browsePath).value = "";
                document.getElementById(elementId.limitSymbolsToIncludedHeaders).checked = false;
                document.getElementById(elementId.databaseFilename).value = "";
            }
        }
        finally {
            this.updating = false;
        }
    };
    SettingsApp.prototype.updateErrors = function (errors) {
        this.updating = true;
        try {
            this.showErrorWithInfo(elementId.configNameInvalid, errors.name);
            this.showErrorWithInfo(elementId.intelliSenseModeInvalid, errors.intelliSenseMode);
            this.showErrorWithInfo(elementId.compilerPathInvalid, errors.compilerPath);
            this.showErrorWithInfo(elementId.includePathInvalid, errors.includePath);
            this.showErrorWithInfo(elementId.macFrameworkPathInvalid, errors.macFrameworkPath);
            this.showErrorWithInfo(elementId.forcedIncludeInvalid, errors.forcedInclude);
            this.showErrorWithInfo(elementId.compileCommandsInvalid, errors.compileCommands);
            this.showErrorWithInfo(elementId.browsePathInvalid, errors.browsePath);
            this.showErrorWithInfo(elementId.databaseFilenameInvalid, errors.databaseFilename);
            this.showErrorWithInfo(elementId.dotConfigInvalid, errors.dotConfig);
        }
        finally {
            this.updating = false;
        }
    };
    SettingsApp.prototype.showErrorWithInfo = function (elementID, errorInfo) {
        this.showElement(elementID, errorInfo ? true : false);
        document.getElementById(elementID).innerHTML = errorInfo ? errorInfo : "";
    };
    SettingsApp.prototype.updateConfigSelection = function (message) {
        this.updating = true;
        try {
            var list = document.getElementById(elementId.configSelection);
            // Clear list before updating
            list.options.length = 0;
            // Update list
            for (var _i = 0, _a = message.selections; _i < _a.length; _i++) {
                var name_1 = _a[_i];
                var option = document.createElement("option");
                option.text = name_1;
                option.value = name_1;
                list.append(option);
            }
            list.selectedIndex = message.selectedIndex;
        }
        finally {
            this.updating = false;
        }
    };
    SettingsApp.prototype.setKnownCompilers = function (compilers) {
        this.updating = true;
        try {
            var list = document.getElementById(elementId.knownCompilers);
            // No need to add items unless webview is reloaded, in which case it will not have any elements.
            // Otherwise, add items again.
            if (list.firstChild) {
                return;
            }
            if (compilers.length === 0) {
                // Get HTML element containing the string, as we can't localize strings in HTML js
                var noCompilerSpan = document.getElementById(elementId.noCompilerPathsDetected);
                var option = document.createElement("option");
                option.text = noCompilerSpan.textContent;
                option.disabled = true;
                list.append(option);
            }
            else {
                for (var _i = 0, compilers_1 = compilers; _i < compilers_1.length; _i++) {
                    var path = compilers_1[_i];
                    var option = document.createElement("option");
                    option.text = path;
                    option.value = path;
                    list.append(option);
                }
            }
            this.showElement(elementId.compilerPath, true);
            this.showElement(elementId.knownCompilers, true);
            // Initialize list with no selected item
            list.value = "";
        }
        finally {
            this.updating = false;
        }
    };
    SettingsApp.prototype.showElement = function (elementID, show) {
        document.getElementById(elementID).style.display = show ? "block" : "none";
    };
    return SettingsApp;
}());
var app = new SettingsApp();
