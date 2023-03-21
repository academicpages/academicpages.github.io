'use strict';

var copy = require('copy-to');

copy(require('./function'))
.and(require('./polyfill'))
.and(require('./optimize'))
.and(require('./crypto'))
.and(require('./number'))
.and(require('./string'))
.and(require('./array'))
.and(require('./json'))
.and(require('./date'))
.and(require('./object'))
.and(require('./web'))
.to(module.exports);
