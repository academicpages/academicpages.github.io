export = utility;
export as namespace utility;


// ---------------------------------
/**
 * @description Types definition by github@ddzy
 * @see https://github.com/node-modules/utility
 */
// ------------------------------------


declare namespace utility {

  /**
   * ---------------0_0----------------
   * @description Defines For Array
   * @see https://github.com/node-modules/utility
   * ---------------0^0----------------
   */


  /**
   * Static object define
   */
  type ObjStatic = { [key: string]: any };


  /**
   * Array random slice with items count.
   * @param {Array} arr
   * @param {Number} num, number of sub items.
   * @return {Array}
   */
  function randomSlice(
    arr: any[],
    num?: number,
  ): any[];

  /**
   * Remove one exists element from an array
   * @param {Array} arr
   * @param  {Number} index - remove element index
   * @return {Array} the array instance
   */
  function spliceOne(
    arr: any[],
    index: number,
  ): any[];


  /**
   * --------------------0_0----------------
   * @description Defines For Crypto
   * @see https://github.com/node-modules/utility#md5
   * --------------0^0------------------
   */


  /**
   * hash
   *
   * @param {String} method hash method, e.g.: 'md5', 'sha1'
   * @param {String|Buffer} s
   * @param {String} [format] output string format, could be 'hex' or 'base64'. default is 'hex'.
   * @return {String} md5 hash string
   * @public
   */
  function hash(
    method: 'md5' | 'sha1',
    s: string | Buffer,
    format?: 'hex' | 'base64',
  ): string;

  /**
   * md5 hash
   *
   * @param {String|Buffer} s
   * @param {String} [format] output string format, could be 'hex' or 'base64'. default is 'hex'.
   * @return {String} md5 hash string
   * @public
   */
  function md5(
    s: string | Buffer,
    format?: 'hex' | 'base64',
  ): string;

  /**
   * sha1 hash
   *
   * @param {String|Buffer} s
   * @param {String} [format] output string format, could be 'hex' or 'base64'. default is 'hex'.
   * @return {String} sha1 hash string
   * @public
   */
  function sha1(
    s: string | Buffer,
    format?: 'hex' | 'base64',
  ): string;

  /**
   * sha256 hash
   *
   * @param {String|Buffer} s
   * @param {String} [format] output string format, could be 'hex' or 'base64'. default is 'hex'.
   * @return {String} sha256 hash string
   * @public
   */
  function sha256(
    s: string | Buffer,
    format?: 'hex' | 'base64',
  ): string;

  /**
   * HMAC algorithm.
   *
   * Equal bash:
   *
   * ```bash
   * $ echo -n "$data" | openssl dgst -binary -$algorithm -hmac "$key" | openssl $encoding
   * ```
   *
   * @param {String} algorithm, dependent on the available algorithms supported by the version of OpenSSL on the platform.
   *   Examples are 'sha1', 'md5', 'sha256', 'sha512', etc.
   *   On recent releases, `openssl list-message-digest-algorithms` will display the available digest algorithms.
   * @param {String} key, the hmac key to be used.
   * @param {String|Buffer} data, content string.
   * @param {String} [encoding='base64']
   * @return {String} digest string.
   */
  function hmac(
    algorithm: string,
    key: string,
    data: string | Buffer,
    encoding?: 'base64' | string,
  ): string;

  /**
   * Base64 encode string.
   *
   * @param {String|Buffer} s
   * @param {Boolean} [urlsafe=false] Encode string s using a URL-safe alphabet,
   *   which substitutes - instead of + and _ instead of / in the standard Base64 alphabet.
   * @return {String} base64 encode format string.
   */
  function base64encode(
    s: string | Buffer,
    urlsafe?: boolean,
  ): string;

  /**
   * Base64 string decode.
   *
   * @param {String} encode, base64 encoding string.
   * @param {Boolean} [urlsafe=false] Decode string s using a URL-safe alphabet,
   *   which substitutes - instead of + and _ instead of / in the standard Base64 alphabet.
   * @param {encoding} [encoding=utf8] if encoding = buffer, will return Buffer instance
   * @return {String|Buffer} plain text.
   */
  function base64decode(
    encode: string,
    urlsafe?: boolean,
    encoding?: 'utf8' | 'buffer',
  ): string | Buffer;


  /**
   * ----------------0_0-----------------
   * @description Defines For Date
   * @see https://github.com/node-modules/utility#date-utils
   * ---------------0^0------------------
   */


