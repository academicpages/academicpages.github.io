exports.id = 317;
exports.ids = [317];
exports.modules = {

/***/ 9317:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

/*!
 * 1DS JS SDK Core, 3.2.3
 * Copyright (c) Microsoft and contributors. All rights reserved.
 * (Microsoft Internal Only)
 */
(function (global, factory) {
     true ? factory(exports, __webpack_require__(7424), __webpack_require__(7855), __webpack_require__(1331)) :
    0;
})(this, (function (exports, applicationinsightsShims, applicationinsightsCoreJs, dynamicProto) { 'use strict';

    function _interopDefaultLegacy (e) { return e && typeof e === 'object' && 'default' in e ? e["default"] : e; }

    var dynamicProto__default = /*#__PURE__*/_interopDefaultLegacy(dynamicProto);

    var ValueKind = applicationinsightsCoreJs.createEnumStyle({
        NotSet: 0 ,
        Pii_DistinguishedName: 1 ,
        Pii_GenericData: 2 ,
        Pii_IPV4Address: 3 ,
        Pii_IPv6Address: 4 ,
        Pii_MailSubject: 5 ,
        Pii_PhoneNumber: 6 ,
        Pii_QueryString: 7 ,
        Pii_SipAddress: 8 ,
        Pii_SmtpAddress: 9 ,
        Pii_Identity: 10 ,
        Pii_Uri: 11 ,
        Pii_Fqdn: 12 ,
        Pii_IPV4AddressLegacy: 13 ,
        CustomerContent_GenericContent: 32
    });
    var EventLatency = applicationinsightsCoreJs.createEnumStyle({
        Normal: 1 ,
        CostDeferred: 2 ,
        RealTime: 3 ,
        Immediate: 4
    });
    var EventPropertyType = applicationinsightsCoreJs.createEnumStyle({
        Unspecified: 0 ,
        String: 1 ,
        Int32: 2 ,
        UInt32: 3 ,
        Int64: 4 ,
        UInt64: 5 ,
        Double: 6 ,
        Bool: 7 ,
        Guid: 8 ,
        DateTime: 9
    });
    var EventPersistence = applicationinsightsCoreJs.createEnumStyle({
        Normal: 1 ,
        Critical: 2
    });
    var TraceLevel = applicationinsightsCoreJs.createEnumStyle({
        NONE: 0 ,
        ERROR: 1 ,
        WARNING: 2 ,
        INFORMATION: 3
    });
    var _ExtendedInternalMessageId = applicationinsightsCoreJs.objFreeze(applicationinsightsShims.__assignFn(applicationinsightsShims.__assignFn({}, applicationinsightsCoreJs._InternalMessageId), applicationinsightsCoreJs.createEnumStyle({
        AuthHandShakeError: 501 ,
        AuthRedirectFail: 502 ,
        BrowserCannotReadLocalStorage: 503 ,
        BrowserCannotWriteLocalStorage: 504 ,
        BrowserDoesNotSupportLocalStorage: 505 ,
        CannotParseBiBlobValue: 506 ,
        CannotParseDataAttribute: 507 ,
        CVPluginNotAvailable: 508 ,
        DroppedEvent: 509 ,
        ErrorParsingAISessionCookie: 510 ,
        ErrorProvidedChannels: 511 ,
        FailedToGetCookies: 512 ,
        FailedToInitializeCorrelationVector: 513 ,
        FailedToInitializeSDK: 514 ,
        InvalidContentBlob: 515 ,
        InvalidCorrelationValue: 516 ,
        SessionRenewalDateIsZero: 517 ,
        SendPostOnCompleteFailure: 518 ,
        PostResponseHandler: 519 ,
        SDKNotInitialized: 520
    })));

    var _a;
    var Version = '3.2.3';
    var FullVersionString = "1DS-Web-JS-" + Version;
    var strDisabledPropertyName = "Microsoft_ApplicationInsights_BypassAjaxInstrumentation";
    var strWithCredentials = "withCredentials";
    var strTimeout = "timeout";
    var _fieldTypeEventPropMap = (_a = {},
        _a[0 ] = 0 ,
        _a[2 ] = 6 ,
        _a[1 ] = 1 ,
        _a[3 ] = 7 ,
        _a[4096  | 2 ] = 6 ,
        _a[4096  | 1 ] = 1 ,
        _a[4096  | 3 ] = 7 ,
        _a);
    var uInt8ArraySupported = null;
    var isDocumentObjectAvailable = Boolean(applicationinsightsCoreJs.getDocument());
    var isWindowObjectAvailable = Boolean(applicationinsightsCoreJs.getWindow());
    function isValueAssigned(value) {
        return !(value === "" || applicationinsightsCoreJs.isNullOrUndefined(value));
    }
    function getTenantId(apiKey) {
        if (apiKey) {
            var indexTenantId = apiKey.indexOf("-");
            if (indexTenantId > -1) {
                return apiKey.substring(0, indexTenantId);
            }
        }
        return "";
    }
    function isUint8ArrayAvailable() {
        if (uInt8ArraySupported === null) {
            uInt8ArraySupported = !applicationinsightsCoreJs.isUndefined(Uint8Array) && !isSafariOrFirefox() && !applicationinsightsCoreJs.isReactNative();
        }
        return uInt8ArraySupported;
    }
    function isLatency(value) {
        if (value && applicationinsightsCoreJs.isNumber(value) && value >= 1  && value <= 4 ) {
            return true;
        }
        return false;
    }
    function sanitizeProperty(name, property, stringifyObjects) {
        if ((!property && !isValueAssigned(property)) || typeof name !== "string") {
            return null;
        }
        var propType = typeof property;
        if (propType === "string" || propType === "number" || propType === "boolean" || applicationinsightsCoreJs.isArray(property)) {
            property = { value: property };
        }
        else if (propType === "object" && !property.hasOwnProperty("value")) {
            property = { value: stringifyObjects ? JSON.stringify(property) : property };
        }
        else if (applicationinsightsCoreJs.isNullOrUndefined(property.value)
            || property.value === "" || (!applicationinsightsCoreJs.isString(property.value)
            && !applicationinsightsCoreJs.isNumber(property.value) && !applicationinsightsCoreJs.isBoolean(property.value)
            && !applicationinsightsCoreJs.isArray(property.value))) {
            return null;
        }
        if (applicationinsightsCoreJs.isArray(property.value) &&
            !isArrayValid(property.value)) {
            return null;
        }
        if (!applicationinsightsCoreJs.isNullOrUndefined(property.kind)) {
            if (applicationinsightsCoreJs.isArray(property.value) || !isValueKind(property.kind)) {
                return null;
            }
            property.value = property.value.toString();
        }
        return property;
    }
    function getCommonSchemaMetaData(value, kind, type) {
        var encodedTypeValue = -1;
        if (!applicationinsightsCoreJs.isUndefined(value)) {
            if (kind > 0) {
                if (kind === 32) {
                    encodedTypeValue = (1 << 13);
                }
                else if (kind <= 13) {
                    encodedTypeValue = (kind << 5);
                }
            }
            if (isDataType(type)) {
                if (encodedTypeValue === -1) {
                    encodedTypeValue = 0;
                }
                encodedTypeValue |= type;
            }
            else {
                var propType = _fieldTypeEventPropMap[getFieldValueType(value)] || -1;
                if (encodedTypeValue !== -1 && propType !== -1) {
                    encodedTypeValue |= propType;
                }
                else if (propType === 6 ) {
                    encodedTypeValue = propType;
                }
            }
        }
        return encodedTypeValue;
    }
    function disableCookies() {
        applicationinsightsCoreJs.safeGetCookieMgr(null).setEnabled(false);
    }
    function setCookie(name, value, days) {
        if (applicationinsightsCoreJs.areCookiesSupported(null)) {
            applicationinsightsCoreJs.safeGetCookieMgr(null).set(name, value, days * 86400, null, "/");
        }
    }
    function deleteCookie(name) {
        if (applicationinsightsCoreJs.areCookiesSupported(null)) {
            applicationinsightsCoreJs.safeGetCookieMgr(null).del(name);
        }
    }
    function getCookie(name) {
        if (applicationinsightsCoreJs.areCookiesSupported(null)) {
            return getCookieValue(applicationinsightsCoreJs.safeGetCookieMgr(null), name);
        }
        return "";
    }
    function getCookieValue(cookieMgr, name, decode) {
        if (decode === void 0) { decode = true; }
        var cookieValue;
        if (cookieMgr) {
            cookieValue = cookieMgr.get(name);
            if (decode && cookieValue && decodeURIComponent) {
                cookieValue = decodeURIComponent(cookieValue);
            }
        }
        return cookieValue || "";
    }
    function createGuid(style) {
        if (style === void 0) { style = "D" ; }
        var theGuid = applicationinsightsCoreJs.newGuid();
        if (style === "B" ) {
            theGuid = "{" + theGuid + "}";
        }
        else if (style === "P" ) {
            theGuid = "(" + theGuid + ")";
        }
        else if (style === "N" ) {
            theGuid = theGuid.replace(/-/g, "");
        }
        return theGuid;
    }
    function extend(obj, obj2, obj3, obj4, obj5) {
        var extended = {};
        var deep = false;
        var i = 0;
        var length = arguments.length;
        var objProto = Object[applicationinsightsCoreJs.strPrototype];
        var theArgs = arguments;
        if (objProto.toString.call(theArgs[0]) === "[object Boolean]") {
            deep = theArgs[0];
            i++;
        }
        for (; i < length; i++) {
            var obj = theArgs[i];
            applicationinsightsCoreJs.objForEachKey(obj, function (prop, value) {
                if (deep && value && applicationinsightsCoreJs.isObject(value)) {
                    if (applicationinsightsCoreJs.isArray(value)) {
                        extended[prop] = extended[prop] || [];
                        applicationinsightsCoreJs.arrForEach(value, function (arrayValue, arrayIndex) {
                            if (arrayValue && applicationinsightsCoreJs.isObject(arrayValue)) {
                                extended[prop][arrayIndex] = extend(true, extended[prop][arrayIndex], arrayValue);
                            }
                            else {
                                extended[prop][arrayIndex] = arrayValue;
                            }
                        });
                    }
                    else {
                        extended[prop] = extend(true, extended[prop], value);
                    }
                }
                else {
                    extended[prop] = value;
                }
            });
        }
        return extended;
    }
    var getTime = applicationinsightsCoreJs.perfNow;
    function isValueKind(value) {
        if (value === 0  || ((value > 0  && value <= 13 ) || value === 32 )) {
            return true;
        }
        return false;
    }
    function isDataType(value) {
        if (value >= 0 && value <= 9) {
            return true;
        }
        return false;
    }
    function isSafariOrFirefox() {
        var nav = applicationinsightsCoreJs.getNavigator();
        if (!applicationinsightsCoreJs.isUndefined(nav) && nav.userAgent) {
            var ua = nav.userAgent.toLowerCase();
            if ((ua.indexOf("safari") >= 0 || ua.indexOf("firefox") >= 0) && ua.indexOf("chrome") < 0) {
                return true;
            }
        }
        return false;
    }
    function isArrayValid(value) {
        return value.length > 0;
    }
    function setProcessTelemetryTimings(event, identifier) {
        var evt = event;
        evt.timings = evt.timings || {};
        evt.timings.processTelemetryStart = evt.timings.processTelemetryStart || {};
        evt.timings.processTelemetryStart[identifier] = getTime();
    }
    function getFieldValueType(value) {
        var theType = 0 ;
        if (value !== null && value !== undefined) {
            var objType = typeof value;
            if (objType === "string") {
                theType = 1 ;
            }
            else if (objType === "number") {
                theType = 2 ;
            }
            else if (objType === "boolean") {
                theType = 3 ;
            }
            else if (objType === applicationinsightsShims.strShimObject) {
                theType = 4 ;
                if (applicationinsightsCoreJs.isArray(value)) {
                    theType = 4096 ;
                    if (value.length > 0) {
                        theType |= getFieldValueType(value[0]);
                    }
                }
                else if (applicationinsightsCoreJs.hasOwnProperty(value, "value")) {
                    theType = 8192  | getFieldValueType(value.value);
                }
            }
        }
        return theType;
    }
    var Utils = {
        Version: Version,
        FullVersionString: FullVersionString,
        strUndefined: applicationinsightsCoreJs.strUndefined,
        strObject: applicationinsightsCoreJs.strObject,
        Undefined: applicationinsightsCoreJs.strUndefined,
        arrForEach: applicationinsightsCoreJs.arrForEach,
        arrIndexOf: applicationinsightsCoreJs.arrIndexOf,
        arrMap: applicationinsightsCoreJs.arrMap,
        arrReduce: applicationinsightsCoreJs.arrReduce,
        objKeys: applicationinsightsCoreJs.objKeys,
        toISOString: applicationinsightsCoreJs.toISOString,
        isReactNative: applicationinsightsCoreJs.isReactNative,
        isString: applicationinsightsCoreJs.isString,
        isNumber: applicationinsightsCoreJs.isNumber,
        isBoolean: applicationinsightsCoreJs.isBoolean,
        isFunction: applicationinsightsCoreJs.isFunction,
        isArray: applicationinsightsCoreJs.isArray,
        isObject: applicationinsightsCoreJs.isObject,
        strTrim: applicationinsightsCoreJs.strTrim,
        isDocumentObjectAvailable: isDocumentObjectAvailable,
        isWindowObjectAvailable: isWindowObjectAvailable,
        isValueAssigned: isValueAssigned,
        getTenantId: getTenantId,
        isBeaconsSupported: applicationinsightsCoreJs.isBeaconsSupported,
        isUint8ArrayAvailable: isUint8ArrayAvailable,
        isLatency: isLatency,
        sanitizeProperty: sanitizeProperty,
        getISOString: applicationinsightsCoreJs.toISOString,
        useXDomainRequest: applicationinsightsCoreJs.useXDomainRequest,
        getCommonSchemaMetaData: getCommonSchemaMetaData,
        cookieAvailable: applicationinsightsCoreJs.areCookiesSupported,
        disallowsSameSiteNone: applicationinsightsCoreJs.uaDisallowsSameSiteNone,
        setCookie: setCookie,
        deleteCookie: deleteCookie,
        getCookie: getCookie,
        createGuid: createGuid,
        extend: extend,
        getTime: getTime,
        isValueKind: isValueKind,
        isArrayValid: isArrayValid,
        objDefineAccessors: applicationinsightsCoreJs.objDefineAccessors,
        addPageUnloadEventListener: applicationinsightsCoreJs.addPageUnloadEventListener,
        setProcessTelemetryTimings: setProcessTelemetryTimings,
        addEventHandler: applicationinsightsCoreJs.addEventHandler,
        getFieldValueType: getFieldValueType,
        strEndsWith: applicationinsightsCoreJs.strEndsWith,
        objForEachKey: applicationinsightsCoreJs.objForEachKey
    };
    var CoreUtils = {
        _canUseCookies: undefined,
        isTypeof: applicationinsightsCoreJs.isTypeof,
        isUndefined: applicationinsightsCoreJs.isUndefined,
        isNullOrUndefined: applicationinsightsCoreJs.isNullOrUndefined,
        hasOwnProperty: applicationinsightsCoreJs.hasOwnProperty,
        isFunction: applicationinsightsCoreJs.isFunction,
        isObject: applicationinsightsCoreJs.isObject,
        isDate: applicationinsightsCoreJs.isDate,
        isArray: applicationinsightsCoreJs.isArray,
        isError: applicationinsightsCoreJs.isError,
        isString: applicationinsightsCoreJs.isString,
        isNumber: applicationinsightsCoreJs.isNumber,
        isBoolean: applicationinsightsCoreJs.isBoolean,
        toISOString: applicationinsightsCoreJs.toISOString,
        arrForEach: applicationinsightsCoreJs.arrForEach,
        arrIndexOf: applicationinsightsCoreJs.arrIndexOf,
        arrMap: applicationinsightsCoreJs.arrMap,
        arrReduce: applicationinsightsCoreJs.arrReduce,
        strTrim: applicationinsightsCoreJs.strTrim,
        objCreate: applicationinsightsShims.objCreateFn,
        objKeys: applicationinsightsCoreJs.objKeys,
        objDefineAccessors: applicationinsightsCoreJs.objDefineAccessors,
        addEventHandler: applicationinsightsCoreJs.addEventHandler,
        dateNow: applicationinsightsCoreJs.dateNow,
        isIE: applicationinsightsCoreJs.isIE,
        disableCookies: disableCookies,
        newGuid: applicationinsightsCoreJs.newGuid,
        perfNow: applicationinsightsCoreJs.perfNow,
        newId: applicationinsightsCoreJs.newId,
        randomValue: applicationinsightsCoreJs.randomValue,
        random32: applicationinsightsCoreJs.random32,
        mwcRandomSeed: applicationinsightsCoreJs.mwcRandomSeed,
        mwcRandom32: applicationinsightsCoreJs.mwcRandom32,
        generateW3CId: applicationinsightsCoreJs.generateW3CId
    };
    function isChromium() {
        return !!applicationinsightsCoreJs.getGlobalInst("chrome");
    }
    function openXhr(method, urlString, withCredentials, disabled, isSync, timeout) {
        if (disabled === void 0) { disabled = false; }
        if (isSync === void 0) { isSync = false; }
        function _wrapSetXhrProp(xhr, prop, value) {
            try {
                xhr[prop] = value;
            }
            catch (e) {
            }
        }
        var xhr = new XMLHttpRequest();
        if (disabled) {
            _wrapSetXhrProp(xhr, strDisabledPropertyName, disabled);
        }
        if (withCredentials) {
            _wrapSetXhrProp(xhr, strWithCredentials, withCredentials);
        }
        xhr.open(method, urlString, !isSync);
        if (withCredentials) {
            _wrapSetXhrProp(xhr, strWithCredentials, withCredentials);
        }
        if (!isSync && timeout) {
            _wrapSetXhrProp(xhr, strTimeout, timeout);
        }
        return xhr;
    }

    var PropVersion = "version";
    var properties = "properties";
    var AppInsightsCore = /** @class */ (function (_super) {
        applicationinsightsShims.__extendsFn(AppInsightsCore, _super);
        function AppInsightsCore() {
            var _this = _super.call(this) || this;
            _this.pluginVersionStringArr = [];
            _this.pluginVersionString = "";
            dynamicProto__default(AppInsightsCore, _this, function (_self, _base) {
                if (!_self.logger || !_self.logger.queue) {
                    _self.logger = new applicationinsightsCoreJs.DiagnosticLogger({ loggingLevelConsole: 1  });
                }
                _self.initialize = function (config, extensions, logger, notificationManager) {
                    applicationinsightsCoreJs.doPerf(_self, function () { return "AppInsightsCore.initialize"; }, function () {
                        if (config) {
                            if (!config.endpointUrl) {
                                config.endpointUrl = "https://browser.events.data.microsoft.com/OneCollector/1.0/";
                            }
                            var propertyStorageOverride = config.propertyStorageOverride;
                            if (propertyStorageOverride && (!propertyStorageOverride.getProperty || !propertyStorageOverride.setProperty)) {
                                throw new Error("Invalid property storage override passed.");
                            }
                            if (config.channels) {
                                applicationinsightsCoreJs.arrForEach(config.channels, function (channels) {
                                    if (channels) {
                                        applicationinsightsCoreJs.arrForEach(channels, function (channel) {
                                            if (channel.identifier && channel.version) {
                                                var ver = channel.identifier + "=" + channel.version;
                                                _self.pluginVersionStringArr.push(ver);
                                            }
                                        });
                                    }
                                });
                            }
                        }
                        _self.getWParam = function () {
                            return typeof document !== "undefined" ? 0 : -1;
                        };
                        if (extensions) {
                            applicationinsightsCoreJs.arrForEach(extensions, function (ext) {
                                if (ext && ext.identifier && ext.version) {
                                    var ver = ext.identifier + "=" + ext.version;
                                    _self.pluginVersionStringArr.push(ver);
                                }
                            });
                        }
                        _self.pluginVersionString = _self.pluginVersionStringArr.join(";");
                        try {
                            _base.initialize(config, extensions, logger, notificationManager);
                            _self.pollInternalLogs("InternalLog");
                        }
                        catch (e) {
                            var logger_1 = _self.logger;
                            var message = applicationinsightsCoreJs.dumpObj(e);
                            if (message.indexOf("channels") !== -1) {
                                message += "\n - Channels must be provided through config.channels only!";
                            }
                            logger_1.throwInternal(1 , 514 , "SDK Initialization Failed - no telemetry will be sent: " + message);
                        }
                    }, function () { return ({ config: config, extensions: extensions, logger: logger, notificationManager: notificationManager }); });
                };
                _self.track = function (item) {
                    applicationinsightsCoreJs.doPerf(_self, function () { return "AppInsightsCore.track"; }, function () {
                        var telemetryItem = item;
                        if (telemetryItem) {
                            telemetryItem.timings = telemetryItem.timings || {};
                            telemetryItem.timings.trackStart = getTime();
                            if (!isLatency(telemetryItem.latency)) {
                                telemetryItem.latency = 1 ;
                            }
                            var itemExt = telemetryItem.ext = telemetryItem.ext || {};
                            itemExt.sdk = itemExt.sdk || {};
                            itemExt.sdk.ver = FullVersionString;
                            var baseData = telemetryItem.baseData = telemetryItem.baseData || {};
                            if (!baseData[properties]) {
                                baseData[properties] = {};
                            }
                            var itemProperties = baseData[properties];
                            if (!itemProperties[PropVersion]) {
                                itemProperties[PropVersion] = "";
                            }
                            if (_self.pluginVersionString !== "") {
                                itemProperties[PropVersion] = _self.pluginVersionString;
                            }
                        }
                        _base.track(telemetryItem);
                    }, function () { return ({ item: item }); }, !(item.sync));
                };
            });
            return _this;
        }
        return AppInsightsCore;
    }(applicationinsightsCoreJs.AppInsightsCore));

    var BaseCore = /** @class */ (function (_super) {
        applicationinsightsShims.__extendsFn(BaseCore, _super);
        function BaseCore() {
            var _this = _super.call(this) || this;
            dynamicProto__default(BaseCore, _this, function (_self, _base) {
                _self.initialize = function (config, extensions, logger, notificationManager) {
                    if (config && !config.endpointUrl) {
                        config.endpointUrl = "https://browser.events.data.microsoft.com/OneCollector/1.0/";
                    }
                    _self.getWParam = function () {
                        return isDocumentObjectAvailable ? 0 : -1;
                    };
                    try {
                        _base.initialize(config, extensions, logger, notificationManager);
                    }
                    catch (e) {
                        applicationinsightsCoreJs._throwInternal(_self.logger, 1 , 514 , "Initialization Failed: " + applicationinsightsCoreJs.dumpObj(e) + "\n - Note: Channels must be provided through config.channels only");
                    }
                };
                _self.track = function (item) {
                    var telemetryItem = item;
                    if (telemetryItem) {
                        var ext = telemetryItem.ext = telemetryItem.ext || {};
                        ext.sdk = ext.sdk || {};
                        ext.sdk.ver = FullVersionString;
                    }
                    _base.track(telemetryItem);
                };
            });
            return _this;
        }
        return BaseCore;
    }(applicationinsightsCoreJs.BaseCore));

    var _isFunction = applicationinsightsCoreJs.isFunction;
    function _createPromiseAllOnResolvedFunction(values, index, resolvedCallback) {
        return function (value) {
            values[index] = value;
            resolvedCallback();
        };
    }
    var ESPromise = /** @class */ (function () {
        function ESPromise(resolverFunc) {
            var _state = 0 ;
            var _settledValue = null;
            var _queue = [];
            dynamicProto__default(ESPromise, this, function (_this) {
                _this.then = function (onResolved, onRejected) {
                    return new ESPromise(function (resolve, reject) {
                        _enqueue(onResolved, onRejected, resolve, reject);
                    });
                };
                _this["catch"] = function (onRejected) {
                    return _this.then(null, onRejected);
                };
            });
            function _enqueue(onResolved, onRejected, resolve, reject) {
                _queue.push(function () {
                    var value;
                    try {
                        if (_state === 1 ) {
                            value = _isFunction(onResolved) ? onResolved(_settledValue) : _settledValue;
                        }
                        else {
                            value = _isFunction(onRejected) ? onRejected(_settledValue) : _settledValue;
                        }
                        if (value instanceof ESPromise) {
                            value.then(resolve, reject);
                        }
                        else if (_state === 2  && !_isFunction(onRejected)) {
                            reject(value);
                        }
                        else {
                            resolve(value);
                        }
                    }
                    catch (error) {
                        reject(error);
                        return;
                    }
                });
                if (_state !== 0 ) {
                    _processQueue();
                }
            }
            function _processQueue() {
                if (_queue.length > 0) {
                    var pending_1 = _queue.slice();
                    _queue = [];
                    setTimeout(function () {
                        for (var i = 0, len = pending_1.length; i < len; ++i) {
                            try {
                                pending_1[i]();
                            }
                            catch (e) {
                            }
                        }
                    }, 0);
                }
            }
            function _resolve(value) {
                if (_state === 0 ) {
                    _settledValue = value;
                    _state = 1 ;
                    _processQueue();
                }
            }
            function _reject(reason) {
                if (_state === 0 ) {
                    _settledValue = reason;
                    _state = 2 ;
                    _processQueue();
                }
            }
            (function _initialize() {
                if (!_isFunction(resolverFunc)) {
                    throw new TypeError("ESPromise: resolvedFunc argument is not a Function");
                }
                try {
                    resolverFunc(_resolve, _reject);
                }
                catch (error) {
                    _reject(error);
                }
            })();
        }
        ESPromise.resolve = function (value) {
            if (value instanceof ESPromise) {
                return value;
            }
            else if (value && _isFunction(value.then)) {
                return new ESPromise(function (resolve, reject) {
                    try {
                        value.then(resolve, reject);
                    }
                    catch (error) {
                        reject(error);
                    }
                });
            }
            return new ESPromise(function (resolve) {
                resolve(value);
            });
        };
        ESPromise.reject = function (reason) {
            return new ESPromise(function (resolve, reject) {
                reject(reason);
            });
        };
        ESPromise.all = function (iterable) {
            if (!iterable || !iterable.length) {
                return;
            }
            return new ESPromise(function (resolve, reject) {
                try {
                    var values_1 = [];
                    var pending_2 = 0;
                    for (var lp = 0; lp < iterable.length; lp++) {
                        var item = iterable[lp];
                        if (item && _isFunction(item.then)) {
                            pending_2++;
                            item.then(_createPromiseAllOnResolvedFunction(values_1, lp, function () {
                                if (--pending_2 === 0) {
                                    resolve(values_1);
                                }
                            }), reject);
                        }
                        else {
                            values_1[lp] = item;
                        }
                    }
                    if (pending_2 === 0) {
                        setTimeout(function () {
                            resolve(values_1);
                        }, 0);
                    }
                }
                catch (error) {
                    reject(error);
                }
            });
        };
        ESPromise.race = function (iterable) {
            return new ESPromise(function (resolve, reject) {
                if (!iterable || !iterable.length) {
                    return;
                }
                try {
                    var _loop_1 = function (lp) {
                        var item = iterable[lp];
                        if (item && _isFunction(item.then)) {
                            item.then(resolve, reject);
                        }
                        else {
                            setTimeout(function () {
                                resolve(item);
                            }, 0);
                        }
                    };
                    for (var lp = 0; lp < iterable.length; lp++) {
                        _loop_1(lp);
                    }
                }
                catch (error) {
                    reject(error);
                }
            });
        };
        return ESPromise;
    }());

    var LazyRejectPeriod = 600000;
    var _schedulerId = 0;
    var _running = [];
    var _waiting = [];
    var _timedOut = [];
    function _getTime() {
        return new Date().getTime();
    }
    var ESPromiseScheduler = /** @class */ (function () {
        function ESPromiseScheduler(name, diagLog) {
            var _promiseId = 0;
            var _scheduledName = (name || "<unnamed>") + "." + _schedulerId;
            _schedulerId++;
            dynamicProto__default(ESPromiseScheduler, this, function (_this) {
                var _lastEvent = null;
                var _eventCount = 0;
                _this.scheduleEvent = function (startEventAction, eventName, timeout) {
                    var uniqueId = _scheduledName + "." + _eventCount;
                    _eventCount++;
                    if (eventName) {
                        uniqueId += "-(" + eventName + ")";
                    }
                    var uniqueEventId = uniqueId + "{" + _promiseId + "}";
                    _promiseId++;
                    var newScheduledEvent = {
                        evt: null,
                        tm: _getTime(),
                        id: uniqueEventId,
                        isRunning: false,
                        isAborted: false
                    };
                    if (!_lastEvent) {
                        newScheduledEvent.evt = _startWaitingEvent(newScheduledEvent);
                    }
                    else {
                        newScheduledEvent.evt = _waitForPreviousEvent(newScheduledEvent, _lastEvent);
                    }
                    _lastEvent = newScheduledEvent;
                    _lastEvent.evt._schId = uniqueEventId;
                    return newScheduledEvent.evt;
                    function _abortAndRemoveOldEvents(eventQueue) {
                        var now = _getTime();
                        var expired = now - LazyRejectPeriod;
                        var len = eventQueue.length;
                        var lp = 0;
                        while (lp < len) {
                            var evt = eventQueue[lp];
                            if (evt && evt.tm < expired) {
                                var message = null;
                                if (evt.abort) {
                                    message = "Aborting [" + evt.id + "] due to Excessive runtime (" + (now - evt.tm) + " ms)";
                                    evt.abort(message);
                                }
                                else {
                                    message = "Removing [" + evt.id + "] due to Excessive runtime (" + (now - evt.tm) + " ms)";
                                }
                                _warnLog(message);
                                eventQueue.splice(lp, 1);
                                len--;
                            }
                            else {
                                lp++;
                            }
                        }
                    }
                    function _cleanup(eventId, completed) {
                        var toQueue = false;
                        var removed = _removeQueuedEvent(_running, eventId);
                        if (!removed) {
                            removed = _removeQueuedEvent(_timedOut, eventId);
                            toQueue = true;
                        }
                        if (removed) {
                            if (removed.to) {
                                clearTimeout(removed.to);
                                removed.to = null;
                            }
                            var tm = _getTime() - removed.tm;
                            if (completed) {
                                if (!toQueue) {
                                    _debugLog("Promise [" + eventId + "] Complete -- " + tm + " ms");
                                }
                                else {
                                    _warnLog("Timed out event [" + eventId + "] finally complete -- " + tm + " ms");
                                }
                            }
                            else {
                                _timedOut.push(removed);
                                _warnLog("Event [" + eventId + "] Timed out and removed -- " + tm + " ms");
                            }
                        }
                        else {
                            _debugLog("Failed to remove [" + eventId + "] from running queue");
                        }
                        if (_lastEvent && _lastEvent.id === eventId) {
                            _lastEvent = null;
                        }
                        _abortAndRemoveOldEvents(_running);
                        _abortAndRemoveOldEvents(_waiting);
                        _abortAndRemoveOldEvents(_timedOut);
                    }
                    function _removeScheduledEvent(eventId, callback) {
                        return function (value) {
                            _cleanup(eventId, true);
                            callback && callback(value);
                            return value;
                        };
                    }
                    function _waitForFinalResult(eventId, startResult, schEventResolve, schEventReject) {
                        startResult.then(function (value) {
                            if (value instanceof ESPromise) {
                                _debugLog("Event [" + eventId + "] returned a promise -- waiting");
                                _waitForFinalResult(eventId, value, schEventResolve, schEventReject);
                                return value;
                            }
                            else {
                                return _removeScheduledEvent(eventId, schEventResolve)(value);
                            }
                        }, _removeScheduledEvent(eventId, schEventReject));
                    }
                    function _createScheduledEvent(eventDetails, startEvent) {
                        var eventId = eventDetails.id;
                        return new ESPromise(function (schEventResolve, schEventReject) {
                            _debugLog("Event [" + eventId + "] Starting -- waited for " + (eventDetails.wTm || "--") + " ms");
                            eventDetails.isRunning = true;
                            eventDetails.abort = function (message) {
                                eventDetails.abort = null;
                                eventDetails.isAborted = true;
                                _cleanup(eventId, false);
                                schEventReject(new Error(message));
                            };
                            var startResult = startEvent(eventId);
                            if (startResult instanceof ESPromise) {
                                if (timeout) {
                                    eventDetails.to = setTimeout(function () {
                                        _cleanup(eventId, false);
                                        schEventReject(new Error("Timed out after [" + timeout + "] ms"));
                                    }, timeout);
                                }
                                _waitForFinalResult(eventId, startResult, function (theResult) {
                                    _debugLog("Event [" + eventId + "] Resolving after " + (_getTime() - eventDetails.tm) + " ms");
                                    schEventResolve(theResult);
                                }, schEventReject);
                            }
                            else {
                                _debugLog("Promise [" + eventId + "] Auto completed as the start action did not return a promise");
                                schEventResolve();
                            }
                        });
                    }
                    function _startWaitingEvent(eventDetails) {
                        var now = _getTime();
                        eventDetails.wTm = now - eventDetails.tm;
                        eventDetails.tm = now;
                        if (eventDetails.isAborted) {
                            return ESPromise.reject(new Error("[" + uniqueId + "] was aborted"));
                        }
                        _running.push(eventDetails);
                        return _createScheduledEvent(eventDetails, startEventAction);
                    }
                    function _waitForPreviousEvent(eventDetails, waitForEvent) {
                        var waitEvent = new ESPromise(function (waitResolve, waitReject) {
                            var runTime = _getTime() - waitForEvent.tm;
                            var prevId = waitForEvent.id;
                            _debugLog("[" + uniqueId + "] is waiting for [" + prevId + ":" + runTime + " ms] to complete before starting -- [" + _waiting.length + "] waiting and [" + _running.length + "] running");
                            eventDetails.abort = function (message) {
                                eventDetails.abort = null;
                                _removeQueuedEvent(_waiting, uniqueId);
                                eventDetails.isAborted = true;
                                waitReject(new Error(message));
                            };
                            waitForEvent.evt.then(function (value) {
                                _removeQueuedEvent(_waiting, uniqueId);
                                _startWaitingEvent(eventDetails).then(waitResolve, waitReject);
                            }, function (reason) {
                                _removeQueuedEvent(_waiting, uniqueId);
                                _startWaitingEvent(eventDetails).then(waitResolve, waitReject);
                            });
                        });
                        _waiting.push(eventDetails);
                        return waitEvent;
                    }
                };
                function _removeQueuedEvent(queue, eventId) {
                    for (var lp = 0; lp < queue.length; lp++) {
                        if (queue[lp].id === eventId) {
                            return queue.splice(lp, 1)[0];
                        }
                    }
                    return null;
                }
            });
            function _debugLog(message) {
                var global = applicationinsightsCoreJs.getGlobal();
                if (global && global["QUnit"]) {
                    console && console.log("ESPromiseScheduler[" + _scheduledName + "] " + message);
                }
            }
            function _warnLog(message) {
                diagLog && diagLog.warnToConsole("ESPromiseScheduler[" + _scheduledName + "] " + message);
            }
        }
        ESPromiseScheduler.incomplete = function () {
            return _running;
        };
        ESPromiseScheduler.waitingToStart = function () {
            return _waiting;
        };
        return ESPromiseScheduler;
    }());

    var ValueSanitizer = /** @class */ (function () {
        function ValueSanitizer(fieldSanitizerProvider) {
            var _self = this;
            var _sanitizerMap = {};
            var _sanitizers = [];
            var _fieldSanitizers = [];
            if (fieldSanitizerProvider) {
                _fieldSanitizers.push(fieldSanitizerProvider);
            }
            function _getFieldSanitizer(path, name) {
                var result;
                var fieldLookup = _sanitizerMap[path];
                if (fieldLookup) {
                    result = fieldLookup[name];
                }
                if (!result && result !== null) {
                    if (applicationinsightsCoreJs.isString(path) && applicationinsightsCoreJs.isString(name)) {
                        if (_fieldSanitizers.length > 0) {
                            for (var lp = 0; lp < _fieldSanitizers.length; lp++) {
                                if (_fieldSanitizers[lp].handleField(path, name)) {
                                    result = {
                                        canHandle: true,
                                        fieldHandler: _fieldSanitizers[lp]
                                    };
                                    break;
                                }
                            }
                        }
                        else if (_sanitizers.length === 0) {
                            result = {
                                canHandle: true
                            };
                        }
                    }
                    if (!result && result !== null) {
                        result = null;
                        for (var lp = 0; lp < _sanitizers.length; lp++) {
                            if (_sanitizers[lp].handleField(path, name)) {
                                result = {
                                    canHandle: true,
                                    handler: _sanitizers[lp],
                                    fieldHandler: null
                                };
                                break;
                            }
                        }
                    }
                    if (!fieldLookup) {
                        fieldLookup = _sanitizerMap[path] = {};
                    }
                    fieldLookup[name] = result;
                }
                return result;
            }
            _self.addSanitizer = function (newSanitizer) {
                if (newSanitizer) {
                    _sanitizers.push(newSanitizer);
                    _sanitizerMap = {};
                }
            };
            _self.addFieldSanitizer = function (fieldSanitizer) {
                if (fieldSanitizer) {
                    _fieldSanitizers.push(fieldSanitizer);
                    _sanitizerMap = {};
                }
            };
            _self.handleField = function (path, name) {
                var mapValue = _getFieldSanitizer(path, name);
                return mapValue ? mapValue.canHandle : false;
            };
            _self.value = function (path, name, value, stringifyObjects) {
                var mapValue = _getFieldSanitizer(path, name);
                if (mapValue && mapValue.canHandle) {
                    if (!mapValue || !mapValue.canHandle) {
                        return null;
                    }
                    if (mapValue.handler) {
                        return mapValue.handler.value(path, name, value, stringifyObjects);
                    }
                    if (!applicationinsightsCoreJs.isString(name) || applicationinsightsCoreJs.isNullOrUndefined(value) || value === "") {
                        return null;
                    }
                    var property = null;
                    var fieldType = getFieldValueType(value);
                    if ((fieldType & 8192 ) === 8192 ) {
                        var subType = fieldType & ~8192 ;
                        property = value;
                        if (!isValueAssigned(property.value) ||
                            (subType !== 1  &&
                                subType !== 2  &&
                                subType !== 3  &&
                                (subType & 4096 ) !== 4096 )) {
                            return null;
                        }
                    }
                    else if (fieldType === 1  ||
                        fieldType === 2  ||
                        fieldType === 3  ||
                        (fieldType & 4096 ) === 4096 ) {
                        property = _convertToProperty(path, name, value);
                    }
                    else if (fieldType === 4 ) {
                        property = _convertToProperty(path, name, !!stringifyObjects ? JSON.stringify(value) : value);
                    }
                    if (property) {
                        return _handleProperty(mapValue, path, name, fieldType, property, stringifyObjects);
                    }
                }
                return null;
            };
            _self.property = function (path, name, property, stringifyObjects) {
                var mapValue = _getFieldSanitizer(path, name);
                if (!mapValue || !mapValue.canHandle) {
                    return null;
                }
                if (!applicationinsightsCoreJs.isString(name) || applicationinsightsCoreJs.isNullOrUndefined(property) || !isValueAssigned(property.value)) {
                    return null;
                }
                var fieldType = getFieldValueType(property.value);
                if (fieldType === 0 ) {
                    return null;
                }
                return _handleProperty(mapValue, path, name, fieldType, property, stringifyObjects);
            };
            function _handleProperty(mapValue, path, name, fieldType, property, stringifyObjects) {
                if (mapValue.handler) {
                    return mapValue.handler.property(path, name, property, stringifyObjects);
                }
                if (!applicationinsightsCoreJs.isNullOrUndefined(property.kind)) {
                    if ((fieldType & 4096 ) === 4096  || !isValueKind(property.kind)) {
                        return null;
                    }
                    property.value = property.value.toString();
                }
                return _callFieldSanitizer(mapValue.fieldHandler, path, name, fieldType, property);
            }
            function _convertToProperty(path, name, value) {
                if (isValueAssigned(value)) {
                    return { value: value };
                }
                return null;
            }
            function _callFieldSanitizer(fieldProvider, path, name, theType, property) {
                if (property && fieldProvider) {
                    var sanitizer = fieldProvider.getSanitizer(path, name, theType, property.kind, property.propertyType);
                    if (sanitizer) {
                        if (theType === 4 ) {
                            var newValue_1 = {};
                            var propValue = property.value;
                            applicationinsightsCoreJs.objForEachKey(propValue, function (propKey, theValue) {
                                var newPath = path + "." + name;
                                if (isValueAssigned(theValue)) {
                                    var newProp = _convertToProperty(newPath, propKey, theValue);
                                    newProp = _callFieldSanitizer(fieldProvider, newPath, propKey, getFieldValueType(theValue), newProp);
                                    if (newProp) {
                                        newValue_1[propKey] = newProp.value;
                                    }
                                }
                            });
                            property.value = newValue_1;
                        }
                        else {
                            var details = {
                                path: path,
                                name: name,
                                type: theType,
                                prop: property,
                                sanitizer: _self
                            };
                            property = sanitizer.call(_self, details);
                        }
                    }
                }
                return property;
            }
        }
        ValueSanitizer.getFieldType = getFieldValueType;
        return ValueSanitizer;
    }());

    exports.BaseTelemetryPlugin = applicationinsightsCoreJs.BaseTelemetryPlugin;
    exports.DiagnosticLogger = applicationinsightsCoreJs.DiagnosticLogger;
    exports.EventHelper = applicationinsightsCoreJs.EventHelper;
    exports.EventsDiscardedReason = applicationinsightsCoreJs.EventsDiscardedReason;
    exports.InternalAppInsightsCore = applicationinsightsCoreJs.AppInsightsCore;
    exports.InternalBaseCore = applicationinsightsCoreJs.BaseCore;
    exports.LoggingSeverity = applicationinsightsCoreJs.LoggingSeverity;
    exports.MinChannelPriorty = applicationinsightsCoreJs.MinChannelPriorty;
    exports.NotificationManager = applicationinsightsCoreJs.NotificationManager;
    exports.PerfEvent = applicationinsightsCoreJs.PerfEvent;
    exports.PerfManager = applicationinsightsCoreJs.PerfManager;
    exports.ProcessTelemetryContext = applicationinsightsCoreJs.ProcessTelemetryContext;
    exports.Undefined = applicationinsightsCoreJs.strUndefined;
    exports._InternalLogMessage = applicationinsightsCoreJs._InternalLogMessage;
    exports._InternalMessageId = applicationinsightsCoreJs._InternalMessageId;
    exports.__getRegisteredEvents = applicationinsightsCoreJs.__getRegisteredEvents;
    exports._throwInternal = applicationinsightsCoreJs._throwInternal;
    exports.addEventHandler = applicationinsightsCoreJs.addEventHandler;
    exports.addEventListeners = applicationinsightsCoreJs.addEventListeners;
    exports.addPageHideEventListener = applicationinsightsCoreJs.addPageHideEventListener;
    exports.addPageShowEventListener = applicationinsightsCoreJs.addPageShowEventListener;
    exports.addPageUnloadEventListener = applicationinsightsCoreJs.addPageUnloadEventListener;
    exports.areCookiesSupported = applicationinsightsCoreJs.areCookiesSupported;
    exports.arrForEach = applicationinsightsCoreJs.arrForEach;
    exports.arrIndexOf = applicationinsightsCoreJs.arrIndexOf;
    exports.arrMap = applicationinsightsCoreJs.arrMap;
    exports.arrReduce = applicationinsightsCoreJs.arrReduce;
    exports.attachEvent = applicationinsightsCoreJs.attachEvent;
    exports.cookieAvailable = applicationinsightsCoreJs.areCookiesSupported;
    exports.createCookieMgr = applicationinsightsCoreJs.createCookieMgr;
    exports.createEnumStyle = applicationinsightsCoreJs.createEnumStyle;
    exports.createProcessTelemetryContext = applicationinsightsCoreJs.createProcessTelemetryContext;
    exports.createTraceParent = applicationinsightsCoreJs.createTraceParent;
    exports.createUniqueNamespace = applicationinsightsCoreJs.createUniqueNamespace;
    exports.createUnloadHandlerContainer = applicationinsightsCoreJs.createUnloadHandlerContainer;
    exports.dateNow = applicationinsightsCoreJs.dateNow;
    exports.detachEvent = applicationinsightsCoreJs.detachEvent;
    exports.disallowsSameSiteNone = applicationinsightsCoreJs.uaDisallowsSameSiteNone;
    exports.doPerf = applicationinsightsCoreJs.doPerf;
    exports.dumpObj = applicationinsightsCoreJs.dumpObj;
    exports.eventOff = applicationinsightsCoreJs.eventOff;
    exports.eventOn = applicationinsightsCoreJs.eventOn;
    exports.findW3cTraceParent = applicationinsightsCoreJs.findW3cTraceParent;
    exports.formatTraceParent = applicationinsightsCoreJs.formatTraceParent;
    exports.generateW3CId = applicationinsightsCoreJs.generateW3CId;
    exports.getConsole = applicationinsightsCoreJs.getConsole;
    exports.getCrypto = applicationinsightsCoreJs.getCrypto;
    exports.getDocument = applicationinsightsCoreJs.getDocument;
    exports.getExceptionName = applicationinsightsCoreJs.getExceptionName;
    exports.getGlobal = applicationinsightsCoreJs.getGlobal;
    exports.getGlobalInst = applicationinsightsCoreJs.getGlobalInst;
    exports.getHistory = applicationinsightsCoreJs.getHistory;
    exports.getIEVersion = applicationinsightsCoreJs.getIEVersion;
    exports.getISOString = applicationinsightsCoreJs.toISOString;
    exports.getJSON = applicationinsightsCoreJs.getJSON;
    exports.getLocation = applicationinsightsCoreJs.getLocation;
    exports.getMsCrypto = applicationinsightsCoreJs.getMsCrypto;
    exports.getNavigator = applicationinsightsCoreJs.getNavigator;
    exports.getPerformance = applicationinsightsCoreJs.getPerformance;
    exports.getSetValue = applicationinsightsCoreJs.getSetValue;
    exports.getWindow = applicationinsightsCoreJs.getWindow;
    exports.hasDocument = applicationinsightsCoreJs.hasDocument;
    exports.hasHistory = applicationinsightsCoreJs.hasHistory;
    exports.hasJSON = applicationinsightsCoreJs.hasJSON;
    exports.hasNavigator = applicationinsightsCoreJs.hasNavigator;
    exports.hasOwnProperty = applicationinsightsCoreJs.hasOwnProperty;
    exports.hasWindow = applicationinsightsCoreJs.hasWindow;
    exports.isArray = applicationinsightsCoreJs.isArray;
    exports.isBeaconsSupported = applicationinsightsCoreJs.isBeaconsSupported;
    exports.isBoolean = applicationinsightsCoreJs.isBoolean;
    exports.isDate = applicationinsightsCoreJs.isDate;
    exports.isError = applicationinsightsCoreJs.isError;
    exports.isFetchSupported = applicationinsightsCoreJs.isFetchSupported;
    exports.isFunction = applicationinsightsCoreJs.isFunction;
    exports.isIE = applicationinsightsCoreJs.isIE;
    exports.isNotTruthy = applicationinsightsCoreJs.isNotTruthy;
    exports.isNullOrUndefined = applicationinsightsCoreJs.isNullOrUndefined;
    exports.isNumber = applicationinsightsCoreJs.isNumber;
    exports.isObject = applicationinsightsCoreJs.isObject;
    exports.isReactNative = applicationinsightsCoreJs.isReactNative;
    exports.isSampledFlag = applicationinsightsCoreJs.isSampledFlag;
    exports.isString = applicationinsightsCoreJs.isString;
    exports.isTruthy = applicationinsightsCoreJs.isTruthy;
    exports.isTypeof = applicationinsightsCoreJs.isTypeof;
    exports.isUndefined = applicationinsightsCoreJs.isUndefined;
    exports.isValidSpanId = applicationinsightsCoreJs.isValidSpanId;
    exports.isValidTraceId = applicationinsightsCoreJs.isValidTraceId;
    exports.isValidTraceParent = applicationinsightsCoreJs.isValidTraceParent;
    exports.isXhrSupported = applicationinsightsCoreJs.isXhrSupported;
    exports.mergeEvtNamespace = applicationinsightsCoreJs.mergeEvtNamespace;
    exports.newGuid = applicationinsightsCoreJs.newGuid;
    exports.newId = applicationinsightsCoreJs.newId;
    exports.normalizeJsName = applicationinsightsCoreJs.normalizeJsName;
    exports.objCreate = applicationinsightsCoreJs.objCreate;
    exports.objDefineAccessors = applicationinsightsCoreJs.objDefineAccessors;
    exports.objForEachKey = applicationinsightsCoreJs.objForEachKey;
    exports.objFreeze = applicationinsightsCoreJs.objFreeze;
    exports.objKeys = applicationinsightsCoreJs.objKeys;
    exports.objSeal = applicationinsightsCoreJs.objSeal;
    exports.optimizeObject = applicationinsightsCoreJs.optimizeObject;
    exports.parseTraceParent = applicationinsightsCoreJs.parseTraceParent;
    exports.perfNow = applicationinsightsCoreJs.perfNow;
    exports.proxyAssign = applicationinsightsCoreJs.proxyAssign;
    exports.proxyFunctionAs = applicationinsightsCoreJs.proxyFunctionAs;
    exports.proxyFunctions = applicationinsightsCoreJs.proxyFunctions;
    exports.random32 = applicationinsightsCoreJs.random32;
    exports.randomValue = applicationinsightsCoreJs.randomValue;
    exports.removeEventHandler = applicationinsightsCoreJs.removeEventHandler;
    exports.removeEventListeners = applicationinsightsCoreJs.removeEventListeners;
    exports.removePageHideEventListener = applicationinsightsCoreJs.removePageHideEventListener;
    exports.removePageShowEventListener = applicationinsightsCoreJs.removePageShowEventListener;
    exports.removePageUnloadEventListener = applicationinsightsCoreJs.removePageUnloadEventListener;
    exports.safeGetCookieMgr = applicationinsightsCoreJs.safeGetCookieMgr;
    exports.safeGetLogger = applicationinsightsCoreJs.safeGetLogger;
    exports.setEnableEnvMocks = applicationinsightsCoreJs.setEnableEnvMocks;
    exports.setValue = applicationinsightsCoreJs.setValue;
    exports.strContains = applicationinsightsCoreJs.strContains;
    exports.strEndsWith = applicationinsightsCoreJs.strEndsWith;
    exports.strFunction = applicationinsightsCoreJs.strFunction;
    exports.strObject = applicationinsightsCoreJs.strObject;
    exports.strPrototype = applicationinsightsCoreJs.strPrototype;
    exports.strStartsWith = applicationinsightsCoreJs.strStartsWith;
    exports.strTrim = applicationinsightsCoreJs.strTrim;
    exports.strUndefined = applicationinsightsCoreJs.strUndefined;
    exports.throwError = applicationinsightsCoreJs.throwError;
    exports.toISOString = applicationinsightsCoreJs.toISOString;
    exports.useXDomainRequest = applicationinsightsCoreJs.useXDomainRequest;
    exports.AppInsightsCore = AppInsightsCore;
    exports.BaseCore = BaseCore;
    exports.CoreUtils = CoreUtils;
    exports.ESPromise = ESPromise;
    exports.ESPromiseScheduler = ESPromiseScheduler;
    exports.EventLatency = EventLatency;
    exports.EventPersistence = EventPersistence;
    exports.EventPropertyType = EventPropertyType;
    exports.FullVersionString = FullVersionString;
    exports.TraceLevel = TraceLevel;
    exports.Utils = Utils;
    exports.ValueKind = ValueKind;
    exports.ValueSanitizer = ValueSanitizer;
    exports.Version = Version;
    exports._ExtendedInternalMessageId = _ExtendedInternalMessageId;
    exports.createGuid = createGuid;
    exports.deleteCookie = deleteCookie;
    exports.disableCookies = disableCookies;
    exports.extend = extend;
    exports.getCommonSchemaMetaData = getCommonSchemaMetaData;
    exports.getCookie = getCookie;
    exports.getCookieValue = getCookieValue;
    exports.getFieldValueType = getFieldValueType;
    exports.getTenantId = getTenantId;
    exports.getTime = getTime;
    exports.isArrayValid = isArrayValid;
    exports.isChromium = isChromium;
    exports.isDocumentObjectAvailable = isDocumentObjectAvailable;
    exports.isLatency = isLatency;
    exports.isUint8ArrayAvailable = isUint8ArrayAvailable;
    exports.isValueAssigned = isValueAssigned;
    exports.isValueKind = isValueKind;
    exports.isWindowObjectAvailable = isWindowObjectAvailable;
    exports.openXhr = openXhr;
    exports.sanitizeProperty = sanitizeProperty;
    exports.setCookie = setCookie;
    exports.setProcessTelemetryTimings = setProcessTelemetryTimings;

    (function(obj, prop, descriptor) { /* ai_es3_polyfil defineProperty */ var func = Object["defineProperty"]; if (func) { try { return func(obj, prop, descriptor); } catch(e) { /* IE8 defines defineProperty, but will throw */ } } if (descriptor && typeof descriptor.value !== undefined) { obj[prop] = descriptor.value; } return obj; })(exports, '__esModule', { value: true });

}));
//# sourceMappingURL=ms.core.js.map


/***/ }),

