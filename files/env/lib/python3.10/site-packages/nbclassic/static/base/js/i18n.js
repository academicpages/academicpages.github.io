// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

// Module to handle i18n ( Internationalization ) and translated UI

define([
    'jed'
	], function(Jed) {
    "use strict";

    var i18n = new Jed(document.nbjs_translations);
    i18n._ = i18n.gettext;
    i18n.msg = i18n; // Just a place holder until the init promise resolves.

    return i18n;
});