  interface IYYYYMMDDHHmmssStaticOptions {
    dateSep?: string,
    timeSep?: string,
  }
  interface IDateStructStaticReturns {
    YYYYMMDD: number,
    H: number,
  }

  /**
   * Access log format date. format: `moment().format('DD/MMM/YYYY:HH:mm:ss ZZ')`
   *
   * @return {String}
   */
  function accessLogDate(d: Date): string;

  /**
   * Normal log format date. format: `moment().format('YYYY-MM-DD HH:mm:ss.SSS')`
   *
   * @return {String}
   */
  function logDate(
    d: string | Date,
    msSep?: string,
  ): string;

  /**
   * `moment().format('YYYY-MM-DD HH:mm:ss')` format date string.
   *
   * @return {String}
   */
  function YYYYMMDDHHmmss(
    d: Date | string,
    options?: IYYYYMMDDHHmmssStaticOptions,
  ): string;

  /**
   * `moment().format('YYYY-MM-DD')` format date string.
   *
   * @return {String}
   */
  function YYYYMMDD(
    d: string | Date,
    sep?: string,
  ): string;

  /**
   * return datetime struct.
   *
   * @return {Object} date
   *  - {Number} YYYYMMDD, 20130401
   *  - {Number} H, 0, 1, 9, 12, 23
   */
  function datestruct(
    now?: Date,
  ): IDateStructStaticReturns;

  /**
   * Get Unix's timestamp in seconds.
   * @return {Number}
   */
  function timestamp(
    t?: string | number,
  ): number | Date;


  /**
   * ---------------0_0-------------------
   * @description Defines For Function Method
   * @see https://github.com/node-modules/utility#others
   * ---------------0^0--------------------
   */


  /**
   * A empty function.
   *
   * @return {Function}
   * @public
   */
  function noop(): () => any;

  /**
   * Get a function parameter's names.
   *
   * @param {Function} func
   * @param {Boolean} [useCache], default is true
   * @return {Array} names
   */
  function getParamNames(
    func: (...args: any[]) => any,
    cache?: boolean,
  ): string[];


  /**
   * ----------------0_0-----------------------
   * @description Defines For JSON methods
   * @see https://github.com/node-modules/utility#json
   * -----------------0^0-----------------------
   */


  interface IJSONStaticOptions {
    space?: number | string,
    replacer?: (
      key: string,
      value: any,
    ) => any,
  }

  function strictJSONParse(
    str: string,
  ): ObjStatic;

  function readJSONSync(
    filepath: string,
  ): ObjStatic;

  function writeJSONSync(
    filepath: string,
    str: string | ObjStatic,
    options?: IJSONStaticOptions,
  ): void;

  function readJSON(
    filepath: string,
  ): Promise<any>;

  function writeJSON(
    filepath: string,
    str: string | ObjStatic,
    options?: IJSONStaticOptions,
  ): Promise<any>;

  function mkdir(
    dir: string,
  ): Promise<any>;


  /**
   * ------------------0_0------------------------
   * @description Defines For Number Methods
   * @see https://github.com/node-modules/utility#number-utils
   * --------------------0^0----------------------
   */


  /**
   * CONSTANTS STATIC
   */
  const MAX_SAFE_INTEGER: number;
  const MIN_SAFE_INTEGER: number;
  const MAX_SAFE_INTEGER_STR: string;
  const MAX_SAFE_INTEGER_STR_LENGTH: number;

  /**
   * Detect a number string can safe convert to Javascript Number.
   *
   * @param {String} s number format string, like `"123"`, `"-1000123123123123123123"`
   * @return {Boolean}
   */
  function isSafeNumberString(
    s: string,
  ): boolean;

  /**
   * Convert string to Number if string in safe Number scope.
   *
   * @param {String} s number format string.
   * @return {Number|String} success will return Number, otherise return the original string.
   */
  function toSafeNumber(
    s: string | number,
  ): number | string;

  /**
   * Produces a random integer between the inclusive `lower` and `upper` bounds.
   *
   * @param {Number} lower The lower bound.
   * @param {Number} upper The upper bound.
   * @return {Number} Returns the random number.
   */
  function random(
    lower?: number,
    upper?: number,
  ): number;


  /**
   * ------------------0_0--------------------------
   * @description Defines For Object Methods
   * @see https://github.com/node-modules/utility#objectassign
   * -------------------0^0------------------------
   */


  /**
   * High performance assign before node6
   * @param {Object} target - target object
   * @param {Object | Array} objects - object assign from
   * @return {Object} - return target object
   */
  function assign(
    target: ObjStatic,
    objects: ObjStatic | any[],
  ): ObjStatic;

