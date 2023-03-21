exports.id = 985;
exports.ids = [985];
exports.modules = {

/***/ 4985:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

/*!
 * 1DS JS SDK POST plugin, 3.2.3
 * Copyright (c) Microsoft and contributors. All rights reserved.
 * (Microsoft Internal Only)
 */
(function (global, factory) {
     true ? factory(exports, __webpack_require__(7253), __webpack_require__(6866), __webpack_require__(1479)) :
    0;
})(this, (function (exports, applicationinsightsShims, dynamicProto, _1dsCoreJs) { 'use strict';

    function _interopDefaultLegacy (e) { return e && typeof e === 'object' && 'default' in e ? e["default"] : e; }

    var dynamicProto__default = /*#__PURE__*/_interopDefaultLegacy(dynamicProto);

    var RT_PROFILE = "REAL_TIME";
    var NRT_PROFILE = "NEAR_REAL_TIME";
    var BE_PROFILE = "BEST_EFFORT";

    var Method = "POST";
    var DisabledPropertyName = "Microsoft_ApplicationInsights_BypassAjaxInstrumentation";
    var strDropped = "drop";
    var strSending = "send";
    var strRequeue = "requeue";
    var strResponseFail = "rspFail";
    var strOther = "oth";
    var defaultCacheControl = "no-cache, no-store";
    var defaultContentType = "application/x-json-stream";
    var strCacheControl = "cache-control";
    var strContentTypeHeader = "content-type";
    var strKillTokensHeader = "kill-tokens";
    var strKillDurationHeader = "kill-duration";
    var strKillDurationSecondsHeader = "kill-duration-seconds";
    var strTimeDeltaHeader = "time-delta-millis";
    var strClientVersion = "client-version";
    var strClientId = "client-id";
    var strTimeDeltaToApply = "time-delta-to-apply-millis";
    var strUploadTime = "upload-time";
    var strApiKey = "apikey";
    var strMsaDeviceTicket = "AuthMsaDeviceTicket";
    var strAuthXToken = "AuthXToken";
    var strNoResponseBody = "NoResponseBody";
    var strMsfpc = "msfpc";

    function _getEventMsfpc(theEvent) {
        var intWeb = ((theEvent.ext || {})["intweb"]);
        if (intWeb && _1dsCoreJs.isValueAssigned(intWeb[strMsfpc])) {
            return intWeb[strMsfpc];
        }
        return null;
    }
    function _getMsfpc(theEvents) {
        var msfpc = null;
        for (var lp = 0; msfpc === null && lp < theEvents.length; lp++) {
            msfpc = _getEventMsfpc(theEvents[lp]);
        }
        return msfpc;
    }
    var EventBatch = /** @class */ (function () {
        function EventBatch(iKey, addEvents) {
            var events = addEvents ? [].concat(addEvents) : [];
            var _self = this;
            var _msfpc = _getMsfpc(events);
            _self.iKey = function () {
                return iKey;
            };
            _self.Msfpc = function () {
                return _msfpc || "";
            };
            _self.count = function () {
                return events.length;
            };
            _self.events = function () {
                return events;
            };
            _self.addEvent = function (theEvent) {
                if (theEvent) {
                    events.push(theEvent);
                    if (!_msfpc) {
                        _msfpc = _getEventMsfpc(theEvent);
                    }
                    return true;
                }
                return false;
            };
            _self.split = function (fromEvent, numEvents) {
                var theEvents;
                if (fromEvent < events.length) {
                    var cnt = events.length - fromEvent;
                    if (!_1dsCoreJs.isNullOrUndefined(numEvents)) {
                        cnt = numEvents < cnt ? numEvents : cnt;
                    }
                    theEvents = events.splice(fromEvent, cnt);
                    _msfpc = _getMsfpc(events);
                }
                return new EventBatch(iKey, theEvents);
            };
        }
        EventBatch.create = function (iKey, theEvents) {
            return new EventBatch(iKey, theEvents);
        };
        return EventBatch;
    }());

    var _MAX_STRING_JOINS = 20;
    var RequestSizeLimitBytes = 3984588;
    var BeaconRequestSizeLimitBytes = 65000;
    var MaxRecordSize = 2000000;
    var MaxBeaconRecordSize = Math.min(MaxRecordSize, BeaconRequestSizeLimitBytes);
    var metadata = "metadata";
    var f = "f";
    var rCheckDot = /\./;
    var Serializer = /** @class */ (function () {
        function Serializer(perfManager, valueSanitizer, stringifyObjects, enableCompoundKey) {
            var strData = "data";
            var strBaseData = "baseData";
            var strExt = "ext";
            var _checkForCompoundkey = !!enableCompoundKey;
            var _processSubMetaData = true;
            var _theSanitizer = valueSanitizer;
            var _isReservedCache = {};
            dynamicProto__default(Serializer, this, function (_self) {
                _self.createPayload = function (retryCnt, isTeardown, isSync, useSendBeacon, sendReason, sendType) {
                    return {
                        apiKeys: [],
                        payloadBlob: "",
                        overflow: null,
                        sizeExceed: [],
                        failedEvts: [],
                        batches: [],
                        numEvents: 0,
                        retryCnt: retryCnt,
                        isTeardown: isTeardown,
                        isSync: isSync,
                        isBeacon: useSendBeacon,
                        sendType: sendType,
                        sendReason: sendReason
                    };
                };
                _self.appendPayload = function (payload, theBatch, maxEventsPerBatch) {
                    var canAddEvents = payload && theBatch && !payload.overflow;
                    if (canAddEvents) {
                        _1dsCoreJs.doPerf(perfManager, function () { return "Serializer:appendPayload"; }, function () {
                            var theEvents = theBatch.events();
                            var payloadBlob = payload.payloadBlob;
                            var payloadEvents = payload.numEvents;
                            var eventsAdded = false;
                            var sizeExceeded = [];
                            var failedEvts = [];
                            var isBeaconPayload = payload.isBeacon;
                            var requestMaxSize = isBeaconPayload ? BeaconRequestSizeLimitBytes : RequestSizeLimitBytes;
                            var recordMaxSize = isBeaconPayload ? MaxBeaconRecordSize : MaxRecordSize;
                            var lp = 0;
                            var joinCount = 0;
                            while (lp < theEvents.length) {
                                var theEvent = theEvents[lp];
                                if (theEvent) {
                                    if (payloadEvents >= maxEventsPerBatch) {
                                        payload.overflow = theBatch.split(lp);
                                        break;
                                    }
                                    var eventBlob = _self.getEventBlob(theEvent);
                                    if (eventBlob && eventBlob.length <= recordMaxSize) {
                                        var blobLength = eventBlob.length;
                                        var currentSize = payloadBlob.length;
                                        if (currentSize + blobLength > requestMaxSize) {
                                            payload.overflow = theBatch.split(lp);
                                            break;
                                        }
                                        if (payloadBlob) {
                                            payloadBlob += "\n";
                                        }
                                        payloadBlob += eventBlob;
                                        joinCount++;
                                        if (joinCount > _MAX_STRING_JOINS) {
                                            payloadBlob.substr(0, 1);
                                            joinCount = 0;
                                        }
                                        eventsAdded = true;
                                        payloadEvents++;
                                    }
                                    else {
                                        if (eventBlob) {
                                            sizeExceeded.push(theEvent);
                                        }
                                        else {
                                            failedEvts.push(theEvent);
                                        }
                                        theEvents.splice(lp, 1);
                                        lp--;
                                    }
                                }
                                lp++;
                            }
                            if (sizeExceeded && sizeExceeded.length > 0) {
                                payload.sizeExceed.push(EventBatch.create(theBatch.iKey(), sizeExceeded));
                            }
                            if (failedEvts && failedEvts.length > 0) {
                                payload.failedEvts.push(EventBatch.create(theBatch.iKey(), failedEvts));
                            }
                            if (eventsAdded) {
                                payload.batches.push(theBatch);
                                payload.payloadBlob = payloadBlob;
                                payload.numEvents = payloadEvents;
                                var apiKey = theBatch.iKey();
                                if (_1dsCoreJs.arrIndexOf(payload.apiKeys, apiKey) === -1) {
                                    payload.apiKeys.push(apiKey);
                                }
                            }
                        }, function () { return ({ payload: payload, theBatch: { iKey: theBatch.iKey(), evts: theBatch.events() }, max: maxEventsPerBatch }); });
                    }
                    return canAddEvents;
                };
                _self.getEventBlob = function (eventData) {
                    try {
                        return _1dsCoreJs.doPerf(perfManager, function () { return "Serializer.getEventBlob"; }, function () {
                            var serializedEvent = {};
                            serializedEvent.name = eventData.name;
                            serializedEvent.time = eventData.time;
                            serializedEvent.ver = eventData.ver;
                            serializedEvent.iKey = "o:" + _1dsCoreJs.getTenantId(eventData.iKey);
                            var serializedExt = {};
                            var eventExt = eventData[strExt];
                            if (eventExt) {
                                serializedEvent[strExt] = serializedExt;
                                _1dsCoreJs.objForEachKey(eventExt, function (key, value) {
                                    var data = serializedExt[key] = {};
                                    _processPathKeys(value, data, "ext." + key, true, null, null, true);
                                });
                            }
                            var serializedData = serializedEvent[strData] = {};
                            serializedData.baseType = eventData.baseType;
                            var serializedBaseData = serializedData[strBaseData] = {};
                            _processPathKeys(eventData.baseData, serializedBaseData, strBaseData, false, [strBaseData], function (pathKeys, name, value) {
                                _addJSONPropertyMetaData(serializedExt, pathKeys, name, value);
                            }, _processSubMetaData);
                            _processPathKeys(eventData.data, serializedData, strData, false, [], function (pathKeys, name, value) {
                                _addJSONPropertyMetaData(serializedExt, pathKeys, name, value);
                            }, _processSubMetaData);
                            return JSON.stringify(serializedEvent);
                        }, function () { return ({ item: eventData }); });
                    }
                    catch (e) {
                        return null;
                    }
                };
                function _isReservedField(path, name) {
                    var result = _isReservedCache[path];
                    if (result === undefined) {
                        if (path.length >= 7) {
                            result = _1dsCoreJs.strStartsWith(path, "ext.metadata") || _1dsCoreJs.strStartsWith(path, "ext.web");
                        }
                        _isReservedCache[path] = result;
                    }
                    return result;
                }
                function _processPathKeys(srcObj, target, thePath, checkReserved, metadataPathKeys, metadataCallback, processSubKeys) {
                    _1dsCoreJs.objForEachKey(srcObj, function (key, srcValue) {
                        var prop = null;
                        if (srcValue || _1dsCoreJs.isValueAssigned(srcValue)) {
                            var path = thePath;
                            var name_1 = key;
                            var theMetaPathKeys = metadataPathKeys;
                            var destObj = target;
                            if (_checkForCompoundkey && !checkReserved && rCheckDot.test(key)) {
                                var subKeys = key.split(".");
                                var keyLen = subKeys.length;
                                if (keyLen > 1) {
                                    if (theMetaPathKeys) {
                                        theMetaPathKeys = theMetaPathKeys.slice();
                                    }
                                    for (var lp = 0; lp < keyLen - 1; lp++) {
                                        var subKey = subKeys[lp];
                                        destObj = destObj[subKey] = destObj[subKey] || {};
                                        path += "." + subKey;
                                        if (theMetaPathKeys) {
                                            theMetaPathKeys.push(subKey);
                                        }
                                    }
                                    name_1 = subKeys[keyLen - 1];
                                }
                            }
                            var isReserved = checkReserved && _isReservedField(path);
                            if (!isReserved && _theSanitizer && _theSanitizer.handleField(path, name_1)) {
                                prop = _theSanitizer.value(path, name_1, srcValue, stringifyObjects);
                            }
                            else {
                                prop = _1dsCoreJs.sanitizeProperty(name_1, srcValue, stringifyObjects);
                            }
                            if (prop) {
                                var newValue = prop.value;
                                destObj[name_1] = newValue;
                                if (metadataCallback) {
                                    metadataCallback(theMetaPathKeys, name_1, prop);
                                }
                                if (processSubKeys && typeof newValue === "object" && !_1dsCoreJs.isArray(newValue)) {
                                    var newPath = theMetaPathKeys;
                                    if (newPath) {
                                        newPath = newPath.slice();
                                        newPath.push(name_1);
                                    }
                                    _processPathKeys(srcValue, newValue, path + "." + name_1, checkReserved, newPath, metadataCallback, processSubKeys);
                                }
                            }
                        }
                    });
                }
            });
        }
        return Serializer;
    }());
    function _addJSONPropertyMetaData(json, propKeys, name, propertyValue) {
        if (propertyValue && json) {
            var encodedTypeValue = _1dsCoreJs.getCommonSchemaMetaData(propertyValue.value, propertyValue.kind, propertyValue.propertyType);
            if (encodedTypeValue > -1) {
                var metaData = json[metadata];
                if (!metaData) {
                    metaData = json[metadata] = { f: {} };
                }
                var metaTarget = metaData[f];
                if (!metaTarget) {
                    metaTarget = metaData[f] = {};
                }
                if (propKeys) {
                    for (var lp = 0; lp < propKeys.length; lp++) {
                        var key = propKeys[lp];
                        if (!metaTarget[key]) {
                            metaTarget[key] = { f: {} };
                        }
                        var newTarget = metaTarget[key][f];
                        if (!newTarget) {
                            newTarget = metaTarget[key][f] = {};
                        }
                        metaTarget = newTarget;
                    }
                }
                metaTarget = metaTarget[name] = {};
                if (_1dsCoreJs.isArray(propertyValue.value)) {
                    metaTarget["a"] = {
                        t: encodedTypeValue
                    };
                }
                else {
                    metaTarget["t"] = encodedTypeValue;
                }
            }
        }
    }

    var RandomizationLowerThreshold = 0.8;
    var RandomizationUpperThreshold = 1.2;
    var BaseBackoff = 3000;
    var MaxBackoff = 600000;
    function retryPolicyShouldRetryForStatus(httpStatusCode) {
        return !((httpStatusCode >= 300 && httpStatusCode < 500 && httpStatusCode != 408 && httpStatusCode != 429)
            || (httpStatusCode == 501)
            || (httpStatusCode == 505));
    }
    function retryPolicyGetMillisToBackoffForRetry(retriesSoFar) {
        var waitDuration = 0;
        var minBackoff = BaseBackoff * RandomizationLowerThreshold;
        var maxBackoff = BaseBackoff * RandomizationUpperThreshold;
        var randomBackoff = Math.floor(Math.random() * (maxBackoff - minBackoff)) + minBackoff;
        waitDuration = Math.pow(2, retriesSoFar) * randomBackoff;
        return Math.min(waitDuration, MaxBackoff);
    }

    var SecToMsMultiplier = 1000;
    var KillSwitch = /** @class */ (function () {
        function KillSwitch() {
            var _killedTokenDictionary = {};
            function _normalizeTenants(values) {
                var result = [];
                if (values) {
                    _1dsCoreJs.arrForEach(values, function (value) {
                        result.push(_1dsCoreJs.strTrim(value));
                    });
                }
                return result;
            }
            dynamicProto__default(KillSwitch, this, function (_self) {
                _self.setKillSwitchTenants = function (killTokens, killDuration) {
                    if (killTokens && killDuration) {
                        try {
                            var killedTokens = _normalizeTenants(killTokens.split(","));
                            if (killDuration === "this-request-only") {
                                return killedTokens;
                            }
                            var durationMs = parseInt(killDuration, 10) * SecToMsMultiplier;
                            for (var i = 0; i < killedTokens.length; ++i) {
                                _killedTokenDictionary[killedTokens[i]] = _1dsCoreJs.dateNow() + durationMs;
                            }
                        }
                        catch (ex) {
                            return [];
                        }
                    }
                    return [];
                };
                _self.isTenantKilled = function (tenantToken) {
                    var killDictionary = _killedTokenDictionary;
                    var name = _1dsCoreJs.strTrim(tenantToken);
                    if (killDictionary[name] !== undefined && killDictionary[name] > _1dsCoreJs.dateNow()) {
                        return true;
                    }
                    delete killDictionary[name];
                    return false;
                };
            });
        }
        return KillSwitch;
    }());

    var ClockSkewManager = /** @class */ (function () {
        function ClockSkewManager() {
            var _allowRequestSending = true;
            var _shouldAddClockSkewHeaders = true;
            var _isFirstRequest = true;
            var _clockSkewHeaderValue = "use-collector-delta";
            var _clockSkewSet = false;
            dynamicProto__default(ClockSkewManager, this, function (_self) {
                _self.allowRequestSending = function () {
                    return _allowRequestSending;
                };
                _self.firstRequestSent = function () {
                    if (_isFirstRequest) {
                        _isFirstRequest = false;
                        if (!_clockSkewSet) {
                            _allowRequestSending = false;
                        }
                    }
                };
                _self.shouldAddClockSkewHeaders = function () {
                    return _shouldAddClockSkewHeaders;
                };
                _self.getClockSkewHeaderValue = function () {
                    return _clockSkewHeaderValue;
                };
                _self.setClockSkew = function (timeDeltaInMillis) {
                    if (!_clockSkewSet) {
                        if (timeDeltaInMillis) {
                            _clockSkewHeaderValue = timeDeltaInMillis;
                            _shouldAddClockSkewHeaders = true;
                            _clockSkewSet = true;
                        }
                        else {
                            _shouldAddClockSkewHeaders = false;
                        }
                        _allowRequestSending = true;
                    }
                };
            });
        }
        return ClockSkewManager;
    }());

    var _a;
    var strSendAttempt = "sendAttempt";
    var _noResponseQs = "&" + strNoResponseBody + "=true";
    var _eventActionMap = (_a = {},
        _a[1 ] = strRequeue,
        _a[100 ] = strRequeue,
        _a[200 ] = "sent",
        _a[8004 ] = strDropped,
        _a[8003 ] = strDropped,
        _a);
    var _collectorQsHeaders = {};
    var _collectorHeaderToQs = {};
    function _addCollectorHeaderQsMapping(qsName, headerName, allowQs) {
        _collectorQsHeaders[qsName] = headerName;
        if (allowQs !== false) {
            _collectorHeaderToQs[headerName] = qsName;
        }
    }
    _addCollectorHeaderQsMapping(strMsaDeviceTicket, strMsaDeviceTicket, false);
    _addCollectorHeaderQsMapping(strClientVersion, strClientVersion);
    _addCollectorHeaderQsMapping(strClientId, "Client-Id");
    _addCollectorHeaderQsMapping(strApiKey, strApiKey);
    _addCollectorHeaderQsMapping(strTimeDeltaToApply, strTimeDeltaToApply);
    _addCollectorHeaderQsMapping(strUploadTime, strUploadTime);
    _addCollectorHeaderQsMapping(strAuthXToken, strAuthXToken);
    function _getResponseText(xhr) {
        try {
            return xhr.responseText;
        }
        catch (e) {
        }
        return "";
    }
    function _hasHeader(headers, header) {
        var hasHeader = false;
        if (headers && header) {
            var keys = _1dsCoreJs.objKeys(headers);
            if (keys && keys.length > 0) {
                var lowerHeader = header.toLowerCase();
                for (var lp = 0; lp < keys.length; lp++) {
                    var value = keys[lp];
                    if (value && _1dsCoreJs.hasOwnProperty(header, value) &&
                        value.toLowerCase() === lowerHeader) {
                        hasHeader = true;
                        break;
                    }
                }
            }
        }
        return hasHeader;
    }
    function _addRequestDetails(details, name, value, useHeaders) {
        if (name && value && value.length > 0) {
            if (useHeaders && _collectorQsHeaders[name]) {
                details.hdrs[_collectorQsHeaders[name]] = value;
                details.useHdrs = true;
            }
            else {
                details.url += "&" + name + "=" + value;
            }
        }
    }
    var HttpManager = /** @class */ (function () {
        function HttpManager(maxEventsPerBatch, maxConnections, maxRequestRetriesBeforeBackoff, actions, timeoutOverride) {
            this._responseHandlers = [];
            var _urlString = "?cors=true&" + strContentTypeHeader.toLowerCase() + "=" + defaultContentType;
            var _killSwitch = new KillSwitch();
            var _paused = false;
            var _clockSkewManager = new ClockSkewManager();
            var _useBeacons = false;
            var _outstandingRequests = 0;
            var _postManager;
            var _sendInterfaces;
            var _core;
            var _customHttpInterface = true;
            var _queryStringParameters = [];
            var _headers = {};
            var _batchQueue = [];
            var _serializer = null;
            var _enableEventTimings = false;
            var _cookieMgr;
            var _isUnloading = false;
            var _useHeaders = false;
            var _xhrTimeout;
            var _disableXhrSync;
            dynamicProto__default(HttpManager, this, function (_self) {
                var _sendCredentials = true;
                _self.initialize = function (endpointUrl, core, postChannel, httpInterface, channelConfig) {
                    var _a;
                    if (!channelConfig) {
                        channelConfig = {};
                    }
                    _urlString = endpointUrl + _urlString;
                    _useHeaders = !_1dsCoreJs.isUndefined(channelConfig.avoidOptions) ? !channelConfig.avoidOptions : true;
                    _core = core;
                    _cookieMgr = core.getCookieMgr();
                    _enableEventTimings = !_core.config.disableEventTimings;
                    var enableCompoundKey = !!_core.config.enableCompoundKey;
                    _postManager = postChannel;
                    var valueSanitizer = channelConfig.valueSanitizer;
                    var stringifyObjects = channelConfig.stringifyObjects;
                    if (!_1dsCoreJs.isUndefined(channelConfig.enableCompoundKey)) {
                        enableCompoundKey = !!channelConfig.enableCompoundKey;
                    }
                    _xhrTimeout = channelConfig.xhrTimeout;
                    _disableXhrSync = channelConfig.disableXhrSync;
                    _useBeacons = !_1dsCoreJs.isReactNative();
                    _serializer = new Serializer(_core, valueSanitizer, stringifyObjects, enableCompoundKey);
                    var syncHttpInterface = httpInterface;
                    var beaconHttpInterface = channelConfig.alwaysUseXhrOverride ? httpInterface : null;
                    var fetchSyncHttpInterface = channelConfig.alwaysUseXhrOverride ? httpInterface : null;
                    if (!httpInterface) {
                        _customHttpInterface = false;
                        var location_1 = _1dsCoreJs.getLocation();
                        if (location_1 && location_1.protocol && location_1.protocol.toLowerCase() === "file:") {
                            _sendCredentials = false;
                        }
                        var theTransports = [];
                        if (_1dsCoreJs.isReactNative()) {
                            theTransports = [2 , 1 ];
                        }
                        else {
                            theTransports = [1 , 2 , 3 ];
                        }
                        var configTransports = channelConfig.transports;
                        if (configTransports) {
                            if (_1dsCoreJs.isNumber(configTransports)) {
                                theTransports = [configTransports].concat(theTransports);
                            }
                            else if (_1dsCoreJs.isArray(configTransports)) {
                                theTransports = configTransports.concat(theTransports);
                            }
                        }
                        httpInterface = _getSenderInterface(theTransports, false);
                        syncHttpInterface = _getSenderInterface(theTransports, true);
                        if (!httpInterface) {
                            _postManager.diagLog().warnToConsole("No available transport to send events");
                        }
                    }
                    _sendInterfaces = (_a = {},
                        _a[0 ] = httpInterface,
                        _a[1 ] = syncHttpInterface || _getSenderInterface([1 , 2 , 3 ], true),
                        _a[2 ] = beaconHttpInterface || _getSenderInterface([3 , 2 ], true) || syncHttpInterface || _getSenderInterface([1 ], true),
                        _a[3 ] = fetchSyncHttpInterface || _getSenderInterface([2 , 3 ], true) || syncHttpInterface || _getSenderInterface([1 ], true),
                        _a);
                };
                function _getSenderInterface(transports, syncSupport) {
                    var transportType = 0 ;
                    var sendPostFunc = null;
                    var lp = 0;
                    while (sendPostFunc == null && lp < transports.length) {
                        transportType = transports[lp];
                        if (transportType === 1 ) {
                            if (_1dsCoreJs.useXDomainRequest()) {
                                sendPostFunc = _xdrSendPost;
                            }
                            else if (_1dsCoreJs.isXhrSupported()) {
                                sendPostFunc = _xhrSendPost;
                            }
                        }
                        else if (transportType === 2  && _1dsCoreJs.isFetchSupported(syncSupport)) {
                            sendPostFunc = _fetchSendPost;
                        }
                        else if (_useBeacons && transportType === 3  && _1dsCoreJs.isBeaconsSupported()) {
                            sendPostFunc = _beaconSendPost;
                        }
                        lp++;
                    }
                    if (sendPostFunc) {
                        return {
                            _transport: transportType,
                            _isSync: syncSupport,
                            sendPOST: sendPostFunc
                        };
                    }
                    return null;
                }
                _self["_getDbgPlgTargets"] = function () {
                    return [_sendInterfaces[0 ], _killSwitch, _serializer, _sendInterfaces];
                };
                function _xdrSendPost(payload, oncomplete, sync) {
                    var xdr = new XDomainRequest();
                    xdr.open(Method, payload.urlString);
                    if (payload.timeout) {
                        xdr.timeout = payload.timeout;
                    }
                    xdr.onload = function () {
                        var response = _getResponseText(xdr);
                        _doOnComplete(oncomplete, 200, {}, response);
                        _handleCollectorResponse(response);
                    };
                    xdr.onerror = function () {
                        _doOnComplete(oncomplete, 400, {});
                    };
                    xdr.ontimeout = function () {
                        _doOnComplete(oncomplete, 500, {});
                    };
                    xdr.onprogress = function () { };
                    if (sync) {
                        xdr.send(payload.data);
                    }
                    else {
                        timeoutOverride.set(function () {
                            xdr.send(payload.data);
                        }, 0);
                    }
                }
                function _fetchSendPost(payload, oncomplete, sync) {
                    var _a;
                    var theUrl = payload.urlString;
                    var ignoreResponse = false;
                    var responseHandled = false;
                    var requestInit = (_a = {
                            body: payload.data,
                            method: Method
                        },
                        _a[DisabledPropertyName] = true,
                        _a);
                    if (sync) {
                        requestInit.keepalive = true;
                        if (payload._sendReason === 2 ) {
                            ignoreResponse = true;
                            theUrl += _noResponseQs;
                        }
                    }
                    if (_sendCredentials) {
                        requestInit.credentials = "include";
                    }
                    if (payload.headers && _1dsCoreJs.objKeys(payload.headers).length > 0) {
                        requestInit.headers = payload.headers;
                    }
                    fetch(theUrl, requestInit).then(function (response) {
                        var headerMap = {};
                        var responseText = "";
                        if (response.headers) {
                            response.headers.forEach(function (value, name) {
                                headerMap[name] = value;
                            });
                        }
                        if (response.body) {
                            response.text().then(function (text) {
                                responseText = text;
                            });
                        }
                        if (!responseHandled) {
                            responseHandled = true;
                            _doOnComplete(oncomplete, response.status, headerMap, responseText);
                            _handleCollectorResponse(responseText);
                        }
                    })["catch"](function (error) {
                        if (!responseHandled) {
                            responseHandled = true;
                            _doOnComplete(oncomplete, 0, {});
                        }
                    });
                    if (ignoreResponse && !responseHandled) {
                        responseHandled = true;
                        _doOnComplete(oncomplete, 200, {});
                    }
                    if (!responseHandled && payload.timeout > 0) {
                        timeoutOverride.set(function () {
                            if (!responseHandled) {
                                responseHandled = true;
                                _doOnComplete(oncomplete, 500, {});
                            }
                        }, payload.timeout);
                    }
                }
                function _xhrSendPost(payload, oncomplete, sync) {
                    var theUrl = payload.urlString;
                    function _appendHeader(theHeaders, xhr, name) {
                        if (!theHeaders[name] && xhr && xhr.getResponseHeader) {
                            var value = xhr.getResponseHeader(name);
                            if (value) {
                                theHeaders[name] = _1dsCoreJs.strTrim(value);
                            }
                        }
                        return theHeaders;
                    }
                    function _getAllResponseHeaders(xhr) {
                        var theHeaders = {};
                        if (!xhr.getAllResponseHeaders) {
                            theHeaders = _appendHeader(theHeaders, xhr, strTimeDeltaHeader);
                            theHeaders = _appendHeader(theHeaders, xhr, strKillDurationHeader);
                            theHeaders = _appendHeader(theHeaders, xhr, strKillDurationSecondsHeader);
                        }
                        else {
                            theHeaders = _convertAllHeadersToMap(xhr.getAllResponseHeaders());
                        }
                        return theHeaders;
                    }
                    function xhrComplete(xhr, responseTxt) {
                        _doOnComplete(oncomplete, xhr.status, _getAllResponseHeaders(xhr), responseTxt);
                    }
                    if (sync && payload.disableXhrSync) {
                        sync = false;
                    }
                    var xhrRequest = _1dsCoreJs.openXhr(Method, theUrl, _sendCredentials, true, sync, payload.timeout);
                    _1dsCoreJs.objForEachKey(payload.headers, function (name, value) {
                        xhrRequest.setRequestHeader(name, value);
                    });
                    xhrRequest.onload = function () {
                        var response = _getResponseText(xhrRequest);
                        xhrComplete(xhrRequest, response);
                        _handleCollectorResponse(response);
                    };
                    xhrRequest.onerror = function () {
                        xhrComplete(xhrRequest);
                    };
                    xhrRequest.ontimeout = function () {
                        xhrComplete(xhrRequest);
                    };
                    xhrRequest.send(payload.data);
                }
                function _doOnComplete(oncomplete, status, headers, response) {
                    try {
                        oncomplete(status, headers, response);
                    }
                    catch (e) {
                        _1dsCoreJs._throwInternal(_postManager.diagLog(), 2 , 518 , _1dsCoreJs.dumpObj(e));
                    }
                }
                function _beaconSendPost(payload, oncomplete, sync) {
                    var internalPayloadData = payload;
                    var status = 200;
                    var thePayload = internalPayloadData._thePayload;
                    var theUrl = payload.urlString + _noResponseQs;
                    try {
                        var nav_1 = _1dsCoreJs.getNavigator();
                        if (!nav_1.sendBeacon(theUrl, payload.data)) {
                            if (thePayload) {
                                var droppedBatches_1 = [];
                                _1dsCoreJs.arrForEach(thePayload.batches, function (theBatch) {
                                    if (droppedBatches_1 && theBatch && theBatch.count() > 0) {
                                        var theEvents = theBatch.events();
                                        for (var lp = 0; lp < theEvents.length; lp++) {
                                            if (!nav_1.sendBeacon(theUrl, _serializer.getEventBlob(theEvents[lp]))) {
                                                droppedBatches_1.push(theBatch.split(lp));
                                                break;
                                            }
                                        }
                                    }
                                    else {
                                        droppedBatches_1.push(theBatch.split(0));
                                    }
                                });
                                _sendBatchesNotification(droppedBatches_1, 8003 , thePayload.sendType, true);
                            }
                            else {
                                status = 0;
                            }
                        }
                    }
                    catch (ex) {
                        _postManager.diagLog().warnToConsole("Failed to send telemetry using sendBeacon API. Ex:" + _1dsCoreJs.dumpObj(ex));
                        status = 0;
                    }
                    finally {
                        _doOnComplete(oncomplete, status, {}, "");
                    }
                }
                function _isBeaconPayload(sendType) {
                    return sendType === 2  || sendType === 3 ;
                }
                function _adjustSendType(sendType) {
                    if (_isUnloading && _isBeaconPayload(sendType)) {
                        sendType = 2 ;
                    }
                    return sendType;
                }
                _self.addQueryStringParameter = function (name, value) {
                    for (var i = 0; i < _queryStringParameters.length; i++) {
                        if (_queryStringParameters[i].name === name) {
                            _queryStringParameters[i].value = value;
                            return;
                        }
                    }
                    _queryStringParameters.push({ name: name, value: value });
                };
                _self.addHeader = function (name, value) {
                    _headers[name] = value;
                };
                _self.canSendRequest = function () {
                    return _hasIdleConnection() && _clockSkewManager.allowRequestSending();
                };
                _self.sendQueuedRequests = function (sendType, sendReason) {
                    if (_1dsCoreJs.isUndefined(sendType)) {
                        sendType = 0 ;
                    }
                    if (_isUnloading) {
                        sendType = _adjustSendType(sendType);
                        sendReason = 2 ;
                    }
                    if (_canSendPayload(_batchQueue, sendType, 0)) {
                        _sendBatches(_clearQueue(), 0, false, sendType, sendReason || 0 );
                    }
                };
                _self.isCompletelyIdle = function () {
                    return !_paused && _outstandingRequests === 0 && _batchQueue.length === 0;
                };
                _self.setUnloading = function (value) {
                    _isUnloading = value;
                };
                _self.addBatch = function (theBatch) {
                    if (theBatch && theBatch.count() > 0) {
                        if (_killSwitch.isTenantKilled(theBatch.iKey())) {
                            return false;
                        }
                        _batchQueue.push(theBatch);
                    }
                    return true;
                };
                _self.teardown = function () {
                    if (_batchQueue.length > 0) {
                        _sendBatches(_clearQueue(), 0, true, 2 , 2 );
                    }
                };
                _self.pause = function () {
                    _paused = true;
                };
                _self.resume = function () {
                    _paused = false;
                    _self.sendQueuedRequests(0 , 4 );
                };
                _self.sendSynchronousBatch = function (batch, sendType, sendReason) {
                    if (batch && batch.count() > 0) {
                        if (_1dsCoreJs.isNullOrUndefined(sendType)) {
                            sendType = 1 ;
                        }
                        if (_isUnloading) {
                            sendType = _adjustSendType(sendType);
                            sendReason = 2 ;
                        }
                        _sendBatches([batch], 0, false, sendType, sendReason || 0 );
                    }
                };
                function _hasIdleConnection() {
                    return !_paused && _outstandingRequests < maxConnections;
                }
                function _clearQueue() {
                    var theQueue = _batchQueue;
                    _batchQueue = [];
                    return theQueue;
                }
                function _canSendPayload(theBatches, sendType, retryCnt) {
                    var result = false;
                    if (theBatches && theBatches.length > 0 && !_paused && _sendInterfaces[sendType] && _serializer) {
                        result = (sendType !== 0 ) || (_hasIdleConnection() && (retryCnt > 0 || _clockSkewManager.allowRequestSending()));
                    }
                    return result;
                }
                function _createDebugBatches(theBatches) {
                    var values = {};
                    if (theBatches) {
                        _1dsCoreJs.arrForEach(theBatches, function (theBatch, idx) {
                            values[idx] = {
                                iKey: theBatch.iKey(),
                                evts: theBatch.events()
                            };
                        });
                    }
                    return values;
                }
                function _sendBatches(theBatches, retryCount, isTeardown, sendType, sendReason) {
                    if (!theBatches || theBatches.length === 0) {
                        return;
                    }
                    if (_paused) {
                        _sendBatchesNotification(theBatches, 1 , sendType);
                        return;
                    }
                    sendType = _adjustSendType(sendType);
                    try {
                        var orgBatches_1 = theBatches;
                        var isSynchronous_1 = sendType !== 0 ;
                        _1dsCoreJs.doPerf(_core, function () { return "HttpManager:_sendBatches"; }, function (perfEvt) {
                            if (perfEvt) {
                                theBatches = theBatches.slice(0);
                            }
                            var droppedBatches = [];
                            var thePayload = null;
                            var serializationStart = _1dsCoreJs.getTime();
                            var sendInterface = _sendInterfaces[sendType] || (isSynchronous_1 ? _sendInterfaces[1 ] : _sendInterfaces[0 ]);
                            var isBeaconTransport = (_isUnloading || _isBeaconPayload(sendType) || (sendInterface && sendInterface._transport === 3 )) && _canUseSendBeaconApi();
                            while (_canSendPayload(theBatches, sendType, retryCount)) {
                                var theBatch = theBatches.shift();
                                if (theBatch && theBatch.count() > 0) {
                                    if (!_killSwitch.isTenantKilled(theBatch.iKey())) {
                                        thePayload = thePayload || _serializer.createPayload(retryCount, isTeardown, isSynchronous_1, isBeaconTransport, sendReason, sendType);
                                        if (!_serializer.appendPayload(thePayload, theBatch, maxEventsPerBatch)) {
                                            _doPayloadSend(thePayload, serializationStart, _1dsCoreJs.getTime(), sendReason);
                                            serializationStart = _1dsCoreJs.getTime();
                                            theBatches = [theBatch].concat(theBatches);
                                            thePayload = null;
                                        }
                                        else if (thePayload.overflow !== null) {
                                            theBatches = [thePayload.overflow].concat(theBatches);
                                            thePayload.overflow = null;
                                            _doPayloadSend(thePayload, serializationStart, _1dsCoreJs.getTime(), sendReason);
                                            serializationStart = _1dsCoreJs.getTime();
                                            thePayload = null;
                                        }
                                    }
                                    else {
                                        droppedBatches.push(theBatch);
                                    }
                                }
                            }
                            if (thePayload) {
                                _doPayloadSend(thePayload, serializationStart, _1dsCoreJs.getTime(), sendReason);
                            }
                            if (theBatches.length > 0) {
                                _batchQueue = theBatches.concat(_batchQueue);
                            }
                            _sendBatchesNotification(droppedBatches, 8004 , sendType);
                        }, function () { return ({ batches: _createDebugBatches(orgBatches_1), retryCount: retryCount, isTeardown: isTeardown, isSynchronous: isSynchronous_1, sendReason: sendReason, useSendBeacon: _isBeaconPayload(sendType), sendType: sendType }); }, !isSynchronous_1);
                    }
                    catch (ex) {
                        _1dsCoreJs._throwInternal(_postManager.diagLog(), 2 , 48 , "Unexpected Exception sending batch: " + _1dsCoreJs.dumpObj(ex));
                    }
                }
                function _buildRequestDetails(thePayload, useHeaders) {
                    var requestDetails = {
                        url: _urlString,
                        hdrs: {},
                        useHdrs: false
                    };
                    if (!useHeaders) {
                        _1dsCoreJs.objForEachKey(_headers, function (name, value) {
                            if (_collectorHeaderToQs[name]) {
                                _addRequestDetails(requestDetails, _collectorHeaderToQs[name], value, false);
                            }
                            else {
                                requestDetails.hdrs[name] = value;
                                requestDetails.useHdrs = true;
                            }
                        });
                    }
                    else {
                        requestDetails.hdrs = _1dsCoreJs.extend(requestDetails.hdrs, _headers);
                        requestDetails.useHdrs = (_1dsCoreJs.objKeys(requestDetails.hdrs).length > 0);
                    }
                    _addRequestDetails(requestDetails, strClientId, "NO_AUTH", useHeaders);
                    _addRequestDetails(requestDetails, strClientVersion, _1dsCoreJs.FullVersionString, useHeaders);
                    var apiQsKeys = "";
                    _1dsCoreJs.arrForEach(thePayload.apiKeys, function (apiKey) {
                        if (apiQsKeys.length > 0) {
                            apiQsKeys += ",";
                        }
                        apiQsKeys += apiKey;
                    });
                    _addRequestDetails(requestDetails, strApiKey, apiQsKeys, useHeaders);
                    _addRequestDetails(requestDetails, strUploadTime, _1dsCoreJs.dateNow().toString(), useHeaders);
                    var msfpc = _getMsfpc(thePayload);
                    if (_1dsCoreJs.isValueAssigned(msfpc)) {
                        requestDetails.url += "&ext.intweb.msfpc=" + msfpc;
                    }
                    if (_clockSkewManager.shouldAddClockSkewHeaders()) {
                        _addRequestDetails(requestDetails, strTimeDeltaToApply, _clockSkewManager.getClockSkewHeaderValue(), useHeaders);
                    }
                    if (_core.getWParam) {
                        var wParam = _core.getWParam();
                        if (wParam >= 0) {
                            requestDetails.url += "&w=" + wParam;
                        }
                    }
                    for (var i = 0; i < _queryStringParameters.length; i++) {
                        requestDetails.url += "&" + _queryStringParameters[i].name + "=" + _queryStringParameters[i].value;
                    }
                    return requestDetails;
                }
                function _canUseSendBeaconApi() {
                    return !_customHttpInterface && _useBeacons && _1dsCoreJs.isBeaconsSupported();
                }
                function _setTimingValue(timings, name, value) {
                    timings[name] = timings[name] || {};
                    timings[name][_postManager.identifier] = value;
                }
                function _doPayloadSend(thePayload, serializationStart, serializationCompleted, sendReason) {
                    if (thePayload && thePayload.payloadBlob && thePayload.payloadBlob.length > 0) {
                        var useSendHook_1 = !!_self.sendHook;
                        var sendInterface_1 = _sendInterfaces[thePayload.sendType];
                        if (!_isBeaconPayload(thePayload.sendType) && thePayload.isBeacon && thePayload.sendReason === 2 ) {
                            sendInterface_1 = _sendInterfaces[2 ] || _sendInterfaces[3 ] || sendInterface_1;
                        }
                        var useHeaders_1 = _useHeaders;
                        if (thePayload.isBeacon || sendInterface_1._transport === 3 ) {
                            useHeaders_1 = false;
                        }
                        var requestDetails_1 = _buildRequestDetails(thePayload, useHeaders_1);
                        useHeaders_1 = useHeaders_1 || requestDetails_1.useHdrs;
                        var sendEventStart_1 = _1dsCoreJs.getTime();
                        _1dsCoreJs.doPerf(_core, function () { return "HttpManager:_doPayloadSend"; }, function () {
                            for (var batchLp = 0; batchLp < thePayload.batches.length; batchLp++) {
                                var theBatch = thePayload.batches[batchLp];
                                var theEvents = theBatch.events();
                                for (var evtLp = 0; evtLp < theEvents.length; evtLp++) {
                                    var telemetryItem = theEvents[evtLp];
                                    if (_enableEventTimings) {
                                        var timings = telemetryItem.timings = telemetryItem.timings || {};
                                        _setTimingValue(timings, "sendEventStart", sendEventStart_1);
                                        _setTimingValue(timings, "serializationStart", serializationStart);
                                        _setTimingValue(timings, "serializationCompleted", serializationCompleted);
                                    }
                                    telemetryItem[strSendAttempt] > 0 ? telemetryItem[strSendAttempt]++ : telemetryItem[strSendAttempt] = 1;
                                }
                            }
                            _sendBatchesNotification(thePayload.batches, (1000  + (sendReason || 0 )), thePayload.sendType, true);
                            var orgPayloadData = {
                                data: thePayload.payloadBlob,
                                urlString: requestDetails_1.url,
                                headers: requestDetails_1.hdrs,
                                _thePayload: thePayload,
                                _sendReason: sendReason,
                                timeout: _xhrTimeout
                            };
                            if (!_1dsCoreJs.isUndefined(_disableXhrSync)) {
                                orgPayloadData.disableXhrSync = !!_disableXhrSync;
                            }
                            if (useHeaders_1) {
                                if (!_hasHeader(orgPayloadData.headers, strCacheControl)) {
                                    orgPayloadData.headers[strCacheControl] = defaultCacheControl;
                                }
                                if (!_hasHeader(orgPayloadData.headers, strContentTypeHeader)) {
                                    orgPayloadData.headers[strContentTypeHeader] = defaultContentType;
                                }
                            }
                            var sender = null;
                            if (sendInterface_1) {
                                sender = function (payload) {
                                    _clockSkewManager.firstRequestSent();
                                    var onComplete = function (status, headers) {
                                        _retryRequestIfNeeded(status, headers, thePayload, sendReason);
                                    };
                                    var isSync = thePayload.isTeardown || thePayload.isSync;
                                    try {
                                        sendInterface_1.sendPOST(payload, onComplete, isSync);
                                        if (_self.sendListener) {
                                            _self.sendListener(orgPayloadData, payload, isSync, thePayload.isBeacon);
                                        }
                                    }
                                    catch (ex) {
                                        _postManager.diagLog().warnToConsole("Unexpected exception sending payload. Ex:" + _1dsCoreJs.dumpObj(ex));
                                        _doOnComplete(onComplete, 0, {});
                                    }
                                };
                            }
                            _1dsCoreJs.doPerf(_core, function () { return "HttpManager:_doPayloadSend.sender"; }, function () {
                                if (sender) {
                                    if (thePayload.sendType === 0 ) {
                                        _outstandingRequests++;
                                    }
                                    if (useSendHook_1 && !thePayload.isBeacon && sendInterface_1._transport !== 3 ) {
                                        var hookData_1 = {
                                            data: orgPayloadData.data,
                                            urlString: orgPayloadData.urlString,
                                            headers: _1dsCoreJs.extend({}, orgPayloadData.headers),
                                            timeout: orgPayloadData.timeout,
                                            disableXhrSync: orgPayloadData.disableXhrSync
                                        };
                                        var senderCalled_1 = false;
                                        _1dsCoreJs.doPerf(_core, function () { return "HttpManager:_doPayloadSend.sendHook"; }, function () {
                                            try {
                                                _self.sendHook(hookData_1, function (payload) {
                                                    senderCalled_1 = true;
                                                    if (!_customHttpInterface && !payload._thePayload) {
                                                        payload._thePayload = payload._thePayload || orgPayloadData._thePayload;
                                                        payload._sendReason = payload._sendReason || orgPayloadData._sendReason;
                                                    }
                                                    sender(payload);
                                                }, thePayload.isSync || thePayload.isTeardown);
                                            }
                                            catch (ex) {
                                                if (!senderCalled_1) {
                                                    sender(orgPayloadData);
                                                }
                                            }
                                        });
                                    }
                                    else {
                                        sender(orgPayloadData);
                                    }
                                }
                            });
                        }, function () { return ({ thePayload: thePayload, serializationStart: serializationStart, serializationCompleted: serializationCompleted, sendReason: sendReason }); }, thePayload.isSync);
                    }
                    if (thePayload.sizeExceed && thePayload.sizeExceed.length > 0) {
                        _sendBatchesNotification(thePayload.sizeExceed, 8003 , thePayload.sendType);
                    }
                    if (thePayload.failedEvts && thePayload.failedEvts.length > 0) {
                        _sendBatchesNotification(thePayload.failedEvts, 8002 , thePayload.sendType);
                    }
                }
                function _addEventCompletedTimings(theEvents, sendEventCompleted) {
                    if (_enableEventTimings) {
                        _1dsCoreJs.arrForEach(theEvents, function (theEvent) {
                            var timings = theEvent.timings = theEvent.timings || {};
                            _setTimingValue(timings, "sendEventCompleted", sendEventCompleted);
                        });
                    }
                }
                function _retryRequestIfNeeded(status, headers, thePayload, sendReason) {
                    var reason = 9000 ;
                    var droppedBatches = null;
                    var isRetrying = false;
                    var backOffTrans = false;
                    try {
                        var shouldRetry = true;
                        if (typeof status !== _1dsCoreJs.strUndefined) {
                            if (headers) {
                                _clockSkewManager.setClockSkew(headers[strTimeDeltaHeader]);
                                var killDuration = headers[strKillDurationHeader] || headers["kill-duration-seconds"];
                                _1dsCoreJs.arrForEach(_killSwitch.setKillSwitchTenants(headers[strKillTokensHeader], killDuration), function (killToken) {
                                    _1dsCoreJs.arrForEach(thePayload.batches, function (theBatch) {
                                        if (theBatch.iKey() === killToken) {
                                            droppedBatches = droppedBatches || [];
                                            var removedEvents = theBatch.split(0);
                                            thePayload.numEvents -= removedEvents.count();
                                            droppedBatches.push(removedEvents);
                                        }
                                    });
                                });
                            }
                            if (status == 200 || status == 204) {
                                reason = 200 ;
                                return;
                            }
                            if (!retryPolicyShouldRetryForStatus(status) || thePayload.numEvents <= 0) {
                                shouldRetry = false;
                            }
                            reason = 9000  + (status % 1000);
                        }
                        if (shouldRetry) {
                            reason = 100 ;
                            var retryCount_1 = thePayload.retryCnt;
                            if (thePayload.sendType === 0 ) {
                                if (retryCount_1 < maxRequestRetriesBeforeBackoff) {
                                    isRetrying = true;
                                    _doAction(function () {
                                        if (thePayload.sendType === 0 ) {
                                            _outstandingRequests--;
                                        }
                                        _sendBatches(thePayload.batches, retryCount_1 + 1, thePayload.isTeardown, _isUnloading ? 2  : thePayload.sendType, 5 );
                                    }, _isUnloading, retryPolicyGetMillisToBackoffForRetry(retryCount_1));
                                }
                                else {
                                    backOffTrans = true;
                                    if (_isUnloading) {
                                        reason = 8001 ;
                                    }
                                }
                            }
                        }
                    }
                    finally {
                        if (!isRetrying) {
                            _clockSkewManager.setClockSkew();
                            _handleRequestFinished(thePayload, reason, sendReason, backOffTrans);
                        }
                        _sendBatchesNotification(droppedBatches, 8004 , thePayload.sendType);
                    }
                }
                function _handleRequestFinished(thePayload, batchReason, sendReason, backOffTrans) {
                    try {
                        if (backOffTrans) {
                            _postManager._backOffTransmission();
                        }
                        if (batchReason === 200 ) {
                            if (!backOffTrans && !thePayload.isSync) {
                                _postManager._clearBackOff();
                            }
                            _addCompleteTimings(thePayload.batches);
                        }
                        _sendBatchesNotification(thePayload.batches, batchReason, thePayload.sendType, true);
                    }
                    finally {
                        if (thePayload.sendType === 0 ) {
                            _outstandingRequests--;
                            if (sendReason !== 5 ) {
                                _self.sendQueuedRequests(thePayload.sendType, sendReason);
                            }
                        }
                    }
                }
                function _addCompleteTimings(theBatches) {
                    if (_enableEventTimings) {
                        var sendEventCompleted_1 = _1dsCoreJs.getTime();
                        _1dsCoreJs.arrForEach(theBatches, function (theBatch) {
                            if (theBatch && theBatch.count() > 0) {
                                _addEventCompletedTimings(theBatch.events(), sendEventCompleted_1);
                            }
                        });
                    }
                }
                function _doAction(cb, isSync, interval) {
                    if (isSync) {
                        cb();
                    }
                    else {
                        timeoutOverride.set(cb, interval);
                    }
                }
                function _convertAllHeadersToMap(headersString) {
                    var headers = {};
                    if (_1dsCoreJs.isString(headersString)) {
                        var headersArray = _1dsCoreJs.strTrim(headersString).split(/[\r\n]+/);
                        _1dsCoreJs.arrForEach(headersArray, function (headerEntry) {
                            if (headerEntry) {
                                var idx = headerEntry.indexOf(": ");
                                if (idx !== -1) {
                                    var header = _1dsCoreJs.strTrim(headerEntry.substring(0, idx)).toLowerCase();
                                    var value = _1dsCoreJs.strTrim(headerEntry.substring(idx + 1));
                                    headers[header] = value;
                                }
                                else {
                                    headers[_1dsCoreJs.strTrim(headerEntry)] = 1;
                                }
                            }
                        });
                    }
                    return headers;
                }
                function _getMsfpc(thePayload) {
                    for (var lp = 0; lp < thePayload.batches.length; lp++) {
                        var msfpc = thePayload.batches[lp].Msfpc();
                        if (msfpc) {
                            return encodeURIComponent(msfpc);
                        }
                    }
                    return "";
                }
                function _handleCollectorResponse(responseText) {
                    var responseHandlers = _self._responseHandlers;
                    try {
                        for (var i = 0; i < responseHandlers.length; i++) {
                            try {
                                responseHandlers[i](responseText);
                            }
                            catch (e) {
                                _1dsCoreJs._throwInternal(_postManager.diagLog(), 1 , 519 , "Response handler failed: " + e);
                            }
                        }
                        if (responseText) {
                            var response = JSON.parse(responseText);
                            if (_1dsCoreJs.isValueAssigned(response.webResult) && _1dsCoreJs.isValueAssigned(response.webResult[strMsfpc])) {
                                _cookieMgr.set("MSFPC", response.webResult[strMsfpc], 365 * 86400);
                            }
                        }
                    }
                    catch (ex) {
                    }
                }
                function _sendBatchesNotification(theBatches, batchReason, sendType, sendSync) {
                    if (theBatches && theBatches.length > 0 && actions) {
                        var theAction_1 = actions[_getNotificationAction(batchReason)];
                        if (theAction_1) {
                            var isSyncRequest_1 = sendType !== 0 ;
                            _1dsCoreJs.doPerf(_core, function () { return "HttpManager:_sendBatchesNotification"; }, function () {
                                _doAction(function () {
                                    try {
                                        theAction_1.call(actions, theBatches, batchReason, isSyncRequest_1, sendType);
                                    }
                                    catch (e) {
                                        _1dsCoreJs._throwInternal(_postManager.diagLog(), 1 , 74 , "send request notification failed: " + e);
                                    }
                                }, sendSync || isSyncRequest_1, 0);
                            }, function () { return ({ batches: _createDebugBatches(theBatches), reason: batchReason, isSync: isSyncRequest_1, sendSync: sendSync, sendType: sendType }); }, !isSyncRequest_1);
                        }
                    }
                }
                function _getNotificationAction(reason) {
                    var action = _eventActionMap[reason];
                    if (!_1dsCoreJs.isValueAssigned(action)) {
                        action = strOther;
                        if (reason >= 9000  && reason <= 9999 ) {
                            action = strResponseFail;
                        }
                        else if (reason >= 8000  && reason <= 8999 ) {
                            action = strDropped;
                        }
                        else if (reason >= 1000  && reason <= 1999 ) {
                            action = strSending;
                        }
                    }
                    return action;
                }
            });
        }
        return HttpManager;
    }());

    function defaultSetTimeout(callback, ms) {
        var args = [];
        for (var _i = 2; _i < arguments.length; _i++) {
            args[_i - 2] = arguments[_i];
        }
        return setTimeout(callback, ms, args);
    }
    function defaultClearTimeout(timeoutId) {
        clearTimeout(timeoutId);
    }
    function createTimeoutWrapper(argSetTimeout, argClearTimeout) {
        return {
            set: argSetTimeout || defaultSetTimeout,
            clear: argClearTimeout || defaultClearTimeout
        };
    }

    var FlushCheckTimer = 0.250;
    var MaxNumberEventPerBatch = 500;
    var EventsDroppedAtOneTime = 20;
    var MaxSendAttempts = 6;
    var MaxSyncUnloadSendAttempts = 2;
    var MaxBackoffCount = 4;
    var MaxConnections = 2;
    var MaxRequestRetriesBeforeBackoff = 1;
    var strEventsDiscarded = "eventsDiscarded";
    var strOverrideInstrumentationKey = "overrideInstrumentationKey";
    var strMaxEventRetryAttempts = "maxEventRetryAttempts";
    var strMaxUnloadEventRetryAttempts = "maxUnloadEventRetryAttempts";
    var strAddUnloadCb = "addUnloadCb";
    var PostChannel = /** @class */ (function (_super) {
        applicationinsightsShims.__extendsFn(PostChannel, _super);
        function PostChannel() {
            var _this = _super.call(this) || this;
            _this.identifier = "PostChannel";
            _this.priority = 1011;
            _this.version = '3.2.3';
            var _config;
            var _isTeardownCalled = false;
            var _flushCallbackQueue = [];
            var _flushCallbackTimerId = null;
            var _paused = false;
            var _immediateQueueSize = 0;
            var _immediateQueueSizeLimit = 500;
            var _queueSize = 0;
            var _queueSizeLimit = 10000;
            var _profiles = {};
            var _currentProfile = RT_PROFILE;
            var _scheduledTimerId = null;
            var _immediateTimerId = null;
            var _currentBackoffCount = 0;
            var _timerCount = 0;
            var _xhrOverride;
            var _httpManager;
            var _batchQueues = {};
            var _autoFlushEventsLimit;
            var _autoFlushBatchLimit;
            var _delayedBatchSendLatency = -1;
            var _delayedBatchReason;
            var _optimizeObject = true;
            var _isPageUnloadTriggered = false;
            var _maxEventSendAttempts = MaxSendAttempts;
            var _maxUnloadEventSendAttempts = MaxSyncUnloadSendAttempts;
            var _evtNamespace;
            var _timeoutWrapper;
            dynamicProto__default(PostChannel, _this, function (_self, _base) {
                _initDefaults();
                _self["_getDbgPlgTargets"] = function () {
                    return [_httpManager];
                };
                _self.initialize = function (coreConfig, core, extensions) {
                    _1dsCoreJs.doPerf(core, function () { return "PostChannel:initialize"; }, function () {
                        var extendedCore = core;
                        _base.initialize(coreConfig, core, extensions);
                        try {
                            var hasAddUnloadCb = !!core[strAddUnloadCb];
                            _evtNamespace = _1dsCoreJs.mergeEvtNamespace(_1dsCoreJs.createUniqueNamespace(_self.identifier), core.evtNamespace && core.evtNamespace());
                            var ctx = _self._getTelCtx();
                            coreConfig.extensionConfig[_self.identifier] = coreConfig.extensionConfig[_self.identifier] || {};
                            _config = ctx.getExtCfg(_self.identifier);
                            _timeoutWrapper = createTimeoutWrapper(_config.setTimeoutOverride, _config.clearTimeoutOverride);
                            _optimizeObject = !_config.disableOptimizeObj && _1dsCoreJs.isChromium();
                            _hookWParam(extendedCore);
                            if (_config.eventsLimitInMem > 0) {
                                _queueSizeLimit = _config.eventsLimitInMem;
                            }
                            if (_config.immediateEventLimit > 0) {
                                _immediateQueueSizeLimit = _config.immediateEventLimit;
                            }
                            if (_config.autoFlushEventsLimit > 0) {
                                _autoFlushEventsLimit = _config.autoFlushEventsLimit;
                            }
                            if (_1dsCoreJs.isNumber(_config[strMaxEventRetryAttempts])) {
                                _maxEventSendAttempts = _config[strMaxEventRetryAttempts];
                            }
                            if (_1dsCoreJs.isNumber(_config[strMaxUnloadEventRetryAttempts])) {
                                _maxUnloadEventSendAttempts = _config[strMaxUnloadEventRetryAttempts];
                            }
                            _setAutoLimits();
                            if (_config.httpXHROverride && _config.httpXHROverride.sendPOST) {
                                _xhrOverride = _config.httpXHROverride;
                            }
                            if (_1dsCoreJs.isValueAssigned(coreConfig.anonCookieName)) {
                                _httpManager.addQueryStringParameter("anoncknm", coreConfig.anonCookieName);
                            }
                            _httpManager.sendHook = _config.payloadPreprocessor;
                            _httpManager.sendListener = _config.payloadListener;
                            var endpointUrl = _config.overrideEndpointUrl ? _config.overrideEndpointUrl : coreConfig.endpointUrl;
                            _self._notificationManager = coreConfig.extensionConfig.NotificationManager;
                            _httpManager.initialize(endpointUrl, _self.core, _self, _xhrOverride, _config);
                            var excludePageUnloadEvents = coreConfig.disablePageUnloadEvents || [];
                            _1dsCoreJs.addPageUnloadEventListener(_handleUnloadEvents, excludePageUnloadEvents, _evtNamespace);
                            _1dsCoreJs.addPageHideEventListener(_handleUnloadEvents, excludePageUnloadEvents, _evtNamespace);
                            _1dsCoreJs.addPageShowEventListener(_handleShowEvents, coreConfig.disablePageShowEvents, _evtNamespace);
                        }
                        catch (e) {
                            _self.setInitialized(false);
                            throw e;
                        }
                    }, function () { return ({ coreConfig: coreConfig, core: core, extensions: extensions }); });
                };
                _self.processTelemetry = function (ev, itemCtx) {
                    _1dsCoreJs.setProcessTelemetryTimings(ev, _self.identifier);
                    itemCtx = _self._getTelCtx(itemCtx);
                    var channelConfig = itemCtx.getExtCfg(_self.identifier);
                    var disableTelemetry = !!_config.disableTelemetry;
                    if (channelConfig) {
                        disableTelemetry = disableTelemetry || !!channelConfig.disableTelemetry;
                    }
                    var event = ev;
                    if (!disableTelemetry && !_isTeardownCalled) {
                        if (_config[strOverrideInstrumentationKey]) {
                            event.iKey = _config[strOverrideInstrumentationKey];
                        }
                        if (channelConfig && channelConfig[strOverrideInstrumentationKey]) {
                            event.iKey = channelConfig[strOverrideInstrumentationKey];
                        }
                        _addEventToQueues(event, true);
                        if (_isPageUnloadTriggered) {
                            _releaseAllQueues(2 , 2 );
                        }
                        else {
                            _scheduleTimer();
                        }
                    }
                    _self.processNext(event, itemCtx);
                };
                _self._doTeardown = function (unloadCtx, unloadState) {
                    _releaseAllQueues(2 , 2 );
                    _isTeardownCalled = true;
                    _httpManager.teardown();
                    _1dsCoreJs.removePageUnloadEventListener(null, _evtNamespace);
                    _1dsCoreJs.removePageHideEventListener(null, _evtNamespace);
                    _1dsCoreJs.removePageShowEventListener(null, _evtNamespace);
                    _initDefaults();
                };
                function _hookWParam(extendedCore) {
                    var existingGetWParamMethod = extendedCore.getWParam;
                    extendedCore.getWParam = function () {
                        var wparam = 0;
                        if (_config.ignoreMc1Ms0CookieProcessing) {
                            wparam = wparam | 2;
                        }
                        return wparam | existingGetWParamMethod();
                    };
                }
                function _handleUnloadEvents(evt) {
                    var theEvt = evt || _1dsCoreJs.getWindow().event;
                    if (theEvt.type !== "beforeunload") {
                        _isPageUnloadTriggered = true;
                        _httpManager.setUnloading(_isPageUnloadTriggered);
                    }
                    _releaseAllQueues(2 , 2 );
                }
                function _handleShowEvents(evt) {
                    _isPageUnloadTriggered = false;
                    _httpManager.setUnloading(_isPageUnloadTriggered);
                }
                function _addEventToQueues(event, append) {
                    if (!event.sendAttempt) {
                        event.sendAttempt = 0;
                    }
                    if (!event.latency) {
                        event.latency = 1 ;
                    }
                    if (event.ext && event.ext["trace"]) {
                        delete (event.ext["trace"]);
                    }
                    if (event.ext && event.ext["user"] && event.ext["user"]["id"]) {
                        delete (event.ext["user"]["id"]);
                    }
                    if (_optimizeObject) {
                        event.ext = _1dsCoreJs.optimizeObject(event.ext);
                        if (event.baseData) {
                            event.baseData = _1dsCoreJs.optimizeObject(event.baseData);
                        }
                        if (event.data) {
                            event.data = _1dsCoreJs.optimizeObject(event.data);
                        }
                    }
                    if (event.sync) {
                        if (_currentBackoffCount || _paused) {
                            event.latency = 3 ;
                            event.sync = false;
                        }
                        else {
                            if (_httpManager) {
                                if (_optimizeObject) {
                                    event = _1dsCoreJs.optimizeObject(event);
                                }
                                _httpManager.sendSynchronousBatch(EventBatch.create(event.iKey, [event]), event.sync === true ? 1  : event.sync, 3 );
                                return;
                            }
                        }
                    }
                    var evtLatency = event.latency;
                    var queueSize = _queueSize;
                    var queueLimit = _queueSizeLimit;
                    if (evtLatency === 4 ) {
                        queueSize = _immediateQueueSize;
                        queueLimit = _immediateQueueSizeLimit;
                    }
                    var eventDropped = false;
                    if (queueSize < queueLimit) {
                        eventDropped = !_addEventToProperQueue(event, append);
                    }
                    else {
                        var dropLatency = 1 ;
                        var dropNumber = EventsDroppedAtOneTime;
                        if (evtLatency === 4 ) {
                            dropLatency = 4 ;
                            dropNumber = 1;
                        }
                        eventDropped = true;
                        if (_dropEventWithLatencyOrLess(event.iKey, event.latency, dropLatency, dropNumber)) {
                            eventDropped = !_addEventToProperQueue(event, append);
                        }
                    }
                    if (eventDropped) {
                        _notifyEvents(strEventsDiscarded, [event], _1dsCoreJs.EventsDiscardedReason.QueueFull);
                    }
                }
                _self.setEventQueueLimits = function (eventLimit, autoFlushLimit) {
                    _queueSizeLimit = eventLimit > 0 ? eventLimit : 10000;
                    _autoFlushEventsLimit = autoFlushLimit > 0 ? autoFlushLimit : 0;
                    _setAutoLimits();
                    var doFlush = _queueSize > eventLimit;
                    if (!doFlush && _autoFlushBatchLimit > 0) {
                        for (var latency = 1 ; !doFlush && latency <= 3 ; latency++) {
                            var batchQueue = _batchQueues[latency];
                            if (batchQueue && batchQueue.batches) {
                                _1dsCoreJs.arrForEach(batchQueue.batches, function (theBatch) {
                                    if (theBatch && theBatch.count() >= _autoFlushBatchLimit) {
                                        doFlush = true;
                                    }
                                });
                            }
                        }
                    }
                    _performAutoFlush(true, doFlush);
                };
                _self.pause = function () {
                    _clearScheduledTimer();
                    _paused = true;
                    _httpManager.pause();
                };
                _self.resume = function () {
                    _paused = false;
                    _httpManager.resume();
                    _scheduleTimer();
                };
                _self.addResponseHandler = function (responseHandler) {
                    _httpManager._responseHandlers.push(responseHandler);
                };
                _self._loadTransmitProfiles = function (profiles) {
                    _resetTransmitProfiles();
                    _1dsCoreJs.objForEachKey(profiles, function (profileName, profileValue) {
                        var profLen = profileValue.length;
                        if (profLen >= 2) {
                            var directValue = (profLen > 2 ? profileValue[2] : 0);
                            profileValue.splice(0, profLen - 2);
                            if (profileValue[1] < 0) {
                                profileValue[0] = -1;
                            }
                            if (profileValue[1] > 0 && profileValue[0] > 0) {
                                var timerMultiplier = profileValue[0] / profileValue[1];
                                profileValue[0] = Math.ceil(timerMultiplier) * profileValue[1];
                            }
                            if (directValue >= 0 && profileValue[1] >= 0 && directValue > profileValue[1]) {
                                directValue = profileValue[1];
                            }
                            profileValue.push(directValue);
                            _profiles[profileName] = profileValue;
                        }
                    });
                };
                _self.flush = function (async, callback, sendReason) {
                    if (async === void 0) { async = true; }
                    if (!_paused) {
                        sendReason = sendReason || 1 ;
                        if (async) {
                            if (_flushCallbackTimerId == null) {
                                _clearScheduledTimer();
                                _queueBatches(1 , 0 , sendReason);
                                _flushCallbackTimerId = _createTimer(function () {
                                    _flushCallbackTimerId = null;
                                    _flushImpl(callback, sendReason);
                                }, 0);
                            }
                            else {
                                _flushCallbackQueue.push(callback);
                            }
                        }
                        else {
                            var cleared = _clearScheduledTimer();
                            _sendEventsForLatencyAndAbove(1 , 1 , sendReason);
                            if (callback !== null && callback !== undefined) {
                                callback();
                            }
                            if (cleared) {
                                _scheduleTimer();
                            }
                        }
                    }
                };
                _self.setMsaAuthTicket = function (ticket) {
                    _httpManager.addHeader(strMsaDeviceTicket, ticket);
                };
                _self.hasEvents = _hasEvents;
                _self._setTransmitProfile = function (profileName) {
                    if (_currentProfile !== profileName && _profiles[profileName] !== undefined) {
                        _clearScheduledTimer();
                        _currentProfile = profileName;
                        _scheduleTimer();
                    }
                };
                function _sendEventsForLatencyAndAbove(latency, sendType, sendReason) {
                    var queued = _queueBatches(latency, sendType, sendReason);
                    _httpManager.sendQueuedRequests(sendType, sendReason);
                    return queued;
                }
                function _hasEvents() {
                    return _queueSize > 0;
                }
                function _scheduleTimer() {
                    if (_delayedBatchSendLatency >= 0 && _queueBatches(_delayedBatchSendLatency, 0 , _delayedBatchReason)) {
                        _httpManager.sendQueuedRequests(0 , _delayedBatchReason);
                    }
                    if (_immediateQueueSize > 0 && !_immediateTimerId && !_paused) {
                        var immediateTimeOut = _profiles[_currentProfile][2];
                        if (immediateTimeOut >= 0) {
                            _immediateTimerId = _createTimer(function () {
                                _immediateTimerId = null;
                                _sendEventsForLatencyAndAbove(4 , 0 , 1 );
                                _scheduleTimer();
                            }, immediateTimeOut);
                        }
                    }
                    var timeOut = _profiles[_currentProfile][1];
                    if (!_scheduledTimerId && !_flushCallbackTimerId && timeOut >= 0 && !_paused) {
                        if (_hasEvents()) {
                            _scheduledTimerId = _createTimer(function () {
                                _scheduledTimerId = null;
                                _sendEventsForLatencyAndAbove(_timerCount === 0 ? 3  : 1 , 0 , 1 );
                                _timerCount++;
                                _timerCount %= 2;
                                _scheduleTimer();
                            }, timeOut);
                        }
                        else {
                            _timerCount = 0;
                        }
                    }
                }
                _self._backOffTransmission = function () {
                    if (_currentBackoffCount < MaxBackoffCount) {
                        _currentBackoffCount++;
                        _clearScheduledTimer();
                        _scheduleTimer();
                    }
                };
                _self._clearBackOff = function () {
                    if (_currentBackoffCount) {
                        _currentBackoffCount = 0;
                        _clearScheduledTimer();
                        _scheduleTimer();
                    }
                };
                function _initDefaults() {
                    _config = null;
                    _isTeardownCalled = false;
                    _flushCallbackQueue = [];
                    _flushCallbackTimerId = null;
                    _paused = false;
                    _immediateQueueSize = 0;
                    _immediateQueueSizeLimit = 500;
                    _queueSize = 0;
                    _queueSizeLimit = 10000;
                    _profiles = {};
                    _currentProfile = RT_PROFILE;
                    _scheduledTimerId = null;
                    _immediateTimerId = null;
                    _currentBackoffCount = 0;
                    _timerCount = 0;
                    _xhrOverride = null;
                    _batchQueues = {};
                    _autoFlushEventsLimit = undefined;
                    _autoFlushBatchLimit = 0;
                    _delayedBatchSendLatency = -1;
                    _delayedBatchReason = null;
                    _optimizeObject = true;
                    _isPageUnloadTriggered = false;
                    _maxEventSendAttempts = MaxSendAttempts;
                    _maxUnloadEventSendAttempts = MaxSyncUnloadSendAttempts;
                    _evtNamespace = null;
                    _timeoutWrapper = createTimeoutWrapper();
                    _httpManager = new HttpManager(MaxNumberEventPerBatch, MaxConnections, MaxRequestRetriesBeforeBackoff, {
                        requeue: _requeueEvents,
                        send: _sendingEvent,
                        sent: _eventsSentEvent,
                        drop: _eventsDropped,
                        rspFail: _eventsResponseFail,
                        oth: _otherEvent
                    }, _timeoutWrapper);
                    _initializeProfiles();
                    _clearQueues();
                    _setAutoLimits();
                }
                function _createTimer(theTimerFunc, timeOut) {
                    if (timeOut === 0 && _currentBackoffCount) {
                        timeOut = 1;
                    }
                    var timerMultiplier = 1000;
                    if (_currentBackoffCount) {
                        timerMultiplier = retryPolicyGetMillisToBackoffForRetry(_currentBackoffCount - 1);
                    }
                    return _timeoutWrapper.set(theTimerFunc, timeOut * timerMultiplier);
                }
                function _clearScheduledTimer() {
                    if (_scheduledTimerId !== null) {
                        _timeoutWrapper.clear(_scheduledTimerId);
                        _scheduledTimerId = null;
                        _timerCount = 0;
                        return true;
                    }
                    return false;
                }
                function _releaseAllQueues(sendType, sendReason) {
                    _clearScheduledTimer();
                    if (_flushCallbackTimerId) {
                        _timeoutWrapper.clear(_flushCallbackTimerId);
                        _flushCallbackTimerId = null;
                    }
                    if (!_paused) {
                        _sendEventsForLatencyAndAbove(1 , sendType, sendReason);
                    }
                }
                function _clearQueues() {
                    _batchQueues[4 ] = {
                        batches: [],
                        iKeyMap: {}
                    };
                    _batchQueues[3 ] = {
                        batches: [],
                        iKeyMap: {}
                    };
                    _batchQueues[2 ] = {
                        batches: [],
                        iKeyMap: {}
                    };
                    _batchQueues[1 ] = {
                        batches: [],
                        iKeyMap: {}
                    };
                }
                function _getEventBatch(iKey, latency, create) {
                    var batchQueue = _batchQueues[latency];
                    if (!batchQueue) {
                        latency = 1 ;
                        batchQueue = _batchQueues[latency];
                    }
                    var eventBatch = batchQueue.iKeyMap[iKey];
                    if (!eventBatch && create) {
                        eventBatch = EventBatch.create(iKey);
                        batchQueue.batches.push(eventBatch);
                        batchQueue.iKeyMap[iKey] = eventBatch;
                    }
                    return eventBatch;
                }
                function _performAutoFlush(isAsync, doFlush) {
                    if (_httpManager.canSendRequest() && !_currentBackoffCount) {
                        if (_autoFlushEventsLimit > 0 && _queueSize > _autoFlushEventsLimit) {
                            doFlush = true;
                        }
                        if (doFlush && _flushCallbackTimerId == null) {
                            _self.flush(isAsync, null, 20 );
                        }
                    }
                }
                function _addEventToProperQueue(event, append) {
                    if (_optimizeObject) {
                        event = _1dsCoreJs.optimizeObject(event);
                    }
                    var latency = event.latency;
                    var eventBatch = _getEventBatch(event.iKey, latency, true);
                    if (eventBatch.addEvent(event)) {
                        if (latency !== 4 ) {
                            _queueSize++;
                            if (append && event.sendAttempt === 0) {
                                _performAutoFlush(!event.sync, _autoFlushBatchLimit > 0 && eventBatch.count() >= _autoFlushBatchLimit);
                            }
                        }
                        else {
                            _immediateQueueSize++;
                        }
                        return true;
                    }
                    return false;
                }
                function _dropEventWithLatencyOrLess(iKey, latency, currentLatency, dropNumber) {
                    while (currentLatency <= latency) {
                        var eventBatch = _getEventBatch(iKey, latency, true);
                        if (eventBatch && eventBatch.count() > 0) {
                            var droppedEvents = eventBatch.split(0, dropNumber);
                            var droppedCount = droppedEvents.count();
                            if (droppedCount > 0) {
                                if (currentLatency === 4 ) {
                                    _immediateQueueSize -= droppedCount;
                                }
                                else {
                                    _queueSize -= droppedCount;
                                }
                                _notifyBatchEvents(strEventsDiscarded, [droppedEvents], _1dsCoreJs.EventsDiscardedReason.QueueFull);
                                return true;
                            }
                        }
                        currentLatency++;
                    }
                    _resetQueueCounts();
                    return false;
                }
                function _resetQueueCounts() {
                    var immediateQueue = 0;
                    var normalQueue = 0;
                    var _loop_1 = function (latency) {
                        var batchQueue = _batchQueues[latency];
                        if (batchQueue && batchQueue.batches) {
                            _1dsCoreJs.arrForEach(batchQueue.batches, function (theBatch) {
                                if (latency === 4 ) {
                                    immediateQueue += theBatch.count();
                                }
                                else {
                                    normalQueue += theBatch.count();
                                }
                            });
                        }
                    };
                    for (var latency = 1 ; latency <= 4 ; latency++) {
                        _loop_1(latency);
                    }
                    _queueSize = normalQueue;
                    _immediateQueueSize = immediateQueue;
                }
                function _queueBatches(latency, sendType, sendReason) {
                    var eventsQueued = false;
                    var isAsync = sendType === 0 ;
                    if (!isAsync || _httpManager.canSendRequest()) {
                        _1dsCoreJs.doPerf(_self.core, function () { return "PostChannel._queueBatches"; }, function () {
                            var droppedEvents = [];
                            var latencyToProcess = 4 ;
                            while (latencyToProcess >= latency) {
                                var batchQueue = _batchQueues[latencyToProcess];
                                if (batchQueue && batchQueue.batches && batchQueue.batches.length > 0) {
                                    _1dsCoreJs.arrForEach(batchQueue.batches, function (theBatch) {
                                        if (!_httpManager.addBatch(theBatch)) {
                                            droppedEvents = droppedEvents.concat(theBatch.events());
                                        }
                                        else {
                                            eventsQueued = eventsQueued || (theBatch && theBatch.count() > 0);
                                        }
                                        if (latencyToProcess === 4 ) {
                                            _immediateQueueSize -= theBatch.count();
                                        }
                                        else {
                                            _queueSize -= theBatch.count();
                                        }
                                    });
                                    batchQueue.batches = [];
                                    batchQueue.iKeyMap = {};
                                }
                                latencyToProcess--;
                            }
                            if (droppedEvents.length > 0) {
                                _notifyEvents(strEventsDiscarded, droppedEvents, _1dsCoreJs.EventsDiscardedReason.KillSwitch);
                            }
                            if (eventsQueued && _delayedBatchSendLatency >= latency) {
                                _delayedBatchSendLatency = -1;
                                _delayedBatchReason = 0 ;
                            }
                        }, function () { return ({ latency: latency, sendType: sendType, sendReason: sendReason }); }, !isAsync);
                    }
                    else {
                        _delayedBatchSendLatency = _delayedBatchSendLatency >= 0 ? Math.min(_delayedBatchSendLatency, latency) : latency;
                        _delayedBatchReason = Math.max(_delayedBatchReason, sendReason);
                    }
                    return eventsQueued;
                }
                function _flushImpl(callback, sendReason) {
                    _sendEventsForLatencyAndAbove(1 , 0 , sendReason);
                    _resetQueueCounts();
                    _waitForIdleManager(function () {
                        if (callback) {
                            callback();
                        }
                        if (_flushCallbackQueue.length > 0) {
                            _flushCallbackTimerId = _createTimer(function () {
                                _flushCallbackTimerId = null;
                                _flushImpl(_flushCallbackQueue.shift(), sendReason);
                            }, 0);
                        }
                        else {
                            _flushCallbackTimerId = null;
                            _scheduleTimer();
                        }
                    });
                }
                function _waitForIdleManager(callback) {
                    if (_httpManager.isCompletelyIdle()) {
                        callback();
                    }
                    else {
                        _flushCallbackTimerId = _createTimer(function () {
                            _flushCallbackTimerId = null;
                            _waitForIdleManager(callback);
                        }, FlushCheckTimer);
                    }
                }
                function _resetTransmitProfiles() {
                    _clearScheduledTimer();
                    _initializeProfiles();
                    _currentProfile = RT_PROFILE;
                    _scheduleTimer();
                }
                function _initializeProfiles() {
                    _profiles = {};
                    _profiles[RT_PROFILE] = [2, 1, 0];
                    _profiles[NRT_PROFILE] = [6, 3, 0];
                    _profiles[BE_PROFILE] = [18, 9, 0];
                }
                function _requeueEvents(batches, reason) {
                    var droppedEvents = [];
                    var maxSendAttempts = _maxEventSendAttempts;
                    if (_isPageUnloadTriggered) {
                        maxSendAttempts = _maxUnloadEventSendAttempts;
                    }
                    _1dsCoreJs.arrForEach(batches, function (theBatch) {
                        if (theBatch && theBatch.count() > 0) {
                            _1dsCoreJs.arrForEach(theBatch.events(), function (theEvent) {
                                if (theEvent) {
                                    if (theEvent.sync) {
                                        theEvent.latency = 4 ;
                                        theEvent.sync = false;
                                    }
                                    if (theEvent.sendAttempt < maxSendAttempts) {
                                        _1dsCoreJs.setProcessTelemetryTimings(theEvent, _self.identifier);
                                        _addEventToQueues(theEvent, false);
                                    }
                                    else {
                                        droppedEvents.push(theEvent);
                                    }
                                }
                            });
                        }
                    });
                    if (droppedEvents.length > 0) {
                        _notifyEvents(strEventsDiscarded, droppedEvents, _1dsCoreJs.EventsDiscardedReason.NonRetryableStatus);
                    }
                    if (_isPageUnloadTriggered) {
                        _releaseAllQueues(2 , 2 );
                    }
                }
                function _callNotification(evtName, theArgs) {
                    var manager = (_self._notificationManager || {});
                    var notifyFunc = manager[evtName];
                    if (notifyFunc) {
                        try {
                            notifyFunc.apply(manager, theArgs);
                        }
                        catch (e) {
                            _1dsCoreJs._throwInternal(_self.diagLog(), 1 , 74 , evtName + " notification failed: " + e);
                        }
                    }
                }
                function _notifyEvents(evtName, theEvents) {
                    var extraArgs = [];
                    for (var _i = 2; _i < arguments.length; _i++) {
                        extraArgs[_i - 2] = arguments[_i];
                    }
                    if (theEvents && theEvents.length > 0) {
                        _callNotification(evtName, [theEvents].concat(extraArgs));
                    }
                }
                function _notifyBatchEvents(evtName, batches) {
                    var extraArgs = [];
                    for (var _i = 2; _i < arguments.length; _i++) {
                        extraArgs[_i - 2] = arguments[_i];
                    }
                    if (batches && batches.length > 0) {
                        _1dsCoreJs.arrForEach(batches, function (theBatch) {
                            if (theBatch && theBatch.count() > 0) {
                                _callNotification(evtName, [theBatch.events()].concat(extraArgs));
                            }
                        });
                    }
                }
                function _sendingEvent(batches, reason, isSyncRequest) {
                    if (batches && batches.length > 0) {
                        _callNotification("eventsSendRequest", [(reason >= 1000  && reason <= 1999  ?
                                reason - 1000  :
                                0 ), isSyncRequest !== true]);
                    }
                }
                function _eventsSentEvent(batches, reason) {
                    _notifyBatchEvents("eventsSent", batches, reason);
                    _scheduleTimer();
                }
                function _eventsDropped(batches, reason) {
                    _notifyBatchEvents(strEventsDiscarded, batches, (reason >= 8000  && reason <= 8999  ?
                        reason - 8000  :
                        _1dsCoreJs.EventsDiscardedReason.Unknown));
                }
                function _eventsResponseFail(batches) {
                    _notifyBatchEvents(strEventsDiscarded, batches, _1dsCoreJs.EventsDiscardedReason.NonRetryableStatus);
                    _scheduleTimer();
                }
                function _otherEvent(batches, reason) {
                    _notifyBatchEvents(strEventsDiscarded, batches, _1dsCoreJs.EventsDiscardedReason.Unknown);
                    _scheduleTimer();
                }
                function _setAutoLimits() {
                    if (!_config || !_config.disableAutoBatchFlushLimit) {
                        _autoFlushBatchLimit = Math.max(MaxNumberEventPerBatch * (MaxConnections + 1), _queueSizeLimit / 6);
                    }
                    else {
                        _autoFlushBatchLimit = 0;
                    }
                }
                _1dsCoreJs.objDefineAccessors(_self, "_setTimeoutOverride", function () { return _timeoutWrapper.set; }, function (value) {
                    _timeoutWrapper = createTimeoutWrapper(value, _timeoutWrapper.clear);
                });
                _1dsCoreJs.objDefineAccessors(_self, "_clearTimeoutOverride", function () { return _timeoutWrapper.clear; }, function (value) {
                    _timeoutWrapper = createTimeoutWrapper(_timeoutWrapper.set, value);
                });
            });
            return _this;
        }
        return PostChannel;
    }(_1dsCoreJs.BaseTelemetryPlugin));

    exports.BE_PROFILE = BE_PROFILE;
    exports.NRT_PROFILE = NRT_PROFILE;
    exports.PostChannel = PostChannel;
    exports.RT_PROFILE = RT_PROFILE;

    (function(obj, prop, descriptor) { /* ai_es3_polyfil defineProperty */ var func = Object["defineProperty"]; if (func) { try { return func(obj, prop, descriptor); } catch(e) { /* IE8 defines defineProperty, but will throw */ } } if (descriptor && typeof descriptor.value !== undefined) { obj[prop] = descriptor.value; } return obj; })(exports, '__esModule', { value: true });

}));
//# sourceMappingURL=ms.post.js.map


/***/ })

};
;
//# sourceMappingURL=985.main.js.map