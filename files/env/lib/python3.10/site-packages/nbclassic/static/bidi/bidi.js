// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

define(['bidi/numericshaping'], function(numericshaping) {
  'use strict';

  var shaperType = '';

  var _uiLang = function() {
    return navigator.language.toLowerCase();
  };

  var _loadLocale = function() {
    if (_isMirroringEnabled()) {
      document.body.dir = 'rtl';
    }

    requirejs(['moment'], function (moment) {
      console.log('Loaded moment locale', moment.locale(_uiLang()));
    });

    shaperType = _uiLang().split('-')[0] == 'ar' ? 'national' : 'defaultNumeral';
  };

  var _isMirroringEnabled = function() {
    return new RegExp('^(ar|ara|arc|ae|ave|egy|he|heb|nqo|pal|phn|sam|syc|syr|fa|per|fas|ckb|ur|urd)').test(_uiLang());
  };

  /**
     * @param value : the string to apply the bidi-support on it.
     * @param flag :indicates the type of bidi-support (Numeric-shaping ,Base-text-dir ).
     */
  var _applyBidi = function(value /*, flag*/) {
    value = numericshaping.shapeNumerals(value, shaperType);
    return value;
  };

  var bidi = {
    applyBidi: _applyBidi,
    isMirroringEnabled: _isMirroringEnabled,
    loadLocale: _loadLocale,
  };

  return bidi;
});