  function has(
    obj: ObjStatic,
    prop: string,
  ): boolean;

  function getOwnEnumerables(
    obj: ObjStatic,
    ignoreNull?: boolean,
  ): string[];

  /**
   * generate a real map object(clean object), no constructor, no __proto__
   * @param {Object} [obj] - init object, optional
   * @return {Object}
   */
  function map(
    obj?: ObjStatic,
  ): ObjStatic;


  /**
   * -----------------0_0---------------------------
   * @description Defines For Optimize Methods
   * @see https://github.com/node-modules/utility#argumentstoarray
   * -----------------0^0------------------------
   */

  interface ITryStaticReturns {
    error: Error | undefined,
    value: any,
  }

  const UNSTABLE_METHOD: {
    /**
     * optimize try catch
     * @param {Function} fn
     * @return {Object}
     *   - {Error} error
     *   - {Mix} value
     */
    try: (
      fn: (...args: any[]) => any,
    ) => ITryStaticReturns,
  };

  /**
   * avoid if (a && a.b && a.b.c)
   * @param {Object} obj
   * @param {...String} keys
   * @return {Object}
   */
  function dig(
    obj: ObjStatic,
    ...args: any[],
  ): any;

  /**
   * optimize arguments to array
   * @param {Arguments} args
   * @return {Array}
   */
  function argumentsToArray(
    ...args: any[],
  ): any[];


  /**
   * -------------------0_0---------------------
   * @description Defines For Polyfill Methods
   * @see https://github.com/node-modules/utility#timers
   * -------------------0^0-------------------
   */


  function setImmediate(
    callback: (...args: any[]) => void,
    ...args: any[],
  ): NodeJS.Immediate;
  function setImmediate(
    fn: (...args: any[]) => any,
    ...args: any[],
  ): void;


  /**
   * ------------------0_0--------------------
   * @description Defines For String Methods
   * @see https://github.com/node-modules/utility#others
   * -------------------0^0---------------------
   */


  interface IReplaceInvalidHttpHeaderCharReturns {
    val: string,
    invalid: boolean,
  }

  function randomString(
    length?: number,
    charSet?: string | string[],
  ): string;

  /**
   * split string to array
   * @param  {String} str
   * @param  {String} [sep] default is ','
   * @return {Array}
   */
  function split(
    str: string,
    sep?: string,
  ): string[];

  /**
   * always optimized
   */
  function splitAlwaysOptimized(
    ...args: any[],
  ): string[];

  /**
   * Replace string
   *
   * @param  {String} str
   * @param  {String|RegExp} substr
   * @param  {String|Function} newSubstr
   * @return {String}
   */
  function replace(
    str: string,
    substr: string | RegExp,
    newSubstr: string | ((...args: any[]) => any),
  ): string;

  /**
   * Replace invalid http header characters with replacement
   *
   * @param  {String} val
   * @param  {String|Function} replacement - can be `function(char)`
   * @return {Object}
   */
  function replaceInvalidHttpHeaderChar(
    val: string,
    replacement?: string | ((...args: any[]) => any)
  ): IReplaceInvalidHttpHeaderCharReturns;

  /**
   * Detect invalid http header characters in a string
   *
   * @param {String} val
   * @return {Boolean}
   */
  function includesInvalidHttpHeaderChar(
    val: string,
  ): boolean;


  /**
   * ------------------0_0----------------------
   * @description Defines For Web Methods
   * @see https://github.com/node-modules/utility#decode-and-encode
   * ------------------0^0------------------------
   */


  /**
   * Escape the given string of `html`.
   *
   * @param {String} html
   * @return {String}
   * @public
   */
  function escape(
    test: string,
  ): string;

  /**
   * Unescape the given string from html
   * @param {String} html
   * @param {String} type
   * @return {String}
   * @public
   */
  function unescape(
    html: string,
    type?: string,
  ): string | ObjStatic;

  /**
   * Safe encodeURIComponent, won't throw any error.
   * If `encodeURIComponent` error happen, just return the original value.
   *
   * @param {String} text
   * @return {String} URL encode string.
   */
  function encodeURIComponent(
    text: string,
  ): string;

  /**
   * Safe decodeURIComponent, won't throw any error.
   * If `decodeURIComponent` error happen, just return the original value.
   *
   * @param {String} encodeText
   * @return {String} URL decode original string.
   */
  function decodeURIComponent(
    encodeText: string,
  ): string;
}