/***/ 7855:
/***/ (function(__unused_webpack_module, exports) {

/*!
 * Application Insights JavaScript SDK - Core, 2.8.4
 * Copyright (c) Microsoft and contributors. All rights reserved.
 */
(function (global, factory) {
     true ? factory(exports) :
    0;
})(this, (function (exports) { 'use strict';

    var MinChannelPriorty = 100;

    var strShimFunction = "function";
    var strShimObject = "object";
    var strShimUndefined = "undefined";
    var strShimPrototype = "prototype";
    var strShimHasOwnProperty = "hasOwnProperty";
    var ObjClass = Object;
    var ObjProto = ObjClass[strShimPrototype];
    var ObjAssign = ObjClass["assign"];
    var ObjCreate = ObjClass["create"];
    var ObjDefineProperty = ObjClass["defineProperty"];
    var ObjHasOwnProperty = ObjProto[strShimHasOwnProperty];

    var _cachedGlobal = null;
    function getGlobal(useCached) {
        if (useCached === void 0) { useCached = true; }
        if (!_cachedGlobal || !useCached) {
            if (typeof globalThis !== strShimUndefined && globalThis) {
                _cachedGlobal = globalThis;
            }
            if (typeof self !== strShimUndefined && self) {
                _cachedGlobal = self;
            }
            if (typeof window !== strShimUndefined && window) {
                _cachedGlobal = window;
            }
            if (typeof global !== strShimUndefined && global) {
                _cachedGlobal = global;
            }
        }
        return _cachedGlobal;
    }
    function throwTypeError(message) {
        throw new TypeError(message);
    }
    function objCreateFn(obj) {
        var func = ObjCreate;
        if (func) {
            return func(obj);
        }
        if (obj == null) {
            return {};
        }
        var type = typeof obj;
        if (type !== strShimObject && type !== strShimFunction) {
            throwTypeError("Object prototype may only be an Object:" + obj);
        }
        function tmpFunc() { }
        tmpFunc[strShimPrototype] = obj;
        return new tmpFunc();
    }

    (getGlobal() || {})["Symbol"];
    (getGlobal() || {})["Reflect"];
    var extendStaticsFn = function (d, b) {
        extendStaticsFn = ObjClass["setPrototypeOf"] ||
            ({ __proto__: [] } instanceof Array && function (d, b) {
                d.__proto__ = b;
            }) ||
            function (d, b) {
                for (var p in b) {
                    if (b[strShimHasOwnProperty](p)) {
                        d[p] = b[p];
                    }
                }
            };
        return extendStaticsFn(d, b);
    };
    function __extendsFn(d, b) {
        if (typeof b !== strShimFunction && b !== null) {
            throwTypeError("Class extends value " + String(b) + " is not a constructor or null");
        }
        extendStaticsFn(d, b);
        function __() {
            this.constructor = d;
        }
        d[strShimPrototype] = b === null ? objCreateFn(b) : (__[strShimPrototype] = b[strShimPrototype], new __());
    }
    function __spreadArrayFn(to, from) {
        for (var i = 0, il = from.length, j = to.length; i < il; i++, j++) {
            to[j] = from[i];
        }
        return to;
    }

    var strEmpty = "";
    var strProcessTelemetry = "processTelemetry";
    var strPriority = "priority";
    var strSetNextPlugin = "setNextPlugin";
    var strIsInitialized = "isInitialized";
    var strTeardown = "teardown";
    var strCore = "core";
    var strUpdate = "update";
    var strDisabled = "disabled";
    var strDoTeardown = "_doTeardown";
    var strProcessNext = "processNext";
    var strResume = "resume";
    var strPause = "pause";
    var strNotificationListener = "NotificationListener";
    var strAddNotificationListener = "add" + strNotificationListener;
    var strRemoveNotificationListener = "remove" + strNotificationListener;
    var strEventsSent = "eventsSent";
    var strEventsDiscarded = "eventsDiscarded";
    var strEventsSendRequest = "eventsSendRequest";
    var strPerfEvent = "perfEvent";

    var strToISOString = "toISOString";
    var cStrEndsWith = "endsWith";
    var cStrStartsWith = "startsWith";
    var strIndexOf = "indexOf";
    var strMap = "map";
    var strReduce = "reduce";
    var cStrTrim = "trim";
    var strToString = "toString";
    var str__Proto$1 = "__proto__";
    var strConstructor = "constructor";
    var _objDefineProperty$1 = ObjDefineProperty;
    var _objFreeze = ObjClass.freeze;
    var _objSeal = ObjClass.seal;
    var _objKeys = ObjClass.keys;
    var StringProto = String[strShimPrototype];
    var _strTrim = StringProto[cStrTrim];
    var _strEndsWith = StringProto[cStrEndsWith];
    var _strStartsWith = StringProto[cStrStartsWith];
    var DateProto = Date[strShimPrototype];
    var _dataToISOString = DateProto[strToISOString];
    var _isArray = Array.isArray;
    var _objToString = ObjProto[strToString];
    var _fnToString = ObjHasOwnProperty[strToString];
    var _objFunctionString = _fnToString.call(ObjClass);
    var rCamelCase = /-([a-z])/g;
    var rNormalizeInvalid = /([^\w\d_$])/g;
    var rLeadingNumeric = /^(\d+[\w\d_$])/;
    var _objGetPrototypeOf$1 = Object["getPrototypeOf"];
    function _getObjProto$1(target) {
        if (target) {
            if (_objGetPrototypeOf$1) {
                return _objGetPrototypeOf$1(target);
            }
            var newProto = target[str__Proto$1] || target[strShimPrototype] || target[strConstructor];
            if (newProto) {
                return newProto;
            }
        }
        return null;
    }
    function objToString(obj) {
        return _objToString.call(obj);
    }
    function isTypeof(value, theType) {
        return typeof value === theType;
    }
    function isUndefined(value) {
        return value === undefined || typeof value === strShimUndefined;
    }
    function isNotUndefined(value) {
        return !isUndefined(value);
    }
    function isNullOrUndefined(value) {
        return (value === null || isUndefined(value));
    }
    function isNotNullOrUndefined(value) {
        return !isNullOrUndefined(value);
    }
    function hasOwnProperty(obj, prop) {
        return !!(obj && ObjHasOwnProperty.call(obj, prop));
    }
    function isObject(value) {
        return !!(value && typeof value === strShimObject);
    }
    function isFunction(value) {
        return !!(value && typeof value === strShimFunction);
    }
    function normalizeJsName(name) {
        var value = name;
        if (value && isString(value)) {
            value = value.replace(rCamelCase, function (_all, letter) {
                return letter.toUpperCase();
            });
            value = value.replace(rNormalizeInvalid, "_");
            value = value.replace(rLeadingNumeric, function (_all, match) {
                return "_" + match;
            });
        }
        return value;
    }
    function objForEachKey(target, callbackfn) {
        if (target) {
            for (var prop in target) {
                if (ObjHasOwnProperty.call(target, prop)) {
                    callbackfn.call(target, prop, target[prop]);
                }
            }
        }
    }
    function strEndsWith(value, search) {
        var result = false;
        if (value && search && !(result = value === search)) {
            result = _strEndsWith ? value[cStrEndsWith](search) : _strEndsWithPoly(value, search);
        }
        return result;
    }
    function _strEndsWithPoly(value, search) {
        var result = false;
        var searchLen = search ? search.length : 0;
        var valLen = value ? value.length : 0;
        if (searchLen && valLen && valLen >= searchLen && !(result = value === search)) {
            var pos = valLen - 1;
            for (var lp = searchLen - 1; lp >= 0; lp--) {
                if (value[pos] != search[lp]) {
                    return false;
                }
                pos--;
            }
            result = true;
        }
        return result;
    }
    function strStartsWith(value, checkValue) {
        var result = false;
        if (value && checkValue && !(result = value === checkValue)) {
            result = _strStartsWith ? value[cStrStartsWith](checkValue) : _strStartsWithPoly(value, checkValue);
        }
        return result;
    }
    function _strStartsWithPoly(value, checkValue) {
        var result = false;
        var chkLen = checkValue ? checkValue.length : 0;
        if (value && chkLen && value.length >= chkLen && !(result = value === checkValue)) {
            for (var lp = 0; lp < chkLen; lp++) {
                if (value[lp] !== checkValue[lp]) {
                    return false;
                }
            }
            result = true;
        }
        return result;
    }
    function strContains(value, search) {
        if (value && search) {
            return value.indexOf(search) !== -1;
        }
        return false;
    }
    function isDate(obj) {
        return !!(obj && _objToString.call(obj) === "[object Date]");
    }
    var isArray = _isArray || _isArrayPoly;
    function _isArrayPoly(obj) {
        return !!(obj && _objToString.call(obj) === "[object Array]");
    }
    function isError(obj) {
        return !!(obj && _objToString.call(obj) === "[object Error]");
    }
    function isString(value) {
        return typeof value === "string";
    }
    function isNumber(value) {
        return typeof value === "number";
    }
    function isBoolean(value) {
        return typeof value === "boolean";
    }
    function isSymbol(value) {
        return typeof value === "symbol";
    }
    function isPlainObject(value) {
        var result = false;
        if (value && typeof value === "object") {
            var proto = _objGetPrototypeOf$1 ? _objGetPrototypeOf$1(value) : _getObjProto$1(value);
            if (!proto) {
                result = true;
            }
            else {
                if (proto[strConstructor] && ObjHasOwnProperty.call(proto, strConstructor)) {
                    proto = proto[strConstructor];
                }
                result = typeof proto === strShimFunction && _fnToString.call(proto) === _objFunctionString;
            }
        }
        return result;
    }
    function toISOString(date) {
        if (date) {
            return _dataToISOString ? date[strToISOString]() : _toISOStringPoly(date);
        }
    }
    function _toISOStringPoly(date) {
        if (date && date.getUTCFullYear) {
            var pad = function (num) {
                var r = String(num);
                if (r.length === 1) {
                    r = "0" + r;
                }
                return r;
            };
            return date.getUTCFullYear()
                + "-" + pad(date.getUTCMonth() + 1)
                + "-" + pad(date.getUTCDate())
                + "T" + pad(date.getUTCHours())
                + ":" + pad(date.getUTCMinutes())
                + ":" + pad(date.getUTCSeconds())
                + "." + String((date.getUTCMilliseconds() / 1000).toFixed(3)).slice(2, 5)
                + "Z";
        }
    }
    function arrForEach(arr, callbackfn, thisArg) {
        var len = arr.length;
        try {
            for (var idx = 0; idx < len; idx++) {
                if (idx in arr) {
                    if (callbackfn.call(thisArg || arr, arr[idx], idx, arr) === -1) {
                        break;
                    }
                }
            }
        }
        catch (e) {
        }
    }
    function arrIndexOf(arr, searchElement, fromIndex) {
        if (arr) {
            if (arr[strIndexOf]) {
                return arr[strIndexOf](searchElement, fromIndex);
            }
            var len = arr.length;
            var from = fromIndex || 0;
            try {
                for (var lp = Math.max(from >= 0 ? from : len - Math.abs(from), 0); lp < len; lp++) {
                    if (lp in arr && arr[lp] === searchElement) {
                        return lp;
                    }
                }
            }
            catch (e) {
            }
        }
        return -1;
    }
    function arrMap(arr, callbackfn, thisArg) {
        var results;
        if (arr) {
            if (arr[strMap]) {
                return arr[strMap](callbackfn, thisArg);
            }
            var len = arr.length;
            var _this = thisArg || arr;
            results = new Array(len);
            try {
                for (var lp = 0; lp < len; lp++) {
                    if (lp in arr) {
                        results[lp] = callbackfn.call(_this, arr[lp], arr);
                    }
                }
            }
            catch (e) {
            }
        }
        return results;
    }
    function arrReduce(arr, callbackfn, initialValue) {
        var value;
        if (arr) {
            if (arr[strReduce]) {
                return arr[strReduce](callbackfn, initialValue);
            }
            var len = arr.length;
            var lp = 0;
            if (arguments.length >= 3) {
                value = arguments[2];
            }
            else {
                while (lp < len && !(lp in arr)) {
                    lp++;
                }
                value = arr[lp++];
            }
            while (lp < len) {
                if (lp in arr) {
                    value = callbackfn(value, arr[lp], lp, arr);
                }
                lp++;
            }
        }
        return value;
    }
    function strTrim(str) {
        if (str) {
            str = (_strTrim && str[cStrTrim]) ? str[cStrTrim]() : (str.replace ? str.replace(/^\s+|\s+$/g, "") : str);
        }
        return str;
    }
    var _objKeysHasDontEnumBug = !({ toString: null }).propertyIsEnumerable("toString");
    var _objKeysDontEnums = [
        "toString",
        "toLocaleString",
        "valueOf",
        "hasOwnProperty",
        "isPrototypeOf",
        "propertyIsEnumerable",
        "constructor"
    ];
    function objKeys(obj) {
        var objType = typeof obj;
        if (objType !== strShimFunction && (objType !== strShimObject || obj === null)) {
            throwTypeError("objKeys called on non-object");
        }
        if (!_objKeysHasDontEnumBug && _objKeys) {
            return _objKeys(obj);
        }
        var result = [];
        for (var prop in obj) {
            if (obj && ObjHasOwnProperty.call(obj, prop)) {
                result.push(prop);
            }
        }
        if (_objKeysHasDontEnumBug) {
            var dontEnumsLength = _objKeysDontEnums.length;
            for (var lp = 0; lp < dontEnumsLength; lp++) {
                if (obj && ObjHasOwnProperty.call(obj, _objKeysDontEnums[lp])) {
                    result.push(_objKeysDontEnums[lp]);
                }
            }
        }
        return result;
    }
    function objDefineAccessors(target, prop, getProp, setProp) {
        if (_objDefineProperty$1) {
            try {
                var descriptor = {
                    enumerable: true,
                    configurable: true
                };
                if (getProp) {
                    descriptor.get = getProp;
                }
                if (setProp) {
                    descriptor.set = setProp;
                }
                _objDefineProperty$1(target, prop, descriptor);
                return true;
            }
            catch (e) {
            }
        }
        return false;
    }
    function _doNothing(value) {
        return value;
    }
    function deepFreeze(obj) {
        if (_objFreeze) {
            objForEachKey(obj, function (name, value) {
                if (isArray(value) || isObject(value)) {
                    _objFreeze(value);
                }
            });
        }
        return objFreeze(obj);
    }
    var objFreeze = _objFreeze || _doNothing;
    var objSeal = _objSeal || _doNothing;
    function dateNow() {
        var dt = Date;
        return dt.now ? dt.now() : new dt().getTime();
    }
    function getExceptionName(object) {
        if (isError(object)) {
            return object.name;
        }
        return strEmpty;
    }
    function setValue(target, field, value, valChk, srcChk) {
        var theValue = value;
        if (target) {
            theValue = target[field];
            if (theValue !== value && (!srcChk || srcChk(theValue)) && (!valChk || valChk(value))) {
                theValue = value;
                target[field] = theValue;
            }
        }
        return theValue;
    }
    function getSetValue(target, field, defValue) {
        var theValue;
        if (target) {
            theValue = target[field];
            if (!theValue && isNullOrUndefined(theValue)) {
                theValue = !isUndefined(defValue) ? defValue : {};
                target[field] = theValue;
            }
        }
        else {
            theValue = !isUndefined(defValue) ? defValue : {};
        }
        return theValue;
    }
    function isNotTruthy(value) {
        return !value;
    }
    function isTruthy(value) {
        return !!value;
    }
    function throwError(message) {
        throw new Error(message);
    }
    function _createProxyFunction(source, funcName) {
        var srcFunc = null;
        var src = null;
        if (isFunction(source)) {
            srcFunc = source;
        }
        else {
            src = source;
        }
        return function () {
            var originalArguments = arguments;
            if (srcFunc) {
                src = srcFunc();
            }
            if (src) {
                return src[funcName].apply(src, originalArguments);
            }
        };
    }
    function proxyAssign(target, source, chkSet) {
        if (target && source && isObject(target) && isObject(source)) {
            var _loop_1 = function (field) {
                if (isString(field)) {
                    var value = source[field];
                    if (isFunction(value)) {
                        if (!chkSet || chkSet(field, true, source, target)) {
                            target[field] = _createProxyFunction(source, field);
                        }
                    }
                    else if (!chkSet || chkSet(field, false, source, target)) {
                        if (hasOwnProperty(target, field)) {
                            delete target[field];
                        }
                        if (!objDefineAccessors(target, field, function () {
                            return source[field];
                        }, function (theValue) {
                            source[field] = theValue;
                        })) {
                            target[field] = value;
                        }
                    }
                }
            };
            for (var field in source) {
                _loop_1(field);
            }
        }
        return target;
    }
    function proxyFunctionAs(target, name, source, theFunc, overwriteTarget) {
        if (target && name && source) {
            if (overwriteTarget !== false || isUndefined(target[name])) {
                target[name] = _createProxyFunction(source, theFunc);
            }
        }
    }
    function proxyFunctions(target, source, functionsToProxy, overwriteTarget) {
        if (target && source && isObject(target) && isArray(functionsToProxy)) {
            arrForEach(functionsToProxy, function (theFuncName) {
                if (isString(theFuncName)) {
                    proxyFunctionAs(target, theFuncName, source, theFuncName, overwriteTarget);
                }
            });
        }
        return target;
    }
    function createClassFromInterface(defaults) {
        return /** @class */ (function () {
            function class_1() {
                var _this_1 = this;
                if (defaults) {
                    objForEachKey(defaults, function (field, value) {
                        _this_1[field] = value;
                    });
                }
            }
            return class_1;
        }());
    }
    function optimizeObject(theObject) {
        if (theObject && ObjAssign) {
            theObject = ObjClass(ObjAssign({}, theObject));
        }
        return theObject;
    }
    function objExtend(obj1, obj2, obj3, obj4, obj5, obj6) {
        var theArgs = arguments;
        var extended = theArgs[0] || {};
        var argLen = theArgs.length;
        var deep = false;
        var idx = 1;
        if (argLen > 0 && isBoolean(extended)) {
            deep = extended;
            extended = theArgs[idx] || {};
            idx++;
        }
        if (!isObject(extended)) {
            extended = {};
        }
        for (; idx < argLen; idx++) {
            var arg = theArgs[idx];
            var isArgArray = isArray(arg);
            var isArgObj = isObject(arg);
            for (var prop in arg) {
                var propOk = (isArgArray && (prop in arg)) || (isArgObj && (ObjHasOwnProperty.call(arg, prop)));
                if (!propOk) {
                    continue;
                }
                var newValue = arg[prop];
                var isNewArray = void 0;
                if (deep && newValue && ((isNewArray = isArray(newValue)) || isPlainObject(newValue))) {
                    var clone = extended[prop];
                    if (isNewArray) {
                        if (!isArray(clone)) {
                            clone = [];
                        }
                    }
                    else if (!isPlainObject(clone)) {
                        clone = {};
                    }
                    newValue = objExtend(deep, clone, newValue);
                }
                if (newValue !== undefined) {
                    extended[prop] = newValue;
                }
            }
        }
        return extended;
    }

    function createEnumStyle(values) {
        var enumClass = {};
        objForEachKey(values, function (field, value) {
            enumClass[field] = value;
            enumClass[value] = field;
        });
        return deepFreeze(enumClass);
    }
    function createEnumMap(values) {
        var mapClass = {};
        objForEachKey(values, function (field, value) {
            mapClass[field] = field;
            mapClass[value] = field;
        });
        return deepFreeze(mapClass);
    }
    function createValueMap(values) {
        var mapClass = {};
        objForEachKey(values, function (field, value) {
            mapClass[field] = value[1];
            mapClass[value[0]] = value[1];
        });
        return deepFreeze(mapClass);
    }

    var EventsDiscardedReason = createEnumStyle({
        Unknown: 0 ,
        NonRetryableStatus: 1 ,
        InvalidEvent: 2 ,
        SizeLimitExceeded: 3 ,
        KillSwitch: 4 ,
        QueueFull: 5
    });

    /*!
     * Microsoft Dynamic Proto Utility, 1.1.6
     * Copyright (c) Microsoft and contributors. All rights reserved.
     */
    var Constructor = 'constructor';
    var Prototype = 'prototype';
    var strFunction = 'function';
    var DynInstFuncTable = '_dynInstFuncs';
    var DynProxyTag = '_isDynProxy';
    var DynClassName = '_dynClass';
    var DynClassNamePrefix = '_dynCls$';
    var DynInstChkTag = '_dynInstChk';
    var DynAllowInstChkTag = DynInstChkTag;
    var DynProtoDefaultOptions = '_dfOpts';
    var UnknownValue = '_unknown_';
    var str__Proto = "__proto__";
    var DynProtoBaseProto = "_dyn" + str__Proto;
    var DynProtoCurrent = "_dynInstProto";
    var strUseBaseInst = 'useBaseInst';
    var strSetInstFuncs = 'setInstFuncs';
    var Obj = Object;
    var _objGetPrototypeOf = Obj["getPrototypeOf"];
    var _objGetOwnProps = Obj["getOwnPropertyNames"];
    var _dynamicNames = 0;
    function _hasOwnProperty(obj, prop) {
        return obj && Obj[Prototype].hasOwnProperty.call(obj, prop);
    }
    function _isObjectOrArrayPrototype(target) {
        return target && (target === Obj[Prototype] || target === Array[Prototype]);
    }
    function _isObjectArrayOrFunctionPrototype(target) {
        return _isObjectOrArrayPrototype(target) || target === Function[Prototype];
    }
    function _getObjProto(target) {
        var newProto;
        if (target) {
            if (_objGetPrototypeOf) {
                return _objGetPrototypeOf(target);
            }
            var curProto = target[str__Proto] || target[Prototype] || (target[Constructor] ? target[Constructor][Prototype] : null);
            newProto = target[DynProtoBaseProto] || curProto;
            if (!_hasOwnProperty(target, DynProtoBaseProto)) {
                delete target[DynProtoCurrent];
                newProto = target[DynProtoBaseProto] = target[DynProtoCurrent] || target[DynProtoBaseProto];
                target[DynProtoCurrent] = curProto;
            }
        }
        return newProto;
    }
    function _forEachProp(target, func) {
        var props = [];
        if (_objGetOwnProps) {
            props = _objGetOwnProps(target);
        }
        else {
            for (var name_1 in target) {
                if (typeof name_1 === "string" && _hasOwnProperty(target, name_1)) {
                    props.push(name_1);
                }
            }
        }
        if (props && props.length > 0) {
            for (var lp = 0; lp < props.length; lp++) {
                func(props[lp]);
            }
        }
    }
    function _isDynamicCandidate(target, funcName, skipOwn) {
        return (funcName !== Constructor && typeof target[funcName] === strFunction && (skipOwn || _hasOwnProperty(target, funcName)));
    }
    function _throwTypeError(message) {
        throw new TypeError("DynamicProto: " + message);
    }
    function _getInstanceFuncs(thisTarget) {
        var instFuncs = {};
        _forEachProp(thisTarget, function (name) {
            if (!instFuncs[name] && _isDynamicCandidate(thisTarget, name, false)) {
                instFuncs[name] = thisTarget[name];
            }
        });
        return instFuncs;
    }
    function _hasVisited(values, value) {
        for (var lp = values.length - 1; lp >= 0; lp--) {
            if (values[lp] === value) {
                return true;
            }
        }
        return false;
    }
    function _getBaseFuncs(classProto, thisTarget, instFuncs, useBaseInst) {
        function _instFuncProxy(target, funcHost, funcName) {
            var theFunc = funcHost[funcName];
            if (theFunc[DynProxyTag] && useBaseInst) {
                var instFuncTable = target[DynInstFuncTable] || {};
                if (instFuncTable[DynAllowInstChkTag] !== false) {
                    theFunc = (instFuncTable[funcHost[DynClassName]] || {})[funcName] || theFunc;
                }
            }
            return function () {
                return theFunc.apply(target, arguments);
            };
        }
        var baseFuncs = {};
        _forEachProp(instFuncs, function (name) {
            baseFuncs[name] = _instFuncProxy(thisTarget, instFuncs, name);
        });
        var baseProto = _getObjProto(classProto);
        var visited = [];
        while (baseProto && !_isObjectArrayOrFunctionPrototype(baseProto) && !_hasVisited(visited, baseProto)) {
            _forEachProp(baseProto, function (name) {
                if (!baseFuncs[name] && _isDynamicCandidate(baseProto, name, !_objGetPrototypeOf)) {
                    baseFuncs[name] = _instFuncProxy(thisTarget, baseProto, name);
                }
            });
            visited.push(baseProto);
            baseProto = _getObjProto(baseProto);
        }
        return baseFuncs;
    }
    function _getInstFunc(target, funcName, proto, currentDynProtoProxy) {
        var instFunc = null;
        if (target && _hasOwnProperty(proto, DynClassName)) {
            var instFuncTable = target[DynInstFuncTable] || {};
            instFunc = (instFuncTable[proto[DynClassName]] || {})[funcName];
            if (!instFunc) {
                _throwTypeError("Missing [" + funcName + "] " + strFunction);
            }
            if (!instFunc[DynInstChkTag] && instFuncTable[DynAllowInstChkTag] !== false) {
                var canAddInst = !_hasOwnProperty(target, funcName);
                var objProto = _getObjProto(target);
                var visited = [];
                while (canAddInst && objProto && !_isObjectArrayOrFunctionPrototype(objProto) && !_hasVisited(visited, objProto)) {
                    var protoFunc = objProto[funcName];
                    if (protoFunc) {
                        canAddInst = (protoFunc === currentDynProtoProxy);
                        break;
                    }
                    visited.push(objProto);
                    objProto = _getObjProto(objProto);
                }
                try {
                    if (canAddInst) {
                        target[funcName] = instFunc;
                    }
                    instFunc[DynInstChkTag] = 1;
                }
                catch (e) {
                    instFuncTable[DynAllowInstChkTag] = false;
                }
            }
        }
        return instFunc;
    }
    function _getProtoFunc(funcName, proto, currentDynProtoProxy) {
        var protoFunc = proto[funcName];
        if (protoFunc === currentDynProtoProxy) {
            protoFunc = _getObjProto(proto)[funcName];
        }
        if (typeof protoFunc !== strFunction) {
            _throwTypeError("[" + funcName + "] is not a " + strFunction);
        }
        return protoFunc;
    }
    function _populatePrototype(proto, className, target, baseInstFuncs, setInstanceFunc) {
        function _createDynamicPrototype(proto, funcName) {
            var dynProtoProxy = function () {
                var instFunc = _getInstFunc(this, funcName, proto, dynProtoProxy) || _getProtoFunc(funcName, proto, dynProtoProxy);
                return instFunc.apply(this, arguments);
            };
            dynProtoProxy[DynProxyTag] = 1;
            return dynProtoProxy;
        }
        if (!_isObjectOrArrayPrototype(proto)) {
            var instFuncTable = target[DynInstFuncTable] = target[DynInstFuncTable] || {};
            var instFuncs_1 = instFuncTable[className] = (instFuncTable[className] || {});
            if (instFuncTable[DynAllowInstChkTag] !== false) {
                instFuncTable[DynAllowInstChkTag] = !!setInstanceFunc;
            }
            _forEachProp(target, function (name) {
                if (_isDynamicCandidate(target, name, false) && target[name] !== baseInstFuncs[name]) {
                    instFuncs_1[name] = target[name];
                    delete target[name];
                    if (!_hasOwnProperty(proto, name) || (proto[name] && !proto[name][DynProxyTag])) {
                        proto[name] = _createDynamicPrototype(proto, name);
                    }
                }
            });
        }
    }
    function _checkPrototype(classProto, thisTarget) {
        if (_objGetPrototypeOf) {
            var visited = [];
            var thisProto = _getObjProto(thisTarget);
            while (thisProto && !_isObjectArrayOrFunctionPrototype(thisProto) && !_hasVisited(visited, thisProto)) {
                if (thisProto === classProto) {
                    return true;
                }
                visited.push(thisProto);
                thisProto = _getObjProto(thisProto);
            }
            return false;
        }
        return true;
    }
    function _getObjName(target, unknownValue) {
        if (_hasOwnProperty(target, Prototype)) {
            return target.name || unknownValue || UnknownValue;
        }
        return (((target || {})[Constructor]) || {}).name || unknownValue || UnknownValue;
    }
    function dynamicProto(theClass, target, delegateFunc, options) {
        if (!_hasOwnProperty(theClass, Prototype)) {
            _throwTypeError("theClass is an invalid class definition.");
        }
        var classProto = theClass[Prototype];
        if (!_checkPrototype(classProto, target)) {
            _throwTypeError("[" + _getObjName(theClass) + "] is not in class hierarchy of [" + _getObjName(target) + "]");
        }
        var className = null;
        if (_hasOwnProperty(classProto, DynClassName)) {
            className = classProto[DynClassName];
        }
        else {
            className = DynClassNamePrefix + _getObjName(theClass, "_") + "$" + _dynamicNames;
            _dynamicNames++;
            classProto[DynClassName] = className;
        }
        var perfOptions = dynamicProto[DynProtoDefaultOptions];
        var useBaseInst = !!perfOptions[strUseBaseInst];
        if (useBaseInst && options && options[strUseBaseInst] !== undefined) {
            useBaseInst = !!options[strUseBaseInst];
        }
        var instFuncs = _getInstanceFuncs(target);
        var baseFuncs = _getBaseFuncs(classProto, target, instFuncs, useBaseInst);
        delegateFunc(target, baseFuncs);
        var setInstanceFunc = !!_objGetPrototypeOf && !!perfOptions[strSetInstFuncs];
        if (setInstanceFunc && options) {
            setInstanceFunc = !!options[strSetInstFuncs];
        }
        _populatePrototype(classProto, className, target, instFuncs, setInstanceFunc !== false);
    }
    var perfDefaults = {
        setInstFuncs: true,
        useBaseInst: true
    };
    dynamicProto[DynProtoDefaultOptions] = perfDefaults;

    var strWindow = "window";
    var strDocument = "document";
    var strDocumentMode = "documentMode";
    var strNavigator = "navigator";
    var strHistory = "history";
    var strLocation = "location";
    var strConsole = "console";
    var strPerformance = "performance";
    var strJSON = "JSON";
    var strCrypto = "crypto";
    var strMsCrypto = "msCrypto";
    var strReactNative = "ReactNative";
    var strMsie = "msie";
    var strTrident = "trident/";
    var strXMLHttpRequest = "XMLHttpRequest";
    var _isTrident = null;
    var _navUserAgentCheck = null;
    var _enableMocks = false;
    var _useXDomainRequest = null;
    var _beaconsSupported = null;
    function _hasProperty(theClass, property) {
        var supported = false;
        if (theClass) {
            try {
                supported = property in theClass;
                if (!supported) {
                    var proto = theClass[strShimPrototype];
                    if (proto) {
                        supported = property in proto;
                    }
                }
            }
            catch (e) {
            }
            if (!supported) {
                try {
                    var tmp = new theClass();
                    supported = !isUndefined(tmp[property]);
                }
                catch (e) {
                }
            }
        }
        return supported;
    }
    function setEnableEnvMocks(enabled) {
        _enableMocks = enabled;
    }
    function getGlobalInst(name) {
        var gbl = getGlobal();
        if (gbl && gbl[name]) {
            return gbl[name];
        }
        if (name === strWindow && hasWindow()) {
            return window;
        }
        return null;
    }
    function hasWindow() {
        return Boolean(typeof window === strShimObject && window);
    }
    function getWindow() {
        if (hasWindow()) {
            return window;
        }
        return getGlobalInst(strWindow);
    }
    function hasDocument() {
        return Boolean(typeof document === strShimObject && document);
    }
    function getDocument() {
        if (hasDocument()) {
            return document;
        }
        return getGlobalInst(strDocument);
    }
    function hasNavigator() {
        return Boolean(typeof navigator === strShimObject && navigator);
    }
    function getNavigator() {
        if (hasNavigator()) {
            return navigator;
        }
        return getGlobalInst(strNavigator);
    }
    function hasHistory() {
        return Boolean(typeof history === strShimObject && history);
    }
    function getHistory() {
        if (hasHistory()) {
            return history;
        }
        return getGlobalInst(strHistory);
    }
    function getLocation(checkForMock) {
        if (checkForMock && _enableMocks) {
            var mockLocation = getGlobalInst("__mockLocation");
            if (mockLocation) {
                return mockLocation;
            }
        }
        if (typeof location === strShimObject && location) {
            return location;
        }
        return getGlobalInst(strLocation);
    }
    function getConsole() {
        if (typeof console !== strShimUndefined) {
            return console;
        }
        return getGlobalInst(strConsole);
    }
    function getPerformance() {
        return getGlobalInst(strPerformance);
    }
    function hasJSON() {
        return Boolean((typeof JSON === strShimObject && JSON) || getGlobalInst(strJSON) !== null);
    }
    function getJSON() {
        if (hasJSON()) {
            return JSON || getGlobalInst(strJSON);
        }
        return null;
    }
    function getCrypto() {
        return getGlobalInst(strCrypto);
    }
    function getMsCrypto() {
        return getGlobalInst(strMsCrypto);
    }
    function isReactNative() {
        var nav = getNavigator();
        if (nav && nav.product) {
            return nav.product === strReactNative;
        }
        return false;
    }
    function isIE() {
        var nav = getNavigator();
        if (nav && (nav.userAgent !== _navUserAgentCheck || _isTrident === null)) {
            _navUserAgentCheck = nav.userAgent;
            var userAgent = (_navUserAgentCheck || strEmpty).toLowerCase();
            _isTrident = (strContains(userAgent, strMsie) || strContains(userAgent, strTrident));
        }
        return _isTrident;
    }
    function getIEVersion(userAgentStr) {
        if (userAgentStr === void 0) { userAgentStr = null; }
        if (!userAgentStr) {
            var navigator_1 = getNavigator() || {};
            userAgentStr = navigator_1 ? (navigator_1.userAgent || strEmpty).toLowerCase() : strEmpty;
        }
        var ua = (userAgentStr || strEmpty).toLowerCase();
        if (strContains(ua, strMsie)) {
            var doc = getDocument() || {};
            return Math.max(parseInt(ua.split(strMsie)[1]), (doc[strDocumentMode] || 0));
        }
        else if (strContains(ua, strTrident)) {
            var tridentVer = parseInt(ua.split(strTrident)[1]);
            if (tridentVer) {
                return tridentVer + 4;
            }
        }
        return null;
    }
    function dumpObj(object) {
        var objectTypeDump = Object[strShimPrototype].toString.call(object);
        var propertyValueDump = strEmpty;
        if (objectTypeDump === "[object Error]") {
            propertyValueDump = "{ stack: '" + object.stack + "', message: '" + object.message + "', name: '" + object.name + "'";
        }
        else if (hasJSON()) {
            propertyValueDump = getJSON().stringify(object);
        }
        return objectTypeDump + propertyValueDump;
    }
    function isSafari(userAgentStr) {
        if (!userAgentStr || !isString(userAgentStr)) {
            var navigator_2 = getNavigator() || {};
            userAgentStr = navigator_2 ? (navigator_2.userAgent || strEmpty).toLowerCase() : strEmpty;
        }
        var ua = (userAgentStr || strEmpty).toLowerCase();
        return (ua.indexOf("safari") >= 0);
    }
    function isBeaconsSupported() {
        if (_beaconsSupported === null) {
            _beaconsSupported = hasNavigator() && Boolean(getNavigator().sendBeacon);
        }
        return _beaconsSupported;
    }
    function isFetchSupported(withKeepAlive) {
        var isSupported = false;
        try {
            isSupported = !!getGlobalInst("fetch");
            var request = getGlobalInst("Request");
            if (isSupported && withKeepAlive && request) {
                isSupported = _hasProperty(request, "keepalive");
            }
        }
        catch (e) {
        }
        return isSupported;
    }
    function useXDomainRequest() {
        if (_useXDomainRequest === null) {
            _useXDomainRequest = (typeof XDomainRequest !== strShimUndefined);
            if (_useXDomainRequest && isXhrSupported()) {
                _useXDomainRequest = _useXDomainRequest && !_hasProperty(getGlobalInst(strXMLHttpRequest), "withCredentials");
            }
        }
        return _useXDomainRequest;
    }
    function isXhrSupported() {
        var isSupported = false;
        try {
            var xmlHttpRequest = getGlobalInst(strXMLHttpRequest);
            isSupported = !!xmlHttpRequest;
        }
        catch (e) {
        }
        return isSupported;
    }
    function _getNamedValue(values, name) {
        if (values) {
            for (var i = 0; i < values.length; i++) {
                var value = values[i];
                if (value.name) {
                    if (value.name === name) {
                        return value;
                    }
                }
            }
        }
        return {};
    }
    function findMetaTag(name) {
        var doc = getDocument();
        if (doc && name) {
            return _getNamedValue(doc.querySelectorAll("meta"), name).content;
        }
        return null;
    }
    function findNamedServerTiming(name) {
        var value;
        var perf = getPerformance();
        if (perf) {
            var navPerf = perf.getEntriesByType("navigation") || [];
            value = _getNamedValue((navPerf.length > 0 ? navPerf[0] : {}).serverTiming, name).description;
        }
        return value;
    }

    var listenerFuncs = ["eventsSent", "eventsDiscarded", "eventsSendRequest", "perfEvent"];
    var _aiNamespace = null;
    var _debugListener;
    function _listenerProxyFunc(name, config) {
        return function () {
            var args = arguments;
            var dbgExt = getDebugExt(config);
            if (dbgExt) {
                var listener = dbgExt.listener;
                if (listener && listener[name]) {
                    listener[name].apply(listener, args);
                }
            }
        };
    }
    function _getExtensionNamespace() {
        var target = getGlobalInst("Microsoft");
        if (target) {
            _aiNamespace = target["ApplicationInsights"];
        }
        return _aiNamespace;
    }
    function getDebugExt(config) {
        var ns = _aiNamespace;
        if (!ns && config.disableDbgExt !== true) {
            ns = _aiNamespace || _getExtensionNamespace();
        }
        return ns ? ns["ChromeDbgExt"] : null;
    }
    function getDebugListener(config) {
        if (!_debugListener) {
            _debugListener = {};
            for (var lp = 0; lp < listenerFuncs.length; lp++) {
                _debugListener[listenerFuncs[lp]] = _listenerProxyFunc(listenerFuncs[lp], config);
            }
        }
        return _debugListener;
    }

    var AiNonUserActionablePrefix = "AI (Internal): ";
    var AiUserActionablePrefix = "AI: ";
    var AIInternalMessagePrefix = "AITR_";
    var strErrorToConsole = "errorToConsole";
    var strWarnToConsole = "warnToConsole";
    function _sanitizeDiagnosticText(text) {
        if (text) {
            return "\"" + text.replace(/\"/g, strEmpty) + "\"";
        }
        return strEmpty;
    }
    function _logToConsole(func, message) {
        var theConsole = getConsole();
        if (!!theConsole) {
            var logFunc = "log";
            if (theConsole[func]) {
                logFunc = func;
            }
            if (isFunction(theConsole[logFunc])) {
                theConsole[logFunc](message);
            }
        }
    }
    var _InternalLogMessage = /** @class */ (function () {
        function _InternalLogMessage(msgId, msg, isUserAct, properties) {
            if (isUserAct === void 0) { isUserAct = false; }
            var _self = this;
            _self.messageId = msgId;
            _self.message =
                (isUserAct ? AiUserActionablePrefix : AiNonUserActionablePrefix) +
                    msgId;
            var strProps = strEmpty;
            if (hasJSON()) {
                strProps = getJSON().stringify(properties);
            }
            var diagnosticText = (msg ? " message:" + _sanitizeDiagnosticText(msg) : strEmpty) +
                (properties ? " props:" + _sanitizeDiagnosticText(strProps) : strEmpty);
            _self.message += diagnosticText;
        }
        _InternalLogMessage.dataType = "MessageData";
        return _InternalLogMessage;
    }());
    function safeGetLogger(core, config) {
        return (core || {}).logger || new DiagnosticLogger(config);
    }
    var DiagnosticLogger = /** @class */ (function () {
        function DiagnosticLogger(config) {
            this.identifier = "DiagnosticLogger";
            this.queue = [];
            var _messageCount = 0;
            var _messageLogged = {};
            dynamicProto(DiagnosticLogger, this, function (_self) {
                if (isNullOrUndefined(config)) {
                    config = {};
                }
                _self.consoleLoggingLevel = function () { return _getConfigValue("loggingLevelConsole", 0); };
                _self.telemetryLoggingLevel = function () { return _getConfigValue("loggingLevelTelemetry", 1); };
                _self.maxInternalMessageLimit = function () { return _getConfigValue("maxMessageLimit", 25); };
                _self.enableDebugExceptions = function () { return _getConfigValue("enableDebugExceptions", false); };
                _self.throwInternal = function (severity, msgId, msg, properties, isUserAct) {
                    if (isUserAct === void 0) { isUserAct = false; }
                    var message = new _InternalLogMessage(msgId, msg, isUserAct, properties);
                    if (_self.enableDebugExceptions()) {
                        throw dumpObj(message);
                    }
                    else {
                        var logFunc = severity === 1  ? strErrorToConsole : strWarnToConsole;
                        if (!isUndefined(message.message)) {
                            var logLevel = _self.consoleLoggingLevel();
                            if (isUserAct) {
                                var messageKey = +message.messageId;
                                if (!_messageLogged[messageKey] && logLevel >= severity) {
                                    _self[logFunc](message.message);
                                    _messageLogged[messageKey] = true;
                                }
                            }
                            else {
                                if (logLevel >= severity) {
                                    _self[logFunc](message.message);
                                }
                            }
                            _self.logInternalMessage(severity, message);
                        }
                        else {
                            _debugExtMsg("throw" + (severity === 1  ? "Critical" : "Warning"), message);
                        }
                    }
                };
                _self.warnToConsole = function (message) {
                    _logToConsole("warn", message);
                    _debugExtMsg("warning", message);
                };
                _self.errorToConsole = function (message) {
                    _logToConsole("error", message);
                    _debugExtMsg("error", message);
                };
                _self.resetInternalMessageCount = function () {
                    _messageCount = 0;
                    _messageLogged = {};
                };
                _self.logInternalMessage = function (severity, message) {
                    if (_areInternalMessagesThrottled()) {
                        return;
                    }
                    var logMessage = true;
                    var messageKey = AIInternalMessagePrefix + message.messageId;
                    if (_messageLogged[messageKey]) {
                        logMessage = false;
                    }
                    else {
                        _messageLogged[messageKey] = true;
                    }
                    if (logMessage) {
                        if (severity <= _self.telemetryLoggingLevel()) {
                            _self.queue.push(message);
                            _messageCount++;
                            _debugExtMsg((severity === 1  ? "error" : "warn"), message);
                        }
                        if (_messageCount === _self.maxInternalMessageLimit()) {
                            var throttleLimitMessage = "Internal events throttle limit per PageView reached for this app.";
                            var throttleMessage = new _InternalLogMessage(23 , throttleLimitMessage, false);
                            _self.queue.push(throttleMessage);
                            if (severity === 1 ) {
                                _self.errorToConsole(throttleLimitMessage);
                            }
                            else {
                                _self.warnToConsole(throttleLimitMessage);
                            }
                        }
                    }
                };
                function _getConfigValue(name, defValue) {
                    var value = config[name];
                    if (!isNullOrUndefined(value)) {
                        return value;
                    }
                    return defValue;
                }
                function _areInternalMessagesThrottled() {
                    return _messageCount >= _self.maxInternalMessageLimit();
                }
                function _debugExtMsg(name, data) {
                    var dbgExt = getDebugExt(config);
                    if (dbgExt && dbgExt.diagLog) {
                        dbgExt.diagLog(name, data);
                    }
                }
            });
        }
        return DiagnosticLogger;
    }());
    function _getLogger(logger) {
        return (logger || new DiagnosticLogger());
    }
    function _throwInternal(logger, severity, msgId, msg, properties, isUserAct) {
        if (isUserAct === void 0) { isUserAct = false; }
        (logger || new DiagnosticLogger()).throwInternal(severity, msgId, msg, properties, isUserAct);
    }
    function _warnToConsole(logger, message) {
        _getLogger(logger).warnToConsole(message);
    }
    function _logInternalMessage(logger, severity, message) {
        _getLogger(logger).logInternalMessage(severity, message);
    }

    var strExecutionContextKey = "ctx";
    var _defaultPerfManager = null;
    var PerfEvent = /** @class */ (function () {
        function PerfEvent(name, payloadDetails, isAsync) {
            var _self = this;
            var accessorDefined = false;
            _self.start = dateNow();
            _self.name = name;
            _self.isAsync = isAsync;
            _self.isChildEvt = function () { return false; };
            if (isFunction(payloadDetails)) {
                var theDetails_1;
                accessorDefined = objDefineAccessors(_self, "payload", function () {
                    if (!theDetails_1 && isFunction(payloadDetails)) {
                        theDetails_1 = payloadDetails();
                        payloadDetails = null;
                    }
                    return theDetails_1;
                });
            }
            _self.getCtx = function (key) {
                if (key) {
                    if (key === PerfEvent.ParentContextKey || key === PerfEvent.ChildrenContextKey) {
                        return _self[key];
                    }
                    return (_self[strExecutionContextKey] || {})[key];
                }
                return null;
            };
            _self.setCtx = function (key, value) {
                if (key) {
                    if (key === PerfEvent.ParentContextKey) {
                        if (!_self[key]) {
                            _self.isChildEvt = function () { return true; };
                        }
                        _self[key] = value;
                    }
                    else if (key === PerfEvent.ChildrenContextKey) {
                        _self[key] = value;
                    }
                    else {
                        var ctx = _self[strExecutionContextKey] = _self[strExecutionContextKey] || {};
                        ctx[key] = value;
                    }
                }
            };
            _self.complete = function () {
                var childTime = 0;
                var childEvts = _self.getCtx(PerfEvent.ChildrenContextKey);
                if (isArray(childEvts)) {
                    for (var lp = 0; lp < childEvts.length; lp++) {
                        var childEvt = childEvts[lp];
                        if (childEvt) {
                            childTime += childEvt.time;
                        }
                    }
                }
                _self.time = dateNow() - _self.start;
                _self.exTime = _self.time - childTime;
                _self.complete = function () { };
                if (!accessorDefined && isFunction(payloadDetails)) {
                    _self.payload = payloadDetails();
                }
            };
        }
        PerfEvent.ParentContextKey = "parent";
        PerfEvent.ChildrenContextKey = "childEvts";
        return PerfEvent;
    }());
    var PerfManager = /** @class */ (function () {
        function PerfManager(manager) {
            this.ctx = {};
            dynamicProto(PerfManager, this, function (_self) {
                _self.create = function (src, payloadDetails, isAsync) {
                    return new PerfEvent(src, payloadDetails, isAsync);
                };
                _self.fire = function (perfEvent) {
                    if (perfEvent) {
                        perfEvent.complete();
                        if (manager && isFunction(manager.perfEvent)) {
                            manager.perfEvent(perfEvent);
                        }
                    }
                };
                _self.setCtx = function (key, value) {
                    if (key) {
                        var ctx = _self[strExecutionContextKey] = _self[strExecutionContextKey] || {};
                        ctx[key] = value;
                    }
                };
                _self.getCtx = function (key) {
                    return (_self[strExecutionContextKey] || {})[key];
                };
            });
        }
        return PerfManager;
    }());
    var doPerfActiveKey = "CoreUtils.doPerf";
    function doPerf(mgrSource, getSource, func, details, isAsync) {
        if (mgrSource) {
            var perfMgr = mgrSource;
            if (isFunction(perfMgr["getPerfMgr"])) {
                perfMgr = perfMgr["getPerfMgr"]();
            }
            if (perfMgr) {
                var perfEvt = void 0;
                var currentActive = perfMgr.getCtx(doPerfActiveKey);
                try {
                    perfEvt = perfMgr.create(getSource(), details, isAsync);
                    if (perfEvt) {
                        if (currentActive && perfEvt.setCtx) {
                            perfEvt.setCtx(PerfEvent.ParentContextKey, currentActive);
                            if (currentActive.getCtx && currentActive.setCtx) {
                                var children = currentActive.getCtx(PerfEvent.ChildrenContextKey);
                                if (!children) {
                                    children = [];
                                    currentActive.setCtx(PerfEvent.ChildrenContextKey, children);
                                }
                                children.push(perfEvt);
                            }
                        }
                        perfMgr.setCtx(doPerfActiveKey, perfEvt);
                        return func(perfEvt);
                    }
                }
                catch (ex) {
                    if (perfEvt && perfEvt.setCtx) {
                        perfEvt.setCtx("exception", ex);
                    }
                }
                finally {
                    if (perfEvt) {
                        perfMgr.fire(perfEvt);
                    }
                    perfMgr.setCtx(doPerfActiveKey, currentActive);
                }
            }
        }
        return func();
    }
    function setGblPerfMgr(perfManager) {
        _defaultPerfManager = perfManager;
    }
    function getGblPerfMgr() {
        return _defaultPerfManager;
    }

    var UInt32Mask = 0x100000000;
    var MaxUInt32 = 0xffffffff;
    var _mwcSeeded = false;
    var _mwcW = 123456789;
    var _mwcZ = 987654321;
    function _mwcSeed(seedValue) {
        if (seedValue < 0) {
            seedValue >>>= 0;
        }
        _mwcW = (123456789 + seedValue) & MaxUInt32;
        _mwcZ = (987654321 - seedValue) & MaxUInt32;
        _mwcSeeded = true;
    }
    function _autoSeedMwc() {
        try {
            var now = dateNow() & 0x7fffffff;
            _mwcSeed(((Math.random() * UInt32Mask) ^ now) + now);
        }
        catch (e) {
        }
    }
    function randomValue(maxValue) {
        if (maxValue > 0) {
            return Math.floor((random32() / MaxUInt32) * (maxValue + 1)) >>> 0;
        }
        return 0;
    }
    function random32(signed) {
        var value = 0;
        var c = getCrypto() || getMsCrypto();
        if (c && c.getRandomValues) {
            value = c.getRandomValues(new Uint32Array(1))[0] & MaxUInt32;
        }
        if (value === 0 && isIE()) {
            if (!_mwcSeeded) {
                _autoSeedMwc();
            }
            value = mwcRandom32() & MaxUInt32;
        }
        if (value === 0) {
            value = Math.floor((UInt32Mask * Math.random()) | 0);
        }
        if (!signed) {
            value >>>= 0;
        }
        return value;
    }
    function mwcRandomSeed(value) {
        if (!value) {
            _autoSeedMwc();
        }
        else {
            _mwcSeed(value);
        }
    }
    function mwcRandom32(signed) {
        _mwcZ = (36969 * (_mwcZ & 0xFFFF) + (_mwcZ >> 16)) & MaxUInt32;
        _mwcW = (18000 * (_mwcW & 0xFFFF) + (_mwcW >> 16)) & MaxUInt32;
        var value = (((_mwcZ << 16) + (_mwcW & 0xFFFF)) >>> 0) & MaxUInt32 | 0;
        if (!signed) {
            value >>>= 0;
        }
        return value;
    }
    function newId(maxLength) {
        if (maxLength === void 0) { maxLength = 22; }
        var base64chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
        var number = random32() >>> 0;
        var chars = 0;
        var result = strEmpty;
        while (result.length < maxLength) {
            chars++;
            result += base64chars.charAt(number & 0x3F);
            number >>>= 6;
            if (chars === 5) {
                number = (((random32() << 2) & 0xFFFFFFFF) | (number & 0x03)) >>> 0;
                chars = 0;
            }
        }
        return result;
    }

    var _objDefineProperty = ObjDefineProperty;
    var version = "2.8.4";
    var instanceName = "." + newId(6);
    var _dataUid = 0;
    function _createAccessor(target, prop, value) {
        if (_objDefineProperty) {
            try {
                _objDefineProperty(target, prop, {
                    value: value,
                    enumerable: false,
                    configurable: true
                });
                return true;
            }
            catch (e) {
            }
        }
        return false;
    }
    function _canAcceptData(target) {
        return target.nodeType === 1 || target.nodeType === 9 || !(+target.nodeType);
    }
    function _getCache(data, target) {
        var theCache = target[data.id];
        if (!theCache) {
            theCache = {};
            try {
                if (_canAcceptData(target)) {
                    if (!_createAccessor(target, data.id, theCache)) {
                        target[data.id] = theCache;
                    }
                }
            }
            catch (e) {
            }
        }
        return theCache;
    }
    function createUniqueNamespace(name, includeVersion) {
        if (includeVersion === void 0) { includeVersion = false; }
        return normalizeJsName(name + (_dataUid++) + (includeVersion ? "." + version : "") + instanceName);
    }
    function createElmNodeData(name) {
        var data = {
            id: createUniqueNamespace("_aiData-" + (name || "") + "." + version),
            accept: function (target) {
                return _canAcceptData(target);
            },
            get: function (target, name, defValue, addDefault) {
                var theCache = target[data.id];
                if (!theCache) {
                    if (addDefault) {
                        theCache = _getCache(data, target);
                        theCache[normalizeJsName(name)] = defValue;
                    }
                    return defValue;
                }
                return theCache[normalizeJsName(name)];
            },
            kill: function (target, name) {
                if (target && target[name]) {
                    try {
                        delete target[name];
                    }
                    catch (e) {
                    }
                }
            }
        };
        return data;
    }

    var strToGMTString = "toGMTString";
    var strToUTCString = "toUTCString";
    var strCookie = "cookie";
    var strExpires = "expires";
    var strEnabled = "enabled";
    var strIsCookieUseDisabled = "isCookieUseDisabled";
    var strDisableCookiesUsage = "disableCookiesUsage";
    var strConfigCookieMgr = "_ckMgr";
    var _supportsCookies = null;
    var _allowUaSameSite = null;
    var _parsedCookieValue = null;
    var _doc = getDocument();
    var _cookieCache = {};
    var _globalCookieConfig = {};
    function _gblCookieMgr(config, logger) {
        var inst = createCookieMgr[strConfigCookieMgr] || _globalCookieConfig[strConfigCookieMgr];
        if (!inst) {
            inst = createCookieMgr[strConfigCookieMgr] = createCookieMgr(config, logger);
            _globalCookieConfig[strConfigCookieMgr] = inst;
        }
        return inst;
    }
    function _isMgrEnabled(cookieMgr) {
        if (cookieMgr) {
            return cookieMgr.isEnabled();
        }
        return true;
    }
    function _createCookieMgrConfig(rootConfig) {
        var cookieMgrCfg = rootConfig.cookieCfg = rootConfig.cookieCfg || {};
        setValue(cookieMgrCfg, "domain", rootConfig.cookieDomain, isNotNullOrUndefined, isNullOrUndefined);
        setValue(cookieMgrCfg, "path", rootConfig.cookiePath || "/", null, isNullOrUndefined);
        if (isNullOrUndefined(cookieMgrCfg[strEnabled])) {
            var cookieEnabled = void 0;
            if (!isUndefined(rootConfig[strIsCookieUseDisabled])) {
                cookieEnabled = !rootConfig[strIsCookieUseDisabled];
            }
            if (!isUndefined(rootConfig[strDisableCookiesUsage])) {
                cookieEnabled = !rootConfig[strDisableCookiesUsage];
            }
            cookieMgrCfg[strEnabled] = cookieEnabled;
        }
        return cookieMgrCfg;
    }
    function safeGetCookieMgr(core, config) {
        var cookieMgr;
        if (core) {
            cookieMgr = core.getCookieMgr();
        }
        else if (config) {
            var cookieCfg = config.cookieCfg;
            if (cookieCfg[strConfigCookieMgr]) {
                cookieMgr = cookieCfg[strConfigCookieMgr];
            }
            else {
                cookieMgr = createCookieMgr(config);
            }
        }
        if (!cookieMgr) {
            cookieMgr = _gblCookieMgr(config, (core || {}).logger);
        }
        return cookieMgr;
    }
    function createCookieMgr(rootConfig, logger) {
        var cookieMgrConfig = _createCookieMgrConfig(rootConfig || _globalCookieConfig);
        var _path = cookieMgrConfig.path || "/";
        var _domain = cookieMgrConfig.domain;
        var _enabled = cookieMgrConfig[strEnabled] !== false;
        var cookieMgr = {
            isEnabled: function () {
                var enabled = _enabled && areCookiesSupported(logger);
                var gblManager = _globalCookieConfig[strConfigCookieMgr];
                if (enabled && gblManager && cookieMgr !== gblManager) {
                    enabled = _isMgrEnabled(gblManager);
                }
                return enabled;
            },
            setEnabled: function (value) {
                _enabled = value !== false;
            },
            set: function (name, value, maxAgeSec, domain, path) {
                var result = false;
                if (_isMgrEnabled(cookieMgr)) {
                    var values = {};
                    var theValue = strTrim(value || strEmpty);
                    var idx = theValue.indexOf(";");
                    if (idx !== -1) {
                        theValue = strTrim(value.substring(0, idx));
                        values = _extractParts(value.substring(idx + 1));
                    }
                    setValue(values, "domain", domain || _domain, isTruthy, isUndefined);
                    if (!isNullOrUndefined(maxAgeSec)) {
                        var _isIE = isIE();
                        if (isUndefined(values[strExpires])) {
                            var nowMs = dateNow();
                            var expireMs = nowMs + (maxAgeSec * 1000);
                            if (expireMs > 0) {
                                var expiry = new Date();
                                expiry.setTime(expireMs);
                                setValue(values, strExpires, _formatDate(expiry, !_isIE ? strToUTCString : strToGMTString) || _formatDate(expiry, _isIE ? strToGMTString : strToUTCString) || strEmpty, isTruthy);
                            }
                        }
                        if (!_isIE) {
                            setValue(values, "max-age", strEmpty + maxAgeSec, null, isUndefined);
                        }
                    }
                    var location_1 = getLocation();
                    if (location_1 && location_1.protocol === "https:") {
                        setValue(values, "secure", null, null, isUndefined);
                        if (_allowUaSameSite === null) {
                            _allowUaSameSite = !uaDisallowsSameSiteNone((getNavigator() || {}).userAgent);
                        }
                        if (_allowUaSameSite) {
                            setValue(values, "SameSite", "None", null, isUndefined);
                        }
                    }
                    setValue(values, "path", path || _path, null, isUndefined);
                    var setCookieFn = cookieMgrConfig.setCookie || _setCookieValue;
                    setCookieFn(name, _formatCookieValue(theValue, values));
                    result = true;
                }
                return result;
            },
            get: function (name) {
                var value = strEmpty;
                if (_isMgrEnabled(cookieMgr)) {
                    value = (cookieMgrConfig.getCookie || _getCookieValue)(name);
                }
                return value;
            },
            del: function (name, path) {
                var result = false;
                if (_isMgrEnabled(cookieMgr)) {
                    result = cookieMgr.purge(name, path);
                }
                return result;
            },
            purge: function (name, path) {
                var _a;
                var result = false;
                if (areCookiesSupported(logger)) {
                    var values = (_a = {},
                        _a["path"] = path ? path : "/",
                        _a[strExpires] = "Thu, 01 Jan 1970 00:00:01 GMT",
                        _a);
                    if (!isIE()) {
                        values["max-age"] = "0";
                    }
                    var delCookie = cookieMgrConfig.delCookie || _setCookieValue;
                    delCookie(name, _formatCookieValue(strEmpty, values));
                    result = true;
                }
                return result;
            }
        };
        cookieMgr[strConfigCookieMgr] = cookieMgr;
        return cookieMgr;
    }
    function areCookiesSupported(logger) {
        if (_supportsCookies === null) {
            _supportsCookies = false;
            try {
                var doc = _doc || {};
                _supportsCookies = doc[strCookie] !== undefined;
            }
            catch (e) {
                _throwInternal(logger, 2 , 68 , "Cannot access document.cookie - " + getExceptionName(e), { exception: dumpObj(e) });
            }
        }
        return _supportsCookies;
    }
    function _extractParts(theValue) {
        var values = {};
        if (theValue && theValue.length) {
            var parts = strTrim(theValue).split(";");
            arrForEach(parts, function (thePart) {
                thePart = strTrim(thePart || strEmpty);
                if (thePart) {
                    var idx = thePart.indexOf("=");
                    if (idx === -1) {
                        values[thePart] = null;
                    }
                    else {
                        values[strTrim(thePart.substring(0, idx))] = strTrim(thePart.substring(idx + 1));
                    }
                }
            });
        }
        return values;
    }
    function _formatDate(theDate, func) {
        if (isFunction(theDate[func])) {
            return theDate[func]();
        }
        return null;
    }
    function _formatCookieValue(value, values) {
        var cookieValue = value || strEmpty;
        objForEachKey(values, function (name, theValue) {
            cookieValue += "; " + name + (!isNullOrUndefined(theValue) ? "=" + theValue : strEmpty);
        });
        return cookieValue;
    }
    function _getCookieValue(name) {
        var cookieValue = strEmpty;
        if (_doc) {
            var theCookie = _doc[strCookie] || strEmpty;
            if (_parsedCookieValue !== theCookie) {
                _cookieCache = _extractParts(theCookie);
                _parsedCookieValue = theCookie;
            }
            cookieValue = strTrim(_cookieCache[name] || strEmpty);
        }
        return cookieValue;
    }
    function _setCookieValue(name, cookieValue) {
        if (_doc) {
            _doc[strCookie] = name + "=" + cookieValue;
        }
    }
    function uaDisallowsSameSiteNone(userAgent) {
        if (!isString(userAgent)) {
            return false;
        }
        if (strContains(userAgent, "CPU iPhone OS 12") || strContains(userAgent, "iPad; CPU OS 12")) {
            return true;
        }
        if (strContains(userAgent, "Macintosh; Intel Mac OS X 10_14") && strContains(userAgent, "Version/") && strContains(userAgent, "Safari")) {
            return true;
        }
        if (strContains(userAgent, "Macintosh; Intel Mac OS X 10_14") && strEndsWith(userAgent, "AppleWebKit/605.1.15 (KHTML, like Gecko)")) {
            return true;
        }
        if (strContains(userAgent, "Chrome/5") || strContains(userAgent, "Chrome/6")) {
            return true;
        }
        if (strContains(userAgent, "UnrealEngine") && !strContains(userAgent, "Chrome")) {
            return true;
        }
        if (strContains(userAgent, "UCBrowser/12") || strContains(userAgent, "UCBrowser/11")) {
            return true;
        }
        return false;
    }

    var strOnPrefix = "on";
    var strAttachEvent = "attachEvent";
    var strAddEventHelper = "addEventListener";
    var strDetachEvent = "detachEvent";
    var strRemoveEventListener = "removeEventListener";
    var strEvents = "events";
    var strVisibilityChangeEvt = "visibilitychange";
    var strPageHide = "pagehide";
    var strPageShow = "pageshow";
    var strUnload = "unload";
    var strBeforeUnload = "beforeunload";
    var strPageHideNamespace = createUniqueNamespace("aiEvtPageHide");
    var strPageShowNamespace = createUniqueNamespace("aiEvtPageShow");
    var rRemoveEmptyNs = /\.[\.]+/g;
    var rRemoveTrailingEmptyNs = /[\.]+$/;
    var _guid = 1;
    var elmNodeData = createElmNodeData("events");
    var eventNamespace = /^([^.]*)(?:\.(.+)|)/;
    function _normalizeNamespace(name) {
        if (name && name.replace) {
            return name.replace(/^\s*\.*|\.*\s*$/g, "");
        }
        return name;
    }
    function _getEvtNamespace(eventName, evtNamespace) {
        if (evtNamespace) {
            var theNamespace_1 = "";
            if (isArray(evtNamespace)) {
                theNamespace_1 = "";
                arrForEach(evtNamespace, function (name) {
                    name = _normalizeNamespace(name);
                    if (name) {
                        if (name[0] !== ".") {
                            name = "." + name;
                        }
                        theNamespace_1 += name;
                    }
                });
            }
            else {
                theNamespace_1 = _normalizeNamespace(evtNamespace);
            }
            if (theNamespace_1) {
                if (theNamespace_1[0] !== ".") {
                    theNamespace_1 = "." + theNamespace_1;
                }
                eventName = (eventName || "") + theNamespace_1;
            }
        }
        var parsedEvent = (eventNamespace.exec(eventName || "") || []);
        return {
            type: parsedEvent[1],
            ns: ((parsedEvent[2] || "").replace(rRemoveEmptyNs, ".").replace(rRemoveTrailingEmptyNs, "").split(".").sort()).join(".")
        };
    }
    function __getRegisteredEvents(target, eventName, evtNamespace) {
        var theEvents = [];
        var eventCache = elmNodeData.get(target, strEvents, {}, false);
        var evtName = _getEvtNamespace(eventName, evtNamespace);
        objForEachKey(eventCache, function (evtType, registeredEvents) {
            arrForEach(registeredEvents, function (value) {
                if (!evtName.type || evtName.type === value.evtName.type) {
                    if (!evtName.ns || evtName.ns === evtName.ns) {
                        theEvents.push({
                            name: value.evtName.type + (value.evtName.ns ? "." + value.evtName.ns : ""),
                            handler: value.handler
                        });
                    }
                }
            });
        });
        return theEvents;
    }
    function _getRegisteredEvents(target, evtName, addDefault) {
        if (addDefault === void 0) { addDefault = true; }
        var aiEvts = elmNodeData.get(target, strEvents, {}, addDefault);
        var registeredEvents = aiEvts[evtName];
        if (!registeredEvents) {
            registeredEvents = aiEvts[evtName] = [];
        }
        return registeredEvents;
    }
    function _doDetach(obj, evtName, handlerRef, useCapture) {
        if (obj && evtName && evtName.type) {
            if (obj[strRemoveEventListener]) {
                obj[strRemoveEventListener](evtName.type, handlerRef, useCapture);
            }
            else if (obj[strDetachEvent]) {
                obj[strDetachEvent](strOnPrefix + evtName.type, handlerRef);
            }
        }
    }
    function _doAttach(obj, evtName, handlerRef, useCapture) {
        var result = false;
        if (obj && evtName && evtName.type && handlerRef) {
            if (obj[strAddEventHelper]) {
                obj[strAddEventHelper](evtName.type, handlerRef, useCapture);
                result = true;
            }
            else if (obj[strAttachEvent]) {
                obj[strAttachEvent](strOnPrefix + evtName.type, handlerRef);
                result = true;
            }
        }
        return result;
    }
    function _doUnregister(target, events, evtName, unRegFn) {
        var idx = events.length;
        while (idx--) {
            var theEvent = events[idx];
            if (theEvent) {
                if (!evtName.ns || evtName.ns === theEvent.evtName.ns) {
                    if (!unRegFn || unRegFn(theEvent)) {
                        _doDetach(target, theEvent.evtName, theEvent.handler, theEvent.capture);
                        events.splice(idx, 1);
                    }
                }
            }
        }
    }
    function _unregisterEvents(target, evtName, unRegFn) {
        if (evtName.type) {
            _doUnregister(target, _getRegisteredEvents(target, evtName.type), evtName, unRegFn);
        }
        else {
            var eventCache = elmNodeData.get(target, strEvents, {});
            objForEachKey(eventCache, function (evtType, events) {
                _doUnregister(target, events, evtName, unRegFn);
            });
            if (objKeys(eventCache).length === 0) {
                elmNodeData.kill(target, strEvents);
            }
        }
    }
    function mergeEvtNamespace(theNamespace, namespaces) {
        var newNamespaces;
        if (namespaces) {
            if (isArray(namespaces)) {
                newNamespaces = [theNamespace].concat(namespaces);
            }
            else {
                newNamespaces = [theNamespace, namespaces];
            }
            newNamespaces = (_getEvtNamespace("xx", newNamespaces).ns).split(".");
        }
        else {
            newNamespaces = theNamespace;
        }
        return newNamespaces;
    }
    function eventOn(target, eventName, handlerRef, evtNamespace, useCapture) {
        if (useCapture === void 0) { useCapture = false; }
        var result = false;
        if (target) {
            try {
                var evtName = _getEvtNamespace(eventName, evtNamespace);
                result = _doAttach(target, evtName, handlerRef, useCapture);
                if (result && elmNodeData.accept(target)) {
                    var registeredEvent = {
                        guid: _guid++,
                        evtName: evtName,
                        handler: handlerRef,
                        capture: useCapture
                    };
                    _getRegisteredEvents(target, evtName.type).push(registeredEvent);
                }
            }
            catch (e) {
            }
        }
        return result;
    }
    function eventOff(target, eventName, handlerRef, evtNamespace, useCapture) {
        if (useCapture === void 0) { useCapture = false; }
        if (target) {
            try {
                var evtName_1 = _getEvtNamespace(eventName, evtNamespace);
                var found_1 = false;
                _unregisterEvents(target, evtName_1, function (regEvent) {
                    if ((evtName_1.ns && !handlerRef) || regEvent.handler === handlerRef) {
                        found_1 = true;
                        return true;
                    }
                    return false;
                });
                if (!found_1) {
                    _doDetach(target, evtName_1, handlerRef, useCapture);
                }
            }
            catch (e) {
            }
        }
    }
    function attachEvent(obj, eventNameWithoutOn, handlerRef, useCapture) {
        if (useCapture === void 0) { useCapture = false; }
        return eventOn(obj, eventNameWithoutOn, handlerRef, null, useCapture);
    }
    function detachEvent(obj, eventNameWithoutOn, handlerRef, useCapture) {
        if (useCapture === void 0) { useCapture = false; }
        eventOff(obj, eventNameWithoutOn, handlerRef, null, useCapture);
    }
    function addEventHandler(eventName, callback, evtNamespace) {
        var result = false;
        var w = getWindow();
        if (w) {
            result = eventOn(w, eventName, callback, evtNamespace);
            result = eventOn(w["body"], eventName, callback, evtNamespace) || result;
        }
        var doc = getDocument();
        if (doc) {
            result = eventOn(doc, eventName, callback, evtNamespace) || result;
        }
        return result;
    }
    function removeEventHandler(eventName, callback, evtNamespace) {
        var w = getWindow();
        if (w) {
            eventOff(w, eventName, callback, evtNamespace);
            eventOff(w["body"], eventName, callback, evtNamespace);
        }
        var doc = getDocument();
        if (doc) {
            eventOff(doc, eventName, callback, evtNamespace);
        }
    }
    function _addEventListeners(events, listener, excludeEvents, evtNamespace) {
        var added = false;
        if (listener && events && events.length > 0) {
            arrForEach(events, function (name) {
                if (name) {
                    if (!excludeEvents || arrIndexOf(excludeEvents, name) === -1) {
                        added = addEventHandler(name, listener, evtNamespace) || added;
                    }
                }
            });
        }
        return added;
    }
    function addEventListeners(events, listener, excludeEvents, evtNamespace) {
        var added = false;
        if (listener && events && isArray(events)) {
            added = _addEventListeners(events, listener, excludeEvents, evtNamespace);
            if (!added && excludeEvents && excludeEvents.length > 0) {
                added = _addEventListeners(events, listener, null, evtNamespace);
            }
        }
        return added;
    }
    function removeEventListeners(events, listener, evtNamespace) {
        if (events && isArray(events)) {
            arrForEach(events, function (name) {
                if (name) {
                    removeEventHandler(name, listener, evtNamespace);
                }
            });
        }
    }
    function addPageUnloadEventListener(listener, excludeEvents, evtNamespace) {
        return addEventListeners([strBeforeUnload, strUnload, strPageHide], listener, excludeEvents, evtNamespace);
    }
    function removePageUnloadEventListener(listener, evtNamespace) {
        removeEventListeners([strBeforeUnload, strUnload, strPageHide], listener, evtNamespace);
    }
    function addPageHideEventListener(listener, excludeEvents, evtNamespace) {
        function _handlePageVisibility(evt) {
            var doc = getDocument();
            if (listener && doc && doc.visibilityState === "hidden") {
                listener(evt);
            }
        }
        var newNamespaces = mergeEvtNamespace(strPageHideNamespace, evtNamespace);
        var pageUnloadAdded = _addEventListeners([strPageHide], listener, excludeEvents, newNamespaces);
        if (!excludeEvents || arrIndexOf(excludeEvents, strVisibilityChangeEvt) === -1) {
            pageUnloadAdded = _addEventListeners([strVisibilityChangeEvt], _handlePageVisibility, excludeEvents, newNamespaces) || pageUnloadAdded;
        }
        if (!pageUnloadAdded && excludeEvents) {
            pageUnloadAdded = addPageHideEventListener(listener, null, evtNamespace);
        }
        return pageUnloadAdded;
    }
    function removePageHideEventListener(listener, evtNamespace) {
        var newNamespaces = mergeEvtNamespace(strPageHideNamespace, evtNamespace);
        removeEventListeners([strPageHide], listener, newNamespaces);
        removeEventListeners([strVisibilityChangeEvt], null, newNamespaces);
    }
    function addPageShowEventListener(listener, excludeEvents, evtNamespace) {
        function _handlePageVisibility(evt) {
            var doc = getDocument();
            if (listener && doc && doc.visibilityState === "visible") {
                listener(evt);
            }
        }
        var newNamespaces = mergeEvtNamespace(strPageShowNamespace, evtNamespace);
        var pageShowAdded = _addEventListeners([strPageShow], listener, excludeEvents, newNamespaces);
        pageShowAdded = _addEventListeners([strVisibilityChangeEvt], _handlePageVisibility, excludeEvents, newNamespaces) || pageShowAdded;
        if (!pageShowAdded && excludeEvents) {
            pageShowAdded = addPageShowEventListener(listener, null, evtNamespace);
        }
        return pageShowAdded;
    }
    function removePageShowEventListener(listener, evtNamespace) {
        var newNamespaces = mergeEvtNamespace(strPageShowNamespace, evtNamespace);
        removeEventListeners([strPageShow], listener, newNamespaces);
        removeEventListeners([strVisibilityChangeEvt], null, newNamespaces);
    }

    var _cookieMgrs = null;
    var _canUseCookies;
    var Undefined = strShimUndefined;
    function newGuid() {
        function randomHexDigit() {
            return randomValue(15);
        }
        return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(GuidRegex, function (c) {
            var r = (randomHexDigit() | 0), v = (c === "x" ? r : r & 0x3 | 0x8);
            return v.toString(16);
        });
    }
    function perfNow() {
        var perf = getPerformance();
        if (perf && perf.now) {
            return perf.now();
        }
        return dateNow();
    }
    function generateW3CId() {
        var hexValues = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"];
        var oct = strEmpty, tmp;
        for (var a = 0; a < 4; a++) {
            tmp = random32();
            oct +=
                hexValues[tmp & 0xF] +
                    hexValues[tmp >> 4 & 0xF] +
                    hexValues[tmp >> 8 & 0xF] +
                    hexValues[tmp >> 12 & 0xF] +
                    hexValues[tmp >> 16 & 0xF] +
                    hexValues[tmp >> 20 & 0xF] +
                    hexValues[tmp >> 24 & 0xF] +
                    hexValues[tmp >> 28 & 0xF];
        }
        var clockSequenceHi = hexValues[8 + (random32() & 0x03) | 0];
        return oct.substr(0, 8) + oct.substr(9, 4) + "4" + oct.substr(13, 3) + clockSequenceHi + oct.substr(16, 3) + oct.substr(19, 12);
    }
    var CoreUtils = {
        _canUseCookies: undefined,
        isTypeof: isTypeof,
        isUndefined: isUndefined,
        isNullOrUndefined: isNullOrUndefined,
        hasOwnProperty: hasOwnProperty,
        isFunction: isFunction,
        isObject: isObject,
        isDate: isDate,
        isArray: isArray,
        isError: isError,
        isString: isString,
        isNumber: isNumber,
        isBoolean: isBoolean,
        toISOString: toISOString,
        arrForEach: arrForEach,
        arrIndexOf: arrIndexOf,
        arrMap: arrMap,
        arrReduce: arrReduce,
        strTrim: strTrim,
        objCreate: objCreateFn,
        objKeys: objKeys,
        objDefineAccessors: objDefineAccessors,
        addEventHandler: addEventHandler,
        dateNow: dateNow,
        isIE: isIE,
        disableCookies: disableCookies,
        newGuid: newGuid,
        perfNow: perfNow,
        newId: newId,
        randomValue: randomValue,
        random32: random32,
        mwcRandomSeed: mwcRandomSeed,
        mwcRandom32: mwcRandom32,
        generateW3CId: generateW3CId
    };
    var GuidRegex = /[xy]/g;
    var EventHelper = {
        Attach: attachEvent,
        AttachEvent: attachEvent,
        Detach: detachEvent,
        DetachEvent: detachEvent
    };
    function _legacyCookieMgr(config, logger) {
        var cookieMgr = _gblCookieMgr(config, logger);
        var legacyCanUseCookies = CoreUtils._canUseCookies;
        if (_cookieMgrs === null) {
            _cookieMgrs = [];
            _canUseCookies = legacyCanUseCookies;
            objDefineAccessors(CoreUtils, "_canUseCookies", function () {
                return _canUseCookies;
            }, function (value) {
                _canUseCookies = value;
                arrForEach(_cookieMgrs, function (mgr) {
                    mgr.setEnabled(value);
                });
            });
        }
        if (arrIndexOf(_cookieMgrs, cookieMgr) === -1) {
            _cookieMgrs.push(cookieMgr);
        }
        if (isBoolean(legacyCanUseCookies)) {
            cookieMgr.setEnabled(legacyCanUseCookies);
        }
        if (isBoolean(_canUseCookies)) {
            cookieMgr.setEnabled(_canUseCookies);
        }
        return cookieMgr;
    }
    function disableCookies() {
        _legacyCookieMgr().setEnabled(false);
    }
    function canUseCookies(logger) {
        return _legacyCookieMgr(null, logger).isEnabled();
    }
    function getCookie(logger, name) {
        return _legacyCookieMgr(null, logger).get(name);
    }
    function setCookie(logger, name, value, domain) {
        _legacyCookieMgr(null, logger).set(name, value, null, domain);
    }
    function deleteCookie(logger, name) {
        return _legacyCookieMgr(null, logger).del(name);
    }

    var TRACE_PARENT_REGEX = /^([\da-f]{2})-([\da-f]{32})-([\da-f]{16})-([\da-f]{2})(-[^\s]*)?$/;
    var DEFAULT_VERSION = "00";
    var INVALID_VERSION = "ff";
    var INVALID_TRACE_ID = "00000000000000000000000000000000";
    var INVALID_SPAN_ID = "0000000000000000";
    var SAMPLED_FLAG = 0x01;
    function _isValid(value, len, invalidValue) {
        if (value && value.length === len && value !== invalidValue) {
            return !!value.match(/^[\da-f]*$/);
        }
        return false;
    }
    function _formatValue(value, len, defValue) {
        if (_isValid(value, len)) {
            return value;
        }
        return defValue;
    }
    function _formatFlags(value) {
        if (isNaN(value) || value < 0 || value > 255) {
            value = 0x01;
        }
        var result = value.toString(16);
        while (result.length < 2) {
            result = "0" + result;
        }
        return result;
    }
    function createTraceParent(traceId, spanId, flags, version) {
        return {
            version: _isValid(version, 2, INVALID_VERSION) ? version : DEFAULT_VERSION,
            traceId: isValidTraceId(traceId) ? traceId : generateW3CId(),
            spanId: isValidSpanId(spanId) ? spanId : generateW3CId().substr(0, 16),
            traceFlags: flags >= 0 && flags <= 0xFF ? flags : 1
        };
    }
    function parseTraceParent(value) {
        if (!value) {
            return null;
        }
        if (isArray(value)) {
            value = value[0] || "";
        }
        if (!value || !isString(value) || value.length > 8192) {
            return null;
        }
        var match = TRACE_PARENT_REGEX.exec(strTrim(value));
        if (!match ||
            match[1] === INVALID_VERSION ||
            match[2] === INVALID_TRACE_ID ||
            match[3] === INVALID_SPAN_ID) {
            return null;
        }
        return {
            version: match[1],
            traceId: match[2],
            spanId: match[3],
            traceFlags: parseInt(match[4], 16)
        };
    }
    function isValidTraceId(value) {
        return _isValid(value, 32, INVALID_TRACE_ID);
    }
    function isValidSpanId(value) {
        return _isValid(value, 16, INVALID_SPAN_ID);
    }
    function isValidTraceParent(value) {
        if (!value ||
            !_isValid(value.version, 2, INVALID_VERSION) ||
            !_isValid(value.traceId, 32, INVALID_TRACE_ID) ||
            !_isValid(value.spanId, 16, INVALID_SPAN_ID) ||
            !_isValid(_formatFlags(value.traceFlags), 2)) {
            return false;
        }
        return true;
    }
    function isSampledFlag(value) {
        if (isValidTraceParent(value)) {
            return (value.traceFlags & SAMPLED_FLAG) === SAMPLED_FLAG;
        }
        return false;
    }
    function formatTraceParent(value) {
        if (value) {
            var flags = _formatFlags(value.traceFlags);
            if (!_isValid(flags, 2)) {
                flags = "01";
            }
            var version = value.version || DEFAULT_VERSION;
            if (version !== "00" && version !== "ff") {
                version = DEFAULT_VERSION;
            }
            return "".concat(version, "-").concat(_formatValue(value.traceId, 32, INVALID_TRACE_ID), "-").concat(_formatValue(value.spanId, 16, INVALID_SPAN_ID), "-").concat(flags);
        }
        return "";
    }
    function findW3cTraceParent() {
        var name = "traceparent";
        var traceParent = parseTraceParent(findMetaTag(name));
        if (!traceParent) {
            traceParent = parseTraceParent(findNamedServerTiming(name));
        }
        return traceParent;
    }

    var strDoUnload = "_doUnload";
    var pluginStateData = createElmNodeData("plugin");
    function _getPluginState(plugin) {
        return pluginStateData.get(plugin, "state", {}, true);
    }
    function initializePlugins(processContext, extensions) {
        var initPlugins = [];
        var lastPlugin = null;
        var proxy = processContext.getNext();
        var pluginState;
        while (proxy) {
            var thePlugin = proxy.getPlugin();
            if (thePlugin) {
                if (lastPlugin &&
                    isFunction(lastPlugin[strSetNextPlugin]) &&
                    isFunction(thePlugin[strProcessTelemetry])) {
                    lastPlugin[strSetNextPlugin](thePlugin);
                }
                var isInitialized = false;
                if (isFunction(thePlugin[strIsInitialized])) {
                    isInitialized = thePlugin[strIsInitialized]();
                }
                else {
                    pluginState = _getPluginState(thePlugin);
                    isInitialized = pluginState[strIsInitialized];
                }
                if (!isInitialized) {
                    initPlugins.push(thePlugin);
                }
                lastPlugin = thePlugin;
                proxy = proxy.getNext();
            }
        }
        arrForEach(initPlugins, function (thePlugin) {
            var core = processContext.core();
            thePlugin.initialize(processContext.getCfg(), core, extensions, processContext.getNext());
            pluginState = _getPluginState(thePlugin);
            if (!thePlugin[strCore] && !pluginState[strCore]) {
                pluginState[strCore] = core;
            }
            pluginState[strIsInitialized] = true;
            delete pluginState[strTeardown];
        });
    }
    function sortPlugins(plugins) {
        return plugins.sort(function (extA, extB) {
            var result = 0;
            if (extB) {
                var bHasProcess = isFunction(extB[strProcessTelemetry]);
                if (isFunction(extA[strProcessTelemetry])) {
                    result = bHasProcess ? extA[strPriority] - extB[strPriority] : 1;
                }
                else if (bHasProcess) {
                    result = -1;
                }
            }
            else {
                result = extA ? 1 : -1;
            }
            return result;
        });
    }
    function unloadComponents(components, unloadCtx, unloadState, asyncCallback) {
        var idx = 0;
        function _doUnload() {
            while (idx < components.length) {
                var component = components[idx++];
                if (component) {
                    var func = component[strDoUnload] || component[strDoTeardown];
                    if (isFunction(func)) {
                        if (func.call(component, unloadCtx, unloadState, _doUnload) === true) {
                            return true;
                        }
                    }
                }
            }
        }
        return _doUnload();
    }
    function createDistributedTraceContext(parentCtx) {
        var trace = {};
        return {
            getName: function () {
                return trace.name;
            },
            setName: function (newValue) {
                parentCtx && parentCtx.setName(newValue);
                trace.name = newValue;
            },
            getTraceId: function () {
                return trace.traceId;
            },
            setTraceId: function (newValue) {
                parentCtx && parentCtx.setTraceId(newValue);
                if (isValidTraceId(newValue)) {
                    trace.traceId = newValue;
                }
            },
            getSpanId: function () {
                return trace.spanId;
            },
            setSpanId: function (newValue) {
                parentCtx && parentCtx.setSpanId(newValue);
                if (isValidSpanId(newValue)) {
                    trace.spanId = newValue;
                }
            },
            getTraceFlags: function () {
                return trace.traceFlags;
            },
            setTraceFlags: function (newTraceFlags) {
                parentCtx && parentCtx.setTraceFlags(newTraceFlags);
                trace.traceFlags = newTraceFlags;
            }
        };
    }

    var strTelemetryPluginChain = "TelemetryPluginChain";
    var strHasRunFlags = "_hasRun";
    var strGetTelCtx = "_getTelCtx";
    var _chainId = 0;
    function _getNextProxyStart(proxy, core, startAt) {
        while (proxy) {
            if (proxy.getPlugin() === startAt) {
                return proxy;
            }
            proxy = proxy.getNext();
        }
        return createTelemetryProxyChain([startAt], core.config || {}, core);
    }
    function _createInternalContext(telemetryChain, config, core, startAt) {
        var _nextProxy = null;
        var _onComplete = [];
        if (startAt !== null) {
            _nextProxy = startAt ? _getNextProxyStart(telemetryChain, core, startAt) : telemetryChain;
        }
        var context = {
            _next: _moveNext,
            ctx: {
                core: function () {
                    return core;
                },
                diagLog: function () {
                    return safeGetLogger(core, config);
                },
                getCfg: function () {
                    return config;
                },
                getExtCfg: _getExtCfg,
                getConfig: _getConfig,
                hasNext: function () {
                    return !!_nextProxy;
                },
                getNext: function () {
                    return _nextProxy;
                },
                setNext: function (nextPlugin) {
                    _nextProxy = nextPlugin;
                },
                iterate: _iterateChain,
                onComplete: _addOnComplete
            }
        };
        function _addOnComplete(onComplete, that) {
            var args = [];
            for (var _i = 2; _i < arguments.length; _i++) {
                args[_i - 2] = arguments[_i];
            }
            if (onComplete) {
                _onComplete.push({
                    func: onComplete,
                    self: !isUndefined(that) ? that : context.ctx,
                    args: args
                });
            }
        }
        function _moveNext() {
            var nextProxy = _nextProxy;
            _nextProxy = nextProxy ? nextProxy.getNext() : null;
            if (!nextProxy) {
                var onComplete = _onComplete;
                if (onComplete && onComplete.length > 0) {
                    arrForEach(onComplete, function (completeDetails) {
                        try {
                            completeDetails.func.call(completeDetails.self, completeDetails.args);
                        }
                        catch (e) {
                            _throwInternal(core.logger, 2 , 73 , "Unexpected Exception during onComplete - " + dumpObj(e));
                        }
                    });
                    _onComplete = [];
                }
            }
            return nextProxy;
        }
        function _getExtCfg(identifier, defaultValue, mergeDefault) {
            if (defaultValue === void 0) { defaultValue = {}; }
            if (mergeDefault === void 0) { mergeDefault = 0 ; }
            var theConfig;
            if (config) {
                var extConfig = config.extensionConfig;
                if (extConfig && identifier) {
                    theConfig = extConfig[identifier];
                }
            }
            if (!theConfig) {
                theConfig = defaultValue;
            }
            else if (isObject(defaultValue)) {
                if (mergeDefault !== 0 ) {
                    var newConfig_1 = objExtend(true, defaultValue, theConfig);
                    if (config && mergeDefault === 2 ) {
                        objForEachKey(defaultValue, function (field) {
                            if (isNullOrUndefined(newConfig_1[field])) {
                                var cfgValue = config[field];
                                if (!isNullOrUndefined(cfgValue)) {
                                    newConfig_1[field] = cfgValue;
                                }
                            }
                        });
                    }
                    theConfig = newConfig_1;
                }
            }
            return theConfig;
        }
        function _getConfig(identifier, field, defaultValue) {
            if (defaultValue === void 0) { defaultValue = false; }
            var theValue;
            var extConfig = _getExtCfg(identifier, null);
            if (extConfig && !isNullOrUndefined(extConfig[field])) {
                theValue = extConfig[field];
            }
            else if (config && !isNullOrUndefined(config[field])) {
                theValue = config[field];
            }
            return !isNullOrUndefined(theValue) ? theValue : defaultValue;
        }
        function _iterateChain(cb) {
            var nextPlugin;
            while (!!(nextPlugin = context._next())) {
                var plugin = nextPlugin.getPlugin();
                if (plugin) {
                    cb(plugin);
                }
            }
        }
        return context;
    }
    function createProcessTelemetryContext(telemetryChain, config, core, startAt) {
        var internalContext = _createInternalContext(telemetryChain, config, core, startAt);
        var context = internalContext.ctx;
        function _processNext(env) {
            var nextPlugin = internalContext._next();
            nextPlugin && nextPlugin.processTelemetry(env, context);
            return !nextPlugin;
        }
        function _createNew(plugins, startAt) {
            if (plugins === void 0) { plugins = null; }
            if (isArray(plugins)) {
                plugins = createTelemetryProxyChain(plugins, config, core, startAt);
            }
            return createProcessTelemetryContext(plugins || context.getNext(), config, core, startAt);
        }
        context.processNext = _processNext;
        context.createNew = _createNew;
        return context;
    }
    function createProcessTelemetryUnloadContext(telemetryChain, core, startAt) {
        var config = core.config || {};
        var internalContext = _createInternalContext(telemetryChain, config, core, startAt);
        var context = internalContext.ctx;
        function _processNext(unloadState) {
            var nextPlugin = internalContext._next();
            nextPlugin && nextPlugin.unload(context, unloadState);
            return !nextPlugin;
        }
        function _createNew(plugins, startAt) {
            if (plugins === void 0) { plugins = null; }
            if (isArray(plugins)) {
                plugins = createTelemetryProxyChain(plugins, config, core, startAt);
            }
            return createProcessTelemetryUnloadContext(plugins || context.getNext(), core, startAt);
        }
        context.processNext = _processNext;
        context.createNew = _createNew;
        return context;
    }
    function createProcessTelemetryUpdateContext(telemetryChain, core, startAt) {
        var config = core.config || {};
        var internalContext = _createInternalContext(telemetryChain, config, core, startAt);
        var context = internalContext.ctx;
        function _processNext(updateState) {
            return context.iterate(function (plugin) {
                if (isFunction(plugin.update)) {
                    plugin.update(context, updateState);
                }
            });
        }
        function _createNew(plugins, startAt) {
            if (plugins === void 0) { plugins = null; }
            if (isArray(plugins)) {
                plugins = createTelemetryProxyChain(plugins, config, core, startAt);
            }
            return createProcessTelemetryUpdateContext(plugins || context.getNext(), core, startAt);
        }
        context.processNext = _processNext;
        context.createNew = _createNew;
        return context;
    }
    function createTelemetryProxyChain(plugins, config, core, startAt) {
        var firstProxy = null;
        var add = startAt ? false : true;
        if (isArray(plugins) && plugins.length > 0) {
            var lastProxy_1 = null;
            arrForEach(plugins, function (thePlugin) {
                if (!add && startAt === thePlugin) {
                    add = true;
                }
                if (add && thePlugin && isFunction(thePlugin.processTelemetry)) {
                    var newProxy = createTelemetryPluginProxy(thePlugin, config, core);
                    if (!firstProxy) {
                        firstProxy = newProxy;
                    }
                    if (lastProxy_1) {
                        lastProxy_1._setNext(newProxy);
                    }
                    lastProxy_1 = newProxy;
                }
            });
        }
        if (startAt && !firstProxy) {
            return createTelemetryProxyChain([startAt], config, core);
        }
        return firstProxy;
    }
    function createTelemetryPluginProxy(plugin, config, core) {
        var nextProxy = null;
        var hasProcessTelemetry = isFunction(plugin.processTelemetry);
        var hasSetNext = isFunction(plugin.setNextPlugin);
        var chainId;
        if (plugin) {
            chainId = plugin.identifier + "-" + plugin.priority + "-" + _chainId++;
        }
        else {
            chainId = "Unknown-0-" + _chainId++;
        }
        var proxyChain = {
            getPlugin: function () {
                return plugin;
            },
            getNext: function () {
                return nextProxy;
            },
            processTelemetry: _processTelemetry,
            unload: _unloadPlugin,
            update: _updatePlugin,
            _id: chainId,
            _setNext: function (nextPlugin) {
                nextProxy = nextPlugin;
            }
        };
        function _getTelCtx() {
            var itemCtx;
            if (plugin && isFunction(plugin[strGetTelCtx])) {
                itemCtx = plugin[strGetTelCtx]();
            }
            if (!itemCtx) {
                itemCtx = createProcessTelemetryContext(proxyChain, config, core);
            }
            return itemCtx;
        }
        function _processChain(itemCtx, processPluginFn, name, details, isAsync) {
            var hasRun = false;
            var identifier = plugin ? plugin.identifier : strTelemetryPluginChain;
            var hasRunContext = itemCtx[strHasRunFlags];
            if (!hasRunContext) {
                hasRunContext = itemCtx[strHasRunFlags] = {};
            }
            itemCtx.setNext(nextProxy);
            if (plugin) {
                doPerf(itemCtx[strCore](), function () { return identifier + ":" + name; }, function () {
                    hasRunContext[chainId] = true;
                    try {
                        var nextId = nextProxy ? nextProxy._id : strEmpty;
                        if (nextId) {
                            hasRunContext[nextId] = false;
                        }
                        hasRun = processPluginFn(itemCtx);
                    }
                    catch (error) {
                        var hasNextRun = nextProxy ? hasRunContext[nextProxy._id] : true;
                        if (hasNextRun) {
                            hasRun = true;
                        }
                        if (!nextProxy || !hasNextRun) {
                            _throwInternal(itemCtx.diagLog(), 1 , 73 , "Plugin [" + identifier + "] failed during " + name + " - " + dumpObj(error) + ", run flags: " + dumpObj(hasRunContext));
                        }
                    }
                }, details, isAsync);
            }
            return hasRun;
        }
        function _processTelemetry(env, itemCtx) {
            itemCtx = itemCtx || _getTelCtx();
            function _callProcessTelemetry(itemCtx) {
                if (!plugin || !hasProcessTelemetry) {
                    return false;
                }
                var pluginState = _getPluginState(plugin);
                if (pluginState.teardown || pluginState[strDisabled]) {
                    return false;
                }
                if (hasSetNext) {
                    plugin.setNextPlugin(nextProxy);
                }
                plugin.processTelemetry(env, itemCtx);
                return true;
            }
            if (!_processChain(itemCtx, _callProcessTelemetry, "processTelemetry", function () { return ({ item: env }); }, !(env.sync))) {
                itemCtx.processNext(env);
            }
        }
        function _unloadPlugin(unloadCtx, unloadState) {
            function _callTeardown() {
                var hasRun = false;
                if (plugin) {
                    var pluginState = _getPluginState(plugin);
                    var pluginCore = plugin[strCore] || pluginState.core;
                    if (plugin && (!pluginCore || pluginCore === unloadCtx[strCore]()) && !pluginState[strTeardown]) {
                        pluginState[strCore] = null;
                        pluginState[strTeardown] = true;
                        pluginState[strIsInitialized] = false;
                        if (plugin[strTeardown] && plugin[strTeardown](unloadCtx, unloadState) === true) {
                            hasRun = true;
                        }
                    }
                }
                return hasRun;
            }
            if (!_processChain(unloadCtx, _callTeardown, "unload", function () { }, unloadState.isAsync)) {
                unloadCtx.processNext(unloadState);
            }
        }
        function _updatePlugin(updateCtx, updateState) {
            function _callUpdate() {
                var hasRun = false;
                if (plugin) {
                    var pluginState = _getPluginState(plugin);
                    var pluginCore = plugin[strCore] || pluginState.core;
                    if (plugin && (!pluginCore || pluginCore === updateCtx[strCore]()) && !pluginState[strTeardown]) {
                        if (plugin[strUpdate] && plugin[strUpdate](updateCtx, updateState) === true) {
                            hasRun = true;
                        }
                    }
                }
                return hasRun;
            }
            if (!_processChain(updateCtx, _callUpdate, "update", function () { }, false)) {
                updateCtx.processNext(updateState);
            }
        }
        return objFreeze(proxyChain);
    }
    var ProcessTelemetryContext = /** @class */ (function () {
        function ProcessTelemetryContext(pluginChain, config, core, startAt) {
            var _self = this;
            var context = createProcessTelemetryContext(pluginChain, config, core, startAt);
            proxyFunctions(_self, context, objKeys(context));
        }
        return ProcessTelemetryContext;
    }());

    var strIKey = "iKey";
    var strExtensionConfig = "extensionConfig";

    var ChannelControllerPriority = 500;
    var ChannelValidationMessage = "Channel has invalid priority - ";
    function _addChannelQueue(channelQueue, queue, config, core) {
        if (queue && isArray(queue) && queue.length > 0) {
            queue = queue.sort(function (a, b) {
                return a.priority - b.priority;
            });
            arrForEach(queue, function (queueItem) {
                if (queueItem.priority < ChannelControllerPriority) {
                    throwError(ChannelValidationMessage + queueItem.identifier);
                }
            });
            channelQueue.push({
                queue: objFreeze(queue),
                chain: createTelemetryProxyChain(queue, config, core)
            });
        }
    }
    function createChannelControllerPlugin(channelQueue, core) {
        var _a;
        function _getTelCtx() {
            return createProcessTelemetryContext(null, core.config, core, null);
        }
        function _processChannelQueue(theChannels, itemCtx, processFn, onComplete) {
            var waiting = theChannels ? (theChannels.length + 1) : 1;
            function _runChainOnComplete() {
                waiting--;
                if (waiting === 0) {
                    onComplete && onComplete();
                    onComplete = null;
                }
            }
            if (waiting > 0) {
                arrForEach(theChannels, function (channels) {
                    if (channels && channels.queue.length > 0) {
                        var channelChain = channels.chain;
                        var chainCtx = itemCtx.createNew(channelChain);
                        chainCtx.onComplete(_runChainOnComplete);
                        processFn(chainCtx);
                    }
                    else {
                        waiting--;
                    }
                });
            }
            _runChainOnComplete();
        }
        function _doUpdate(updateCtx, updateState) {
            var theUpdateState = updateState || {
                reason: 0
            };
            _processChannelQueue(channelQueue, updateCtx, function (chainCtx) {
                chainCtx[strProcessNext](theUpdateState);
            }, function () {
                updateCtx[strProcessNext](theUpdateState);
            });
            return true;
        }
        function _doTeardown(unloadCtx, unloadState) {
            var theUnloadState = unloadState || {
                reason: 0 ,
                isAsync: false
            };
            _processChannelQueue(channelQueue, unloadCtx, function (chainCtx) {
                chainCtx[strProcessNext](theUnloadState);
            }, function () {
                unloadCtx[strProcessNext](theUnloadState);
                isInitialized = false;
            });
            return true;
        }
        function _getChannel(pluginIdentifier) {
            var thePlugin = null;
            if (channelQueue && channelQueue.length > 0) {
                arrForEach(channelQueue, function (channels) {
                    if (channels && channels.queue.length > 0) {
                        arrForEach(channels.queue, function (ext) {
                            if (ext.identifier === pluginIdentifier) {
                                thePlugin = ext;
                                return -1;
                            }
                        });
                        if (thePlugin) {
                            return -1;
                        }
                    }
                });
            }
            return thePlugin;
        }
        var isInitialized = false;
        var channelController = (_a = {
                identifier: "ChannelControllerPlugin",
                priority: ChannelControllerPriority,
                initialize: function (config, core, extensions, pluginChain) {
                    isInitialized = true;
                    arrForEach(channelQueue, function (channels) {
                        if (channels && channels.queue.length > 0) {
                            initializePlugins(createProcessTelemetryContext(channels.chain, config, core), extensions);
                        }
                    });
                },
                isInitialized: function () {
                    return isInitialized;
                },
                processTelemetry: function (item, itemCtx) {
                    _processChannelQueue(channelQueue, itemCtx || _getTelCtx(), function (chainCtx) {
                        chainCtx[strProcessNext](item);
                    }, function () {
                        itemCtx[strProcessNext](item);
                    });
                },
                update: _doUpdate
            },
            _a[strPause] = function () {
                _processChannelQueue(channelQueue, _getTelCtx(), function (chainCtx) {
                    chainCtx.iterate(function (plugin) {
                        plugin[strPause] && plugin[strPause]();
                    });
                }, null);
            },
            _a[strResume] = function () {
                _processChannelQueue(channelQueue, _getTelCtx(), function (chainCtx) {
                    chainCtx.iterate(function (plugin) {
                        plugin[strResume] && plugin[strResume]();
                    });
                }, null);
            },
            _a[strTeardown] = _doTeardown,
            _a.getChannel = _getChannel,
            _a.flush = function (isAsync, callBack, sendReason, cbTimeout) {
                var waiting = 1;
                var doneIterating = false;
                var cbTimer = null;
                cbTimeout = cbTimeout || 5000;
                function doCallback() {
                    waiting--;
                    if (doneIterating && waiting === 0) {
                        if (cbTimer) {
                            clearTimeout(cbTimer);
                            cbTimer = null;
                        }
                        callBack && callBack(doneIterating);
                        callBack = null;
                    }
                }
                _processChannelQueue(channelQueue, _getTelCtx(), function (chainCtx) {
                    chainCtx.iterate(function (plugin) {
                        if (plugin.flush) {
                            waiting++;
                            var handled_1 = false;
                            if (!plugin.flush(isAsync, function () {
                                handled_1 = true;
                                doCallback();
                            }, sendReason)) {
                                if (!handled_1) {
                                    if (isAsync && cbTimer == null) {
                                        cbTimer = setTimeout(function () {
                                            cbTimer = null;
                                            doCallback();
                                        }, cbTimeout);
                                    }
                                    else {
                                        doCallback();
                                    }
                                }
                            }
                        }
                    });
                }, function () {
                    doneIterating = true;
                    doCallback();
                });
                return true;
            },
            _a._setQueue = function (queue) {
                channelQueue = queue;
            },
            _a);
        return channelController;
    }
    function createChannelQueues(channels, extensions, config, core) {
        var channelQueue = [];
        if (channels) {
            arrForEach(channels, function (queue) { return _addChannelQueue(channelQueue, queue, config, core); });
        }
        if (extensions) {
            var extensionQueue_1 = [];
            arrForEach(extensions, function (plugin) {
                if (plugin.priority > ChannelControllerPriority) {
                    extensionQueue_1.push(plugin);
                }
            });
            _addChannelQueue(channelQueue, extensionQueue_1, config, core);
        }
        return channelQueue;
    }

    function createUnloadHandlerContainer() {
        var handlers = [];
        function _addHandler(handler) {
            if (handler) {
                handlers.push(handler);
            }
        }
        function _runHandlers(unloadCtx, unloadState) {
            arrForEach(handlers, function (handler) {
                try {
                    handler(unloadCtx, unloadState);
                }
                catch (e) {
                    _throwInternal(unloadCtx.diagLog(), 2 , 73 , "Unexpected error calling unload handler - " + dumpObj(e));
                }
            });
            handlers = [];
        }
        return {
            add: _addHandler,
            run: _runHandlers
        };
    }

    var strGetPlugin = "getPlugin";
    var BaseTelemetryPlugin = /** @class */ (function () {
        function BaseTelemetryPlugin() {
            var _self = this;
            var _isinitialized;
            var _rootCtx;
            var _nextPlugin;
            var _unloadHandlerContainer;
            var _hooks;
            _initDefaults();
            dynamicProto(BaseTelemetryPlugin, _self, function (_self) {
                _self.initialize = function (config, core, extensions, pluginChain) {
                    _setDefaults(config, core, pluginChain);
                    _isinitialized = true;
                };
                _self.teardown = function (unloadCtx, unloadState) {
                    var core = _self.core;
                    if (!core || (unloadCtx && core !== unloadCtx.core())) {
                        return;
                    }
                    var result;
                    var unloadDone = false;
                    var theUnloadCtx = unloadCtx || createProcessTelemetryUnloadContext(null, core, _nextPlugin && _nextPlugin[strGetPlugin] ? _nextPlugin[strGetPlugin]() : _nextPlugin);
                    var theUnloadState = unloadState || {
                        reason: 0 ,
                        isAsync: false
                    };
                    function _unloadCallback() {
                        if (!unloadDone) {
                            unloadDone = true;
                            _unloadHandlerContainer.run(theUnloadCtx, unloadState);
                            arrForEach(_hooks, function (fn) {
                                fn.rm();
                            });
                            _hooks = [];
                            if (result === true) {
                                theUnloadCtx.processNext(theUnloadState);
                            }
                            _initDefaults();
                        }
                    }
                    if (!_self[strDoTeardown] || _self[strDoTeardown](theUnloadCtx, theUnloadState, _unloadCallback) !== true) {
                        _unloadCallback();
                    }
                    else {
                        result = true;
                    }
                    return result;
                };
                _self.update = function (updateCtx, updateState) {
                    var core = _self.core;
                    if (!core || (updateCtx && core !== updateCtx.core())) {
                        return;
                    }
                    var result;
                    var updateDone = false;
                    var theUpdateCtx = updateCtx || createProcessTelemetryUpdateContext(null, core, _nextPlugin && _nextPlugin[strGetPlugin] ? _nextPlugin[strGetPlugin]() : _nextPlugin);
                    var theUpdateState = updateState || {
                        reason: 0
                    };
                    function _updateCallback() {
                        if (!updateDone) {
                            updateDone = true;
                            _setDefaults(theUpdateCtx.getCfg(), theUpdateCtx.core(), theUpdateCtx.getNext());
                        }
                    }
                    if (!_self._doUpdate || _self._doUpdate(theUpdateCtx, theUpdateState, _updateCallback) !== true) {
                        _updateCallback();
                    }
                    else {
                        result = true;
                    }
                    return result;
                };
                _self._addHook = function (hooks) {
                    if (hooks) {
                        if (isArray(hooks)) {
                            _hooks = _hooks.concat(hooks);
                        }
                        else {
                            _hooks.push(hooks);
                        }
                    }
                };
                proxyFunctionAs(_self, "_addUnloadCb", function () { return _unloadHandlerContainer; }, "add");
            });
            _self.diagLog = function (itemCtx) {
                return _getTelCtx(itemCtx).diagLog();
            };
            _self[strIsInitialized] = function () {
                return _isinitialized;
            };
            _self.setInitialized = function (isInitialized) {
                _isinitialized = isInitialized;
            };
            _self[strSetNextPlugin] = function (next) {
                _nextPlugin = next;
            };
            _self.processNext = function (env, itemCtx) {
                if (itemCtx) {
                    itemCtx.processNext(env);
                }
                else if (_nextPlugin && isFunction(_nextPlugin.processTelemetry)) {
                    _nextPlugin.processTelemetry(env, null);
                }
            };
            _self._getTelCtx = _getTelCtx;
            function _getTelCtx(currentCtx) {
                if (currentCtx === void 0) { currentCtx = null; }
                var itemCtx = currentCtx;
                if (!itemCtx) {
                    var rootCtx = _rootCtx || createProcessTelemetryContext(null, {}, _self.core);
                    if (_nextPlugin && _nextPlugin[strGetPlugin]) {
                        itemCtx = rootCtx.createNew(null, _nextPlugin[strGetPlugin]);
                    }
                    else {
                        itemCtx = rootCtx.createNew(null, _nextPlugin);
                    }
                }
                return itemCtx;
            }
            function _setDefaults(config, core, pluginChain) {
                if (config) {
                    setValue(config, strExtensionConfig, [], null, isNullOrUndefined);
                }
                if (!pluginChain && core) {
                    pluginChain = core.getProcessTelContext().getNext();
                }
                var nextPlugin = _nextPlugin;
                if (_nextPlugin && _nextPlugin[strGetPlugin]) {
                    nextPlugin = _nextPlugin[strGetPlugin]();
                }
                _self.core = core;
                _rootCtx = createProcessTelemetryContext(pluginChain, config, core, nextPlugin);
            }
            function _initDefaults() {
                _isinitialized = false;
                _self.core = null;
                _rootCtx = null;
                _nextPlugin = null;
                _hooks = [];
                _unloadHandlerContainer = createUnloadHandlerContainer();
            }
        }
        return BaseTelemetryPlugin;
    }());

    var TelemetryInitializerPlugin = /** @class */ (function (_super) {
        __extendsFn(TelemetryInitializerPlugin, _super);
        function TelemetryInitializerPlugin() {
            var _this = _super.call(this) || this;
            _this.identifier = "TelemetryInitializerPlugin";
            _this.priority = 199;
            var _id;
            var _initializers;
            _initDefaults();
            dynamicProto(TelemetryInitializerPlugin, _this, function (_self, _base) {
                _self.addTelemetryInitializer = function (telemetryInitializer) {
                    var theInitializer = {
                        id: _id++,
                        fn: telemetryInitializer
                    };
                    _initializers.push(theInitializer);
                    var handler = {
                        remove: function () {
                            arrForEach(_initializers, function (initializer, idx) {
                                if (initializer.id === theInitializer.id) {
                                    _initializers.splice(idx, 1);
                                    return -1;
                                }
                            });
                        }
                    };
                    return handler;
                };
                _self.processTelemetry = function (item, itemCtx) {
                    var doNotSendItem = false;
                    var telemetryInitializersCount = _initializers.length;
                    for (var i = 0; i < telemetryInitializersCount; ++i) {
                        var telemetryInitializer = _initializers[i];
                        if (telemetryInitializer) {
                            try {
                                if (telemetryInitializer.fn.apply(null, [item]) === false) {
                                    doNotSendItem = true;
                                    break;
                                }
                            }
                            catch (e) {
                                _throwInternal(itemCtx.diagLog(), 1 , 64 , "One of telemetry initializers failed, telemetry item will not be sent: " + getExceptionName(e), { exception: dumpObj(e) }, true);
                            }
                        }
                    }
                    if (!doNotSendItem) {
                        _self.processNext(item, itemCtx);
                    }
                };
                _self[strDoTeardown] = function () {
                    _initDefaults();
                };
            });
            function _initDefaults() {
                _id = 0;
                _initializers = [];
            }
            return _this;
        }
        return TelemetryInitializerPlugin;
    }(BaseTelemetryPlugin));

    var strValidationError = "Plugins must provide initialize method";
    var strNotificationManager = "_notificationManager";
    var strSdkUnloadingError = "SDK is still unloading...";
    var strSdkNotInitialized = "SDK is not initialized";
    var defaultInitConfig = {
        loggingLevelConsole: 1
    };
    function _createPerfManager(core, notificationMgr) {
        return new PerfManager(notificationMgr);
    }
    function _validateExtensions(logger, channelPriority, allExtensions) {
        var coreExtensions = [];
        var extPriorities = {};
        arrForEach(allExtensions, function (ext) {
            if (isNullOrUndefined(ext) || isNullOrUndefined(ext.initialize)) {
                throwError(strValidationError);
            }
            var extPriority = ext.priority;
            var identifier = ext.identifier;
            if (ext && extPriority) {
                if (!isNullOrUndefined(extPriorities[extPriority])) {
                    _warnToConsole(logger, "Two extensions have same priority #" + extPriority + " - " + extPriorities[extPriority] + ", " + identifier);
                }
                else {
                    extPriorities[extPriority] = identifier;
                }
            }
            if (!extPriority || extPriority < channelPriority) {
                coreExtensions.push(ext);
            }
        });
        return {
            all: allExtensions,
            core: coreExtensions
        };
    }
    function _isPluginPresent(thePlugin, plugins) {
        var exists = false;
        arrForEach(plugins, function (plugin) {
            if (plugin === thePlugin) {
                exists = true;
                return -1;
            }
        });
        return exists;
    }
    function _createDummyNotificationManager() {
        var _a;
        return objCreateFn((_a = {},
            _a[strAddNotificationListener] = function (listener) { },
            _a[strRemoveNotificationListener] = function (listener) { },
            _a[strEventsSent] = function (events) { },
            _a[strEventsDiscarded] = function (events, reason) { },
            _a[strEventsSendRequest] = function (sendReason, isAsync) { },
            _a));
    }
    var BaseCore = /** @class */ (function () {
        function BaseCore() {
            var _isInitialized;
            var _eventQueue;
            var _notificationManager;
            var _perfManager;
            var _cfgPerfManager;
            var _cookieManager;
            var _pluginChain;
            var _configExtensions;
            var _coreExtensions;
            var _channelControl;
            var _channelConfig;
            var _channelQueue;
            var _isUnloading;
            var _telemetryInitializerPlugin;
            var _internalLogsEventName;
            var _evtNamespace;
            var _unloadHandlers;
            var _debugListener;
            var _traceCtx;
            var _internalLogPoller = 0;
            dynamicProto(BaseCore, this, function (_self) {
                _initDefaults();
                _self.isInitialized = function () { return _isInitialized; };
                _self.initialize = function (config, extensions, logger, notificationManager) {
                    if (_isUnloading) {
                        throwError(strSdkUnloadingError);
                    }
                    if (_self.isInitialized()) {
                        throwError("Core should not be initialized more than once");
                    }
                    if (!config || isNullOrUndefined(config.instrumentationKey)) {
                        throwError("Please provide instrumentation key");
                    }
                    _notificationManager = notificationManager;
                    _self[strNotificationManager] = notificationManager;
                    _self.config = config || {};
                    _initDebugListener(config);
                    _initPerfManager(config);
                    config.extensions = isNullOrUndefined(config.extensions) ? [] : config.extensions;
                    _initExtConfig(config);
                    if (logger) {
                        _self.logger = logger;
                    }
                    _configExtensions = [];
                    _configExtensions.push.apply(_configExtensions, __spreadArrayFn(__spreadArrayFn([], extensions, false), config.extensions));
                    _channelConfig = (config || {}).channels;
                    _initPluginChain(config, null);
                    if (!_channelQueue || _channelQueue.length === 0) {
                        throwError("No channels available");
                    }
                    _isInitialized = true;
                    _self.releaseQueue();
                };
                _self.getTransmissionControls = function () {
                    var controls = [];
                    if (_channelQueue) {
                        arrForEach(_channelQueue, function (channels) {
                            controls.push(channels.queue);
                        });
                    }
                    return objFreeze(controls);
                };
                _self.track = function (telemetryItem) {
                    setValue(telemetryItem, strIKey, _self.config.instrumentationKey, null, isNotTruthy);
                    setValue(telemetryItem, "time", toISOString(new Date()), null, isNotTruthy);
                    setValue(telemetryItem, "ver", "4.0", null, isNullOrUndefined);
                    if (!_isUnloading && _self.isInitialized()) {
                        _createTelCtx().processNext(telemetryItem);
                    }
                    else {
                        _eventQueue.push(telemetryItem);
                    }
                };
                _self.getProcessTelContext = _createTelCtx;
                _self.getNotifyMgr = function () {
                    if (!_notificationManager) {
                        _notificationManager = _createDummyNotificationManager();
                        _self[strNotificationManager] = _notificationManager;
                    }
                    return _notificationManager;
                };
                _self[strAddNotificationListener] = function (listener) {
                    if (_notificationManager) {
                        _notificationManager[strAddNotificationListener](listener);
                    }
                };
                _self[strRemoveNotificationListener] = function (listener) {
                    if (_notificationManager) {
                        _notificationManager[strRemoveNotificationListener](listener);
                    }
                };
                _self.getCookieMgr = function () {
                    if (!_cookieManager) {
                        _cookieManager = createCookieMgr(_self.config, _self.logger);
                    }
                    return _cookieManager;
                };
                _self.setCookieMgr = function (cookieMgr) {
                    _cookieManager = cookieMgr;
                };
                _self.getPerfMgr = function () {
                    if (!_perfManager && !_cfgPerfManager) {
                        if (_self.config && _self.config.enablePerfMgr && isFunction(_self.config.createPerfMgr)) {
                            _cfgPerfManager = _self.config.createPerfMgr(_self, _self.getNotifyMgr());
                        }
                    }
                    return _perfManager || _cfgPerfManager || getGblPerfMgr();
                };
                _self.setPerfMgr = function (perfMgr) {
                    _perfManager = perfMgr;
                };
                _self.eventCnt = function () {
                    return _eventQueue.length;
                };
                _self.releaseQueue = function () {
                    if (_isInitialized && _eventQueue.length > 0) {
                        var eventQueue = _eventQueue;
                        _eventQueue = [];
                        arrForEach(eventQueue, function (event) {
                            _createTelCtx().processNext(event);
                        });
                    }
                };
                _self.pollInternalLogs = function (eventName) {
                    _internalLogsEventName = eventName || null;
                    var interval = _self.config.diagnosticLogInterval;
                    if (!interval || !(interval > 0)) {
                        interval = 10000;
                    }
                    if (_internalLogPoller) {
                        clearInterval(_internalLogPoller);
                    }
                    _internalLogPoller = setInterval(function () {
                        _flushInternalLogs();
                    }, interval);
                    return _internalLogPoller;
                };
                _self.stopPollingInternalLogs = function () {
                    if (_internalLogPoller) {
                        clearInterval(_internalLogPoller);
                        _internalLogPoller = 0;
                        _flushInternalLogs();
                    }
                };
                proxyFunctions(_self, function () { return _telemetryInitializerPlugin; }, ["addTelemetryInitializer"]);
                _self.unload = function (isAsync, unloadComplete, cbTimeout) {
                    if (isAsync === void 0) { isAsync = true; }
                    if (!_isInitialized) {
                        throwError(strSdkNotInitialized);
                    }
                    if (_isUnloading) {
                        throwError(strSdkUnloadingError);
                    }
                    var unloadState = {
                        reason: 50 ,
                        isAsync: isAsync,
                        flushComplete: false
                    };
                    var processUnloadCtx = createProcessTelemetryUnloadContext(_getPluginChain(), _self);
                    processUnloadCtx.onComplete(function () {
                        _initDefaults();
                        unloadComplete && unloadComplete(unloadState);
                    }, _self);
                    function _doUnload(flushComplete) {
                        unloadState.flushComplete = flushComplete;
                        _isUnloading = true;
                        _unloadHandlers.run(processUnloadCtx, unloadState);
                        _self.stopPollingInternalLogs();
                        processUnloadCtx.processNext(unloadState);
                    }
                    if (!_flushChannels(isAsync, _doUnload, 6 , cbTimeout)) {
                        _doUnload(false);
                    }
                };
                _self.getPlugin = _getPlugin;
                _self.addPlugin = function (plugin, replaceExisting, isAsync, addCb) {
                    if (!plugin) {
                        addCb && addCb(false);
                        _logOrThrowError(strValidationError);
                        return;
                    }
                    var existingPlugin = _getPlugin(plugin.identifier);
                    if (existingPlugin && !replaceExisting) {
                        addCb && addCb(false);
                        _logOrThrowError("Plugin [" + plugin.identifier + "] is already loaded!");
                        return;
                    }
                    var updateState = {
                        reason: 16
                    };
                    function _addPlugin(removed) {
                        _configExtensions.push(plugin);
                        updateState.added = [plugin];
                        _initPluginChain(_self.config, updateState);
                        addCb && addCb(true);
                    }
                    if (existingPlugin) {
                        var removedPlugins_1 = [existingPlugin.plugin];
                        var unloadState = {
                            reason: 2 ,
                            isAsync: !!isAsync
                        };
                        _removePlugins(removedPlugins_1, unloadState, function (removed) {
                            if (!removed) {
                                addCb && addCb(false);
                            }
                            else {
                                updateState.removed = removedPlugins_1;
                                updateState.reason |= 32 ;
                                _addPlugin();
                            }
                        });
                    }
                    else {
                        _addPlugin();
                    }
                };
                _self.evtNamespace = function () {
                    return _evtNamespace;
                };
                _self.flush = _flushChannels;
                _self.getTraceCtx = function (createNew) {
                    if (!_traceCtx) {
                        _traceCtx = createDistributedTraceContext();
                    }
                    return _traceCtx;
                };
                _self.setTraceCtx = function (traceCtx) {
                    _traceCtx = traceCtx || null;
                };
                proxyFunctionAs(_self, "addUnloadCb", function () { return _unloadHandlers; }, "add");
                function _initDefaults() {
                    _isInitialized = false;
                    _self.config = objExtend(true, {}, defaultInitConfig);
                    _self.logger = new DiagnosticLogger(_self.config);
                    _self._extensions = [];
                    _telemetryInitializerPlugin = new TelemetryInitializerPlugin();
                    _eventQueue = [];
                    _notificationManager = null;
                    _perfManager = null;
                    _cfgPerfManager = null;
                    _cookieManager = null;
                    _pluginChain = null;
                    _coreExtensions = null;
                    _configExtensions = [];
                    _channelControl = null;
                    _channelConfig = null;
                    _channelQueue = null;
                    _isUnloading = false;
                    _internalLogsEventName = null;
                    _evtNamespace = createUniqueNamespace("AIBaseCore", true);
                    _unloadHandlers = createUnloadHandlerContainer();
                    _traceCtx = null;
                }
                function _createTelCtx() {
                    return createProcessTelemetryContext(_getPluginChain(), _self.config, _self);
                }
                function _initPluginChain(config, updateState) {
                    var theExtensions = _validateExtensions(_self.logger, ChannelControllerPriority, _configExtensions);
                    _coreExtensions = theExtensions.core;
                    _pluginChain = null;
                    var allExtensions = theExtensions.all;
                    _channelQueue = objFreeze(createChannelQueues(_channelConfig, allExtensions, config, _self));
                    if (_channelControl) {
                        var idx = arrIndexOf(allExtensions, _channelControl);
                        if (idx !== -1) {
                            allExtensions.splice(idx, 1);
                        }
                        idx = arrIndexOf(_coreExtensions, _channelControl);
                        if (idx !== -1) {
                            _coreExtensions.splice(idx, 1);
                        }
                        _channelControl._setQueue(_channelQueue);
                    }
                    else {
                        _channelControl = createChannelControllerPlugin(_channelQueue, _self);
                    }
                    allExtensions.push(_channelControl);
                    _coreExtensions.push(_channelControl);
                    _self._extensions = sortPlugins(allExtensions);
                    _channelControl.initialize(config, _self, allExtensions);
                    initializePlugins(_createTelCtx(), allExtensions);
                    _self._extensions = objFreeze(sortPlugins(_coreExtensions || [])).slice();
                    if (updateState) {
                        _doUpdate(updateState);
                    }
                }
                function _getPlugin(pluginIdentifier) {
                    var theExt = null;
                    var thePlugin = null;
                    arrForEach(_self._extensions, function (ext) {
                        if (ext.identifier === pluginIdentifier && ext !== _channelControl && ext !== _telemetryInitializerPlugin) {
                            thePlugin = ext;
                            return -1;
                        }
                    });
                    if (!thePlugin && _channelControl) {
                        thePlugin = _channelControl.getChannel(pluginIdentifier);
                    }
                    if (thePlugin) {
                        theExt = {
                            plugin: thePlugin,
                            setEnabled: function (enabled) {
                                _getPluginState(thePlugin)[strDisabled] = !enabled;
                            },
                            isEnabled: function () {
                                var pluginState = _getPluginState(thePlugin);
                                return !pluginState[strTeardown] && !pluginState[strDisabled];
                            },
                            remove: function (isAsync, removeCb) {
                                if (isAsync === void 0) { isAsync = true; }
                                var pluginsToRemove = [thePlugin];
                                var unloadState = {
                                    reason: 1 ,
                                    isAsync: isAsync
                                };
                                _removePlugins(pluginsToRemove, unloadState, function (removed) {
                                    if (removed) {
                                        _initPluginChain(_self.config, {
                                            reason: 32 ,
                                            removed: pluginsToRemove
                                        });
                                    }
                                    removeCb && removeCb(removed);
                                });
                            }
                        };
                    }
                    return theExt;
                }
                function _getPluginChain() {
                    if (!_pluginChain) {
                        var extensions = (_coreExtensions || []).slice();
                        if (arrIndexOf(extensions, _telemetryInitializerPlugin) === -1) {
                            extensions.push(_telemetryInitializerPlugin);
                        }
                        _pluginChain = createTelemetryProxyChain(sortPlugins(extensions), _self.config, _self);
                    }
                    return _pluginChain;
                }
                function _removePlugins(thePlugins, unloadState, removeComplete) {
                    if (thePlugins && thePlugins.length > 0) {
                        var unloadChain = createTelemetryProxyChain(thePlugins, _self.config, _self);
                        var unloadCtx = createProcessTelemetryUnloadContext(unloadChain, _self);
                        unloadCtx.onComplete(function () {
                            var removed = false;
                            var newConfigExtensions = [];
                            arrForEach(_configExtensions, function (plugin, idx) {
                                if (!_isPluginPresent(plugin, thePlugins)) {
                                    newConfigExtensions.push(plugin);
                                }
                                else {
                                    removed = true;
                                }
                            });
                            _configExtensions = newConfigExtensions;
                            var newChannelConfig = [];
                            if (_channelConfig) {
                                arrForEach(_channelConfig, function (queue, idx) {
                                    var newQueue = [];
                                    arrForEach(queue, function (channel) {
                                        if (!_isPluginPresent(channel, thePlugins)) {
                                            newQueue.push(channel);
                                        }
                                        else {
                                            removed = true;
                                        }
                                    });
                                    newChannelConfig.push(newQueue);
                                });
                                _channelConfig = newChannelConfig;
                            }
                            removeComplete && removeComplete(removed);
                        });
                        unloadCtx.processNext(unloadState);
                    }
                    else {
                        removeComplete(false);
                    }
                }
                function _flushInternalLogs() {
                    var queue = _self.logger ? _self.logger.queue : [];
                    if (queue) {
                        arrForEach(queue, function (logMessage) {
                            var item = {
                                name: _internalLogsEventName ? _internalLogsEventName : "InternalMessageId: " + logMessage.messageId,
                                iKey: _self.config.instrumentationKey,
                                time: toISOString(new Date()),
                                baseType: _InternalLogMessage.dataType,
                                baseData: { message: logMessage.message }
                            };
                            _self.track(item);
                        });
                        queue.length = 0;
                    }
                }
                function _flushChannels(isAsync, callBack, sendReason, cbTimeout) {
                    if (_channelControl) {
                        return _channelControl.flush(isAsync, callBack, sendReason || 6 , cbTimeout);
                    }
                    callBack && callBack(false);
                    return true;
                }
                function _initDebugListener(config) {
                    if (config.disableDbgExt === true && _debugListener) {
                        _notificationManager[strRemoveNotificationListener](_debugListener);
                        _debugListener = null;
                    }
                    if (_notificationManager && !_debugListener && config.disableDbgExt !== true) {
                        _debugListener = getDebugListener(config);
                        _notificationManager[strAddNotificationListener](_debugListener);
                    }
                }
                function _initPerfManager(config) {
                    if (!config.enablePerfMgr && _cfgPerfManager) {
                        _cfgPerfManager = null;
                    }
                    if (config.enablePerfMgr) {
                        setValue(_self.config, "createPerfMgr", _createPerfManager);
                    }
                }
                function _initExtConfig(config) {
                    var extConfig = getSetValue(config, strExtensionConfig);
                    extConfig.NotificationManager = _notificationManager;
                }
                function _doUpdate(updateState) {
                    var updateCtx = createProcessTelemetryUpdateContext(_getPluginChain(), _self);
                    if (!_self._updateHook || _self._updateHook(updateCtx, updateState) !== true) {
                        updateCtx.processNext(updateState);
                    }
                }
                function _logOrThrowError(message) {
                    var logger = _self.logger;
                    if (logger) {
                        _throwInternal(logger, 2 , 73 , message);
                    }
                    else {
                        throwError(message);
                    }
                }
            });
        }
        return BaseCore;
    }());

    function _runListeners(listeners, name, isAsync, callback) {
        arrForEach(listeners, function (listener) {
            if (listener && listener[name]) {
                if (isAsync) {
                    setTimeout(function () { return callback(listener); }, 0);
                }
                else {
                    try {
                        callback(listener);
                    }
                    catch (e) {
                    }
                }
            }
        });
    }
    var NotificationManager = /** @class */ (function () {
        function NotificationManager(config) {
            this.listeners = [];
            var perfEvtsSendAll = !!(config || {}).perfEvtsSendAll;
            dynamicProto(NotificationManager, this, function (_self) {
                _self[strAddNotificationListener] = function (listener) {
                    _self.listeners.push(listener);
                };
                _self[strRemoveNotificationListener] = function (listener) {
                    var index = arrIndexOf(_self.listeners, listener);
                    while (index > -1) {
                        _self.listeners.splice(index, 1);
                        index = arrIndexOf(_self.listeners, listener);
                    }
                };
                _self[strEventsSent] = function (events) {
                    _runListeners(_self.listeners, strEventsSent, true, function (listener) {
                        listener[strEventsSent](events);
                    });
                };
                _self[strEventsDiscarded] = function (events, reason) {
                    _runListeners(_self.listeners, strEventsDiscarded, true, function (listener) {
                        listener[strEventsDiscarded](events, reason);
                    });
                };
                _self[strEventsSendRequest] = function (sendReason, isAsync) {
                    _runListeners(_self.listeners, strEventsSendRequest, isAsync, function (listener) {
                        listener[strEventsSendRequest](sendReason, isAsync);
                    });
                };
                _self[strPerfEvent] = function (perfEvent) {
                    if (perfEvent) {
                        if (perfEvtsSendAll || !perfEvent.isChildEvt()) {
                            _runListeners(_self.listeners, strPerfEvent, false, function (listener) {
                                if (perfEvent.isAsync) {
                                    setTimeout(function () { return listener[strPerfEvent](perfEvent); }, 0);
                                }
                                else {
                                    listener[strPerfEvent](perfEvent);
                                }
                            });
                        }
                    }
                };
            });
        }
        return NotificationManager;
    }());

    var AppInsightsCore = /** @class */ (function (_super) {
        __extendsFn(AppInsightsCore, _super);
        function AppInsightsCore() {
            var _this = _super.call(this) || this;
            dynamicProto(AppInsightsCore, _this, function (_self, _base) {
                _self.initialize = function (config, extensions, logger, notificationManager) {
                    _base.initialize(config, extensions, logger || new DiagnosticLogger(config), notificationManager || new NotificationManager(config));
                };
                _self.track = function (telemetryItem) {
                    doPerf(_self.getPerfMgr(), function () { return "AppInsightsCore:track"; }, function () {
                        if (telemetryItem === null) {
                            _notifyInvalidEvent(telemetryItem);
                            throwError("Invalid telemetry item");
                        }
                        _validateTelemetryItem(telemetryItem);
                        _base.track(telemetryItem);
                    }, function () { return ({ item: telemetryItem }); }, !(telemetryItem.sync));
                };
                function _validateTelemetryItem(telemetryItem) {
                    if (isNullOrUndefined(telemetryItem.name)) {
                        _notifyInvalidEvent(telemetryItem);
                        throwError("telemetry name required");
                    }
                }
                function _notifyInvalidEvent(telemetryItem) {
                    var manager = _self.getNotifyMgr();
                    if (manager) {
                        manager.eventsDiscarded([telemetryItem], 2 );
                    }
                }
            });
            return _this;
        }
        return AppInsightsCore;
    }(BaseCore));

    var LoggingSeverity = createEnumStyle({
        CRITICAL: 1 ,
        WARNING: 2
    });
    var _InternalMessageId = createEnumStyle({
        BrowserDoesNotSupportLocalStorage: 0 ,
        BrowserCannotReadLocalStorage: 1 ,
        BrowserCannotReadSessionStorage: 2 ,
        BrowserCannotWriteLocalStorage: 3 ,
        BrowserCannotWriteSessionStorage: 4 ,
        BrowserFailedRemovalFromLocalStorage: 5 ,
        BrowserFailedRemovalFromSessionStorage: 6 ,
        CannotSendEmptyTelemetry: 7 ,
        ClientPerformanceMathError: 8 ,
        ErrorParsingAISessionCookie: 9 ,
        ErrorPVCalc: 10 ,
        ExceptionWhileLoggingError: 11 ,
        FailedAddingTelemetryToBuffer: 12 ,
        FailedMonitorAjaxAbort: 13 ,
        FailedMonitorAjaxDur: 14 ,
        FailedMonitorAjaxOpen: 15 ,
        FailedMonitorAjaxRSC: 16 ,
        FailedMonitorAjaxSend: 17 ,
        FailedMonitorAjaxGetCorrelationHeader: 18 ,
        FailedToAddHandlerForOnBeforeUnload: 19 ,
        FailedToSendQueuedTelemetry: 20 ,
        FailedToReportDataLoss: 21 ,
        FlushFailed: 22 ,
        MessageLimitPerPVExceeded: 23 ,
        MissingRequiredFieldSpecification: 24 ,
        NavigationTimingNotSupported: 25 ,
        OnError: 26 ,
        SessionRenewalDateIsZero: 27 ,
        SenderNotInitialized: 28 ,
        StartTrackEventFailed: 29 ,
        StopTrackEventFailed: 30 ,
        StartTrackFailed: 31 ,
        StopTrackFailed: 32 ,
        TelemetrySampledAndNotSent: 33 ,
        TrackEventFailed: 34 ,
        TrackExceptionFailed: 35 ,
        TrackMetricFailed: 36 ,
        TrackPVFailed: 37 ,
        TrackPVFailedCalc: 38 ,
        TrackTraceFailed: 39 ,
        TransmissionFailed: 40 ,
        FailedToSetStorageBuffer: 41 ,
        FailedToRestoreStorageBuffer: 42 ,
        InvalidBackendResponse: 43 ,
        FailedToFixDepricatedValues: 44 ,
        InvalidDurationValue: 45 ,
        TelemetryEnvelopeInvalid: 46 ,
        CreateEnvelopeError: 47 ,
        CannotSerializeObject: 48 ,
        CannotSerializeObjectNonSerializable: 49 ,
        CircularReferenceDetected: 50 ,
        ClearAuthContextFailed: 51 ,
        ExceptionTruncated: 52 ,
        IllegalCharsInName: 53 ,
        ItemNotInArray: 54 ,
        MaxAjaxPerPVExceeded: 55 ,
        MessageTruncated: 56 ,
        NameTooLong: 57 ,
        SampleRateOutOfRange: 58 ,
        SetAuthContextFailed: 59 ,
        SetAuthContextFailedAccountName: 60 ,
        StringValueTooLong: 61 ,
        StartCalledMoreThanOnce: 62 ,
        StopCalledWithoutStart: 63 ,
        TelemetryInitializerFailed: 64 ,
        TrackArgumentsNotSpecified: 65 ,
        UrlTooLong: 66 ,
        SessionStorageBufferFull: 67 ,
        CannotAccessCookie: 68 ,
        IdTooLong: 69 ,
        InvalidEvent: 70 ,
        FailedMonitorAjaxSetRequestHeader: 71 ,
        SendBrowserInfoOnUserInit: 72 ,
        PluginException: 73 ,
        NotificationException: 74 ,
        SnippetScriptLoadFailure: 99 ,
        InvalidInstrumentationKey: 100 ,
        CannotParseAiBlobValue: 101 ,
        InvalidContentBlob: 102 ,
        TrackPageActionEventFailed: 103 ,
        FailedAddingCustomDefinedRequestContext: 104 ,
        InMemoryStorageBufferFull: 105 ,
        InstrumentationKeyDeprecation: 106
    });

    var aiInstrumentHooks = "_aiHooks";
    var cbNames = [
        "req", "rsp", "hkErr", "fnErr"
    ];
    function _arrLoop(arr, fn) {
        if (arr) {
            for (var lp = 0; lp < arr.length; lp++) {
                if (fn(arr[lp], lp)) {
                    break;
                }
            }
        }
    }
    function _doCallbacks(hooks, callDetails, cbArgs, hookCtx, type) {
        if (type >= 0  && type <= 2 ) {
            _arrLoop(hooks, function (hook, idx) {
                var cbks = hook.cbks;
                var cb = cbks[cbNames[type]];
                if (cb) {
                    callDetails.ctx = function () {
                        var ctx = hookCtx[idx] = (hookCtx[idx] || {});
                        return ctx;
                    };
                    try {
                        cb.apply(callDetails.inst, cbArgs);
                    }
                    catch (err) {
                        var orgEx = callDetails.err;
                        try {
                            var hookErrorCb = cbks[cbNames[2 ]];
                            if (hookErrorCb) {
                                callDetails.err = err;
                                hookErrorCb.apply(callDetails.inst, cbArgs);
                            }
                        }
                        catch (e) {
                        }
                        finally {
                            callDetails.err = orgEx;
                        }
                    }
                }
            });
        }
    }
    function _createFunctionHook(aiHook) {
        return function () {
            var funcThis = this;
            var orgArgs = arguments;
            var hooks = aiHook.h;
            var funcArgs = {
                name: aiHook.n,
                inst: funcThis,
                ctx: null,
                set: _replaceArg
            };
            var hookCtx = [];
            var cbArgs = _createArgs([funcArgs], orgArgs);
            funcArgs.evt = getGlobalInst("event");
            function _createArgs(target, theArgs) {
                _arrLoop(theArgs, function (arg) {
                    target.push(arg);
                });
                return target;
            }
            function _replaceArg(idx, value) {
                orgArgs = _createArgs([], orgArgs);
                orgArgs[idx] = value;
                cbArgs = _createArgs([funcArgs], orgArgs);
            }
            _doCallbacks(hooks, funcArgs, cbArgs, hookCtx, 0 );
            var theFunc = aiHook.f;
            if (theFunc) {
                try {
                    funcArgs.rslt = theFunc.apply(funcThis, orgArgs);
                }
                catch (err) {
                    funcArgs.err = err;
                    _doCallbacks(hooks, funcArgs, cbArgs, hookCtx, 3 );
                    throw err;
                }
            }
            _doCallbacks(hooks, funcArgs, cbArgs, hookCtx, 1 );
            return funcArgs.rslt;
        };
    }
    function _getOwner(target, name, checkPrototype) {
        var owner = null;
        if (target) {
            if (hasOwnProperty(target, name)) {
                owner = target;
            }
            else if (checkPrototype) {
                owner = _getOwner(_getObjProto$1(target), name, false);
            }
        }
        return owner;
    }
    function InstrumentProto(target, funcName, callbacks) {
        if (target) {
            return InstrumentFunc(target[strShimPrototype], funcName, callbacks, false);
        }
        return null;
    }
    function InstrumentProtos(target, funcNames, callbacks) {
        if (target) {
            return InstrumentFuncs(target[strShimPrototype], funcNames, callbacks, false);
        }
        return null;
    }
    function _createInstrumentHook(owner, funcName, fn, callbacks) {
        var aiHook = fn && fn[aiInstrumentHooks];
        if (!aiHook) {
            aiHook = {
                i: 0,
                n: funcName,
                f: fn,
                h: []
            };
            var newFunc = _createFunctionHook(aiHook);
            newFunc[aiInstrumentHooks] = aiHook;
            owner[funcName] = newFunc;
        }
        var theHook = {
            id: aiHook.i,
            cbks: callbacks,
            rm: function () {
                var id = this.id;
                _arrLoop(aiHook.h, function (hook, idx) {
                    if (hook.id === id) {
                        aiHook.h.splice(idx, 1);
                        return 1;
                    }
                });
            }
        };
        aiHook.i++;
        aiHook.h.push(theHook);
        return theHook;
    }
    function InstrumentFunc(target, funcName, callbacks, checkPrototype) {
        if (checkPrototype === void 0) { checkPrototype = true; }
        if (target && funcName && callbacks) {
            var owner = _getOwner(target, funcName, checkPrototype);
            if (owner) {
                var fn = owner[funcName];
                if (typeof fn === strShimFunction) {
                    return _createInstrumentHook(owner, funcName, fn, callbacks);
                }
            }
        }
        return null;
    }
    function InstrumentFuncs(target, funcNames, callbacks, checkPrototype) {
        if (checkPrototype === void 0) { checkPrototype = true; }
        var hooks = null;
        _arrLoop(funcNames, function (funcName) {
            var hook = InstrumentFunc(target, funcName, callbacks, checkPrototype);
            if (hook) {
                if (!hooks) {
                    hooks = [];
                }
                hooks.push(hook);
            }
        });
        return hooks;
    }
    function InstrumentEvent(target, evtName, callbacks, checkPrototype) {
        if (target && evtName && callbacks) {
            var owner = _getOwner(target, evtName, checkPrototype) || target;
            if (owner) {
                return _createInstrumentHook(owner, evtName, owner[evtName], callbacks);
            }
        }
        return null;
    }

    exports.AppInsightsCore = AppInsightsCore;
    exports.BaseCore = BaseCore;
    exports.BaseTelemetryPlugin = BaseTelemetryPlugin;
    exports.CoreUtils = CoreUtils;
    exports.DiagnosticLogger = DiagnosticLogger;
    exports.EventHelper = EventHelper;
    exports.EventsDiscardedReason = EventsDiscardedReason;
    exports.InstrumentEvent = InstrumentEvent;
    exports.InstrumentFunc = InstrumentFunc;
    exports.InstrumentFuncs = InstrumentFuncs;
    exports.InstrumentProto = InstrumentProto;
    exports.InstrumentProtos = InstrumentProtos;
    exports.LoggingSeverity = LoggingSeverity;
    exports.MinChannelPriorty = MinChannelPriorty;
    exports.NotificationManager = NotificationManager;
    exports.PerfEvent = PerfEvent;
    exports.PerfManager = PerfManager;
    exports.ProcessTelemetryContext = ProcessTelemetryContext;
    exports.Undefined = Undefined;
    exports._InternalLogMessage = _InternalLogMessage;
    exports._InternalMessageId = _InternalMessageId;
    exports.__getRegisteredEvents = __getRegisteredEvents;
    exports._legacyCookieMgr = _legacyCookieMgr;
    exports._logInternalMessage = _logInternalMessage;
    exports._throwInternal = _throwInternal;
    exports._warnToConsole = _warnToConsole;
    exports.addEventHandler = addEventHandler;
    exports.addEventListeners = addEventListeners;
    exports.addPageHideEventListener = addPageHideEventListener;
    exports.addPageShowEventListener = addPageShowEventListener;
    exports.addPageUnloadEventListener = addPageUnloadEventListener;
    exports.areCookiesSupported = areCookiesSupported;
    exports.arrForEach = arrForEach;
    exports.arrIndexOf = arrIndexOf;
    exports.arrMap = arrMap;
    exports.arrReduce = arrReduce;
    exports.attachEvent = attachEvent;
    exports.canUseCookies = canUseCookies;
    exports.createClassFromInterface = createClassFromInterface;
    exports.createCookieMgr = createCookieMgr;
    exports.createEnumMap = createEnumMap;
    exports.createEnumStyle = createEnumStyle;
    exports.createProcessTelemetryContext = createProcessTelemetryContext;
    exports.createTraceParent = createTraceParent;
    exports.createUniqueNamespace = createUniqueNamespace;
    exports.createUnloadHandlerContainer = createUnloadHandlerContainer;
    exports.createValueMap = createValueMap;
    exports.dateNow = dateNow;
    exports.deepFreeze = deepFreeze;
    exports.deleteCookie = deleteCookie;
    exports.detachEvent = detachEvent;
    exports.disableCookies = disableCookies;
    exports.doPerf = doPerf;
    exports.dumpObj = dumpObj;
    exports.eventOff = eventOff;
    exports.eventOn = eventOn;
    exports.findMetaTag = findMetaTag;
    exports.findNamedServerTiming = findNamedServerTiming;
    exports.findW3cTraceParent = findW3cTraceParent;
    exports.formatTraceParent = formatTraceParent;
    exports.generateW3CId = generateW3CId;
    exports.getConsole = getConsole;
    exports.getCookie = getCookie;
    exports.getCrypto = getCrypto;
    exports.getDebugExt = getDebugExt;
    exports.getDebugListener = getDebugListener;
    exports.getDocument = getDocument;
    exports.getExceptionName = getExceptionName;
    exports.getGblPerfMgr = getGblPerfMgr;
    exports.getGlobal = getGlobal;
    exports.getGlobalInst = getGlobalInst;
    exports.getHistory = getHistory;
    exports.getIEVersion = getIEVersion;
    exports.getJSON = getJSON;
    exports.getLocation = getLocation;
    exports.getMsCrypto = getMsCrypto;
    exports.getNavigator = getNavigator;
    exports.getPerformance = getPerformance;
    exports.getSetValue = getSetValue;
    exports.getWindow = getWindow;
    exports.hasDocument = hasDocument;
    exports.hasHistory = hasHistory;
    exports.hasJSON = hasJSON;
    exports.hasNavigator = hasNavigator;
    exports.hasOwnProperty = hasOwnProperty;
    exports.hasWindow = hasWindow;
    exports.initializePlugins = initializePlugins;
    exports.isArray = isArray;
    exports.isBeaconsSupported = isBeaconsSupported;
    exports.isBoolean = isBoolean;
    exports.isDate = isDate;
    exports.isError = isError;
    exports.isFetchSupported = isFetchSupported;
    exports.isFunction = isFunction;
    exports.isIE = isIE;
    exports.isNotNullOrUndefined = isNotNullOrUndefined;
    exports.isNotTruthy = isNotTruthy;
    exports.isNotUndefined = isNotUndefined;
    exports.isNullOrUndefined = isNullOrUndefined;
    exports.isNumber = isNumber;
    exports.isObject = isObject;
    exports.isReactNative = isReactNative;
    exports.isSafari = isSafari;
    exports.isSampledFlag = isSampledFlag;
    exports.isString = isString;
    exports.isSymbol = isSymbol;
    exports.isTruthy = isTruthy;
    exports.isTypeof = isTypeof;
    exports.isUndefined = isUndefined;
    exports.isValidSpanId = isValidSpanId;
    exports.isValidTraceId = isValidTraceId;
    exports.isValidTraceParent = isValidTraceParent;
    exports.isXhrSupported = isXhrSupported;
    exports.mergeEvtNamespace = mergeEvtNamespace;
    exports.mwcRandom32 = mwcRandom32;
    exports.mwcRandomSeed = mwcRandomSeed;
    exports.newGuid = newGuid;
    exports.newId = newId;
    exports.normalizeJsName = normalizeJsName;
    exports.objCreate = objCreateFn;
    exports.objDefineAccessors = objDefineAccessors;
    exports.objExtend = objExtend;
    exports.objForEachKey = objForEachKey;
    exports.objFreeze = objFreeze;
    exports.objKeys = objKeys;
    exports.objSeal = objSeal;
    exports.objToString = objToString;
    exports.optimizeObject = optimizeObject;
    exports.parseTraceParent = parseTraceParent;
    exports.perfNow = perfNow;
    exports.proxyAssign = proxyAssign;
    exports.proxyFunctionAs = proxyFunctionAs;
    exports.proxyFunctions = proxyFunctions;
    exports.random32 = random32;
    exports.randomValue = randomValue;
    exports.removeEventHandler = removeEventHandler;
    exports.removeEventListeners = removeEventListeners;
    exports.removePageHideEventListener = removePageHideEventListener;
    exports.removePageShowEventListener = removePageShowEventListener;
    exports.removePageUnloadEventListener = removePageUnloadEventListener;
    exports.safeGetCookieMgr = safeGetCookieMgr;
    exports.safeGetLogger = safeGetLogger;
    exports.setCookie = setCookie;
    exports.setEnableEnvMocks = setEnableEnvMocks;
    exports.setGblPerfMgr = setGblPerfMgr;
    exports.setValue = setValue;
    exports.sortPlugins = sortPlugins;
    exports.strContains = strContains;
    exports.strEndsWith = strEndsWith;
    exports.strFunction = strShimFunction;
    exports.strObject = strShimObject;
    exports.strPrototype = strShimPrototype;
    exports.strStartsWith = strStartsWith;
    exports.strTrim = strTrim;
    exports.strUndefined = strShimUndefined;
    exports.throwError = throwError;
    exports.toISOString = toISOString;
    exports.uaDisallowsSameSiteNone = uaDisallowsSameSiteNone;
    exports.unloadComponents = unloadComponents;
    exports.useXDomainRequest = useXDomainRequest;

    (function(obj, prop, descriptor) { /* ai_es3_polyfil defineProperty */ var func = Object["defineProperty"]; if (func) { try { return func(obj, prop, descriptor); } catch(e) { /* IE8 defines defineProperty, but will throw */ } } if (descriptor && typeof descriptor.value !== undefined) { obj[prop] = descriptor.value; } return obj; })(exports, '__esModule', { value: true });

}));
//# sourceMappingURL=applicationinsights-core-js.js.map


/***/ }),

/***/ 7424:
/***/ (function(__unused_webpack_module, exports) {

/*!
 * Microsoft Application Insights JavaScript SDK - Shim functions, 2.0.1
 * Copyright (c) Microsoft and contributors. All rights reserved.
 */
(function (global, factory) {
     true ? factory(exports) :
    0;
})(this, (function (exports) { 'use strict';

    var strShimFunction = "function";
    var strShimObject = "object";
    var strShimUndefined = "undefined";
    var strShimPrototype = "prototype";
    var strShimHasOwnProperty = "hasOwnProperty";
    var strDefault = "default";
    var ObjClass = Object;
    var ObjProto = ObjClass[strShimPrototype];
    var ObjAssign = ObjClass["assign"];
    var ObjCreate = ObjClass["create"];
    var ObjDefineProperty = ObjClass["defineProperty"];
    var ObjHasOwnProperty = ObjProto[strShimHasOwnProperty];

    var _cachedGlobal = null;
    /**
     * Returns the current global scope object, for a normal web page this will be the current
     * window, for a Web Worker this will be current worker global scope via "self". The internal
     * implementation returns the first available instance object in the following order
     * - globalThis (New standard)
     * - self (Will return the current window instance for supported browsers)
     * - window (fallback for older browser implementations)
     * - global (NodeJS standard)
     * - <null> (When all else fails)
     * While the return type is a Window for the normal case, not all environments will support all
     * of the properties or functions.
     */
    function getGlobal(useCached) {
        if (useCached === void 0) { useCached = true; }
        if (!_cachedGlobal || !useCached) {
            if (typeof globalThis !== strShimUndefined && globalThis) {
                _cachedGlobal = globalThis;
            }
            if (typeof self !== strShimUndefined && self) {
                _cachedGlobal = self;
            }
            if (typeof window !== strShimUndefined && window) {
                _cachedGlobal = window;
            }
            if (typeof global !== strShimUndefined && global) {
                _cachedGlobal = global;
            }
        }
        return _cachedGlobal;
    }
    function throwTypeError(message) {
        throw new TypeError(message);
    }
    /**
     * Creates an object that has the specified prototype, and that optionally contains specified properties. This helper exists to avoid adding a polyfil
     * for older browsers that do not define Object.create eg. ES3 only, IE8 just in case any page checks for presence/absence of the prototype implementation.
     * Note: For consistency this will not use the Object.create implementation if it exists as this would cause a testing requirement to test with and without the implementations
     * @param obj Object to use as a prototype. May be null
     */
    function objCreateFn(obj) {
        var func = ObjCreate;
        // Use build in Object.create
        if (func) {
            // Use Object create method if it exists
            return func(obj);
        }
        if (obj == null) {
            return {};
        }
        var type = typeof obj;
        if (type !== strShimObject && type !== strShimFunction) {
            throwTypeError("Object prototype may only be an Object:" + obj);
        }
        function tmpFunc() { }
        tmpFunc[strShimPrototype] = obj;
        return new tmpFunc();
    }

    // Most of these functions have been directly shamelessly "lifted" from the https://github.com/@microsoft/tslib and
    // modified to be ES3 compatible and applying several minification and tree-shaking techniques so that Application Insights
    // can successfully use TypeScript "importHelpers" which imports tslib during compilation but it will use these at runtime
    // Which is also why all of the functions have not been included as Application Insights currently doesn't use or require
    // them.
    var SymbolObj = (getGlobal() || {})["Symbol"];
    var ReflectObj = (getGlobal() || {})["Reflect"];
    var __hasReflect = !!ReflectObj;
    var strDecorate = "decorate";
    var strMetadata = "metadata";
    var strGetOwnPropertySymbols = "getOwnPropertySymbols";
    var strIterator = "iterator";
    var __objAssignFnImpl = function (t) {
        // tslint:disable-next-line: ban-comma-operator
        for (var s, i = 1, n = arguments.length; i < n; i++) {
            s = arguments[i];
            for (var p in s) {
                if (ObjProto[strShimHasOwnProperty].call(s, p)) {
                    t[p] = s[p];
                }
            }
        }
        return t;
    };
    var __assignFn = ObjAssign || __objAssignFnImpl;
    // tslint:disable-next-line: only-arrow-functions
    var extendStaticsFn = function (d, b) {
        extendStaticsFn = ObjClass["setPrototypeOf"] ||
            // tslint:disable-next-line: only-arrow-functions
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            // tslint:disable-next-line: only-arrow-functions
            function (d, b) {
                for (var p in b) {
                    if (b[strShimHasOwnProperty](p)) {
                        d[p] = b[p];
                    }
                }
            };
        return extendStaticsFn(d, b);
    };
    function __extendsFn(d, b) {
        if (typeof b !== strShimFunction && b !== null) {
            throwTypeError("Class extends value " + String(b) + " is not a constructor or null");
        }
        extendStaticsFn(d, b);
        function __() { this.constructor = d; }
        // tslint:disable-next-line: ban-comma-operator
        d[strShimPrototype] = b === null ? objCreateFn(b) : (__[strShimPrototype] = b[strShimPrototype], new __());
    }
    function __restFn(s, e) {
        var t = {};
        for (var k in s) {
            if (ObjHasOwnProperty.call(s, k) && e.indexOf(k) < 0) {
                t[k] = s[k];
            }
        }
        if (s != null && typeof ObjClass[strGetOwnPropertySymbols] === strShimFunction) {
            for (var i = 0, p = ObjClass[strGetOwnPropertySymbols](s); i < p.length; i++) {
                if (e.indexOf(p[i]) < 0 && ObjProto["propertyIsEnumerable"].call(s, p[i])) {
                    t[p[i]] = s[p[i]];
                }
            }
        }
        return t;
    }
    function __decorateFn(decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = ObjClass["getOwnPropertyDescriptor"](target, key) : desc, d;
        if (__hasReflect && typeof ReflectObj[strDecorate] === strShimFunction) {
            r = ReflectObj[strDecorate](decorators, target, key, desc);
        }
        else {
            for (var i = decorators.length - 1; i >= 0; i--) {
                // eslint-disable-next-line no-cond-assign
                if (d = decorators[i]) {
                    r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
                }
            }
        }
        // tslint:disable-next-line:ban-comma-operator
        return c > 3 && r && ObjDefineProperty(target, key, r), r;
    }
    function __paramFn(paramIndex, decorator) {
        return function (target, key) {
            decorator(target, key, paramIndex);
        };
    }
    function __metadataFn(metadataKey, metadataValue) {
        if (__hasReflect && ReflectObj[strMetadata] === strShimFunction) {
            return ReflectObj[strMetadata](metadataKey, metadataValue);
        }
    }
    function __exportStarFn(m, o) {
        for (var p in m) {
            if (p !== strDefault && !ObjHasOwnProperty.call(o, p)) {
                __createBindingFn(o, m, p);
            }
        }
    }
    function __createBindingFn(o, m, k, k2) {
        if (k2 === undefined) {
            k2 = k;
        }
        if (ObjCreate) {
            ObjDefineProperty(o, k2, {
                enumerable: true,
                get: function () {
                    return m[k];
                }
            });
        }
        else {
            o[k2] = m[k];
        }
    }
    function __valuesFn(o) {
        var s = typeof SymbolObj === strShimFunction && SymbolObj[strIterator], m = s && o[s], i = 0;
        if (m) {
            return m.call(o);
        }
        if (o && typeof o.length === "number") {
            return {
                next: function () {
                    if (o && i >= o.length) {
                        o = void 0;
                    }
                    return { value: o && o[i++], done: !o };
                }
            };
        }
        throwTypeError(s ? "Object is not iterable." : "Symbol.iterator is not defined.");
    }
    function __readFn(o, n) {
        var m = typeof SymbolObj === strShimFunction && o[SymbolObj[strIterator]];
        if (!m) {
            return o;
        }
        var i = m.call(o), r, ar = [], e;
        try {
            while ((n === void 0 || n-- > 0) && !(r = i.next()).done) {
                ar.push(r.value);
            }
        }
        catch (error) {
            e = {
                error: error
            };
        }
        finally {
            try {
                // tslint:disable-next-line:no-conditional-assignment
                if (r && !r.done && (m = i["return"])) {
                    m.call(i);
                }
            }
            finally {
                if (e) {
                    // eslint-disable-next-line no-unsafe-finally
                    throw e.error;
                }
            }
        }
        return ar;
    }
    /** @deprecated */
    function __spreadArraysFn() {
        var theArgs = arguments;
        // Calculate new total size
        for (var s = 0, i = 0, il = theArgs.length; i < il; i++) {
            s += theArgs[i].length;
        }
        // Create new full array
        for (var r = Array(s), k = 0, i = 0; i < il; i++) {
            for (var a = theArgs[i], j = 0, jl = a.length; j < jl; j++, k++) {
                r[k] = a[j];
            }
        }
        return r;
    }
    function __spreadArrayFn(to, from) {
        for (var i = 0, il = from.length, j = to.length; i < il; i++, j++) {
            to[j] = from[i];
        }
        return to;
    }
    function __makeTemplateObjectFn(cooked, raw) {
        if (ObjDefineProperty) {
            ObjDefineProperty(cooked, "raw", { value: raw });
        }
        else {
            cooked.raw = raw;
        }
        return cooked;
    }
    function __importStarFn(mod) {
        if (mod && mod.__esModule) {
            return mod;
        }
        var result = {};
        if (mod != null) {
            for (var k in mod) {
                if (k !== strDefault && Object.prototype.hasOwnProperty.call(mod, k)) {
                    __createBindingFn(result, mod, k);
                }
            }
        }
        // Set default module
        if (ObjCreate) {
            ObjDefineProperty(result, strDefault, { enumerable: true, value: mod });
        }
        else {
            result[strDefault] = mod;
        }
        return result;
    }
    function __importDefaultFn(mod) {
        return (mod && mod.__esModule) ? mod : { strDefault: mod };
    }

    function __exposeGlobalTsLib() {
        var globalObj = getGlobal() || {};
        // tslint:disable: only-arrow-functions
        (function (root, assignFn, extendsFn, createBindingFn) {
            // Assign the globally scoped versions of the functions -- used when consuming individual ts files
            // If check is to support NativeScript where these are marked as readonly
            if (!root.__assign) {
                root.__assign = ObjAssign || assignFn;
            }
            if (!root.__extends) {
                root.__extends = extendsFn;
            }
            if (!root.__createBinding) {
                root.__createBinding = createBindingFn;
            }
        })(globalObj, __assignFn, __extendsFn, __createBindingFn);
        // Assign local variables that will be used for embedded scenarios, if check is to support NativeScript where these are marked as readonly
        if (!__assign) {
            __assign = globalObj.__assign;
        }
        if (!__extends) {
            __extends = globalObj.__extends;
        }
        if (!__createBinding) {
            __createBinding = globalObj.__createBinding;
        }
    }

    exports.ObjAssign = ObjAssign;
    exports.ObjClass = ObjClass;
    exports.ObjCreate = ObjCreate;
    exports.ObjDefineProperty = ObjDefineProperty;
    exports.ObjHasOwnProperty = ObjHasOwnProperty;
    exports.ObjProto = ObjProto;
    exports.__assignFn = __assignFn;
    exports.__createBindingFn = __createBindingFn;
    exports.__decorateFn = __decorateFn;
    exports.__exportStarFn = __exportStarFn;
    exports.__exposeGlobalTsLib = __exposeGlobalTsLib;
    exports.__extendsFn = __extendsFn;
    exports.__importDefaultFn = __importDefaultFn;
    exports.__importStarFn = __importStarFn;
    exports.__makeTemplateObjectFn = __makeTemplateObjectFn;
    exports.__metadataFn = __metadataFn;
    exports.__paramFn = __paramFn;
    exports.__readFn = __readFn;
    exports.__restFn = __restFn;
    exports.__spreadArrayFn = __spreadArrayFn;
    exports.__spreadArraysFn = __spreadArraysFn;
    exports.__valuesFn = __valuesFn;
    exports.getGlobal = getGlobal;
    exports.objCreateFn = objCreateFn;
    exports.strDefault = strDefault;
    exports.strShimFunction = strShimFunction;
    exports.strShimHasOwnProperty = strShimHasOwnProperty;
    exports.strShimObject = strShimObject;
    exports.strShimPrototype = strShimPrototype;
    exports.strShimUndefined = strShimUndefined;
    exports.throwTypeError = throwTypeError;

    (function(obj, prop, descriptor) { /* ai_es3_polyfil defineProperty */ var func = Object["defineProperty"]; if (func) { try { return func(obj, prop, descriptor); } catch(e) { /* IE8 defines defineProperty, but will throw */ } } if (descriptor && typeof descriptor.value !== undefined) { obj[prop] = descriptor.value; } return obj; })(exports, '__esModule', { value: true });

}));


/***/ }),

/***/ 1331:
/***/ (function(module) {

/*!
 * Microsoft Dynamic Proto Utility, 1.1.6
 * Copyright (c) Microsoft and contributors. All rights reserved.
 */
(function (global, factory) {
     true ? module.exports = factory() :
    0;
})(this, (function () { 'use strict';

    /**
     * Constant string defined to support minimization
     * @ignore
     */
    var Constructor = 'constructor';
    /**
     * Constant string defined to support minimization
     * @ignore
     */
    var Prototype = 'prototype';
    /**
     * Constant string defined to support minimization
     * @ignore
     */
    var strFunction = 'function';
    /**
     * Used to define the name of the instance function lookup table
     * @ignore
     */
    var DynInstFuncTable = '_dynInstFuncs';
    /**
     * Name used to tag the dynamic prototype function
     * @ignore
     */
    var DynProxyTag = '_isDynProxy';
    /**
     * Name added to a prototype to define the dynamic prototype "class" name used to lookup the function table
     * @ignore
     */
    var DynClassName = '_dynClass';
    /**
     * Prefix added to the classname to avoid any name clashes with other instance level properties
     * @ignore
     */
    var DynClassNamePrefix = '_dynCls$';
    /**
     * A tag which is used to check if we have already to attempted to set the instance function if one is not present
     * @ignore
     */
    var DynInstChkTag = '_dynInstChk';
    /**
     * A tag which is used to check if we are allows to try and set an instance function is one is not present. Using the same
     * tag name as the function level but a different const name for readability only.
     */
    var DynAllowInstChkTag = DynInstChkTag;
    /**
     * The global (imported) instances where the global performance options are stored
     */
    var DynProtoDefaultOptions = '_dfOpts';
    /**
     * Value used as the name of a class when it cannot be determined
     * @ignore
     */
    var UnknownValue = '_unknown_';
    /**
     * Constant string defined to support minimization
     * @ignore
     */
    var str__Proto = "__proto__";
    /**
     * The polyfill version of __proto__ so that it doesn't cause issues for anyone not expecting it to exist
     */
    var DynProtoBaseProto = "_dyn" + str__Proto;
    /**
     * Track the current prototype for IE8 as you can't look back to get the prototype
     */
    var DynProtoCurrent = "_dynInstProto";
    /**
     * Constant string defined to support minimization
     * @ignore
     */
    var strUseBaseInst = 'useBaseInst';
    /**
     * Constant string defined to support minimization
     * @ignore
     */
    var strSetInstFuncs = 'setInstFuncs';
    var Obj = Object;
    /**
     * Pre-lookup to check if we are running on a modern browser (i.e. not IE8)
     * @ignore
     */
    var _objGetPrototypeOf = Obj["getPrototypeOf"];
    /**
     * Pre-lookup to check for the existence of this function
     */
    var _objGetOwnProps = Obj["getOwnPropertyNames"];
    /**
     * Internal Global used to generate a unique dynamic class name, every new class will increase this value
     * @ignore
     */
    var _dynamicNames = 0;
    /**
     * Helper to check if the object contains a property of the name
     * @ignore
     */
    function _hasOwnProperty(obj, prop) {
        return obj && Obj[Prototype].hasOwnProperty.call(obj, prop);
    }
    /**
     * Helper used to check whether the target is an Object prototype or Array prototype
     * @ignore
     */
    function _isObjectOrArrayPrototype(target) {
        return target && (target === Obj[Prototype] || target === Array[Prototype]);
    }
    /**
     * Helper used to check whether the target is an Object prototype, Array prototype or Function prototype
     * @ignore
     */
    function _isObjectArrayOrFunctionPrototype(target) {
        return _isObjectOrArrayPrototype(target) || target === Function[Prototype];
    }
    /**
     * Helper used to get the prototype of the target object as getPrototypeOf is not available in an ES3 environment.
     * @ignore
     */
    function _getObjProto(target) {
        var newProto;
        if (target) {
            // This method doesn't exist in older browsers (e.g. IE8)
            if (_objGetPrototypeOf) {
                return _objGetPrototypeOf(target);
            }
            var curProto = target[str__Proto] || target[Prototype] || (target[Constructor] ? target[Constructor][Prototype] : null);
            // Using the pre-calculated value as IE8 doesn't support looking up the prototype of a prototype and thus fails for more than 1 base class
            newProto = target[DynProtoBaseProto] || curProto;
            if (!_hasOwnProperty(target, DynProtoBaseProto)) {
                // As this prototype doesn't have this property then this is from an inherited class so newProto is the base to return so save it
                // so we can look it up value (which for a multiple hierarchy dynamicProto will be the base class)
                delete target[DynProtoCurrent]; // Delete any current value allocated to this instance so we pick up the value from prototype hierarchy
                newProto = target[DynProtoBaseProto] = target[DynProtoCurrent] || target[DynProtoBaseProto];
                target[DynProtoCurrent] = curProto;
            }
        }
        return newProto;
    }
    /**
     * Helper to get the properties of an object, including none enumerable ones as functions on a prototype in ES6
     * are not enumerable.
     * @param target
     */
    function _forEachProp(target, func) {
        var props = [];
        if (_objGetOwnProps) {
            props = _objGetOwnProps(target);
        }
        else {
            for (var name_1 in target) {
                if (typeof name_1 === "string" && _hasOwnProperty(target, name_1)) {
                    props.push(name_1);
                }
            }
        }
        if (props && props.length > 0) {
            for (var lp = 0; lp < props.length; lp++) {
                func(props[lp]);
            }
        }
    }
    /**
     * Helper function to check whether the provided function name is a potential candidate for dynamic
     * callback and prototype generation.
     * @param target The target object, may be a prototype or class object
     * @param funcName The function name
     * @param skipOwn Skips the check for own property
     * @ignore
     */
    function _isDynamicCandidate(target, funcName, skipOwn) {
        return (funcName !== Constructor && typeof target[funcName] === strFunction && (skipOwn || _hasOwnProperty(target, funcName)));
    }
    /**
     * Helper to throw a TypeError exception
     * @param message the message
     * @ignore
     */
    function _throwTypeError(message) {
        throw new TypeError("DynamicProto: " + message);
    }
    /**
     * Returns a collection of the instance functions that are defined directly on the thisTarget object, it does
     * not return any inherited functions
     * @param thisTarget The object to get the instance functions from
     * @ignore
     */
    function _getInstanceFuncs(thisTarget) {
        // Get the base proto
        var instFuncs = {};
        // Save any existing instance functions
        _forEachProp(thisTarget, function (name) {
            // Don't include any dynamic prototype instances - as we only want the real functions
            if (!instFuncs[name] && _isDynamicCandidate(thisTarget, name, false)) {
                // Create an instance callback for passing the base function to the caller
                instFuncs[name] = thisTarget[name];
            }
        });
        return instFuncs;
    }
    /**
     * Returns whether the value is included in the array
     * @param values The array of values
     * @param value  The value
     */
    function _hasVisited(values, value) {
        for (var lp = values.length - 1; lp >= 0; lp--) {
            if (values[lp] === value) {
                return true;
            }
        }
        return false;
    }
    /**
     * Returns an object that contains callback functions for all "base/super" functions, this is used to "save"
     * enabling calling super.xxx() functions without requiring that the base "class" has defined a prototype references
     * @param target The current instance
     * @ignore
     */
    function _getBaseFuncs(classProto, thisTarget, instFuncs, useBaseInst) {
        function _instFuncProxy(target, funcHost, funcName) {
            var theFunc = funcHost[funcName];
            if (theFunc[DynProxyTag] && useBaseInst) {
                // grab and reuse the hosted looking function (if available) otherwise the original passed function
                var instFuncTable = target[DynInstFuncTable] || {};
                if (instFuncTable[DynAllowInstChkTag] !== false) {
                    theFunc = (instFuncTable[funcHost[DynClassName]] || {})[funcName] || theFunc;
                }
            }
            return function () {
                // eslint-disable-next-line prefer-rest-params
                return theFunc.apply(target, arguments);
            };
        }
        // Start creating a new baseFuncs by creating proxies for the instance functions (as they may get replaced)
        var baseFuncs = {};
        _forEachProp(instFuncs, function (name) {
            // Create an instance callback for passing the base function to the caller
            baseFuncs[name] = _instFuncProxy(thisTarget, instFuncs, name);
        });
        // Get the base prototype functions
        var baseProto = _getObjProto(classProto);
        var visited = [];
        // Don't include base object functions for Object, Array or Function
        while (baseProto && !_isObjectArrayOrFunctionPrototype(baseProto) && !_hasVisited(visited, baseProto)) {
            // look for prototype functions
            _forEachProp(baseProto, function (name) {
                // Don't include any dynamic prototype instances - as we only want the real functions
                // For IE 7/8 the prototype lookup doesn't provide the full chain so we need to bypass the 
                // hasOwnProperty check we get all of the methods, main difference is that IE7/8 doesn't return
                // the Object prototype methods while bypassing the check
                if (!baseFuncs[name] && _isDynamicCandidate(baseProto, name, !_objGetPrototypeOf)) {
                    // Create an instance callback for passing the base function to the caller
                    baseFuncs[name] = _instFuncProxy(thisTarget, baseProto, name);
                }
            });
            // We need to find all possible functions that might be overloaded by walking the entire prototype chain
            // This avoids the caller from needing to check whether it's direct base class implements the function or not
            // by walking the entire chain it simplifies the usage and issues from upgrading any of the base classes.
            visited.push(baseProto);
            baseProto = _getObjProto(baseProto);
        }
        return baseFuncs;
    }
    function _getInstFunc(target, funcName, proto, currentDynProtoProxy) {
        var instFunc = null;
        // We need to check whether the class name is defined directly on this prototype otherwise
        // it will walk the proto chain and return any parent proto classname.
        if (target && _hasOwnProperty(proto, DynClassName)) {
            var instFuncTable = target[DynInstFuncTable] || {};
            instFunc = (instFuncTable[proto[DynClassName]] || {})[funcName];
            if (!instFunc) {
                // Avoid stack overflow from recursive calling the same function
                _throwTypeError("Missing [" + funcName + "] " + strFunction);
            }
            // We have the instance function, lets check it we can speed up further calls
            // by adding the instance function back directly on the instance (avoiding the dynamic func lookup)
            if (!instFunc[DynInstChkTag] && instFuncTable[DynAllowInstChkTag] !== false) {
                // If the instance already has an instance function we can't replace it
                var canAddInst = !_hasOwnProperty(target, funcName);
                // Get current prototype
                var objProto = _getObjProto(target);
                var visited = [];
                // Lookup the function starting at the top (instance level prototype) and traverse down, if the first matching function
                // if nothing is found or if the first hit is a dynamic proto instance then we can safely add an instance shortcut
                while (canAddInst && objProto && !_isObjectArrayOrFunctionPrototype(objProto) && !_hasVisited(visited, objProto)) {
                    var protoFunc = objProto[funcName];
                    if (protoFunc) {
                        canAddInst = (protoFunc === currentDynProtoProxy);
                        break;
                    }
                    // We need to find all possible initial functions to ensure that we don't bypass a valid override function
                    visited.push(objProto);
                    objProto = _getObjProto(objProto);
                }
                try {
                    if (canAddInst) {
                        // This instance doesn't have an instance func and the class hierarchy does have a higher level prototype version
                        // so it's safe to directly assign for any subsequent calls (for better performance)
                        target[funcName] = instFunc;
                    }
                    // Block further attempts to set the instance function for any
                    instFunc[DynInstChkTag] = 1;
                }
                catch (e) {
                    // Don't crash if the object is readonly or the runtime doesn't allow changing this
                    // And set a flag so we don't try again for any function
                    instFuncTable[DynAllowInstChkTag] = false;
                }
            }
        }
        return instFunc;
    }
    function _getProtoFunc(funcName, proto, currentDynProtoProxy) {
        var protoFunc = proto[funcName];
        // Check that the prototype function is not a self reference -- try to avoid stack overflow!
        if (protoFunc === currentDynProtoProxy) {
            // It is so lookup the base prototype
            protoFunc = _getObjProto(proto)[funcName];
        }
        if (typeof protoFunc !== strFunction) {
            _throwTypeError("[" + funcName + "] is not a " + strFunction);
        }
        return protoFunc;
    }
    /**
     * Add the required dynamic prototype methods to the the class prototype
     * @param proto - The class prototype
     * @param className - The instance classname
     * @param target - The target instance
     * @param baseInstFuncs - The base instance functions
     * @param setInstanceFunc - Flag to allow prototype function to reset the instance function if one does not exist
     * @ignore
     */
    function _populatePrototype(proto, className, target, baseInstFuncs, setInstanceFunc) {
        function _createDynamicPrototype(proto, funcName) {
            var dynProtoProxy = function () {
                // Use the instance or prototype function
                var instFunc = _getInstFunc(this, funcName, proto, dynProtoProxy) || _getProtoFunc(funcName, proto, dynProtoProxy);
                // eslint-disable-next-line prefer-rest-params
                return instFunc.apply(this, arguments);
            };
            // Tag this function as a proxy to support replacing dynamic proxy elements (primary use case is for unit testing
            // via which can dynamically replace the prototype function reference)
            dynProtoProxy[DynProxyTag] = 1;
            return dynProtoProxy;
        }
        if (!_isObjectOrArrayPrototype(proto)) {
            var instFuncTable = target[DynInstFuncTable] = target[DynInstFuncTable] || {};
            var instFuncs_1 = instFuncTable[className] = (instFuncTable[className] || {}); // fetch and assign if as it may not exist yet
            // Set whether we are allow to lookup instances, if someone has set to false then do not re-enable
            if (instFuncTable[DynAllowInstChkTag] !== false) {
                instFuncTable[DynAllowInstChkTag] = !!setInstanceFunc;
            }
            _forEachProp(target, function (name) {
                // Only add overridden functions
                if (_isDynamicCandidate(target, name, false) && target[name] !== baseInstFuncs[name]) {
                    // Save the instance Function to the lookup table and remove it from the instance as it's not a dynamic proto function
                    instFuncs_1[name] = target[name];
                    delete target[name];
                    // Add a dynamic proto if one doesn't exist or if a prototype function exists and it's not a dynamic one
                    if (!_hasOwnProperty(proto, name) || (proto[name] && !proto[name][DynProxyTag])) {
                        proto[name] = _createDynamicPrototype(proto, name);
                    }
                }
            });
        }
    }
    /**
     * Checks whether the passed prototype object appears to be correct by walking the prototype hierarchy of the instance
     * @param classProto The class prototype instance
     * @param thisTarget The current instance that will be checked whether the passed prototype instance is in the hierarchy
     * @ignore
     */
    function _checkPrototype(classProto, thisTarget) {
        // This method doesn't existing in older browsers (e.g. IE8)
        if (_objGetPrototypeOf) {
            // As this is primarily a coding time check, don't bother checking if running in IE8 or lower
            var visited = [];
            var thisProto = _getObjProto(thisTarget);
            while (thisProto && !_isObjectArrayOrFunctionPrototype(thisProto) && !_hasVisited(visited, thisProto)) {
                if (thisProto === classProto) {
                    return true;
                }
                // This avoids the caller from needing to check whether it's direct base class implements the function or not
                // by walking the entire chain it simplifies the usage and issues from upgrading any of the base classes.
                visited.push(thisProto);
                thisProto = _getObjProto(thisProto);
            }
            return false;
        }
        // If objGetPrototypeOf doesn't exist then just assume everything is ok.
        return true;
    }
    /**
     * Gets the current prototype name using the ES6 name if available otherwise falling back to a use unknown as the name.
     * It's not critical for this to return a name, it's used to decorate the generated unique name for easier debugging only.
     * @param target
     * @param unknownValue
     * @ignore
     */
    function _getObjName(target, unknownValue) {
        if (_hasOwnProperty(target, Prototype)) {
            // Look like a prototype
            return target.name || unknownValue || UnknownValue;
        }
        return (((target || {})[Constructor]) || {}).name || unknownValue || UnknownValue;
    }
    /**
     * Helper function when creating dynamic (inline) functions for classes, this helper performs the following tasks :-
     * - Saves references to all defined base class functions
     * - Calls the delegateFunc with the current target (this) and a base object reference that can be used to call all "super" functions.
     * - Will populate the class prototype for all overridden functions to support class extension that call the prototype instance.
     * Callers should use this helper when declaring all function within the constructor of a class, as mentioned above the delegateFunc is
     * passed both the target "this" and an object that can be used to call any base (super) functions, using this based object in place of
     * super.XXX() (which gets expanded to _super.prototype.XXX()) provides a better minification outcome and also ensures the correct "this"
     * context is maintained as TypeScript creates incorrect references using super.XXXX() for dynamically defined functions i.e. Functions
     * defined in the constructor or some other function (rather than declared as complete typescript functions).
     * ### Usage
     * ```typescript
     * import dynamicProto from "@microsoft/dynamicproto-js";
     * class ExampleClass extends BaseClass {
     *     constructor() {
     *         dynamicProto(ExampleClass, this, (_self, base) => {
     *             // This will define a function that will be converted to a prototype function
     *             _self.newFunc = () => {
     *                 // Access any "this" instance property
     *                 if (_self.someProperty) {
     *                     ...
     *                 }
     *             }
     *             // This will define a function that will be converted to a prototype function
     *             _self.myFunction = () => {
     *                 // Access any "this" instance property
     *                 if (_self.someProperty) {
     *                     // Call the base version of the function that we are overriding
     *                     base.myFunction();
     *                 }
     *                 ...
     *             }
     *             _self.initialize = () => {
     *                 ...
     *             }
     *             // Warnings: While the following will work as _self is simply a reference to
     *             // this, if anyone overrides myFunction() the overridden will be called first
     *             // as the normal JavaScript method resolution will occur and the defined
     *             // _self.initialize() function is actually gets removed from the instance and
     *             // a proxy prototype version is created to reference the created method.
     *             _self.initialize();
     *         });
     *     }
     * }
     * ```
     * @typeparam DPType This is the generic type of the class, used to keep intellisense valid
     * @typeparam DPCls The type that contains the prototype of the current class
     * @param theClass - This is the current class instance which contains the prototype for the current class
     * @param target - The current "this" (target) reference, when the class has been extended this.prototype will not be the 'theClass' value.
     * @param delegateFunc - The callback function (closure) that will create the dynamic function
     * @param options - Additional options to configure how the dynamic prototype operates
     */
    function dynamicProto(theClass, target, delegateFunc, options) {
        // Make sure that the passed theClass argument looks correct
        if (!_hasOwnProperty(theClass, Prototype)) {
            _throwTypeError("theClass is an invalid class definition.");
        }
        // Quick check to make sure that the passed theClass argument looks correct (this is a common copy/paste error)
        var classProto = theClass[Prototype];
        if (!_checkPrototype(classProto, target)) {
            _throwTypeError("[" + _getObjName(theClass) + "] is not in class hierarchy of [" + _getObjName(target) + "]");
        }
        var className = null;
        if (_hasOwnProperty(classProto, DynClassName)) {
            // Only grab the class name if it's defined on this prototype (i.e. don't walk the prototype chain)
            className = classProto[DynClassName];
        }
        else {
            // As not all browser support name on the prototype creating a unique dynamic one if we have not already
            // assigned one, so we can use a simple string as the lookup rather than an object for the dynamic instance
            // function table lookup.
            className = DynClassNamePrefix + _getObjName(theClass, "_") + "$" + _dynamicNames;
            _dynamicNames++;
            classProto[DynClassName] = className;
        }
        var perfOptions = dynamicProto[DynProtoDefaultOptions];
        var useBaseInst = !!perfOptions[strUseBaseInst];
        if (useBaseInst && options && options[strUseBaseInst] !== undefined) {
            useBaseInst = !!options[strUseBaseInst];
        }
        // Get the current instance functions
        var instFuncs = _getInstanceFuncs(target);
        // Get all of the functions for any base instance (before they are potentially overridden)
        var baseFuncs = _getBaseFuncs(classProto, target, instFuncs, useBaseInst);
        // Execute the delegate passing in both the current target "this" and "base" function references
        // Note casting the same type as we don't actually have the base class here and this will provide some intellisense support
        delegateFunc(target, baseFuncs);
        // Don't allow setting instance functions for older IE instances
        var setInstanceFunc = !!_objGetPrototypeOf && !!perfOptions[strSetInstFuncs];
        if (setInstanceFunc && options) {
            setInstanceFunc = !!options[strSetInstFuncs];
        }
        // Populate the Prototype for any overridden instance functions
        _populatePrototype(classProto, className, target, instFuncs, setInstanceFunc !== false);
    }
    /**
     * Exposes the default global options to allow global configuration, if the global values are disabled these will override
     * any passed values. This is primarily exposed to support unit-testing without the need for individual classes to expose
     * their internal usage of dynamic proto.
     */
    var perfDefaults = {
        setInstFuncs: true,
        useBaseInst: true
    };
    // And expose for testing
    dynamicProto[DynProtoDefaultOptions] = perfDefaults;

    return dynamicProto;

}));
//# sourceMappingURL=dynamicproto-js.js.map


/***/ })

};
;
//# sourceMappingURL=317.main.js.map