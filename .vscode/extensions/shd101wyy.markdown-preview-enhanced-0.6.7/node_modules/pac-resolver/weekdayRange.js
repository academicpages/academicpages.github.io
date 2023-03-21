
/**
 * Module exports.
 */

module.exports = weekdayRange;

/**
 * Only the first parameter is mandatory. Either the second, the third, or both
 * may be left out.
 *
 * If only one parameter is present, the function yeilds a true value on the
 * weekday that the parameter represents. If the string "GMT" is specified as
 * a second parameter, times are taken to be in GMT, otherwise in local timezone.
 *
 * If both wd1 and wd1 are defined, the condition is true if the current weekday
 * is in between those two weekdays. Bounds are inclusive. If the "GMT" parameter
 * is specified, times are taken to be in GMT, otherwise the local timezone is
 * used.
 *
 * Valid "weekday strings" are:
 *
 *     SUN MON TUE WED THU FRI SAT
 *
 * Examples:
 *
 * ``` js
 * weekdayRange("MON", "FRI")
 * true Monday trhough Friday (local timezone).
 *
 * weekdayRange("MON", "FRI", "GMT")
 * same as above, but GMT timezone.
 *
 * weekdayRange("SAT")
 * true on Saturdays local time.
 *
 * weekdayRange("SAT", "GMT")
 * true on Saturdays GMT time.
 *
 * weekdayRange("FRI", "MON")
 * true Friday through Monday (note, order does matter!).
 * ```
 *
 * 
 * @param {String} wd1 one of the weekday strings.
 * @param {String} wd2 one of the weekday strings.
 * @param {String} gmt is either the string: GMT or is left out.
 * @return {Boolean}
 */

const dayOrder = { "SUN": 0, "MON": 1, "TUE": 2, "WED": 3, "THU": 4, "FRI": 5, "SAT": 6 };

function weekdayRange (wd1, wd2, gmt) {

  var useGMTzone = (wd2 == "GMT" || gmt == "GMT"),
      todaysDay  = getTodaysDay(useGMTzone),
      wd1Index   = dayOrder[wd1] || -1,
      wd2Index   = dayOrder[wd2] || -1,
      result     = false;

  if (wd2Index < 0) {
    result = (todaysDay == wd1Index);
  } else {
    if (wd1Index <= wd2Index) {
      result = valueInRange(wd1Index, todaysDay, wd2Index);
    } else {
      result = valueInRange(wd1Index, todaysDay, 6) || valueInRange(0, todaysDay, wd2Index);
    }
  }
  return result;
}

function getTodaysDay (gmt) {
  return (gmt ? (new Date()).getUTCDay() : (new Date()).getDay());
}

// start <= value <= finish
function valueInRange (start, value, finish) {
  return (start <= value) && (value <= finish);
}
