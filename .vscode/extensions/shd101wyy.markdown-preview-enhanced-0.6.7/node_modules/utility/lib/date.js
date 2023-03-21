'use strict';

var MONTHS = [
  'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
];

// only set once.
var TIMEZONE = ' ';
var _hourOffset = parseInt(-(new Date().getTimezoneOffset()) / 60, 10);
if (_hourOffset >= 0) {
  TIMEZONE += '+';
} else {
  TIMEZONE += '-';
}
_hourOffset = Math.abs(_hourOffset);
if (_hourOffset < 10) {
  _hourOffset = '0' + _hourOffset;
}
TIMEZONE += _hourOffset + '00';

/**
 * Access log format date. format: `moment().format('DD/MMM/YYYY:HH:mm:ss ZZ')`
 *
 * @return {String}
 */
exports.accessLogDate = function (d) {
  // 16/Apr/2013:16:40:09 +0800
  d = d || new Date();
  var date = d.getDate();
  if (date < 10) {
    date = '0' + date;
  }
  var hours = d.getHours();
  if (hours < 10) {
    hours = '0' + hours;
  }
  var mintues = d.getMinutes();
  if (mintues < 10) {
    mintues = '0' + mintues;
  }
  var seconds = d.getSeconds();
  if (seconds < 10) {
    seconds = '0' + seconds;
  }
  return date + '/' + MONTHS[d.getMonth()] + '/' + d.getFullYear() +
    ':' + hours + ':' + mintues + ':' + seconds + TIMEZONE;
};

/**
 * Normal log format date. format: `moment().format('YYYY-MM-DD HH:mm:ss.SSS')`
 *
 * @return {String}
 */
exports.logDate = exports.YYYYMMDDHHmmssSSS = function (d, msSep) {
  if (typeof d === 'string') {
    // logDate(msSep)
    msSep = d;
    d = new Date();
  } else {
    // logDate(d, msSep)
    d = d || new Date();
  }
  var date = d.getDate();
  if (date < 10) {
    date = '0' + date;
  }
  var month = d.getMonth() + 1;
  if (month < 10) {
    month = '0' + month;
  }
  var hours = d.getHours();
  if (hours < 10) {
    hours = '0' + hours;
  }
  var mintues = d.getMinutes();
  if (mintues < 10) {
    mintues = '0' + mintues;
  }
  var seconds = d.getSeconds();
  if (seconds < 10) {
    seconds = '0' + seconds;
  }
  var milliseconds = d.getMilliseconds();
  if (milliseconds < 10) {
    milliseconds = '00' + milliseconds;
  } else if (milliseconds < 100) {
    milliseconds = '0' + milliseconds;
  }
  return d.getFullYear() + '-' + month + '-' + date + ' ' +
    hours + ':' + mintues + ':' + seconds + (msSep || '.') + milliseconds;
};

/**
 * `moment().format('YYYY-MM-DD HH:mm:ss')` format date string.
 *
 * @return {String}
 */
exports.YYYYMMDDHHmmss = function (d, options) {
  d = d || new Date();
  if (!(d instanceof Date)) {
    d = new Date(d);
  }

  var dateSep = '-';
  var timeSep = ':';
  if (options) {
    if (options.dateSep) {
      dateSep = options.dateSep;
    }
    if (options.timeSep) {
      timeSep = options.timeSep;
    }
  }
  var date = d.getDate();
  if (date < 10) {
    date = '0' + date;
  }
  var month = d.getMonth() + 1;
  if (month < 10) {
    month = '0' + month;
  }
  var hours = d.getHours();
  if (hours < 10) {
    hours = '0' + hours;
  }
  var mintues = d.getMinutes();
  if (mintues < 10) {
    mintues = '0' + mintues;
  }
  var seconds = d.getSeconds();
  if (seconds < 10) {
    seconds = '0' + seconds;
  }
  return d.getFullYear() + dateSep + month + dateSep + date + ' ' +
    hours + timeSep + mintues + timeSep + seconds;
};

/**
 * `moment().format('YYYY-MM-DD')` format date string.
 *
 * @return {String}
 */
exports.YYYYMMDD = function YYYYMMDD(d, sep) {
  if (typeof d === 'string') {
    // YYYYMMDD(sep)
    sep = d;
    d = new Date();
  } else {
    // YYYYMMDD(d, sep)
    d = d || new Date();
    if (typeof sep !== 'string') {
      sep = '-';
    }
  }
  var date = d.getDate();
  if (date < 10) {
    date = '0' + date;
  }
  var month = d.getMonth() + 1;
  if (month < 10) {
    month = '0' + month;
  }
  return d.getFullYear() + sep + month + sep + date;
};

/**
 * return datetime struct.
 *
 * @return {Object} date
 *  - {Number} YYYYMMDD, 20130401
 *  - {Number} H, 0, 1, 9, 12, 23
 */
exports.datestruct = function (now) {
  now = now || new Date();
  return {
    YYYYMMDD: now.getFullYear() * 10000 + (now.getMonth() + 1) * 100 + now.getDate(),
    H: now.getHours()
  };
};

/**
 * Get Unix's timestamp in seconds.
 * @return {Number}
 */
exports.timestamp = function timestamp(t) {
  if (t) {
    var v = t;
    if (typeof v === 'string') {
      v = Number(v);
    }
    if (String(t).length === 10) {
      v *= 1000;
    }
    return new Date(v);
  }
  return Math.round(Date.now() / 1000);
};
