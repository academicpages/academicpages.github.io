/*************************************************************
 *
 *  MathJax/extensions/TeX/xypic.js
 *
 *  Implements Xy-pic environment.
 *  
 *  ---------------------------------------------------------------------
 *  
 *  Copyright (c) 2011-2014 Isao Sonobe <sonoisa@gmail.com>.
 * 
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 * 
 *      http://www.apache.org/licenses/LICENSE-2.0
 * 
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 */

(function () {
  
  var FP = MathJax.Extension.fp = {
    version: "0.1"
  };
  
  /************ Matcher **************/
  FP.Matcher = MathJax.Object.Subclass({
    Init: function () { this.cases = []; },
    Case: function (klass, f) {
      this.cases.push([klass, f]);
      return this;
    },
    match: function (x) {
      if (x instanceof Object && "isa" in x) {
        var i, count, klass, op;
        i = 0;
        count = this.cases.length;
        while (i < count) {
          klass = this.cases[i][0];
          if (x.isa(klass)) {
            op = klass.unapply(x);
            if (op.isDefined) {
              return this.cases[i][1](op.get);
            }
          }
          i = i + 1;
        }
      }
      throw FP.MatchError(x);
    }
  });
  
  /************ Option **************/
  FP.Option = MathJax.Object.Subclass({});

  FP.Option.Some = FP.Option.Subclass({
    Init: function (value) {
      this.get = value;
    },
    isEmpty: false,
    isDefined: true,
    getOrElse: function (ignore) { return this.get; },
    flatMap: function (k) {
      return k(this.get);
    },
    map: function (f) {
      return FP.Option.Some(f(this.get));
    },
    foreach: function (f) {
      f(this.get);
    },
    toString: function () {
      return "Some(" + this.get + ")";
    }
  }, {
    unapply: function (x) { return FP.Option.Some(x.get); }
  });

  FP.Option.None = FP.Option.Subclass({
    Init: function () {},
    isEmpty: true,
    isDefined: false,
    getOrElse: function (value) { return value; },
    flatMap: function (k) { return this; },
    foreach: function (f) {},
    map: function (k) { return this; },
    toString: function () { return "None"; }
  }, {
    unapply: function (x) { return FP.Option.Some(x); }
  });

  FP.Option.Augment({}, {
    empty: FP.Option.None()
  });


  /************ List **************/
  FP.List = MathJax.Object.Subclass({});

  FP.List.Cons = FP.List.Subclass({
    Init: function (head, tail) {
      this.head = head;
      this.tail = tail;
    },
    isEmpty: false,
    at: function (index) {
      if (index < 0 || index >= this.length()) {
        throw Error("no such element at " + index + ". index must be lower than " + this.length() + ".");
      }
      var t = this;
      for (var i = 0; i < index; i++) {
        t = t.tail;
      }
      return t.head;
    },
    length: function () {
      var t = this;
      var l = 0;
      while (!t.isEmpty) {
        l++;
        t = t.tail;
      }
      return l;
    },
    prepend: function (element) {
      return FP.List.Cons(element, this);
    },
    append: function (element) {
      var result = FP.List.Cons(element, FP.List.empty);
      this.reverse().foreach(function (e) {
        result = FP.List.Cons(e, result);
      });
      return result;
    },
    concat: function (that) {
      var result = that;
      this.reverse().foreach(function (e) {
        result = FP.List.Cons(e, result);
      });
      return result;
    },
    foldLeft: function (x0, f) {
      var r, c;
      r = f(x0, this.head);
      c = this.tail;
      while (!c.isEmpty) {
        r = f(r, c.head);
        c = c.tail;
      }
      return r;
    },
    foldRight: function (x0, f) {
      if (this.tail.isEmpty) {
        return f(this.head, x0);
      } else {
        return f(this.head, this.tail.foldRight(x0, f));
      }
    },
    map: function (f) {
      return FP.List.Cons(f(this.head), this.tail.map(f));
    },
    flatMap: function (k) {
      return k(this.head).concat(this.tail.flatMap(k));
    },
    foreach: function (f) {
      var e = this;
      while (!e.isEmpty) {
        f(e.head);
        e = e.tail;
      }
    },
    reverse: function () {
      var r = FP.List.empty;
      this.foreach(function (c) {
        r = FP.List.Cons(c, r);
      });
      return r;
    },
    mkString: function () {
      var open, delim, close;
      switch (arguments.length) {
        case 0:
          open = delim = close = "";
          break;
        case 1:
          delim = arguments[0];
          open = close = "";
          break;
        case 2:
          open = arguments[0];
          delim = arguments[1];
          close = "";
          break;
        default:
          open = arguments[0];
          delim = arguments[1];
          close = arguments[2];
          break;
      }
      var desc, nxt;
      desc = open + this.head.toString();
      nxt = this.tail;
      while (nxt.isa(FP.List.Cons)) {
        desc += delim + nxt.head.toString(); 
        nxt = nxt.tail;
      }
      desc += close;
      return desc;
    },
    toString: function () {
      return this.mkString("[", ", ", "]");
    }
  }, {
    unapply: function (x) { return FP.Option.Some([x.head, x.tail]); }
  });

  FP.List.Nil = FP.List.Subclass({
    isEmpty: true,
    at: function (index) {
      throw Error("cannot get element from an empty list.");
    },
    length: function () { return 0; },
    prepend: function (element) {
      return FP.List.Cons(element, FP.List.empty);
    },
    append: function (element) {
      return FP.List.Cons(element, FP.List.empty);
    },
    concat: function (that) {
      return that;
    },
    foldLeft: function (x0, f) { return x0; },
    foldRight: function (x0, f) { return x0; },
    flatMap: function (f) { return this; },
    map: function (f) { return this; },
    foreach: function (f) {},
    reverse: function () { return this; },
    mkString: function () {
      switch (arguments.length) {
        case 0:
        case 1:
          return "";
        case 2:
          return arguments[0]
        default:
          return arguments[0]+arguments[2];
      }
    },
    toString: function () { return '[]'; }
  }, {
    unapply: function (x) { return FP.Option.Some(x); }
  });

  FP.List.Augment({}, {
    empty: FP.List.Nil(),
    fromArray: function (as) {
      var list, i;
      list = FP.List.empty;
      i = as.length - 1;
      while (i >= 0) {
        list = FP.List.Cons(as[i], list);
        i -= 1;
      }
      return list;
    }
  });


  /************ MatchError **************/
  FP.MatchError = MathJax.Object.Subclass({
    Init: function (obj) { this.obj = obj; },
  //  getMessage: function () {
  //    if (this.obj === null) {
  //      return "null"
  //    } else {
  //      return obj.toString() + " (of class " + obj. + ")"
  //    }
  //  }
    toString: function () { return "MatchError(" + this.obj + ")"; }
  });


  /************ OffsetPosition **************/
  FP.OffsetPosition = MathJax.Object.Subclass({
    Init: function (source, offset) {
      // assert(source.length >= offset)
      this.source = source;
      if (offset === undefined) { this.offset = 0; } else { this.offset = offset; } 
      this._index = null;
      this._line = null;
    },
    index: function () {
      if (this._index !== null) { return this._index; }
      this._index = [];
      this._index.push(0);
      var i = 0;
      while (i < this.source.length) {
        if (this.source.charAt(i) === '\n') { this._index.push(i + 1); }
        i += 1;
      }
      this._index.push(this.source.length);
      return this._index;
    },
    line: function () {
      var lo, hi, mid;
      if (this._line !== null) { return this._line; }
      lo = 0;
      hi = this.index().length - 1;
      while (lo + 1 < hi) {
        mid = (hi + lo) >> 1;
        if (this.offset < this.index()[mid]) {
          hi = mid;
        } else {
          lo = mid;
        }
      }
      this._line = lo + 1;
      return this._line;
    },
    column: function () {
      return this.offset - this.index()[this.line() - 1] + 1;
    },
    lineContents: function () {
      var i, l;
      i = this.index();
      l = this.line();
      return this.source.substring(i[l - 1], i[l]);
    },
    toString: function () { return this.line().toString() + '.' + this.column(); },
    longString: function () {
      var desc, i;
      desc = this.lineContents() + '\n';
      i = 0;
      while (i < this.column()) {
        if (this.lineContents().charAt(i) === '\t') {
          desc += '\t';
        } else {
          desc += ' ';
        }
        i += 1;
      }
      desc += '^';
      return desc;
    },
    isLessThan: function (that) {
      if (that.isa(FP.OffsetPosition)) {
        return this.offset < that.offset;
      } else {
        return (
          this.line() < that.line() || 
          (this.line() === that.line() && this.column() < that.column())
        );
      }
    } 
  });


  /************ StringReader **************/
  FP.StringReader = MathJax.Object.Subclass({
    Init: function (source, offset, context) {
      this.source = source;
      this.offset = offset;
      this.context = context;
    },
    first: function () {
      if (this.offset < this.source.length) {
        return this.source.charAt(this.offset);
      } else {
        return FP.StringReader.EofCh;
      }
    },
    rest: function () {
      if (this.offset < this.source.length) {
        return FP.StringReader(this.source, this.offset + 1, this.context);
      } else {
        return this;
      }
    },
    pos: function () { return FP.OffsetPosition(this.source, this.offset); },
    atEnd: function () { return this.offset >= this.source.length; },
    drop: function (n) {
      var r, count;
      r = this;
      count = n;
      while (count > 0) {
        r = r.rest();
        count -= 1;
      }
      return r;
    }
  }, {
    EofCh: '\x03'
  });


  /************ Parsers **************/
  FP.Parsers = MathJax.Object.Subclass({}, {
    parse: function (p, input) {
      return p.apply(input);
    },
    parseAll: function (p, input) {
      return p.andl(function () { return FP.Parsers.eos(); }).apply(input);
    },
    parseString: function (p, str) {
      var input = FP.StringReader(str, 0, { lastNoSuccess: undefined });
      return FP.Parsers.parse(p, input);
    },
    parseAllString: function (p, str) {
      var input = FP.StringReader(str, 0, { lastNoSuccess: undefined });
      return FP.Parsers.parseAll(p, input);
    },
    _handleWhiteSpace: function (input) {
      var whiteSpaceRegex = input.context.whiteSpaceRegex;
      var source = input.source;
      var offset = input.offset;
      var m = whiteSpaceRegex.exec(source.substring(offset, source.length));
      if (m !== null) {
        return offset + m[0].length;
      } else {
        return offset;
      }
    },
    literal: function (str) {
      return FP.Parsers.Parser(function (input) {
        var source, offset, start, i, j, found;
        source = input.source;
        offset = input.offset;
        start = FP.Parsers._handleWhiteSpace(input);
        i = 0;
        j = start;
        while (i < str.length && j < source.length && 
            str.charAt(i) === source.charAt(j)) {
          i += 1;
          j += 1;
        }
        if (i === str.length) {
          return FP.Parsers.Success(str, input.drop(j - offset));
        } else {
          if (start === source.length) {
            found = "end of source";
          } else {
            found = "`" + source.charAt(start) + "'";
          }
          return FP.Parsers.Failure(
            "`" + str + "' expected but " + found + " found",
            input.drop(start - offset)
          );
        }
      });
    },
    regex: function (rx /* must start with ^ */) {
      if (rx.toString().substring(0, 2) !== "/^") {
        throw ("regex must start with `^' but " + rx);
      }
      return FP.Parsers.Parser(function (input) {
        var source, offset, m, found;
        source = input.source;
        offset = input.offset;
        m = rx.exec(source.substring(offset, source.length));
        if (m !== null) {
          return FP.Parsers.Success(m[0], input.drop(m[0].length));
        } else {
          if (offset === source.length) {
            found = "end of source";
          } else {
            found = "`" + source.charAt(offset) + "'";
          }
          return FP.Parsers.Failure(
            "string matching regex " + rx + " expected but " + found + " found",
            input
          );
        }
      });
    },
    regexLiteral: function (rx /* must start with ^ */) {
      if (rx.toString().substring(0, 2) !== "/^") {
        throw ("regex must start with `^' but " + rx);
      }
      return FP.Parsers.Parser(function (input) {
        var source, offset, start, m, found;
        source = input.source;
        offset = input.offset;
        start = FP.Parsers._handleWhiteSpace(input);
        m = rx.exec(source.substring(start, source.length));
        if (m !== null) {
          return FP.Parsers.Success(m[0], input.drop(start + m[0].length - offset));
        } else {
          if (start === source.length) {
            found = "end of source";
          } else {
            found = "`" + source.charAt(start) + "'";
          }
          return FP.Parsers.Failure(
            "string matching regex " + rx + " expected but " + found + " found",
            input.drop(start - offset)
          );
        }
      });
    },
    eos: function () {
      return FP.Parsers.Parser(function (input) {
        var source, offset, start;
        source = input.source;
        offset = input.offset;
        start = FP.Parsers._handleWhiteSpace(input);
        if (source.length === start) {
          return FP.Parsers.Success("", input);
        } else {
          return FP.Parsers.Failure("end of source expected but `" + 
            source.charAt(start) + "' found", input);
        }
      });
    },
    commit: function (/*lazy*/ p) {
      return FP.Parsers.Parser(function (input) {
        var res = p()(input);
        return (FP.Matcher()
          .Case(FP.Parsers.Success, function (x) { return res; })
          .Case(FP.Parsers.Error, function (x) { return res; })
          .Case(FP.Parsers.Failure, function (x) {
            return FP.Parsers.Error(x[0], x[1]);
          }).match(res)
        );
      });
    },
    //elem: function (kind, p)
    elem: function (e) { return FP.Parsers.accept(e).named('"' + e + '"'); },
    accept: function (e) {
      return FP.Parsers.acceptIf(
        function (x) { return x === e; },
        function (x) { return "`" + e + "' expected but `" + x + "' found"; }
      );
    },
    acceptIf: function (p, err) {
      return FP.Parsers.Parser(function (input) {
        if (p(input.first())) {
          return FP.Parsers.Success(input.first(), input.rest());
        } else {
          return FP.Parsers.Failure(err(input.first()), input);
        }
      });
    },
    //acceptMatch: function (expected, f)
    //acceptSeq: function (es)
    failure: function (msg) {
      return FP.Parsers.Parser(function (input) {
        return FP.Parsers.Failure(msg, input);
      });
    },
    err: function (msg) {
      return FP.Parsers.Parser(function (input) {
        return FP.Parsers.Error(msg, input);
      });
    },
    success: function (v) {
      return FP.Parsers.Parser(function (input) {
        return FP.Parsers.Success(v, input);
      });
    },
    log: function (/*lazy*/ p, name) {
      return FP.Parsers.Parser(function (input) {
        console.log("trying " + name + " at " + input);
        var r = p().apply(input);
        console.log(name + " --> " + r);
        return r;
      });
    },
    rep: function (/*lazy*/ p) {
      var s = FP.Parsers.success(FP.List.empty);
      return FP.Parsers.rep1(p).or(function () { return s; });
    },
    rep1: function (/*lazy*/ p) {
      return FP.Parsers.Parser(function (input) {
        var elems, i, p0, res;
        elems = [];
        i = input;
        p0 = p();
        res = p0.apply(input);
        if (res.isa(FP.Parsers.Success)) {
          while (res.isa(FP.Parsers.Success)) {
            elems.push(res.result);
            i = res.next;
            res = p0.apply(i);
          }
          return FP.Parsers.Success(FP.List.fromArray(elems), i);
        } else {
          return res;
        }
      });
    },
    //rep1: function (/*lazy*/ first, /*lazy*/ p)
    repN: function (num, /*lazy*/ p) {
      if (num === 0) {
        return FP.Parsers.success(FP.List.empty);
      }
      return FP.Parsers.Parser(function (input) {
        var elems, i, p0, res;
        elems = [];
        i = input;
        p0 = p();
        res = p0.apply(i);
        while (res.isa(FP.Parsers.Success)) {
          elems.push(res.result);
          i = res.next;
          if (num === elems.length) {
            return FP.Parsers.Success(FP.List.fromArray(elems), i);
          }
          res = p0.apply(i);
        }
        return res; // NoSuccess
      });
    },
    repsep: function (/*lazy*/ p, /*lazy*/ q) {
      var s = FP.Parsers.success(FP.List.empty);
      return FP.Parsers.rep1sep(p, q).or(function () { return s; });
    },
    rep1sep: function (/*lazy*/ p, /*lazy*/ q) {
      return p().and(FP.Parsers.rep(q().andr(p))).to(function (res) {
        return FP.List.Cons(res.head, res.tail);
      });
    },
  //  chainl1: function (/*lazy*/ p, /*lazy*/ q) {
  //    return this.chainl1(p, p, q)
  //  },
    chainl1: function (/*lazy*/ first, /*lazy*/ p, /*lazy*/ q) {
      return first().and(FP.Parsers.rep(q().and(p))).to(function (res) {
        return res.tail.foldLeft(res.head, function (a, fb) { return fb.head(a, fb.tail); });
      });
    },
    chainr1: function (/*lazy*/ p, /*lazy*/ q, combine, first) {
      return p().and(this.rep(q().and(p))).to(function (res) {
        return FP.List.Cons(FP.Parsers.Pair(combine, res.head),
          res.tail).foldRight(first, function (fa, b) { return fa.head(fa.tail, b); }
          );
      });
    },
    opt: function (/*lazy*/ p) {
      return p().to(function (x) {
        return FP.Option.Some(x);
      }).or(function () {
        return FP.Parsers.success(FP.Option.empty);
      });
    },
    not: function (/*lazy*/ p) {
      return FP.Parsers.Parser(function (input) {
        var r = p().apply(input);
        if (r.successful) {
          return FP.Parsers.Failure("Expected failure", input);
        } else {
          return FP.Parsers.Success(FP.Option.empty, input);
        }
      });
    },
    guard: function (/*lazy*/ p) {
      return FP.Parsers.Parser(function (input) {
        var r = p().apply(input);
        if (r.successful) {
          return FP.Parsers.Success(r.result, input);
        } else {
          return r;
        }
      });
    },
    //positioned: function (/*lazy*/ p)
    //phrase: function (p)
    mkList: function (pair) { return FP.List.Cons(pair.head, pair.tail); },
    fun: function (x) { return function () { return x; }; },
    lazyParser: function (x) {
      var lit, r;
      if (x instanceof String || (typeof x) === "string") {
        lit = FP.Parsers.literal(x);
        return function () { return lit; };
      } else if (x instanceof Function) {
        // x is deemed to be a function which has the return value as Parser. 
        return x;
      } else if (x instanceof Object) {
        if("isa" in x && x.isa(FP.Parsers.Parser)) {
          return function () { return x; };
        } else if (x instanceof RegExp) {
          r = FP.Parsers.regexLiteral(x);
          return function () { return r; };
        } else {
          return FP.Parsers.err("unhandlable type");
        }
      } else {
        return FP.Parsers.err("unhandlable type");
      }
    },
    seq: function () {
      var count, parser, i;
      count = arguments.length;
      if (count === 0) { return FP.Parsers.err("at least one element must be specified"); }
      parser = FP.Parsers.lazyParser(arguments[0])();
      i = 1;
      while (i < count) {
        parser = parser.and(FP.Parsers.lazyParser(arguments[i]));
        i += 1;
      }
      return parser;
    },
    or: function () {
      var count, parser, i;
      count = arguments.length;
      if (count === 0) { return FP.Parsers.err("at least one element must be specified"); }
      parser = FP.Parsers.lazyParser(arguments[0])();
      i = 1;
      while (i < count) {
        parser = parser.or(FP.Parsers.lazyParser(arguments[i]));
        i += 1;
      }
      return parser;
    }
  });


  /************ Pair **************/
  FP.Parsers.Pair = MathJax.Object.Subclass({
    Init: function (head, tail) {
      this.head = head;
      this.tail = tail;
    },
    toString: function () { return '(' + this.head + '~' + this.tail + ')'; }
  }, {
    unapply: function (x) { return FP.Option.Some([x.head, x.tail]); }
  });


  /************ ParseResult **************/
  FP.Parsers.ParseResult = MathJax.Object.Subclass({
    Init: function () {},
    isEmpty: function () { return !this.successful; },
    getOrElse: function (/*lazy*/ defaultValue) {
      if (this.isEmpty) { return defaultValue(); } else { return this.get(); }
    } 
  });


  /************ Success **************/
  FP.Parsers.Success = FP.Parsers.ParseResult.Subclass({
    Init: function (result, next) {
      this.result = result;
      this.next = next;
    },
    map: function (f) { return FP.Parsers.Success(f(this.result), this.next); },
    mapPartial: function (f, err) {
      try {
        return FP.Parsers.Success(f(this.result), this.next);
      } catch (e) {
        if ("isa" in e && e.isa(FP.MatchError)) {
          return FP.Parsers.Failure(err(this.result), this.next);
        } else {
          throw e;
        }
      }
    },
    flatMapWithNext: function (f) { return f(this.result).apply(this.next); },
    append: function (/*lazy*/ a) { return this; },
    get: function () { return this.result; },
    successful: true,
    toString: function () { return '[' + this.next.pos() + '] parsed: ' + this.result; }
  }, {
    unapply: function (x) { return FP.Option.Some([x.result, x.next]); }
  });


  /************ NoSuccess **************/
  FP.Parsers.NoSuccess = FP.Parsers.ParseResult.Subclass({
    Init: function () {},
    _setLastNoSuccess: function () {
      var context = this.next.context;
      if (context.lastNoSuccess === undefined || !this.next.pos().isLessThan(context.lastNoSuccess.next.pos())) {
        context.lastNoSuccess = this;
      }
    },
    map: function (f) { return this; },
    mapPartial: function (f, error) { return this; },
    flatMapWithNext: function (f) { return this; },
    get: function () { return FP.Parsers.error("No result when parsing failed"); },
    successful: false
  });


  /************ Failure **************/
  FP.Parsers.Failure = FP.Parsers.NoSuccess.Subclass({
    Init: function (msg, next) {
      this.msg = msg;
      this.next = next;
      this._setLastNoSuccess();
    },
    append: function (/*lazy*/ a) {
      var alt = a();
      if (alt.isa(FP.Parsers.Success)) {
        return alt;
      } else if (alt.isa(FP.Parsers.NoSuccess)) {
        if (alt.next.pos().isLessThan(this.next.pos())) {
          return this;
        } else {
          return alt;
        }
      } else {
        throw FP.MatchError(alt);
      }
    },
    toString: function () { return ('[' + this.next.pos() + '] failure: ' + 
      this.msg + '\n\n' + this.next.pos().longString()); }
  }, {
    unapply: function (x) { return FP.Option.Some([x.msg, x.next]); }
  });


  /************ Error **************/
  FP.Parsers.Error = FP.Parsers.NoSuccess.Subclass({
    Init: function (msg, next) {
      this.msg = msg;
      this.next = next;
      this._setLastNoSuccess();
    },
    append: function (/*lazy*/ a) { return this; },
    toString: function () { return ('[' + this.next.pos() + '] error: ' + 
      this.msg + '\n\n' + this.next.pos().longString()); }
  }, {
    unapply: function (x) { return FP.Option.Some([x.msg, x.next]); }
  });


  /************ Parser **************/
  FP.Parsers.Parser = MathJax.Object.Subclass({
    Init: function (f) { this.apply = f; },
    name: '',
    named: function (name) { this.name = name; return this; },
    toString: function () { return 'Parser (' + this.name + ')'; },
    flatMap: function (f) {
      var app = this.apply;
      return FP.Parsers.Parser(function (input) {
        return app(input).flatMapWithNext(f);
      });
    },
    map: function (f) {
      var app = this.apply;
      return FP.Parsers.Parser(function (input) {
        return app(input).map(f);
      });
    },
    append: function (/*lazy*/ p) {
      var app = this.apply;
      return FP.Parsers.Parser(function (input) {
        return app(input).append(function () {
          return p().apply(input);
        });
      });
    },
    and: function (/*lazy*/ p) {
      return this.flatMap(function (a) {
        return p().map(function (b) {
          return FP.Parsers.Pair(a, b);
        });
      }).named('~');
    },
    andr: function (/*lazy*/ p) {
      return this.flatMap(function (a) {
        return p().map(function (b) {
          return b;
        });
      }).named('~>');
    },
    andl: function (/*lazy*/ p) {
      return this.flatMap(function (a) {
        return p().map(function (b) {
          return a;
        });
      }).named('<~');
    },
    or: function (/*lazy*/ q) { return this.append(q).named("|"); },
    andOnce: function (/*lazy*/ p) {
      var flatMap = this.flatMap;
      return FP.Parsers.OnceParser(function () {
        return flatMap(function (a) {
          return FP.Parsers.commit(p).map(function (b) {
            return FP.Parsers.Pair(a, b);
          });
        }).named('~!');
      });
    },
    longestOr: function (/*lazy*/ q0) {
      var app = this.apply;
      return FP.Parsers.Parser(function (input) {
        var res1, res2;
        res1 = app(input);
        res2 = q0()(input);
        if (res1.successful) {
          if (res2.successful) {
            if (res2.next.pos().isLessThan(res1.next.pos())) {
              return res1;
            } else {
              return res2;
            }
          } else {
            return res1;
          }
        } else if (res2.successful) {
          return res2;
        } else if (res1.isa(FP.Parsers.Error)) {
          return res1;
        } else {
          if (res2.next.pos().isLessThan(res1.next.pos())) {
            return res1;
          } else {
            return res2;
          }
        }
      }).named("|||");
    },
    to: function (f) { return this.map(f).named(this.toString() + '^^'); },
    ret: function (/*lazy*/ v) {
      var app = this.apply;
      return FP.Parsers.Parser(function (input) {
        return app(input).map(function (x) { return v(); });
      }).named(this.toString() + "^^^");
    },
    toIfPossible: function (f, error) {
      if (error === undefined) {
        error = function (r) { return "Constructor function not defined at " + r; };
      }
      var app = this.apply;
      return FP.Parsers.Parser(function (input) {
        return app(input).mapPartial(f, error);
      }).named(this.toString() + "^?");
    },
    into: function (fq) { return this.flatMap(fq); },
    rep: function () {
      var p = this;
      return FP.Parsers.rep(function () { return p; });
    },
    chain: function (/*lazy*/ sep) {
      var p, lp;
      p = this;
      lp = function () { return p; };
      return FP.Parsers.chainl1(lp, lp, sep);
    },
    rep1: function () {
      var p = this;
      return FP.Parsers.rep1(function () { return p; });
    },
    opt: function () {
      var p = this;
      return FP.Parsers.opt(function () { return p; });
    }
  });


  /************ OnceParser **************/
  FP.Parsers.OnceParser = FP.Parsers.Parser.Subclass({
    Init: function (f) { this.apply = f; },
    and: function (p) {
      var flatMap = this.flatMap;
      return FP.Parsers.OnceParser(function () {
        return flatMap(function (a) {
          return FP.Parsers.commit(p).map(function (b) {
            return FP.Parsers.Pair(a, b);
          });
        });
      }).named('~');
    }
  });
  
  MathJax.Hub.Startup.signal.Post("Functional Programming library Ready");
})();

MathJax.Extension.xypic = {
  version: "0.1",
  constants: {
    whiteSpaceRegex: /^(\s+|%[^\r\n]*(\r\n|\r|\n)?)+/,
    unsupportedBrowserErrorMessage: "Unsupported Browser. Please open with Firefox/Safari/Chrome/Opera"
  },
  signalHandler: {
    signals: [],
    hookedSignals: [],
    chains: [],
    chainSignal: function (successor, predecessors) {
      for (var i = 0; i < predecessors.length; i++) {
        MathJax.Extension.xypic.signalHandler.addSignal(predecessors[i]);
      }
      MathJax.Extension.xypic.signalHandler.chains.push({succ:successor, pred:predecessors});
    },
    addSignal: function (signal) {
      var signals = MathJax.Extension.xypic.signalHandler.signals;
      for (var i = 0; i < signals.length; i++) {
        if (signals[i] === signal) {
          return;
        }
      }
      MathJax.Extension.xypic.signalHandler.signals.push(signal);
      var handler = MathJax.Extension.xypic.signalHandler.handleSignal(signal);
      MathJax.Hub.Register.StartupHook(signal, handler);
    },
    handleSignal: function (signal) {
      return function () {
        MathJax.Extension.xypic.signalHandler.hookedSignals.push(signal);
        MathJax.Extension.xypic.signalHandler.handleChains();
      }
    },
    handleChains: function () {
      var i = 0;
      var chains = MathJax.Extension.xypic.signalHandler.chains;
      var remainingChains = [];
      var invokableSignals = [];
      while (i < chains.length) {
        var c = chains[i];
        var pred = c.pred;
        var invokable = true;
        for (var j = 0; j < pred.length; j++) {
          var p = pred[j];
          if (!MathJax.Extension.xypic.signalHandler.listenedSignal(p)) {
            invokable = false;
            break;
          }
        }
        if (invokable) {
          invokableSignals.push(c.succ);
        } else {
          remainingChains.push(c);
        }
        i++;
      }
      MathJax.Extension.xypic.signalHandler.chains = remainingChains;
      for (i = 0; i < invokableSignals.length; i++) {
        MathJax.Hub.Startup.signal.Post(invokableSignals[i]);
      }
    },
    listenedSignal: function (signal) {
      var signals = MathJax.Extension.xypic.signalHandler.hookedSignals;
      for (var i = 0; i < signals.length; i++) {
        if (signals[i] === signal) {
          return true;
        }
      }
      return false;
    }
  }
}

// "TeX Xy-pic" depends on "Functional Programming library" and "TeX Jax".
MathJax.Extension.xypic.signalHandler.chainSignal("TeX Xy-pic Require", ["Functional Programming library Ready", "TeX Jax Ready"]);

// "HTML-CSS Xy-pic Config" depends on "TeX Xy-pic" and "HTML-CSS Jax".
MathJax.Extension.xypic.signalHandler.chainSignal("HTML-CSS Xy-pic Config Require", ["TeX Xy-pic Ready", "HTML-CSS Jax Ready"]);

// "SVG Xy-pic Config" depends on "TeX Xy-pic" and "SVG Jax".
MathJax.Extension.xypic.signalHandler.chainSignal("SVG Xy-pic Config Require", ["TeX Xy-pic Ready", "SVG Jax Ready"]);

// "Device-Independent Xy-pic" depends on "TeX Xy-pic" OR "SVG Jax".
MathJax.Extension.xypic.signalHandler.chainSignal("Device-Independent Xy-pic Require", ["HTML-CSS Xy-pic Config Ready"]);
MathJax.Extension.xypic.signalHandler.chainSignal("Device-Independent Xy-pic Require", ["SVG Xy-pic Config Ready"]);

// "HTML-CSS Xy-pic" depends on "HTML-CSS Xy-pic Config" and "Device-Independent Xy-pic".
MathJax.Extension.xypic.signalHandler.chainSignal("HTML-CSS Xy-pic Require", ["HTML-CSS Xy-pic Config Ready", "Device-Independent Xy-pic Ready"]);

// "SVG Xy-pic" depends on "SVG Xy-pic Config" and "Device-Independent Xy-pic".
MathJax.Extension.xypic.signalHandler.chainSignal("SVG Xy-pic Require", ["SVG Xy-pic Config Ready", "Device-Independent Xy-pic Ready"]);

MathJax.Hub.Register.StartupHook("TeX Xy-pic Require",function () {
  var FP = MathJax.Extension.fp;
  var MML = MathJax.ElementJax.mml;
  var TEX = MathJax.InputJax.TeX;
  var TEXDEF = TEX.Definitions;
  var xypic = MathJax.Extension.xypic;
  var AST = xypic.AST = MathJax.Object.Subclass({});
  
  MathJax.Hub.Insert(TEXDEF, {
    macros: {
      //hole: ['Macro', '{\\bbox[3pt]{}}']
      hole: ['Macro', '{\\style{visibility:hidden}{x}}'],
      objectstyle: ['Macro', '\\textstyle'],
      labelstyle: ['Macro', '\\scriptstyle'],
      twocellstyle: ['Macro', '\\scriptstyle'],
      xybox: 'Xybox',
      xymatrix: 'Xymatrix',
      newdir: 'XypicNewdir',
      includegraphics: 'Xyincludegraphics'
    },
    environment: {
      xy: ['ExtensionEnv', null, 'XYpic']
    }
  });
  
  // override MathJax.InputJax.TeX.formatError function to display parse error.
  var tex_formatError = TEX.formatError;
  TEX.formatError = function (err, math, displaystyle, script) {
    if (err.xyjaxError !== undefined) {
      return err.toMML();
    } else {
      return tex_formatError(err, math, displaystyle, script);
    }
  }
  
  xypic.memoize = function (object, funcName) {
    var func = object[funcName];
    var memo = function () {
        var value = func.call(this);
        var constFunc = function () {
            return value;
        }
        constFunc.reset = reset;
        object[funcName] = constFunc;
        return value;
    }
    var reset = function () {
        object[funcName] = memo;
    }
    memo.reset = reset;
    reset();
  };
  
  AST.xypic = MML.mbase.Subclass({
    Init: function (cmd) {
      this.data = [];
      this.cmd = cmd;
    },
    type: "xypic",
    inferRow: false,
    defaults: {
      mathbackground: MML.INHERIT,
      mathcolor: MML.INHERIT,
      notation: MML.NOTATION.LONGDIV,
      texClass: MML.TEXCLASS.ORD
    },
    setTeXclass: MML.mbase.setSeparateTeXclasses,
    toString: function () { return this.type + "(" + this.cmd + ")"; }
  });
  
  AST.xypic.newdir = MML.mbase.Subclass({
    Init: function (cmd) {
      this.data = [];
      this.cmd = cmd;
    },
    type: "newdir",
    inferRow: false,
    defaults: {
      mathbackground: MML.INHERIT,
      mathcolor: MML.INHERIT,
      notation: MML.NOTATION.LONGDIV,
      texClass: MML.TEXCLASS.ORD
    },
    setTeXclass: MML.mbase.setSeparateTeXclasses,
    toString: function () { return this.type + "(" + this.cmd + ")"; }
  });
  
  AST.xypic.includegraphics = MML.mbase.Subclass({
    Init: function (cmd) {
      this.data = [];
      this.cmd = cmd;
    },
    type: "includegraphics",
    inferRow: false,
    defaults: {
      mathbackground: MML.INHERIT,
      mathcolor: MML.INHERIT,
      notation: MML.NOTATION.LONGDIV,
      texClass: MML.TEXCLASS.ORD
    },
    setTeXclass: MML.mbase.setSeparateTeXclasses,
    toString: function () { return this.type + "(" + this.cmd + ")"; }
  });
  
  // <pos-decor> ::= <pos> <decor>
  AST.PosDecor = MathJax.Object.Subclass({
    Init: function (pos, decor) {
      this.pos = pos;
      this.decor = decor;
    },
    toString: function () {
      return this.pos.toString() + " " + this.decor;
    }
  });
  
  // <pos>
  AST.Pos = MathJax.Object.Subclass({});
  // <pos> ::= <coord> <pos2>*
  AST.Pos.Coord = MathJax.Object.Subclass({
    Init: function (coord, pos2s) {
      this.coord = coord;
      this.pos2s = pos2s;
    },
    toString: function () {
      return this.coord.toString() + " " + this.pos2s.mkString(" ");
    }
  });
  // <pos2> ::= '+' <coord>
  AST.Pos.Plus = MathJax.Object.Subclass({
    Init: function (coord) {
      this.coord = coord;
    },
    toString: function () {
      return "+(" + this.coord + ")";
    }
  });
  // <pos2> ::= '-' <coord>
  AST.Pos.Minus = MathJax.Object.Subclass({
    Init: function (coord) {
      this.coord = coord;
    },
    toString: function () {
      return "-(" + this.coord + ")";
    }
  });
  // <pos2> ::= '!' <coord>
  AST.Pos.Skew = MathJax.Object.Subclass({
    Init: function (coord) {
      this.coord = coord;
    },
    toString: function () {
      return "!(" + this.coord + ")";
    }
  });
  // <pos2> ::= '.' <coord>
  AST.Pos.Cover = MathJax.Object.Subclass({
    Init: function (coord) {
      this.coord = coord;
    },
    toString: function () {
      return ".(" + this.coord + ")";
    }
  });
  // <pos2> ::= ',' <coord>
  AST.Pos.Then = MathJax.Object.Subclass({
    Init: function (coord) {
      this.coord = coord;
    },
    toString: function () {
      return ",(" + this.coord + ")";
    }
  });
  // <pos2> ::= ';' <coord>
  AST.Pos.SwapPAndC = MathJax.Object.Subclass({
    Init: function (coord) {
      this.coord = coord;
    },
    toString: function () {
      return ";(" + this.coord + ")";
    }
  });
  // <pos2> ::= ':' <coord>
  AST.Pos.SetBase = MathJax.Object.Subclass({
    Init: function (coord) {
      this.coord = coord;
    },
    toString: function () {
      return ":(" + this.coord + ")";
    }
  });
  // <pos2> ::= '::' <coord>
  AST.Pos.SetYBase = MathJax.Object.Subclass({
    Init: function (coord) {
      this.coord = coord;
    },
    toString: function () {
      return "::(" + this.coord + ")";
    }
  });
  // <pos2> ::= '**' <object>
  AST.Pos.ConnectObject = MathJax.Object.Subclass({
    Init: function (object) {
      this.object = object;
    },
    toString: function () {
      return "**(" + this.object + ")";
    }
  });
  // <pos2> ::= '*' <object>
  AST.Pos.DropObject = MathJax.Object.Subclass({
    Init: function (object) {
      this.object = object;
    },
    toString: function () {
      return "*(" + this.object + ")";
    }
  });
  // <pos2> ::= '?' <place>
  AST.Pos.Place = MathJax.Object.Subclass({
    Init: function (place) {
      this.place = place;
    },
    toString: function () {
      return "?(" + this.place + ")";
    }
  });
  // <pos2> ::= '@+' <coord>
  AST.Pos.PushCoord = MathJax.Object.Subclass({
    Init: function (coord) {
      this.coord = coord;
    },
    toString: function () {
      return "@+(" + this.coord + ")";
    }
  });
  // <pos2> ::= '@-' <coord>
  AST.Pos.EvalCoordThenPop = MathJax.Object.Subclass({
    Init: function (coord) {
      this.coord = coord;
    },
    toString: function () {
      return "@-(" + this.coord + ")";
    }
  });
  // <pos2> ::= '@=' <coord>
  AST.Pos.LoadStack = MathJax.Object.Subclass({
    Init: function (coord) {
      this.coord = coord;
    },
    toString: function () {
      return "@=(" + this.coord + ")";
    }
  });
  // <pos2> ::= '@@' <coord>
  AST.Pos.DoCoord = MathJax.Object.Subclass({
    Init: function (coord) {
      this.coord = coord;
    },
    toString: function () {
      return "@@(" + this.coord + ")";
    }
  });
  // <pos2> ::= '@i'
  AST.Pos.InitStack = MathJax.Object.Subclass({
    Init: function () {
    },
    toString: function () {
      return "@i";
    }
  });
  // <pos2> ::= '@('
  AST.Pos.EnterFrame = MathJax.Object.Subclass({
    Init: function () {
    },
    toString: function () {
      return "@(";
    }
  });
  // <pos2> ::= '@)'
  AST.Pos.LeaveFrame = MathJax.Object.Subclass({
    Init: function () {
    },
    toString: function () {
      return "@)";
    }
  });
  // <pos2> ::= '=' '"' <id> '"'
  AST.Pos.SavePos = MathJax.Object.Subclass({
    Init: function (id) {
      this.id = id;
    },
    toString: function () {
      return '="' + this.id + '"';
    }
  });
  // <pos2> ::= '=' <coord> '"' <id> '"'
  AST.Pos.SaveMacro = MathJax.Object.Subclass({
    Init: function (macro, id) {
      this.macro = macro;
      this.id = id;
    },
    toString: function () {
      return "=(" + this.macro + ' "' + this.id + '")';
    }
  });
  // <pos2> ::= '=:' '"' <id> '"'
  AST.Pos.SaveBase = MathJax.Object.Subclass({
    Init: function (id) {
      this.id = id;
    },
    toString: function () {
      return '=:"' + this.id + '"';
    }
  });
  // <pos2> ::= '=@' '"' <id> '"'
  AST.Pos.SaveStack = MathJax.Object.Subclass({
    Init: function (id) {
      this.id = id;
    },
    toString: function () {
      return '=@"' + this.id + '"';
    }
  });
  
  // <coord> 
  AST.Coord = MathJax.Object.Subclass({});
  // <coord> ::= <vector>
  AST.Coord.Vector = MathJax.Object.Subclass({
    Init: function (vector) {
      this.vector = vector;
    },
    toString: function () {
      return this.vector.toString();
    }
  });
  // <coord> ::= <empty> | 'c'
  AST.Coord.C = MathJax.Object.Subclass({
    toString: function () {
      return "c";
    }
  });
  // <coord> ::= 'p'
  AST.Coord.P = MathJax.Object.Subclass({
    toString: function () {
      return "p";
    }
  });
  // <coord> ::= 'x'
  AST.Coord.X = MathJax.Object.Subclass({
    toString: function () {
      return "x";
    }
  });
  // <coord> ::= 'y'
  AST.Coord.Y = MathJax.Object.Subclass({
    toString: function () {
      return "y";
    }
  });
  // <coord> ::= '"' <id> '"'
  AST.Coord.Id = MathJax.Object.Subclass({
    Init: function (id) {
      this.id = id;
    },
    toString: function () {
      return '"' + this.id + '"';
    }
  });
  // <coord> ::= '{' <pos> <decor> '}'
  AST.Coord.Group = MathJax.Object.Subclass({
    Init: function (posDecor) {
      this.posDecor = posDecor;
    },
    toString: function () {
      return '{' + this.posDecor + '}';
    }
  });
  // <coord> ::= 's' <digit>
  // <coord> ::= 's' '{' <nonnegative-number> '}'
  AST.Coord.StackPosition = MathJax.Object.Subclass({
    Init: function (number) {
      this.number = number;
    },
    toString: function () {
      return 's{' + this.number + '}';
    }
  });
  
  // coordinate for xymatrix
  // <coord> ::= '[' ('"'<prefix>'"')? <number> ',' <number> ']'
  AST.Coord.DeltaRowColumn = MathJax.Object.Subclass({
    /**
     * @param {String} prefix name of the xymatrix
     * @param {Number} dr rows below
     * @param {Number} dc columns right
     */
    Init: function (prefix, dr, dc) {
      this.prefix = prefix;
      this.dr = dr;
      this.dc = dc;
    },
    toString: function () {
      return '[' + (this.prefix === ''? '' : '"' + this.prefix + '"') + this.dr + "," + this.dc + "]";
    }
  });
  // coordinate for xymatrix
  // <coord> ::= '[' ('"'<prefix>'"')? ( 'l' | 'r' | 'u' | 'd' )* ']'
  AST.Coord.Hops = MathJax.Object.Subclass({
    /**
     * @param {String} prefix name of the xymatrix
     * @param {List[String]} hops hops
     */
    Init: function (prefix, hops) {
      this.prefix = prefix;
      this.hops = hops;
    },
    toString: function () {
      return '[' + (this.prefix === ''? '' : '"' + this.prefix + '"') + this.hops.mkString("") + "]";
    }
  });
  // coordinate for xymatrix
  // <coord> ::= '[' ('"'<prefix>'"')? ( 'l' | 'r' | 'u' | 'd' )+ <place> ']'
  AST.Coord.HopsWithPlace = MathJax.Object.Subclass({
    /**
     * @param {String} prefix name of the xymatrix
     * @param {List[String]} hops hops
     * @param {AST.Pos.Place} place place
     */
    Init: function (prefix, hops, place) {
      this.prefix = prefix;
      this.hops = hops;
      this.place = place;
    },
    toString: function () {
      return '[' + (this.prefix === ''? '' : '"' + this.prefix + '"') + this.hops.mkString("") + this.place + "]";
    }
  });
  
  // <vector>
  AST.Vector = MathJax.Object.Subclass({});
  // <vector> ::= '(' <factor> ',' <factor> ')'
  AST.Vector.InCurBase = MathJax.Object.Subclass({
    Init: function (x, y) {
      this.x = x;
      this.y = y;
    },
    toString: function () {
      return "(" + this.x + ", " + this.y + ")";
    }
  });
  // <vector> ::= '<' <dimen> ',' <dimen> '>'
  // <vector> ::= '<' <dimen> '>'
  AST.Vector.Abs = MathJax.Object.Subclass({
    Init: function (x, y) {
      this.x = x;
      this.y = y;
    },
    toString: function () {
      return "<" + this.x + ", " + this.y + ">";
    }
  });
  // <vector> ::= 'a' '(' <number> ')'
  AST.Vector.Angle = MathJax.Object.Subclass({
    Init: function (degree) {
      this.degree = degree;
    },
    toString: function () {
      return "a(" + this.degree + ")";
    }
  });
  // <vector> ::= '/' <direction> <dimen> '/'
  AST.Vector.Dir = MathJax.Object.Subclass({
    Init: function (dir, dimen) {
      this.dir = dir;
      this.dimen = dimen;
    },
    toString: function () {
      return "/" + this.dir + " " + this.dimen + "/";
    }
  });
  // <vector> ::= <corner>
  //          |   <corner> '(' <factor> ')'
  AST.Vector.Corner = MathJax.Object.Subclass({
    Init: function (corner, factor) {
      this.corner = corner;
      this.factor = factor;
    },
    toString: function () {
      return this.corner.toString() + "(" + this.factor + ")";
    }
  });
  
  // <corner> ::= 'L' | 'R' | 'D' | 'U'
  //          | 'CL' | 'CR' | 'CD' | 'CU'
  //          | 'LD' | 'RD' | 'LU' | 'RU'
  //          | 'E' | 'P'
  //          | 'A'
  AST.Corner = MathJax.Object.Subclass({});
  AST.Corner.L = MathJax.Object.Subclass({
    toString: function () { return "L"; }
  });
  AST.Corner.R = MathJax.Object.Subclass({
    toString: function () { return "R"; }
  });
  AST.Corner.D = MathJax.Object.Subclass({
    toString: function () { return "D"; }
  });
  AST.Corner.U = MathJax.Object.Subclass({
    toString: function () { return "U"; }
  });
  AST.Corner.CL = MathJax.Object.Subclass({
    toString: function () { return "CL"; }
  });
  AST.Corner.CR = MathJax.Object.Subclass({
    toString: function () { return "CR"; }
  });
  AST.Corner.CD = MathJax.Object.Subclass({
    toString: function () { return "CD"; }
  });
  AST.Corner.CU = MathJax.Object.Subclass({
    toString: function () { return "CU"; }
  });
  AST.Corner.LD = MathJax.Object.Subclass({
    toString: function () { return "LD"; }
  });
  AST.Corner.RD = MathJax.Object.Subclass({
    toString: function () { return "RD"; }
  });
  AST.Corner.LU = MathJax.Object.Subclass({
    toString: function () { return "LU"; }
  });
  AST.Corner.RU = MathJax.Object.Subclass({
    toString: function () { return "RU"; }
  });
  AST.Corner.NearestEdgePoint = MathJax.Object.Subclass({
    toString: function () { return "E"; }
  });
  AST.Corner.PropEdgePoint = MathJax.Object.Subclass({
    toString: function () { return "P"; }
  });
  AST.Corner.Axis = MathJax.Object.Subclass({
    toString: function () { return "A"; }
  });
  
  // <place> ::= '<' <place>
  // <place> ::= '>' <place>
  // <place> ::= '(' <factor> ')' <place>
  // <place> ::= '!' '{' <pos> '}' <slide>
  // <place> ::= <slide>
  AST.Place = MathJax.Object.Subclass({
    Init: function (shaveP, shaveC, factor, slide) {
      this.shaveP = shaveP;
      this.shaveC = shaveC;
      this.factor = factor;
      this.slide = slide;
    },
    compound: function (that) {
      return AST.Place(
        this.shaveP + that.shaveP,
        this.shaveC + that.shaveC,
        that.factor === undefined? this.factor : that.factor,
        that.slide);
    },
    toString: function () {
      var desc = "";
      for (var l = 0; l < this.shaveP; l++) {
        desc += "<";
      }
      for (var r = 0; r < this.shaveC; r++) {
        desc += ">";
      }
      if (this.factor !== undefined) {
        desc += "(" + this.factor + ")";
      }
      this.slide.dimen.foreach(function (d) {
        desc += "/" + d + "/";
      });
      return desc;
    }
  });
  AST.Place.Factor = MathJax.Object.Subclass({
    Init: function (factor) {
      this.factor = factor;
    },
    isIntercept: false,
    toString: function () {
      return this.factor.toString();
    }
  });
  AST.Place.Intercept = MathJax.Object.Subclass({
    Init: function (pos) {
      this.pos = pos;
    },
    isIntercept: true,
    toString: function () {
      return "!{" + this.pos + "}";
    }
  });
  
  // <slide> ::= <empty>
  // <slide> ::= '/' <dimen> '/'
  AST.Slide = MathJax.Object.Subclass({
    Init: function (dimen) {
      this.dimen = dimen;
    },
    toString: function () {
      return this.dimen.getOrElse("");
    }
  });
  
  
  // <object> ::= <modifier>* <objectbox>
  AST.Object = MathJax.Object.Subclass({
    Init: function (modifiers, object) {
      this.modifiers = modifiers;
      this.object = object;
    },
    dirVariant: function () { return this.object.dirVariant(); },
    dirMain: function () { return this.object.dirMain(); },
    isDir: function () { return this.object.isDir(); },
    toString: function () {
      return this.modifiers.mkString() + this.object.toString();
    }
  });
  
  // <objectbox>
  AST.ObjectBox = MathJax.Object.Subclass({
    dirVariant: function () { return undefined; },
    dirMain: function () { return undefined; },
    isDir: function () { return false; },
    isEmpty: false
  });
  // <objectbox> ::= '{' <text> '}'
  // <objectbox> ::= <TeX box> '{' <text> '}'
  AST.ObjectBox.Text = AST.ObjectBox.Subclass({
    Init: function (math) {
      this.math = math;
    },
    toString: function () { return "{" + this.math.toString() + "}"; }
  });
  AST.ObjectBox.Empty = AST.ObjectBox.Subclass({
    isEmpty: true,
    toString: function () { return "{}"; }
  });
  
  // <objectbox> ::= 'xymatrix' <xymatrix>
  AST.ObjectBox.Xymatrix = AST.ObjectBox.Subclass({
    /**
     * @param {AST.Command.Xymatrix} xymatrix xymatrix
     */
    Init: function (xymatrix) {
      this.xymatrix = xymatrix;
    },
    toString: function () { return this.xymatrix.toString(); }
  });
  
  // <objectbox> ::= '\txt' <width> <style> '{' <text> '}'
  AST.ObjectBox.Txt = AST.ObjectBox.Subclass({
    Init: function (width, textObject) {
      this.width = width;
      this.textObject = textObject;
    },
    toString: function () { return "\\txt" + this.width + "{" + this.textObject.toString() + "}"; }
  });
  AST.ObjectBox.Txt.Width = AST.ObjectBox.Subclass({
  });
  AST.ObjectBox.Txt.Width.Vector = AST.ObjectBox.Subclass({
    Init: function (vector) {
      this.vector = vector;
    },
    toString: function () { return this.vector.toString(); }
  });
  AST.ObjectBox.Txt.Width.Default = AST.ObjectBox.Subclass({
    toString: function () { return ""; }
  });
  
  // <objectbox> ::= '\object' <object>
  AST.ObjectBox.WrapUpObject = AST.ObjectBox.Subclass({
    Init: function (object) {
      this.object = object;
    },
    toString: function () { return "\\object" + this.object.toString(); }
  });
  
  // <objectbox> ::= '\composite' '{' <composite_object> '}'
  // <composite_object> ::= <object> ( '*' <object> )*
  AST.ObjectBox.CompositeObject = AST.ObjectBox.Subclass({
    Init: function (objects) {
      this.objects = objects;
    },
    toString: function () { return "\\composite{" + this.objects.mkString(" * ") + "}"; }
  });
  
  // <objectbox> ::= '\xybox' '{' <pos> <decor> '}'
  AST.ObjectBox.Xybox = AST.ObjectBox.Subclass({
    Init: function (posDecor) {
      this.posDecor = posDecor;
    },
    toString: function () { return "\\xybox{" + this.posDecor.toString() + "}"; }
  });
  
  // <objectbox> ::= '\cir' <radius> '{' <cir> '}'
  // <cir_radius> ::= <vector>
  //          | <empty>
  // <cir> ::= <diag> <orient> <diag>
  //       | <empty>
  AST.ObjectBox.Cir = AST.ObjectBox.Subclass({
    Init: function (radius, cir) {
      this.radius = radius;
      this.cir = cir;
    },
    toString: function () {
      return "\\cir"+this.radius+"{"+this.cir+"}";
    }
  });
  AST.ObjectBox.Cir.Radius = MathJax.Object.Subclass({});
  AST.ObjectBox.Cir.Radius.Vector = MathJax.Object.Subclass({
    Init: function (vector) {
      this.vector = vector;
    },
    toString: function () { return this.vector.toString(); }
  });
  AST.ObjectBox.Cir.Radius.Default = MathJax.Object.Subclass({
    toString: function () { return ""; }
  });
  AST.ObjectBox.Cir.Cir = MathJax.Object.Subclass({});
  AST.ObjectBox.Cir.Cir.Segment = MathJax.Object.Subclass({
    Init: function (startDiag, orient, endDiag) {
      this.startDiag = startDiag;
      this.orient = orient;
      this.endDiag = endDiag;
    },
    toString: function () { return this.startDiag.toString()+this.orient+this.endDiag; }
  });
  AST.ObjectBox.Cir.Cir.Full = MathJax.Object.Subclass({
    toString: function () { return ""; }
  });
  
  // <objectbox> ::= '\dir' <variant> '{' <main> '}'
  // <variant> ::= '^' | '_' | '0' | '1' | '2' | '3' | <empty>
  // <main> ::= ('-' | '.' | '~' | '>' | '<' | '(' | ')' | '`' | "'" | '|' | '*' | '+' | 'x' | '/' | 'o' | '=' | ':' | /[a-zA-Z@ ]/)*
  AST.ObjectBox.Dir = AST.ObjectBox.Subclass({
    Init: function (variant, main) {
      this.variant = variant;
      this.main = main;
    },
    dirVariant: function () { return this.variant; },
    dirMain: function () { return this.main; },
    isDir: function () { return true; },
    toString: function () { return "\\dir" + this.variant + "{" + this.main + "}"; }
  });
  
  // <objectbox> ::= '\crv' <curve-modifier> '{' <curve-object> <curve-poslist> '}'
  AST.ObjectBox.Curve = AST.ObjectBox.Subclass({
    Init: function (modifiers, objects, poslist) {
      this.modifiers = modifiers;
      this.objects = objects;
      this.poslist = poslist;
    },
    dirVariant: function () { return ""; },
    dirMain: function () { return "-"; },
    isDir: function () { return false; },
    toString: function () { return "\\curve"+this.modifiers.mkString("")+"{"+this.objects.mkString(" ")+" "+this.poslist.mkString("&")+"}"; }
  });
  // <curve-modifier> ::= ( '~' <curve-option> )*
  // <curve-option> ::= 'p' | 'P' | 'l' | 'L' | 'c' | 'C'
  //                |   'pc' | 'pC' | 'Pc' | 'PC'
  //                |   'lc' | 'lC' | 'Lc' | 'LC'
  //                |   'cC'
  AST.ObjectBox.Curve.Modifier = MathJax.Object.Subclass({});
  AST.ObjectBox.Curve.Modifier.p = MathJax.Object.Subclass({
    toString: function () { return "~p"; }
  });
  AST.ObjectBox.Curve.Modifier.P = MathJax.Object.Subclass({
    toString: function () { return "~P"; }
  });
  AST.ObjectBox.Curve.Modifier.l = MathJax.Object.Subclass({
    toString: function () { return "~l"; }
  });
  AST.ObjectBox.Curve.Modifier.L = MathJax.Object.Subclass({
    toString: function () { return "~L"; }
  });
  AST.ObjectBox.Curve.Modifier.c = MathJax.Object.Subclass({
    toString: function () { return "~c"; }
  });
  AST.ObjectBox.Curve.Modifier.C = MathJax.Object.Subclass({
    toString: function () { return "~C"; }
  });
  AST.ObjectBox.Curve.Modifier.pc = MathJax.Object.Subclass({
    toString: function () { return "~pc"; }
  });
  AST.ObjectBox.Curve.Modifier.pC = MathJax.Object.Subclass({
    toString: function () { return "~pC"; }
  });
  AST.ObjectBox.Curve.Modifier.Pc = MathJax.Object.Subclass({
    toString: function () { return "~Pc"; }
  });
  AST.ObjectBox.Curve.Modifier.PC = MathJax.Object.Subclass({
    toString: function () { return "~PC"; }
  });
  AST.ObjectBox.Curve.Modifier.lc = MathJax.Object.Subclass({
    toString: function () { return "~lc"; }
  });
  AST.ObjectBox.Curve.Modifier.lC = MathJax.Object.Subclass({
    toString: function () { return "~lC"; }
  });
  AST.ObjectBox.Curve.Modifier.Lc = MathJax.Object.Subclass({
    toString: function () { return "~Lc"; }
  });
  AST.ObjectBox.Curve.Modifier.LC = MathJax.Object.Subclass({
    toString: function () { return "~LC"; }
  });
  AST.ObjectBox.Curve.Modifier.cC = MathJax.Object.Subclass({
    toString: function () { return "~cC"; }
  });
  // <curve-object> ::= <empty>
  //                |   '~*' <object> <curve-object>
  //                |   '~**' <object> <curve-object>
  AST.ObjectBox.Curve.Object = MathJax.Object.Subclass({});
  AST.ObjectBox.Curve.Object.Drop = MathJax.Object.Subclass({
    Init: function (object) {
      this.object = object;
    },
    toString: function () { return "~*" + this.object; }
  });
  AST.ObjectBox.Curve.Object.Connect = MathJax.Object.Subclass({
    Init: function (object) {
      this.object = object;
    },
    toString: function () { return "~**" + this.object; }
  });
  // <curve-poslist> ::= <empty> ^^ Empty List
  //           |   '&' <curve-poslist2> ^^ (c, <poslist>)
  //           |   <nonemptyPos> ^^ (<nonemptyPos>, Nil)
  //           |   <nonemptyPos> '&' <curve-poslist2> ^^ (<nonemptyPos>, <poslist>)
  //           |   '~@' ^^ (~@, Nil)
  //           |   '~@' '&' <curve-poslist2> ^^ (~@, <poslist>)
  // <curve-poslist2> ::= <empty> ^^ (c, Nil)
  //           |   '&' <curve-poslist2> ^^ (c, <poslist>)
  //           |   <nonemptyPos> ^^ (<nonemptyPos>, Nil)
  //           |   <nonemptyPos> '&' <curve-poslist2> ^^ (<nonemptyPos>, <poslist>)
  //           |   '~@' ^^ (~@, Nil)
  //           |   '~@' '&' <curve-poslist2> ^^ (~@, <poslist>)
  AST.ObjectBox.Curve.PosList = MathJax.Object.Subclass({});
  AST.ObjectBox.Curve.PosList.CurPos = MathJax.Object.Subclass({
    toString: function () { return ""; }
  });
  AST.ObjectBox.Curve.PosList.Pos = MathJax.Object.Subclass({
    Init: function (pos) {
      this.pos = pos;
    },
    toString: function () { return this.pos.toString(); }
  });
  AST.ObjectBox.Curve.PosList.AddStack = MathJax.Object.Subclass({
    toString: function () { return "~@"; }
  });
  
  // <modifier>
  AST.Modifier = MathJax.Object.Subclass({
  });
  // <modifier> ::= '!' <vector>
  AST.Modifier.Vector = AST.Modifier.Subclass({
    Init: function (vector) {
      this.vector = vector;
    },
    toString: function () { return "!" + this.vector; }
  });
  // <modifier> ::= '!'
  AST.Modifier.RestoreOriginalRefPoint = AST.Modifier.Subclass({
    toString: function () { return "!"; }
  });
  // <modifier> ::= <add-op> <size>
  // <add-op> ::= '+' | '-' | '=' | '+=' | '-='
  // <size> ::= <vector> | <empty>
  AST.Modifier.AddOp = AST.Modifier.Subclass({
    Init: function (op, size) {
      this.op = op;
      this.size = size;
    },
    toString: function () { return this.op.toString() + " " + this.size; }
  });
  AST.Modifier.AddOp.Grow = MathJax.Object.Subclass({
    toString: function () { return '+'; }
  });
  AST.Modifier.AddOp.Shrink = MathJax.Object.Subclass({
    toString: function () { return '-'; }
  });
  AST.Modifier.AddOp.Set = MathJax.Object.Subclass({
    toString: function () { return '='; }
  });
  AST.Modifier.AddOp.GrowTo = MathJax.Object.Subclass({
    toString: function () { return '+='; }
  });
  AST.Modifier.AddOp.ShrinkTo = MathJax.Object.Subclass({
    toString: function () { return '-='; }
  });
  AST.Modifier.AddOp.VactorSize = MathJax.Object.Subclass({
    Init: function (vector) {
      this.vector = vector;
    },
    isDefault: false,
    toString: function () { return this.vector.toString(); }
  });
  AST.Modifier.AddOp.DefaultSize = MathJax.Object.Subclass({
    isDefault: true,
    toString: function () { return ""; }
  });
  
  // <modifier> ::= '[' <shape> ']'
  // <shape> ::= '.' 
  //          | <frame_shape>
  //          | <alphabets>
  //          | '=' <alphabets>
  //          | <empty>
  // <alphabets> ::= /[a-zA-Z]+/
  AST.Modifier.Shape = MathJax.Object.Subclass({});
  AST.Modifier.Shape.Point = AST.Modifier.Subclass({
    toString: function () { return "[.]"; }
  });
  AST.Modifier.Shape.Rect = AST.Modifier.Subclass({
    toString: function () { return "[]"; }
  });
  AST.Modifier.Shape.Alphabets = AST.Modifier.Subclass({
    Init: function (alphabets) {
      this.alphabets = alphabets;
    },
    toString: function () { return "[" + this.alphabets + "]"; }
  });
  AST.Modifier.Shape.DefineShape = AST.Modifier.Subclass({
    Init: function (shape) {
      this.shape = shape;
    },
    toString: function () { return "[" + this.shape + "]"; }
  });
  // 以下はxypic.ModifierRepositoryに格納されるもの
  AST.Modifier.Shape.Circle = AST.Modifier.Subclass({
    toString: function () { return "[o]"; }
  });
  AST.Modifier.Shape.L = AST.Modifier.Subclass({
    toString: function () { return "[l]"; }
  });
  AST.Modifier.Shape.R = AST.Modifier.Subclass({
    toString: function () { return "[r]"; }
  });
  AST.Modifier.Shape.U = AST.Modifier.Subclass({
    toString: function () { return "[u]"; }
  });
  AST.Modifier.Shape.D = AST.Modifier.Subclass({
    toString: function () { return "[d]"; }
  });
  AST.Modifier.Shape.C = AST.Modifier.Subclass({
    toString: function () { return "[c]"; }
  });
  AST.Modifier.Shape.ChangeColor = AST.Modifier.Subclass({
    Init: function (colorName) {
      this.colorName = colorName;
    },
    toString: function () { return "[" + this.colorName + "]"; }
  });
  // ユーザ定義されたshape
  AST.Modifier.Shape.CompositeModifiers = AST.Modifier.Subclass({
    /**
     * @param {List[AST.Modifier.Shape.*]} modifiers ユーザ定義されたmodifierのリスト
     */
    Init: function (modifiers) {
      this.modifiers = modifiers;
    },
    toString: function () { return this.modifiers.mkString(""); }
  });
  
  // <frame_shape> ::= 'F' <frame_main> ( ':' ( <frame_radius_vector> | <color_name> ))*
  AST.Modifier.Shape.Frame = AST.Modifier.Subclass({
    Init: function (main, options) {
      this.main = main;
      this.options = options;
    },
    toString: function () {
      return "[F" + this.main + this.options.mkString("") + "]";
    }
  });
  AST.Modifier.Shape.Frame.Radius = MathJax.Object.Subclass({
    Init: function (vector) {
      this.vector = vector;
    },
    toString: function () {
      return ":" + this.vector;
    }
  });
  // <color_name> ::= /[a-zA-Z][a-zA-Z0-9]*/
  AST.Modifier.Shape.Frame.Color = MathJax.Object.Subclass({
    Init: function (colorName) {
      this.colorName = colorName;
    },
    toString: function () {
      return ":" + this.colorName;
    }
  });
  
  // <modifier> ::= 'i'
  AST.Modifier.Invisible = AST.Modifier.Subclass({
    toString: function () { return "i"; }
  });
  
  // <modifier> ::= 'h'
  AST.Modifier.Hidden = AST.Modifier.Subclass({
    toString: function () { return "h"; }
  });
  
  // <modifier> ::= <nonempty-direction>
  AST.Modifier.Direction = AST.Modifier.Subclass({
    Init: function (direction) {
      this.direction = direction;
    },
    toString: function () { return this.direction.toString(); }
  });
  
  // <direction>
  AST.Direction = MathJax.Object.Subclass({});
  // <direction> ::= <direction0> <direction1>*
  AST.Direction.Compound = MathJax.Object.Subclass({
    Init: function (dir, rots) {
      this.dir = dir;
      this.rots = rots;
    },
    toString: function () {
      return this.dir.toString() + this.rots.mkString();
    }
  });
  // <direction0> ::= <diag>
  AST.Direction.Diag = MathJax.Object.Subclass({
    Init: function (diag) {
      this.diag = diag;
    },
    toString: function () { return this.diag.toString(); }
  });
  // <direction0> ::= 'v' <vector>
  AST.Direction.Vector = MathJax.Object.Subclass({
    Init: function (vector) {
      this.vector = vector;
    },
    toString: function () { return "v" + this.vector.toString(); }
  });
  // <direction0> ::= 'q' '{' <pos> <decor> '}'
  AST.Direction.ConstructVector = MathJax.Object.Subclass({
    Init: function (posDecor) {
      this.posDecor = posDecor;
    },
    toString: function () { return "q{" + this.posDecor.toString() + "}"; }
  });
  // <direction1> ::= ':' <vector>
  AST.Direction.RotVector = MathJax.Object.Subclass({
    Init: function (vector) {
      this.vector = vector;
    },
    toString: function () { return ":" + this.vector.toString(); }
  });
  // <direction1> ::= '_'
  AST.Direction.RotAntiCW = MathJax.Object.Subclass({
    toString: function () { return "_"; }
  });
  // <direction1> ::= '^'
  AST.Direction.RotCW = MathJax.Object.Subclass({
    toString: function () { return "^"; }
  });
  
  // <diag>
  AST.Diag = MathJax.Object.Subclass({});
  // <diag> ::= <empty>
  AST.Diag.Default = MathJax.Object.Subclass({
    toString: function () { return ""; }
  });
  // <diag> ::= 'l' | 'r' | 'd' | 'u' | 'ld' | 'rd' | 'lu' | 'ru'
  AST.Diag.Angle = MathJax.Object.Subclass({
    toString: function () { return this.symbol; }
  });
  AST.Diag.LD = AST.Diag.Angle.Subclass({
    symbol: 'ld',
    ang: -3*Math.PI/4,
    turn: function (orient) {
      return (orient === "^"? AST.Diag.RD() : AST.Diag.LU());
    }
  });
  AST.Diag.RD = AST.Diag.Angle.Subclass({
    symbol: 'rd',
    ang: -Math.PI/4,
    turn: function (orient) {
      return (orient === "^"? AST.Diag.RU() : AST.Diag.LD());
    }
  });
  AST.Diag.LU = AST.Diag.Angle.Subclass({
    symbol: 'lu',
    ang: 3*Math.PI/4,
    turn: function (orient) {
      return (orient === "^"? AST.Diag.LD() : AST.Diag.RU());
    }
  });
  AST.Diag.RU = AST.Diag.Angle.Subclass({
    symbol: 'ru',
    ang: Math.PI/4,
    turn: function (orient) {
      return (orient === "^"? AST.Diag.LU() : AST.Diag.RD());
    }
  });
  AST.Diag.L = AST.Diag.Angle.Subclass({
    symbol: 'l',
    ang: Math.PI,
    turn: function (orient) {
      return (orient === "^"? AST.Diag.D() : AST.Diag.U());
    }
  });
  AST.Diag.R = AST.Diag.Angle.Subclass({
    symbol: 'r',
    ang: 0,
    turn: function (orient) {
      return (orient === "^"? AST.Diag.U() : AST.Diag.D());
    }
  });
  AST.Diag.D = AST.Diag.Angle.Subclass({
    symbol: 'd',
    ang: -Math.PI/2,
    turn: function (orient) {
      return (orient === "^"? AST.Diag.R() : AST.Diag.L());
    }
  });
  AST.Diag.U = AST.Diag.Angle.Subclass({
    symbol: 'u',
    ang: Math.PI/2,
    turn: function (orient) {
      return (orient === "^"? AST.Diag.L() : AST.Diag.R());
    }
  });
  
  // <objectbox> ::= '\frm' <frame_radius> '{' <frame_main> '}'
  // <frame_radius> ::= <frame_radius_vector>
  //          | <empty>
  // <frame_main> ::= ( '-' | '=' | '.' | ',' | 'o' | 'e' | '*' )*
  //          | ( '_' | '^' )? ( '\{' | '\}' | '(' | ')' )
  // <frame_radius_vector> ::= '<' <dimen> ',' <dimen> '>'
  //          |   '<' <dimen> '>'
  AST.ObjectBox.Frame = AST.ObjectBox.Subclass({
    Init: function (radius, main) {
      this.radius = radius;
      this.main = main;
    },
    toString: function () {
      return "\\frm"+this.radius+"{"+this.main+"}";
    }
  });
  AST.ObjectBox.Frame.Radius = MathJax.Object.Subclass({});
  AST.ObjectBox.Frame.Radius.Vector = MathJax.Object.Subclass({
    Init: function (vector) {
      this.vector = vector;
    },
    toString: function () { return this.vector.toString(); }
  });
  AST.ObjectBox.Frame.Radius.Default = MathJax.Object.Subclass({
    toString: function () { return ""; }
  });
  
  // <decor> ::= <command>*
  AST.Decor = MathJax.Object.Subclass({
    Init: function (commands) {
      this.commands = commands;
    },
    toString: function () {
      return this.commands.mkString(" ");
    }
  });
  
  AST.Command = MathJax.Object.Subclass({});
  // <command> ::= '\save' <pos>
  AST.Command.Save = MathJax.Object.Subclass({
    Init: function (pos) {
      this.pos = pos;
    },
    toString: function () {
      return "\\save " + this.pos;
    }
  });
  // <command> ::= '\restore'
  AST.Command.Restore = MathJax.Object.Subclass({
    toString: function () {
      return "\\restore";
    }
  });
  // <command> ::= '\POS' <pos>
  AST.Command.Pos = MathJax.Object.Subclass({
    Init: function (pos) {
      this.pos = pos;
    },
    toString: function () {
      return "\\POS " + this.pos;
    }
  });
  // <command> ::= '\afterPOS' '{' <decor> '}' <pos>
  AST.Command.AfterPos = MathJax.Object.Subclass({
    Init: function (decor, pos) {
      this.decor = decor;
      this.pos = pos;
    },
    toString: function () {
      return "\\afterPOS{" + this.decor + "} " + this.pos;
    }
  });
  // <command> ::= '\drop' <object>
  AST.Command.Drop = MathJax.Object.Subclass({
    Init: function (object) {
      this.object = object;
    },
    toString: function () {
      return "\\drop " + this.object;
    }
  });
  // <command> ::= '\connect' <object>
  AST.Command.Connect = MathJax.Object.Subclass({
    Init: function (object) {
      this.object = object;
    },
    toString: function () {
      return "\\connect " + this.object;
    }
  });
  // <command> ::= '\relax'
  AST.Command.Relax = MathJax.Object.Subclass({
    toString: function () {
      return "\\relax";
    }
  });
  // <command> ::= '\xyignore' '{' <pos> <decor> '}'
  AST.Command.Ignore = MathJax.Object.Subclass({
    Init: function (pos, decor) {
      this.pos = pos;
      this.decor = decor;
    },
    toString: function () {
      return "\\ignore{" + this.pos + " " + this.decor + "}";
    }
  });
  // <command> ::= '\xyshowAST' '{' <pos> <decor> '}'
  AST.Command.ShowAST = MathJax.Object.Subclass({
    Init: function (pos, decor) {
      this.pos = pos;
      this.decor = decor;
    },
    toString: function () {
      return "\\xyshowAST{" + this.pos + " " + this.decor + "}";
    }
  });
  
  // <command> ::= '\PATH' <path>
  AST.Command.Path = MathJax.Object.Subclass({
    Init: function (path) {
      this.path = path;
    },
    toString: function () {
      return "\\PATH " + this.path;
    }
  });
  // <command> ::= '\afterPATH' '{' <decor> '}' <path>
  AST.Command.AfterPath = MathJax.Object.Subclass({
    Init: function (decor, path) {
      this.decor = decor;
      this.path = path;
    },
    toString: function () {
      return "\\afterPATH{" + this.decor + "} " + this.path;
    }
  });
  
  // <path> ::= <path2>(Nil)
  AST.Command.Path.Path = MathJax.Object.Subclass({
    Init: function (pathElements) {
      this.pathElements = pathElements;
    },
    toString: function () {
      return this.pathElements.mkString("[", ", ", "]");
    }
  });
  // <path2> ::= '~' <action> '{' <pos> <decor> '}' <path2>(fc)
  // <action> ::= '=' | '/'
  AST.Command.Path.SetBeforeAction = MathJax.Object.Subclass({
    Init: function (posDecor) {
      this.posDecor = posDecor;
    },
    toString: function () {
      return "~={" + this.posDecor + "}";
    }
  });
  AST.Command.Path.SetAfterAction = MathJax.Object.Subclass({
    Init: function (posDecor) {
      this.posDecor = posDecor;
    },
    toString: function () {
      return "~/{" + this.posDecor + "}";
    }
  });
  // <path2> ::= '~' <which> '{' <labels> '}' <path2>(fc)
  // <which> ::= '<' | '>' | '+'
  AST.Command.Path.AddLabelNextSegmentOnly = MathJax.Object.Subclass({
    Init: function (labels) {
      this.labels = labels;
    },
    toString: function () {
      return "~<{" + this.labels + "}";
    }
  });
  AST.Command.Path.AddLabelLastSegmentOnly = MathJax.Object.Subclass({
    Init: function (labels) {
      this.labels = labels;
    },
    toString: function () {
      return "~>{" + this.labels + "}";
    }
  });
  AST.Command.Path.AddLabelEverySegment = MathJax.Object.Subclass({
    Init: function (labels) {
      this.labels = labels;
    },
    toString: function () {
      return "~+{" + this.labels + "}";
    }
  });
  // <path2> ::= "'" <segment> <path2>(fc)
  AST.Command.Path.StraightSegment = MathJax.Object.Subclass({
    Init: function (segment) {
      this.segment = segment;
    },
    toString: function () {
      return "'" + this.segment;
    }
  });
  // <path2> ::= '`' <turn> <segment> <path2>(fc)
  AST.Command.Path.TurningSegment = MathJax.Object.Subclass({
    Init: function (turn, segment) {
      this.turn = turn;
      this.segment = segment;
    },
    toString: function () {
      return "`" + this.turn + " " + this.segment;
    }
  });
  // <path2> ::= <segment>
  AST.Command.Path.LastSegment = MathJax.Object.Subclass({
    Init: function (segment) {
      this.segment = segment;
    },
    toString: function () {
      return this.segment.toString();
    }
  });
  
  // <turn> ::= <diag> <turn-radius>
  AST.Command.Path.Turn = MathJax.Object.Subclass({});
  AST.Command.Path.Turn.Diag = MathJax.Object.Subclass({
    Init: function (diag, radius) {
      this.diag = diag;
      this.radius = radius;
    },
    toString: function () {
      return this.diag.toString() + " " + this.radius;
    }
  });
  // <turn> ::= <cir> <turnradius>
  AST.Command.Path.Turn.Cir = MathJax.Object.Subclass({
    Init: function (cir, radius) {
      this.cir = cir;
      this.radius = radius;
    },
    toString: function () {
      return this.cir.toString() + " " + this.radius;
    }
  });
  // <turn-radius> ::= <empty> | '/' <dimen>
  AST.Command.Path.TurnRadius = MathJax.Object.Subclass({});
  AST.Command.Path.TurnRadius.Default = MathJax.Object.Subclass({
    toString: function () {
      return "";
    }
  });
  AST.Command.Path.TurnRadius.Dimen = MathJax.Object.Subclass({
    Init: function (dimen) {
      this.dimen = dimen;
    },
    toString: function () {
      return "/" + this.dimen;
    }
  });
  
  // <segment> ::= <nonempty-pos> <slide> <labels>
  AST.Command.Path.Segment = MathJax.Object.Subclass({
    Init: function (pos, slide, labels) {
      this.pos = pos;
      this.slide = slide;
      this.labels = labels;
    },
    toString: function () {
      return this.pos.toString() + " " + this.slide + " " + this.labels;
    }
  });
  
  // <labels> ::= <label>*
  AST.Command.Path.Labels = MathJax.Object.Subclass({
    Init: function (labels) {
      this.labels = labels;
    },
    toString: function () {
      return this.labels.mkString(" ");
    }
  });
  // <label> ::= '^' <anchor> <it> <alias>?
  // <anchor> ::= '-' | <place>
  // <it> ::= ( '[' <shape> ']' )* <it2>
  // <it2> ::= <digit> | <letter>
  //       |   '{' <text> '}'
  //       |   '*' <object>
  //       |   '@' <dir>
  AST.Command.Path.Label = MathJax.Object.Subclass({
    Init: function (anchor, it, aliasOption) {
      this.anchor = anchor;
      this.it = it;
      this.aliasOption = aliasOption;
    }
  });
  AST.Command.Path.Label.Above = AST.Command.Path.Label.Subclass({
    toString: function () {
      return "^(" + this.anchor + " " + this.it + " " + this.aliasOption + ")";
    }
  });
  // <label> ::= '_' <anchor> <it> <alias>?
  AST.Command.Path.Label.Below = AST.Command.Path.Label.Subclass({
    toString: function () {
      return "_(" + this.anchor + " " + this.it + " " + this.aliasOption + ")";
    }
  });
  // <label> ::= '|' <anchor> <it> <alias>?
  AST.Command.Path.Label.At = AST.Command.Path.Label.Subclass({
    toString: function () {
      return "|(" + this.anchor + " " + this.it + " " + this.aliasOption + ")";
    }
  });
  
  // <command> ::= '\ar' ( <arrow_form> )* <path>
  AST.Command.Ar = MathJax.Object.Subclass({
    Init: function (forms, path) {
      this.forms = forms;
      this.path = path;
    },
    toString: function () {
      return "\\ar " + this.forms.mkString(" ") + " " + this.path;
    }
  });
  
  // <arrow_form>
  AST.Command.Ar.Form = MathJax.Object.Subclass({});
  // <arrow_form> ::= '@' <variant> ( '{' <tip> ( <conn> <tip> )? '}' )?
  // <variant> ::= /[^_0123]/ | <empty>
  AST.Command.Ar.Form.BuildArrow = AST.Command.Ar.Form.Subclass({
    /**
     * @param {String} variant variant
     * @param {AST.Command.Ar.Form.Tip.*} tailTip arrow tail
     * @param {AST.Command.Ar.Form.Conn.*} stemConn arrow stem
     * @param {AST.Command.Ar.Form.Tip.*} headTip arrow head
     */
    Init: function (variant, tailTip, stemConn, headTip) {
      this.variant = variant;
      this.tailTip = tailTip;
      this.stemConn = stemConn;
      this.headTip = headTip;
    },
    toString: function () {
      return "@" + this.variant + "{" + this.tailTip.toString() + ", " + this.stemConn.toString() + ", " + this.headTip.toString() + "}";
    }
  });
  // <arrow_form> ::= '@' <variant>
  AST.Command.Ar.Form.ChangeVariant = AST.Command.Ar.Form.Subclass({
    /**
     * @param {String} variant variant
     */
    Init: function (variant) {
      this.variant = variant;
    },
    toString: function () {
      return "@" + this.variant;
    }
  });
  // <tip> ::= /[<>()|'`+/a-zA-Z ]+/
  //         | <arrow_dir>
  //         | <empty>
  // <arrow_dir> ::= '*' <object>
  //               | <dir>
  AST.Command.Ar.Form.Tip = MathJax.Object.Subclass({});
  AST.Command.Ar.Form.Tip.Tipchars = MathJax.Object.Subclass({
    /**
     * @param {String} tipchars tip characters
     */
    Init: function (tipchars) {
      this.tipchars = tipchars;
    },
    toString: function () {
      return this.tipchars;
    }
  });
  AST.Command.Ar.Form.Tip.Object = MathJax.Object.Subclass({
    /**
     * @param {AST.Object} object object as a dir
     */
    Init: function (object) {
      this.object = object;
    },
    toString: function () {
      return "*" + this.object;
    }
  });
  AST.Command.Ar.Form.Tip.Dir = MathJax.Object.Subclass({
    /**
     * @param {AST.ObjectBox.Dir} dir dir
     */
    Init: function (dir) {
      this.dir = dir;
    },
    toString: function () {
      return this.dir;
    }
  });
  
  // <conn> ::= /[\-\.~=:]+/
  //          | <arrow_dir>
  //          | <empty>
  AST.Command.Ar.Form.Conn = MathJax.Object.Subclass({});
  AST.Command.Ar.Form.Conn.Connchars = MathJax.Object.Subclass({
    /**
     * @param {String} connchars direction name
     */
    Init: function (connchars) {
      this.connchars = connchars;
    },
    toString: function () {
      return this.connchars;
    }
  });
  AST.Command.Ar.Form.Conn.Object = MathJax.Object.Subclass({
    /**
     * @param {AST.Object} object object as a dir
     */
    Init: function (object) {
      this.object = object;
    },
    toString: function () {
      return "*" + this.object;
    }
  });
  AST.Command.Ar.Form.Conn.Dir = MathJax.Object.Subclass({
    /**
     * @param {AST.ObjectBox.Dir} dir dir
     */
    Init: function (dir) {
      this.dir = dir;
    },
    toString: function () {
      return this.dir;
    }
  });
  
  // <arrow_form> ::= '@' <conchar>
  // <conchar> ::= /[\-\.~=:]/
  AST.Command.Ar.Form.ChangeStem = MathJax.Object.Subclass({
    /**
     * @param {String} connchar arrow stem name
     */
    Init: function (connchar) {
      this.connchar = connchar;
    },
    toString: function () {
      return "@" + this.connchar;
    }
  });
  
  // <arrow_form> ::= '@' '!'
  AST.Command.Ar.Form.DashArrowStem = MathJax.Object.Subclass({
    toString: function () {
      return "@!";
    }
  });
  
  // <arrow_form> ::= '@' '/' <direction> ( <loose-dimen> )? '/'
  AST.Command.Ar.Form.CurveArrow = MathJax.Object.Subclass({
    /**
     * @param {AST.Direction.*} curve direction 
     * @param {String} dist curve distance (dimension)
     */
    Init: function (direction, dist) {
      this.direction = direction;
      this.dist = dist;
    },
    toString: function () {
      return "@/" + this.direction + " " + this.dist + "/";
    }
  });
  
  // <arrow_form> ::= '@' '(' <direction> ',' <direction> ')'
  AST.Command.Ar.Form.CurveFitToDirection = MathJax.Object.Subclass({
    /**
     * @param {AST.Direction.*} out direction 
     * @param {AST.Direction.*} in direction 
     */
    Init: function (outDirection, inDirection) {
      this.outDirection = outDirection;
      this.inDirection = inDirection;
    },
    toString: function () {
      return "@(" + this.outDirection + "," + this.inDirection + ")";
    }
  });
  
  // <arrow_form> ::= '@' '`' <coord>
  AST.Command.Ar.Form.CurveWithControlPoints = MathJax.Object.Subclass({
    /**
     * @param {AST.Coord} controlPoints
     */
    Init: function (coord) {
      this.coord = coord;
    },
    toString: function () {
      return "@`{" + this.coord + "}"
    }
  });
  
  // <arrow_form> ::= '@' '[' <shape> ']'
  AST.Command.Ar.Form.AddShape = MathJax.Object.Subclass({
    /**
     * @param {AST.Modifier.Shape.*} shape shape
     */
    Init: function (shape) {
      this.shape = shape;
    },
    toString: function () {
      return "@[" + this.shape + "]";
    }
  });
  
  // <arrow_form> ::= '@' '*' '{' ( <modifier> )* '}'
  AST.Command.Ar.Form.AddModifiers = MathJax.Object.Subclass({
    /**
     * @param {List[AST.Modifier.*]} modifiers modifiers
     */
    Init: function (modifiers) {
      this.modifiers = modifiers;
    },
    toString: function () {
      return "@*{" + this.modifiers.mkString(" ") + "}";
    }
  });
  
  // <arrow_form> ::= '@' '<' <dimen> '>'
  AST.Command.Ar.Form.Slide = MathJax.Object.Subclass({
    /**
     * @param {String} slide dimension
     */
    Init: function (slideDimen) {
      this.slideDimen = slideDimen;
    },
    toString: function () {
      return "@<" + this.slideDimen + ">";
    }
  });
  
  // <arrow_form> ::= '|' <anchor> <it>
  AST.Command.Ar.Form.LabelAt = MathJax.Object.Subclass({
    /**
     * @param {AST.Place} anchor label anchor
     * @param {AST.Object} it label
     */
    Init: function (anchor, it) {
      this.anchor = anchor;
      this.it = it;
    },
    toString: function () {
      return "|" + this.anchor + " " + this.it;
    }
  });
  
  // <arrow_form> ::= '^' <anchor> <it>
  AST.Command.Ar.Form.LabelAbove = MathJax.Object.Subclass({
    /**
     * @param {AST.Place} anchor label anchor
     * @param {AST.Object} it label
     */
    Init: function (anchor, it) {
      this.anchor = anchor;
      this.it = it;
    },
    toString: function () {
      return "^" + this.anchor + " " + this.it;
    }
  });
  
  // <arrow_form> ::= '_' <anchor> <it>
  AST.Command.Ar.Form.LabelBelow = MathJax.Object.Subclass({
    /**
     * @param {AST.Place} anchor label anchor
     * @param {AST.Object} it label
     */
    Init: function (anchor, it) {
      this.anchor = anchor;
      this.it = it;
    },
    toString: function () {
      return "_" + this.anchor + " " + this.it;
    }
  });
  
  // <arrow_form> ::= '@' '?'
  AST.Command.Ar.Form.ReverseAboveAndBelow = MathJax.Object.Subclass({
    toString: function () {
      return "@?";
    }
  });
  
  
  // <decor> ::= '\xymatrix' <xymatrix>
  // <xymatrix> ::= <setup> '{' <rows> '}'
  AST.Command.Xymatrix = MathJax.Object.Subclass({
    /**
     * @param {List[AST.Command.Xymatrix.Setup.*]} setup setup configurations
     * @param {List[AST.Command.Xymatrix.Row]} rows rows
     */
    Init: function (setup, rows) {
      this.setup = setup;
      this.rows = rows;
    },
    toString: function () {
      return "\\xymatrix" + this.setup + "{\n" + this.rows.mkString("", "\\\\\n", "") + "\n}";
    }
  });
  // <setup> ::= <switch>*
  AST.Command.Xymatrix.Setup = MathJax.Object.Subclass({});
  
  // <switch> ::= '"' <prefix> '"'
  AST.Command.Xymatrix.Setup.Prefix = MathJax.Object.Subclass({
    /**
     * @param {String} prefix name of the xymatrix
     */
    Init: function (prefix) {
      this.prefix = prefix;
    },
    toString: function () {
      return '"' + this.prefix + '"';
    }
  });
  
  // <switch> ::= '@' <rcchar> <add op> <dimen>
  AST.Command.Xymatrix.Setup.ChangeSpacing = MathJax.Object.Subclass({
    /**
     * @param {AST.Modifier.AddOp.*} addop sizing operator
     * @param {String} dimen size
     */
    Init: function (addop, dimen) {
      this.addop = addop;
      this.dimen = dimen;
    }
  });
  AST.Command.Xymatrix.Setup.ChangeSpacing.Row = AST.Command.Xymatrix.Setup.ChangeSpacing.Subclass({
    toString: function () {
      return "@R" + this.addop + this.dimen;
    }
  });
  AST.Command.Xymatrix.Setup.ChangeSpacing.Column = AST.Command.Xymatrix.Setup.ChangeSpacing.Subclass({
    toString: function () {
      return "@C" + this.addop + this.dimen;
    }
  });
  AST.Command.Xymatrix.Setup.ChangeSpacing.RowAndColumn = AST.Command.Xymatrix.Setup.ChangeSpacing.Subclass({
    toString: function () {
      return "@" + this.addop + this.dimen;
    }
  });
  
  // <switch> ::= '@' '!' <rcchar> '0'
  // <switch> ::= '@' '!' <rcchar> '=' <dimen>
  // <rcchar> ::= 'R' | 'C' | <empty>
  AST.Command.Xymatrix.Setup.PretendEntrySize = MathJax.Object.Subclass({
    /**
     * @param {String} dimen size
     */
    Init: function (dimen) {
      this.dimen = dimen;
    }
  });
  AST.Command.Xymatrix.Setup.PretendEntrySize.Height = AST.Command.Xymatrix.Setup.PretendEntrySize.Subclass({
    toString: function () {
      return "@!R=" + this.dimen;
    }
  });
  AST.Command.Xymatrix.Setup.PretendEntrySize.Width = AST.Command.Xymatrix.Setup.PretendEntrySize.Subclass({
    toString: function () {
      return "@!C=" + this.dimen;
    }
  });
  AST.Command.Xymatrix.Setup.PretendEntrySize.HeightAndWidth = AST.Command.Xymatrix.Setup.PretendEntrySize.Subclass({
    toString: function () {
      return "@!=" + this.dimen;
    }
  });
  
  // <switch> ::= '@' '!' <rcchar>
  AST.Command.Xymatrix.Setup.FixGrid = MathJax.Object.Subclass({});
  AST.Command.Xymatrix.Setup.FixGrid.Row = AST.Command.Xymatrix.Setup.FixGrid.Subclass({
    toString: function () {
      return "@!R";
    }
  });
  AST.Command.Xymatrix.Setup.FixGrid.Column = AST.Command.Xymatrix.Setup.FixGrid.Subclass({
    toString: function () {
      return "@!C";
    }
  });
  AST.Command.Xymatrix.Setup.FixGrid.RowAndColumn = AST.Command.Xymatrix.Setup.FixGrid.Subclass({
    toString: function () {
      return "@!";
    }
  });
  
  // <switch> ::= '@' ( 'M' | 'W' | 'H' ) <add op> <dimen>
  // <switch> ::= '@' '1'
  AST.Command.Xymatrix.Setup.AdjustEntrySize = MathJax.Object.Subclass({
    /**
     * @param {AST.Modifier.AddOp.*} addop sizing operator
     * @param {String} dimen size
     */
    Init: function (addop, dimen) {
      this.addop = addop;
      this.dimen = dimen;
    }
  });
  AST.Command.Xymatrix.Setup.AdjustEntrySize.Margin = AST.Command.Xymatrix.Setup.AdjustEntrySize.Subclass({
    toString: function () {
      return "@M" + this.addop + this.dimen;
    }
  });
  AST.Command.Xymatrix.Setup.AdjustEntrySize.Width = AST.Command.Xymatrix.Setup.AdjustEntrySize.Subclass({
    toString: function () {
      return "@W" + this.addop + this.dimen;
    }
  });
  AST.Command.Xymatrix.Setup.AdjustEntrySize.Height = AST.Command.Xymatrix.Setup.AdjustEntrySize.Subclass({
    toString: function () {
      return "@H" + this.addop + this.dimen;
    }
  });
  
  // <switch> ::= '@' 'L' <add op> <dimen>
  AST.Command.Xymatrix.Setup.AdjustLabelSep = MathJax.Object.Subclass({
    /**
     * @param {AST.Modifier.AddOp.*} addop sizing operator
     * @param {String} dimen size
     */
    Init: function (addop, dimen) {
      this.addop = addop;
      this.dimen = dimen;
    },
    toString: function () {
      return "@L" + this.addop + this.dimen;
    }
  });
  
  // <switch> ::= '@' <nonemptyDirection>
  AST.Command.Xymatrix.Setup.SetOrientation = MathJax.Object.Subclass({
    /**
     * @param {AST.Direction} direction the orientation of the row
     */
    Init: function (direction) {
      this.direction = direction;
    },
    toString: function () {
      return "@" + this.direction;
    }
  });
  
  // <switch> ::= '@' '*' '[' <shape> ']'
  //          |   '@' '*' <add op> <size>
  AST.Command.Xymatrix.Setup.AddModifier = MathJax.Object.Subclass({
    /**
     * @param {AST.Modifier.*} shape  object shape modifier for all entries
     */
    Init: function (modifier) {
      this.modifier = modifier;
    },
    toString: function () {
      return "@*" + this.modifier;
    }
  });
  
  // <rows> ::= <row> ( '\\' <row> )*
  // <row> ::= <entry> ( '&' <entry> )*
  AST.Command.Xymatrix.Row = MathJax.Object.Subclass({
    /**
     * @param {List[AST.Command.Xymatrix.Entry.*]} entries entries in the row
     */
    Init: function (entries) {
      this.entries = entries;
    },
    toString: function () {
      return this.entries.mkString(" & ");
    }
  });
  // <entry> ::= ( '**' '[' <shape> ']' | '**' '{' <modifier>* '}' )* <loose objectbox> <decor>
  //         |   '*' <object> <pos> <decor>
  // <loose objectbox> ::= <objectbox>
  //                   |   /[^\\{}&]+/* ( ( '\' not( '\' | <decor command names> ) ( '{' | '}' | '&' ) | '{' <text> '}' ) /[^\\{}&]+/* )*
  // <decor command names> ::= 'ar' | 'xymatrix' | 'PATH' | 'afterPATH'
  //                       |   'save' | 'restore' | 'POS' | 'afterPOS' | 'drop' | 'connect' | 'xyignore'
  AST.Command.Xymatrix.Entry = MathJax.Object.Subclass({});
  AST.Command.Xymatrix.Entry.SimpleEntry = AST.Command.Xymatrix.Entry.Subclass({
    /**
     * @param {List[AST.Modifier.*]} modifiers object modifiers
     * @param {AST.ObjectBox.*} objectbox entry objectbox
     * @param {AST.Decor} decor decoration
     */
    Init: function (modifiers, objectbox, decor) {
      this.modifiers = modifiers;
      this.objectbox = objectbox;
      this.decor = decor;
    },
    isEmpty: false,
    toString: function () {
      return this.modifiers.mkString("**{", "", "}") + " " + this.objectbox + " " + this.decor;
    }
  });
  AST.Command.Xymatrix.Entry.ObjectEntry = AST.Command.Xymatrix.Entry.Subclass({
    /**
     * @param {AST.Object} object entry object
     * @param {AST.Pos.Coord} pos position (ignorable)
     * @param {AST.Decor} decor decoration
     */
    Init: function (object, pos, decor) {
      this.object = object;
      this.pos = pos;
      this.decor = decor;
    },
    isEmpty: false,
    toString: function () {
      return "*" + this.object + " " + this.pos + " " + this.decor;
    }
  });
  AST.Command.Xymatrix.Entry.EmptyEntry = AST.Command.Xymatrix.Entry.Subclass({
    /**
     * @param {AST.Decor} decor decoration
     */
    Init: function (decor) {
      this.decor = decor;
    },
    isEmpty: true,
    toString: function () {
      return "" + this.decor;
    }
  });
  
  // <command> ::= <twocell> <twocell switch>* <twocell arrow>
  AST.Command.Twocell = MathJax.Object.Subclass({
    /**
     * @param {AST.Command.Twocell.Hops2cell} twocell 2-cell
     * @param {List[AST.Command.Twocell.Switch.*]} switches switches
     * @param {AST.Command.Twocell.Arrow.*} arrow
     */
    Init: function (twocell, switches, arrow) {
      this.twocell = twocell;
      this.switches = switches;
      this.arrow = arrow;
    },
    toString: function () {
      return this.twocell.toString() + this.switches.mkString("") + this.arrow;
    }
  });
  // <twocell> ::= '\' /[lrud]+/ 'twocell'
  //           |   '\xtwocell' '[' /[lrud]+/ ']' '{' <text> '}'
  AST.Command.Twocell.Hops2cell = MathJax.Object.Subclass({
    /**
     * @param {String} hops hops
     * @param {Option[AST.Object]} maybeDisplace displacement
     */
    Init: function (hops, maybeDisplace) {
      this.hops = hops;
      this.maybeDisplace = maybeDisplace;
    }
  });
  AST.Command.Twocell.Twocell = AST.Command.Twocell.Hops2cell.Subclass({
    toString: function () {
      return "\\xtwocell[" + this.hops + "]" + this.maybeDisplace.getOrElse("{}");
    }
  });
  //           |   '\' /[lrud]+/ 'uppertwocell'
  //           |   '\xuppertwocell' '[' /[lrud]+/ ']' '{' <text> '}'
  AST.Command.Twocell.UpperTwocell = AST.Command.Twocell.Hops2cell.Subclass({
    toString: function () {
      return "\\xuppertwocell[" + this.hops + "]" + this.maybeDisplace.getOrElse("{}");
    }
  });
  //           |   '\' /[lrud]+/ 'lowertwocell'
  //           |   '\xlowertwocell' '[' /[lrud]+/ ']' '{' <text> '}'
  AST.Command.Twocell.LowerTwocell = AST.Command.Twocell.Hops2cell.Subclass({
    toString: function () {
      return "\\xlowertwocell[" + this.hops + "]" + this.maybeDisplace.getOrElse("{}");
    }
  });
  //           |   '\' /[lrud]+/ 'compositemap'
  //           |   '\xcompositemap' '[' /[lrud]+/ ']' '{' <text> '}'
  AST.Command.Twocell.CompositeMap = AST.Command.Twocell.Hops2cell.Subclass({
    toString: function () {
      return "\\xcompositemap[" + this.hops + "]" + this.maybeDisplace.getOrElse("{}");
    }
  });
  
  // <twocell switch> ::= '^' <twocell label>
  AST.Command.Twocell.Switch = MathJax.Object.Subclass({});
  AST.Command.Twocell.Switch.UpperLabel = MathJax.Object.Subclass({
    /**
     * @param {AST.Command.Twocell.Label} label label
     */
    Init: function (label) {
      this.label = label;
    },
    toString: function () {
      return "^" + this.label;
    }
  });
  //          |   '_' <twocell label>
  AST.Command.Twocell.Switch.LowerLabel = MathJax.Object.Subclass({
    /**
     * @param {AST.Command.Twocell.Label} label label
     */
    Init: function (label) {
      this.label = label;
    },
    toString: function () {
      return "_" + this.label;
    }
  });
  //          |   <nudge>
  AST.Command.Twocell.Switch.SetCurvature = MathJax.Object.Subclass({
    /**
     * @param {AST.Command.Twocell.Nudge.*} nudge
     */
    Init: function (nudge) {
      this.nudge = nudge;
    },
    toString: function () {
      return this.nudge.toString();
    }
  });
  //          |   '\omit'
  AST.Command.Twocell.Switch.DoNotSetCurvedArrows = MathJax.Object.Subclass({
    toString: function () {
      return "\\omit";
    }
  });
  //          |   '~!'
  AST.Command.Twocell.Switch.PlaceModMapObject = MathJax.Object.Subclass({
    toString: function () {
      return "~!";
    }
  });
  
  //          |   '~' ( '`' | "'" ) '{' <object> '}'
  AST.Command.Twocell.Switch.ChangeHeadTailObject = MathJax.Object.Subclass({
    /**
     * @param {String} what
     * @param {AST.Object} object
     */
    Init: function (what, object) {
      this.what = what;
      this.object = object;
    },
    toString: function () {
      return "~" + this.what + "{" + this.object + "}";
    }
  });
  
  //          |   '~' ( '' | '^' | '_' ) '{' <object> ( '~**' <object> )? '}'
  AST.Command.Twocell.Switch.ChangeCurveObject = MathJax.Object.Subclass({
    /**
     * @param {String} what
     * @param {AST.Object} spacer
     * @param {AST.Object} maybeObject
     */
    Init: function (what, spacer, maybeObject) {
      this.what = what;
      this.spacer = spacer;
      this.maybeObject = maybeObject;
    },
    toString: function () {
      return "~" + this.what + "{" + this.spacer + (this.maybeObject.isDefined? "~**" + this.maybeObject.get : "") + "}";
    }
  });
  
  // <twocell label> ::= <digit> | <letter> | <cs>
  //                 |   '{' <nudge>? '*' <object> '}'
  //                 |   '{' <nudge>? <text> '}'
  AST.Command.Twocell.Label = MathJax.Object.Subclass({
    /**
     * @param {Option[AST.Command.Twocell.Nudge.*]} maybeNudge
     * @param {AST.Object} labelObject
     */
    Init: function (maybeNudge, labelObject) {
      this.maybeNudge = maybeNudge;
      this.labelObject = labelObject;
    },
    toString: function () {
      return this.maybeNudge.toString() + this.labelObject;
    }
  });
  
  // <nudge> ::= '<' <factor> '>'
  //         |   '<\omit>'
  AST.Command.Twocell.Nudge = MathJax.Object.Subclass({});
  AST.Command.Twocell.Nudge.Number = AST.Command.Twocell.Nudge.Subclass({
    /**
     * @param {Number} number number
     */
    Init: function (number) {
      this.number = number;
    },
    toString: function () {
      return "<" + this.number + ">";
    }
  });
  AST.Command.Twocell.Nudge.Omit = AST.Command.Twocell.Nudge.Subclass({
    toString: function () {
      return "<\\omit>";
    }
  });
  
  // <twocell arrow> ::= '{' <twocell tok> (<twocell label entry> '}'
  //                 |   '{' <twocell label entry> '}'
  //                 |   <empty>
  // <twocell tok> ::= '^' | '_' | '='
  //               |   '\omit'
  //               |   '`' | "'" | '"' | '!'
  // <twocell label entry> ::= '*' <object>
  //                       |   <text>
  AST.Command.Twocell.Arrow = MathJax.Object.Subclass({});
  AST.Command.Twocell.Arrow.WithOrientation = AST.Command.Twocell.Arrow.Subclass({
    /**
     * @param {String} tok
     * @param {AST.Object} labelObject
     */
    Init: function (tok, labelObject) {
      this.tok = tok;
      this.labelObject = labelObject;
    },
    toString: function () {
      return "{[" + this.tok + "] " + this.labelObject + "}";
    }
  });
  //                 |   '{' <nudge> <twocell label entry> '}'
  AST.Command.Twocell.Arrow.WithPosition = AST.Command.Twocell.Arrow.Subclass({
    /**
     * @param {AST.Command.Twocell.Nudge.*} nudge
     * @param {AST.Object} labelObject
     */
    Init: function (nudge, labelObject) {
      this.nudge = nudge;
      this.labelObject = labelObject;
    },
    toString: function () {
      return "{[" + this.nudge + "] " + this.labelObject + "}";
    }
  });
  
  // '\newdir' '{' <main> '}' '{' <composite_object> '}'
  AST.Command.Newdir = MathJax.Object.Subclass({
    /**
     * @param {String} dirMain
     * @param {AST.ObjectBox.CompositeObject} compositeObject
     */
    Init: function (dirMain, compositeObject) {
      this.dirMain = dirMain;
      this.compositeObject = compositeObject;
    },
    toString: function () {
      return "\\newdir{" + this.dirMain + "}{" + this.compositeObject + "}";
    }
  });
  
  // '\xyimport' '(' <factor> ',' <factor> ')' ( '(' <factor> ',' <factor> ')' )? '{' <TeX command> '}'
  AST.Pos.Xyimport = MathJax.Object.Subclass({});
  AST.Pos.Xyimport.TeXCommand = AST.Pos.Xyimport.Subclass({
    /**
     * @param {Number} width the width of the graphics in the coordinate system
     * @param {Number} height the height of the graphics in the coordinate system
     * @param {Number} xOffset the distance of the origin of coordinates from left corner
     * @param {Number} yOffset the distance of the origin of coordinates from bottom corner
     * @param {AST.Command.*} graphics object
     */
    Init: function (width, height, xOffset, yOffset, graphics) {
      this.width = width;
      this.height = height;
      this.xOffset = xOffset;
      this.yOffset = yOffset;
      this.graphics = graphics;
    },
    toString: function () {
      return "\\xyimport(" + this.width + ", " + this.height + ")(" + this.xOffset + ", " + this.yOffset + "){" + this.graphics + "}";
    }
  });
  
  // '\xyimport' '(' <factor> ',' <factor> ')' ( '(' <factor> ',' <factor> ')' )? '{' <include graphics> '}'
  AST.Pos.Xyimport.Graphics = AST.Pos.Xyimport.Subclass({
    /**
     * @param {Number} width the width of the graphics in the coordinate system
     * @param {Number} height the height of the graphics in the coordinate system
     * @param {Number} xOffset the distance of the origin of coordinates from left corner
     * @param {Number} yOffset the distance of the origin of coordinates from bottom corner
     * @param {AST.Command.Includegraphics} graphics object
     */
    Init: function (width, height, xOffset, yOffset, graphics) {
      this.width = width;
      this.height = height;
      this.xOffset = xOffset;
      this.yOffset = yOffset;
      this.graphics = graphics;
    },
    toString: function () {
      return "\\xyimport(" + this.width + ", " + this.height + ")(" + this.xOffset + ", " + this.yOffset + "){" + this.graphics + "}";
    }
  });
  
  /* \includegraphics command from the graphicx package */
  // '\includegraphics' '*'? '[' ( <includegraphics attr key val> ( ',' <includegraphics attr key val> )* )? ']' '{' <file path> '}'
  AST.Command.Includegraphics = MathJax.Object.Subclass({
    /**
     * @param {boolean} isClipped whether the graphics is clipped to the size specified or not
     * @param {List[AST.Command.Includegraphics.Attr]} attributeList attribute key-value list
     * @param {String} filepath image file path
     */
    Init: function (isClipped, attributeList, filepath) {
      this.isClipped = isClipped;
      this.attributeList = attributeList;
      this.filepath = filepath;
    },
    isIncludegraphics: true,
    toString: function () {
      return "\\includegraphics" + (this.isClipped? "*" : "") + this.attributeList.mkString("[", ",", "]") + "{" + this.filepath + "}";
    }
  });
  
  // TODO: define <includegraphics attr key val>
  // <includegraphics attr key val> := 'width' '=' <dimen>
  //                                |  'height' '=' <dimen>
  AST.Command.Includegraphics.Attr = MathJax.Object.Subclass({});
  AST.Command.Includegraphics.Attr.Width = AST.Command.Includegraphics.Attr.Subclass({
    /**
     * @param {String} dimen 
     */
    Init: function (dimen) {
      this.dimen = dimen;
    },
    toString: function () {
      return "width=" + this.dimen;
    }
  });
  AST.Command.Includegraphics.Attr.Height = AST.Command.Includegraphics.Attr.Subclass({
    /**
     * @param {String} dimen 
     */
    Init: function (dimen) {
      this.dimen = dimen;
    },
    toString: function () {
      return "height=" + this.dimen;
    }
  });
  
  var fun = FP.Parsers.fun;
  var elem = FP.Parsers.elem;
  var felem = function (x) { return fun(FP.Parsers.elem(x)); }
  var lit = FP.Parsers.literal;
  var regex = FP.Parsers.regex;
  var regexLit = FP.Parsers.regexLiteral;
  var flit = function (x) { return fun(FP.Parsers.literal(x)); }
  var seq = FP.Parsers.seq;
  var or = FP.Parsers.or;
  var rep = function (x) { return FP.Parsers.lazyParser(x)().rep(); }
  var rep1 = function (x) { return FP.Parsers.lazyParser(x)().rep1(); }
  var opt = function (x) { return FP.Parsers.lazyParser(x)().opt(); }
  var not = function (x) { return FP.Parsers.not(FP.Parsers.lazyParser(x)); }
  var success = FP.Parsers.success;
  var memo = function (parser) {
    return function () {
      var m = parser.memo;
      if (m === undefined) {
        m = parser.memo = parser();
      }
      return m;
    }
  }
  
  var p = FP.Parsers.Subclass({
    // <pos-decor> '\end' '{' 'xy' '}'
    xy: memo(function () {
      return p.posDecor().into(function (pd) {
        return FP.Parsers.guard(function() { return lit('\\end').andl(flit('{')).andl(flit('xy')).andl(flit('}')).to(function () {
          return pd;
        })});
      });
    }),
    
    // \xyboxの後の
    // '{' <pos-decor> '}'
    xybox: memo(function () {
      return lit("{").andr(p.posDecor).andl(flit("}")).to(function (pd) {
        return pd;
      });
    }),
    
    // \xymatrixの後の
    // <xymatrix>
    xymatrixbox: memo(function () {
      return p.xymatrix().to(function (m) {
        return AST.PosDecor(AST.Pos.Coord(AST.Coord.C(), FP.List.empty), AST.Decor(FP.List.empty.append(m)));
      });
    }),
    
    // <pos-decor> ::= <pos> <decor>
    posDecor: memo(function () {
      return seq(p.pos, p.decor).to(function (pd) {
        return AST.PosDecor(pd.head, pd.tail);
      });
    }),
    
    // <pos> ::= <coord> <pos2>*
    pos: memo(function () {
      return seq(p.coord, rep(p.pos2)).to(function (cps) {
        return AST.Pos.Coord(cps.head, cps.tail);
      });
    }),
    
    // <nonemptyPos> ::= <coord> <pos2>*
    nonemptyPos: memo(function () {
      return or(
        seq(p.nonemptyCoord, rep(p.pos2)),
        seq(p.coord, rep1(p.pos2))
      ).to(function (cps) {
        return AST.Pos.Coord(cps.head, cps.tail);
      });
    }),
    
    // <pos2> ::= '+' <coord>
    //        |   '-' <coord>
    //        |   '!' <coord>
    //        |   '.' <coord>
    //        |   ',' <coord>
    //        |   ';' <coord>
    //        |   '::' <coord>
    //        |   ':' <coord>
    //        |   '**' <object>
    //        |   '*' <object>
    //        |   '?' <place>
    //        |   '@+' <corrd>
    //        |   '@-' <corrd>
    //        |   '@=' <corrd>
    //        |   '@@' <corrd>
    //        |   '@i'
    //        |   '@('
    //        |   '@)'
    //        |   '=:' '"' <id> '"'
    //        |   '=@' '"' <id> '"'
    //        |   '=' '"' <id> '"'
    //        |   '=' <nonemptyCoord> '"' <id> '"'
    //        |   <xyimport>
    pos2: memo(function () {
      return or(
        lit('+').andr(p.coord).to(function (c) { return AST.Pos.Plus(c); }),
        lit('-').andr(p.coord).to(function (c) { return AST.Pos.Minus(c); }),
        lit('!').andr(p.coord).to(function (c) { return AST.Pos.Skew(c); }),
        lit('.').andr(p.coord).to(function (c) { return AST.Pos.Cover(c); }),
        lit(',').andr(p.coord).to(function (c) { return AST.Pos.Then(c); }),
        lit(';').andr(p.coord).to(function (c) { return AST.Pos.SwapPAndC(c); }),
        lit('::').andr(p.coord).to(function (c) { return AST.Pos.SetYBase(c); }),
        lit(':').andr(p.coord).to(function (c) { return AST.Pos.SetBase(c); }),
        lit('**').andr(p.object).to(function (o) { return AST.Pos.ConnectObject(o); }),
        lit('*').andr(p.object).to(function (o) { return AST.Pos.DropObject(o); }),
        lit('?').andr(p.place).to(function (o) { return AST.Pos.Place(o); }),
        lit('@+').andr(p.coord).to(function (c) { return AST.Pos.PushCoord(c); }),
        lit('@-').andr(p.coord).to(function (c) { return AST.Pos.EvalCoordThenPop(c); }),
        lit('@=').andr(p.coord).to(function (c) { return AST.Pos.LoadStack(c); }),
        lit('@@').andr(p.coord).to(function (c) { return AST.Pos.DoCoord(c); }),
        lit('@i').to(function () { return AST.Pos.InitStack(); }),
        lit('@(').to(function () { return AST.Pos.EnterFrame(); }),
        lit('@)').to(function () { return AST.Pos.LeaveFrame(); }),
        lit('=:').andr(flit('"')).andr(p.id).andl(felem('"')).to(function (id) { return AST.Pos.SaveBase(id); }),
        lit('=@').andr(flit('"')).andr(p.id).andl(felem('"')).to(function (id) { return AST.Pos.SaveStack(id); }),
        lit('=').andr(flit('"')).andr(p.id).andl(felem('"')).to(function (id) { return AST.Pos.SavePos(id); }),
        lit('=').andr(p.nonemptyCoord).andl(flit('"')).and(p.id).andl(felem('"')).to(function (mid) { return AST.Pos.SaveMacro(mid.head, mid.tail); }),
        p.xyimport
      );
    }),
    
    // <coord> ::= <nonemptyCoord> | <empty>
    coord: memo(function () {
      return or(
        p.nonemptyCoord,
        success('empty').to(function () { return AST.Coord.C(); })
      );
    }),
    
    // <nonemptyCoord> ::= 'c' | 'p' | 'x' | 'y'
    //                 |   <vector>
    //                 |   '"' <id> '"'
    //                 |   '{' <pos> <decor> '}'
    //                 |   's' <digit>
    //                 |   's' '{' <nonnegative-number> '}'
    //                 |   '[' ('"'<prefix>'"')? <number> ',' <number> ']'
    //                 |   '[' ('"'<prefix>'"')? ( 'l' | 'r' | 'u' | 'd' )* ']'
    //                 |   '[' ('"'<prefix>'"')? ( 'l' | 'r' | 'u' | 'd' )+ <place> ']'
    nonemptyCoord: memo(function () {
      return or(
        lit('c').to(function () { return AST.Coord.C(); }), 
        lit('p').to(function () { return AST.Coord.P(); }), 
        lit('x').to(function () { return AST.Coord.X(); }), 
        lit('y').to(function () { return AST.Coord.Y(); }),
        p.vector().to(function (v) { return AST.Coord.Vector(v); }), 
        lit('"').andr(p.id).andl(felem('"')).to(function (id) { return AST.Coord.Id(id) }),
        lit('{').andr(p.posDecor).andl(flit('}')).to(function (pd) { return AST.Coord.Group(pd) }),
        lit('s').andr(fun(regexLit(/^\d/))).to(function (n) {
          return AST.Coord.StackPosition(parseInt(n));
        }),
        lit('s').andr(flit('{')).and(p.nonnegativeNumber).andl(flit('}')).to(function (n) {
          return AST.Coord.StackPosition(n);
        }),
        lit('[').andr(fun(
          opt(lit('"').andr(p.id).andl(felem('"'))).to(function (id) { return id.getOrElse(""); }) )
        ).and(p.number).andl(flit(",")).and(p.number).andl(flit("]")).to(function (prc) {
          return AST.Coord.DeltaRowColumn(prc.head.head, prc.head.tail, prc.tail);
        }),
        lit('[').andr(fun(
          opt(lit('"').andr(p.id).andl(felem('"'))).to(function (id) { return id.getOrElse(""); }) )
        ).and(fun(rep(regex(/^[lrud]/)))).andl(flit("]")).to(function (ph) {
          return AST.Coord.Hops(ph.head, ph.tail);
        }),
        lit('[').andr(fun(
          opt(lit('"').andr(p.id).andl(felem('"'))).to(function (id) { return id.getOrElse(""); }) )
        ).and(fun(rep1(regex(/^[lrud]/)))).and(p.place).andl(flit("]")).to(function (php) {
          return AST.Coord.DeltaRowColumn(php.head.head, php.head.tail, AST.Pos.Place(php.tail));
        })
      );
    }),
    
    // <vector> ::= '(' <factor> ',' <factor> ')'
    //          |   '<' <dimen> ',' <dimen> '>'
    //          |   '<' <dimen> '>'
    //          |   'a' '(' <number> ')'
    //          |   '/' <direction> <loose-dimen> '/'
    //          |   0
    //          |   <corner>
    //          |   <corner> '(' <factor> ')'
    vector: memo(function () {
      return or(
        lit('(').andr(p.factor).andl(flit(',')).and(p.factor).andl(flit(')')).to(
          function (xy) {
            return AST.Vector.InCurBase(xy.head, xy.tail);
          }
        ),
        lit('<').andr(p.dimen).andl(flit(',')).and(p.dimen).andl(flit('>')).to(
          function (xy) {
            return AST.Vector.Abs(xy.head, xy.tail);
          }
        ),
        lit('<').andr(p.dimen).andl(flit('>')).to(
          function (x) {
            return AST.Vector.Abs(x, x);
          }
        ),
        lit('a').andr(flit('(')).andr(p.number).andl(flit(')')).to(
          function (d) {
            return AST.Vector.Angle(d);
          }
        ),
        lit('/').andr(p.direction).and(p.looseDimen).andl(flit('/')).to(
          function (dd) {
            return AST.Vector.Dir(dd.head, dd.tail);
          }
        ),
        lit('0').to(function (x) { return AST.Vector.Abs("0mm", "0mm"); }),
        function () { return p.corner().and(fun(FP.Parsers.opt(
          fun(lit('(').andr(p.factor).andl(flit(')')))).to(function (f) {
            return f.getOrElse(1);
          }))).to(function (cf) {
            return AST.Vector.Corner(cf.head, cf.tail);
          })
        }
      );
    }),
    
    // <corner> ::= 'L' | 'R' | 'D' | 'U'
    //          | 'CL' | 'CR' | 'CD' | 'CU' | 'LC' | 'RC' | 'DC' | 'UC'
    //          | 'LD' | 'RD' | 'LU' | 'RU' | 'DL' | 'DR' | 'UL' | 'UR'
    //          | 'E' | 'P'
    //          | 'A'
    corner: memo(function () {
      return or(
        regexLit(/^(CL|LC)/).to(function () { return AST.Corner.CL(); }),
        regexLit(/^(CR|RC)/).to(function () { return AST.Corner.CR(); }),
        regexLit(/^(CD|DC)/).to(function () { return AST.Corner.CD(); }),
        regexLit(/^(CU|UC)/).to(function () { return AST.Corner.CU(); }),
        regexLit(/^(LD|DL)/).to(function () { return AST.Corner.LD(); }),
        regexLit(/^(RD|DR)/).to(function () { return AST.Corner.RD(); }),
        regexLit(/^(LU|UL)/).to(function () { return AST.Corner.LU(); }),
        regexLit(/^(RU|UR)/).to(function () { return AST.Corner.RU(); }),
        lit('L').to(function () { return AST.Corner.L(); }),
        lit('R').to(function () { return AST.Corner.R(); }),
        lit('D').to(function () { return AST.Corner.D(); }),
        lit('U').to(function () { return AST.Corner.U(); }),
        lit('E').to(function () { return AST.Corner.NearestEdgePoint(); }),
        lit('P').to(function () { return AST.Corner.PropEdgePoint(); }),
        lit('A').to(function () { return AST.Corner.Axis(); })
      );
    }),
    
    // <place> ::= '<' <place>
    //         | '>' <place>
    //         | '(' <factor> ')' <place>
    //         | '!' '{' <pos> '}' <slide>
    //         | <slide>
    place: memo(function () {
      return or(
        lit('<').andr(p.place).to(function (pl) {
          return AST.Place(1, 0, undefined, undefined).compound(pl);
        }), 
        lit('>').andr(p.place).to(function (pl) {
          return AST.Place(0, 1, undefined, undefined).compound(pl);
        }), 
        lit('(').andr(p.factor).andl(flit(')')).and(p.place).to(function (pl) {
          return AST.Place(0, 0, AST.Place.Factor(pl.head), undefined).compound(pl.tail);
        }), 
        lit('!').andr(flit('{')).andr(p.pos).andl(flit('}')).and(p.slide).to(function (ps) {
          return AST.Place(0, 0, AST.Place.Intercept(ps.head), ps.tail);
        }),
        function () { return p.slide().to(function (s) {
          return AST.Place(0, 0, undefined, s);
        }) }
      );
    }),
    
    // <slide> ::= '/' <dimen> '/'
    //         | <empty>
    slide: memo(function () {
      return or(
        lit('/').andr(p.dimen).andl(flit('/')).to(function (d) {
          return AST.Slide(FP.Option.Some(d));
        }),
        success("no slide").to(function () {
          return AST.Slide(FP.Option.empty);
        })
      );
    }),
    
    // <factor>
    factor: memo(fun(regexLit(/^[+\-]?(\d+(\.\d*)?|\d*\.\d+)/).to(
      function (v) { return parseFloat(v); })
    )),
    
    // <number>
    number: memo(fun(regexLit(/^[+\-]?\d+/).to(
      function (n) { return parseInt(n); })
    )),
    
    // <nonnegative-number>
    nonnegativeNumber: memo(fun(regexLit(/^\d+/).to(
      function (n) { return parseInt(n); })
    )),
    
    unit: memo(fun(regexLit(/^(em|ex|px|pt|pc|in|cm|mm|mu)/).to(function (d) {
        return d
    }))),
    
    // <dimen> ::= <factor> ( 'em' | 'ex' | 'px' | 'pt' | 'pc' | 'in' | 'cm' | 'mm' | 'mu' )
    dimen: memo(function () {
      return p.factor().and(p.unit).to(function (x) {
        return x.head.toString() + x.tail;
      })
    }),
    
    // <loose-dimen> ::= <loose-factor> ( 'em' | 'ex' | 'px' | 'pt' | 'pc' | 'in' | 'cm' | 'mm' | 'mu' )
    looseDimen: memo(function () {
      return p.looseFactor().and(p.unit).to(function (x) {
        return x.head.toString() + x.tail;
      })
    }),
    
    // <loose-factor>
    // makeshift against /^ 3.5mm/ converted to /^ 3 .5mm/ by MathJax.InputJax.TeX.prefilterMath()
    looseFactor: memo(fun(or(
      regexLit(/^(\d \d*(\.\d*))/).to(function (v) {
        return parseFloat(v.replace(/ /, ""));
      }),
      regexLit(/^[+\-]?(\d+(\.\d*)?|\d*\.\d+)/).to(function (v) {
        return parseFloat(v);
      })
    ))),
    
    // <id>
    id: memo(fun(regex(/^[^"]+/))), // "
    
    // <object> ::= <modifier>* <objectbox>
    object: memo(function () {
      return or(
        rep(p.modifier).and(p.objectbox).to(function (mso) {
          return AST.Object(mso.head, mso.tail);
        })
      );
    }),
    
    // <objectbox> ::= '{' <text> '}'
    //          | '@' <dir>
    //          | '\dir' <dir>
    //          | '\cir' <cir_radius> '{' <cir> '}'
    //          | '\frm' <frame_radius> '{' <frame_main> '}'
    //          | '\object' <object>
    //          | '\composite' '{' <composite_object> '}'
    //          | '\xybox' '{' <pos> <decor> '}'
    //          | '\xymatrix' <xymatrix>
    //          | <curve>
    //          | <TeX box> '{' <text> '}'
    objectbox: memo(function () {
      return or(
        p.mathText,
        lit("@").andr(p.dir),
        lit("\\dir").andr(p.dir),
        lit("\\cir").andr(p.cirRadius).andl(flit("{")).and(p.cir).andl(flit("}")).to(function (rc) {
          return AST.ObjectBox.Cir(rc.head, rc.tail);
        }),
        lit("\\frm").andr(p.frameRadius).andl(flit("{")).and(p.frameMain).andl(flit("}")).to(function (rm) {
          return AST.ObjectBox.Frame(rm.head, rm.tail);
        }),
        lit("\\object").andr(p.object).to(function (o) {
          return AST.ObjectBox.WrapUpObject(o);
        }),
        lit("\\composite").and(flit("{")).andr(p.compositeObject).andl(flit("}")).to(function (os) {
          return AST.ObjectBox.CompositeObject(os);
        }),
        lit("\\xybox").and(flit("{")).andr(p.posDecor).andl(flit("}")).to(function (pd) {
          return AST.ObjectBox.Xybox(pd);
        }),
        lit("\\xymatrix").andr(p.xymatrix).to(function (m) {
          return AST.ObjectBox.Xymatrix(m);
        }),
        p.txt,
        p.curve,
        regex(/^(\\[a-zA-Z@][a-zA-Z0-9@]+)/).andl(flit("{")).and(p.text).andl(flit("}")).to(function (bt) {
          return p.toMath(bt.head + "{" + bt.tail + "}");
        })
      );
    }),
    
    // <composite_object> ::= <object> ( '*' <object> )*
    compositeObject: memo(function () {
      return p.object().and(fun(rep(lit("*").andr(p.object)))).to(function (oos) {
        return oos.tail.prepend(oos.head);
      });
    }),
    
    // <math-text> ::= '{' <text> '}'
    mathText: memo(function () {
      return lit("{").andr(p.text).andl(felem("}")).to(function (text) {
        return p.toMath("\\hbox{$\\objectstyle{" + text + "}$}");
      });
    }),
    toMath: function (math) {
      var mml = TEX.Parse(math).mml();
      if (mml.inferred) {
        mml = MML.apply(MathJax.ElementJax, mml.data);
      } else {
        mml = MML(mml);
      }
      TEX.combineRelations(mml.root);
      return AST.ObjectBox.Text(mml.root);
    },
    
    // <text> ::= /[^{}\\%]*/ (( '\{' | '\}' | '\%' | '\\' | '{' <text> '}' | /%[^\r\n]*(\r\n|\r|\n)?/ ) /[^{}\\%]*/ )*
    text: memo(function () {
      return regex(/^[^{}\\%]*/).and(function () {
        return (
          or(
            regex(/^(\\\{|\\\}|\\%|\\)/).to(function (x) {
              return x;
            }),
            elem("{").andr(p.text).andl(felem("}")).to(function (x) {
              return "{" + x + "}";
            }),
            regex(/^%[^\r\n]*(\r\n|\r|\n)?/).to(function (x) {
              return ' '; // ignore comments
            })
          ).and(fun(regex(/^[^{}\\%]*/)))).rep().to(function (xs) {
            var res = "";
            xs.foreach(function (x) {
              res += x.head + x.tail;
            });
            return res;
        })
      }).to(function (x) {
        return x.head + x.tail
      });
    }),
    
    txt: memo(function () {
      return lit("\\txt").andr(p.txtWidth).and(fun(regex(/^(\\[a-zA-Z@][a-zA-Z0-9@]+)?/))).andl(flit("{")).and(p.text).andl(flit("}")).to(function (wst) {
          var width = wst.head.head;
          var style = wst.head.tail;
          var text = wst.tail;
          var math;
          var lines = text.split("\\\\");
          if (lines.length <= 1) {
            math = style + "{\\hbox{" + text + "}}";
          } else {
            math = "\\hbox{$\\begin{array}{c}\n";
            for (var i = 0; i < lines.length; i++) {
              math += style + "{\\hbox{" + lines[i].replace(/(^[\r\n\s]+)|([\r\n\s]+$)/g, "") + "}}";
              if (i != lines.length - 1) {
                math += "\\\\\n";
              }
            }
            math += "\\end{array}$}";
          }
          return AST.ObjectBox.Txt(width, p.toMath(math));
        });
    }),
    
    // <txt_width> ::= '<' <dimen> '>'
    //          | <empty>
    txtWidth: memo(function () {
      return or(
        lit('<').andr(p.dimen).andl(flit('>')).to(
          function (x) {
            return AST.Vector.Abs(x, x);
          }
        ).to(function (v) {
          return AST.ObjectBox.Txt.Width.Vector(v);
        }),
        success("default").to(function () {
          return AST.ObjectBox.Txt.Width.Default();
        })
      );
    }),
    
    // <dir> ::= <variant> '{' <main> '}'
    // <variant> ::= '^' | '_' | '0' | '1' | '2' | '3' | <empty>
    dir: memo(function () {
      return regexLit(/^[\^_0123]/).opt().andl(flit('{')).and(p.dirMain).andl(flit('}')).to(function (vm) {
        return AST.ObjectBox.Dir(vm.head.getOrElse(""), vm.tail);
      })
    }),
    
    // <main> ::= ('-' | '.' | '~' | '>' | '<' | '(' | ')' | '`' | "'" | '|' | '*' | '+' | 'x' | '/' | 'o' | '=' | ':' | /[a-zA-Z@ ]/)*
    dirMain: memo(function () {
      return regex(/^(-|\.|~|>|<|\(|\)|`|'|\||\*|\+|x|\/|o|=|:|[a-zA-Z@ ])+/ /*'*/).opt().to(function (m) {
        return m.getOrElse("");
      })
    }),
    
    // <cir_radius> ::= <vector>
    //          | <empty>
    cirRadius: memo(function () {
      return or(
        p.vector().to(function (v) {
          return AST.ObjectBox.Cir.Radius.Vector(v);
        }),
        success("default").to(function () {
          return AST.ObjectBox.Cir.Radius.Default();
        })
      );
    }),
    
    // <frame_radius> ::= <frame_radius_vector>
    //          | <empty>
    frameRadius: memo(function () {
      return or(
        p.frameRadiusVector().to(function (v) {
          return AST.ObjectBox.Frame.Radius.Vector(v);
        }),
        success("default").to(function () {
          return AST.ObjectBox.Frame.Radius.Default();
        })
      );
    }),

    // <frame_radius_vector> ::= '<' <dimen> ',' <dimen> '>'
    //          |   '<' <dimen> '>'
    frameRadiusVector: memo(function () {
      return or(
        lit('<').andr(p.dimen).andl(flit(',')).and(p.dimen).andl(flit('>')).to(
          function (xy) {
            return AST.Vector.Abs(xy.head, xy.tail);
          }
        ),
        lit('<').andr(p.dimen).andl(flit('>')).to(
          function (x) {
            return AST.Vector.Abs(x, x);
          }
        )
      );
    }),
    
    // <frame_main> ::= ( '-' | '=' | '.' | ',' | 'o' | 'e' | '*' )*
    //          | ( '_' | '^' )? ( '\{' | '\}' | '(' | ')' )
    frameMain: memo(function () {
      return regex(/^(((_|\^)?(\\\{|\\\}|\(|\)))|[\-=oe,\.\*]*)/);
    }),
    
    // <cir> ::= <diag> <orient> <diag>
    //       | <empty>
    cir: memo(function () {
      return or(
        p.nonemptyCir,
        success("full").to(function () {
          return AST.ObjectBox.Cir.Cir.Full();
        })
      );
    }),
    nonemptyCir: memo(function () {
      return p.diag().and(fun(regexLit(/^[_\^]/))).and(p.diag).to(function (dod) {
        return AST.ObjectBox.Cir.Cir.Segment(dod.head.head, dod.head.tail, dod.tail);
      });
    }),
    
    // <curve> ::= '\crv' <curve-modifier> '{' <curve-object> <curve-poslist> '}'
    curve: memo(function () {
      return lit("\\crv").andr(p.curveModifier).andl(flit("{")).and(p.curveObject).and(p.curvePoslist).andl(flit("}")).to(function (mop) {
        return AST.ObjectBox.Curve(mop.head.head, mop.head.tail, mop.tail);
      });
    }),
    
    // <curve-modifier> ::= ( '~' <curve-option> )*
    curveModifier: memo(function () {
      return rep(fun(lit("~").andr(p.curveOption)));
    }),
    
    // <curve-option> ::= 'p' | 'P' | 'l' | 'L' | 'c' | 'C'
    //                |   'pc' | 'pC' | 'Pc' | 'PC'
    //                |   'lc' | 'lC' | 'Lc' | 'LC'
    //                |   'cC'
    curveOption: memo(function () {
      return or(
        lit("p").to(function () { return AST.ObjectBox.Curve.Modifier.p(); }),
        lit("P").to(function () { return AST.ObjectBox.Curve.Modifier.P(); }),
        lit("l").to(function () { return AST.ObjectBox.Curve.Modifier.l(); }),
        lit("L").to(function () { return AST.ObjectBox.Curve.Modifier.L(); }),
        lit("c").to(function () { return AST.ObjectBox.Curve.Modifier.c(); }),
        lit("C").to(function () { return AST.ObjectBox.Curve.Modifier.C(); }),
        lit("pc").to(function () { return AST.ObjectBox.Curve.Modifier.pc(); }),
        lit("pC").to(function () { return AST.ObjectBox.Curve.Modifier.pC(); }),
        lit("Pc").to(function () { return AST.ObjectBox.Curve.Modifier.Pc(); }),
        lit("PC").to(function () { return AST.ObjectBox.Curve.Modifier.PC(); }),
        lit("lc").to(function () { return AST.ObjectBox.Curve.Modifier.lc(); }),
        lit("lC").to(function () { return AST.ObjectBox.Curve.Modifier.lC(); }),
        lit("Lc").to(function () { return AST.ObjectBox.Curve.Modifier.Lc(); }),
        lit("LC").to(function () { return AST.ObjectBox.Curve.Modifier.LC(); }),
        lit("cC").to(function () { return AST.ObjectBox.Curve.Modifier.cC(); })
      );
    }),
    
    // <curve-object> ::= <empty>
    //                |   '~*' <object> <curve-object>
    //                |   '~**' <object> <curve-object>
    curveObject: memo(function () {
      return rep(or(
        lit("~*").andr(p.object).to(function (obj) {
          return AST.ObjectBox.Curve.Object.Drop(obj);
        }),
        lit("~**").andr(p.object).to(function (obj) {
          return AST.ObjectBox.Curve.Object.Connect(obj);
        })
      ));
    }),
    
    // <curve-poslist> ::= <empty> ^^ Empty List
    //           |   '&' <curve-poslist2> ^^ (c, <poslist>)
    //           |   <nonemptyPos> ^^ (<nonemptyPos>, Nil)
    //           |   <nonemptyPos> '&' <curve-poslist2> ^^ (<nonemptyPos>, <poslist>)
    //           |   '~@' ^^ (~@, Nil)
    //           |   '~@' '&' <curve-poslist2> ^^ (~@, <poslist>)
    // <curve-poslist2> ::= <empty> ^^ (c, Nil)
    //           |   '&' <curve-poslist2> ^^ (c, <poslist>)
    //           |   <nonemptyPos> ^^ (<nonemptyPos>, Nil)
    //           |   <nonemptyPos> '&' <curve-poslist2> ^^ (<nonemptyPos>, <poslist>)
    //           |   '~@' ^^ (~@, Nil)
    //           |   '~@' '&' <curve-poslist2> ^^ (~@, <poslist>)
    curvePoslist: memo(function () {
      return or(
        lit("&").andr(p.curvePoslist2).to(function (ps) {
          return ps.prepend(AST.ObjectBox.Curve.PosList.CurPos());
        }),
        lit("~@").andr(flit("&")).andr(p.curvePoslist2).to(function (ps) {
          return ps.prepend(AST.ObjectBox.Curve.PosList.AddStack());
        }),
        lit("~@").to(function () {
          return FP.List.empty.prepend(AST.ObjectBox.Curve.PosList.AddStack());
        }),
        p.pos().andl(flit("&")).and(p.curvePoslist2).to(function (pps) {
          return pps.tail.prepend(AST.ObjectBox.Curve.PosList.Pos(pps.head));
        }),
        p.nonemptyPos().to(function (p) {
          return FP.List.empty.prepend(AST.ObjectBox.Curve.PosList.Pos(p));
        }),
        success("empty").to(function () {
          return FP.List.empty;
        })
      );
    }),
    curvePoslist2: memo(function () {
      return or(
        lit("&").andr(p.curvePoslist2).to(function (ps) {
          return ps.prepend(AST.ObjectBox.Curve.PosList.CurPos());
        }),
        lit("~@").andr(flit("&")).andr(p.curvePoslist2).to(function (ps) {
          return ps.prepend(AST.ObjectBox.Curve.PosList.AddStack());
        }),
        lit("~@").to(function () {
          return FP.List.empty.prepend(AST.ObjectBox.Curve.PosList.AddStack());
        }),
        p.nonemptyPos().andl(flit("&")).and(p.curvePoslist2).to(function (pps) {
          return pps.tail.prepend(AST.ObjectBox.Curve.PosList.Pos(pps.head));
        }),
        p.nonemptyPos().to(function (p) {
          return FP.List.empty.prepend(AST.ObjectBox.Curve.PosList.Pos(p));
        }),
        success("empty").to(function () {
          return FP.List.empty.prepend(AST.ObjectBox.Curve.PosList.CurPos());
        })
      );
    }),
    
    // <modifier> ::= '!' <vector>
    //            |   '[' <shape> ']'
    //            |   'i'
    //            |   'h'
    //            |   <add-op> <size>
    //            |   <nonemptyDirection>
    modifier: memo(function () {
      return or(
        lit("!").andr(p.vector).to(function (v) {
          return AST.Modifier.Vector(v);
        }),
        lit("!").to(function (v) {
          return AST.Modifier.RestoreOriginalRefPoint();
        }),
        lit("[").andr(p.shape).andl(flit("]")).to(function (s) {
          return s;
        }),
        lit("i").to(function (v) {
          return AST.Modifier.Invisible();
        }),
        lit("h").to(function (v) {
          return AST.Modifier.Hidden();
        }),
        p.addOp().and(p.size).to(function (os) {
          return AST.Modifier.AddOp(os.head, os.tail);
        }),
        p.nonemptyDirection().to(function (d) {
          return AST.Modifier.Direction(d);
        })
      );
    }),
    
    // <add-op> ::= '+' | '-' | '=' | '+=' | '-='
    addOp: memo(function () {
      return or(
        lit("+=").to(function () { return AST.Modifier.AddOp.GrowTo(); }),
        lit("-=").to(function () { return AST.Modifier.AddOp.ShrinkTo(); }),
        lit("+").to(function () { return AST.Modifier.AddOp.Grow(); }),
        lit("-").to(function () { return AST.Modifier.AddOp.Shrink(); }),
        lit("=").to(function () { return AST.Modifier.AddOp.Set(); })
      );
    }),
    
    // <size> ::= <vector> | <empty>
    size: memo(function () {
      return or(
        function () { return p.vector().to(function (v) {
          return AST.Modifier.AddOp.VactorSize(v);
        }) },
        success("default size").to(function () {
          return AST.Modifier.AddOp.DefaultSize();
        })
      );
    }),
    
    // <shape> ::= '.' 
    //          | <frame_shape>
    //          | <alphabets>
    //          | '=' <alphabets>
    //          | <empty>
    shape: memo(function () {
      return or(
        lit(".").to(function () { return AST.Modifier.Shape.Point(); }),
        p.frameShape,
        p.alphabets().to(function (name) {
          return AST.Modifier.Shape.Alphabets(name);
        }),
        lit("=").andr(p.alphabets).to(function (name) {
          return AST.Modifier.Shape.DefineShape(name);
        }),
        success("rect").to(function () { return AST.Modifier.Shape.Rect(); })
      );
    }),
    
    // <frame_shape> ::= 'F' <frame_main> ( ':' ( <frame_radius_vector> | <color_name> ))*
    frameShape: memo(function () {
      return lit("F").andr(p.frameMain).and(fun(
        rep(lit(":").andr(fun(
          or(
            p.frameRadiusVector().to(function (v) {
              return AST.Modifier.Shape.Frame.Radius(v);
            }),
            p.colorName().to(function (c) {
                return AST.Modifier.Shape.Frame.Color(c);
            })
          )
        )))
      )).to(function (mo) {
        var main = mo.head;
        if (main === "") {
          main = "-";
        }
        return AST.Modifier.Shape.Frame(main, mo.tail);
      });
    }),
    
    // <alphabets> ::= /[a-zA-Z]+/
    alphabets: memo(function () {
      return regex(/^([a-zA-Z]+)/);
    }),
    
    // <color_name> ::= /[a-zA-Z][a-zA-Z0-9]*/
    colorName: memo(function () {
      return regex(/^([a-zA-Z][a-zA-Z0-9]*)/);
    }),
    
    // <direction> ::= <direction0> <direction1>*
    // <direction0> ::= <direction2>
    //              |   <diag>
    // <direction1> | ':' <vector>
    //              | '_'
    //              | '^'
    // <direction2> ::= 'v' <vector>
    //              |   'q' '{' <pos> <decor> '}'
    direction: memo(function () {
      return seq(p.direction0, rep(p.direction1)).to(function (drs){
        return AST.Direction.Compound(drs.head, drs.tail);
      });
    }),
    direction0: memo(function () {
      return or(
        p.direction2,
        p.diag().to(function (d) {
          return AST.Direction.Diag(d);
        })
      );
    }),
    direction1: memo(function () {
      return or(
        lit(':').andr(p.vector).to(function (v) {
          return AST.Direction.RotVector(v);
        }),
        lit('_').to(function (x) {
          return AST.Direction.RotAntiCW();
        }),
        lit('^').to(function (x) {
          return AST.Direction.RotCW();
        })
      );
    }),
    direction2: memo(function () {
      return or(
        lit('v').andr(p.vector).to(function (v) {
          return AST.Direction.Vector(v);
        }),
        lit('q').andr(flit('{')).andr(p.posDecor).andl(flit('}')).to(function (pd) {
          return AST.Direction.ConstructVector(pd);
        })
      );
    }),
    
    // <nonempty-direction> ::= <nonempty-direction0> <direction1>*
    //                      |   <direction0> <direction1>+
    // <nonempty-direction0> ::= <nonempty-diag>
    //                       |   <direction2>
    nonemptyDirection: memo(function () {
      return or(
        seq(p.nonemptyDirection0, rep(p.direction1)),
        seq(p.direction0, rep1(p.direction1))
      ).to(function (drs){
        return AST.Direction.Compound(drs.head, drs.tail);
      });
    }),
    nonemptyDirection0: memo(function () {
      return or(
        p.direction2,
        p.nonemptyDiag().to(function (d) {
          return AST.Direction.Diag(d);
        })
      );
    }),
    
    // <diag> ::= <nonempty-diag> | <empty>
    // <nonempty-diag> ::= 'l' | 'r' | 'd' | 'u' | 'ld' | 'rd' | 'lu' | 'ru'
    diag: memo(function () {
      return or(
        p.nonemptyDiag,
        success("empty").to(function (x) {
          return AST.Diag.Default();
        })
      );
    }),
    nonemptyDiag: memo(function () {
      return or(
        regexLit(/^(ld|dl)/).to(function (x) { return AST.Diag.LD(); }),
        regexLit(/^(rd|dr)/).to(function (x) { return AST.Diag.RD(); }),
        regexLit(/^(lu|ul)/).to(function (x) { return AST.Diag.LU(); }),
        regexLit(/^(ru|ur)/).to(function (x) { return AST.Diag.RU(); }),
        lit('l').to(function (x) { return AST.Diag.L(); }),
        lit('r').to(function (x) { return AST.Diag.R(); }),
        lit('d').to(function (x) { return AST.Diag.D(); }),
        lit('u').to(function (x) { return AST.Diag.U(); })
      );
    }),
    
    // <decor> ::= <command>*
    decor: memo(function () {
      return p.command().rep().to(function (cs) {
        return AST.Decor(cs);
      })
    }),
    
    // <command> ::= '\ar' ( <arrow_form> )* <path>
    //           |   '\xymatrix' <xymatrix>
    //           |   '\PATH' <path>
    //           |   '\afterPATH' '{' <decor> '}' <path>
    //           |   '\save' <pos>
    //           |   '\restore'
    //           |   '\POS' <pos>
    //           |   '\afterPOS' '{' <decor> '}' <pos>
    //           |   '\drop' <object>
    //           |   '\connect' <object>
    //           |   '\relax'
    //           |   '\xyignore' '{' <pos> <decor> '}'
    //           |   <twocell command>
    command: memo(function () {
      return or(
        lit("\\ar").andr(fun(rep(p.arrowForm))).and(p.path).to(function (fsp) {
          return AST.Command.Ar(fsp.head, fsp.tail);
        }),
        lit("\\xymatrix").andr(p.xymatrix),
        lit("\\PATH").andr(p.path).to(function (path) {
          return AST.Command.Path(path);
        }),
        lit("\\afterPATH").andr(flit('{')).andr(p.decor).andl(flit('}')).and(p.path).to(function (dp) {
          return AST.Command.AfterPath(dp.head, dp.tail);
        }),
        lit("\\save").andr(p.pos).to(function (pos) {
          return AST.Command.Save(pos);
        }),
        lit("\\restore").to(function () {
          return AST.Command.Restore();
        }),
        lit("\\POS").andr(p.pos).to(function (pos) {
          return AST.Command.Pos(pos);
        }),
        lit("\\afterPOS").andr(flit('{')).andr(p.decor).andl(flit('}')).and(p.pos).to(function (dp) {
          return AST.Command.AfterPos(dp.head, dp.tail);
        }),
        lit("\\drop").andr(p.object).to(function (obj) {
          return AST.Command.Drop(obj);
        }),
        lit("\\connect").andr(p.object).to(function (obj) {
          return AST.Command.Connect(obj);
        }),
        lit("\\relax").to(function () {
          return AST.Command.Relax();
        }),
        lit("\\xyignore").andr(flit('{')).andr(p.pos).and(p.decor).andl(flit('}')).to(function (pd) {
          return AST.Command.Ignore(pd.head, pd.tail);
        }),
        lit("\\xyshowAST").andr(flit('{')).andr(p.pos).and(p.decor).andl(flit('}')).to(function (pd) {
          return AST.Command.ShowAST(pd.head, pd.tail);
        }),
        p.twocellCommand
      );
    }),
    
    // <arrow_form> ::= '@' <conchar>
    //              |   '@' '!'
    //              |   '@' '/' <direction> ( <loose-dimen> )? '/'
    //              |   '@' '(' <direction> ',' <direction> ')'
    //              |   '@' '`' '{' <curve-poslist> '}'
    //              |   '@' '[' <shape> ']'
    //              |   '@' '*' '{' ( <modifier> )* '}'
    //              |   '@' '<' <dimen> '>'
    //              |   '|' <anchor> <it>
    //              |   '^' <anchor> <it>
    //              |   '_' <anchor> <it>
    //              |   '@' '?'
    //              |   '@' <variant> ( <tip_conn_tip> )?
    // <conchar> ::= /[\-\.~=:]/
    // <variant> ::= /[\^_0123]/ | <empty>
    arrowForm: memo(function () {
      return or(
        lit("@").andr(fun(regex(/^([\-\.~=:])/))).to(function (c) {
          return AST.Command.Ar.Form.ChangeStem(c);
        }),
        lit("@").andr(flit("!")).to(function (c) {
          return AST.Command.Ar.Form.DashArrowStem();
        }),
        lit("@").andr(flit("/")).andr(p.direction).and(fun(opt(p.looseDimen))).andl(flit("/")).to(function (dd) {
          return AST.Command.Ar.Form.CurveArrow(dd.head, dd.tail.getOrElse(".5pc"));
        }),
        lit("@").andr(flit("(")).andr(p.direction).andl(flit(",")).and(p.direction).andl(flit(")")).to(function (dd) {
          return AST.Command.Ar.Form.CurveFitToDirection(dd.head, dd.tail);
        }),
        lit("@").andr(flit("`")).andr(p.coord).to(function (c) {
          return AST.Command.Ar.Form.CurveWithControlPoints(c);
        }),
        lit("@").andr(flit("[")).andr(p.shape).andl(flit("]")).to(function (s) {
          return AST.Command.Ar.Form.AddShape(s);
        }),
        lit("@").andr(flit("*")).andr(flit("{")).andr(fun(rep(p.modifier))).andl(flit("}")).to(function (ms) {
          return AST.Command.Ar.Form.AddModifiers(ms);
        }),
        lit("@").andr(flit("<")).andr(p.dimen).andl(flit(">")).to(function (d) {
          return AST.Command.Ar.Form.Slide(d);
        }),
        lit("|").andr(p.anchor).and(p.it).to(function (ai) {
          return AST.Command.Ar.Form.LabelAt(ai.head, ai.tail);
        }),
        lit("^").andr(p.anchor).and(p.it).to(function (ai) {
          return AST.Command.Ar.Form.LabelAbove(ai.head, ai.tail);
        }),
        lit("_").andr(p.anchor).and(p.it).to(function (ai) {
          return AST.Command.Ar.Form.LabelBelow(ai.head, ai.tail);
        }),
        lit("@").andr(flit("?")).to(function () {
          return AST.Command.Ar.Form.ReverseAboveAndBelow();
        }),
        lit("@").andr(fun(regex(/^([\^_0123])/).opt())).and(fun(opt(p.tipConnTip))).to(function (vtct) {
          var variant = vtct.head.getOrElse("");
          if (vtct.tail.isDefined) {
            var tct = vtct.tail.get;
            return AST.Command.Ar.Form.BuildArrow(variant, tct.tail, tct.stem, tct.head);
          } else {
            return AST.Command.Ar.Form.ChangeVariant(variant);
          }
        })
      );
    }),
    
    // <tip_conn_tip> ::= '{' <nonempty_tip>? <nonempty_conn>? <nonempty_tip>? '}'
    tipConnTip: memo(function () {
      return lit("{").andr(fun(opt(p.nonemptyTip))).and(fun(opt(p.nonemptyConn))).and(fun(opt(p.nonemptyTip))).andl(flit("}")).to(function (pcp) {
        var maybeTail = pcp.head.head;
        var maybeStem = pcp.head.tail;
        var maybeHead = pcp.tail;
        
        var emptyTip = AST.Command.Ar.Form.Tip.Tipchars("");
        var tail, stem, head;
        if (!maybeStem.isDefined && !maybeHead.isDefined) {
          if (!maybeTail.isDefined) {
            tail = emptyTip;
            stem = AST.Command.Ar.Form.Conn.Connchars("");
            head = emptyTip;
          } else {
            tail = emptyTip;
            stem = AST.Command.Ar.Form.Conn.Connchars("-");
            head = maybeTail.getOrElse(emptyTip);
          }
        } else {
          tail = maybeTail.getOrElse(emptyTip);
          stem = maybeStem.getOrElse(AST.Command.Ar.Form.Conn.Connchars(""));
          head = maybeHead.getOrElse(emptyTip);
        }
        return {
          tail:tail,
          stem:stem,
          head:head
        };
      });
    }),
    
    // <nonempty_tip> ::= /[<>()|'`+/a-zA-Z ]+/
    //         | <arrow_dir>
    // <arrow_dir> ::= '*' <object>
    //               | <dir>
    nonemptyTip: memo(function () {
      return or(
        regex(/^([<>()|'`+\/a-zA-Z ]+)/).to(function (cs) {
          return AST.Command.Ar.Form.Tip.Tipchars(cs);
        }),
        lit("*").andr(p.object).to(function (o) {
          return AST.Command.Ar.Form.Tip.Object(o);
        }),
        p.dir().to(function (d) {
          return AST.Command.Ar.Form.Tip.Dir(d);
        })
      );
    }),
    
    // <nonempty_conn> ::= /[\-\.~=:]+/
    //          | <arrow_dir>
    nonemptyConn: memo(function () {
      return or(
        regex(/^([\-\.~=:]+)/).to(function (cs) {
          return AST.Command.Ar.Form.Conn.Connchars(cs);
        }),
        lit("*").andr(p.object).to(function (o) {
          return AST.Command.Ar.Form.Conn.Object(o);
        }),
        p.dir().to(function (d) {
          return AST.Command.Ar.Form.Conn.Dir(d);
        })
      );
    }),
    
    // <path> ::= <path2>(Nil)
    path: memo(function () {
      return p.path2(FP.List.empty /* initial failure continuation */).to(function (ps) {
        return AST.Command.Path.Path(ps);
      })
    }),
    
    // <path2>(fc) ::= '~' <action> '{' <pos> <decor> '}' <path2>(fc)
    //             |   '~' <which> '{' <labels> '}' <path2>(fc)
    //             |   "'" <segment> <path2>(fc)
    //             |   '`' <turn> <segment> <path2>(fc)
    //             |   '~' '{' <path2 as fc'> '}' <path2>(fc')
    //             |   <segment>
    //             |   <empty>
    // <action> ::= '=' | '/'
    // <which> ::= '<' | '>' | '+'
    path2: function (fc) {
      var q = memo(function () { return p.path2(fc) });
      return or(
        p.path3().and(q).to(function (ep) {
          return ep.tail.prepend(ep.head);
        }),
        seq('~', '{', q, '}').to(function (newFc) {
          return newFc.head.tail;
        }).into(function (newFc) {
          return p.path2(newFc);
        }),
        p.segment().to(function (s) {
          return FP.List.empty.prepend(AST.Command.Path.LastSegment(s));
        }),
        success(fc).to(function (fc) {
          return fc;
        })
      );
    },
    path3: memo(function () {
      return or(
        seq('~', '=', '{', p.posDecor, '}').to(function (pd) {
          return AST.Command.Path.SetBeforeAction(pd.head.tail);
        }),
        seq('~', '/', '{', p.posDecor, '}').to(function (pd) {
          return AST.Command.Path.SetAfterAction(pd.head.tail);
        }),
        seq('~', '<', '{', p.labels, '}').to(function (ls) {
          return AST.Command.Path.AddLabelNextSegmentOnly(ls.head.tail);
        }),
        seq('~', '>', '{', p.labels, '}').to(function (ls) {
          return AST.Command.Path.AddLabelLastSegmentOnly(ls.head.tail);
        }),
        seq('~', '+', '{', p.labels, '}').to(function (ls) {
          return AST.Command.Path.AddLabelEverySegment(ls.head.tail);
        }),
        seq("'", p.segment).to(function (s) {
          return AST.Command.Path.StraightSegment(s.tail);
        }),
        seq('`', p.turn, p.segment).to(function (ts) {
          return AST.Command.Path.TurningSegment(ts.head.tail, ts.tail);
        })
      );
    }),
    
    // <turn> ::= <diag> <turn-radius>
    //        |   <cir> <turnradius>
    turn: memo(function () {
      return or(
        p.nonemptyCir().and(p.turnRadius).to(function (cr) {
          return AST.Command.Path.Turn.Cir(cr.head, cr.tail);
        }),
        p.diag().and(p.turnRadius).to(function (dr) {
          return AST.Command.Path.Turn.Diag(dr.head, dr.tail);
        })
      );
    }),
    
    // <turn-radius> ::= <empty> | '/' <dimen>
    turnRadius: memo(function () {
      return or(
        lit('/').andr(p.dimen).to(function (d) {
          return AST.Command.Path.TurnRadius.Dimen(d);
        }),
        success("default").to(function () {
          return AST.Command.Path.TurnRadius.Default();
        })
      );
    }),
    
    // <segment> ::= <nonempty-pos> <slide> <labels>
    segment: memo(function () {
      return p.nonemptyPos().and(p.pathSlide).and(p.labels).to(function (psl) {
        return AST.Command.Path.Segment(psl.head.head, psl.head.tail, psl.tail);
      });
    }),
    
    // <slide> ::= '<' <dimen> '>'
    //         | <empty>
    pathSlide: memo(function () {
      return or(
        lit('<').andr(p.dimen).andl(flit('>')).to(function (d) {
          return AST.Slide(FP.Option.Some(d));
        }),
        success("no slide").to(function () {
          return AST.Slide(FP.Option.empty);
        })
      );
    }),
    
    // <labels> ::= <label>*
    labels: memo(function () {
      return p.label().rep().to(function (ls) {
        return AST.Command.Path.Labels(ls);
      });
    }),
    
    // <label> ::= '^' <anchor> <it> <alias>?
    // <label> ::= '_' <anchor> <it> <alias>?
    // <label> ::= '|' <anchor> <it> <alias>?
    label: memo(function () {
      return or(
        seq('^', p.anchor, p.it, p.alias).to(function (aia) {
          return AST.Command.Path.Label.Above(AST.Pos.Place(aia.head.head.tail), aia.head.tail, aia.tail);
        }),
        seq('_', p.anchor, p.it, p.alias).to(function (aia) {
          return AST.Command.Path.Label.Below(AST.Pos.Place(aia.head.head.tail), aia.head.tail, aia.tail);
        }),
        seq('|', p.anchor, p.it, p.alias).to(function (aia) {
          return AST.Command.Path.Label.At(AST.Pos.Place(aia.head.head.tail), aia.head.tail, aia.tail);
        })
      );
    }),
    
    // <anchor> ::= '-' <anchor> | <place>
    anchor: memo(function () {
      return or(
        lit('-').andr(p.anchor).to(function (a) {
          return AST.Place(1, 1, AST.Place.Factor(0.5), undefined).compound(a);
        }),
        p.place
      );
    }),
    
    // <it> ::= ( '[' <shape> ']' )* <it2>
    it: memo(function () {
      return rep(lit('[').andr(p.shape).andl(flit(']')).to(function (s) {
        return s;
      })).and(p.it2).to(function (si) {
        return AST.Object(si.head.concat(si.tail.modifiers), si.tail.object);
      });
    }),
    
    // <it2> ::= <digit> | <letter>
    //       |   '{' <text> '}'
    //       |   '\' <letters>
    //       |   '*' <object>
    //       |   '@' <dir>
    it2: memo(function () {
      return or(
        regexLit(/^[0-9a-zA-Z]/).to(function (c) {
          return AST.Object(FP.List.empty, p.toMath("\\labelstyle " + c));
        }),
        regexLit(/^(\\[a-zA-Z][a-zA-Z0-9]*)/).to(function (c) {
          return AST.Object(FP.List.empty, p.toMath("\\labelstyle " + c));
        }),
        lit("{").andr(p.text).andl(felem("}")).to(function (t) {
          return AST.Object(FP.List.empty, p.toMath("\\labelstyle " + t));
        }),
        lit('*').andr(p.object),
        lit('@').andr(p.dir).to(function (dir) {
          return AST.Object(FP.List.empty, dir);
        })
      );
    }),
    
    // <alias> ::= '=' '"' <id> '"'
    alias: memo(function () {
      return seq('=', '"', p.id, '"').opt().to(function (optId) {
        return optId.map(function (id) { return id.head.tail; });
      });
    }),
    
    // <xymatrix> ::= <setup> '{' <rows> '}'
    xymatrix: memo(function () {
      return p.setup().andl(flit("{")).and(p.rows).andl(flit("}")).to(function (sr) {
        return AST.Command.Xymatrix(sr.head, sr.tail);
      })
    }),
    
    // <setup> ::= <switch>*
    // <switch> ::= '"' <prefix> '"'
    //          |   '@' <rcchar> <add op> <dimen>
    //          |   '@' '!' <rcchar> '0'
    //          |   '@' '!' <rcchar> '=' <dimen>
    //          |   '@' '!' <rcchar>
    //          |   '@' ( 'M' | 'W' | 'H' ) <add op> <dimen>
    //          |   '@' '1'
    //          |   '@' 'L' <add op> <dimen>
    //          |   '@' <nonemptyDirection>
    //          |   '@' '*' '[' <shape> ']'
    //          |   '@' '*' <add op> <size>
    // <rcchar> ::= 'R' | 'C' | <empty>
    // <mwhlchar> ::= 'M' | 'W' | 'H' | 'L'
    setup: memo(function () {
      return rep(fun(or(
        lit('"').andr(fun(regex(/^[^"]+/))).andl(felem('"')).to(function (p) {
          return AST.Command.Xymatrix.Setup.Prefix(p);
        }),
        lit("@!").andr(fun(regex(/^[RC]/).opt().to(function (c) {
          return c.getOrElse("");
        }))).and(fun(
          or(
            elem("0").to(function() { return "0em"; }),
            elem("=").andr(p.dimen)
          )
        )).to(function (cd) {
          var dimen = cd.tail;
          switch (cd.head) {
            case "R": return AST.Command.Xymatrix.Setup.PretendEntrySize.Height(dimen);
            case "C": return AST.Command.Xymatrix.Setup.PretendEntrySize.Width(dimen);
            default: return AST.Command.Xymatrix.Setup.PretendEntrySize.HeightAndWidth(dimen);
          }
        }),
        lit("@!").andr(fun(
          or(
            elem("R").to(function () { return AST.Command.Xymatrix.Setup.FixGrid.Row(); }),
            elem("C").to(function () { return AST.Command.Xymatrix.Setup.FixGrid.Column(); })
          ).opt().to(function (rc) {
            return rc.getOrElse(AST.Command.Xymatrix.Setup.FixGrid.RowAndColumn());
          })
        )),
        lit("@").andr(fun(regex(/^[MWHL]/))).and(p.addOp).and(p.dimen).to(function (cod) {
          var addop = cod.head.tail;
          var dimen = cod.tail;
          switch (cod.head.head) {
            case "M": return AST.Command.Xymatrix.Setup.AdjustEntrySize.Margin(addop, dimen);
            case "W": return AST.Command.Xymatrix.Setup.AdjustEntrySize.Width(addop, dimen);
            case "H": return AST.Command.Xymatrix.Setup.AdjustEntrySize.Height(addop, dimen);
            case "L": return AST.Command.Xymatrix.Setup.AdjustLabelSep(addop, dimen);
          }
        }),
        lit("@").andr(p.nonemptyDirection).to(function (d) {
          return AST.Command.Xymatrix.Setup.SetOrientation(d);
        }),
        lit("@*[").andr(p.shape).andl(flit("]")).to(function (s) {
          return AST.Command.Xymatrix.Setup.AddModifier(s);
        }),
        lit("@*").andr(p.addOp).and(p.size).to(function (os) {
          return AST.Command.Xymatrix.Setup.AddModifier(AST.Modifier.AddOp(os.head, os.tail));
        }),
        lit("@").andr(fun(regex(/^[RC]/).opt().to(function (c) {
          return c.getOrElse("");
        }))).and(p.addOp).and(p.dimen).to(function (cod) {
          var addop = cod.head.tail;
          var dimen = cod.tail;
          switch (cod.head.head) {
            case "R": return AST.Command.Xymatrix.Setup.ChangeSpacing.Row(addop, dimen);
            case "C": return AST.Command.Xymatrix.Setup.ChangeSpacing.Column(addop, dimen);
            default: return AST.Command.Xymatrix.Setup.ChangeSpacing.RowAndColumn(addop, dimen);
          }
        }),
        lit("@1").to(function () {
          return AST.Command.Xymatrix.Setup.AdjustEntrySize.Margin(AST.Modifier.AddOp.Set(), "1pc");
        })
      )));
    }),
    
    // <rows> ::= <row> ( '\\' <row> )*
    rows: memo(function () {
      return p.row().and(fun(rep(lit("\\\\").andr(p.row)))).to(function (rrs) {
        var rows = rrs.tail.prepend(rrs.head);
        if (!rows.isEmpty) {
          var lastRow = rows.at(rows.length() - 1);
          if (lastRow.entries.length() === 1 && lastRow.entries.at(0).isEmpty) {
            rows = rows.reverse().tail.reverse();
          }
        }
        return rows;
      })
    }),
    
    // <row> ::= <entry> ( '&' <entry> )*
    row: memo(function () {
      return p.entry().and(fun(rep(lit("&").andr(p.entry)))).to(function (ees) {
        return AST.Command.Xymatrix.Row(ees.tail.prepend(ees.head));
      })
    }),
    
    // <entry> ::= '*' <object> <pos> <decor>
    //         |   <entry modifier>* <loose objectbox> <decor>
    entry: memo(function () {
      return or(
        lit("*").andr(p.object).and(p.pos).and(p.decor).to(function (opd) {
          var obj = opd.head.head;
          var pos = opd.head.tail;
          var decor = opd.tail;
          return AST.Command.Xymatrix.Entry.ObjectEntry(obj, pos, decor);
        }),
        p.entryModifier().rep().and(p.looseObjectbox).and(p.decor).to(function (mopd) {
          var modifiers = mopd.head.head.foldLeft(FP.List.empty, function (tmpMs, ms) {
            return ms.concat(tmpMs);
          });
          var isEmpty = mopd.head.tail.isEmpty;
          var objbox = mopd.head.tail.object;
          var decor = mopd.tail;
          if (isEmpty && modifiers.isEmpty) {
            return AST.Command.Xymatrix.Entry.EmptyEntry(decor);
          }
          return AST.Command.Xymatrix.Entry.SimpleEntry(modifiers, objbox, decor);
        })
      );
    }),
    
    // <entry modifier> ::= '**' '[' <shape> ']' | '**' '{' <modifier>* '}'
    entryModifier: memo(function () {
      return or(
        lit("**").andr(flit("[")).andr(p.shape).andl(flit("]")).to(function (s) {
          return FP.List.empty.append(s);
        }),
        lit("**").andr(flit("{")).andr(fun(rep(p.modifier))).andl(flit("}"))
      );
    }),
    
    // <loose objectbox> ::= <objectbox>
    //                   |   /[^\\{}%&]+/* ( ( '\' not( '\' | <decor command names> ) ( '{' | '}' | '%' | '&' ) | '{' <text> '}' | /%[^\r\n]*(\r\n|\r|\n)?/ ) /[^\\{}%&]+/* )*
    // <decor command names> ::= 'ar' | 'xymatrix' | 'PATH' | 'afterPATH'
    //                       |   'save' | 'restore' | 'POS' | 'afterPOS' | 'drop' | 'connect' | 'xyignore'
    looseObjectbox: memo(function () {
      return or(
        p.objectbox().to(function (o) { return {
          isEmpty:false, object:o
        } }),
        regex(/^[^\\{}%&]+/).opt().to(function (rs) { return rs.getOrElse(""); }).and(fun(
          rep(
            or(
              elem("{").andr(p.text).andl(felem("}")).to(function (t) { return "{" + t + "}"; }),
              elem("\\").andr(fun(
                not(regex(/^(\\|ar|xymatrix|PATH|afterPATH|save|restore|POS|afterPOS|drop|connect|xyignore|([lrud]+(twocell|uppertwocell|lowertwocell|compositemap))|xtwocell|xuppertwocell|xlowertwocell|xcompositemap)/))
              )).andr(fun(
                regex(/^[{}%&]/).opt().to(function (c) { return c.getOrElse(""); })
              )).to(function (t) {
                return "\\" + t;
              }),
              regex(/^%[^\r\n]*(\r\n|\r|\n)?/).to(function (x) {
                return ' '; // ignore comments
              })
            ).and(fun(
              regex(/^[^\\{}%&]+/).opt().to(function (cs) { return cs.getOrElse(""); })
            )).to(function (tt) {
              return tt.head + tt.tail;
            })
          ).to(function (cs) { return cs.mkString("") })
        )).to(function (tt) {
          var text = tt.head + tt.tail;
          var isEmpty = (text.trim().length === 0);
          var object = p.toMath("\\hbox{$\\objectstyle{" + text + "}$}");
          return {
            isEmpty:isEmpty, object:object
          };
        })
      )
    }),
    
    // <command> ::= <twocell> <twocell switch>* <twocell arrow>
    twocellCommand: memo(function () {
      return p.twocell().and(fun(rep(p.twocellSwitch))).and(p.twocellArrow).to(function (tsa) {
        return AST.Command.Twocell(tsa.head.head, tsa.head.tail, tsa.tail);
      });
    }),
    
    // <twocell> ::= '\' /[lrud]+/ 'twocell'
    //           |   '\' /[lrud]+/ 'uppertwocell'
    //           |   '\' /[lrud]+/ 'lowertwocell'
    //           |   '\' /[lrud]+/ 'compositemap'
    //           |   '\xtwocell' '[' /[lrud]+/ ']' '{' <text> '}'
    //           |   '\xuppertwocell' '[' /[lrud]+/ ']' '{' <text> '}'
    //           |   '\xlowertwocell' '[' /[lrud]+/ ']' '{' <text> '}'
    //           |   '\xcompositemap' '[' /[lrud]+/ ']' '{' <text> '}'
    twocell: memo(function () {
      return or(
        regexLit(/^\\[lrud]+twocell/).to(function (h) {
          var hops = h.substring(1, h.length - "twocell".length);
          return AST.Command.Twocell.Twocell(hops, FP.Option.empty);
        }),
        regexLit(/^\\[lrud]+uppertwocell/).to(function (h) {
          var hops = h.substring(1, h.length - "uppertwocell".length);
          return AST.Command.Twocell.UpperTwocell(hops, FP.Option.empty);
        }),
        regexLit(/^\\[lrud]+lowertwocell/).to(function (h) {
          var hops = h.substring(1, h.length - "lowertwocell".length);
          return AST.Command.Twocell.LowerTwocell(hops, FP.Option.empty);
        }),
        regexLit(/^\\[lrud]+compositemap/).to(function (h) {
          var hops = h.substring(1, h.length - "compositemap".length);
          return AST.Command.Twocell.CompositeMap(hops, FP.Option.empty);
        }),
        or(
          lit("\\xtwocell").to(function () { return AST.Command.Twocell.Twocell; }),
          lit("\\xuppertwocell").to(function () { return AST.Command.Twocell.UpperTwocell; }),
          lit("\\xlowertwocell").to(function () { return AST.Command.Twocell.LowerTwocell; }),
          lit("\\xcompositemap").to(function () { return AST.Command.Twocell.CompositeMap; })
        ).andl(flit("[")).and(fun(regex(/^[lrud]+/))).andl(flit("]")).andl(flit("{")).and(p.text).andl(flit("}")).to(function (cht) {
          var textObject = AST.Object(FP.List.empty, p.toMath("\\labelstyle " + cht.tail));
          return cht.head.head(cht.head.tail, FP.Option.Some(textObject));
        })
      );
    }),
    
    // <twocell switch> ::= '^' <twocell label>
    //          |   '_' <twocell label>
    //          |   '\omit'
    //          |   '~!'
    //          |   '~' ( '`' | "'" ) '{' <object> '}'
    //          |   '~' ( '' | '^' | '_' ) '{' <object> ( '~**' <object> )? '}'
    //          |   <nudge>
    twocellSwitch: memo(function () {
      return or(
        lit("^").andr(p.twocellLabel).to(function (l) {
          return AST.Command.Twocell.Switch.UpperLabel(l);
        }),
        lit("_").andr(p.twocellLabel).to(function (l) {
          return AST.Command.Twocell.Switch.LowerLabel(l);
        }),
        lit("\\omit").to(function () {
          return AST.Command.Twocell.Switch.DoNotSetCurvedArrows();
        }),
        lit("~!").to(function () {
          return AST.Command.Twocell.Switch.PlaceModMapObject();
        }),
        regexLit(/^(~[`'])/).andl(flit("{")).and(p.object).andl(flit("}")).to(function (wo) {
          var what = wo.head.substring(1);
          return AST.Command.Twocell.Switch.ChangeHeadTailObject(what, wo.tail);
        }),
        regexLit(/^(~[\^_]?)/).andl(flit("{")).and(p.object).and(fun(opt(lit("~**").andr(p.object)))).andl(flit("}")).to(function (wso) {
          var what = wso.head.head.substring(1);
          var spacer = wso.head.tail;
          var maybeObject = wso.tail;
          return AST.Command.Twocell.Switch.ChangeCurveObject(what, spacer, maybeObject);
        }),
        p.nudge().to(function (n) {
          return AST.Command.Twocell.Switch.SetCurvature(n);
        })
      );
    }),
    
    // <twocell label> ::= <digit> | <letter> | <cs>
    //                 |   '{' <nudge>? '*' <object> '}'
    //                 |   '{' <nudge>? <text> '}'
    twocellLabel: memo(function () {
      return or(
        regexLit(/^[0-9a-zA-Z]/).to(function (c) {
          var obj = AST.Object(FP.List.empty, p.toMath("\\twocellstyle " + c));
          return AST.Command.Twocell.Label(FP.Option.empty, obj);
        }),
        regexLit(/^(\\[a-zA-Z][a-zA-Z0-9]*)/).to(function (c) {
          var obj = AST.Object(FP.List.empty, p.toMath("\\twocellstyle " + c));
          return AST.Command.Twocell.Label(FP.Option.empty, obj);
        }),
        lit("{").andr(fun(opt(p.nudge))).andl(flit("*")).and(p.object).andl(flit("}")).to(function (no) {
          return AST.Command.Twocell.Label(no.head, no.tail);
        }),
        lit("{").andr(fun(opt(p.nudge))).and(p.text).andl(felem("}")).to(function (nt) {
          var obj = AST.Object(FP.List.empty, p.toMath("\\twocellstyle " + nt.tail));
          return AST.Command.Twocell.Label(nt.head, obj);
        })
      );
    }),
    
    // <nudge> ::= '<' <factor> '>'
    //         |   '<\omit>'
    nudge: memo(function () {
      return or(
        lit("<\\omit>").to(function () {
          return AST.Command.Twocell.Nudge.Omit();
        }),
        lit("<").andr(p.factor).andl(flit(">")).to(function (n) {
          return AST.Command.Twocell.Nudge.Number(n);
        })
      );
    }),
    
    // <twocell arrow> ::= '{' <twocell tok> (<twocell label entry> '}'
    //                 |   '{' <nudge> <twocell label entry> '}'
    //                 |   '{' <twocell label entry> '}'
    //                 |   <empty>
    // <twocell tok> ::= '^' | '_' | '='
    //               |   '\omit'
    //               |   '`' | "'" | '"' | '!'
    twocellArrow: memo(function () {
      return or(
        lit("{").andr(fun(regexLit(/^([\^_=`'"!]|\\omit)/))).and(p.twocellLabelEntry).andl(flit("}")).to(function (te) {
          return AST.Command.Twocell.Arrow.WithOrientation(te.head, te.tail);
        }),
        lit("{").andr(p.nudge).and(p.twocellLabelEntry).andl(flit("}")).to(function (te) {
          return AST.Command.Twocell.Arrow.WithPosition(te.head, te.tail);
        }),
        lit("{").andr(p.twocellLabelEntry).andl(flit("}")).to(function (e) {
          return AST.Command.Twocell.Arrow.WithOrientation('', e);
        }),
        success("no arrow label").to(function () {
          // TODO 無駄な空描画処理をなくす。
          return AST.Command.Twocell.Arrow.WithOrientation('', AST.Object(FP.List.empty, p.toMath("\\twocellstyle{}")));
        })
      );
    }),
    
    // <twocell label entry> ::= '*' <object>
    //                       |   <text>
    twocellLabelEntry: memo(function () {
      return or(
        lit("*").andr(p.object),
        p.text().to(function (t) {
          return AST.Object(FP.List.empty, p.toMath("\\twocellstyle " + t));
        })
      );
    }),
    
    // \newdirの後の
    // '{' <main> '}' '{' <composite_object> '}'
    newdir: memo(function () {
      return lit("{").andr(p.dirMain).andl(felem("}")).andl(flit("{")).and(p.compositeObject).andl(flit("}")).to(function (mc) {
        return AST.Command.Newdir(mc.head, AST.ObjectBox.CompositeObject(mc.tail));
      });
    }),
    
    // '\xyimport' '(' <factor> ',' <factor> ')' ( '(' <factor> ',' <factor> ')' )? '{' ( <include graphics> | <TeX command> ) '}'
    xyimport: memo(function () {
      return lit("\\xyimport").andr(flit("(")).andr(p.factor).andl(flit(",")).and(p.factor).andl(flit(")")).and(fun(
        opt(lit("(").andr(p.factor).andl(flit(",")).and(p.factor).andl(flit(")")))
      )).andl(flit("{")).and(fun(
        or(
          lit("\\includegraphics").andr(p.includegraphics),
          p.text().to(function (t) { return p.toMath("\\hbox{$\\objectstyle{" + t + "}$}"); })
      ))).andl(flit("}")).to(function (whog) {
        var w = whog.head.head.head;
        var h = whog.head.head.tail;
        var xOffset, yOffset;
        if (whog.head.tail.isDefined) {
          xOffset = whog.head.tail.get.head;
          yOffset = whog.head.tail.get.tail;
        } else {
          xOffset = 0;
          yOffset = 0;
        }
        var graphics = whog.tail;
        if (graphics.isIncludegraphics !== undefined) {
          return AST.Pos.Xyimport.Graphics(w, h, xOffset, yOffset, graphics);
        } else {
          return AST.Pos.Xyimport.TeXCommand(w, h, xOffset, yOffset, graphics);
        }
      });
    }),
    
    // \includegraphicsの後の
    // '*'? '[' ( <includegraphics attr list> )? ']' '{' <file path> '}'
    includegraphics: memo(function () {
      return lit("[").andr(fun(opt(p.includegraphicsAttrList))).andl(flit("]")).andl(flit("{")).and(fun(regexLit(/^[^\s{}]+/))).andl(flit("}")).to(function (af) {
        var attrList = af.head.getOrElse(FP.List.empty);
        var file = af.tail;
        return AST.Command.Includegraphics(false, attrList, file);
      });
    }),
    
    // <includegraphics attr list> := <includegraphics attr key val> ( ',' <includegraphics attr key val> )*
    includegraphicsAttrList: memo(function () {
      return p.includegraphicsAttr().and(fun(rep(lit(",").andr(p.includegraphicsAttr)))).to(function (aas) {
        return aas.tail.prepend(aas.head);
      });
    }),
    
    // <includegraphics attr key val> := 'width' '=' <dimen>
    //                                |  'height' '=' <dimen>
    includegraphicsAttr: memo(function () {
      return or(
        lit("width").andr(flit("=")).andr(p.dimen).to(function (d) {
          return AST.Command.Includegraphics.Attr.Width(d);
        }),
        lit("height").andr(flit("=")).andr(p.dimen).to(function (d) {
          return AST.Command.Includegraphics.Attr.Height(d);
        })
      );
    })
    
  })();
  
  MathJax.Hub.Insert(TEXDEF,{
    environment: {
      xy:            ['XY', null]
    }
  });
  
  xypic.ExecutionError = MathJax.Object.Subclass({
    Init: function (message) {
      this.message = message;
    },
    toMML: function () {
      return MML.merror(MML.mtext(this.message));
    },
    texError: true,
    xyjaxError: true
  });
  
  xypic.ParseError = MathJax.Object.Subclass({
    Init: function (parseResult) {
      this.parseResult = parseResult;
    },
    toMML: function () {
      var pos = this.parseResult.next.pos();
      var lineContents = pos.lineContents();
      return MML.merror(MML.mtext('parse error at or near "' + lineContents + '"'));
      /*
      var col = pos.column();
      var left = lineContents.substring(0, col-1);
      var mid = lineContents.substring(col-1, col);
      var right = lineContents.substring(col);
      return MML.merror(MML.mtext('parse error at or near "'), MML.mtext(left).With({color:"black"}), MML.mtext(mid).With({color:"red"}), MML.mtext(right).With({color:"black"}), MML.mtext('"'));
      */
    },
    texError: true,
    xyjaxError: true
  });
  
  TEX.Parse.Augment({
    /*
     * Handle XY environment
     */
    XY: function(begin) {
      try {
        var parseContext = {
          lastNoSuccess: undefined,
          whiteSpaceRegex: xypic.constants.whiteSpaceRegex
        };
        var input = FP.StringReader(this.string, this.i, parseContext);
        var result = FP.Parsers.parse(p.xy(), input);
        this.i = result.next.offset;
      } catch (e) {
        throw e;
      }
      
      if (result.successful) {
        if (supportGraphics) {
          this.Push(AST.xypic(result.result));
        } else {
          this.Push(MML.merror(xypic.unsupportedBrowserErrorMessage));
        }
      } else {
        throw xypic.ParseError(parseContext.lastNoSuccess);
      }
      
      return begin;
    },
    
    /**
     * Handle xybox
     */
    Xybox: function () {
      try {
        var parseContext = {
          lastNoSuccess: undefined,
          whiteSpaceRegex: xypic.constants.whiteSpaceRegex
        };
        var input = FP.StringReader(this.string, this.i, parseContext);
        var result = FP.Parsers.parse(p.xybox(), input);
        this.i = result.next.offset;
      } catch (e) {
        throw e;
      }
      
      if (result.successful) {
        if (supportGraphics) {
          this.Push(AST.xypic(result.result));
        } else {
          this.Push(MML.merror(xypic.unsupportedBrowserErrorMessage));
        }
      } else {
        throw xypic.ParseError(parseContext.lastNoSuccess);
      }
    },
    
    /**
     * Handle xymatrix
     */
    Xymatrix: function () {
      try {
        var parseContext = {
          lastNoSuccess: undefined,
          whiteSpaceRegex: xypic.constants.whiteSpaceRegex
        };
        var input = FP.StringReader(this.string, this.i, parseContext);
        var result = FP.Parsers.parse(p.xymatrixbox(), input);
        this.i = result.next.offset;
      } catch (e) {
        throw e;
      }
      
      if (result.successful) {
        if (supportGraphics) {
          this.Push(AST.xypic(result.result));
        } else {
          this.Push(MML.merror(xypic.unsupportedBrowserErrorMessage));
        }
      } else {
        throw xypic.ParseError(parseContext.lastNoSuccess);
      }
    },
    
    /**
     * Handle newdir
     */
    XypicNewdir: function () {
      try {
        var parseContext = {
          lastNoSuccess: undefined,
          whiteSpaceRegex: xypic.constants.whiteSpaceRegex
        };
        var input = FP.StringReader(this.string, this.i, parseContext);
        var result = FP.Parsers.parse(p.newdir(), input);
        this.i = result.next.offset;
      } catch (e) {
        throw e;
      }
      
      if (result.successful) {
        if (supportGraphics) {
          this.Push(AST.xypic.newdir(result.result));
        } else {
          this.Push(MML.merror(xypic.unsupportedBrowserErrorMessage));
        }
      } else {
        throw xypic.ParseError(parseContext.lastNoSuccess);
      }
    },
    
    
    /**
     * Handle includegraphics
     */
    Xyincludegraphics: function () {
      try {
        var parseContext = {
          lastNoSuccess: undefined,
          whiteSpaceRegex: xypic.constants.whiteSpaceRegex
        };
        var input = FP.StringReader(this.string, this.i, parseContext);
        var result = FP.Parsers.parse(p.includegraphics(), input);
        this.i = result.next.offset;
      } catch (e) {
        throw e;
      }
      
      if (result.successful) {
        if (supportGraphics) {
          this.Push(AST.xypic.includegraphics(result.result));
        } else {
          this.Push(MML.merror(xypic.unsupportedBrowserErrorMessage));
        }
      } else {
        throw xypic.ParseError(parseContext.lastNoSuccess);
      }
    }
  });
  
  var supportGraphics = false;
  MathJax.Hub.Browser.Select({
    Firefox: function (browser) {
      supportGraphics = true;
    },
    Safari: function (browser) {
      supportGraphics = true;
    },
    Chrome: function (browser) {
      supportGraphics = true;
    },
    Opera: function (browser) {
      supportGraphics = true;
    },
    MSIE: function (browser) {
      if (MathJax.Hub.Browser.versionAtLeast("9.0") && document.documentMode >= 9) {
        supportGraphics = true;
      }
    }
  });
  
  MathJax.Hub.Startup.signal.Post("TeX Xy-pic Ready");
});












MathJax.Hub.Register.StartupHook("HTML-CSS Xy-pic Config Require",function () {
  MathJax.Hub.Startup.signal.Post("HTML-CSS Xy-pic Config Ready");
});

MathJax.Hub.Register.StartupHook("SVG Xy-pic Config Require",function () {
  MathJax.Hub.Startup.signal.Post("SVG Xy-pic Config Ready");
});

MathJax.Hub.Register.StartupHook("Device-Independent Xy-pic Require",function () {
  var FP = MathJax.Extension.fp;
  var MML = MathJax.ElementJax.mml;
  var HUB = MathJax.Hub;
  var xypic = MathJax.Extension.xypic;
  var AST = xypic.AST;
  
  var SVGNS = "http://www.w3.org/2000/svg";
  var XHTMLNS = "http://www.w3.org/1999/xhtml";
  var XLINKNS = "http://www.w3.org/1999/xlink";
  
  
  // override MathJax.Hub.formatError function to display runtime error.
  var hub_formatError = HUB.formatError;
  HUB.formatError = function (script, err) {
    if (err.xyjaxError !== undefined) {
      var origMessage = HUB.config.errorSettings.message;
      HUB.config.errorSettings.message = "[" + err.message + "]";
      hub_formatError.apply(HUB, [script, err]);
      HUB.config.errorSettings.message = origMessage;
    } else {
      throw err;
      hub_formatError.apply(HUB, [script, err]);
    }
  }
  
  var memoize = xypic.memoize;
  
  AST.xypic.Augment({}, {
    lengthResolution: 128,
    interpolationResolution: 5,
    machinePrecision: 1e-12
  });
  
  xypic.DirRepository = MathJax.Object.Subclass({
    Init: function () {
      this.userDirMap = {};
    },
    get: function (dirMain) {
      return this.userDirMap[dirMain];
    },
    put: function (dirMain, compositeObject) {
      this.userDirMap[dirMain] = compositeObject;
    }
  });
  
  xypic.ModifierRepository = MathJax.Object.Subclass({
    Init: function () {
      this.userModifierMap = {};
    },
    get: function (shapeName) {
      var modifier = xypic.ModifierRepository.embeddedModifierMap[shapeName];
      if (modifier !== undefined) {
        return modifier;
      }
      return this.userModifierMap[shapeName];
    },
    put: function (shapeName, modifier) {
      if (xypic.ModifierRepository.embeddedModifierMap[shapeName] === undefined) {
        this.userModifierMap[shapeName] = modifier;
      }
    }
  }, {
    embeddedModifierMap: {
      "o":AST.Modifier.Shape.Circle(),
      "l":AST.Modifier.Shape.L(),
      "r":AST.Modifier.Shape.R(),
      "u":AST.Modifier.Shape.U(),
      "d":AST.Modifier.Shape.D(),
      "c":AST.Modifier.Shape.C(),
      "aliceblue":AST.Modifier.Shape.ChangeColor("aliceblue"),
      "antiquewhite":AST.Modifier.Shape.ChangeColor("antiquewhite"),
      "aqua":AST.Modifier.Shape.ChangeColor("aqua"),
      "aquamarine":AST.Modifier.Shape.ChangeColor("aquamarine"),
      "azure":AST.Modifier.Shape.ChangeColor("azure"),
      "beige":AST.Modifier.Shape.ChangeColor("beige"),
      "bisque":AST.Modifier.Shape.ChangeColor("bisque"),
      "black":AST.Modifier.Shape.ChangeColor("black"),
      "blanchedalmond":AST.Modifier.Shape.ChangeColor("blanchedalmond"),
      "blue":AST.Modifier.Shape.ChangeColor("blue"),
      "blueviolet":AST.Modifier.Shape.ChangeColor("blueviolet"),
      "brown":AST.Modifier.Shape.ChangeColor("brown"),
      "burlywood":AST.Modifier.Shape.ChangeColor("burlywood"),
      "cadetblue":AST.Modifier.Shape.ChangeColor("cadetblue"),
      "chartreuse":AST.Modifier.Shape.ChangeColor("chartreuse"),
      "chocolate":AST.Modifier.Shape.ChangeColor("chocolate"),
      "coral":AST.Modifier.Shape.ChangeColor("coral"),
      "cornflowerblue":AST.Modifier.Shape.ChangeColor("cornflowerblue"),
      "cornsilk":AST.Modifier.Shape.ChangeColor("cornsilk"),
      "crimson":AST.Modifier.Shape.ChangeColor("crimson"),
      "cyan":AST.Modifier.Shape.ChangeColor("cyan"),
      "darkblue":AST.Modifier.Shape.ChangeColor("darkblue"),
      "darkcyan":AST.Modifier.Shape.ChangeColor("darkcyan"),
      "darkgoldenrod":AST.Modifier.Shape.ChangeColor("darkgoldenrod"),
      "darkgray":AST.Modifier.Shape.ChangeColor("darkgray"),
      "darkgreen":AST.Modifier.Shape.ChangeColor("darkgreen"),
      "darkgrey":AST.Modifier.Shape.ChangeColor("darkgrey"),
      "darkkhaki":AST.Modifier.Shape.ChangeColor("darkkhaki"),
      "darkmagenta":AST.Modifier.Shape.ChangeColor("darkmagenta"),
      "darkolivegreen":AST.Modifier.Shape.ChangeColor("darkolivegreen"),
      "darkorange":AST.Modifier.Shape.ChangeColor("darkorange"),
      "darkorchid":AST.Modifier.Shape.ChangeColor("darkorchid"),
      "darkred":AST.Modifier.Shape.ChangeColor("darkred"),
      "darksalmon":AST.Modifier.Shape.ChangeColor("darksalmon"),
      "darkseagreen":AST.Modifier.Shape.ChangeColor("darkseagreen"),
      "darkslateblue":AST.Modifier.Shape.ChangeColor("darkslateblue"),
      "darkslategray":AST.Modifier.Shape.ChangeColor("darkslategray"),
      "darkslategrey":AST.Modifier.Shape.ChangeColor("darkslategrey"),
      "darkturquoise":AST.Modifier.Shape.ChangeColor("darkturquoise"),
      "darkviolet":AST.Modifier.Shape.ChangeColor("darkviolet"),
      "deeppink":AST.Modifier.Shape.ChangeColor("deeppink"),
      "deepskyblue":AST.Modifier.Shape.ChangeColor("deepskyblue"),
      "dimgray":AST.Modifier.Shape.ChangeColor("dimgray"),
      "dimgrey":AST.Modifier.Shape.ChangeColor("dimgrey"),
      "dodgerblue":AST.Modifier.Shape.ChangeColor("dodgerblue"),
      "firebrick":AST.Modifier.Shape.ChangeColor("firebrick"),
      "floralwhite":AST.Modifier.Shape.ChangeColor("floralwhite"),
      "forestgreen":AST.Modifier.Shape.ChangeColor("forestgreen"),
      "fuchsia":AST.Modifier.Shape.ChangeColor("fuchsia"),
      "gainsboro":AST.Modifier.Shape.ChangeColor("gainsboro"),
      "ghostwhite":AST.Modifier.Shape.ChangeColor("ghostwhite"),
      "gold":AST.Modifier.Shape.ChangeColor("gold"),
      "goldenrod":AST.Modifier.Shape.ChangeColor("goldenrod"),
      "gray":AST.Modifier.Shape.ChangeColor("gray"),
      "grey":AST.Modifier.Shape.ChangeColor("grey"),
      "green":AST.Modifier.Shape.ChangeColor("green"),
      "greenyellow":AST.Modifier.Shape.ChangeColor("greenyellow"),
      "honeydew":AST.Modifier.Shape.ChangeColor("honeydew"),
      "hotpink":AST.Modifier.Shape.ChangeColor("hotpink"),
      "indianred":AST.Modifier.Shape.ChangeColor("indianred"),
      "indigo":AST.Modifier.Shape.ChangeColor("indigo"),
      "ivory":AST.Modifier.Shape.ChangeColor("ivory"),
      "khaki":AST.Modifier.Shape.ChangeColor("khaki"),
      "lavender":AST.Modifier.Shape.ChangeColor("lavender"),
      "lavenderblush":AST.Modifier.Shape.ChangeColor("lavenderblush"),
      "lawngreen":AST.Modifier.Shape.ChangeColor("lawngreen"),
      "lemonchiffon":AST.Modifier.Shape.ChangeColor("lemonchiffon"),
      "lightblue":AST.Modifier.Shape.ChangeColor("lightblue"),
      "lightcoral":AST.Modifier.Shape.ChangeColor("lightcoral"),
      "lightcyan":AST.Modifier.Shape.ChangeColor("lightcyan"),
      "lightgoldenrodyellow":AST.Modifier.Shape.ChangeColor("lightgoldenrodyellow"),
      "lightgray":AST.Modifier.Shape.ChangeColor("lightgray"),
      "lightgreen":AST.Modifier.Shape.ChangeColor("lightgreen"),
      "lightgrey":AST.Modifier.Shape.ChangeColor("lightgrey"),
      "lightpink":AST.Modifier.Shape.ChangeColor("lightpink"),
      "lightsalmon":AST.Modifier.Shape.ChangeColor("lightsalmon"),
      "lightseagreen":AST.Modifier.Shape.ChangeColor("lightseagreen"),
      "lightskyblue":AST.Modifier.Shape.ChangeColor("lightskyblue"),
      "lightslategray":AST.Modifier.Shape.ChangeColor("lightslategray"),
      "lightslategrey":AST.Modifier.Shape.ChangeColor("lightslategrey"),
      "lightsteelblue":AST.Modifier.Shape.ChangeColor("lightsteelblue"),
      "lightyellow":AST.Modifier.Shape.ChangeColor("lightyellow"),
      "lime":AST.Modifier.Shape.ChangeColor("lime"),
      "limegreen":AST.Modifier.Shape.ChangeColor("limegreen"),
      "linen":AST.Modifier.Shape.ChangeColor("linen"),
      "magenta":AST.Modifier.Shape.ChangeColor("magenta"),
      "maroon":AST.Modifier.Shape.ChangeColor("maroon"),
      "mediumaquamarine":AST.Modifier.Shape.ChangeColor("mediumaquamarine"),
      "mediumblue":AST.Modifier.Shape.ChangeColor("mediumblue"),
      "mediumorchid":AST.Modifier.Shape.ChangeColor("mediumorchid"),
      "mediumpurple":AST.Modifier.Shape.ChangeColor("mediumpurple"),
      "mediumseagreen":AST.Modifier.Shape.ChangeColor("mediumseagreen"),
      "mediumslateblue":AST.Modifier.Shape.ChangeColor("mediumslateblue"),
      "mediumspringgreen":AST.Modifier.Shape.ChangeColor("mediumspringgreen"),
      "mediumturquoise":AST.Modifier.Shape.ChangeColor("mediumturquoise"),
      "mediumvioletred":AST.Modifier.Shape.ChangeColor("mediumvioletred"),
      "midnightblue":AST.Modifier.Shape.ChangeColor("midnightblue"),
      "mintcream":AST.Modifier.Shape.ChangeColor("mintcream"),
      "mistyrose":AST.Modifier.Shape.ChangeColor("mistyrose"),
      "moccasin":AST.Modifier.Shape.ChangeColor("moccasin"),
      "navajowhite":AST.Modifier.Shape.ChangeColor("navajowhite"),
      "navy":AST.Modifier.Shape.ChangeColor("navy"),
      "oldlace":AST.Modifier.Shape.ChangeColor("oldlace"),
      "olive":AST.Modifier.Shape.ChangeColor("olive"),
      "olivedrab":AST.Modifier.Shape.ChangeColor("olivedrab"),
      "orange":AST.Modifier.Shape.ChangeColor("orange"),
      "orangered":AST.Modifier.Shape.ChangeColor("orangered"),
      "orchid":AST.Modifier.Shape.ChangeColor("orchid"),
      "palegoldenrod":AST.Modifier.Shape.ChangeColor("palegoldenrod"),
      "palegreen":AST.Modifier.Shape.ChangeColor("palegreen"),
      "paleturquoise":AST.Modifier.Shape.ChangeColor("paleturquoise"),
      "palevioletred":AST.Modifier.Shape.ChangeColor("palevioletred"),
      "papayawhip":AST.Modifier.Shape.ChangeColor("papayawhip"),
      "peachpuff":AST.Modifier.Shape.ChangeColor("peachpuff"),
      "peru":AST.Modifier.Shape.ChangeColor("peru"),
      "pink":AST.Modifier.Shape.ChangeColor("pink"),
      "plum":AST.Modifier.Shape.ChangeColor("plum"),
      "powderblue":AST.Modifier.Shape.ChangeColor("powderblue"),
      "purple":AST.Modifier.Shape.ChangeColor("purple"),
      "red":AST.Modifier.Shape.ChangeColor("red"),
      "rosybrown":AST.Modifier.Shape.ChangeColor("rosybrown"),
      "royalblue":AST.Modifier.Shape.ChangeColor("royalblue"),
      "saddlebrown":AST.Modifier.Shape.ChangeColor("saddlebrown"),
      "salmon":AST.Modifier.Shape.ChangeColor("salmon"),
      "sandybrown":AST.Modifier.Shape.ChangeColor("sandybrown"),
      "seagreen":AST.Modifier.Shape.ChangeColor("seagreen"),
      "seashell":AST.Modifier.Shape.ChangeColor("seashell"),
      "sienna":AST.Modifier.Shape.ChangeColor("sienna"),
      "silver":AST.Modifier.Shape.ChangeColor("silver"),
      "skyblue":AST.Modifier.Shape.ChangeColor("skyblue"),
      "slateblue":AST.Modifier.Shape.ChangeColor("slateblue"),
      "slategray":AST.Modifier.Shape.ChangeColor("slategray"),
      "slategrey":AST.Modifier.Shape.ChangeColor("slategrey"),
      "snow":AST.Modifier.Shape.ChangeColor("snow"),
      "springgreen":AST.Modifier.Shape.ChangeColor("springgreen"),
      "steelblue":AST.Modifier.Shape.ChangeColor("steelblue"),
      "tan":AST.Modifier.Shape.ChangeColor("tan"),
      "teal":AST.Modifier.Shape.ChangeColor("teal"),
      "thistle":AST.Modifier.Shape.ChangeColor("thistle"),
      "tomato":AST.Modifier.Shape.ChangeColor("tomato"),
      "turquoise":AST.Modifier.Shape.ChangeColor("turquoise"),
      "violet":AST.Modifier.Shape.ChangeColor("violet"),
      "wheat":AST.Modifier.Shape.ChangeColor("wheat"),
      "white":AST.Modifier.Shape.ChangeColor("white"),
      "whitesmoke":AST.Modifier.Shape.ChangeColor("whitesmoke"),
      "yellow":AST.Modifier.Shape.ChangeColor("yellow"),
      "yellowgreen":AST.Modifier.Shape.ChangeColor("yellowgreen")
    }
  });
  
  // user defined shapes are global in scope.
  xypic.repositories = MathJax.Object.Subclass({});
  
  xypic.repositories.modifierRepository = xypic.ModifierRepository();
  xypic.repositories.dirRepository = xypic.DirRepository();
  
  xypic.Graphics = MathJax.Object.Subclass({}, {
    createElement: function (type) {
//      if (document.createElementNS !== undefined) {
        return document.createElementNS(SVGNS, type);
//      } else {
//        return document.createElement(type);
//      }
    }
  });
  xypic.Graphics.SVG = xypic.Graphics.Subclass({
    createGroup: function (transform) {
      return xypic.Graphics.SVG.Group(this, transform);
    },
    createChangeColorGroup: function (color) {
      return xypic.Graphics.SVG.ChangeColorGroup(this, color);
    },
    createSVGElement: function (type, def) {
      var obj = xypic.Graphics.createElement(type);
      if (def) {
        for (var id in def) {
          if (def.hasOwnProperty(id)) {
            if (id === "xlink:href") {
              obj.setAttributeNS(XLINKNS, id, def[id].toString());
            } else {
              obj.setAttribute(id, def[id].toString());
            }
          }
        }
      }
      this.drawArea.appendChild(obj);
      return obj;
    },
    appendChild: function (svgElement) {
      this.drawArea.appendChild(svgElement);
      return svgElement;
    },
    transformBuilder: function () {
      return xypic.Graphics.SVG.Transform();
    }
  });
  xypic.Graphics.SVG.World = xypic.Graphics.SVG.Subclass({
    Init: function (height, depth, width, strokeWidth, color, def) {
      var svg = xypic.Graphics.createElement("svg");
      svg.setAttribute("xmlns", SVGNS);
      svg.setAttribute("version", "1.1");
      if (def) {
        for (var id in def) {
          if (def.hasOwnProperty(id)) {
            svg.setAttribute(id, def[id].toString());
          }
        }
      }
      if (svg.style) {
        svg.style.width = xypic.Em(width);
        svg.style.height = xypic.Em(height + depth);
      }
      var def = {
        fill:"none", stroke:color, "stroke-linecap":"round",
        "stroke-width":xypic.em2px(strokeWidth)
      };
      this.drawArea = xypic.Graphics.createElement("g");
      for (var id in def) {
        if (def.hasOwnProperty(id)) {
          this.drawArea.setAttribute(id, def[id].toString());
        }
      }
      svg.appendChild(this.drawArea);
      this.svg = svg;
      this.boundingBox = undefined;
      this.color = color;
    },
    setHeight: function (height) {
      this.svg.style.height = xypic.Em(height);
    },
    setWidth: function (height) {
      this.svg.style.width = xypic.Em(height);
    },
    setAttribute: function (name, value) {
      this.svg.setAttribute(name, value.toString());
    },
    extendBoundingBox: function (boundingBox) {
      this.boundingBox = xypic.Frame.combineRect(this.boundingBox, boundingBox);
    },
    getOrigin: function () {
      return { x:0, y:0 };
    },
    getCurrentColor: function () {
      return this.color;
    }
  });
  
  xypic.Graphics.SVG.Transform = MathJax.Object.Subclass({
    Init: function (transform) {
      this.transform = transform || FP.List.empty;
    },
    translate: function (x, y) {
      return xypic.Graphics.SVG.Transform(
        this.transform.append(xypic.Graphics.SVG.Transform.Translate(x, y))
      );
    },
    rotateDegree: function (degree) {
      return xypic.Graphics.SVG.Transform(
        this.transform.append(xypic.Graphics.SVG.Transform.Rotate(degree / 180 * Math.PI))
      );
    },
    rotateRadian: function (radian) {
      return xypic.Graphics.SVG.Transform(
        this.transform.append(xypic.Graphics.SVG.Transform.Rotate(radian))
      );
    },
    toString: function () {
      var form = "";
      this.transform.foreach(function (tr) { form += tr.toTranslateForm() });
      return form;
    },
    apply: function (x, y) {
      var o = { x:x, y:y };
      this.transform.foreach(function (tr) { o = tr.apply(o.x, o.y) });
      return o;
    }
  });
  
  xypic.Graphics.SVG.Transform.Translate = MathJax.Object.Subclass({
    Init: function (dx, dy) {
      this.dx = dx;
      this.dy = dy;
    },
    apply: function (x, y) {
      return { x:x - this.dx, y:y + this.dy };
    },
    toTranslateForm: function () {
      return "translate(" + xypic.em2px(this.dx) + "," + xypic.em2px(-this.dy) + ") ";
    }
  });
  
  xypic.Graphics.SVG.Transform.Rotate = MathJax.Object.Subclass({
    Init: function (radian) {
      this.radian = radian;
    },
    apply: function (x, y) {
      var c = Math.cos(this.radian);
      var s = Math.sin(this.radian);
      return { x:c * x + s * y, y:-s * x + c * y };
    },
    toTranslateForm: function () {
      return "rotate(" + (-180 * this.radian / Math.PI) + ") ";
    }
  });
  
  xypic.Graphics.SVG.Group = xypic.Graphics.SVG.Subclass({
    Init: function (parent, transform) {
      this.parent = parent;
      this.drawArea = parent.createSVGElement("g", 
        transform === undefined? {} : { transform: transform.toString() });
      var parentOrigin = parent.getOrigin();
      if (transform === undefined) {
        this.origin = parentOrigin;
      } else {
        this.origin = transform.apply(parentOrigin.x, parentOrigin.y);
      }
      memoize(this, "getCurrentColor");
    },
    remove: function () {
      this.drawArea.parentNode.removeChild(this.drawArea);
    },
    extendBoundingBox: function (boundingBox) {
      this.parent.extendBoundingBox(boundingBox);
    },
    getOrigin: function () {
      return this.origin;
    },
    getCurrentColor: function () {
      return this.parent.getCurrentColor();
    }
  });
  
  xypic.Graphics.SVG.ChangeColorGroup = xypic.Graphics.SVG.Subclass({
    Init: function (parent, color) {
      this.parent = parent;
      this.drawArea = parent.createSVGElement("g", {
        stroke: color
      });
      this.color = color;
      memoize(this, "getOrigin");
    },
    remove: function () {
      this.drawArea.parentNode.removeChild(this.drawArea);
    },
    extendBoundingBox: function (boundingBox) {
      this.parent.extendBoundingBox(boundingBox);
    },
    getOrigin: function () {
      return this.parent.getOrigin();
    },
    getCurrentColor: function () {
      return this.color;
    }
  });
  
  xypic.Graphics.Augment({}, {
    createSVG: function (height, depth, width, strokeWidth, color, def) {
      return xypic.Graphics.SVG.World(height, depth, width, strokeWidth, color, def);
    }
  });
  
  xypic.DrawingContext = MathJax.Object.Subclass({
    Init: function (shape, env) {
      this.shape = shape;
      this.env = env;
    },
    
    duplicateEnv: function () {
      var newEnv = this.env.duplicate();
      return xypic.DrawingContext(this.shape, newEnv);
    },
    
    /**
     * shapeを最前面に追加する。
     * @param {xypic.Shape} shape 追加する図形
     */
    appendShapeToFront: function (shape) {
      if (shape.isNone) {
      } else if (this.shape.isNone) {
        this.shape = shape;
      } else {
        this.shape = xypic.Shape.CompositeShape(shape, this.shape);
      }
    },
    
    /**
     * shapeを最背面に追加する。
     * @param {xypic.Shape} shape 追加する図形
     */
    appendShapeToBack: function (shape) {
      if (shape.isNone) {
      } else if (this.shape.isNone) {
        this.shape = shape;
      } else {
        this.shape = xypic.Shape.CompositeShape(this.shape, shape);
      }
    }
  });
  
  xypic.Util = MathJax.Object.Subclass({}, {
    extProd: function (v1, v2) {
      return [v1[1]*v2[2]-v1[2]*v2[1], v1[2]*v2[0]-v1[0]*v2[2], v1[0]*v2[1]-v1[1]*v2[0]];
    },
    sign: function (x) {
      return (x < 0? -1 : (x > 0? 1 : 0));
    },
    sign2: function (x) {
      return (x < 0? -1 : 1);
    },
    roundEpsilon: function (x) {
      if (Math.abs(x) < AST.xypic.machinePrecision) {
        return 0;
      } else {
        return x;
      }
    }
  });
  
  HUB.Browser.Select({
    MSIE: function (browser) {
      if (HUB.Browser.versionAtLeast("9.0") && document.documentMode >= 9) {
        xypic.useSVG = true;
      }
    },
    Firefox: function (browser) {
      xypic.useSVG = true;
    },
    Safari: function (browser) {
      xypic.useSVG = true;
    },
    Chrome: function (browser) {
      xypic.useSVG = true;
    },
    Opera: function (browser) {
      xypic.useSVG = true;
    }
  });
  
  xypic.Frame = MathJax.Object.Subclass({
    toRect: function (def) {
      return xypic.Frame.Rect(this.x, this.y, def);
    },
    toPoint: function () {
      return xypic.Frame.Point(this.x, this.y);
    },
    combineRect: function (that) {
      return xypic.Frame.combineRect(this, that);
    }
  },{
    combineRect: function (frame1, frame2) {
      if (frame1 === undefined) {
        return frame2;
      } else if (frame2 === undefined) {
        return frame1;
      } else {
        var l = -(Math.min(frame1.x-frame1.l, frame2.x-frame2.l) - frame1.x);
        var r = Math.max(frame1.x+frame1.r, frame2.x+frame2.r) - frame1.x;
        var d = -(Math.min(frame1.y-frame1.d, frame2.y-frame2.d) - frame1.y);
        var u = Math.max(frame1.y+frame1.u, frame2.y+frame2.u) - frame1.y;
        return frame1.toRect({l:l, r:r, d:d, u:u});
      }
    }
  });
  
  xypic.Frame.Point = xypic.Frame.Subclass({
    Init: function (x, y) {
      this.x = x;
      this.y = y;
    },
    l: 0,
    r: 0,
    u: 0,
    d: 0,
    isPoint: function () { return true; },
    isRect: function () { return false; },
    isCircle: function () { return false; },
    edgePoint: function (x, y) { return this; },
    proportionalEdgePoint: function (x, y) { return this; },
    grow: function (xMargin, yMargin) {
      var xm = Math.max(0, xMargin);
      var ym = Math.max(0, yMargin);
      return this.toRect({l:xm, r:xm, u:ym, d:ym});
    },
    toSize: function (width, height) {
      return this.toRect({ l:width / 2, r:width / 2, u:height / 2, d:height / 2 });
    },
    growTo: function (width, height) {
      var w = Math.max(0, width);
      var h = Math.max(0, height);
      return this.toRect({ l:w / 2, r:w / 2, u:h / 2, d:h / 2 });
    },
    shrinkTo: function (width, height) {
      return this;
    },
    move: function (x, y) {
      return xypic.Frame.Point(x, y);
    },
    shiftFrame: function (dx, dy) {
      return this;
    },
    rotate: function (angle) {
      return this;
    },
    contains: function (point) {
      return false;
    },
    toString: function () {
      return "{x:"+this.x+", y:"+this.y+"}";
    }
  });
  
  xypic.Frame.Rect = xypic.Frame.Subclass({
    Init: function (x, y, def) {
      this.x = x;
      this.y = y;
      this.l = (def.l || 0);
      this.r = (def.r || 0);
      this.u = (def.u || 0);
      this.d = (def.d || 0);
    },
    isPoint: function () {
      return this.l === 0 && this.r === 0 && this.u === 0 && this.d === 0;
    },
    isRect: function () { return !this.isPoint(); },
    isCircle: function () { return false; },
    edgePoint: function (x, y) {
      if (this.isPoint()) {
        return this;
      }
      var dx = x - this.x;
      var dy = y - this.y;
      if (dx > 0) {
        var ey = dy * this.r / dx;
        if (ey > this.u) {
          return xypic.Frame.Point(this.x + this.u * dx / dy, this.y + this.u);
        } else if (ey < -this.d) {
          return xypic.Frame.Point(this.x - this.d * dx / dy, this.y - this.d);
        }
        return xypic.Frame.Point(this.x + this.r, this.y + ey);
      } else if (dx < 0) {
        var ey = -dy * this.l / dx;
        if (ey > this.u) {
          return xypic.Frame.Point(this.x + this.u * dx / dy, this.y + this.u);
        } else if (ey < -this.d) {
          return xypic.Frame.Point(this.x - this.d * dx / dy, this.y - this.d);
        }
        return xypic.Frame.Point(this.x - this.l, this.y + ey);
      } else {
        if (dy > 0) {
          return xypic.Frame.Point(this.x, this.y + this.u);
        }
        return xypic.Frame.Point(this.x, this.y - this.d);
      }
    },
    proportionalEdgePoint: function (x, y) {
      if (this.isPoint()) {
        return this;
      }
      var dx = x - this.x;
      var dy = y - this.y;
      if (Math.abs(dx) < AST.xypic.machinePrecision && Math.abs(dy) < AST.xypic.machinePrecision) {
        return xypic.Frame.Point(this.x - this.l, this.y + this.u);
      }
      var w = this.l + this.r, h = this.u + this.d;
      var pi = Math.PI;
      var angle = Math.atan2(dy, dx);
      var f;
      if (-3*pi/4 < angle && angle <= -pi/4) {
        // d
        f = (angle + 3*pi/4)/(pi/2);
        return xypic.Frame.Point(this.x + this.r - f * w, this.y + this.u);
      } else if (-pi/4 < angle && angle <= pi/4) {
        // r
        f = (angle + pi/4)/(pi/2);
        return xypic.Frame.Point(this.x - this.l, this.y + this.u - f * h);
      } else if (pi/4 < angle && angle <= 3*pi/4) {
        // u
        f = (angle - pi/4)/(pi/2);
        return xypic.Frame.Point(this.x - this.l + f * w, this.y - this.d);
      } else {
        // l
        f = (angle - (angle > 0? 3*pi/4 : -5*pi/4))/(pi/2);
        return xypic.Frame.Point(this.x + this.r, this.y - this.d + f * h);
      }
    },
    grow: function (xMargin, yMargin) {
      return this.toRect({
        l:Math.max(0, this.l + xMargin),
        r:Math.max(0, this.r + xMargin),
        u:Math.max(0, this.u + yMargin),
        d:Math.max(0, this.d + yMargin)
      });
    },
    toSize: function (width, height) {
      var u, d, r, l;
      var ow = this.l + this.r;
      var oh = this.u + this.d;
      if (ow === 0) {
        l = width / 2;
        r = width / 2;
      } else {
        l = width * this.l / ow;
        r = width * this.r / ow;
      }
      if (oh === 0) {
        u = height / 2;
        d = height / 2;
      } else {
        u = height * this.u / oh;
        d = height * this.d / oh;
      }
      return this.toRect({ l:l, r:r, u:u, d:d });
    },
    growTo: function (width, height) {
      var u = this.u;
      var d = this.d;
      var r = this.r;
      var l = this.l;
      var ow = l + r;
      var oh = u + d;
      if (width > ow) {
        if (ow === 0) {
          l = width / 2;
          r = width / 2;
        } else {
          l = width * this.l / ow;
          r = width * this.r / ow;
        }
      }
      if (height > oh) {
        if (oh === 0) {
          u = height / 2;
          d = height / 2;
        } else {
          u = height * this.u / oh;
          d = height * this.d / oh;
        }
      }
      return this.toRect({ l:l, r:r, u:u, d:d });
    },
    shrinkTo: function (width, height) {
      var u = this.u;
      var d = this.d;
      var r = this.r;
      var l = this.l;
      var ow = l + r;
      var oh = u + d;
      if (width < ow) {
        if (ow === 0) {
          l = width / 2;
          r = width / 2;
        } else {
          l = width * this.l / ow;
          r = width * this.r / ow;
        }
      }
      if (height < oh) {
        if (oh === 0) {
          u = height / 2;
          d = height / 2;
        } else {
          u = height * this.u / oh;
          d = height * this.d / oh;
        }
      }
      
      return this.toRect({ l:l, r:r, u:u, d:d });
    },
    move: function (x, y) {
      return xypic.Frame.Rect(x, y, { l:this.l, r:this.r, u:this.u, d:this.d });
    },
    shiftFrame: function (dx, dy) {
      return xypic.Frame.Rect(this.x, this.y, {
        l:Math.max(0, this.l - dx),
        r:Math.max(0, this.r + dx),
        u:Math.max(0, this.u + dy),
        d:Math.max(0, this.d - dy)
      });
    },
    rotate: function (angle) {
      var c = Math.cos(angle), s = Math.sin(angle);
      var lx = -this.l, rx = this.r, uy = this.u, dy = -this.d;
      var lu = {x:lx*c-uy*s, y:lx*s+uy*c};
      var ld = {x:lx*c-dy*s, y:lx*s+dy*c};
      var ru = {x:rx*c-uy*s, y:rx*s+uy*c};
      var rd = {x:rx*c-dy*s, y:rx*s+dy*c};
      return this.toRect({
        l:-Math.min(lu.x, ld.x, ru.x, rd.x),
        r:Math.max(lu.x, ld.x, ru.x, rd.x),
        u:Math.max(lu.y, ld.y, ru.y, rd.y),
        d:-Math.min(lu.y, ld.y, ru.y, rd.y)
      });
    },
    contains: function (point) {
      var x = point.x;
      var y = point.y;
      return (x >= this.x - this.l) && (x <= this.x + this.r) && (y >= this.y - this.d) && (y <= this.y + this.u);
    },
    toString: function () {
      return "{x:"+this.x+", y:"+this.y+", l:"+this.l+", r:"+this.r+", u:"+this.u+", d:"+this.d+"}";
    }
  });
  
  xypic.Frame.Ellipse = xypic.Frame.Subclass({
    Init: function (x, y, l, r, u, d) {
      this.x = x;
      this.y = y;
      this.l = l;
      this.r = r;
      this.u = u;
      this.d = d;
    },
    isPoint: function () { return this.r === 0 && this.l ===0 || this.u === 0 && this.d ===0; },
    isRect: function () { return false; },
    isCircle: function () { return !this.isPoint(); },
    isPerfectCircle: function () {
      return this.l === this.r && this.l === this.u && this.l === this.d;
    },
    edgePoint: function (x, y) {
      if (this.isPoint()) {
        return this;
      }
      if (this.isPerfectCircle()) {
        var dx = x - this.x;
        var dy = y - this.y;
        var angle;
        if (Math.abs(dx) < AST.xypic.machinePrecision && Math.abs(dy) < AST.xypic.machinePrecision) {
          angle = -Math.PI/2;
        } else {
          angle = Math.atan2(dy, dx);
        }
        return xypic.Frame.Point(this.x + this.r * Math.cos(angle), this.y + this.r * Math.sin(angle));
      } else {
        // ellipse
        var pi = Math.PI;
        var l = this.l;
        var r = this.r;
        var u = this.u;
        var d = this.d;
        var x0 = this.x;
        var y0 = this.y;
        var cx = x0 + (r - l) / 2;
        var cy = y0 + (u - d) / 2;
        var rx = (l + r) / 2;
        var ry = (u + d) / 2;
        
        var dx = x - x0;
        var dy = y - y0;
        var a0 = dy;
        var b0 = -dx;
        var c0 = dx * y0 - dy * x0;
        var a = a0 * rx;
        var b = b0 * ry;
        var c = c0 * rx + (rx - ry) * b0 * cy;
        var aabb = a * a + b * b;
        var d = a * cx + b * cy + c;
        var e = -d / aabb;
        var ff = aabb * rx * rx - d * d;
        if (ff < 0) {
          return xypic.Frame.Point(this.x, this.y - this.d);
        }
        var f = Math.sqrt(ff) / aabb;
        
        var xp = a * e + b * f + cx;
        var yp = b * e - a * f + cy;
        var xm = a * e - b * f + cx;
        var ym = b * e + a * f + cy;
        
        var eps = ry / rx;
        var xp0 = xp;
        var yp0 = eps * (yp - cy) + cy;
        var xm0 = xm;
        var ym0 = eps * (ym - cy) + cy;
        
        var sign = xypic.Util.sign;
        
        if (sign(xp0 - cx) === sign(x - cx) && sign(yp0 - cy) === sign(y - cy)) {
          return xypic.Frame.Point(xp0, yp0);
        } else {
          return xypic.Frame.Point(xm0, ym0);
        }
      }
    },
    proportionalEdgePoint: function (x, y) {
      if (this.isPoint()) {
        return this;
      }
      if (this.isPerfectCircle()) {
        var dx = x - this.x;
        var dy = y - this.y;
        var angle;
        if (Math.abs(dx) < AST.xypic.machinePrecision && Math.abs(dy) < AST.xypic.machinePrecision) {
          angle = -Math.PI/2;
        } else {
          angle = Math.atan2(dy, dx);
        }
        return xypic.Frame.Point(this.x - this.r * Math.cos(angle), this.y - this.r * Math.sin(angle));
      } else {
        // ellipse
        var pi = Math.PI;
        var l = this.l;
        var r = this.r;
        var u = this.u;
        var d = this.d;
        var x0 = this.x;
        var y0 = this.y;
        var cx = x0 + (r - l) / 2;
        var cy = y0 + (u - d) / 2;
        var rx = (l + r) / 2;
        var ry = (u + d) / 2;
        
        var dx = x - x0;
        var dy = y - y0;
        var a0 = dy;
        var b0 = -dx;
        var c0 = dx * y0 - dy * x0;
        var a = a0 * rx;
        var b = b0 * ry;
        var c = c0 * rx + (rx - ry) * b0 * cy;
        var aabb = a * a + b * b;
        var d = a * cx + b * cy + c;
        var e = -d / aabb;
        var ff = aabb * rx * rx - d * d;
        if (ff < 0) {
          return xypic.Frame.Point(this.x, this.y - this.d);
        }
        var f = Math.sqrt(ff) / aabb;
        
        var xp = a * e + b * f + cx;
        var yp = b * e - a * f + cy;
        var xm = a * e - b * f + cx;
        var ym = b * e + a * f + cy;
        
        var eps = ry / rx;
        var xp0 = xp;
        var yp0 = eps * (yp - cy) + cy;
        var xm0 = xm;
        var ym0 = eps * (ym - cy) + cy;
        
        var dxp = xp0 - x;
        var dyp = yp0 - y;
        var dxm = xm0 - x;
        var dym = ym0 - y;
        
        if (sign(xp0 - cx) === sign(x - cx) && sign(yp0 - cy) === sign(y - cy)) {
          return xypic.Frame.Point(xm0, ym0);
        } else {
          return xypic.Frame.Point(xp0, yp0);
        }
      }
    },
    grow: function (xMargin, yMargin) {
      return xypic.Frame.Ellipse(
        this.x, this.y, 
        Math.max(0, this.l + xMargin), 
        Math.max(0, this.r + xMargin), 
        Math.max(0, this.u + yMargin), 
        Math.max(0, this.d + yMargin));
    },
    toSize: function (width, height) {
      var u, d, r, l;
      var ow = this.l + this.r;
      var oh = this.u + this.d;
      if (ow === 0) {
        l = width / 2;
        r = width / 2;
      } else {
        l = width * this.l / ow;
        r = width * this.r / ow;
      }
      if (oh === 0) {
        u = height / 2;
        d = height / 2;
      } else {
        u = height * this.u / oh;
        d = height * this.d / oh;
      }
      
      return xypic.Frame.Ellipse(this.x, this.y, l, r, u, d);
    },
    growTo: function (width, height) {
      var u = this.u;
      var d = this.d;
      var r = this.r;
      var l = this.l;
      var ow = l + r;
      var oh = u + d;
      if (width > ow) {
        if (ow === 0) {
          l = width / 2;
          r = width / 2;
        } else {
          l = width * this.l / ow;
          r = width * this.r / ow;
        }
      }
      if (height > oh) {
        if (oh === 0) {
          u = height / 2;
          d = height / 2;
        } else {
          u = height * this.u / oh;
          d = height * this.d / oh;
        }
      }
      
      return xypic.Frame.Ellipse(this.x, this.y, l, r, u, d);
    },
    shrinkTo: function (width, height) {
      var u = this.u;
      var d = this.d;
      var r = this.r;
      var l = this.l;
      var ow = l + r;
      var oh = u + d;
      if (width < ow) {
        if (ow === 0) {
          l = width / 2;
          r = width / 2;
        } else {
          l = width * this.l / ow;
          r = width * this.r / ow;
        }
      }
      if (height < oh) {
        if (oh === 0) {
          u = height / 2;
          d = height / 2;
        } else {
          u = height * this.u / oh;
          d = height * this.d / oh;
        }
      }
      
      return xypic.Frame.Ellipse(this.x, this.y, l, r, u, d);
    },
    move: function (x, y) {
      return xypic.Frame.Ellipse(x, y, this.l, this.r, this.u, this.d);
    },
    shiftFrame: function (dx, dy) {
      return xypic.Frame.Ellipse(this.x, this.y, 
        Math.max(0, this.l - dx),
        Math.max(0, this.r + dx),
        Math.max(0, this.u + dy),
        Math.max(0, this.d - dy)
      );
    },
    rotate: function (angle) {
      return this;
    },
    contains: function (point) {
      var x = point.x;
      var y = point.y;
      if (this.isPoint()) {
        return false;
      }
      var l = this.l;
      var r = this.r;
      var u = this.u;
      var d = this.d;
      var x0 = this.x;
      var y0 = this.y;
      var cx = x0 + (r - l) / 2;
      var cy = y0 + (u - d) / 2;
      var rx = (l + r) / 2;
      var ry = (u + d) / 2;
      
      var eps = ry / rx;
      var dx = x - cx;
      var dy = (y - cy) / eps;
      
      return dx * dx + dy * dy <= rx * rx;
    },
    toString: function () {
      return "{x:" + this.x + ", y:" + this.y + ", l:" + this.l + ", r:" + this.r + ", u:" + this.u + ", d:" + this.d + "}";
    }
  });
  
  xypic.Range = MathJax.Object.Subclass({
    Init: function (start, end) {
      if (start > end) {
        this.start = end;
        this.end = start;
      } else {
        this.start = start;
        this.end = end;
      }
    },
    /**
     * returns difference ranges between this range and a given range: this range \ a given range.
     */
    difference: function (range) {
      var diff = FP.List.empty;
      var a0 = this.start;
      var a1 = this.end;
      var b0 = range.start;
      var b1 = range.end;
      if (a1 <= b0) {
        // a0 < a1 <= b0 < b1
        diff = diff.prepend(this);
      } else if (b1 <= a0) {
        // b0 < b1 <= a0 < a1
        diff = diff.prepend(this);
      } else if (a0 < b0) {
        if (a1 <= b1) {
          // a0 < b0 <= a1 <= b1
          diff = diff.prepend(xypic.Range(a0, b0));
        } else {
          // a0 < b0 < b1 < a1
          diff = diff.prepend(xypic.Range(a0, b0));
          diff = diff.prepend(xypic.Range(b1, a1));
        }
      } else /* if (b0 <= a0) */ {
        if (b1 < a1) {
          // b0 <= a0 <= b1 < a1
          diff = diff.prepend(xypic.Range(b1, a1));
        } /* else {
          // b0 <= a0 < a1 <= b1
        } */
      }
      return diff;
    },
    differenceRanges: function (ranges) {
      var result = FP.List.empty.prepend(this);
      ranges.foreach(function (range) {
        result = result.flatMap(function (remaining) {
          return remaining.difference(range);
        });
      });
      return result;
    },
    toString: function () {
      return "[" + this.start + ", " + this.end + "]";
    }
  });
  
  xypic.Shape = MathJax.Object.Subclass({
    // <<interface>>
    /**
     * 図形を描画する。
     * @param {xypic.Graphics.SVG} svg SVG
     */
    // draw: function (svg) {}
    
    /**
     * Bounding Boxを返す。
     * @returns {xypic.Frame.Rect} Bounding Box (ない場合はundefined)
     */
    // getBoundingBox: function () {}
    
    /**
     * 中身が空であるかどうかを返す。
     * @returns {boolean} true:空である、false:空でない
     */
    isNone: false
  });
  
  xypic.Shape.NoneShape = xypic.Shape.Subclass({
    draw: function (svg) {
    },
    getBoundingBox: function () {
      return undefined;
    },
    toString: function () {
      return "NoneShape";
    },
    isNone: true
  });
  
  xypic.Shape.Augment({}, {
    none: xypic.Shape.NoneShape()
  });
  
  xypic.Shape.InvisibleBoxShape = xypic.Shape.Subclass({
    Init: function (bbox) {
      this.bbox = bbox;
    },
    draw: function (svg) {
    },
    getBoundingBox: function () {
      return this.bbox;
    },
    toString: function () {
      return "InvisibleBoxShape[bbox:" + this.bbox.toString() + "]";
    }
  });
  
  xypic.Shape.TranslateShape = xypic.Shape.Subclass({
    Init: function (dx, dy, shape) {
      this.dx = dx;
      this.dy = dy;
      this.shape = shape;
      memoize(this, "getBoundingBox");
    },
    draw: function (svg) {
      var g = svg.createGroup(svg.transformBuilder().translate(this.dx, this.dy));
      this.shape.draw(g);
    },
    getBoundingBox: function () {
      var bbox = this.shape.getBoundingBox();
      if (bbox === undefined) {
        return undefined;
      }
      return xypic.Frame.Rect(bbox.x + this.dx, bbox.y + this.dy, bbox);
    },
    toString: function () {
      return "TranslateShape[dx:" + this.dx + ", dy:" + this.dy + ", shape:" + this.shape.toString() + "]";
    }
  });
  
  xypic.Shape.CompositeShape = xypic.Shape.Subclass({
    Init: function (foregroundShape, backgroundShape) {
      this.foregroundShape = foregroundShape;
      this.backgroundShape = backgroundShape;
      memoize(this, "getBoundingBox");
    },
    draw: function (svg) {
      this.backgroundShape.draw(svg);
      this.foregroundShape.draw(svg);
    },
    getBoundingBox: function () {
      return xypic.Frame.combineRect(this.foregroundShape.getBoundingBox(), this.backgroundShape.getBoundingBox());
    },
    toString: function () {
      return "(" + this.foregroundShape.toString() + ", " + this.backgroundShape.toString() + ")";
    }
  });
  
  xypic.Shape.ChangeColorShape = xypic.Shape.Subclass({
    Init: function (color, shape) {
      this.color = color;
      this.shape = shape;
      memoize(this, "getBoundingBox");
    },
    draw: function (svg) {
      var g = svg.createChangeColorGroup(this.color);
      this.shape.draw(g);
    },
    getBoundingBox: function () {
      return this.shape.getBoundingBox();
    },
    toString: function () {
      return "" + this.shape + ", color:" + this.color;
    }
  });
  
  xypic.Shape.CircleSegmentShape = xypic.Shape.Subclass({
    Init: function (x, y, sx, sy, r, large, flip, ex, ey) {
      this.x = x;
      this.y = y;
      this.sx = sx;
      this.sy = sy;
      this.r = r;
      this.large = large;
      this.flip = flip;
      this.ex = ex;
      this.ey = ey;
      memoize(this, "getBoundingBox");
    },
    draw: function (svg) {
      svg.createSVGElement("path", {
        d:"M" + xypic.em2px(this.sx) + "," + xypic.em2px(-this.sy) + " A" + xypic.em2px(this.r) + "," + xypic.em2px(this.r) + " 0 " + this.large + "," + this.flip + " " + xypic.em2px(this.ex) + "," + xypic.em2px(-this.ey)
      });
    },
    getBoundingBox: function () {
      return xypic.Frame.Ellipse(this.x, this.y, this.r, this.r, this.r, this.r);
    },
    toString: function () {
      return "CircleSegmentShape[x:" + this.x + ", y:" + this.y + ", sx:" + this.sx + ", sy:" + this.sy + ", r:" + this.r + ", large:" + this.large + ", flip:" + this.flip + ", ex:" + this.ex + ", ey:" + this.ey + "]";
    }
  });
  
  xypic.Shape.FullCircleShape = xypic.Shape.Subclass({
    Init: function (x, y, r) {
      this.x = x;
      this.y = y;
      this.r = r;
      memoize(this, "getBoundingBox");
    },
    draw: function (svg) {
      svg.createSVGElement("circle", {
        cx:xypic.em2px(this.x), cy:xypic.em2px(-this.y), r:xypic.em2px(this.r)
      });
    },
    getBoundingBox: function () {
      return xypic.Frame.Ellipse(this.x, this.y, this.r, this.r, this.r, this.r);
    },
    toString: function () {
      return "FullCircleShape[x:" + this.x + ", y:" + this.y + ", r:" + this.r + "]";
    }
  });
  
  xypic.Shape.RectangleShape = xypic.Shape.Subclass({
    Init: function (x, y, left, right, up, down, r, isDoubled, color, dasharray, fillColor, hideLine) {
      this.x = x;
      this.y = y;
      this.left = left;
      this.right = right;
      this.up = up;
      this.down = down;
      this.r = r;
      this.isDoubled = isDoubled;
      this.color = color;
      this.dasharray = dasharray;
      this.fillColor = fillColor;
      this.hideLine = hideLine || false;
      memoize(this, "getBoundingBox");
    },
    draw: function (svg) {
      var def;
      def = {
        x:xypic.em2px(this.x - this.left), 
        y:-xypic.em2px(this.y + this.up), 
        width:xypic.em2px(this.left + this.right), 
        height:xypic.em2px(this.up + this.down), 
        rx:xypic.em2px(this.r)
      };
      if (this.dasharray !== undefined) {
        def["stroke-dasharray"] = this.dasharray;
      }
      if (this.hideLine) {
        def["stroke"] = "none";
      } else if (this.color !== undefined) {
        def["stroke"] = this.color;
      }
      if (this.fillColor !== undefined) {
        def["fill"] = this.fillColor;
      }
      svg.createSVGElement("rect", def);
      if (this.isDoubled) {
        def = {
          x:xypic.em2px(this.x - this.left + AST.xypic.thickness), 
          y:-xypic.em2px(this.y + this.up - AST.xypic.thickness), 
          width:xypic.em2px(this.left + this.right - 2 * AST.xypic.thickness), 
          height:xypic.em2px(this.up + this.down - 2 * AST.xypic.thickness), 
          rx:xypic.em2px(Math.max(this.r - AST.xypic.thickness, 0))
        };
        if (this.dasharray !== undefined) {
          def["stroke-dasharray"] = this.dasharray;
        }
        if (this.hideLine) {
          def["stroke"] = "none";
        } else if (this.color !== undefined) {
          def["stroke"] = this.color;
        }
        if (this.fillColor !== undefined) {
          def["fill"] = this.fillColor;
        }
        svg.createSVGElement("rect", def);
      }
    },
    getBoundingBox: function () {
      return xypic.Frame.Rect(this.x, this.y, { l:this.left, r:this.right, u:this.up, d:this.down });
    },
    toString: function () {
      return "RectangleShape[x:" + this.x + ", y:" + this.y + ", left:" + this.left + ", right:" + this.right + ", up:" + this.up + ", down:" + this.down + ", r:" + this.r + ", isDouble:" + this.isDouble + ", dasharray:" + this.dasharray + "]";
    }
  });
  
  xypic.Shape.EllipseShape = xypic.Shape.Subclass({
    Init: function (x, y, rx, ry, isDoubled, color, dasharray, fillColor, hideLine) {
      this.x = x;
      this.y = y;
      this.rx = rx;
      this.ry = ry;
      this.isDoubled = isDoubled;
      this.color = color;
      this.dasharray = dasharray;
      this.fillColor = fillColor;
      this.hideLine = hideLine || false;
      memoize(this, "getBoundingBox");
    },
    draw: function (svg) {
      var def;
      def = {
        cx:xypic.em2px(this.x), 
        cy:-xypic.em2px(this.y), 
        rx:xypic.em2px(this.rx), 
        ry:xypic.em2px(this.ry)
      };
      if (this.dasharray !== undefined) {
        def["stroke-dasharray"] = this.dasharray;
      }
      if (this.hideLine) {
        def["stroke"] = "none";
      } else if (this.color !== undefined) {
        def["stroke"] = this.color;
      }
      if (this.fillColor !== undefined) {
        def["fill"] = this.fillColor;
      }
      svg.createSVGElement("ellipse", def);
      if (this.isDoubled) {
        def = {
          cx:xypic.em2px(this.x), 
          cy:-xypic.em2px(this.y), 
          rx:xypic.em2px(Math.max(this.rx - AST.xypic.thickness)), 
          ry:xypic.em2px(Math.max(this.ry - AST.xypic.thickness))
        };
        if (this.dasharray !== undefined) {
          def["stroke-dasharray"] = this.dasharray;
        }
        if (this.hideLine) {
          def["stroke"] = "none";
        } else if (this.color !== undefined) {
          def["stroke"] = this.color;
        }
        if (this.fillColor !== undefined) {
          def["fill"] = this.fillColor;
        }
        svg.createSVGElement("ellipse", def);
      }
    },
    getBoundingBox: function () {
      return xypic.Frame.Rect(this.x, this.y, { l:this.rx, r:this.rx, u:this.ry, d:this.ry });
    },
    toString: function () {
      return "EllipseShape[x:" + this.x + ", y:" + this.y + ", rx:" + this.rx + ", ry:" + this.ry + ", isDoubled:" + this.isDoubled + ", dasharray:" + this.dasharray + "]";
    }
  });
  
  xypic.Shape.BoxShadeShape = xypic.Shape.Subclass({
    Init: function (x, y, left, right, up, down, depth, color) {
      this.x = x;
      this.y = y;
      this.left = left;
      this.right = right;
      this.up = up;
      this.down = down;
      this.depth = depth;
      this.color = color || "currentColor";
      memoize(this, "getBoundingBox");
    },
    draw: function (svg) {
      var x = xypic.em2px(this.x);
      var y = xypic.em2px(this.y);
      var l = xypic.em2px(this.left);
      var r = xypic.em2px(this.right);
      var u = xypic.em2px(this.up);
      var d = xypic.em2px(this.down);
      var depth = xypic.em2px(this.depth);
      svg.createSVGElement("path", {
        d: "M" + (x - l + depth) + "," + (-y + d) + 
          "L" + (x + r) + "," + (-y + d) + 
          "L" + (x + r) + "," + (-y - u + depth) + 
          "L" + (x + r + depth) + "," + (-y - u + depth) + 
          "L" + (x + r + depth) + "," + (-y + d + depth) + 
          "L" + (x - l + depth) + "," + (-y + d + depth) + 
          "Z",
        stroke: this.color,
        fill: this.color
      });
    },
    getBoundingBox: function () {
      return xypic.Frame.Rect(this.x, this.y, { l:this.left, r:this.right + this.depth, u:this.up, d:this.down + this.depth });
    },
    toString: function () {
      return "RectangleShape[x:" + this.x + ", y:" + this.y + ", left:" + this.left + ", right:" + this.right + ", up:" + this.up + ", down:" + this.down + ", depth:" + this.depth + "]";
    }
  });
  
  xypic.Shape.LeftBrace = xypic.Shape.Subclass({
    Init: function (x, y, up, down, degree, color) {
      this.x = x;
      this.y = y;
      this.up = up;
      this.down = down;
      this.degree = degree;
      this.color = color || "currentColor";
      memoize(this, "getBoundingBox");
    },
    draw: function (svg) {
      var scale = xypic.oneem;
      var down = Math.max(0.759375 + 0.660375, this.down / scale * 1.125) - 0.660375;
      var up = - Math.max(0.759375 + 0.660375, this.up / scale * 1.125) + 0.660375;
      
      var d;
      d = "M" + xypic.em2px(-0.0675) + " " + xypic.em2px(down) + 
        "T" + xypic.em2px(-0.068625) + " " + xypic.em2px(0.07875 + down) + 
        "Q" + xypic.em2px(-0.068625) + " " + xypic.em2px(0.190125 + down) + 
        " " + xypic.em2px(-0.0585) + " " + xypic.em2px(0.250875 + down) + 
        "T" + xypic.em2px(-0.01125) + " " + xypic.em2px(0.387 + down) + 
        "Q" + xypic.em2px(0.07425) + " " + xypic.em2px(0.55575 + down) + 
        " " + xypic.em2px(0.2475) + " " + xypic.em2px(0.6525 + down) + 
        "L" + xypic.em2px(0.262125) + " " + xypic.em2px(0.660375 + down) + 
        "L" + xypic.em2px(0.3015) + " " + xypic.em2px(0.660375 + down) + 
        "L" + xypic.em2px(0.30825) + " " + xypic.em2px(0.653625 + down) + 
        "V" + xypic.em2px(0.622125 + down) + 
        "Q" + xypic.em2px(0.30825) + " " + xypic.em2px(0.60975 + down) + 
        " " + xypic.em2px(0.2925) + " " + xypic.em2px(0.60075 + down) + 
        "Q" + xypic.em2px(0.205875) + " " + xypic.em2px(0.541125 + down) + 
        " " + xypic.em2px(0.149625) + " " + xypic.em2px(0.44775 + down) + 
        "T" + xypic.em2px(0.07425) + " " + xypic.em2px(0.239625 + down) + 
        "Q" + xypic.em2px(0.07425) + " " + xypic.em2px(0.2385 + down) + 
        " " + xypic.em2px(0.073125) + " " + xypic.em2px(0.235125 + down) + 
        "Q" + xypic.em2px(0.068625) + " " + xypic.em2px(0.203625 + down) + 
        " " + xypic.em2px(0.0675) + " " + xypic.em2px(0.041625 + down) + 
        "L" + xypic.em2px(0.0675) + " " + xypic.em2px(0.75825) + 
        "Q" + xypic.em2px(0.0675) + " " + xypic.em2px(0.496125) + 
        " " + xypic.em2px(0.066375) + " " + xypic.em2px(0.486) + 
        "Q" + xypic.em2px(0.05625) + " " + xypic.em2px(0.336375) + 
        " " + xypic.em2px(-0.021375) + " " + xypic.em2px(0.212625) + 
        "T" + xypic.em2px(-0.226125) + " " + xypic.em2px(0.010125) + 
        "L" + xypic.em2px(-0.241875) + " 0" + 
        "L" + xypic.em2px(-0.226125) + " " + xypic.em2px(-0.010125) + 
        "Q" + xypic.em2px(-0.106875) + " " + xypic.em2px(-0.084375) + 
        " " + xypic.em2px(-0.025875) + " " + xypic.em2px(-0.207) + 
        "T" + xypic.em2px(0.066375) + " " + xypic.em2px(-0.486) + 
        "Q" + xypic.em2px(0.0675) + " " + xypic.em2px(-0.496125) + 
        " " + xypic.em2px(0.0675) + " " + xypic.em2px(-0.75825) + 
        "L" + xypic.em2px(0.0675) + " " + xypic.em2px(-0.041625 + up) + 
        "Q" + xypic.em2px(0.068625) + " " + xypic.em2px(-0.203625 + up) + 
        " " + xypic.em2px(0.073125) + " " + xypic.em2px(-0.235125 + up) + 
        "Q" + xypic.em2px(0.07425) + " " + xypic.em2px(-0.2385 + up) + 
        " " + xypic.em2px(0.07425) + " " + xypic.em2px(-0.239625 + up) + 
        "Q" + xypic.em2px(0.093375) + " " + xypic.em2px(-0.354375 + up) + 
        " " + xypic.em2px(0.149625) + " " + xypic.em2px(-0.44775 + up) + 
        "T" + xypic.em2px(0.2925) + " " + xypic.em2px(-0.60075 + up) + 
        "Q" + xypic.em2px(0.30825) + " " + xypic.em2px(-0.60975 + up) + 
        " " + xypic.em2px(0.30825) + " " + xypic.em2px(-0.622125 + up) + 
        "L" + xypic.em2px(0.30825) + " " + xypic.em2px(-0.653625 + up) + 
        "L" + xypic.em2px(0.3015) + " " + xypic.em2px(-0.660375 + up) + 
        "L" + xypic.em2px(0.262125) + " " + xypic.em2px(-0.660375 + up) + 
        "L" + xypic.em2px(0.2475) + " " + xypic.em2px(-0.6525 + up) + 
        "Q" + xypic.em2px(0.07425) + " " + xypic.em2px(-0.55575 + up) + 
        " " + xypic.em2px(-0.01125) + " " + xypic.em2px(-0.387 + up) + 
        "Q" + xypic.em2px(-0.048375) + " " + xypic.em2px(-0.311625 + up) + 
        " " + xypic.em2px(-0.0585) + " " + xypic.em2px(-0.250875 + up) + 
        "T" + xypic.em2px(-0.068625) + " " + xypic.em2px(-0.07875 + up) + 
        "Q" + xypic.em2px(-0.0675) + " " + xypic.em2px(up) + 
        " " + xypic.em2px(-0.0675) + " " + xypic.em2px(up) + 
        "L" + xypic.em2px(-0.0675) + " " + xypic.em2px(-0.759375) + 
        "V" + xypic.em2px(-0.5985) + 
        "Q" + xypic.em2px(-0.0675) + " " + xypic.em2px(-0.47925) + 
        " " + xypic.em2px(-0.075375) + " " + xypic.em2px(-0.41175) + 
        "T" + xypic.em2px(-0.11475) + " " + xypic.em2px(-0.27) + 
        "Q" + xypic.em2px(-0.133875) + " " + xypic.em2px(-0.2205) + 
        " " + xypic.em2px(-0.160875) + " " + xypic.em2px(-0.17775) + 
        "T" + xypic.em2px(-0.212625) + " " + xypic.em2px(-0.106875) + 
        "T" + xypic.em2px(-0.25875) + " " + xypic.em2px(-0.06075) + 
        "T" + xypic.em2px(-0.293625) + " " + xypic.em2px(-0.0315) + 
        "T" + xypic.em2px(-0.307125) + " " + xypic.em2px(-0.02025) + 
        "Q" + xypic.em2px(-0.30825) + " " + xypic.em2px(-0.019125) + 
        " " + xypic.em2px(-0.30825) + " 0" + 
        "T" + xypic.em2px(-0.307125) + " " + xypic.em2px(0.02025) + 
        "Q" + xypic.em2px(-0.307125) + " " + xypic.em2px(0.021375) + 
        " " + xypic.em2px(-0.284625) + " " + xypic.em2px(0.03825) + 
        "T" + xypic.em2px(-0.2295) + " " + xypic.em2px(0.091125) + 
        "T" + xypic.em2px(-0.162) + " " + xypic.em2px(0.176625) + 
        "T" + xypic.em2px(-0.10125) + " " + xypic.em2px(0.30825) + 
        "T" + xypic.em2px(-0.068625) + " " + xypic.em2px(0.482625) + 
        "Q" + xypic.em2px(-0.0675) + " " + xypic.em2px(0.496125) + 
        " " + xypic.em2px(-0.0675) + " " + xypic.em2px(0.759375) + 
        "Z";
      svg.createSVGElement("path", {
        d:d, 
        fill:this.color, 
        stroke:this.color, 
        "stroke-width":"0pt", 
        transform:"translate(" + xypic.em2px(this.x) + "," + xypic.em2px(-this.y) +") rotate(" + (-this.degree) + ") scale(" + (scale / 1.125) + ")"
      });
    },
    getBoundingBox: function () {
      var scale = xypic.oneem;
      return xypic.Frame.Rect(this.x, this.y, { l:0.274 * scale, r:0.274 * scale, u:Math.max((0.759375 + 0.660375) * scale / 1.125, this.up), d:Math.max((0.759375 + 0.660375) * scale / 1.125, this.down) }).rotate(this.degree * Math.PI / 180);
    },
    toString: function () {
      return "LeftBrace[x:" + this.x + ", y:" + this.y + ", up:" + this.up + ", down:" + this.down + "]";
    }
  });
  
  xypic.Shape.LeftParenthesis = xypic.Shape.Subclass({
    Init: function (x, y, height, degree, color) {
      this.x = x;
      this.y = y;
      this.height = height;
      this.degree = degree;
      this.color = color || "currentColor";
      memoize(this, "getBoundingBox");
    },
    draw: function (svg) {
      var scale = xypic.oneem;
      var down = Math.max(0.660375, this.height / 2 / scale * 1.125) - 0.660375;
      var up = -down;
      
      var d;
      d = "M" + xypic.em2px(-0.0675) + " " + xypic.em2px(down) + 
        "T" + xypic.em2px(-0.068625) + " " + xypic.em2px(0.07875 + down) + 
        "Q" + xypic.em2px(-0.068625) + " " + xypic.em2px(0.190125 + down) + 
        " " + xypic.em2px(-0.0585) + " " + xypic.em2px(0.250875 + down) + 
        "T" + xypic.em2px(-0.01125) + " " + xypic.em2px(0.387 + down) + 
        "Q" + xypic.em2px(0.07425) + " " + xypic.em2px(0.55575 + down) + 
        " " + xypic.em2px(0.2475) + " " + xypic.em2px(0.6525 + down) + 
        "L" + xypic.em2px(0.262125) + " " + xypic.em2px(0.660375 + down) + 
        "L" + xypic.em2px(0.3015) + " " + xypic.em2px(0.660375 + down) + 
        "L" + xypic.em2px(0.30825) + " " + xypic.em2px(0.653625 + down) + 
        "V" + xypic.em2px(0.622125 + down) + 
        "Q" + xypic.em2px(0.30825) + " " + xypic.em2px(0.60975 + down) + 
        " " + xypic.em2px(0.2925) + " " + xypic.em2px(0.60075 + down) + 
        "Q" + xypic.em2px(0.205875) + " " + xypic.em2px(0.541125 + down) + 
        " " + xypic.em2px(0.149625) + " " + xypic.em2px(0.44775 + down) + 
        "T" + xypic.em2px(0.07425) + " " + xypic.em2px(0.239625 + down) + 
        "Q" + xypic.em2px(0.07425) + " " + xypic.em2px(0.2385 + down) + 
        " " + xypic.em2px(0.073125) + " " + xypic.em2px(0.235125 + down) + 
        "Q" + xypic.em2px(0.068625) + " " + xypic.em2px(0.203625 + down) + 
        " " + xypic.em2px(0.0675) + " " + xypic.em2px(0.041625 + down) + 
        "L" + xypic.em2px(0.0675) + " " + xypic.em2px(-0.041625 + up) + 
        "Q" + xypic.em2px(0.068625) + " " + xypic.em2px(-0.203625 + up) + 
        " " + xypic.em2px(0.073125) + " " + xypic.em2px(-0.235125 + up) + 
        "Q" + xypic.em2px(0.07425) + " " + xypic.em2px(-0.2385 + up) + 
        " " + xypic.em2px(0.07425) + " " + xypic.em2px(-0.239625 + up) + 
        "Q" + xypic.em2px(0.093375) + " " + xypic.em2px(-0.354375 + up) + 
        " " + xypic.em2px(0.149625) + " " + xypic.em2px(-0.44775 + up) + 
        "T" + xypic.em2px(0.2925) + " " + xypic.em2px(-0.60075 + up) + 
        "Q" + xypic.em2px(0.30825) + " " + xypic.em2px(-0.60975 + up) + 
        " " + xypic.em2px(0.30825) + " " + xypic.em2px(-0.622125 + up) + 
        "L" + xypic.em2px(0.30825) + " " + xypic.em2px(-0.653625 + up) + 
        "L" + xypic.em2px(0.3015) + " " + xypic.em2px(-0.660375 + up) + 
        "L" + xypic.em2px(0.262125) + " " + xypic.em2px(-0.660375 + up) + 
        "L" + xypic.em2px(0.2475) + " " + xypic.em2px(-0.6525 + up) + 
        "Q" + xypic.em2px(0.07425) + " " + xypic.em2px(-0.55575 + up) + 
        " " + xypic.em2px(-0.01125) + " " + xypic.em2px(-0.387 + up) + 
        "Q" + xypic.em2px(-0.048375) + " " + xypic.em2px(-0.311625 + up) + 
        " " + xypic.em2px(-0.0585) + " " + xypic.em2px(-0.250875 + up) + 
        "T" + xypic.em2px(-0.068625) + " " + xypic.em2px(-0.07875 + up) + 
        "Q" + xypic.em2px(-0.0675) + " " + xypic.em2px(up) + 
        " " + xypic.em2px(-0.0675) + " " + xypic.em2px(up) + 
        "Z";
      svg.createSVGElement("path", {
        d:d, 
        fill:this.color, 
        stroke:this.color, 
        "stroke-width":"0pt", 
        transform:"translate(" + xypic.em2px(this.x) + "," + xypic.em2px(-this.y) +") rotate(" + (-this.degree) + ") scale(" + (scale / 1.125) + ")"
      });
    },
    getBoundingBox: function () {
      var scale = xypic.oneem;
      return xypic.Frame.Rect(this.x, this.y, { l:0.06 * scale, r:0.274 * scale, u:Math.max(0.660375 * scale / 1.125, this.height / 2), d:Math.max(0.660375 * scale / 1.125, this.height / 2) }).rotate(this.degree * Math.PI / 180);
    },
    toString: function () {
      return "LeftBrace[x:" + this.x + ", y:" + this.y + ", up:" + this.up + ", down:" + this.down + "]";
    }
  });
  
  xypic.Shape.TextShape = xypic.Shape.Subclass({
    Init: function (c, math, svgForTestLayout) {
      this.c = c;
      this.math = math;
      this.svgForTestLayout = svgForTestLayout;
      this.originalBBox = undefined;
      memoize(this, "getBoundingBox");
      memoize(this, "getOriginalReferencePoint");
    },
    draw: function (svg) {
      this._draw(svg, false);
    },
    getBoundingBox: function () {
      return this._draw(this.svgForTestLayout, true);
    },
    getOriginalReferencePoint: function () {
      this.getBoundingBox();
      var originalBBox = this.originalBBox;
      
      var c = this.c;
      var H = originalBBox.H;
      var D = originalBBox.D;
      return xypic.Frame.Point(c.x, c.y - (H - D) / 2);
    },
    toString: function () {
      return "TextShape[c:" + this.c.toString() + ", math:" + this.math.toString() + "]";
    }
  });
  
  xypic.Shape.ImageShape = xypic.Shape.Subclass({
    Init: function (c, url) {
      this.c = c;
      this.url = url;
      memoize(this, "getBoundingBox");
      memoize(this, "getOriginalReferencePoint");
    },
    draw: function (svg) {
      var c = this.c;
      svg.createSVGElement("image", {
        x: xypic.em2px(c.x - c.l),
        y: xypic.em2px(-c.y - c.u),
        width: xypic.em2px(c.l + c.r),
        height: xypic.em2px(c.u + c.d),
        preserveAspectRatio: "none",
        "xlink:href": this.url
      });
    },
    getBoundingBox: function () {
      return this.c;
    },
    getOriginalReferencePoint: function () {
      return this.c;
    },
    toString: function () {
      return "ImageShape[c:" + this.c.toString() + ", height:" + this.height + ", width:" + this.width + ", url:" + this.url + "]";
    }
  });
  
  xypic.Shape.ArrowheadShape = xypic.Shape.Subclass({
    draw: function (svg) {
      var g = svg.createGroup(svg.transformBuilder().translate(this.c.x, this.c.y).rotateRadian(this.angle));
      this.drawDelegate(g);
    },
    getBoundingBox: function () {
      return this.c.toRect(this.getBox()).rotate(this.angle);
    },
    toString: function () {
      return "ArrowheadShape[c:" + this.c.toString() + ", angle:" + this.angle + "]";
    }
  });
  
  // @2{>}
  xypic.Shape.GT2ArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { var scale = xypic.oneem; return { l:0.456 * scale, r:0, d:0.229 * scale, u:0.229 * scale }; },
    getRadius: function () {
      var scale = xypic.oneem;
      return 0.213 * scale;
    },
    drawDelegate: function (svg) {
      var scale = xypic.oneem;
      var gu = svg.createGroup(svg.transformBuilder().rotateDegree(-10));
      var gd = svg.createGroup(svg.transformBuilder().rotateDegree(10));
      gu.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(-0.222 * scale) + "," + xypic.em2px(-0.020 * scale) + " " + xypic.em2px(-0.489 * scale) + "," + xypic.em2px(-0.147 * scale)
      });
      gd.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(-0.222 * scale) + ","+xypic.em2px(0.020 * scale) + " " + xypic.em2px(-0.489 * scale) + "," + xypic.em2px(0.147 * scale)
      });
    }
  });
  
  // @3{>}
  xypic.Shape.GT3ArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { var scale = xypic.oneem; return { l:0.507 * scale, r:0, d:0.268 * scale, u:0.268 * scale }; }, 
    getRadius: function () {
      var scale = xypic.oneem;
      return 0.325 * scale;
    },
    drawDelegate: function (svg) {
      var scale = xypic.oneem;
      var gu = svg.createGroup(svg.transformBuilder().rotateDegree(-15));
      var gd = svg.createGroup(svg.transformBuilder().rotateDegree(15));
      gu.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(-0.222 * scale) + "," + xypic.em2px(-0.020 * scale) + " " + xypic.em2px(-0.489 * scale) + "," + xypic.em2px(-0.147 * scale)
      });
      svg.createSVGElement("line", {
        x1:0, y1:0, x2:xypic.em2px(-0.507 * scale), y2:0
      });
      gd.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(-0.222 * scale) + "," + xypic.em2px(0.020 * scale) + " " + xypic.em2px(-0.489 * scale) + "," + xypic.em2px(0.147 * scale)
      });
    }
  });
  
  // @^{>}
  xypic.Shape.UpperGTArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { var scale = xypic.oneem; return { l:0.489 * scale, r:0, d:0, u:0.147 * scale }; }, 
    drawDelegate: function (svg) {
      var scale = xypic.oneem;
      svg.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(-0.222 * scale) + "," + xypic.em2px(-0.020 * scale) + " " + xypic.em2px(-0.489 * scale) + "," + xypic.em2px(-0.147 * scale)
      });
    }
  });
  
  // @_{>}
  xypic.Shape.LowerGTArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { var scale = xypic.oneem; return { l:0.489 * scale, r:0, d:0.147 * scale, u:0 }; },
    drawDelegate: function (svg) {
      var scale = xypic.oneem;
      svg.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(-0.222 * scale) + "," + xypic.em2px(0.020 * scale) + " " + xypic.em2px(-0.489 * scale) + "," + xypic.em2px(0.147 * scale)
      });
    }
  });
  
  // @{>}
  xypic.Shape.GTArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { var scale = xypic.oneem; return { l:0.489 * scale, r:0, d:0.147 * scale, u:0.147 * scale }; },
    drawDelegate: function (svg) {
      var scale = xypic.oneem;
      svg.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(-0.222 * scale) + "," + xypic.em2px(0.020 * scale) + " " + xypic.em2px(-0.489 * scale) + "," + xypic.em2px(0.147 * scale)
      });
      svg.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(-0.222 * scale) + "," + xypic.em2px(-0.020 * scale) + " " + xypic.em2px(-0.489 * scale) + "," + xypic.em2px(-0.147 * scale)
      });
    }
  });
  
  // @2{<}
  xypic.Shape.LT2ArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { var scale = xypic.oneem; return { l:0, r:0.456 * scale, d:0.229 * scale, u:0.229  * scale }; }, 
    getRadius: function () {
      var scale = xypic.oneem;
      return 0.213 * scale;
    },
    drawDelegate: function (svg) {
      var scale = xypic.oneem;
      var gu = svg.createGroup(svg.transformBuilder().rotateDegree(10)); 
      var gd = svg.createGroup(svg.transformBuilder().rotateDegree(-10));
      gu.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(0.222 * scale) + "," + xypic.em2px(-0.020 * scale) + " " + xypic.em2px(0.489 * scale) + "," + xypic.em2px(-0.147 * scale)
      });
      gd.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(0.222 * scale) + "," + xypic.em2px(0.020 * scale) + " " + xypic.em2px(0.489 * scale) + "," + xypic.em2px(0.147 * scale)
      });
    }
  });
  
  // @3{<}
  xypic.Shape.LT3ArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { var scale = xypic.oneem; return { l:0, r:0.507 * scale, d:0.268 * scale, u:0.268 * scale }; }, 
    getRadius: function () {
      var scale = xypic.oneem;
      return 0.325 * scale;
    },
    drawDelegate: function (svg) {
      var scale = xypic.oneem;
      var gu = svg.createGroup(svg.transformBuilder().rotateDegree(15));
      var gd = svg.createGroup(svg.transformBuilder().rotateDegree(-15));
      gu.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(0.222 * scale) + "," + xypic.em2px(-0.020 * scale) + " " + xypic.em2px(0.489 * scale) + "," + xypic.em2px(-0.147 * scale)
      });
      svg.createSVGElement("line", {
        x1:0, y1:0, x2:xypic.em2px(0.507 * scale), y2:0
      });
      gd.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(0.222 * scale) + "," + xypic.em2px(0.020 * scale) + " " + xypic.em2px(0.489 * scale) + "," + xypic.em2px(0.147 * scale)
      });
    }
  });
  
  // @^{<}
  xypic.Shape.UpperLTArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { var scale = xypic.oneem; return { l:0, r:0.489 * scale, d:0, u:0.147 * scale }; }, 
    drawDelegate: function (svg) {
      var scale = xypic.oneem;
      svg.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(0.222 * scale) + "," + xypic.em2px(-0.020 * scale) + " " + xypic.em2px(0.489 * scale) + "," + xypic.em2px(-0.147 * scale)
      });
    }
  });
  
  // @_{<}
  xypic.Shape.LowerLTArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { var scale = xypic.oneem; return { l:0, r:0.489 * scale, d:0.147 * scale, u:0 }; }, 
    drawDelegate: function (svg) {
      var scale = xypic.oneem;
      svg.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(0.222 * scale) + "," + xypic.em2px(0.020 * scale) + " " + xypic.em2px(0.489 * scale) + "," + xypic.em2px(0.147 * scale)
      });
    }
  });
  
  // @{<}
  xypic.Shape.LTArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { var scale = xypic.oneem; return { l:0, r:0.489 * scale, d:0.147 * scale, u:0.147 * scale }; }, 
    drawDelegate: function (svg) {
      var scale = xypic.oneem;
      svg.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(0.222 * scale) + "," + xypic.em2px(-0.020 * scale) + " " + xypic.em2px(0.489 * scale) + "," + xypic.em2px(-0.147 * scale)
      });
      svg.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(0.222 * scale) + "," + xypic.em2px(0.020 * scale) + " " + xypic.em2px(0.489 * scale) + "," + xypic.em2px(0.147 * scale)
      });
    }
  });
  
  // @^{|}
  xypic.Shape.UpperColumnArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { return { l:0, r:0, u:AST.xypic.lineElementLength, d:0 }; }, 
    drawDelegate: function (svg) {
      var l = xypic.em2px(AST.xypic.lineElementLength);
      svg.createSVGElement("line", {
        x1:0, y1:0, x2:0, y2:-l
      });
    }
  });
  
  // @_{|}
  xypic.Shape.LowerColumnArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { return { l:0, r:0, u:0, d:AST.xypic.lineElementLength }; }, 
    drawDelegate: function (svg) {
      var l = xypic.em2px(AST.xypic.lineElementLength);
      svg.createSVGElement("line", {
        x1:0, y1:0, x2:0, y2:l
      });
    }
  });
  
  // @2{|}
  xypic.Shape.Column2ArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { return { l:0, r:0, u:0.5 * (AST.xypic.lineElementLength + AST.xypic.thickness), d:0.5 * (AST.xypic.lineElementLength + AST.xypic.thickness) }; }, 
    drawDelegate: function (svg) {
      var l = xypic.em2px(0.5 * (AST.xypic.lineElementLength + AST.xypic.thickness));
      svg.createSVGElement("line", {
        x1:0, y1:l, x2:0, y2:-l
      });
    }
  });
  
  // @3{|}
  xypic.Shape.Column3ArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { return { l:0, r:0, u:0.5 * AST.xypic.lineElementLength + AST.xypic.thickness, d:0.5 * AST.xypic.lineElementLength + AST.xypic.thickness }; }, 
    drawDelegate: function (svg) {
      var l = xypic.em2px(0.5 * AST.xypic.lineElementLength + AST.xypic.thickness);
      svg.createSVGElement("line", {
        x1:0, y1:l, x2:0, y2:-l
      });
    }
  });
  
  // @{|}
  xypic.Shape.ColumnArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { return { l:0, r:0, u:0.5 * AST.xypic.lineElementLength, d:0.5 * AST.xypic.lineElementLength }; }, 
    drawDelegate: function (svg) {
      var t = AST.xypic.thickness;
      var l = xypic.em2px(0.5 * AST.xypic.lineElementLength);
      svg.createSVGElement("line", {
        x1:0, y1:l, x2:0, y2:-l
      });
    }
  });
  
  // @^{(}
  xypic.Shape.UpperLParenArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { return { l:0.5 * AST.xypic.lineElementLength, r:0, u:AST.xypic.lineElementLength, d:0 }; }, 
    drawDelegate: function (svg) {
      var t = AST.xypic.thickness;
      var r = xypic.em2px(0.5 * AST.xypic.lineElementLength);
      svg.createSVGElement("path", {
        d:"M0,0 A " + r + "," + r + " 0 0,1 0," + (-2 * r)
      });
    }
  });
  
  // @_{(}
  xypic.Shape.LowerLParenArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { return { l:0.5 * AST.xypic.lineElementLength, r:0, u:0, d:AST.xypic.lineElementLength }; }, 
    drawDelegate: function (svg) {
      var t = AST.xypic.thickness;
      var r = xypic.em2px(0.5 * AST.xypic.lineElementLength);
      svg.createSVGElement("path", {
        d:"M0,0 A " + r + "," + r + " 0 0,0 0," + (2 * r)
      });
    }
  });
  
  // @{(}
  xypic.Shape.LParenArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { return { l:0, r:0.5 * AST.xypic.lineElementLength, u:0.5 * AST.xypic.lineElementLength, d:0.5 * AST.xypic.lineElementLength }; }, 
    drawDelegate: function (svg) {
      var t = AST.xypic.thickness;
      var r = xypic.em2px(0.5 * AST.xypic.lineElementLength);
      svg.createSVGElement("path", {
        d:"M" + r + "," + (-r) + " A " + r + "," + r + " 0 0,0 " + r + "," + r
      });
    }
  });
  
  // @^{)}
  xypic.Shape.UpperRParenArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { return { l:0, r:0.5 * AST.xypic.lineElementLength, u:AST.xypic.lineElementLength, d:0 }; }, 
    drawDelegate: function (svg) {
      var t = AST.xypic.thickness;
      var r = xypic.em2px(0.5 * AST.xypic.lineElementLength);
      svg.createSVGElement("path", {
        d:"M0,0 A " + r + "," + r + " 0 0,0 0," + (-2 * r)
      });
    }
  });
  
  // @_{)}
  xypic.Shape.LowerRParenArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { return { l:0, r:0.5 * AST.xypic.lineElementLength, u:0, d:AST.xypic.lineElementLength }; }, 
    drawDelegate: function (svg) {
      var t = AST.xypic.thickness;
      var r = xypic.em2px(0.5 * AST.xypic.lineElementLength);
      svg.createSVGElement("path", {
        d:"M0,0 A " + r + "," + r + " 0 0,1 0," + (2 * r)
      });
    }
  });
  
  // @{)}
  xypic.Shape.RParenArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { return { l:0.5 * AST.xypic.lineElementLength, r:0, u:0.5 * AST.xypic.lineElementLength, d:0.5 * AST.xypic.lineElementLength }; },
    drawDelegate: function (svg) {
      var t = AST.xypic.thickness;
      var r = xypic.em2px(0.5 * AST.xypic.lineElementLength);
      svg.createSVGElement("path", {
        d:"M" + (-r) + "," + (-r) + " A " + r + "," + r + " 0 0,1 " + (-r) + "," + r
      });
    }
  });
  
  // @_{`}
  xypic.Shape.LowerBackquoteArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { return { l:0.5 * AST.xypic.lineElementLength, r:0, u:0, d:0.5 * AST.xypic.lineElementLength }; }, 
    drawDelegate: function (svg) {
      var t = AST.xypic.thickness;
      var r = xypic.em2px(0.5 * AST.xypic.lineElementLength);
      svg.createSVGElement("path", {
        d:"M0,0 A " + r + "," + r + " 0 0,0 " + (-r) + "," + (r)
      });
    }
  });
  
  // @{`}, @^{`}
  xypic.Shape.UpperBackquoteArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { return { l:0.5 * AST.xypic.lineElementLength, r:0, u:0.5 * AST.xypic.lineElementLength, d:0 }; }, 
    drawDelegate: function (svg) {
      var t = AST.xypic.thickness;
      var r = xypic.em2px(0.5 * AST.xypic.lineElementLength);
      svg.createSVGElement("path", {
        d:"M0,0 A " + r + "," + r + " 0 0,1 " + (-r) + "," + (-r)
      });
    }
  });
  
  // @_{'}
  xypic.Shape.LowerQuoteArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { return { l:0, r:0.5 * AST.xypic.lineElementLength, u:0, d:0.5 * AST.xypic.lineElementLength }; }, 
    drawDelegate: function (svg) {
      var t = AST.xypic.thickness;
      var r = xypic.em2px(0.5 * AST.xypic.lineElementLength);
      svg.createSVGElement("path", {
        d:"M0,0 A " + r + "," + r + " 0 0,1 " + r + "," + (r)
      });
    }
  });
  
  // @{'}, @^{'}
  xypic.Shape.UpperQuoteArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { return { l:0, r:0.5 * AST.xypic.lineElementLength, u:0.5 * AST.xypic.lineElementLength, d:0 }; }, 
    drawDelegate: function (svg) {
      var t = AST.xypic.thickness;
      var r = xypic.em2px(0.5 * AST.xypic.lineElementLength);
      svg.createSVGElement("path", {
        d:"M0,0 A " + r + "," + r + " 0 0,0 " + r + "," + (-r)
      });
    }
  });
  
  // @{*}
  xypic.Shape.AsteriskArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = 0;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { return { l:AST.xypic.thickness, r:AST.xypic.thickness, u:AST.xypic.thickness, d:AST.xypic.thickness }; }, 
    drawDelegate: function (svg) {
      svg.createSVGElement("circle", {
        cx:0, cy:0, r:xypic.em2px(AST.xypic.thickness),
        fill: "currentColor"
      });
    }
  });
  
  // @{o}
  xypic.Shape.OArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = 0;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { return { l:AST.xypic.thickness, r:AST.xypic.thickness, u:AST.xypic.thickness, d:AST.xypic.thickness }; }, 
    drawDelegate: function (svg) {
      svg.createSVGElement("circle", {
        cx:0, cy:0, r:xypic.em2px(AST.xypic.thickness)
      });
    }
  });
  
  // @{+}
  xypic.Shape.PlusArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { return { l:0.5 * AST.xypic.lineElementLength, r:0.5 * AST.xypic.lineElementLength, u:0.5 * AST.xypic.lineElementLength, d:0.5 * AST.xypic.lineElementLength }; }, 
    drawDelegate: function (svg) {
      var halfLen = AST.xypic.lineElementLength / 2;
      var halfLenPx = xypic.em2px(halfLen);
      svg.createSVGElement("line", {
        x1:-halfLenPx, y1:0, x2:halfLenPx, y2:0
      });
      svg.createSVGElement("line", {
        x1:0, y1:halfLenPx, x2:0, y2:-halfLenPx
      });
    }
  });
  
  // @{x}
  xypic.Shape.XArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle + Math.PI / 4;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { return { l:0.5 * AST.xypic.lineElementLength, r:0.5 * AST.xypic.lineElementLength, u:0.5 * AST.xypic.lineElementLength, d:0.5 * AST.xypic.lineElementLength }; }, 
    drawDelegate: function (svg) {
      var halfLen = AST.xypic.lineElementLength / 2;
      var halfLenPx = xypic.em2px(halfLen);
      svg.createSVGElement("line", {
        x1:-halfLenPx, y1:0, x2:halfLenPx, y2:0
      });
      svg.createSVGElement("line", {
        x1:0, y1:halfLenPx, x2:0, y2:-halfLenPx
      });
    }
  });
  
  // @{/}
  xypic.Shape.SlashArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle - Math.PI / 10;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { return { l:0, r:0, u:AST.xypic.lineElementLength / 2, d:AST.xypic.lineElementLength / 2 }; }, 
    drawDelegate: function (svg) {
      var halfLen = AST.xypic.lineElementLength / 2;
      var halfLenPx = xypic.em2px(halfLen);
      svg.createSVGElement("line", {
        x1:0, y1:halfLenPx, x2:0, y2:-halfLenPx
      });
    }
  });
  
  // @3{-}
  xypic.Shape.Line3ArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { return { l:0, r:AST.xypic.lineElementLength, u:AST.xypic.thickness, d:AST.xypic.thickness }; }, 
    drawDelegate: function (svg) {
      var lineLen = xypic.em2px(AST.xypic.lineElementLength);
      var vshift = xypic.em2px(AST.xypic.thickness);
      svg.createSVGElement("line", {
        x1:0, y1:vshift, x2:lineLen, y2:vshift
      });
      svg.createSVGElement("line", {
        x1:0, y1:0, x2:lineLen, y2:0
      });
      svg.createSVGElement("line", {
        x1:0, y1:-vshift, x2:lineLen, y2:-vshift
      });
    }
  });
  
  // @2{-}
  xypic.Shape.Line2ArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { return { l:0, r:AST.xypic.lineElementLength, u:0.5 * AST.xypic.thickness, d:0.5 * AST.xypic.thickness }; }, 
    drawDelegate: function (svg) {
      var vshift = xypic.em2px(0.5 * AST.xypic.thickness);
      var lineLen = xypic.em2px(AST.xypic.lineElementLength);
      svg.createSVGElement("line", {
        x1:0, y1:vshift, x2:lineLen, y2:vshift
      });
      svg.createSVGElement("line", {
        x1:0, y1:-vshift, x2:lineLen, y2:-vshift
      });
    }
  });
  
  // @{-}
  xypic.Shape.LineArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { return { l:0, r:AST.xypic.lineElementLength, u:0, d:0 }; }, 
    drawDelegate: function (svg) {
      var lineLen = xypic.em2px(AST.xypic.lineElementLength);
      svg.createSVGElement("line", {
        x1:0, y1:0, x2:lineLen, y2:0
      });
    }
  });
  
  // @3{.}
  xypic.Shape.Dot3ArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { return { l:0, r:0, u:AST.xypic.thickness, d:AST.xypic.thickness }; }, 
    drawDelegate: function (svg) {
      var scale = xypic.oneem;
      var vshift = xypic.em2px(AST.xypic.thickness);
      var lineLen = xypic.em2px(AST.xypic.thickness);
      var dasharray = AST.xypic.dottedDasharray;
      svg.createSVGElement("line", {
        x1:0, y1:vshift, x2:lineLen, y2:vshift,
        "stroke-dasharray": dasharray
      });
      svg.createSVGElement("line", {
        x1:0, y1:0, x2:lineLen, y2:0,
        "stroke-dasharray": dasharray
      });
      svg.createSVGElement("line", {
        x1:0, y1:-vshift, x2:lineLen, y2:-vshift,
        "stroke-dasharray": dasharray
      });
      
    }
  });
  
  // @2{.}
  xypic.Shape.Dot2ArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { return { l:0, r:0, u:0.5 * AST.xypic.thickness, d:0.5 * AST.xypic.thickness }; }, 
    drawDelegate: function (svg) {
      var vshift = xypic.em2px(0.5 * AST.xypic.thickness);
      var lineLen = xypic.em2px(AST.xypic.thickness);
      var dasharray = AST.xypic.dottedDasharray;
      svg.createSVGElement("line", {
        x1:0, y1:vshift, x2:lineLen, y2:vshift,
      "stroke-dasharray": dasharray
      });
      svg.createSVGElement("line", {
        x1:0, y1:-vshift, x2:lineLen, y2:-vshift,
      "stroke-dasharray": dasharray
      });
    }
  });
  
  // @{.}
  xypic.Shape.DotArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { return { l:0, r:0, u:0, d:0 }; }, 
    drawDelegate: function (svg) {
      var scale = xypic.oneem;
      var lineLen = xypic.em2px(AST.xypic.thickness);
      var dasharray = AST.xypic.dottedDasharray;
      svg.createSVGElement("line", {
        x1:0, y1:0, x2:lineLen, y2:0,
        "stroke-dasharray": dasharray
      });
    }
  });
  
  // @3{~}
  xypic.Shape.Tilde3ArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { return { l:-2 * AST.xypic.thickness, r:2 * AST.xypic.thickness, u:2 * AST.xypic.thickness, d:2* AST.xypic.thickness }; }, 
    drawDelegate: function (svg) {
      var s = xypic.em2px(AST.xypic.thickness);
      svg.createSVGElement("path", {
        d:"M" + (-2 * s) + "," + s + 
          " Q" + (-s) + ",0" + 
          " 0," + s +
          " T" + (2 * s) + "," + s + 
          "M" + (-2 * s) + ",0" + 
          " Q" + (-s) + "," + (-s) +
          " 0,0" +
          " T" + (2 * s) + ",0" + 
          "M" + (-2 * s) + "," + (-s) + 
          " Q" + (-s) + "," + (-2 * s) +
          " 0," + (-s) +
          " T" + (2 * s) + "," + (-s)
      });
    }
  });
  
  // @2{~}
  xypic.Shape.Tilde2ArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { return { l:-2 * AST.xypic.thickness, r:2 * AST.xypic.thickness, u:1.5 * AST.xypic.thickness, d:1.5 * AST.xypic.thickness }; }, 
    drawDelegate: function (svg) {
      var s = xypic.em2px(AST.xypic.thickness);
      svg.createSVGElement("path", {
        d:"M" + (-2 * s) + "," + (0.5 * s) + 
          " Q" + (-s) + "," + (-0.5 * s) +
          " 0," + (0.5 * s) +
          " T" + (2 * s) + "," + (0.5 * s) + 
          "M" + (-2 * s) + "," + (-0.5 * s) + 
          " Q" + (-s) + "," + (-1.5 * s) +
          " 0," + (-0.5 * s) +
          " T" + (2 * s) + "," + (-0.5 * s)
      });
    }
  });
  
  // @{~}
  xypic.Shape.TildeArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { return { l:-2 * AST.xypic.thickness, r:2 * AST.xypic.thickness, u:AST.xypic.thickness, d:AST.xypic.thickness }; }, 
    drawDelegate: function (svg) {
      var s = xypic.em2px(AST.xypic.thickness);
      svg.createSVGElement("path", {
        d:"M" + (-2 * s) + ",0" + 
          " Q" + (-s) + "," + (-s) +
          " 0,0" +
          " T" + (2 * s) + ",0"
      });
    }
  });
  
  // @{~}
  xypic.Shape.TildeArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { return { l:-2 * AST.xypic.thickness, r:2 * AST.xypic.thickness, u:AST.xypic.thickness, d:AST.xypic.thickness }; }, 
    drawDelegate: function (svg) {
      var s = xypic.em2px(AST.xypic.thickness);
      svg.createSVGElement("path", {
        d:"M" + (-2 * s) + ",0" + 
          " Q" + (-s) + "," + (-s) +
          " 0,0" +
          " T" + (2 * s) + ",0"
      });
    }
  });
  
  // @{>>}
  xypic.Shape.GTGTArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { var scale = xypic.oneem; return { l:0.489 * scale + 2 * AST.xypic.thickness, r:0, d:0.147 * scale, u:0.147 * scale }; },
    drawDelegate: function (svg) {
      var scale = xypic.oneem;
      var t = AST.xypic.thickness;
      var hshift = xypic.em2px(2 * t);
      svg.createSVGElement("path", {
        d:"M" + (-hshift) + ",0 Q" + (xypic.em2px(-0.222 * scale) - hshift) + "," + xypic.em2px(0.020 * scale) + " " + (xypic.em2px(-0.489 * scale) - hshift) + "," + xypic.em2px(0.147 * scale)
      });
      svg.createSVGElement("path", {
        d:"M" + (-hshift) + ",0 Q" + (xypic.em2px(-0.222 * scale) - hshift) + "," + xypic.em2px(-0.020 * scale) + " " + (xypic.em2px(-0.489 * scale) - hshift) + "," + xypic.em2px(-0.147 * scale)
      });
      svg.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(-0.222 * scale) + "," + xypic.em2px(0.020 * scale) + " " + xypic.em2px(-0.489 * scale) + "," + xypic.em2px(0.147 * scale)
      });
      svg.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(-0.222 * scale) + "," + xypic.em2px(-0.020 * scale) + " " + xypic.em2px(-0.489 * scale) + "," + xypic.em2px(-0.147 * scale)
      });
    }
  });
  
  // @^{>>}
  xypic.Shape.UpperGTGTArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { var scale = xypic.oneem; return { l:0.489 * scale + 2 * AST.xypic.thickness, r:0, d:0, u:0.147 * scale }; },
    drawDelegate: function (svg) {
      var scale = xypic.oneem;
      var t = AST.xypic.thickness;
      var hshift = xypic.em2px(2 * t);
      svg.createSVGElement("path", {
        d:"M" + (-hshift) + ",0 Q" + (xypic.em2px(-0.222 * scale) - hshift) + "," + xypic.em2px(-0.020 * scale) + " " + (xypic.em2px(-0.489 * scale) - hshift) + "," + xypic.em2px(-0.147 * scale)
      });
      svg.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(-0.222 * scale) + "," + xypic.em2px(-0.020 * scale) + " " + xypic.em2px(-0.489 * scale) + "," + xypic.em2px(-0.147 * scale)
      });
    }
  });
  
  // @_{>>}
  xypic.Shape.LowerGTGTArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { var scale = xypic.oneem; return { l:0.489 * scale + 2 * AST.xypic.thickness, r:0, d:0.147 * scale, u:0 }; },
    drawDelegate: function (svg) {
      var scale = xypic.oneem;
      var t = AST.xypic.thickness;
      var hshift = xypic.em2px(2 * t);
      svg.createSVGElement("path", {
        d:"M" + (-hshift) + ",0 Q" + (xypic.em2px(-0.222 * scale) - hshift) + "," + xypic.em2px(0.020 * scale) + " " + (xypic.em2px(-0.489 * scale) - hshift) + "," + xypic.em2px(0.147 * scale)
      });
      svg.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(-0.222 * scale) + "," + xypic.em2px(0.020 * scale) + " " + xypic.em2px(-0.489 * scale) + "," + xypic.em2px(0.147 * scale)
      });
    }
  });
  
  // @2{>>}
  xypic.Shape.GTGT2ArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { var scale = xypic.oneem; return { l:0.456 * scale + 2 * AST.xypic.thickness, r:0, d:0.229 * scale, u:0.229 * scale }; },
    getRadius: function () {
      var scale = xypic.oneem;
      return 0.213 * scale;
    },
    drawDelegate: function (svg) {
      var scale = xypic.oneem;
      var t = AST.xypic.thickness;
      var gu1 = svg.createGroup(svg.transformBuilder().rotateDegree(-10));
      var gd1 = svg.createGroup(svg.transformBuilder().rotateDegree(10));
      gu1.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(-0.222 * scale) + "," + xypic.em2px(-0.020 * scale) + " " + xypic.em2px(-0.489 * scale) + "," + xypic.em2px(-0.147 * scale)
      });
      gd1.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(-0.222 * scale) + ","+xypic.em2px(0.020 * scale) + " " + xypic.em2px(-0.489 * scale) + "," + xypic.em2px(0.147 * scale)
      });
      var gu2 = svg.createGroup(svg.transformBuilder().translate(-2 * t, 0).rotateDegree(-10));
      var gd2 = svg.createGroup(svg.transformBuilder().translate(-2 * t, 0).rotateDegree(10));
      gu2.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(-0.222 * scale) + "," + xypic.em2px(-0.020 * scale) + " " + xypic.em2px(-0.489 * scale) + "," + xypic.em2px(-0.147 * scale)
      });
      gd2.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(-0.222 * scale) + ","+xypic.em2px(0.020 * scale) + " " + xypic.em2px(-0.489 * scale) + "," + xypic.em2px(0.147 * scale)
      });
    }
  });
  
  // @3{>>}
  xypic.Shape.GTGT3ArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { var scale = xypic.oneem; return { l:0.507 * scale + 2 * AST.xypic.thickness, r:0, d:0.268 * scale, u:0.268 * scale }; }, 
    getRadius: function () {
      var scale = xypic.oneem;
      return 0.325 * scale;
    },
    drawDelegate: function (svg) {
      var scale = xypic.oneem;
      var t = AST.xypic.thickness;
      var gu1 = svg.createGroup(svg.transformBuilder().rotateDegree(-15));
      var gd1 = svg.createGroup(svg.transformBuilder().rotateDegree(15));
      gu1.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(-0.222 * scale) + "," + xypic.em2px(-0.020 * scale) + " " + xypic.em2px(-0.489 * scale) + "," + xypic.em2px(-0.147 * scale)
      });
      gd1.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(-0.222 * scale) + ","+xypic.em2px(0.020 * scale) + " " + xypic.em2px(-0.489 * scale) + "," + xypic.em2px(0.147 * scale)
      });
      var gu2 = svg.createGroup(svg.transformBuilder().translate(-2 * t, 0).rotateDegree(-15));
      var gd2 = svg.createGroup(svg.transformBuilder().translate(-2 * t, 0).rotateDegree(15));
      gu2.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(-0.222 * scale) + "," + xypic.em2px(-0.020 * scale) + " " + xypic.em2px(-0.489 * scale) + "," + xypic.em2px(-0.147 * scale)
      });
      gd2.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(-0.222 * scale) + ","+xypic.em2px(0.020 * scale) + " " + xypic.em2px(-0.489 * scale) + "," + xypic.em2px(0.147 * scale)
      });
      svg.createSVGElement("line", {
        x1:0, y1:0, x2:xypic.em2px(-0.507 * scale - 2 * t), y2:0
      });
    }
  });
  
  // @{<<}
  xypic.Shape.LTLTArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { var scale = xypic.oneem; return { l:0, r:0.489 * scale + 2 * AST.xypic.thickness, d:0.147 * scale, u:0.147 * scale }; }, 
    drawDelegate: function (svg) {
      var scale = xypic.oneem;
      var t = AST.xypic.thickness;
      var hshift = xypic.em2px(2 * t);
      svg.createSVGElement("path", {
        d:"M" + hshift + ",0 Q" + (xypic.em2px(0.222 * scale) + hshift) + "," + xypic.em2px(-0.020 * scale) + " " + (xypic.em2px(0.489 * scale) + hshift) + "," + xypic.em2px(-0.147 * scale)
      });
      svg.createSVGElement("path", {
        d:"M" + hshift + ",0 Q" + (xypic.em2px(0.222 * scale) + hshift) + "," + xypic.em2px(0.020 * scale) + " " + (xypic.em2px(0.489 * scale) + hshift) + "," + xypic.em2px(0.147 * scale)
      });
      svg.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(0.222 * scale) + "," + xypic.em2px(-0.020 * scale) + " " + xypic.em2px(0.489 * scale) + "," + xypic.em2px(-0.147 * scale)
      });
      svg.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(0.222 * scale) + "," + xypic.em2px(0.020 * scale) + " " + xypic.em2px(0.489 * scale) + "," + xypic.em2px(0.147 * scale)
      });
    }
  });
  
  // @^{<<}
  xypic.Shape.UpperLTLTArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { var scale = xypic.oneem; return { l:0, r:0.489 * scale + 2 * AST.xypic.thickness, d:0, u:0.147 * scale }; }, 
    drawDelegate: function (svg) {
      var scale = xypic.oneem;
      var t = AST.xypic.thickness;
      var hshift = xypic.em2px(2 * t);
      svg.createSVGElement("path", {
        d:"M" + hshift + ",0 Q" + (xypic.em2px(0.222 * scale) + hshift) + "," + xypic.em2px(-0.020 * scale) + " " + (xypic.em2px(0.489 * scale) + hshift) + "," + xypic.em2px(-0.147 * scale)
      });
      svg.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(0.222 * scale) + "," + xypic.em2px(-0.020 * scale) + " " + xypic.em2px(0.489 * scale) + "," + xypic.em2px(-0.147 * scale)
      });
    }
  });
  
  // @_{<<}
  xypic.Shape.LowerLTLTArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { var scale = xypic.oneem; return { l:0, r:0.489 * scale + 2 * AST.xypic.thickness, d:0.147 * scale, u:0 }; }, 
    drawDelegate: function (svg) {
      var scale = xypic.oneem;
      var t = AST.xypic.thickness;
      var hshift = xypic.em2px(2 * t);
      svg.createSVGElement("path", {
        d:"M" + hshift + ",0 Q" + (xypic.em2px(0.222 * scale) + hshift) + "," + xypic.em2px(0.020 * scale) + " " + (xypic.em2px(0.489 * scale) + hshift) + "," + xypic.em2px(0.147 * scale)
      });
      svg.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(0.222 * scale) + "," + xypic.em2px(0.020 * scale) + " " + xypic.em2px(0.489 * scale) + "," + xypic.em2px(0.147 * scale)
      });
    }
  });
  
  // @2{<<}
  xypic.Shape.LTLT2ArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { var scale = xypic.oneem; return { l:0, r:0.456 + scale + 2 * AST.xypic.thickness, d:0.229 * scale, u:0.229 * scale }; }, 
    getRadius: function () {
      var scale = xypic.oneem;
      return 0.213 * scale;
    },
    drawDelegate: function (svg) {
      var scale = xypic.oneem;
      var t = AST.xypic.thickness;
      var gu1 = svg.createGroup(svg.transformBuilder().translate(2 * t, 0).rotateDegree(10)); 
      var gd1 = svg.createGroup(svg.transformBuilder().translate(2 * t, 0).rotateDegree(-10));
      gu1.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(0.222 * scale) + "," + xypic.em2px(-0.020 * scale) + " " + xypic.em2px(0.489 * scale) + "," + xypic.em2px(-0.147 * scale)
      });
      gd1.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(0.222 * scale) + "," + xypic.em2px(0.020 * scale) + " " + xypic.em2px(0.489 * scale) + "," + xypic.em2px(0.147 * scale)
      });
      var gu2 = svg.createGroup(svg.transformBuilder().rotateDegree(10)); 
      var gd2 = svg.createGroup(svg.transformBuilder().rotateDegree(-10));
      gu2.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(0.222 * scale) + "," + xypic.em2px(-0.020 * scale) + " " + xypic.em2px(0.489 * scale) + "," + xypic.em2px(-0.147 * scale)
      });
      gd2.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(0.222 * scale) + "," + xypic.em2px(0.020 * scale) + " " + xypic.em2px(0.489 * scale) + "," + xypic.em2px(0.147 * scale)
      });
    }
  });
  
  // @3{<<}
  xypic.Shape.LTLT3ArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { var scale = xypic.oneem; return { l:0, r:0.507 * scale + 2 * AST.xypic.thickness, d:0.268 * scale, u:0.268 * scale }; }, 
    getRadius: function () {
      var scale = xypic.oneem;
      return 0.325 * scale;
    },
    drawDelegate: function (svg) {
      var scale = xypic.oneem;
      var t = AST.xypic.thickness;
      var gu1 = svg.createGroup(svg.transformBuilder().translate(2 * t, 0).rotateDegree(15)); 
      var gd1 = svg.createGroup(svg.transformBuilder().translate(2 * t, 0).rotateDegree(-15));
      gu1.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(0.222 * scale) + "," + xypic.em2px(-0.020 * scale) + " " + xypic.em2px(0.489 * scale) + "," + xypic.em2px(-0.147 * scale)
      });
      gd1.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(0.222 * scale) + "," + xypic.em2px(0.020 * scale) + " " + xypic.em2px(0.489 * scale) + "," + xypic.em2px(0.147 * scale)
      });
      var gu2 = svg.createGroup(svg.transformBuilder().rotateDegree(15)); 
      var gd2 = svg.createGroup(svg.transformBuilder().rotateDegree(-15));
      gu2.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(0.222 * scale) + "," + xypic.em2px(-0.020 * scale) + " " + xypic.em2px(0.489 * scale) + "," + xypic.em2px(-0.147 * scale)
      });
      gd2.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(0.222 * scale) + "," + xypic.em2px(0.020 * scale) + " " + xypic.em2px(0.489 * scale) + "," + xypic.em2px(0.147 * scale)
      });
      svg.createSVGElement("line", {
        x1:0, y1:0, x2:xypic.em2px(0.507 * scale + 2 * t), y2:0
      });
    }
  });
  
  // @{||}
  xypic.Shape.ColumnColumnArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { return { l:AST.xypic.thickness, r:0, u:0.5 * AST.xypic.lineElementLength, d:0.5 * AST.xypic.lineElementLength }; }, 
    drawDelegate: function (svg) {
      var t = AST.xypic.thickness;
      var l = xypic.em2px(0.5 * AST.xypic.lineElementLength);
      svg.createSVGElement("line", {
        x1:0, y1:l, x2:0, y2:-l
      });
      svg.createSVGElement("line", {
        x1:-xypic.em2px(t), y1:l, x2:-xypic.em2px(t), y2:-l
      });
    }
  });
  
  // @^{||}
  xypic.Shape.UpperColumnColumnArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { return { l:AST.xypic.thickness, r:0, u:AST.xypic.lineElementLength, d:0 }; }, 
    drawDelegate: function (svg) {
      var t = AST.xypic.thickness;
      var l = xypic.em2px(AST.xypic.lineElementLength);
      svg.createSVGElement("line", {
        x1:0, y1:0, x2:0, y2:-l
      });
      svg.createSVGElement("line", {
        x1:-xypic.em2px(t), y1:0, x2:-xypic.em2px(t), y2:-l
      });
    }
  });
  
  // @_{||}
  xypic.Shape.LowerColumnColumnArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { return { l:AST.xypic.thickness, r:0, u:0, d:AST.xypic.lineElementLength }; }, 
    drawDelegate: function (svg) {
      var t = AST.xypic.thickness;
      var l = xypic.em2px(AST.xypic.lineElementLength);
      svg.createSVGElement("line", {
        x1:0, y1:0, x2:0, y2:l
      });
      svg.createSVGElement("line", {
        x1:-xypic.em2px(t), y1:0, x2:-xypic.em2px(t), y2:l
      });
    }
  });
  
  // @2{||}
  xypic.Shape.ColumnColumn2ArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { return { l:AST.xypic.thickness, r:0, u:0.5 * (AST.xypic.lineElementLength + AST.xypic.thickness), d:0.5 * (AST.xypic.lineElementLength + AST.xypic.thickness) }; }, 
    drawDelegate: function (svg) {
      var t = AST.xypic.thickness;
      var l = xypic.em2px(0.5 * (AST.xypic.lineElementLength + AST.xypic.thickness));
      svg.createSVGElement("line", {
        x1:0, y1:l, x2:0, y2:-l
      });
      svg.createSVGElement("line", {
        x1:-xypic.em2px(t), y1:l, x2:-xypic.em2px(t), y2:-l
      });
    }
  });
  
  // @3{||}
  xypic.Shape.ColumnColumn3ArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { return { l:AST.xypic.thickness, r:0, u:0.5 * AST.xypic.lineElementLength + AST.xypic.thickness, d:0.5 * AST.xypic.lineElementLength + AST.xypic.thickness }; }, 
    drawDelegate: function (svg) {
      var t = AST.xypic.thickness;
      var t = AST.xypic.thickness;
      var l = xypic.em2px(0.5 * AST.xypic.lineElementLength + AST.xypic.thickness);
      svg.createSVGElement("line", {
        x1:0, y1:l, x2:0, y2:-l
      });
      svg.createSVGElement("line", {
        x1:-xypic.em2px(t), y1:l, x2:-xypic.em2px(t), y2:-l
      });
    }
  });
  
  // @{|-}
  xypic.Shape.ColumnLineArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { return { l:0, r:AST.xypic.lineElementLength, u:0.5 * AST.xypic.lineElementLength, d:0.5 * AST.xypic.lineElementLength }; }, 
    drawDelegate: function (svg) {
      var l = xypic.em2px(0.5 * AST.xypic.lineElementLength);
      svg.createSVGElement("line", {
        x1:0, y1:l, x2:0, y2:-l
      });
      var lineLen = xypic.em2px(AST.xypic.lineElementLength);
      svg.createSVGElement("line", {
        x1:0, y1:0, x2:lineLen, y2:0
      });
    }
  });
  
  // @^{|-}
  xypic.Shape.UpperColumnLineArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { return { l:0, r:AST.xypic.lineElementLength, u:AST.xypic.lineElementLength, d:0 }; }, 
    drawDelegate: function (svg) {
      var t = AST.xypic.thickness;
      var l = xypic.em2px(AST.xypic.lineElementLength);
      svg.createSVGElement("line", {
        x1:0, y1:0, x2:0, y2:-l
      });
      var lineLen = xypic.em2px(AST.xypic.lineElementLength);
      svg.createSVGElement("line", {
        x1:0, y1:0, x2:lineLen, y2:0
      });
    }
  });
  
  // @_{|-}
  xypic.Shape.LowerColumnLineArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { return { l:0, r:AST.xypic.lineElementLength, u:0, d:AST.xypic.lineElementLength }; }, 
    drawDelegate: function (svg) {
      var t = AST.xypic.thickness;
      var l = xypic.em2px(AST.xypic.lineElementLength);
      svg.createSVGElement("line", {
        x1:0, y1:0, x2:0, y2:l
      });
      var lineLen = xypic.em2px(AST.xypic.lineElementLength);
      svg.createSVGElement("line", {
        x1:0, y1:0, x2:lineLen, y2:0
      });
    }
  });
  
  // @2{|-}
  xypic.Shape.ColumnLine2ArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { return { l:0, r:AST.xypic.lineElementLength, u:0.5 * (AST.xypic.lineElementLength + AST.xypic.thickness), d:0.5 * (AST.xypic.lineElementLength + AST.xypic.thickness) }; }, 
    drawDelegate: function (svg) {
      var t = AST.xypic.thickness;
      var l = xypic.em2px(0.5 * (AST.xypic.lineElementLength + AST.xypic.thickness));
      svg.createSVGElement("line", {
        x1:0, y1:-l, x2:0, y2:l
      });
      var vshift = xypic.em2px(0.5 * t);
      var lineLen = xypic.em2px(AST.xypic.lineElementLength);
      svg.createSVGElement("line", {
        x1:0, y1:vshift, x2:lineLen, y2:vshift
      });
      svg.createSVGElement("line", {
        x1:0, y1:-vshift, x2:lineLen, y2:-vshift
      });
    }
  });
  
  // @3{|-}
  xypic.Shape.ColumnLine3ArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { return { l:0, r:AST.xypic.lineElementLength, u:0.5 * AST.xypic.lineElementLength + AST.xypic.thickness, d:0.5 * AST.xypic.lineElementLength + AST.xypic.thickness }; }, 
    drawDelegate: function (svg) {
      var t = AST.xypic.thickness;
      var l = xypic.em2px(0.5 * AST.xypic.lineElementLength + AST.xypic.thickness);
      svg.createSVGElement("line", {
        x1:0, y1:-l, x2:0, y2:l
      });
      var lineLen = xypic.em2px(AST.xypic.lineElementLength);
      var vshift = xypic.em2px(t);
      svg.createSVGElement("line", {
        x1:0, y1:vshift, x2:lineLen, y2:vshift
      });
      svg.createSVGElement("line", {
        x1:0, y1:0, x2:lineLen, y2:0
      });
      svg.createSVGElement("line", {
        x1:0, y1:-vshift, x2:lineLen, y2:-vshift
      });
    }
  });
  
  // @{>|}
  xypic.Shape.GTColumnArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { var scale = xypic.oneem; return { l:0.489 * scale, r:0, u:0.5 * AST.xypic.lineElementLength, d:0.5 * AST.xypic.lineElementLength }; }, 
    drawDelegate: function (svg) {
      var scale = xypic.oneem;
      var l = xypic.em2px(0.5 * AST.xypic.lineElementLength);
      svg.createSVGElement("line", {
        x1:0, y1:l, x2:0, y2:-l
      });
      svg.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(-0.222 * scale) + "," + xypic.em2px(0.020 * scale) + " " + xypic.em2px(-0.489 * scale) + "," + xypic.em2px(0.147 * scale)
      });
      svg.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(-0.222 * scale) + "," + xypic.em2px(-0.020 * scale) + " " + xypic.em2px(-0.489 * scale) + "," + xypic.em2px(-0.147 * scale)
      });
    }
  });
  
  // @{>>|}
  xypic.Shape.GTGTColumnArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { var scale = xypic.oneem; return { l:0.489 * scale + 2 * AST.xypic.thickness, r:0, u:0.5 * AST.xypic.lineElementLength, d:0.5 * AST.xypic.lineElementLength }; }, 
    drawDelegate: function (svg) {
      var scale = xypic.oneem;
      var t = AST.xypic.thickness;
      var l = xypic.em2px(0.5 * AST.xypic.lineElementLength);
      svg.createSVGElement("line", {
        x1:0, y1:l, x2:0, y2:-l
      });
      var hshift = xypic.em2px(2 * t);
      svg.createSVGElement("path", {
        d:"M" + (-hshift) + ",0 Q" + (xypic.em2px(-0.222 * scale) - hshift) + "," + xypic.em2px(0.020 * scale) + " " + (xypic.em2px(-0.489 * scale) - hshift) + "," + xypic.em2px(0.147 * scale)
      });
      svg.createSVGElement("path", {
        d:"M" + (-hshift) + ",0 Q" + (xypic.em2px(-0.222 * scale) - hshift) + "," + xypic.em2px(-0.020 * scale) + " " + (xypic.em2px(-0.489 * scale) - hshift) + "," + xypic.em2px(-0.147 * scale)
      });
      svg.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(-0.222 * scale) + "," + xypic.em2px(0.020 * scale) + " " + xypic.em2px(-0.489 * scale) + "," + xypic.em2px(0.147 * scale)
      });
      svg.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(-0.222 * scale) + "," + xypic.em2px(-0.020 * scale) + " " + xypic.em2px(-0.489 * scale) + "," + xypic.em2px(-0.147 * scale)
      });
    }
  });
  
  // @{|<}
  xypic.Shape.ColumnLTArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { var scale = xypic.oneem; return { l:0, r:0.489 * scale, u:0.5 * AST.xypic.lineElementLength, d:0.5 * AST.xypic.lineElementLength }; }, 
    drawDelegate: function (svg) {
      var scale = xypic.oneem;
      var t = AST.xypic.thickness;
      var l = xypic.em2px(0.5 * AST.xypic.lineElementLength);
      svg.createSVGElement("line", {
        x1:0, y1:l, x2:0, y2:-l
      });
      svg.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(0.222 * scale) + "," + xypic.em2px(-0.020 * scale) + " " + xypic.em2px(0.489 * scale) + "," + xypic.em2px(-0.147 * scale)
      });
      svg.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(0.222 * scale) + "," + xypic.em2px(0.020 * scale) + " " + xypic.em2px(0.489 * scale) + "," + xypic.em2px(0.147 * scale)
      });
    }
  });
  
  // @{|<<}
  xypic.Shape.ColumnLTLTArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { var scale = xypic.oneem; return { l:0, r:0.489 * scale + 2 * AST.xypic.thickness, u:0.5 * AST.xypic.lineElementLength, d:0.5 * AST.xypic.lineElementLength }; }, 
    drawDelegate: function (svg) {
      var scale = xypic.oneem;
      var t = AST.xypic.thickness;
      var l = xypic.em2px(0.5 * AST.xypic.lineElementLength);
      svg.createSVGElement("line", {
        x1:0, y1:l, x2:0, y2:-l
      });
      var hshift = xypic.em2px(2 * t);
      svg.createSVGElement("path", {
        d:"M" + hshift + ",0 Q" + (xypic.em2px(0.222 * scale) + hshift) + "," + xypic.em2px(-0.020 * scale) + " " + (xypic.em2px(0.489 * scale) + hshift) + "," + xypic.em2px(-0.147 * scale)
      });
      svg.createSVGElement("path", {
        d:"M" + hshift + ",0 Q" + (xypic.em2px(0.222 * scale) + hshift) + "," + xypic.em2px(0.020 * scale) + " " + (xypic.em2px(0.489 * scale) + hshift) + "," + xypic.em2px(0.147 * scale)
      });
      svg.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(0.222 * scale) + "," + xypic.em2px(-0.020 * scale) + " " + xypic.em2px(0.489 * scale) + "," + xypic.em2px(-0.147 * scale)
      });
      svg.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(0.222 * scale) + "," + xypic.em2px(0.020 * scale) + " " + xypic.em2px(0.489 * scale) + "," + xypic.em2px(0.147 * scale)
      });
    }
  });
  
  // @{//}
  xypic.Shape.SlashSlashArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle - Math.PI / 10;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { return { l:AST.xypic.thickness, r:0, u:0.5 * AST.xypic.lineElementLength, d:0.5 * AST.xypic.lineElementLength }; }, 
    drawDelegate: function (svg) {
      var hshift = xypic.em2px(AST.xypic.thickness);
      var halfLenPx = xypic.em2px(0.5 * AST.xypic.lineElementLength);
      svg.createSVGElement("line", {
        x1:0, y1:halfLenPx, x2:0, y2:-halfLenPx
      });
      svg.createSVGElement("line", {
        x1:-hshift, y1:halfLenPx, x2:-hshift, y2:-halfLenPx
      });
    }
  });
  
  // @{=>}
  xypic.Shape.LineGT2ArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { var scale = xypic.oneem; return { l:AST.xypic.lineElementLength, r:AST.xypic.lineElementLength, d:0.229 * scale, u:0.229 * scale }; },
    getRadius: function () {
      var scale = xypic.oneem;
      return 0.213 * scale;
    },
    drawDelegate: function (svg) {
      var scale = xypic.oneem;
      var halfLen = AST.xypic.lineElementLength;
      var hshift = xypic.em2px(halfLen);
      var v = 0.5 * AST.xypic.thickness;
      var vshift = xypic.em2px(v);
      var r = this.getRadius();
      var delta = xypic.em2px(Math.sqrt(r * r - v * v));
      
      var gu = svg.createGroup(svg.transformBuilder().translate(halfLen, 0).rotateDegree(-10));
      var gd = svg.createGroup(svg.transformBuilder().translate(halfLen, 0).rotateDegree(10));
      gu.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(-0.222 * scale) + "," + xypic.em2px(-0.020 * scale) + " " + xypic.em2px(-0.489 * scale) + "," + xypic.em2px(-0.147 * scale)
      });
      gd.createSVGElement("path", {
        d:"M0,0 Q" + xypic.em2px(-0.222 * scale) + ","+xypic.em2px(0.020 * scale) + " " + xypic.em2px(-0.489 * scale) + "," + xypic.em2px(0.147 * scale)
      });
      svg.createSVGElement("path", {
        d:"M" + (-hshift) + "," + vshift + " L" + (hshift - delta) + "," + vshift + 
          " M" + (-hshift) + "," + (-vshift) + " L" + (hshift - delta) + "," + (-vshift)
      });
    }
  });
  
  // twocell equality arrow
  xypic.Shape.TwocellEqualityArrowheadShape = xypic.Shape.ArrowheadShape.Subclass({
    Init: function (c, angle) {
      this.c = c;
      this.angle = angle;
      memoize(this, "getBoundingBox");
    },
    getBox: function () { var scale = xypic.oneem; return { l:AST.xypic.lineElementLength, r:AST.xypic.lineElementLength, d:0.5 * AST.xypic.thickness, u:0.5 * AST.xypic.thickness }; },
    drawDelegate: function (svg) {
      var scale = xypic.oneem;
      var hshift = xypic.em2px(AST.xypic.lineElementLength);
      var vshift = xypic.em2px(0.5 * AST.xypic.thickness);
      svg.createSVGElement("path", {
        d:"M" + (-hshift) + "," + vshift + " L" + hshift + "," + vshift + 
          " M" + (-hshift) + "," + (-vshift) + " L" + hshift + "," + (-vshift)
      });
    }
  });
  
  
  xypic.Shape.LineShape = xypic.Shape.Subclass({
    Init: function (line, object, main, variant, bbox) {
      this.line = line;
      this.object = object;
      this.main = main;
      this.variant = variant;
      this.bbox = bbox;
      this.holeRanges = FP.List.empty;
    },
    sliceHole: function (range) {
      this.holeRanges = this.holeRanges.prepend(range);
    },
    draw: function (svg) {
      this.line.drawLine(svg, this.object, this.main, this.variant, this.holeRanges);
    },
    getBoundingBox: function () {
      return this.bbox;
    },
    toString: function () {
      return "LineShape[line:" + this.line + ", object:" + this.object + ", main:" + this.main + ", variant:" + this.variant + "]";
    }
  });
  
  xypic.Shape.CurveShape = xypic.Shape.Subclass({
    Init: function (curve, objectForDrop, objectForConnect, bbox) {
      this.curve = curve;
      this.objectForDrop = objectForDrop;
      this.objectForConnect = objectForConnect;
      this.bbox = bbox;
      this.holeRanges = FP.List.empty;
    },
    sliceHole: function (range) {
      this.holeRanges = this.holeRanges.prepend(range);
    },
    draw: function (svg) {
      this.curve.drawCurve(svg, this.objectForDrop, this.objectForConnect, this.holeRanges);
    },
    getBoundingBox: function () {
      return this.bbox;
    },
    toString: function () {
      return "CurveShape[curve" + this.curve + ", objectForDrop:" + (this.objectForDrop !== undefined? this.objectForDrop.toString() : "null") + ", objectForConnect:" + (this.objectForConnect !== undefined? this.objectForConnect.toString() : "null") + "]";
    }
  });
  
  
  xypic.Curve = MathJax.Object.Subclass({
    velocity: function (t) {
      var dx = this.dpx(t);
      var dy = this.dpy(t);
      return Math.sqrt(dx*dx+dy*dy);
    },
    length: function (t) {
      if (t < 0 || t > 1) {
        throw xypic.ExecutionError("illegal cubic Bezier parameter t:"+t);
      }
      this.buildLengthArray();
      
      var n = AST.xypic.lengthResolution;
      var tn = t*n;
      var f = Math.floor(tn);
      var c = Math.ceil(tn);
      if (f === c) {
        return this.lengthArray[f];
      }
      var sf = this.lengthArray[f];
      var sc = this.lengthArray[c];
      return sf + (sc-sf)/(c-f)*(tn-f);  // linear interpolation 
    },
    tOfLength: function (s) {
      this.buildLengthArray();
      
      var a = this.lengthArray;
      if (s < a[0]) {
        return 0;
      } else if (s > a[a.length - 1]) {
        return 1;
      }
      
      var m, al, ah;
      var l = 0;
      var r = a.length-2;
      while (l <= r) {
        m = (l + r) >> 1;
        al = a[m];
        ah = a[m+1];
        if (s >= al && s <= ah) {
          break;
        }
        if (s < al) {
          r = m-1;
        } else {
          l = m+1;
        }
      }
      
      var n = AST.xypic.lengthResolution;
      if (al === ah) {
        return m/n;
      }
      var t = (m + (s-al)/(ah-al))/n;
      return t;
    },
    tOfShavedStart: function (frame) {
      if (frame.isPoint()) {
        return 0; // trivial
      }
      
      var ts = this.tOfIntersections(frame);
      if (ts.length == 0) {
        return undefined; // No solution.
      }
      return Math.min.apply(Math, ts);
    },
    tOfShavedEnd: function (frame) {
      if (frame.isPoint()) {
        return 1; // trivial
      }
      
      var ts = this.tOfIntersections(frame);
      if (ts.length == 0) {
        return undefined; // No solution.
      }
      return Math.max.apply(Math, ts);
    },
    shaveStart: function (frame) {
      if (frame.isPoint()) {
        return this; // trivial
      }
      
      var ts = this.tOfIntersections(frame);
      if (ts.length == 0) {
        return undefined; // No solution.
      }
      var t = Math.min.apply(Math, ts);
      return this.divide(t)[1];
    },
    shaveEnd: function (frame) {
      if (frame.isPoint()) {
        return this; // trivial
      }
      
      var ts = this.tOfIntersections(frame);
      if (ts.length == 0) {
        return undefined; // No solution.
      }
      var t = Math.max.apply(Math, ts);
      return this.divide(t)[0];
    },
    buildLengthArray: function () {
      if (this.lengthArray !== undefined) {
        return;
      }
      
      var n = AST.xypic.lengthResolution;
      // lengthArray[i]: \int_0^{t_{2i}} v(t) dt with Simpson's rule, (i=0, 1, \cdots, n)
      // where, t_k=k h, h=1/(2n): step length.
      var lengthArray = new Array(n+1);
      
      var sum = 0;
      var h = 1/2/n;
      var i = 0;
      var delta = h/3;
      lengthArray[0] = 0;
      sum = this.velocity(0) + 4*this.velocity(h);
      lastv = this.velocity(2*h);
      lengthArray[1] = delta*(sum + lastv);
      for (i = 2; i <= n; i++) {
        sum += 2*lastv + 4*this.velocity((2*i-1)*h);
        lastv = this.velocity(2*i*h);
        lengthArray[i] = delta*(sum + lastv);
      }
      this.lengthArray = lengthArray;
    },
    drawParallelCurve: function (svg, vshift) {
      var i, n = this.countOfSegments() * AST.xypic.interpolationResolution;
      var ts = new Array(n+1);
      var x1s = new Array(n+1);
      var y1s = new Array(n+1);
      var x2s = new Array(n+1);
      var y2s = new Array(n+1);
      var hpi = Math.PI/2;
      var d = vshift;
      var t, angle, p, x, y, dc, ds;
      for (i = 0; i <= n; i++) {
        t = i/n;
        ts[i] = t;  // TODO: 高速化。ts[i+1]-ts[i]が定数の場合に特化した作りにする。
        angle = this.angle(t);
        p = this.position(t);
        x = p.x;
        y = p.y;
        dc = d*Math.cos(angle+hpi);
        ds = d*Math.sin(angle+hpi);
        x1s[i] = x+dc;
        y1s[i] = y+ds;
        x2s[i] = x-dc;
        y2s[i] = y-ds;
      }
      xypic.Curve.CubicBeziers.interpolation(ts, x1s, y1s).drawPrimitive(svg, "none");
      xypic.Curve.CubicBeziers.interpolation(ts, x2s, y2s).drawPrimitive(svg, "none");
    },
    drawParallelDottedCurve: function (svg, spacing, vshift) {
      var px = 1/xypic.em, hpx = px/2;
      var sp = px + spacing;
      var len = this.length(1);
      var n = Math.floor((len-px)/sp);
      var d = vshift;
      if (n >= 0) {
        var i, hpi = Math.PI/2;
        var s = this.startPosition(), e = this.endPosition();
        for (i = 0; i <= n; i++) {
          var s = hpx + i*sp;
          // TODO: 高速化。毎回二分探索せず、端から線形探索・適用するようにする。
          var t = this.tOfLength(s);
          var angle = this.angle(t);
          var p = this.position(t);
          var x = p.x, y = p.y
          var dc = d*Math.cos(angle+hpi), ds = d*Math.sin(angle+hpi);
          svg.createSVGElement("circle", {
            cx:xypic.em2px(x+dc), cy:-xypic.em2px(y+ds), r:0.12,
            fill: "currentColor"
          });
          svg.createSVGElement("circle", {
            cx:xypic.em2px(x-dc), cy:-xypic.em2px(y-ds), r:0.12,
            fill: "currentColor"
          });
        }
      }
    },
    drawParallelDashedCurve: function (svg, dash, vshift) {
      var len = this.length(1);
      var n = Math.floor((len-dash)/(2*dash)), m = 2*n+1;
      var hshift = (len-dash)/2-n*dash;
      var i;
      var ts = new Array(n+1);
      var x1s = new Array(n+1);
      var y1s = new Array(n+1);
      var x2s = new Array(n+1);
      var y2s = new Array(n+1);
      var hpi = Math.PI/2;
      var d = vshift;
      var t, angle, p, x, y, dc, ds;
      for (i = 0; i <= m; i++) {
        // TODO: 高速化。毎回二分探索せず、端から線形探索・適用するようにする。
        t = this.tOfLength(hshift + i*dash);
        ts[i] = t;
        angle = this.angle(t);
        p = this.position(t);
        x = p.x;
        y = p.y;
        dc = d*Math.cos(angle+hpi);
        ds = d*Math.sin(angle+hpi);
        x1s[i] = x+dc;
        y1s[i] = y+ds;
        x2s[i] = x-dc;
        y2s[i] = y-ds;
      }
      xypic.Curve.CubicBeziers.interpolation(ts, x1s, y1s).drawSkipped(svg);
      xypic.Curve.CubicBeziers.interpolation(ts, x2s, y2s).drawSkipped(svg);
    },
    drawSquigCurve: function (svg, variant) {
      var thickness = xypic.length2em("0.15em");
      var len = this.length(1);
      var wave = 4*thickness;
      var amp = thickness;
      if (len >= wave) {
        var n = Math.floor(len/wave);
        var shiftLen = (len-n*wave)/2;
        
        var s, t, p, angle, nx, ny, hpi = Math.PI/2, d1, d2, d3;
        switch (variant) {
          case "3":
            s = shiftLen;
            t = this.tOfLength(s);
            p = this.position(t);
            angle = this.angle(t);
            nx = amp*Math.cos(angle+hpi);
            ny = amp*Math.sin(angle+hpi);
            d1 = "M"+xypic.em2px(p.x+nx)+","+xypic.em2px(-p.y-ny);
            d2 = "M"+xypic.em2px(p.x)+","+xypic.em2px(-p.y);
            d3 = "M"+xypic.em2px(p.x-nx)+","+xypic.em2px(-p.y+ny);
            
            for (var i = 0; i < n; i++) {
              s = shiftLen + wave*i + thickness;
              t = this.tOfLength(s);
              p = this.position(t);
              angle = this.angle(t);
              nx = amp*Math.cos(angle+hpi);
              ny = amp*Math.sin(angle+hpi);
              d1 += " Q"+xypic.em2px(p.x+2*nx)+","+xypic.em2px(-p.y-2*ny);
              d2 += " Q"+xypic.em2px(p.x+nx)+","+xypic.em2px(-p.y-ny);
              d3 += " Q"+xypic.em2px(p.x)+","+xypic.em2px(-p.y);
              
              s = shiftLen + wave*i + 2*thickness;
              t = this.tOfLength(s);
              p = this.position(t);
              angle = this.angle(t);
              nx = amp*Math.cos(angle+hpi);
              ny = amp*Math.sin(angle+hpi);
              d1 += " "+xypic.em2px(p.x+nx)+","+xypic.em2px(-p.y-ny);
              d2 += " "+xypic.em2px(p.x)+","+xypic.em2px(-p.y);
              d3 += " "+xypic.em2px(p.x-nx)+","+xypic.em2px(-p.y+ny);
              
              s = shiftLen + wave*i + 3*thickness;
              t = this.tOfLength(s);
              p = this.position(t);
              angle = this.angle(t);
              nx = amp*Math.cos(angle+hpi);
              ny = amp*Math.sin(angle+hpi);
              d1 += " Q"+xypic.em2px(p.x)+","+xypic.em2px(-p.y);
              d2 += " Q"+xypic.em2px(p.x-nx)+","+xypic.em2px(-p.y+ny);
              d3 += " "+xypic.em2px(p.x-2*nx)+","+xypic.em2px(-p.y+2*ny);
              
              s = shiftLen + wave*(i+1);
              t = this.tOfLength(s);
              p = this.position(t);
              angle = this.angle(t);
              nx = amp*Math.cos(angle+hpi);
              ny = amp*Math.sin(angle+hpi);
              d1 += " "+xypic.em2px(p.x+nx)+","+xypic.em2px(-p.y-ny);
              d2 += " "+xypic.em2px(p.x)+","+xypic.em2px(-p.y);
              d3 += " "+xypic.em2px(p.x-nx)+","+xypic.em2px(-p.y+ny);
            }
            svg.createSVGElement("path", {"d":d1});
            svg.createSVGElement("path", {"d":d2});
            svg.createSVGElement("path", {"d":d3});
            break;
            
          case "2":
            s = shiftLen;
            t = this.tOfLength(s);
            p = this.position(t);
            angle = this.angle(t);
            nx = amp*Math.cos(angle+hpi)/2;
            ny = amp*Math.sin(angle+hpi)/2;
            d1 = "M"+xypic.em2px(p.x+nx)+","+xypic.em2px(-p.y-ny);
            d2 = "M"+xypic.em2px(p.x-nx)+","+xypic.em2px(-p.y+ny);
            
            for (var i = 0; i < n; i++) {
              s = shiftLen + wave*i + thickness;
              t = this.tOfLength(s);
              p = this.position(t);
              angle = this.angle(t);
              nx = amp*Math.cos(angle+hpi)/2;
              ny = amp*Math.sin(angle+hpi)/2;
              d1 += " Q"+xypic.em2px(p.x+3*nx)+","+xypic.em2px(-p.y-3*ny);
              d2 += " Q"+xypic.em2px(p.x+nx)+","+xypic.em2px(-p.y-ny);
              
              s = shiftLen + wave*i + 2*thickness;
              t = this.tOfLength(s);
              p = this.position(t);
              angle = this.angle(t);
              nx = amp*Math.cos(angle+hpi)/2;
              ny = amp*Math.sin(angle+hpi)/2;
              d1 += " "+xypic.em2px(p.x+nx)+","+xypic.em2px(-p.y-ny);
              d2 += " "+xypic.em2px(p.x-nx)+","+xypic.em2px(-p.y+ny);
              
              s = shiftLen + wave*i + 3*thickness;
              t = this.tOfLength(s);
              p = this.position(t);
              angle = this.angle(t);
              nx = amp*Math.cos(angle+hpi)/2;
              ny = amp*Math.sin(angle+hpi)/2;
              d1 += " Q"+xypic.em2px(p.x-nx)+","+xypic.em2px(-p.y+ny);
              d2 += " Q"+xypic.em2px(p.x-3*nx)+","+xypic.em2px(-p.y+3*ny);
              
              s = shiftLen + wave*(i+1);
              t = this.tOfLength(s);
              p = this.position(t);
              angle = this.angle(t);
              nx = amp*Math.cos(angle+hpi)/2;
              ny = amp*Math.sin(angle+hpi)/2;
              d1 += " "+xypic.em2px(p.x+nx)+","+xypic.em2px(-p.y-ny);
              d2 += " "+xypic.em2px(p.x-nx)+","+xypic.em2px(-p.y+ny);
            }
            svg.createSVGElement("path", {"d":d1});
            svg.createSVGElement("path", {"d":d2});
            break;
            
          default:
            s = shiftLen;
            t = this.tOfLength(s);
            p = this.position(t);
            d1 = "M"+xypic.em2px(p.x)+","+xypic.em2px(-p.y);
            
            for (var i = 0; i < n; i++) {
              s = shiftLen + wave*i + thickness;
              t = this.tOfLength(s);
              p = this.position(t);
              angle = this.angle(t);
              nx = amp*Math.cos(angle+hpi);
              ny = amp*Math.sin(angle+hpi);
              d1 += " Q"+xypic.em2px(p.x+nx)+","+xypic.em2px(-p.y-ny);
              
              s = shiftLen + wave*i + 2*thickness;
              t = this.tOfLength(s);
              p = this.position(t);
              d1 += " "+xypic.em2px(p.x)+","+xypic.em2px(-p.y);
              
              s = shiftLen + wave*i + 3*thickness;
              t = this.tOfLength(s);
              p = this.position(t);
              angle = this.angle(t);
              nx = amp*Math.cos(angle+hpi);
              ny = amp*Math.sin(angle+hpi);
              d1 += " Q"+xypic.em2px(p.x-nx)+","+xypic.em2px(-p.y+ny);
              
              s = shiftLen + wave*(i+1);
              t = this.tOfLength(s);
              p = this.position(t);
              d1 += " "+xypic.em2px(p.x)+","+xypic.em2px(-p.y);
            }
            svg.createSVGElement("path", {"d":d1});
        }
      }
    },
    drawDashSquigCurve: function (svg, variant) {
      var thickness = AST.xypic.thickness;
      var len = this.length(1);
      var wave = 4*thickness;
      var amp = thickness;
      if (len >= wave) {
        var n = Math.floor((len-wave)/2/wave);
        var shiftLen = (len-wave)/2-n*wave;
        
        var s, t, p, angle, nx, ny, hpi = Math.PI/2, d1, d2, d3;
        switch (variant) {
          case "3":
            d1 = d2 = d3 = "";
            for (var i = 0; i <= n; i++) {
              s = shiftLen + wave*i*2;
              t = this.tOfLength(s);
              p = this.position(t);
              angle = this.angle(t);
              nx = amp*Math.cos(angle+hpi);
              ny = amp*Math.sin(angle+hpi);
              d1 += " M"+xypic.em2px(p.x+nx)+","+xypic.em2px(-p.y-ny);
              d2 += " M"+xypic.em2px(p.x)+","+xypic.em2px(-p.y);
              d3 += " M"+xypic.em2px(p.x-nx)+","+xypic.em2px(-p.y+ny);
              
              s = shiftLen + wave*i*2 + thickness;
              t = this.tOfLength(s);
              p = this.position(t);
              angle = this.angle(t);
              nx = amp*Math.cos(angle+hpi);
              ny = amp*Math.sin(angle+hpi);
              d1 += " Q"+xypic.em2px(p.x+2*nx)+","+xypic.em2px(-p.y-2*ny);
              d2 += " Q"+xypic.em2px(p.x+nx)+","+xypic.em2px(-p.y-ny);
              d3 += " Q"+xypic.em2px(p.x)+","+xypic.em2px(-p.y);
              
              s = shiftLen + wave*i*2 + 2*thickness;
              t = this.tOfLength(s);
              p = this.position(t);
              angle = this.angle(t);
              nx = amp*Math.cos(angle+hpi);
              ny = amp*Math.sin(angle+hpi);
              d1 += " "+xypic.em2px(p.x+nx)+","+xypic.em2px(-p.y-ny);
              d2 += " "+xypic.em2px(p.x)+","+xypic.em2px(-p.y);
              d3 += " "+xypic.em2px(p.x-nx)+","+xypic.em2px(-p.y+ny);
              
              s = shiftLen + wave*i*2 + 3*thickness;
              t = this.tOfLength(s);
              p = this.position(t);
              angle = this.angle(t);
              nx = amp*Math.cos(angle+hpi);
              ny = amp*Math.sin(angle+hpi);
              d1 += " Q"+xypic.em2px(p.x)+","+xypic.em2px(-p.y);
              d2 += " Q"+xypic.em2px(p.x-nx)+","+xypic.em2px(-p.y+ny);
              d3 += " "+xypic.em2px(p.x-2*nx)+","+xypic.em2px(-p.y+2*ny);
              
              s = shiftLen + wave*(i*2+1);
              t = this.tOfLength(s);
              p = this.position(t);
              angle = this.angle(t);
              nx = amp*Math.cos(angle+hpi);
              ny = amp*Math.sin(angle+hpi);
              d1 += " "+xypic.em2px(p.x+nx)+","+xypic.em2px(-p.y-ny);
              d2 += " "+xypic.em2px(p.x)+","+xypic.em2px(-p.y);
              d3 += " "+xypic.em2px(p.x-nx)+","+xypic.em2px(-p.y+ny);
            }
            svg.createSVGElement("path", {"d":d1});
            svg.createSVGElement("path", {"d":d2});
            svg.createSVGElement("path", {"d":d3});
            break;
            
          case "2":
            d1 = d2 = "";
            for (var i = 0; i <= n; i++) {
              s = shiftLen + wave*i*2;
              t = this.tOfLength(s);
              p = this.position(t);
              angle = this.angle(t);
              nx = amp*Math.cos(angle+hpi)/2;
              ny = amp*Math.sin(angle+hpi)/2;
              d1 += " M"+xypic.em2px(p.x+nx)+","+xypic.em2px(-p.y-ny);
              d2 += " M"+xypic.em2px(p.x-nx)+","+xypic.em2px(-p.y+ny);
              
              s = shiftLen + wave*i*2 + thickness;
              t = this.tOfLength(s);
              p = this.position(t);
              angle = this.angle(t);
              nx = amp*Math.cos(angle+hpi)/2;
              ny = amp*Math.sin(angle+hpi)/2;
              d1 += " Q"+xypic.em2px(p.x+3*nx)+","+xypic.em2px(-p.y-3*ny);
              d2 += " Q"+xypic.em2px(p.x+nx)+","+xypic.em2px(-p.y-ny);
              
              s = shiftLen + wave*i*2 + 2*thickness;
              t = this.tOfLength(s);
              p = this.position(t);
              angle = this.angle(t);
              nx = amp*Math.cos(angle+hpi)/2;
              ny = amp*Math.sin(angle+hpi)/2;
              d1 += " "+xypic.em2px(p.x+nx)+","+xypic.em2px(-p.y-ny);
              d2 += " "+xypic.em2px(p.x-nx)+","+xypic.em2px(-p.y+ny);
              
              s = shiftLen + wave*i*2 + 3*thickness;
              t = this.tOfLength(s);
              p = this.position(t);
              angle = this.angle(t);
              nx = amp*Math.cos(angle+hpi)/2;
              ny = amp*Math.sin(angle+hpi)/2;
              d1 += " Q"+xypic.em2px(p.x-nx)+","+xypic.em2px(-p.y+ny);
              d2 += " Q"+xypic.em2px(p.x-3*nx)+","+xypic.em2px(-p.y+3*ny);
              
              s = shiftLen + wave*(i*2+1);
              t = this.tOfLength(s);
              p = this.position(t);
              angle = this.angle(t);
              nx = amp*Math.cos(angle+hpi)/2;
              ny = amp*Math.sin(angle+hpi)/2;
              d1 += " "+xypic.em2px(p.x+nx)+","+xypic.em2px(-p.y-ny);
              d2 += " "+xypic.em2px(p.x-nx)+","+xypic.em2px(-p.y+ny);
            }
            svg.createSVGElement("path", {"d":d1});
            svg.createSVGElement("path", {"d":d2});
            break;
            
          default:
            d1 = "";
            for (var i = 0; i <= n; i++) {
              s = shiftLen + wave*i*2;
              t = this.tOfLength(s);
              p = this.position(t);
              d1 += " M"+xypic.em2px(p.x)+","+xypic.em2px(-p.y);
              
              s = shiftLen + wave*i*2 + thickness;
              t = this.tOfLength(s);
              p = this.position(t);
              angle = this.angle(t);
              nx = amp*Math.cos(angle+hpi);
              ny = amp*Math.sin(angle+hpi);
              d1 += " Q"+xypic.em2px(p.x+nx)+","+xypic.em2px(-p.y-ny);
              
              s = shiftLen + wave*i*2 + 2*thickness;
              t = this.tOfLength(s);
              p = this.position(t);
              d1 += " "+xypic.em2px(p.x)+","+xypic.em2px(-p.y);
              
              s = shiftLen + wave*i*2 + 3*thickness;
              t = this.tOfLength(s);
              p = this.position(t);
              angle = this.angle(t);
              nx = amp*Math.cos(angle+hpi);
              ny = amp*Math.sin(angle+hpi);
              d1 += " Q"+xypic.em2px(p.x-nx)+","+xypic.em2px(-p.y+ny);
              
              s = shiftLen + wave*(i*2+1);
              t = this.tOfLength(s);
              p = this.position(t);
              d1 += " "+xypic.em2px(p.x)+","+xypic.em2px(-p.y);
            }
            svg.createSVGElement("path", {"d":d1});
        }
      }
    },
    drawCurve: function (svg, objectForDrop, objectForConnect, holeRanges) {
      if (holeRanges.isEmpty) {
        this._drawCurve(svg, objectForDrop, objectForConnect);
      } else {
        var clippingRanges = xypic.Range(0, 1).differenceRanges(holeRanges);
        var self = this;
        clippingRanges.foreach(function (range) {
          self.slice(range.start, range.end)._drawCurve(svg, objectForDrop, objectForConnect);
        });
      }
    },
    _drawCurve: function (svg, objectForDrop, objectForConnect) {
      var thickness = xypic.length2em("0.15em");
      var vshift;
      if (objectForConnect !== undefined) {
        var main = objectForConnect.dirMain();
        var variant = objectForConnect.dirVariant();
        switch (main) {
          case "=":
            main = "-";
            variant = "2";
            break;
          case "==":
            main = "--";
            variant = "2";
            break;
          case ':':
          case '::':
            main = ".";
            variant = "2";
            break;
        }
        
        switch (main) {
          case '':
            // draw nothing.
            break;
            
          case '-':
            switch (variant) {
              case "2":
                vshift = thickness/2;
                this.drawParallelCurve(svg, vshift);
                break;
              case "3":
                vshift = thickness;
                this.drawParallelCurve(svg, vshift);
                this.drawPrimitive(svg, "none");
                break;
              default:
                vshift = 0;
                this.drawPrimitive(svg, "none");
            }
            break;
            
          case '.':
          case '..':
            switch (variant) {
              case "2":
                vshift = thickness/2;
                this.drawParallelDottedCurve(svg, thickness, vshift)
                break;
                
              case "3":
                vshift = thickness;
                this.drawParallelDottedCurve(svg, thickness, vshift)
                this.drawPrimitive(svg, AST.xypic.dottedDasharray);
                break;
                
              default:
                vshift = 0;
                this.drawPrimitive(svg, AST.xypic.dottedDasharray);
                break;
            }
            break;
            
          case '--':
            var dash = 3 * thickness;
            var len = this.length(1);
            if (len >= dash) {
              switch (variant) {
                case "2":
                  vshift = thickness / 2;
                  this.drawParallelDashedCurve(svg, dash, vshift);
                  break;
                  
                case "3":
                  vshift = thickness;
                  this.drawParallelDashedCurve(svg, dash, vshift);
                  var shiftLen = (len - dash) / 2 - Math.floor((len - dash) / 2 / dash) * dash;
                  var shiftT = this.tOfLength(shiftLen);
                  var shifted = this.divide(shiftT)[1];
                  shifted.drawPrimitive(svg, xypic.em2px(dash) + " " + xypic.em2px(dash))
                  break;
                  
                default:
                  vshift = 0;
                  var shiftLen = (len - dash) / 2 - Math.floor((len - dash) / 2 / dash) * dash;
                  var shiftT = this.tOfLength(shiftLen);
                  var shifted = this.divide(shiftT)[1];
                  shifted.drawPrimitive(svg, xypic.em2px(dash) + " " + xypic.em2px(dash));
              }
            }
            break;
            
          case '~':
            this.drawSquigCurve(svg, variant);
            switch (variant) {
              case "2":
                vshift = 1.5 * thickness;
                break;
              case "3":
                vshift = 2 * thickness;
                break;
              default:
                vshift = 0
            }
            break;
            
          case '~~':
            this.drawDashSquigCurve(svg, variant);
            switch (variant) {
              case "2":
                vshift = 1.5 * thickness;
                break;
              case "3":
                vshift = 2 * thickness;
                break;
              default:
                vshift = 0
            }
            break;
            
          default:
            // TODO: ~* と ~** の順序を考慮する。
            var dummyEnv = xypic.Env();
            dummyEnv.c = xypic.Env.originPosition;
            var dummyContext = xypic.DrawingContext(xypic.Shape.none, dummyEnv);
            var conBBox = objectForConnect.boundingBox(dummyContext);
            if (conBBox == undefined) {
              return;
            }
            
            var cl = conBBox.l;
            var conLen = cl + conBBox.r;
            
            var dropLen, dl;
            if (objectForDrop !== undefined) {
              var dropBBox = objectForDrop.boundingBox(dummyContext);
              if (dropBBox !== undefined) {
                dl = dropBBox.l;
                dropLen = dl + dropBBox.r;
              }
            } else {
              dropLen = 0;
            }
            
            var compositeLen = conLen + dropLen;
            if (compositeLen == 0) {
              compositeLen = AST.xypic.strokeWidth;
            }
            
            var len = this.length(1);
            var n = Math.floor(len / compositeLen);
            if (n == 0) {
              return;
            }
            
            var shiftLen = (len - n * compositeLen) / 2;
            
            var dummyContext = xypic.DrawingContext(xypic.Shape.none, dummyEnv);
            var s, t;
            for (var i = 0; i < n; i++) {
              s = shiftLen + i * compositeLen;
              if (objectForDrop !== undefined) {
                t = this.tOfLength(s + dl);
                dummyEnv.c = this.position(t);
                dummyEnv.angle = this.angle(t);
                objectForDrop.toDropShape(dummyContext).draw(svg);
              }
              t = this.tOfLength(s + dropLen + cl);
              dummyEnv.c = this.position(t);
              dummyEnv.angle = this.angle(t);
              bbox = objectForConnect.toDropShape(dummyContext).draw(svg);
            }
        }
      } else {
        var dummyEnv = xypic.Env();
        dummyEnv.c = xypic.Env.originPosition;
        var dummyContext = xypic.DrawingContext(xypic.Shape.none, dummyEnv);
        var object = objectForDrop;
        var objectBBox = object.boundingBox(dummyContext);
        if (objectBBox === undefined) {
          return;
        }
        var objectWidth = objectBBox.l + objectBBox.r;
        var objectLen = objectWidth;
        if (objectLen == 0) {
          objectLen = AST.xypic.strokeWidth;
        }
        
        var len = this.length(1);
        var n = Math.floor(len / objectLen);
        if (n == 0) {
          return;
        }
        
        var shiftLen = (len - n * objectLen + objectLen - objectWidth) / 2 + objectBBox.l;
        var dummyContext = xypic.DrawingContext(xypic.Shape.none, dummyEnv);
        for (var i = 0; i < n; i++) {
          var s = shiftLen + i * objectLen;
          var t = this.tOfLength(s);
          dummyEnv.c = this.position(t);
          dummyEnv.angle = 0;
          object.toDropShape(dummyContext).draw(svg);
        }
      }
    },
    toShape: function (context, objectForDrop, objectForConnect) {
      var env = context.env;
      var thickness = xypic.length2em("0.15em");
      var shape = xypic.Shape.none;
      var vshift;
      if (objectForConnect !== undefined) {
        var main = objectForConnect.dirMain();
        var variant = objectForConnect.dirVariant();
        switch (main) {
          case "=":
            main = "-";
            variant = "2";
            break;
          case "==":
            main = "--";
            variant = "2";
            break;
          case ':':
          case '::':
            main = ".";
            variant = "2";
            break;
        }
        
        switch (main) {
          case '':
            vshift = 0;
            break;
            
          case '-':
          case '.':
          case '..':
            switch (variant) {
              case "2":
                vshift = thickness / 2;
                break;
                
              case "3":
                vshift = thickness;
                break;
                
              default:
                vshift = 0;
                break;
            }
            break;
            
          case '--':
            var dash = 3 * thickness;
            var len = this.length(1);
            if (len >= dash) {
              switch (variant) {
                case "2":
                  vshift = thickness / 2;
                  break;
                  
                case "3":
                  vshift = thickness;
                  break;
                  
                default:
                  vshift = 0;
              }
            }
            break;
            
          case '~':
          case '~~':
            switch (variant) {
              case "2":
                vshift = 1.5 * thickness;
                break;
              case "3":
                vshift = 2 * thickness;
                break;
              default:
                vshift = 0
            }
            break;
            
          default:
            // TODO: ~* と ~** の順序を考慮する。
            var conBBox = objectForConnect.boundingBox(context);
            if (conBBox == undefined) {
              env.angle = 0;
              env.lastCurve = xypic.LastCurve.none;
              return xypic.Shape.none;
            }
            vshift = Math.max(conBBox.u, conBBox.d);
            
            var cl = conBBox.l;
            var conLen = cl + conBBox.r;
            
            var dropLen, dl;
            if (objectForDrop !== undefined) {
              var dropBBox = objectForDrop.boundingBox(context);
              if (dropBBox !== undefined) {
                dl = dropBBox.l;
                dropLen = dl + dropBBox.r;
                vshift = Math.max(vshift, dropBBox.u, dropBBox.d);
              }
            } else {
              dropLen = 0;
            }
            
            var compositeLen = conLen + dropLen;
            if (compositeLen == 0) {
              compositeLen = AST.xypic.strokeWidth;
            }
            
            var len = this.length(1);
            var n = Math.floor(len / compositeLen);
            if (n == 0) {
              env.angle = 0;
              env.lastCurve = xypic.LastCurve.none;
              return xypic.Shape.none;
            }
            
            shape = xypic.Shape.CurveShape(this, objectForDrop, objectForConnect, this.boundingBox(vshift));
            context.appendShapeToFront(shape);
            return shape;
        }
        if (vshift === undefined) {
          return xypic.Shape.none;
        } else {
          shape = xypic.Shape.CurveShape(this, objectForDrop, objectForConnect, this.boundingBox(vshift));
          context.appendShapeToFront(shape);
          return shape;
        }
      } else if (objectForDrop !== undefined) {
        var object = objectForDrop;
        var objectBBox = object.boundingBox(context);
        if (objectBBox == undefined) {
          env.angle = 0;
          env.lastCurve = xypic.LastCurve.none;
          return xypic.Shape.none;
        }
        
        var objectWidth = objectBBox.l + objectBBox.r;
        var objectLen = objectWidth;
        if (objectLen == 0) {
          objectLen = AST.xypic.strokeWidth;
        }
        
        var len = this.length(1);
        var n = Math.floor(len / objectLen);
        if (n == 0) {
          env.angle = 0;
          env.lastCurve = xypic.LastCurve.none;
          return xypic.Shape.none;
        }
        
        vshift = Math.max(objectBBox.u, objectBBox.d);
        shape = xypic.Shape.CurveShape(this, objectForDrop, objectForConnect, this.boundingBox(vshift));
        context.appendShapeToFront(shape);
        return shape;
      }
      return shape;
    }
  }, {
    sign: function (x) { return x>0? 1 : (x===0? 0 : -1); },
    solutionsOfCubicEq: function (a3, a2, a1, a0) {
      // find solutions t in [0, 1]
      if (a3 === 0) {
        return xypic.Curve.solutionsOfQuadEq(a2, a1, a0);
      }
      var b2 = a2/3/a3, b1 = a1/a3, b0 = a0/a3;
      var p = b2*b2-b1/3, q = -b0/2+b1*b2/2-b2*b2*b2;
      var d = q*q-p*p*p;
      if (d === 0) {
        var s = Math.pow(q, 1/3);
        var t0 = 2*s-b2, t1 = -s-b2;
        return xypic.Curve.filterByIn0to1([t0, t1]);
      } else if (d > 0) {
        var u = q+xypic.Curve.sign(q)*Math.sqrt(d);
        var r = xypic.Curve.sign(u)*Math.pow(Math.abs(u), 1/3);
        var s = p/r;
        var t = r+s-b2;
        return xypic.Curve.filterByIn0to1([t]);
      } else {
        var r = 2*Math.sqrt(p);
        var s = Math.acos(2*q/p/r);
        var t0 = r*Math.cos(s/3)-b2;
        var t1 = r*Math.cos((s+2*Math.PI)/3)-b2;
        var t2 = r*Math.cos((s+4*Math.PI)/3)-b2;
        return xypic.Curve.filterByIn0to1([t0, t1, t2]);
      }
    },
    solutionsOfQuadEq: function (a2, a1, a0) {
      // find solutions t in [0, 1]
      if (a2 === 0) {
        return xypic.Curve.solutionsOfLinearEq(a1, a0);
      } else {
        var d = a1 * a1 - 4 * a0 * a2;
        if (d >= 0) {
          var s = Math.sqrt(d);
          var tp = (-a1 + s) / 2 / a2;
          var tm = (-a1 - s) / 2 / a2;
          return xypic.Curve.filterByIn0to1([tp, tm]);
        } else {
          return [];
        }
      }
    },
    solutionsOfLinearEq: function (a1, a0) {
      // find solution t in [0, 1]
      if (a1 === 0) {
        return (a0 === 0? 0 : []);
      }
      return xypic.Curve.filterByIn0to1([-a0 / a1]);
    },
    filterByIn0to1: function (ts) {
      var filterdTs = [];
      for (var i = 0; i < ts.length; i++) {
        var t = ts[i];
        if (t >= 0 && t <= 1) {
          filterdTs.push(t);
        }
      }
      return filterdTs;
    }
  });
  
  xypic.Curve.QuadBezier = xypic.Curve.Subclass({
    Init: function (cp0, cp1, cp2) {
      this.cp0 = cp0;
      this.cp1 = cp1;
      this.cp2 = cp2;
      
      var a0x = cp0.x;
      var a1x = 2*(cp1.x - cp0.x);
      var a2x = cp2.x - 2*cp1.x + cp0.x;
      this.px = function(t) { return a0x + t*a1x + t*t*a2x; }
      this.dpx = function(t) { return a1x + 2*t*a2x; }
      
      var a0y = cp0.y;
      var a1y = 2*(cp1.y - cp0.y);
      var a2y = cp2.y - 2*cp1.y + cp0.y;
      this.py = function(t) { return a0y + t*a1y + t*t*a2y; }
      this.dpy = function(t) { return a1y + 2*t*a2y; }
    },
    startPosition: function () {
      return this.cp0;
    },
    endPosition: function () {
      return this.cp2;
    },
    position: function (t) {
      return xypic.Frame.Point(this.px(t), this.py(t));
    },
    derivative: function (t) {
      return xypic.Frame.Point(this.dpx(t), this.dpy(t));
    },
    angle: function (t) {
      return Math.atan2(this.dpy(t), this.dpx(t));
    },
    boundingBox: function (vshift) {
      var maxMinX = this.maxMin(this.cp0.x, this.cp1.x, this.cp2.x, vshift);
      var maxMinY = this.maxMin(this.cp0.y, this.cp1.y, this.cp2.y, vshift);
      if (vshift === 0) {
        return xypic.Frame.Rect(this.cp0.x, this.cp0.y, {
          l:this.cp0.x-maxMinX.min, r:maxMinX.max-this.cp0.x,
          u:maxMinY.max-this.cp0.y, d:this.cp0.y-maxMinY.min
        });
      } else {
        var hpi = Math.PI/2;
        var sx = this.cp0.x;
        var sy = this.cp0.y;
        var ex = this.cp2.x;
        var ey = this.cp2.y;
        var a0 = this.angle(0)+hpi;
        var a1 = this.angle(1)+hpi;
        var vc0 = vshift*Math.cos(a0), vs0 = vshift*Math.sin(a0);
        var vc1 = vshift*Math.cos(a1), vs1 = vshift*Math.sin(a1);
        var minX = Math.min(maxMinX.min, sx+vc0, sx-vc0, ex+vc1, ex-vc1);
        var maxX = Math.max(maxMinX.max, sx+vc0, sx-vc0, ex+vc1, ex-vc1);
        var minY = Math.min(maxMinY.min, sy+vs0, sy-vs0, ey+vs1, ey-vs1);
        var maxY = Math.max(maxMinY.max, sy+vs0, sy-vs0, ey+vs1, ey-vs1);
        return xypic.Frame.Rect(sx, sy, {
          l:sx-minX, r:maxX-sx, u:maxY-sy, d:sy-minY
        });
      }
    },
    maxMin: function (x0, x1, x2, vshift) {
      var max, min;
      if (x0 > x2) {
        max = x0;
        min = x2;
      } else {
        max = x2;
        min = x0;
      }
      
      var roundEp = xypic.Util.roundEpsilon;
      
      var a0 = roundEp(x0);
      var a1 = roundEp(x1 - x0);
      var a2 = roundEp(x2 - 2*x1 + x0);
      var p = function(t) { return a0 + 2*t*a1 + t*t*a2 }
      
      var x, t;
      if (a2 != 0) {
        t = -a1/a2;
        if (t > 0 && t < 1) {
          x = p(t);
          max = Math.max(max, x + vshift, x - vshift);
          min = Math.min(min, x + vshift, x - vshift);
        }
      }
      return {min:min, max:max};
    },
    divide: function (t) {
      if (t < 0 || t > 1) {
        throw xypic.ExecutionError("illegal quadratic Bezier parameter t:"+t);
      }
      
      var x0 = this.cp0.x;
      var x1 = this.cp1.x;
      var x2 = this.cp2.x;
      
      var y0 = this.cp0.y;
      var y1 = this.cp1.y;
      var y2 = this.cp2.y;
      
      var tx = this.px(t);
      var ty = this.py(t);
      
      var p0 = this.cp0;
      var p1 = xypic.Frame.Point(x0+t*(x1-x0), y0+t*(y1-y0));
      var p2 = xypic.Frame.Point(tx, ty);
      
      var q0 = p2;
      var q1 = xypic.Frame.Point(x1+t*(x2-x1), y1+t*(y2-y1));
      var q2 = this.cp2;
      
      return [
        xypic.Curve.QuadBezier(p0, p1, p2),
        xypic.Curve.QuadBezier(q0, q1, q2)
      ]
    },
    slice: function (t0, t1) {
      if (t0 >= t1) {
        return undefined;
      }
      
      if (t0 < 0) {
        t0 = 0;
      } 
      if (t1 > 1) {
        t1 = 1;
      }
      
      if (t0 === 0 && t1 === 1) {
        return this;
      }
      
      var x0 = this.cp0.x;
      var x1 = this.cp1.x;
      var x2 = this.cp2.x;
      
      var y0 = this.cp0.y;
      var y1 = this.cp1.y;
      var y2 = this.cp2.y;
      
      var q0x = this.px(t0);
      var q0y = this.py(t0);
      var q1x = x1 + t0 * (x2 - x1);
      var q1y = y1 + t0 * (y2 - y1);
      
      var p0 = xypic.Frame.Point(q0x, q0y);
      var p1 = xypic.Frame.Point(q0x + t1 * (q1x - q0x), q0y + t1 * (q1y - q0y));
      var p2 = xypic.Frame.Point(this.px(t1), this.py(t1));
      
      return xypic.Curve.QuadBezier(p0, p1, p2);
    },
    tOfIntersections: function (frame) {
      if (frame.isPoint()) {
        return []; // CAUTION: Point does not intersect with any curves.
      }
      
      if (frame.isRect()) {
        // find starting edge point
        var rx = frame.x + frame.r;
        var lx = frame.x - frame.l;
        var uy = frame.y + frame.u;
        var dy = frame.y - frame.d;
        
        var roundEp = xypic.Util.roundEpsilon;
        
        var x0 = this.cp0.x;
        var x1 = this.cp1.x;
        var x2 = this.cp2.x;
        
        var a0x = roundEp(x0);
        var a1x = roundEp(2*(x1 - x0));
        var a2x = roundEp(x2 - 2*x1 + x0);
        var px = function(t) { return a0x + t*a1x + t*t*a2x; }
        
        var y0 = this.cp0.y;
        var y1 = this.cp1.y;
        var y2 = this.cp2.y;
        
        var a0y = roundEp(y0);
        var a1y = roundEp(2*(y1 - y0));
        var a2y = roundEp(y2 - 2*y1 + y0);
        var py = function(t) { return a0y + t*a1y + t*t*a2y; }
        
        var ts = [];
        
        var tsCandidate;
        tsCandidate = xypic.Curve.solutionsOfQuadEq(a2x, a1x, a0x - rx);
        tsCandidate = tsCandidate.concat(xypic.Curve.solutionsOfQuadEq(a2x, a1x, a0x - lx));
        for (var i = 0; i < tsCandidate.length; i++) {
          var t = tsCandidate[i];
          var y = py(t);
          if (y >= dy && y <= uy) {
            ts.push(t);
          }
        }
        tsCandidate = xypic.Curve.solutionsOfQuadEq(a2y, a1y, a0y - uy);
        tsCandidate = tsCandidate.concat(xypic.Curve.solutionsOfQuadEq(a2y, a1y, a0y - dy));
        for (var i = 0; i < tsCandidate.length; i++) {
          var t = tsCandidate[i];
          var x = px(t);
          if (x >= lx && x <= rx) {
            ts.push(t);
          }
        }
        
        return ts;
      } else if (frame.isCircle()) {
        var pi = Math.PI;
        var x = frame.x;
        var y = frame.y;
        var l = frame.l;
        var r = frame.r;
        var u = frame.u;
        var d = frame.d;
        var cx = x + (r - l) / 2;
        var cy = y + (u - d) / 2;
        var rx = (l + r) / 2;
        var ry = (u + d) / 2;
        
        var delta = pi / 180; // overlapping
        var arc0 = xypic.CurveSegment.Arc(cx, cy, rx, ry, -pi - delta, -pi / 2 + delta);
        var arc1 = xypic.CurveSegment.Arc(cx, cy, rx, ry, -pi / 2 - delta, 0 + delta);
        var arc2 = xypic.CurveSegment.Arc(cx, cy, rx, ry, 0 - delta, pi / 2 + delta);
        var arc3 = xypic.CurveSegment.Arc(cx, cy, rx, ry, pi / 2 - delta, pi + delta);
        
        var bezier = xypic.CurveSegment.QuadBezier(this, 0, 1);
        
        var intersec = [];
        intersec = intersec.concat(xypic.CurveSegment.findIntersections(arc0, bezier));
        intersec = intersec.concat(xypic.CurveSegment.findIntersections(arc1, bezier));
        intersec = intersec.concat(xypic.CurveSegment.findIntersections(arc2, bezier));
        intersec = intersec.concat(xypic.CurveSegment.findIntersections(arc3, bezier));
        
        var ts = [];
        for (var i = 0; i < intersec.length; i++) { 
          var t = (intersec[i][1].min + intersec[i][1].max) / 2;
          ts.push(t);
        }
        return ts;
      }
    },
    countOfSegments: function () { return 1; },
    drawPrimitive: function (svg, dasharray) {
      var cp0 = this.cp0, cp1 = this.cp1, cp2 = this.cp2;
      svg.createSVGElement("path", {
        "d":"M"+xypic.em2px(cp0.x)+","+xypic.em2px(-cp0.y)+
          " Q"+xypic.em2px(cp1.x)+","+xypic.em2px(-cp1.y)+
          " "+xypic.em2px(cp2.x)+","+xypic.em2px(-cp2.y),
        "stroke-dasharray":dasharray
      });
    },
    toString: function () {
      return "QuadBezier("+this.cp0.x+", "+this.cp0.y+")-("+this.cp1.x+", "+this.cp1.y+")-("+this.cp2.x+", "+this.cp2.y+")"
    }
  });
  
  xypic.Curve.CubicBezier = xypic.Curve.Subclass({
    Init: function (cp0, cp1, cp2, cp3) {
      this.cp0 = cp0;
      this.cp1 = cp1;
      this.cp2 = cp2;
      this.cp3 = cp3;
      
      var a0x = cp0.x;
      var a1x = 3*(cp1.x - cp0.x);
      var a2x = 3*(cp2.x - 2*cp1.x + cp0.x);
      var a3x = cp3.x - 3*cp2.x + 3*cp1.x - cp0.x;
      this.px = function(t) { return a0x + t*a1x + t*t*a2x + t*t*t*a3x; }
      this.dpx = function(t) { return a1x + 2*t*a2x + 3*t*t*a3x; }
      
      var a0y = cp0.y;
      var a1y = 3*(cp1.y - cp0.y);
      var a2y = 3*(cp2.y - 2*cp1.y + cp0.y);
      var a3y = cp3.y - 3*cp2.y + 3*cp1.y - cp0.y;
      this.py = function(t) { return a0y + t*a1y + t*t*a2y + t*t*t*a3y; }
      this.dpy = function(t) { return a1y + 2*t*a2y + 3*t*t*a3y; }
    },
    startPosition: function () {
      return this.cp0;
    },
    endPosition: function () {
      return this.cp3;
    },
    position: function (t) {
      return xypic.Frame.Point(this.px(t), this.py(t));
    },
    derivative: function (t) {
      return xypic.Frame.Point(this.dpx(t), this.dpy(t));
    },
    angle: function (t) {
      return Math.atan2(this.dpy(t), this.dpx(t));
    },
    boundingBox: function (vshift) {
      var maxMinX = this.maxMin(this.cp0.x, this.cp1.x, this.cp2.x, this.cp3.x, vshift);
      var maxMinY = this.maxMin(this.cp0.y, this.cp1.y, this.cp2.y, this.cp3.y, vshift);
      if (vshift === 0) {
        return xypic.Frame.Rect(this.cp0.x, this.cp0.y, {
          l:this.cp0.x-maxMinX.min, r:maxMinX.max-this.cp0.x,
          u:maxMinY.max-this.cp0.y, d:this.cp0.y-maxMinY.min
        });
      } else {
        var hpi = Math.PI/2;
        var sx = this.cp0.x;
        var sy = this.cp0.y;
        var ex = this.cp3.x;
        var ey = this.cp3.y;
        var a0 = this.angle(0)+hpi;
        var a1 = this.angle(1)+hpi;
        var vc0 = vshift*Math.cos(a0), vs0 = vshift*Math.sin(a0);
        var vc1 = vshift*Math.cos(a1), vs1 = vshift*Math.sin(a1);
        var minX = Math.min(maxMinX.min, sx+vc0, sx-vc0, ex+vc1, ex-vc1);
        var maxX = Math.max(maxMinX.max, sx+vc0, sx-vc0, ex+vc1, ex-vc1);
        var minY = Math.min(maxMinY.min, sy+vs0, sy-vs0, ey+vs1, ey-vs1);
        var maxY = Math.max(maxMinY.max, sy+vs0, sy-vs0, ey+vs1, ey-vs1);
        return xypic.Frame.Rect(sx, sy, {
          l:sx-minX, r:maxX-sx, u:maxY-sy, d:sy-minY
        });
      }
    },
    maxMin: function (x0, x1, x2, x3, vshift) {
      var max, min;
      if (x0 > x3) {
        max = x0;
        min = x3;
      } else {
        max = x3;
        min = x0;
      }
      
      var roundEp = xypic.Util.roundEpsilon;
      var a0 = roundEp(x0);
      var a1 = roundEp(x1 - x0);
      var a2 = roundEp(x2 - 2*x1 + x0);
      var a3 = roundEp(x3 - 3*x2 + 3*x1 - x0);
      var p = function(t) { return a0 + 3*t*a1 + 3*t*t*a2 + t*t*t*a3 }
      
      var updateMinMax = function (t) {
        if (t > 0 && t < 1) {
          x = p(t);
          max = Math.max(max, x + vshift, x - vshift);
          min = Math.min(min, x + vshift, x - vshift);
        }
      }
      
      var t, x;
      if (a3 == 0) {
        if (a2 != 0) {
          t = -a1/a2/2;
          updateMinMax(t);
        }
      } else {
        var d = a2*a2 - a1*a3;
        if (d > 0) {
          t = (-a2 + Math.sqrt(d))/a3;
          updateMinMax(t);
          t = (-a2 - Math.sqrt(d))/a3;
          updateMinMax(t);
        } else if (d == 0) {
          t = -a2/a3;
          updateMinMax(t);
        }
      }
      return {min:min, max:max};
    },
    divide: function (t) {
      if (t < 0 || t > 1) {
        throw xypic.ExecutionError("illegal cubic Bezier parameter t:"+t);
      }
      
      var x0 = this.cp0.x;
      var x1 = this.cp1.x;
      var x2 = this.cp2.x;
      var x3 = this.cp3.x;
      
      var y0 = this.cp0.y;
      var y1 = this.cp1.y;
      var y2 = this.cp2.y;
      var y3 = this.cp3.y;
      
      var tx = this.px(t);
      var ty = this.py(t);
      
      var p0 = this.cp0;
      var p1 = xypic.Frame.Point(x0+t*(x1-x0), y0+t*(y1-y0));
      var p2 = xypic.Frame.Point(
        x0+2*t*(x1-x0)+t*t*(x2-2*x1+x0),
        y0+2*t*(y1-y0)+t*t*(y2-2*y1+y0)
      );
      var p3 = xypic.Frame.Point(tx, ty);
      
      var q0 = p3;
      var q1 = xypic.Frame.Point(
        x1+2*t*(x2-x1)+t*t*(x3-2*x2+x1),
        y1+2*t*(y2-y1)+t*t*(y3-2*y2+y1)
      );
      var q2 = xypic.Frame.Point(x2+t*(x3-x2), y2+t*(y3-y2));
      var q3 = this.cp3;
      
      return [
        xypic.Curve.CubicBezier(p0, p1, p2, p3),
        xypic.Curve.CubicBezier(q0, q1, q2, q3)
      ]
    },
    slice: function (t0, t1) {
      if (t0 >= t1) {
        return undefined;
      }
      
      if (t0 < 0) {
        t0 = 0;
      } 
      if (t1 > 1) {
        t1 = 1;
      }
      
      if (t0 === 0 && t1 === 1) {
        return this;
      }
      
      var x0 = this.cp0.x;
      var x1 = this.cp1.x;
      var x2 = this.cp2.x;
      var x3 = this.cp3.x;
      
      var y0 = this.cp0.y;
      var y1 = this.cp1.y;
      var y2 = this.cp2.y;
      var y3 = this.cp3.y;
      
      var q0x = this.px(t0);
      var q0y = this.py(t0);
      var q1x = x1 + 2 * t0 * (x2 - x1) + t0 * t0 * (x3 - 2 * x2 + x1);
      var q1y = y1 + 2 * t0 * (y2 - y1) + t0 * t0 * (y3 - 2 * y2 + y1);
      var q2x = x2 + t0 * (x3 - x2);
      var q2y = y2 + t0 * (y3 - y2);
      
      var p0 = xypic.Frame.Point(q0x, q0y);
      var p1 = xypic.Frame.Point(q0x + t1 * (q1x - q0x), q0y + t1 * (q1y - q0y));
      var p2 = xypic.Frame.Point(
        q0x + 2 * t1 * (q1x - q0x) + t1 * t1 * (q2x - 2 * q1x + q0x),
        q0y + 2 * t1 * (q1y - q0y) + t1 * t1 * (q2y - 2 * q1y + q0y)
      );
      var p3 = xypic.Frame.Point(this.px(t1), this.py(t1));
      
      return xypic.Curve.CubicBezier(p0, p1, p2, p3);
    },
    tOfIntersections: function (frame) {
      if (frame.isPoint()) {
        return []; // CAUTION: Point does not intersect with any curves.
      }
      
      if (frame.isRect()) {
        // find starting edge point
        var rx = frame.x + frame.r;
        var lx = frame.x - frame.l;
        var uy = frame.y + frame.u;
        var dy = frame.y - frame.d;
        
        var roundEp = xypic.Util.roundEpsilon;
        
        var x0 = this.cp0.x;
        var x1 = this.cp1.x;
        var x2 = this.cp2.x;
        var x3 = this.cp3.x;
        
        var y0 = this.cp0.y;
        var y1 = this.cp1.y;
        var y2 = this.cp2.y;
        var y3 = this.cp3.y;
        
        var a0x = roundEp(x0);
        var a1x = roundEp(3*(x1 - x0));
        var a2x = roundEp(3*(x2 - 2*x1 + x0));
        var a3x = roundEp(x3 - 3*x2 + 3*x1 - x0);
        var px = function(t) { return a0x + t*a1x + t*t*a2x + t*t*t*a3x }
        
        var a0y = roundEp(y0);
        var a1y = roundEp(3*(y1 - y0));
        var a2y = roundEp(3*(y2 - 2*y1 + y0));
        var a3y = roundEp(y3 - 3*y2 + 3*y1 - y0);
        var py = function(t) { return a0y + t*a1y + t*t*a2y + t*t*t*a3y }
        
        var ts = [];
        var tsCandidate;
        tsCandidate = xypic.Curve.solutionsOfCubicEq(a3x, a2x, a1x, a0x-rx);
        tsCandidate = tsCandidate.concat(xypic.Curve.solutionsOfCubicEq(a3x, a2x, a1x, a0x-lx));
        for (var i = 0; i < tsCandidate.length; i++) {
          var t = tsCandidate[i];
          var y = py(t);
          if (y >= dy && y <= uy) {
            ts.push(t);
          }
        }
        tsCandidate = xypic.Curve.solutionsOfCubicEq(a3y, a2y, a1y, a0y-uy);
        tsCandidate = tsCandidate.concat(xypic.Curve.solutionsOfCubicEq(a3y, a2y, a1y, a0y-dy));
        for (var i = 0; i < tsCandidate.length; i++) {
          var t = tsCandidate[i];
          var x = px(t);
          if (x >= lx && x <= rx) {
            ts.push(t);
          }
        }
        
        return ts;
      } else if (frame.isCircle()) {
        var pi = Math.PI;
        var x = frame.x;
        var y = frame.y;
        var l = frame.l;
        var r = frame.r;
        var u = frame.u;
        var d = frame.d;
        var cx = x + (r - l) / 2;
        var cy = y + (u - d) / 2;
        var rx = (l + r) / 2;
        var ry = (u + d) / 2;
        
        var delta = pi / 180; // overlapping
        var arc0 = xypic.CurveSegment.Arc(cx, cy, rx, ry, -pi - delta, -pi / 2 + delta);
        var arc1 = xypic.CurveSegment.Arc(cx, cy, rx, ry, -pi / 2 - delta, 0 + delta);
        var arc2 = xypic.CurveSegment.Arc(cx, cy, rx, ry, 0 - delta, pi / 2 + delta);
        var arc3 = xypic.CurveSegment.Arc(cx, cy, rx, ry, pi / 2 - delta, pi + delta);
        
        var bezier = xypic.CurveSegment.CubicBezier(this, 0, 1);
        
        var intersec = [];
        intersec = intersec.concat(xypic.CurveSegment.findIntersections(arc0, bezier));
        intersec = intersec.concat(xypic.CurveSegment.findIntersections(arc1, bezier));
        intersec = intersec.concat(xypic.CurveSegment.findIntersections(arc2, bezier));
        intersec = intersec.concat(xypic.CurveSegment.findIntersections(arc3, bezier));
        
        var ts = [];
        for (var i = 0; i < intersec.length; i++) { 
          var t = (intersec[i][1].min + intersec[i][1].max) / 2;
          ts.push(t);
        }
        return ts;
      }
    },
    countOfSegments: function () { return 1; },
    drawPrimitive: function (svg, dasharray) {
      var cp0 = this.cp0, cp1 = this.cp1, cp2 = this.cp2, cp3 = this.cp3;
      svg.createSVGElement("path", {
        "d":"M"+xypic.em2px(cp0.x)+","+xypic.em2px(-cp0.y)+
          " C"+xypic.em2px(cp1.x)+","+xypic.em2px(-cp1.y)+
          " "+xypic.em2px(cp2.x)+","+xypic.em2px(-cp2.y)+
          " "+xypic.em2px(cp3.x)+","+xypic.em2px(-cp3.y),
        "stroke-dasharray":dasharray
      });
    },
    toString: function () {
      return "CubicBezier("+this.cp0.x+", "+this.cp0.y+")-("+this.cp1.x+", "+this.cp1.y+")-("+this.cp2.x+", "+this.cp2.y+")-("+this.cp3.x+", "+this.cp3.y+")"
    }
  });
  
  xypic.Curve.CubicBeziers = xypic.Curve.Subclass({
    Init: function (cbs) {
      this.cbs = cbs;
      var n = this.cbs.length;
      this.delegate = (n == 0?
        function (t, succ, fail) {
          return fail;
        } : function (t, succ, fail) {
          var tn = t * n;
          var i = Math.floor(tn);
          if (i < 0) { i = 0; }
          if (i >= n) { i = n - 1; }
          var s = tn - i;
          var cb = cbs[i];
          return succ(cb, s);
        }
      );
    },
    startPosition: function () {
      return this.cbs[0].cp0;
    },
    endPosition: function () {
      return this.cbs[this.cbs.length - 1].cp3;
    },
    position: function (t) {
      return this.delegate(t, function (cb, s) { return cb.position(s) }, undefined);
    },
    derivative: function (t) {
      return this.delegate(t, function (cb, s) { return cb.derivative(s) }, undefined);
    },
    angle: function (t) {
      return this.delegate(t, function (cb, s) { return cb.angle(s) }, 0);
    },
    velocity: function (t) {
      var n = this.cbs.length;
      return this.delegate(t, function (cb, s) { return n * cb.velocity(s) }, 0);
    },
    boundingBox: function (vshift) {
      if (this.cbs.length == 0) {
        return undefined;
      }
      var bbox = this.cbs[0].boundingBox(vshift);
      var i, n = this.cbs.length;
      for (i = 1; i < n; i++) {
        bbox = bbox.combineRect(this.cbs[i].boundingBox(vshift))
      }
      return bbox;
    },
    tOfIntersections: function (frame) {
      var ts = [];
      var i = 0, n = this.cbs.length;
      for (i = 0; i < n; i++) {
        var cb = this.cbs[i];
        unnormalizedTs = cb.tOfIntersections(frame);
        for (j = 0; j < unnormalizedTs.length; j++) {
          ts.push((unnormalizedTs[j] + i) / n);
        }
      }
      return ts;
    },
    divide: function (t) {
      if (t < 0 || t > 1) {
        throw xypic.ExecutionError("illegal cubic Bezier parameter t:"+t);
      } else if (t === 0) {
        return [xypic.Curve.CubicBeziers([]), this];
      } else if (t === 1) {
        return [this, xypic.Curve.CubicBeziers([])];
      }
      
      var n = this.cbs.length;
      var tn = t * n;
      var i = Math.floor(tn);
      if (i === n) {
        i = n - 1;
      }
      var s = tn - i;
      var divS = this.cbs.slice(0, i);
      var divE = this.cbs.slice(i + 1);
      var cb = this.cbs[i];
      var divB = cb.divide(s);
      divS.push(divB[0]);
      divE.unshift(divB[1]);
      return [xypic.Curve.CubicBeziers(divS), xypic.Curve.CubicBeziers(divE)];
    },
    slice: function (t0, t1) {
      if (t0 >= t1) {
        return undefined;
      }
      
      if (t0 < 0) {
        t0 = 0;
      } 
      if (t1 > 1) {
        t1 = 1;
      }
      
      if (t0 === 0 && t1 === 1) {
        return this;
      }
      
      var n = this.cbs.length;
      var tn0 = t0 * n;
      var tn1 = t1 * n;
      var i0 = Math.floor(tn0);
      var i1 = Math.floor(tn1);
      if (i0 === n) {
        i0 = n - 1;
      }
      if (i1 === n) {
        i1 = n - 1;
      }
      var s0 = tn0 - i0;
      var s1 = tn1 - i1;
      var subBeziers;
      if (i0 === i1) {
        subBeziers = [this.cbs[i0].slice(s0, s1)];
      } else {
        subBeziers = this.cbs.slice(i0 + 1, i1);
        subBeziers.push(this.cbs[i1].slice(0, s1));
        subBeziers.unshift(this.cbs[i0].slice(s0, 1));
      }
      return xypic.Curve.CubicBeziers(subBeziers);
    },
    countOfSegments: function () { return this.cbs.length; },
    drawPrimitive: function (svg, dasharray) {
      var n = this.cbs.length;
      var cbs = this.cbs;
      var cb = cbs[0];
      var cp0 = cb.cp0, cp1 = cb.cp1, cp2 = cb.cp2, cp3 = cb.cp3;
      var d = ("M"+xypic.em2px(cp0.x)+","+xypic.em2px(-cp0.y)+
          " C"+xypic.em2px(cp1.x)+","+xypic.em2px(-cp1.y)+
          " "+xypic.em2px(cp2.x)+","+xypic.em2px(-cp2.y)+
          " "+xypic.em2px(cp3.x)+","+xypic.em2px(-cp3.y));
      for (var i = 1; i < n; i++) {
        cb = cbs[i];
        cp2 = cb.cp2, cp3 = cb.cp3;
        d += " S"+xypic.em2px(cp2.x)+","+xypic.em2px(-cp2.y)+" "+xypic.em2px(cp3.x)+","+xypic.em2px(-cp3.y);
      }
      svg.createSVGElement("path", {"d":d, "stroke-dasharray":dasharray});
    },
    drawSkipped: function (svg) {
      var n = this.cbs.length;
      var cbs = this.cbs;
      var d = "";
      for (var i = 0; i < n; i+=2) {
        var cb = cbs[i];
        var cp0 = cb.cp0, cp1 = cb.cp1, cp2 = cb.cp2, cp3 = cb.cp3;
        d += ("M"+xypic.em2px(cp0.x)+","+xypic.em2px(-cp0.y)+
            " C"+xypic.em2px(cp1.x)+","+xypic.em2px(-cp1.y)+
            " "+xypic.em2px(cp2.x)+","+xypic.em2px(-cp2.y)+
            " "+xypic.em2px(cp3.x)+","+xypic.em2px(-cp3.y));
      }
      svg.createSVGElement("path", {"d":d});
    }
  },{
    interpolation: function (ts, xs, ys) {
      var x12 = xypic.Curve.CubicBeziers.cubicSplineInterpolation(ts, xs);
      var x1 = x12[0];
      var x2 = x12[1];
      
      var y12 = xypic.Curve.CubicBeziers.cubicSplineInterpolation(ts, ys);
      var y1 = y12[0];
      var y2 = y12[1];
      
      var i, n = ts.length;
      var beziers = new Array(n-1);
      for (i = 0; i < n-1; i++) {
        beziers[i] = xypic.Curve.CubicBezier(
          xypic.Frame.Point(xs[i], ys[i]),
          xypic.Frame.Point(x1[i], y1[i]),
          xypic.Frame.Point(x2[i], y2[i]),
          xypic.Frame.Point(xs[i+1], ys[i+1])
        )
      }
      return xypic.Curve.CubicBeziers(beziers);
    },
    cubicSplineInterpolation: function (ts, xs) {
      var n = ts.length-1;
      var hs = new Array(n);
      var i;
      for (i = 0; i < n; i++) {
        hs[i] = ts[i+1] - ts[i];
      }
      var as = new Array(n);
      for (i = 1; i < n; i++) {
        as[i] = 3*(xs[i+1] - xs[i])/hs[i] - 3*(xs[i] - xs[i-1])/hs[i-1];
      }
      var ls = new Array(n+1);
      var ms = new Array(n+1);
      var zs = new Array(n+1);
      ls[0] = 1;
      ms[0] = 0;
      zs[0] = 0;
      for (i = 1; i < n; i++) {
        ls[i] = 2*(ts[i+1] - ts[i-1]) - hs[i-1]*ms[i-1];
        ms[i] = hs[i]/ls[i];
        zs[i] = (as[i] - hs[i-1]*zs[i-1])/ls[i];
      }
      ls[n] = 1;
      zs[n] = 0;
      var bs = new Array(n);
      var cs = new Array(n+1);
      cs[n] = 0;
      for (i = n-1; i >= 0; i--) {
        var h = hs[i], c1 = cs[i+1], c0 = h*h*zs[i] - ms[i]*c1;
        cs[i] = c0;
        bs[i] = (xs[i+1] - xs[i]) - (c1 + 2*c0)/3;
      }
      var p1s = new Array(n);
      var p2s = new Array(n);
      for (i = 0; i < n; i++) {
        var a = xs[i], b = bs[i], c = cs[i];
        p1s[i] = a + b/3;
        p2s[i] = a + (2*b + c)/3;
      }
      return [p1s, p2s];
    }
  });
  
  // xypic.Curve.CubicBeziers factory class
  xypic.Curve.CubicBSpline = MathJax.Object.Subclass({
    Init: function (s, intCps, e) {
      if (intCps.length < 1) {
        throw xypic.ExecutionError("the number of internal control points of cubic B-spline must be greater than or equal to 1");
      }
      
      var controlPoints = [];
      controlPoints.push(s);
      for (var i = 0, l = intCps.length; i < l; i++) {
        controlPoints.push(intCps[i]);
      }
      controlPoints.push(e);
      this.cps = controlPoints;
      
      var n = this.cps.length - 1;
      var cps = function (i) {
        if (i < 0) {
          return controlPoints[0];
        } else if (i > n) {
          return controlPoints[n];
        } else {
          return controlPoints[i];
        }
      }
      var N = function (t) {
        var s = Math.abs(t);
        if (s <= 1) {
          return (3*s*s*s - 6*s*s + 4)/6;
        } else if (s <= 2) {
          return -(s-2)*(s-2)*(s-2)/6;
        } else {
          return 0;
        }
      }
      this.px = function (t) {
        var s = (n+2)*t-1;
        var minj = Math.ceil(s-2);
        var maxj = Math.floor(s+2);
        var p = 0;
        for (var j = minj; j <= maxj; j++) {
          p += N(s-j)*cps(j).x;
        }
        return p;
      }
      this.py = function (t) {
        var s = (n+2)*t-1;
        var minj = Math.ceil(s-2);
        var maxj = Math.floor(s+2);
        var p = 0;
        for (var j = minj; j <= maxj; j++) {
          p += N(s-j)*cps(j).y;
        }
        return p;
      }
      var dN = function (t) {
        var u = (t>0? 1 : (t<0? -1 : 0));
        var s = Math.abs(t);
        if (s <= 1) {
          return u*(3*s*s - 4*s)/2;
        } else if (s <= 2) {
          return -u*(s-2)*(s-2)/2;
        } else {
          return 0;
        }
      }
      this.dpx = function (t) {
        var s = (n+2)*t-1;
        var minj = Math.ceil(s-2);
        var maxj = Math.floor(s+2);
        var p = 0;
        for (var j = minj; j <= maxj; j++) {
          p += dN(s-j)*cps(j).x;
        }
        return p;
      }
      this.dpy = function (t) {
        var s = (n+2)*t-1;
        var minj = Math.ceil(s-2);
        var maxj = Math.floor(s+2);
        var p = 0;
        for (var j = minj; j <= maxj; j++) {
          p += dN(s-j)*cps(j).y;
        }
        return p;
      }
    },
    position: function (t) {
      return xypic.Frame.Point(this.px(t), this.py(t));
    },
    angle: function (t) {
      return Math.atan2(this.dpy(t), this.dpx(t));
    },
    toCubicBeziers: function () {
      var cbs = [];
      var cps = this.cps;
      
      var cp0 = cps[0];
      var cp1 = cps[1];
      var cp2 = cps[2];
      var p0x = cp0.x;
      var p0y = cp0.y;
      var p1x = p0x+(cp1.x-p0x)/3;
      var p1y = p0y+(cp1.y-p0y)/3;
      var p2x = p0x+(cp1.x-p0x)*2/3;
      var p2y = p0y+(cp1.y-p0y)*2/3;
      var n1x = cp1.x+(cp2.x-cp1.x)/3;
      var n1y = cp1.y+(cp2.y-cp1.y)/3;
      var p3x = (p2x+n1x)/2;
      var p3y = (p2y+n1y)/2;
      var p0 = cp0;
      var p1 = xypic.Frame.Point(p1x, p1y);
      var p2 = xypic.Frame.Point(p2x, p2y);
      var p3 = xypic.Frame.Point(p3x, p3y);
      var cb = xypic.Curve.CubicBezier(p0, p1, p2, p3);
      cbs.push(cb);
      
      var len = this.cps.length - 1;
      for (var i=2; i < len; i++) {
        cp0 = cp1;
        cp1 = cp2;
        cp2 = cps[i+1];
        p0x = p3x;
        p0y = p3y;
        p1x = 2*p3x - p2x;
        p1y = 2*p3y - p2y;
        p2x = cp0.x+(cp1.x-cp0.x)*2/3;
        p2y = cp0.y+(cp1.y-cp0.y)*2/3;
        n1x = cp1.x+(cp2.x-cp1.x)/3;
        n1y = cp1.y+(cp2.y-cp1.y)/3;
        p3x = (p2x+n1x)/2;
        p3y = (p2y+n1y)/2;
        p0 = p3;
        p1 = xypic.Frame.Point(p1x, p1y);
        p2 = xypic.Frame.Point(p2x, p2y);
        p3 = xypic.Frame.Point(p3x, p3y);
        cb = xypic.Curve.CubicBezier(p0, p1, p2, p3);
        cbs.push(cb);
      }
      
      cp0 = cp1;
      cp1 = cp2;
      p0x = p3x;
      p0y = p3y;
      p1x = 2*p3x - p2x;
      p1y = 2*p3y - p2y;
      p2x = cp0.x+(cp1.x-cp0.x)*2/3;
      p2y = cp0.y+(cp1.y-cp0.y)*2/3;
      p3x = cp1.x;
      p3y = cp1.y;
      p0 = p3;
      p1 = xypic.Frame.Point(p1x, p1y);
      p2 = xypic.Frame.Point(p2x, p2y);
      p3 = xypic.Frame.Point(p3x, p3y);
      cb = xypic.Curve.CubicBezier(p0, p1, p2, p3);
      cbs.push(cb);
      
      return cbs;
    },
    countOfSegments: function () { return this.cps.length - 1; }
  });
  
  xypic.Curve.Line = MathJax.Object.Subclass({
    Init: function (s, e) {
      this.s = s;
      this.e = e;
    },
    position: function (t) {
      return xypic.Frame.Point(
        this.s.x + t * (this.e.x - this.s.x),
        this.s.y + t * (this.e.y - this.s.y)
      );
    },
    slice: function (t0, t1) {
      if (t0 >= t1) {
        return undefined;
      }
      
      if (t0 < 0) {
        t0 = 0;
      }
      
      if (t1 > 1) {
        t1 = 1;
      }
      
      if (t0 === 0 && t1 === 1) {
        return this;
      }
      
      var s = this.s;
      var e = this.e;
      var dx = e.x - s.x;
      var dy = e.y - s.y;
      var newS = xypic.Frame.Point(s.x + t0 * dx, s.y + t0 * dy);
      var newE = xypic.Frame.Point(s.x + t1 * dx, s.y + t1 * dy);
      return xypic.Curve.Line(newS, newE);
    },
    tOfIntersections: function (frame) {
      if (frame.isPoint()) {
        return []; // CAUTION: Point does not intersect with any curves.
      }
      
      var s = this.s;
      var e = this.e;
      if (frame.isRect()) {
        // find starting edge point
        var rx = frame.x + frame.r;
        var lx = frame.x - frame.l;
        var uy = frame.y + frame.u;
        var dy = frame.y - frame.d;
        
        var a0x = s.x;
        var a0y = s.y;
        var a1x = e.x - a0x;
        var a1y = e.y - a0y;
        var px = function (t) { return a0x + t * a1x; }
        var py = function (t) { return a0y + t * a1y; }
        
        var ts = [];
        var tsCandidate;
        tsCandidate = xypic.Curve.solutionsOfLinearEq(a1x, a0x - rx);
        tsCandidate = tsCandidate.concat(xypic.Curve.solutionsOfLinearEq(a1x, a0x - lx));
        for (var i = 0; i < tsCandidate.length; i++) {
          var t = tsCandidate[i];
          var y = py(t);
          if (y >= dy && y <= uy) {
            ts.push(t);
          }
        }
        tsCandidate = xypic.Curve.solutionsOfLinearEq(a1y, a0y - uy);
        tsCandidate = tsCandidate.concat(xypic.Curve.solutionsOfLinearEq(a1y, a0y - dy));
        for (var i = 0; i < tsCandidate.length; i++) {
          var t = tsCandidate[i];
          var x = px(t);
          if (x >= lx && x <= rx) {
            ts.push(t);
          }
        }
        
        return ts;
      } else if (frame.isCircle()) {
        var pi = Math.PI;
        var l = frame.l;
        var r = frame.r;
        var u = frame.u;
        var d = frame.d;
        var x0 = frame.x;
        var y0 = frame.y;
        var cx = x0 + (r - l) / 2;
        var cy = y0 + (u - d) / 2;
        var rx = (l + r) / 2;
        var ry = (u + d) / 2;
        
        var sx = s.x;
        var sy = s.y;
        var ex = e.x;
        var ey = e.y;
        
        var dx = ex - sx;
        var dy = ey - sy;
        var a0 = dy;
        var b0 = -dx;
        var c0 = dx * sy - dy * sx;
        var a = a0 * rx;
        var b = b0 * ry;
        var c = c0 * rx + (rx - ry) * b0 * cy;
        var aabb = a * a + b * b;
        var d = a * cx + b * cy + c;
        var e = -d / aabb;
        var ff = aabb * rx * rx - d * d;
        if (ff < 0) {
          return [];
        }
        var f = Math.sqrt(ff) / aabb;
        
        var xp = a * e + b * f + cx;
        var yp = b * e - a * f + cy;
        var xm = a * e - b * f + cx;
        var ym = b * e + a * f + cy;
        
        var eps = ry / rx;
        var xp0 = xp;
        var yp0 = eps * (yp - cy) + cy;
        var xm0 = xm;
        var ym0 = eps * (ym - cy) + cy;
        
        var tp, tm;
        if (Math.abs(dx) > Math.abs(dy)) {
          tp = (xp0 - sx) / dx;
          tm = (xm0 - sx) / dx;
        } else {
          tp = (yp0 - sy) / dy;
          tm = (ym0 - sy) / dy;
        }
        
        var ts = [];
        if (tp >= 0 && tp <= 1) {
          ts.push(tp);
        }
        if (tm >= 0 && tm <= 1) {
          ts.push(tm);
        }
        return ts;
      }
    },
    toShape: function (context, object, main, variant) {
      // 多重線の幅、点線・破線の幅の基準
      var env = context.env;
      var thickness = AST.xypic.thickness;
      var s = this.s;
      var e = this.e;
      if (s.x !== e.x || s.y !== e.y) {
        var dx = e.x - s.x;
        var dy = e.y - s.y;
        var angle = Math.atan2(dy, dx);
        var vshift;
        var shape = xypic.Shape.none;
        switch (main) {
          case "=":
            main = "-";
            variant = "2";
            break;
          case "==":
            main = "--";
            variant = "2";
            break;
          case ':':
          case '::':
            main = ".";
            variant = "2";
            break;
        }
        
        switch (main) {
          case '':
            // draw invisible line
            env.angle = angle;
            env.lastCurve = xypic.LastCurve.Line(s, e, env.p, env.c, undefined);
            return shape;
            
          case '-':
          case '.':
          case '..':
            switch (variant) {
              case "2":
                vshift = thickness / 2;
                break;
                
              case "3":
                vshift = thickness;
                break;
                
              default:
                vshift = 0;
                break;
            }
            break;
            
          case '--':
            var dash = 3 * thickness;
            var len = Math.sqrt(dx * dx + dy * dy);
            if (len >= dash) {
              switch (variant) {
                case "2":
                  vshift = thickness / 2;
                  break;
                  
                case "3":
                  vshift = thickness;
                  break;
                  
                default:
                  vshift = 0;
              }
            }
            break;
            
          case '~':
          case '~~':
            switch (variant) {
              case "2":
                vshift = 1.5 * thickness;
                break;
              case "3":
                vshift = 2 * thickness;
                break;
              default:
                vshift = 0
            }
            break;
            
          default:
            // connect by arrowheads
            var arrowBBox = object.boundingBox(context);
            if (arrowBBox == undefined) {
              env.angle = 0;
              env.lastCurve = xypic.LastCurve.none;
              return xypic.Shape.none;
            }
            
            var arrowLen = arrowBBox.l + arrowBBox.r;
            if (arrowLen == 0) {
              arrowLen = AST.xypic.strokeWidth;
            }
            
            var len = Math.sqrt(dx * dx + dy * dy);
            var n = Math.floor(len / arrowLen);
            if (n == 0) {
              env.angle = 0;
              env.lastCurve = xypic.LastCurve.none;
              return xypic.Shape.none;
            }
            
            vshift = Math.max(arrowBBox.u, arrowBBox.d);
        }
        
        if (vshift !== undefined) {
          var bbox = this.boundingBox(vshift);
          shape = xypic.Shape.LineShape(this, object, main, variant, bbox);
          context.appendShapeToFront(shape);
          
          env.angle = angle;
          env.lastCurve = xypic.LastCurve.Line(s, e, env.p, env.c, shape);
          return shape;
        }
      }
      
      env.angle = 0;
      env.lastCurve = xypic.LastCurve.none;
      return xypic.Shape.none;
    },
    boundingBox: function (vshift) {
      var s = this.s;
      var e = this.e;
      var dx = e.x - s.x;
      var dy = e.y - s.y;
      var angle = Math.atan2(dy, dx);
      var cx = vshift * Math.cos(angle + Math.PI/2);
      var cy = vshift * Math.sin(angle + Math.PI/2);
      return xypic.Frame.Rect(s.x, s.y, {
        l:s.x-Math.min(s.x+cx, s.x-cx, e.x+cx, e.x-cx),
        r:Math.max(s.x+cx, s.x-cx, e.x+cx, e.x-cx)-s.x,
        u:Math.max(s.y+cy, s.y-cy, e.y+cy, e.y-cy)-s.y,
        d:s.y-Math.min(s.y+cy, s.y-cy, e.y+cy, e.y-cy)
      });
    },
    drawLine: function (svg, object, main, variant, holeRanges) {
      if (holeRanges.isEmpty) {
        this._drawLine(svg, object, main, variant);
      } else {
        var clippingRanges = xypic.Range(0, 1).differenceRanges(holeRanges);
        var self = this;
        clippingRanges.foreach(function (range) {
          self.slice(range.start, range.end)._drawLine(svg, object, main, variant);
        });
      }
    },
    _drawLine: function (svg, object, main, variant) {
      // 多重線の幅、点線・破線の幅の基準
      var t = AST.xypic.thickness;
      var s = this.s;
      var e = this.e;
      if (s.x !== e.x || s.y !== e.y) {
        var dx = e.x - s.x;
        var dy = e.y - s.y;
        var angle = Math.atan2(dy, dx);
        var shift = { x:0, y:0 };
        
        switch (main) {
          case '':
            // draw nothing
            break;
          case '-':
            this.drawStraightLine(svg, s, e, shift, angle, t, variant, "");
            break;
          case '=':
            this.drawStraightLine(svg, s, e, shift, angle, t, "2", "");
            break;
          case '.':
          case '..':
            this.drawStraightLine(svg, s, e, shift, angle, t, variant, AST.xypic.dottedDasharray);
            break;
          case ':':
          case '::':
            this.drawStraightLine(svg, s, e, shift, angle, t, "2", AST.xypic.dottedDasharray);
            break;
          case '--':
          case '==':
            var len = Math.sqrt(dx * dx + dy * dy);
            var dash = 3 * t;
            if (len >= dash) {
              var shiftLen = (len - dash) / 2 - Math.floor((len - dash) / 2 / dash) * dash;
              shift = { x:shiftLen * Math.cos(angle), y:shiftLen * Math.sin(angle) };
              this.drawStraightLine(svg, s, e, shift, angle, t, (main === "=="? "2" : variant), xypic.em2px(dash) + " " + xypic.em2px(dash));
            }
            break;
          case '~':
            var len = Math.sqrt(dx * dx + dy * dy);
            var wave = 4 * t;
            if (len >= wave) {
              var n = Math.floor(len / wave);
              var shiftLen = (len - n * wave) / 2;
              shift = { x:shiftLen * Math.cos(angle), y:shiftLen * Math.sin(angle) };
              var cx = t * Math.cos(angle + Math.PI / 2);
              var cy = t * Math.sin(angle + Math.PI / 2);
              var tx = t * Math.cos(angle);
              var ty = t * Math.sin(angle);
              var sx = s.x + shift.x;
              var sy = -s.y - shift.y;
              var d = "M" + xypic.em2px(sx) + "," + xypic.em2px(sy) +
                " Q" + xypic.em2px(sx + tx + cx) + "," + xypic.em2px(sy - ty - cy) +
                " " + xypic.em2px(sx + 2 * tx) + "," + xypic.em2px(sy - 2 * ty) +
                " T" + xypic.em2px(sx + 4 * tx) + "," + xypic.em2px(sy - 4 * ty);
              for (var i = 1; i < n; i++) {
                d += " T" + xypic.em2px(sx + (4 * i + 2) * tx) + "," + xypic.em2px(sy - (4 * i + 2) * ty) +
                  " T" + xypic.em2px(sx + (4 * i + 4) * tx) + "," + xypic.em2px(sy - (4 * i + 4) * ty);
              }
              this.drawSquigglyLineShape(svg, d, s, e, cx, cy, variant);
            }
            break;
          case '~~':
            var len = Math.sqrt(dx * dx + dy * dy);
            var wave = 4 * t;
            if (len >= wave) {
              var n = Math.floor((len - wave) / 2 / wave);
              var shiftLen = (len - wave) / 2 - n * wave;
              shift = { x:shiftLen * Math.cos(angle), y:shiftLen * Math.sin(angle) };
              var cx = t * Math.cos(angle + Math.PI / 2);
              var cy = t * Math.sin(angle + Math.PI / 2);
              var tx = t * Math.cos(angle);
              var ty = t * Math.sin(angle);
              var sx = s.x + shift.x;
              var sy = -s.y - shift.y;
              var d = "";
              for (var i = 0; i <= n; i++) {
                d += " M" + xypic.em2px(sx + 8 * i * tx) + "," + xypic.em2px(sy - 8 * i * ty) + 
                  " Q" + xypic.em2px(sx + (8 * i + 1) * tx + cx) + "," + xypic.em2px(sy - (8 * i + 1) * ty - cy) + 
                  " " + xypic.em2px(sx + (8 * i + 2) * tx) + "," + xypic.em2px(sy - (8 * i + 2) * ty) + 
                  " T" + xypic.em2px(sx + (8 * i + 4) * tx) + "," + xypic.em2px(sy - (8 * i + 4) * ty);
              }
              this.drawSquigglyLineShape(svg, d, s, e, cx, cy, variant);
            }
            break;
            
          default:
            // connect by arrowheads
            var dummyEnv = xypic.Env();
            dummyEnv.c = xypic.Env.originPosition;
            var dummyContext = xypic.DrawingContext(xypic.Shape.none, dummyEnv);
            var arrowBBox = object.boundingBox(dummyContext);
            if (arrowBBox == undefined) {
              return;
            }
            
            var arrowLen = arrowBBox.l + arrowBBox.r;
            if (arrowLen == 0) {
              arrowLen = AST.xypic.strokeWidth;
            }
            
            var len = Math.sqrt(dx * dx + dy * dy);
            var n = Math.floor(len / arrowLen);
            if (n == 0) {
              return;
            }
            
            var shiftLen = (len - n * arrowLen) / 2;
            var cos = Math.cos(angle), sin = Math.sin(angle);
            var ac = arrowLen * cos, as = arrowLen * sin;
            var startX = s.x + (shiftLen + arrowBBox.l) * cos;
            var startY = s.y + (shiftLen + arrowBBox.l) * sin;
            
            var dummyContext = xypic.DrawingContext(xypic.Shape.none, dummyEnv);
            for (var i = 0; i < n; i++) {
              dummyEnv.c = xypic.Frame.Point(startX + i * ac, startY + i * as);
              dummyEnv.angle = angle;
              object.toDropShape(dummyContext).draw(svg);
            }
        }
      }
    },
    drawStraightLine: function (svg, s, e, shift, angle, t, variant, dasharray) {
      if (variant === "3") {
        var cx = t*Math.cos(angle+Math.PI/2);
        var cy = t*Math.sin(angle+Math.PI/2);
        svg.createSVGElement("line", {
          x1:xypic.em2px(s.x+shift.x), y1:-xypic.em2px(s.y+shift.y),
          x2:xypic.em2px(e.x), y2:-xypic.em2px(e.y), 
          "stroke-dasharray":dasharray
        });
        svg.createSVGElement("line", {
          x1:xypic.em2px(s.x+cx+shift.x), y1:-xypic.em2px(s.y+cy+shift.y),
          x2:xypic.em2px(e.x+cx), y2:-xypic.em2px(e.y+cy), 
          "stroke-dasharray":dasharray
        });
        svg.createSVGElement("line", {
          x1:xypic.em2px(s.x-cx+shift.x), y1:-xypic.em2px(s.y-cy+shift.y),
          x2:xypic.em2px(e.x-cx), y2:-xypic.em2px(e.y-cy), 
          "stroke-dasharray":dasharray
        });
      } else if (variant === "2") {
        var cx = t*Math.cos(angle+Math.PI/2)/2;
        var cy = t*Math.sin(angle+Math.PI/2)/2;
        svg.createSVGElement("line", {
          x1:xypic.em2px(s.x+cx+shift.x), y1:-xypic.em2px(s.y+cy+shift.y),
          x2:xypic.em2px(e.x+cx), y2:-xypic.em2px(e.y+cy), 
          "stroke-dasharray":dasharray
        });
        svg.createSVGElement("line", {
          x1:xypic.em2px(s.x-cx+shift.x), y1:-xypic.em2px(s.y-cy+shift.y),
          x2:xypic.em2px(e.x-cx), y2:-xypic.em2px(e.y-cy), 
          "stroke-dasharray":dasharray
        });
      } else {
        svg.createSVGElement("line", {
          x1:xypic.em2px(s.x+shift.x), y1:-xypic.em2px(s.y+shift.y),
          x2:xypic.em2px(e.x), y2:-xypic.em2px(e.y), 
          "stroke-dasharray":dasharray
        });
      }
    },
    drawSquigglyLineShape: function (svg, d, s, e, cx, cy, variant) {
      var g1, g2;
      if (variant === "3") {
        svg.createSVGElement("path", { d:d });
        g1 = svg.createGroup(svg.transformBuilder().translate(cx, cy));
        g1.createSVGElement("path", { d:d });
        g2 = svg.createGroup(svg.transformBuilder().translate(-cx, -cy));
        g2.createSVGElement("path", { d:d });
      } else if (variant === "2") {
        g1 = svg.createGroup(svg.transformBuilder().translate(cx / 2, cy / 2));
        g1.createSVGElement("path", { d:d });
        g2 = svg.createGroup(svg.transformBuilder().translate(-cx / 2, -cy / 2));
        g2.createSVGElement("path", { d:d });
      } else {
        svg.createSVGElement("path", { d:d });
      }
    }
  });
  
  xypic.CurveSegment = MathJax.Object.Subclass({
    bezierFatLine: function (n) {
      var p0 = this.cps[0], pn = this.cps[n];
      var a, b, c;
      if (p0.x !== pn.x || p0.y !== pn.y) {
        a = p0.y-pn.y;
        b = pn.x-p0.x;
        l = Math.sqrt(a*a+b*b);
        a /= l;
        b /= l;
        c = (p0.x*pn.y-p0.y*pn.x)/l;
      } else {
        var angle = this.bezier.angle(this.tmin);
        a = -Math.sin(angle);
        b = Math.cos(angle);
        c = -a*this.cp0.x-b*this.cp0.y;
      }
      
      var cmin = c, cmax = c;
      for (var i = 1; i < n; i++) {
        var ci = -a*this.cps[i].x-b*this.cps[i].y;
        if (ci > cmax) {
          cmax = ci;
        } else if (ci < cmin) {
          cmin = ci;
        }
      }
      return {min:[a, b, cmin], max:[a, b, cmax]};
    }, 
    clippedLineRange: function (ps, lineMin, lineMax) {
      var n = ps.length - 1;
      var es = new Array(n+1);
      var extProd = xypic.Util.extProd;
      for (var i = 0; i <= n; i++) {
        es[i] = [i/n, -lineMin[0]*ps[i].x-lineMin[1]*ps[i].y-lineMin[2], 1];
      }
      
      var vminAgainstLineMin, vmaxAgainstLineMin, t;
      if (es[0][1] < 0) {
        var allLiesBelow = true;
        for (i = 1; i <= n; i++) {
          var l0i = extProd(es[0], es[i]);
          v = -l0i[2]/l0i[0];
          if (v > 0 && v < 1 && (vminAgainstLineMin === undefined || v < vminAgainstLineMin)) {
            vminAgainstLineMin = v;
          }
          if (es[i][1] >= 0) {
            allLiesBelow = false;
          }
        }
        if (allLiesBelow) {
          // clip away everything.
          return undefined;
        }
      } else {
        vminAgainstLineMin = 0;
      }
      if (es[n][1] < 0) {
        for (i = 0; i < n; i++) {
          var lni = extProd(es[n], es[i]);
          v = -lni[2]/lni[0];
          if (v > 0 && v < 1 && (vmaxAgainstLineMin === undefined || v > vmaxAgainstLineMin)) {
            vmaxAgainstLineMin = v;
          }
        }
      } else {
        vmaxAgainstLineMin = 1;
      }
      
      for (i = 0; i <= n; i++) {
        es[i] = [i/n, lineMax[0]*ps[i].x+lineMax[1]*ps[i].y+lineMax[2], 1];
      }
      
      var vminAgainstLineMax, vmaxAgainstLineMax;
      if (es[0][1] < 0) {
        var allLiesAbove = true;
        for (i = 1; i <= n; i++) {
          var l0i = extProd(es[0], es[i]);
          v = -l0i[2]/l0i[0];
          if (v > 0 && v < 1 && (vminAgainstLineMax === undefined || v < vminAgainstLineMax)) {
            vminAgainstLineMax = v;
          }
          if (es[i][1] >= 0) {
            allLiesAbove = false;
          }
        }
        if (allLiesAbove) {
          // clip away everything.
          return undefined;
        }
      } else {
        vminAgainstLineMax = 0;
      }
      if (es[n][1] < 0) {
        for (i = 0; i < n; i++) {
          var lni = extProd(es[n], es[i]);
          v = -lni[2]/lni[0];
          if (v > 0 && v < 1 && (vmaxAgainstLineMax === undefined || v > vmaxAgainstLineMax)) {
            vmaxAgainstLineMax = v;
          }
        }
      } else {
        vmaxAgainstLineMax = 1;
      }
      
      var vmin = Math.max(vminAgainstLineMin, vminAgainstLineMax);
      var vmax = Math.min(vmaxAgainstLineMin, vmaxAgainstLineMax);
      return {min:this.tmin + vmin*(this.tmax - this.tmin), max:this.tmin + vmax*(this.tmax - this.tmin)};
    }
  }, {
    findIntersections: function (segment0, segment1) {
      var n = xypic.CurveSegment.maxIterations;
      var acc = xypic.CurveSegment.goalAccuracy;
      var queue = [[segment0, segment1, false]];
      var i = 0;
      var intersections = [];
      while (i < n && queue.length > 0) {
        i++;
        var head = queue.shift();
        var segment0 = head[0];
        var segment1 = head[1];
        var swapped = head[2];
        
//        segment0.drawFatLine();
        
        var fatLine = segment0.fatLine();
        var tminMax = segment1.clippedRange(fatLine.min, fatLine.max);
        if (tminMax == undefined) {
          // clip away everything
          continue;
        }
        
        var tmin = tminMax.min;
        var tmax = tminMax.max;
        var tlen = tmax - tmin;
        if (tlen < acc && segment0.paramLength() < acc) {
          // intersection found
          if (swapped) {
            intersections.push([segment1.clip(tmin, tmax).paramRange(), segment0.paramRange()]);
          } else {
            intersections.push([segment0.paramRange(), segment1.clip(tmin, tmax).paramRange()]);
          }
          continue;
        }
        if (tlen <= segment1.paramLength() * 0.8) {
          queue.push([segment1.clip(tmin, tmax), segment0, !swapped]);
        } else {
          // subdivision
          if (tlen > segment0.paramLength()) {
            var tmid = (tmax + tmin)/2;
            queue.push([segment1.clip(tmin, tmid), segment0, !swapped]);
            queue.push([segment1.clip(tmid, tmax), segment0, !swapped]);
          } else {
            var newSegment = segment1.clip(tmin, tmax);
            var range0 = segment0.paramRange();
            var mid0 = (range0.min + range0.max)/2;
            queue.push([newSegment, segment0.clip(range0.min, mid0), !swapped]);
            queue.push([newSegment, segment0.clip(mid0, range0.max), !swapped]);
          }
        }
      }
      return intersections;
    },
    maxIterations: 30,
    goalAccuracy: 1e-4
  });
  
  xypic.CurveSegment.Line = xypic.CurveSegment.Subclass({
    Init: function (p0, p1, tmin, tmax) {
      this.p0 = p0;
      this.p1 = p1;
      this.tmin = tmin;
      this.tmax = tmax;
    },
    paramRange: function () { return {min:this.tmin, max:this.tmax}; },
    paramLength: function () { return this.tmax - this.tmin; },
    containsParam: function (t) { return t >= this.tmin && t <= this.tmax; }, 
    position: function (t) {
      return {
        x:this.p0.x + t*(this.p1.x - this.p0.x),
        y:this.p0.y + t*(this.p1.y - this.p0.y)
      };
    },
    fatLine: function () {
      var a = (this.p1.y - this.p0.y), b = (this.p0.x - this.p1.x), c = this.p1.x*this.p0.y - this.p0.x*this.p1.y;
      var l = Math.sqrt(a * a + b * b);
      if (l === 0) {
        a = 1;
        b = 0;
      } else {
        a /= l;
        b /= l;
        c /= l;
      }
      return {min:[a, b, c], max:[a, b, c]};
    },
    clip: function (tmin, tmax) {
      return xypic.CurveSegment.Line(this.p0, this.p1, tmin, tmax);
    },
    clippedRange: function (lineMin, lineMax) {
      var ps = new Array(2);
      ps[0] = this.position(this.tmin);
      ps[1] = this.position(this.tmax);
      return this.clippedLineRange(ps, lineMin, lineMax);
    },
    drawFatLine: function () {
      var fatLine = this.fatLine();
      var lmin = fatLine.min;
      var y = function (x, l) {
        return -(x*l[0] + l[2])/l[1];
      }
      var xmin = this.p0.x;
      var xmax = this.p1.x;
      xypic.svgForDebug.createSVGElement("line", {
        x1:xypic.em2px(xmin), y1:-xypic.em2px(y(xmin, lmax)),
        x2:xypic.em2px(xmax), y2:-xypic.em2px(y(xmax, lmax)),
        "stroke-width":xypic.em2px(0.02 * xypic.oneem), stroke:"red"
      });
    }
  });

  xypic.CurveSegment.QuadBezier = xypic.CurveSegment.Subclass({
    Init: function (bezier, tmin, tmax) {
      this.bezier = bezier;
      this.tmin = tmin;
      this.tmax = tmax;
      this.cp0 = bezier.position(tmin);
      this.cp1 = xypic.Frame.Point(
        (1-tmax)*(1-tmin)*bezier.cp0.x + (tmin+tmax-2*tmin*tmax)*bezier.cp1.x + tmin*tmax*bezier.cp2.x,
        (1-tmax)*(1-tmin)*bezier.cp0.y + (tmin+tmax-2*tmin*tmax)*bezier.cp1.y + tmin*tmax*bezier.cp2.y
      );
      this.cp2 = bezier.position(tmax);
      this.cps = [this.cp0, this.cp1, this.cp2];
    },
    paramRange: function () { return {min:this.tmin, max:this.tmax}; },
    paramLength: function () { return this.tmax - this.tmin; },
    fatLine: function () { return this.bezierFatLine(2); },
    clip: function (tmin, tmax) {
      return xypic.CurveSegment.QuadBezier(this.bezier, tmin, tmax);
    },
    clippedRange: function (lineMin, lineMax) {
      return this.clippedLineRange(this.cps, lineMin, lineMax);
    },
    drawFatLine: function () {
      var fatLine = this.fatLine();
      var lmin = fatLine.min;
      var lmax = fatLine.max;
      var y = function (x, l) {
        return -(x*l[0] + l[2])/l[1];
      }
      var xmin = this.cp0.x
      var xmax = this.cp2.x
      xypic.svgForDebug.createSVGElement("line", {
        x1:xypic.em2px(xmin), y1:-xypic.em2px(y(xmin, lmin)),
        x2:xypic.em2px(xmax), y2:-xypic.em2px(y(xmax, lmin)),
        "stroke-width":xypic.em2px(0.02 * xypic.oneem), stroke:"blue"
      });
      xypic.svgForDebug.createSVGElement("line", {
        x1:xypic.em2px(xmin), y1:-xypic.em2px(y(xmin, lmax)),
        x2:xypic.em2px(xmax), y2:-xypic.em2px(y(xmax, lmax)),
        "stroke-width":xypic.em2px(0.02 * xypic.oneem), stroke:"red"
      });
    }
  });
  
  xypic.CurveSegment.CubicBezier = xypic.CurveSegment.Subclass({
    Init: function (bezier, tmin, tmax) {
      this.bezier = bezier;
      this.tmin = tmin;
      this.tmax = tmax;
      this.cp0 = bezier.position(tmin);
      this.cp1 = xypic.Frame.Point(
        (1-tmax)*(1-tmin)*(1-tmin)*bezier.cp0.x + (1-tmin)*(2*tmin+tmax-3*tmin*tmax)*bezier.cp1.x + tmin*(2*tmax+tmin-3*tmin*tmax)*bezier.cp2.x + tmin*tmin*tmax*bezier.cp3.x,
        (1-tmax)*(1-tmin)*(1-tmin)*bezier.cp0.y + (1-tmin)*(2*tmin+tmax-3*tmin*tmax)*bezier.cp1.y + tmin*(2*tmax+tmin-3*tmin*tmax)*bezier.cp2.y + tmin*tmin*tmax*bezier.cp3.y
      );
      this.cp2 = xypic.Frame.Point(
        (1-tmin)*(1-tmax)*(1-tmax)*bezier.cp0.x + (1-tmax)*(2*tmax+tmin-3*tmin*tmax)*bezier.cp1.x + tmax*(2*tmin+tmax-3*tmin*tmax)*bezier.cp2.x + tmin*tmax*tmax*bezier.cp3.x,
        (1-tmin)*(1-tmax)*(1-tmax)*bezier.cp0.y + (1-tmax)*(2*tmax+tmin-3*tmin*tmax)*bezier.cp1.y + tmax*(2*tmin+tmax-3*tmin*tmax)*bezier.cp2.y + tmin*tmax*tmax*bezier.cp3.y
      );
      this.cp3 = bezier.position(tmax);
      this.cps = [this.cp0, this.cp1, this.cp2, this.cp3];
    },
    paramRange: function () { return {min:this.tmin, max:this.tmax}; },
    paramLength: function () { return this.tmax - this.tmin; },
    fatLine: function () { return this.bezierFatLine(3); },
    clip: function (tmin, tmax) {
      return xypic.CurveSegment.CubicBezier(this.bezier, tmin, tmax);
    },
    clippedRange: function (lineMin, lineMax) {
      return this.clippedLineRange(this.cps, lineMin, lineMax);
    },
    drawFatLine: function () {
      var fatLine = this.fatLine();
      var lmin = fatLine.min;
      var lmax = fatLine.max;
      var y = function (x, l) {
        return -(x*l[0] + l[2])/l[1];
      }
      var xmin = this.cp0.x
      var xmax = this.cp3.x
      xypic.svgForDebug.createSVGElement("line", {
        x1:xypic.em2px(xmin), y1:-xypic.em2px(y(xmin, lmin)),
        x2:xypic.em2px(xmax), y2:-xypic.em2px(y(xmax, lmin)),
        "stroke-width":xypic.em2px(0.02 * xypic.oneem), stroke:"blue"
      });
      xypic.svgForDebug.createSVGElement("line", {
        x1:xypic.em2px(xmin), y1:-xypic.em2px(y(xmin, lmax)),
        x2:xypic.em2px(xmax), y2:-xypic.em2px(y(xmax, lmax)),
        "stroke-width":xypic.em2px(0.02 * xypic.oneem), stroke:"red"
      });
    }
  });
  
  xypic.CurveSegment.Arc = xypic.CurveSegment.Subclass({
    Init: function (x, y, rx, ry, angleMin, angleMax) {
      this.x = x;
      this.y = y;
      this.rx = rx;
      this.ry = ry;
      this.angleMin = angleMin;
      this.angleMax = angleMax;
    },
    paramRange: function () { return { min:this.angleMin, max:this.angleMax }; },
    paramLength: function () { return this.angleMax - this.angleMin; },
    normalizeAngle: function (angle) {
      angle = angle % 2 * Math.PI;
      if (angle > Math.PI) {
        return angle - 2 * Math.PI;
      }
      if (angle < -Math.PI) {
        return angle + 2 * Math.PI;
      }
      return angle;
    },
    containsParam: function (angle) { return angle >= this.angleMin && angle <= this.angleMax; }, 
    fatLine: function () {
      var rx = this.rx;
      var ry = this.ry;
      var tp = (this.angleMax + this.angleMin) / 2;
      var tm = (this.angleMax - this.angleMin) / 2;
      var cosp = Math.cos(tp), sinp = Math.sin(tp);
      var r = Math.sqrt(rx * rx * sinp * sinp + ry * ry * cosp * cosp);
      if (r < AST.xypic.machinePrecision) {
        var Lmin = [1, 0, this.x * ry * cosp + this.y * rx * sinp + rx * ry * Math.cos(tm)];
        var Lmax = [1, 0, this.x * ry * cosp + this.y * rx * sinp + rx * ry];
      } else {
        var rrx = rx / r;
        var rry = ry / r;
        var Lmin = [-rry * cosp, -rrx * sinp, this.x * rry * cosp + this.y * rrx * sinp + rx * ry / r * Math.cos(tm)];
        var Lmax = [-rry * cosp, -rrx * sinp, this.x * rry * cosp + this.y * rrx * sinp + rx * ry / r];
      }
      return { min:Lmin, max:Lmax };
    },
    clip: function (angleMin, angleMax) {
      return xypic.CurveSegment.Arc(this.x, this.y, this.rx, this.ry, angleMin, angleMax);
    },
    toCircleLine: function (line, x0, y0, rx, ry) {
      var a = line[0];
      var b = line[1];
      var c = line[2];
      var a2 = a * rx;
      var b2 = b * ry;
      var c2 = c * rx + (rx - ry) * b * y0;
      var l = Math.sqrt(a2 * a2 + b2 * b2);
      if (l < AST.xypic.machinePrecision) {
        a2 = 1;
        b2 = 0;
      } else {
        a2 /= l;
        b2 /= l;
        c2 /= l;
      }
      return [a2, b2, c2];
    },
    clippedRange: function (origLineMin, origLineMax) {
      var x = this.x;
      var y = this.y;
      var rx = this.rx;
      var ry = this.ry;
      
      var lineMin = this.toCircleLine(origLineMin, x, y, rx, ry);
      var lineMax = this.toCircleLine(origLineMax, x, y, rx, ry);
      var r = rx;
      
      var angleMin = this.angleMin;
      var angleMax = this.angleMax;
      var d = -(lineMin[0] * x + lineMin[1] * y + lineMin[2]);
      
      var sign = xypic.Util.sign2;
      var angles = [];
      var det = r * r - d * d;
      if (det >= 0) {
        var xp = lineMin[0] * d - lineMin[1] * Math.sqrt(r * r - d * d);
        var yp = lineMin[1] * d + lineMin[0] * Math.sqrt(r * r - d * d);
        var xm = lineMin[0] * d + lineMin[1] * Math.sqrt(r * r - d * d);
        var ym = lineMin[1] * d - lineMin[0] * Math.sqrt(r * r - d * d);
        var anglep = Math.atan2(yp, xp);
        var anglem = Math.atan2(ym, xm);
        if (this.containsParam(anglep)) {
          angles.push(anglep);
        }
        if (this.containsParam(anglem)) {
          angles.push(anglem);
        }
      }
      
      var d0 = -(lineMin[0] * (x + r * Math.cos(angleMin)) + lineMin[1] * (y + r * Math.sin(angleMin)) + lineMin[2]);
      var d1 = -(lineMin[0] * (x + r * Math.cos(angleMax)) + lineMin[1] * (y + r * Math.sin(angleMax)) + lineMin[2]);
      var angleMinAgainstLineMin, angleMaxAgainstLineMin;
      if (d0 < 0) {
        if (angles.length == 0) {
          // no intersection
          return undefined;
        }
        angleMinAgainstLineMin = Math.min.apply(Math, angles);
      } else {
        angleMinAgainstLineMin = this.angleMin;
      }
      if (d1 < 0) {
        if (angles.length == 0) {
          // no intersection
          return undefined;
        }
        angleMaxAgainstLineMin = Math.max.apply(Math, angles);
      } else {
        angleMaxAgainstLineMin = this.angleMax;
      }
      
      var d = lineMax[0] * x + lineMax[1] * y + lineMax[2];
      var angles = [];
      var det = r * r - d * d;
      if (det >= 0) {
        var xp = -lineMin[0] * d + lineMin[1] * Math.sqrt(r * r - d * d);
        var yp = -lineMin[1] * d - lineMin[0] * Math.sqrt(r * r - d * d);
        var xm = -lineMin[0] * d - lineMin[1] * Math.sqrt(r * r - d * d);
        var ym = -lineMin[1] * d + lineMin[0] * Math.sqrt(r * r - d * d);
        var anglep = Math.atan2(yp, xp);
        var anglem = Math.atan2(ym, xm);
        if (this.containsParam(anglep)) {
          angles.push(anglep);
        }
        if (this.containsParam(anglem)) {
          angles.push(anglem);
        }
      }
      
      var d0 = lineMax[0] * (x + r * Math.cos(angleMin)) + lineMax[1] * (y + r * Math.sin(angleMin)) + lineMax[2];
      var d1 = lineMax[0] * (x + r * Math.cos(angleMax)) + lineMax[1] * (y + r * Math.sin(angleMax)) + lineMax[2];
      var angleMinAgainstLineMax, angleMaxAgainstLineMax;
      if (d0 < 0) {
        if (angles.length == 0) {
          // no intersection
          return undefined;
        }
        angleMinAgainstLineMax = Math.min.apply(Math, angles);
      } else {
        angleMinAgainstLineMax = this.angleMin;
      }
      if (d1 < 0) {
        if (angles.length == 0) {
          // no intersection
          return undefined;
        }
        angleMaxAgainstLineMax = Math.max.apply(Math, angles);
      } else {
        angleMaxAgainstLineMax = this.angleMax;
      }
      
      return {
        min:Math.max(angleMinAgainstLineMin, angleMinAgainstLineMax), 
        max:Math.min(angleMaxAgainstLineMin, angleMaxAgainstLineMax)
      };
    },
    drawFatLine: function () {
      var fatLine = this.fatLine();
      var lmin = fatLine.min;
      var lmax = fatLine.max;
      var y = function (x, l) {
        return -(x * l[0] + l[2]) / l[1];
      }
      var x0 = this.x + this.r * Math.cos(this.angleMin);
      var x1 = this.x + this.r * Math.cos(this.angleMax);
      var xmin = x0;
      var xmax = x1;
      xypic.svgForDebug.createSVGElement("line", {
        x1:xypic.em2px(xmin), y1:-xypic.em2px(y(xmin, lmin)),
        x2:xypic.em2px(xmax), y2:-xypic.em2px(y(xmax, lmin)),
        "stroke-width":xypic.em2px(0.02 * xypic.oneem), stroke:"blue"
      });
      xypic.svgForDebug.createSVGElement("line", {
        x1:xypic.em2px(xmin), y1:-xypic.em2px(y(xmin, lmax)),
        x2:xypic.em2px(xmax), y2:-xypic.em2px(y(xmax, lmax)),
        "stroke-width":xypic.em2px(0.02 * xypic.oneem), stroke:"red"
      });
    }
  });
  
  
  xypic.LastCurve = MathJax.Object.Subclass({});
  
  xypic.LastCurve.None = xypic.LastCurve.Subclass({
    Init: function () {}, 
    isDefined: false,
    segments: function () { return []; },
    angle: function () { return 0; }
  });
  
  xypic.LastCurve.Augment({}, {
    none: xypic.LastCurve.None()
  });
  
  xypic.LastCurve.Line = xypic.LastCurve.Subclass({
    Init: function (start, end, p, c, lineShape) {
      this.start = start;
      this.end = end;
      this.p = p;
      this.c = c;
      this.lineShape = lineShape; // line from start to end.
    },
    isDefined: true,
    position: function (t) {
      return xypic.Frame.Point(
        this.p.x + t*(this.c.x - this.p.x),
        this.p.y + t*(this.c.y - this.p.y)
      );
    },
    derivative: function (t) {
      return xypic.Frame.Point(
        this.c.x - this.p.x,
        this.c.y - this.p.y
      );
    },
    angle: function (t) {
      var dx = this.c.x - this.p.x;
      var dy = this.c.y - this.p.y;
      if (dx === 0 && dy === 0) {
        return 0;
      }
      return Math.atan2(dy, dx);
    },
    tOfPlace: function (shaveP, shaveC, factor, slideEm) {
      var start = (shaveP? this.start : this.p);
      var end = (shaveC? this.end : this.c);
      if (start.x === end.x && start.y === end.y) {
        return 0;
      } else {
        var dx = end.x - start.x;
        var dy = end.y - start.y;
        var l = Math.sqrt(dx * dx + dy * dy);
        var x, y;
        if (factor > 0.5) {
          x = end.x - (1 - factor) * dx + slideEm * dx / l;
          y = end.y - (1 - factor) * dy + slideEm * dy / l;
        } else {
          x = start.x + factor * dx + slideEm * dx / l;
          y = start.y + factor * dy + slideEm * dy / l;
        }
        var tx = this.c.x - this.p.x;
        var ty = this.c.y - this.p.y;
        if (tx === 0 && ty === 0) {
          return 0;
        }
        if (Math.abs(tx) > Math.abs(ty)) {
          return (x - this.p.x) / tx;
        } else {
          return (y - this.p.y) / ty;
        }
      }
    },
    sliceHole: function (holeFrame, t) {
      if (this.lineShape === undefined || holeFrame.isPoint()) {
        return;
      }
      var shape = this.lineShape;
      var line = shape.line;
      var intersections = line.tOfIntersections(holeFrame); // ts of the line from start to end.
      intersections.push(0);
      intersections.push(1);
      intersections.sort();
      
      var t0 = intersections[0], t1;
      for (var i = 1; i < intersections.length; i++) {
        var t1 = intersections[i];
        var p = line.position((t1 + t0) / 2);
        if (holeFrame.contains(p)) {
          var range = xypic.Range(t0, t1);
          shape.sliceHole(range);
        }
        t0 = t1;
      }
    },
    segments: function () {
      return [xypic.CurveSegment.Line(this.p, this.c, 0, 1)];
    }
  });
  
  xypic.LastCurve.QuadBezier = xypic.LastCurve.Subclass({
    Init: function (origBezier, tOfShavedStart, tOfShavedEnd, curveShape) {
      this.origBezier = origBezier; // unshaved
      this.tOfShavedStart = tOfShavedStart;
      this.tOfShavedEnd = tOfShavedEnd;
      if (!curveShape.isNone) {
        this.curveShape = curveShape;
        if (tOfShavedStart > 0) { curveShape.sliceHole(xypic.Range(0, tOfShavedStart)); }
        if (tOfShavedEnd < 1) { curveShape.sliceHole(xypic.Range(tOfShavedEnd, 1)); }
      }
    },
    isDefined: true,
    position: function (t) {
      return this.origBezier.position(t);
    },
    derivative: function (t) {
      return this.origBezier.derivative(t);
    },
    angle: function (t) {
      return this.origBezier.angle(t);
    },
    tOfPlace: function (shaveP, shaveC, factor, slide) {
      var offset;
      var normalizer;
      if (shaveP) {
        offset = this.tOfShavedStart;
        if (shaveC) {
          normalizer = this.tOfShavedEnd - this.tOfShavedStart;
        } else {
          normalizer = 1  - this.tOfShavedStart;
        }
      } else {
        offset = 0;
        if (shaveC) {
          normalizer = this.tOfShavedEnd;
        } else {
          normalizer = 1;
        }
      }
      var bezier = this.origBezier;
      var pos, angle;
      var normalizedFactor = offset + normalizer * factor;
      if (slide !== 0) {
        var fd = bezier.length(normalizedFactor);
        normalizedFactor = bezier.tOfLength(fd + slide);
      }
      return normalizedFactor;
    },
    sliceHole: function (holeFrame, t) {
      var shape = this.curveShape;
      if (shape === undefined || holeFrame.isPoint()) {
        return;
      }
      var curve = shape.curve;
      var intersections = curve.tOfIntersections(holeFrame); // ts of the curve from p to c.
      intersections.push(0);
      intersections.push(1);
      intersections.sort();
      
      var t0 = intersections[0], t1;
      for (var i = 1; i < intersections.length; i++) {
        var t1 = intersections[i];
        if (t0 <= t && t <= t1) {
          var p = curve.position((t1 + t0) / 2);
          if (holeFrame.contains(p)) {
            var range = xypic.Range(t0, t1);
            shape.sliceHole(range);
          }
        }
        t0 = t1;
      }
    },
    segments: function () {
      return [xypic.CurveSegment.QuadBezier(this.origBezier, 0, 1)];
    }
  });
  
  xypic.LastCurve.CubicBezier = xypic.LastCurve.Subclass({
    Init: function (origBezier, tOfShavedStart, tOfShavedEnd, curveShape) {
      this.origBezier = origBezier; // unshaved
      this.tOfShavedStart = tOfShavedStart;
      this.tOfShavedEnd = tOfShavedEnd;
      if (!curveShape.isNone) {
        this.curveShape = curveShape;
        if (tOfShavedStart > 0) { curveShape.sliceHole(xypic.Range(0, tOfShavedStart)); }
        if (tOfShavedEnd < 1) { curveShape.sliceHole(xypic.Range(tOfShavedEnd, 1)); }
      }
    },
    originalLine: function () {
      return this.originalLine;
    },
    isDefined: true,
    position: function (t) {
      return this.origBezier.position(t);
    },
    derivative: function (t) {
      return this.origBezier.derivative(t);
    },
    angle: function (t) {
      return this.origBezier.angle(t);
    },
    tOfPlace: function (shaveP, shaveC, factor, slide) {
      var offset;
      var normalizer;
      if (shaveP) {
        offset = this.tOfShavedStart;
        if (shaveC) {
          normalizer = this.tOfShavedEnd - this.tOfShavedStart;
        } else {
          normalizer = 1  - this.tOfShavedStart;
        }
      } else {
        offset = 0;
        if (shaveC) {
          normalizer = this.tOfShavedEnd;
        } else {
          normalizer = 1;
        }
      }
      var bezier = this.origBezier;
      var pos, angle;
      var normalizedFactor = offset + normalizer * factor;
      if (slide !== 0) {
        var fd = bezier.length(normalizedFactor);
        normalizedFactor = bezier.tOfLength(fd + slide);
      }
      return normalizedFactor;
    },
    sliceHole: function (holeFrame, t) {
      var shape = this.curveShape;
      if (shape === undefined || holeFrame.isPoint()) {
        return;
      }
      var curve = shape.curve;
      var intersections = curve.tOfIntersections(holeFrame); // ts of the curve from p to c.
      intersections.push(0);
      intersections.push(1);
      intersections.sort();
      
      var t0 = intersections[0], t1;
      for (var i = 1; i < intersections.length; i++) {
        var t1 = intersections[i];
        if (t0 <= t && t <= t1) {
          var p = curve.position((t1 + t0) / 2);
          if (holeFrame.contains(p)) {
            var range = xypic.Range(t0, t1);
            shape.sliceHole(range);
          }
        }
        t0 = t1;
      }
    },
    segments: function () {
      return [xypic.CurveSegment.CubicBezier(this.origBezier, 0, 1)];
    }
  });
  
  xypic.LastCurve.CubicBSpline = xypic.LastCurve.Subclass({
    Init: function (s, e, origBeziers, tOfShavedStart, tOfShavedEnd, curveShape) {
      this.s = s;
      this.e = e;
      this.origBeziers = origBeziers; // unshaved
      this.tOfShavedStart = tOfShavedStart;
      this.tOfShavedEnd = tOfShavedEnd;
      if (!curveShape.isNone) {
        this.curveShape = curveShape;
        if (tOfShavedStart > 0) { curveShape.sliceHole(xypic.Range(0, tOfShavedStart)); }
        if (tOfShavedEnd < 1) { curveShape.sliceHole(xypic.Range(tOfShavedEnd, 1)); }
      }
    },
    isDefined: true,
    position: function (t) {
      return this.origBeziers.position(t);
    },
    derivative: function (t) {
      return this.origBeziers.derivative(t);
    },
    angle: function (t) {
      return this.origBeziers.angle(t);
    },
    tOfPlace: function (shaveP, shaveC, factor, slide) {
      var offset;
      var normalizer;
      if (shaveP) {
        offset = this.tOfShavedStart;
        if (shaveC) {
          normalizer = this.tOfShavedEnd - this.tOfShavedStart;
        } else {
          normalizer = 1  - this.tOfShavedStart;
        }
      } else {
        offset = 0;
        if (shaveC) {
          normalizer = this.tOfShavedEnd;
        } else {
          normalizer = 1;
        }
      }
      var beziers = this.origBeziers;
      var pos, angle;
      var normalizedFactor = offset + normalizer * factor;
      if (slide !== 0) {
        var fd = beziers.length(normalizedFactor);
        normalizedFactor = beziers.tOfLength(fd + slide);
      }
      return normalizedFactor;
    },
    sliceHole: function (holeFrame, t) {
      var shape = this.curveShape;
      if (shape === undefined || holeFrame.isPoint()) {
        return;
      }
      var curve = shape.curve;
      var intersections = curve.tOfIntersections(holeFrame); // ts of the curve from p to c.
      intersections.push(0);
      intersections.push(1);
      intersections.sort();
      
      var t0 = intersections[0], t1;
      for (var i = 1; i < intersections.length; i++) {
        var t1 = intersections[i];
        if (t0 <= t && t <= t1) {
          var p = curve.position((t1 + t0) / 2);
          if (holeFrame.contains(p)) {
            var range = xypic.Range(t0, t1);
            shape.sliceHole(range);
          }
        }
        t0 = t1;
      }
    },
    segments: function () {
      var segments = new Array(this.origBeziers.length);
      var n = segments.length;
      for (var i = 0; i < n; i++) {
        segments[i] = xypic.CurveSegment.CubicBezier(this.origBezier, i/n, (i+1)/n);
      }
      return segments;
    }
  });
  
  
  xypic.Saving = MathJax.Object.Subclass({});
  xypic.Saving.Position = MathJax.Object.Subclass({
    Init: function (pos) {
      this.pos = pos;
    },
    position: function (context) {
      return this.pos;
    },
    toString: function () {
      return this.pos.toString();
    }
  });
  
  xypic.Saving.Macro = MathJax.Object.Subclass({
    Init: function (macro) {
      this.macro = macro;
    },
    position: function (context) {
      env.c = this.macro.position(context);
      return env.c;
    },
    toString: function () {
      return this.macro.toString();
    }
  });
  
  xypic.Saving.Base = MathJax.Object.Subclass({
    Init: function (origin, xBase, yBase) {
      this.origin = origin;
      this.xBase = xBase;
      this.yBase = yBase;
    },
    position: function (context) {
      var env = context.env;
      env.origin = this.origin;
      env.xBase = this.xBase;
      env.yBase = this.yBase;
      return env.c;
    },
    toString: function () {
      return "origin:" + this.origin + ", xBase:" + this.xBase + ", yBase:" + this.yBase;
    }
  });
  
  xypic.Saving.Stack = MathJax.Object.Subclass({
    Init: function (stack) {
      this.stack = stack;
    },
    position: function (context) {
      var env = context.env;
      if (!this.stack.isEmpty) {
        this.stack.tail.reverse().foreach(function (p) {
          env.capturePosition(p);
        });
        env.c = this.stack.head;
      }
      return env.c;
    },
    toString: function () {
      return this.stack.toString();
    }
  });
  
  
  xypic.Env = MathJax.Object.Subclass({
    Init: function () {
      var onemm = xypic.length2em("1mm");
      this.origin = {x:0, y:0};
      this.xBase = {x:onemm, y:0};
      this.yBase = {x:0, y:onemm};
      this.savedPosition = {};
      this.stateStack = FP.List.empty;
      this.stackFrames = FP.List.empty;
      this.stack = FP.List.empty;
      this.angle = 0; // radian
      this.lastCurve = xypic.LastCurve.none;
      this.p = this.c = xypic.Env.originPosition;
      this.shouldCapturePos = false;
      this.capturedPositions = FP.List.empty;
      this.objectmargin = AST.xypic.objectmargin;
      this.objectheight = AST.xypic.objectheight;
      this.objectwidth = AST.xypic.objectwidth;
      this.labelmargin = AST.xypic.labelmargin;
    },
    duplicate: function () {
      var newEnv = xypic.Env();
      xypic.Env.copyFields(this, newEnv);
      return newEnv;
    },
    saveState: function () {
      var currentState = this.duplicate();
      this.stateStack = this.stateStack.prepend(currentState);
    },
    restoreState: function () {
      if (!this.stateStack.isEmpty) {
        var savedState = this.stateStack.head;
        this.stateStack = this.stateStack.tail;
        xypic.Env.copyFields(savedState, this);
      }
    },
    absVector: function (x, y) {
      var ax = this.origin.x + x * this.xBase.x + y * this.yBase.x;
      var ay = this.origin.y + x * this.xBase.y + y * this.yBase.y;
      return {x:ax, y:ay};
    },
    inverseAbsVector: function (ax, ay) {
      var bxx = this.xBase.x;
      var bxy = this.xBase.y;
      var byx = this.yBase.x;
      var byy = this.yBase.y;
      var det = bxx * byy - bxy * byx;
      var dx = ax - this.origin.x;
      var dy = ay - this.origin.y
      var x = (byy * dx - byx * dy) / det;
      var y = (-bxy * dx + bxx * dy) / det;
      return {x:x, y:y};
    },
    setOrigin: function (x, y) {
      this.origin = {x:x, y:y};
    },
    setXBase: function (x, y) {
      this.xBase = {x:x, y:y};
    },
    setYBase: function (x, y) {
      this.yBase = {x:x, y:y};
    },
    swapPAndC: function () {
      var t = this.p;
      this.p = this.c;
      this.c = t;
    },
    enterStackFrame: function () {
      this.stackFrames = this.stackFrames.prepend(this.stack);
      this.initStack();
    },
    leaveStackFrame: function () {
      if (!this.stackFrames.isEmpty) {
        this.stack = this.stackFrames.head;
        this.stackFrames = this.stackFrames.tail;
      } else {
        this.initStack();
      } 
    },
    savePos: function (id, pos) {
      this.savedPosition[id] = pos;
    },
    startCapturePositions: function () {
      this.shouldCapturePos = true;
      this.capturedPositions = FP.List.empty;
    },
    endCapturePositions: function () {
      this.shouldCapturePos = false;
      var positions = this.capturedPositions;
      this.capturedPositions = FP.List.empty;
      return positions;
    },
    capturePosition: function (pos) {
      if (this.shouldCapturePos && pos !== undefined) {
        this.capturedPositions = this.capturedPositions.prepend(pos);
      }
    },
    pushPos: function (pos) {
      if (pos !== undefined) {
        this.stack = this.stack.prepend(pos);
      }
    },
    popPos: function () {
      if (this.stack.isEmpty) {
        throw xypic.ExecutionError("cannot pop from the empty stack");
      } else {
        var pos = this.stack.head;
        this.stack = this.stack.tail;
        return pos;
      }
    },
    initStack: function () {
      this.stack = FP.List.empty;
    },
    setStack: function (positions) {
      this.stack = positions;
    },
    stackAt: function (number) {
      return this.stack.at(number);
    },
    lookupPos: function (id, errorMessage) {
      var pos = this.savedPosition[id];
      if (pos === undefined) {
        if (errorMessage !== undefined) {
          throw xypic.ExecutionError(errorMessage);
        } else {
          throw xypic.ExecutionError('<pos> "' + id + '" not defined.');
        }
      } else {
        return pos;
      }
    },
    toString: function () {
      var savedPositionDesc = "";
      for (var id in this.savedPosition) {
        if (this.savedPosition.hasOwnProperty(id)) {
          if (savedPositionDesc.length > 0) {
            savedPositionDesc += ", "
          }
          savedPositionDesc += id.toString()+":"+this.savedPosition[id];
        }
      }
      return "Env\n  p:"+this.p+"\n  c:"+this.c+"\n  angle:"+this.angle+"\n  lastCurve:"+this.lastCurve+"\n  savedPosition:{"+savedPositionDesc+"}\n  origin:{x:"+this.origin.x+", y:"+this.origin.y+"}\n  xBase:{x:"+this.xBase.x+", y:"+this.xBase.y+"}\n  yBase:{x:"+this.yBase.x+", y:"+this.yBase.y+"}\n  stackFrames:"+this.stackFrames+"\n  stack:"+this.stack+"\n  shouldCapturePos:"+this.shouldCapturePos+"\n  capturedPositions:"+this.capturedPositions;
    }
  }, {
    originPosition: xypic.Frame.Point(0, 0),
    copyFields: function (from, to) {
      for (var attr in from) {
        if (from.hasOwnProperty(attr)) {
          to[attr] = from[attr];
        }
      }
      to.savedPosition = {};
      for (var id in from.savedPosition) {
        if (from.savedPosition.hasOwnProperty(id)) {
          to.savedPosition[id] = from.savedPosition[id];
        }
      }
    }
  });
  
  AST.PosDecor.Augment({
    toShape: function (context) {
      this.pos.toShape(context);
      this.decor.toShape(context);
    }
  });
  
  AST.Pos.Coord.Augment({
    toShape: function (context) {
      context.env.c = this.coord.position(context);
      this.pos2s.foreach(function (p) { p.toShape(context); });
    }
  });
  
  AST.Pos.Plus.Augment({
    toShape: function (context) {
      var env = context.env;
      var pos = this.coord.position(context);
      env.c = pos.move(env.c.x + pos.x, env.c.y + pos.y);
    }
  });
  
  AST.Pos.Minus.Augment({
    toShape: function (context) {
      var env = context.env;
      var pos = this.coord.position(context);
      env.c = pos.move(env.c.x - pos.x, env.c.y - pos.y);
    }
  });
  
  AST.Pos.Skew.Augment({
    toShape: function (context) {
      var env = context.env;
      var pos = this.coord.position(context);
      var rp = xypic.Frame.Point(pos.x + env.c.x, pos.y + env.c.y);
      env.c = rp.combineRect(env.c);
    }
  });
  
  AST.Pos.Cover.Augment({
    toShape: function (context) {
      var env = context.env;
      var pos = this.coord.position(context);
      env.c = env.c.combineRect(pos);
    }
  });
  
  AST.Pos.Then.Augment({
    toShape: function (context) {
      var env = context.env;
      env.capturePosition(env.c);
      env.c = this.coord.position(context);
    }
  });
  
  AST.Pos.SwapPAndC.Augment({
    toShape: function (context) {
      var env = context.env;
      env.swapPAndC();
      env.c = this.coord.position(context);
    }
  });
  
  AST.Pos.SetBase.Augment({
    toShape: function (context) {
      var env = context.env;
      var p = env.p;
      var x = env.c.x - p.x;
      var y = env.c.y - p.y;
      env.setOrigin(p.x, p.y);
      env.setXBase(x, y);
      env.setYBase(-y, x);
      env.c = this.coord.position(context);
    }
  });
  
  AST.Pos.SetYBase.Augment({
    toShape: function (context) {
      var env = context.env;
      env.setYBase(env.c.x - env.origin.x, env.c.y - env.origin.y);
      env.c = this.coord.position(context);
    }
  });
  
  AST.Pos.ConnectObject.Augment({
    toShape: function (context) {
      this.object.toConnectShape(context);
    }
  });
  
  AST.Pos.DropObject.Augment({
    toShape: function (context) {
      this.object.toDropShape(context);
    }
  });
  
  AST.Pos.Place.Augment({
    toShape: function (context) {
      var env = context.env;
      if (env.lastCurve.isDefined) {
        var place = this.place;
        var start, end, f, dimen;
        var shouldShaveP = (place.shaveP > 0);
        var shouldShaveC = (place.shaveC > 0);
        var jotP = (shouldShaveP? place.shaveP - 1 : 0);
        var jotC = (shouldShaveC? place.shaveC - 1 : 0);
        
        if (shouldShaveP) { f = 0; }
        if (shouldShaveC) { f = 1; }
        if (shouldShaveP == shouldShaveC) {
          f = 0.5;
        }
        if (place.factor !== undefined) {
          if (place.factor.isIntercept) {
            shouldShaveC = shouldShaveP = false;
            f = place.factor.value(context);
            if (f === undefined) {
              return;
            }
          } else {
            f = place.factor.value(context);
          }
        }
        
        dimen = xypic.length2em(place.slide.dimen.getOrElse("0"));
        var jot = AST.xypic.jot;
        var slideEm = dimen + (jotP - jotC) * jot;
        var t = env.lastCurve.tOfPlace(shouldShaveP, shouldShaveC, f, slideEm);
        var pos = env.lastCurve.position(t);
        var angle = env.lastCurve.angle(t);
        env.c = pos;
        env.angle = angle;
        return t;
      }
      return undefined;
    }
  });
  
  AST.Pos.PushCoord.Augment({
    toShape: function (context) {
      var env = context.env;
      var pos = this.coord.position(context);
      env.pushPos(pos);
    }
  });
  
  AST.Pos.EvalCoordThenPop.Augment({
    toShape: function (context) {
      var env = context.env;
      env.c = this.coord.position(context);
      env.popPos();
    }
  });
  
  AST.Pos.LoadStack.Augment({
    toShape: function (context) {
      var env = context.env;
      env.startCapturePositions();
      this.coord.position(context);
      var positions = env.endCapturePositions();
      env.setStack(positions);
      env.pushPos(env.c);
    }
  });
  
  AST.Pos.DoCoord.Augment({
    toShape: function (context) {
      var env = context.env;
      var coord = this.coord;
      var pos = env.stack.reverse();
      pos.foreach(function (c) {
        env.c = c;
        coord.position(context);
      });
    }
  });
  
  AST.Pos.InitStack.Augment({
    toShape: function (context) {
      context.env.initStack();
    }
  });
  
  AST.Pos.EnterFrame.Augment({
    toShape: function (context) {
      context.env.enterStackFrame();
    }
  });
  
  AST.Pos.LeaveFrame.Augment({
    toShape: function (context) {
      context.env.leaveStackFrame();
    }
  });
  
  AST.Place.Factor.Augment({
    value: function (context) {
      return this.factor;
    }
  });
  
  AST.Place.Intercept.Augment({
    value: function (context) {
      var env = context.env;
      if (!env.lastCurve.isDefined) {
        return undefined;
      }
      
      var tmpEnv = env.duplicate();
      tmpEnv.angle = 0;
      tmpEnv.lastCurve = xypic.LastCurve.none;
      tmpEnv.p = tmpEnv.c = xypic.Env.originPosition;
      var tmpContext = xypic.DrawingContext(xypic.Shape.none, tmpEnv);
      
      var box = this.pos.toShape(tmpContext);
      context.appendShapeToFront(tmpContext.shape);
      
      if (!tmpEnv.lastCurve.isDefined) {
        tmpEnv.lastCurve = xypic.LastCurve.Line(tmpEnv.p, tmpEnv.c, tmpEnv.p, tmpEnv.c, undefined);
      }
      
      var intersec = [];
      var thisSegs = env.lastCurve.segments();
      var thatSegs = tmpEnv.lastCurve.segments();
      
      for (var i = 0; i < thisSegs.length; i++) {
        for (var j = 0; j < thatSegs.length; j++) {
          intersec = intersec.concat(xypic.CurveSegment.findIntersections(thisSegs[i], thatSegs[j]));
        }
      }
      
      if (intersec.length === 0) {
        // find the nearest point, if no intersection was found.
        console.log("perhaps no curve intersection.");
        
        // Levenberg-Marqardt Method
        var line0 = env.lastCurve;
        var line1 = tmpEnv.lastCurve;
        
        var n = 100; // maxIterations
        var goalAccuracy = 1e-5;
        var tau = 1e-3;
        
        var k = 0;
        var nu = 2;
        
        // TODO: 複数個の開始地点から探索し、尤もらしい解を選択する。
        var x0 = 0;
        var x1 = 0;
        
        var tx = function (x) {
          return 1 / (1 + Math.exp(-x));
        }
        var dtx = function (x) {
          var ex = Math.exp(-x);
          return ex / (1 + ex) / (1 + ex);
        }
        
        var t0 = tx(x0);
        var t1 = tx(x1);
        var dt0 = dtx(x0);
        var dt1 = dtx(x1);
        
        var dp0 = line0.derivative(t0);
        var dp1 = line1.derivative(t1);
        
        var j00 = dp0.x * dt0, j01 = -dp1.x * dt1;
        var j10 = dp0.y * dt0, j11 = -dp1.y * dt1;
        
        var a00 = j00 * j00 + j10 * j10, a01 = j00 * j01 + j10 * j11;
        var a10 = j01 * j00 + j11 * j10, a11 = j01 * j01 + j11 * j11;
        
        var p0 = line0.position(t0);
        var p1 = line1.position(t1);
        
        var f0 = p0.x - p1.x;
        var f1 = p0.y - p1.y;
        
        var g0 = j00 * f0 + j10 * f1;
        var g1 = j01 * f0 + j11 * f1;
        
        var stop = Math.sqrt(g0 * g0 + g1 * g1) < goalAccuracy;
        var mu = tau * Math.max(a00, a11);
        
        while (!stop && k < n) {
          k++;
          do {
            var am00 = a00 + mu, am01 = a01;
            var am10 = a10, am11 = a11 + mu;
            
            var det = am00 * am11 - am01 * am10;
            var d0 = (am11 * g0 - a01 * g1) / det;
            var d1 = (-am10 * g0 + a00 * g1) / det;
            
            if ((d0 * d0 + d1 * d1) < goalAccuracy * goalAccuracy * (x0 * x0 + x1 * x1)) {
              stop = true;
            } else {
              var newX0 = x0 - d0;
              var newX1 = x1 - d1;
              
              var newT0 = tx(newX0);
              var newT1 = tx(newX1);
              
              var newP0 = line0.position(newT0);
              var newP1 = line1.position(newT1);
              
              var newF0 = newP0.x - newP1.x;
              var newF1 = newP0.y - newP1.y;
              
              var rho = ((f0 * f0 + f1 * f1) - (newF0 * newF0 + newF1 * newF1)) / (d0 * (mu * d0 + g0) + d1 * (mu * d1 + g1));
              
              if (rho > 0) {
                x0 = newX0;
                x1 = newX1;
                t0 = newT0;
                t1 = newT1;
                dt0 = dtx(x0);
                dt1 = dtx(x1);
                dp0 = line0.derivative(t0);
                dp1 = line1.derivative(t1);
                j00 = dp0.x * dt0;  j01 = -dp1.x * dt1;
                j10 = dp0.y * dt0;  j11 = -dp1.y * dt1;
                a00 = j00 * j00 + j10 * j10;  a01 = j00 * j01 + j10 * j11;
                a10 = j01 * j00 + j11 * j10;  a11 = j01 * j01 + j11 * j11;
                f0 = newF0;
                f1 = newF1;
                g0 = j00 * f0 + j10 * f1;
                g1 = j01 * f0 + j11 * f1;
                stop = Math.sqrt(g0 * g0 + g1 * g1) < goalAccuracy;
                var sigma = 2 * rho - 1;
                mu = mu + Math.max(1 / 3, 1 - sigma * sigma * sigma);
                nu = 2;
              } else {
                mu = mu * nu;
                nu = 2 * nu;
              }
            }
          } while (!stop && !(rho !== undefined && rho > 0))
        }
        
        return tx(x0);
      } else {
        var t = (intersec[0][0].min + intersec[0][0].max)/2;
        for (var i = 1; i < intersec.length; i++) { 
          var ttmp = (intersec[i][0].min + intersec[i][0].max)/2;
          if (t > ttmp) { t = ttmp; }
        }
        return t;
      }
    }
  });
  
  AST.Pos.SavePos.Augment({
    toShape: function (context) {
      var env = context.env;
      env.savePos(this.id, xypic.Saving.Position(env.c));
    }
  });
  
  AST.Pos.SaveMacro.Augment({
    toShape: function (context) {
      var env = context.env;
      env.savePos(this.id, xypic.Saving.Macro(this.macro));
    }
  });
  
  AST.Pos.SaveBase.Augment({
    toShape: function (context) {
      var env = context.env;
      env.savePos(this.id, xypic.Saving.Base(env.origin, env.xBase, env.yBase));
    }
  });
  
  AST.Pos.SaveStack.Augment({
    toShape: function (context) {
      var env = context.env;
      env.savePos(this.id, xypic.Saving.Stack(env.stack));
    }
  });
  
  AST.Object.Augment({
    toDropShape: function (context) {
      var env = context.env;
      if (env.c === undefined) {
        return xypic.Shape.none;
      }
      
      var modifiers = this.modifiers;
      if (modifiers.isEmpty) {
        return this.object.toDropShape(context);
      } else {
        var tmpEnv = env.duplicate();
        var subcontext = xypic.DrawingContext(xypic.Shape.none, tmpEnv);
        var reversedProcessedModifiers = FP.List.empty;
        modifiers.foreach(function (m) {
          m.preprocess(subcontext, reversedProcessedModifiers);
          reversedProcessedModifiers = reversedProcessedModifiers.prepend(m);
        });
        var objectShape = this.object.toDropShape(subcontext);
        var objectBoundingBox = tmpEnv.c;
        if (objectBoundingBox === undefined) {
          return xypic.Shape.none;
        }
        var originalReferencePoint = tmpEnv.originalReferencePoint;
        tmpEnv = env.duplicate(); // restore angle
        tmpEnv.c = objectBoundingBox;
        tmpEnv.originalReferencePoint = originalReferencePoint;
        subcontext = xypic.DrawingContext(xypic.Shape.none, tmpEnv);
        objectShape = modifiers.head.modifyShape(subcontext, objectShape, modifiers.tail);
        context.appendShapeToFront(objectShape);
        env.c = tmpEnv.c.move(env.c.x, env.c.y);
        return objectShape;
      }
    },
    toConnectShape: function (context) {
      var env = context.env;
      if (env.c === undefined) {
        return xypic.Shape.none;
      }
      
      var modifiers = this.modifiers;
      if (modifiers.isEmpty) {
        return this.object.toConnectShape(context);
      } else {
        var tmpEnv = env.duplicate();
        var subcontext = xypic.DrawingContext(xypic.Shape.none, tmpEnv);
        var reversedProcessedModifiers = FP.List.empty;
        modifiers.foreach(function (m) {
          m.preprocess(subcontext, reversedProcessedModifiers);
          reversedProcessedModifiers = reversedProcessedModifiers.prepend(m);
        });
        var objectShape = this.object.toConnectShape(subcontext);
        env.angle = tmpEnv.angle;
        env.lastCurve = tmpEnv.lastCurve;
        var objectBoundingBox = tmpEnv.c;
        if (objectBoundingBox === undefined) {
          return xypic.Shape.none;
        }
        var originalReferencePoint = tmpEnv.originalReferencePoint;
        tmpEnv = env.duplicate(); // restore angle
        tmpEnv.c = objectBoundingBox;
        tmpEnv.originalReferencePoint = originalReferencePoint;
        subcontext = xypic.DrawingContext(xypic.Shape.none, tmpEnv);
        objectShape = modifiers.head.modifyShape(subcontext, objectShape, modifiers.tail);
        context.appendShapeToFront(objectShape);
        env.c = tmpEnv.c.move(env.c.x, env.c.y);
        return objectShape;
      }
    },
    boundingBox: function (context) {
      var tmpEnvContext = context.duplicateEnv();
      var tmpEnv = tmpEnvContext.env;
      tmpEnv.angle = 0;
      tmpEnv.p = tmpEnv.c = xypic.Env.originPosition;
      tmpEnvContext.shape = xypic.Shape.none;
      var dropShape = this.toDropShape(tmpEnvContext);
      return dropShape.getBoundingBox();
    }
  });
  
  AST.ObjectBox.Augment({
    toConnectShape: function (context) {
      // 多重線の幅、点線・破線の幅の基準
      var env = context.env;
      var origC = env.c;
      var env = context.env;
      var t = AST.xypic.thickness;
      var s = env.p.edgePoint(env.c.x, env.c.y);
      var e = env.c.edgePoint(env.p.x, env.p.y);
      if (s.x !== e.x || s.y !== e.y) {
        var shape = xypic.Curve.Line(s, e).toShape(context, this, "196883" /* dummy dir name */, "");
        env.originalReferencePoint = origC;
        return shape;
      } else {
        env.angle = 0;
        env.lastCurve = xypic.LastCurve.none;
        env.originalReferencePoint = origC;
        return xypic.Shape.none;
      }
    },
    boundingBox: function (context) {
      var tmpEnvContext = context.duplicateEnv();
      var tmpEnv = tmpEnvContext.env;
      tmpEnv.angle = 0;
      tmpEnv.p = tmpEnv.c = xypic.Env.originPosition;
      tmpEnvContext.shape = xypic.Shape.none;
      var dropShape = this.toDropShape(tmpEnvContext);
      return dropShape.getBoundingBox();
    }
  });
  
  AST.ObjectBox.WrapUpObject.Augment({
    toDropShape: function (context) {
      var env = context.env;
      var shape = this.object.toDropShape(context);
      env.originalReferencePoint = env.c;
      return shape;
    },
    toConnectShape: function (context) {
      var env = context.env;
      var shape = this.object.toConnectShape(context);
      env.originalReferencePoint = env.c;
      return shape;
    }
  });
  
  AST.ObjectBox.CompositeObject.Augment({
    toDropShape: function (context) {
      var env = context.env;
      var origC = env.c;
      if (origC === undefined) {
        return xypic.Shape.none;
      }
      var c = origC;
      var tmpEnv = env.duplicate();
      var subcontext = xypic.DrawingContext(xypic.Shape.none, tmpEnv);
      this.objects.foreach(function (obj) {
        tmpEnv.c = origC;
        var tmpShape = obj.toDropShape(subcontext);
        c = xypic.Frame.combineRect(c, tmpEnv.c);
        c = xypic.Frame.combineRect(c, tmpShape.getBoundingBox().toPoint());
      });
      env.c = c;
      var compositeShape = subcontext.shape;
      context.appendShapeToFront(compositeShape);
      env.originalReferencePoint = origC;
      return compositeShape;
    }
  });
  
  AST.ObjectBox.Xybox.Augment({
    toDropShape: function (context) {
      var env = context.env;
      var c = env.c;
      if (c === undefined) {
        return xypic.Shape.none;
      }
      var subenv = xypic.Env();
      var subcontext = xypic.DrawingContext(xypic.Shape.none, subenv);
      this.posDecor.toShape(subcontext);
      var subshape = subcontext.shape;
      var bbox = subshape.getBoundingBox();
      if (bbox === undefined) {
        return xypic.Shape.none;
      }
      var l = Math.max(0, bbox.l - bbox.x);
      var r = Math.max(0, bbox.r + bbox.x);
      var u = Math.max(0, bbox.u + bbox.y);
      var d = Math.max(0, bbox.d - bbox.y);
      env.c = xypic.Frame.Rect(c.x, c.y, { l:l, r:r, u:u, d:d });
      env.originalReferencePoint = c;
      var objectShape = xypic.Shape.TranslateShape(c.x, c.y, subshape);
      context.appendShapeToFront(objectShape);
      return objectShape;
    }
  });
  
  AST.ObjectBox.Xymatrix.Augment({
    toDropShape: function (context) {
      var env = context.env;
      var c = env.c;
      var shape = this.xymatrix.toShape(context);
      env.originalReferencePoint = c;
      return shape;
    }
  });
  
  AST.ObjectBox.Text.Augment({
    toDropShape: function (context) {
      var env = context.env;
      var textShape = xypic.Shape.TextShape(env.c, this.math, xypic.svgForTestLayout);
      context.appendShapeToFront(textShape);
      env.c = textShape.getBoundingBox();
      env.originalReferencePoint = textShape.getOriginalReferencePoint();
      return textShape;
    }
  });
  
  AST.ObjectBox.Empty.Augment({
    toDropShape: function (context) {
      var env = context.env;
      env.originalReferencePoint = env.c;
      env.c = xypic.Frame.Point(env.c.x, env.c.y);
      return xypic.Shape.none;
    }
  });

  
  AST.ObjectBox.Txt.Augment({
    toDropShape: function (context) {
      var env = context.env;
      if (env.c === undefined) {
        return xypic.Shape.none;
      }
      // TODO change width
      var textShape = this.textObject.toDropShape(context);
      env.originalReferencePoint = env.c;
      return textShape;
    }
  });
  AST.ObjectBox.Txt.Width.Vector.Augment({
    width: function (context) {
      return this.vector.xy().x;
    }
  });
  AST.ObjectBox.Txt.Width.Vector.Augment({
    width: function (context) {
      var c = context.env.c;
      return c.r + c.l;
    }
  });
  
  AST.ObjectBox.Cir.Augment({
    toDropShape: function (context) {
      var env = context.env;
      if (env.c === undefined) {
        return xypic.Shape.none;
      }
      env.originalReferencePoint = env.c;
      var r = this.radius.radius(context);
      var x = env.c.x;
      var y = env.c.y;
      var circleShape = this.cir.toDropShape(context, x, y, r);
      env.c = xypic.Frame.Ellipse(x, y, r, r, r, r);
      
      return circleShape;
    },
    toConnectShape: function (context) {
      // TODO: 何もしなくてよいかTeXの出力結果を確認する。
      var env = context.env;
      env.originalReferencePoint = env.c;
      return xypic.Shape.none;
    }
  });
  
  AST.ObjectBox.Cir.Radius.Vector.Augment({
    radius: function (context) {
      return this.vector.xy(context).x;
    }
  });
  AST.ObjectBox.Cir.Radius.Default.Augment({
    radius: function (context) {
      return context.env.c.r;
    }
  });
  AST.ObjectBox.Cir.Cir.Segment.Augment({
    toDropShape: function (context, x, y, r) {
      var env = context.env;
      var sa = this.startPointDegree(context);
      var ea = this.endPointDegree(context, sa);
      var da = ea - sa;
      da = (da < 0? da + 360 : da);
      if (da === 0) {
        return xypic.Shape.none;
      }
      
      var large, flip;
      if (this.orient === "^") {
        large = (da > 180? "1" : "0");
        flip = "0";
      } else {
        large = (da > 180? "0" : "1");
        flip = "1";
      }
      
      var degToRadCoef = Math.PI / 180;
      var sx = x + r * Math.cos(sa * degToRadCoef);
      var sy = y + r * Math.sin(sa * degToRadCoef);
      var ex = x + r * Math.cos(ea * degToRadCoef);
      var ey = y + r * Math.sin(ea * degToRadCoef);
      
      var circleSegmentShape = xypic.Shape.CircleSegmentShape(x, y, sx, sy, r, large, flip, ex, ey);
      context.appendShapeToFront(circleSegmentShape);
      return circleSegmentShape;
    },
    startPointDegree: function (contect) {
      var sd = this.startDiag.toString();
      var sa;
      if (this.orient === "^") {
        sa = this.diagToAngleACW(sd);
      } else {
        sa = this.diagToAngleCW(sd);
      }
      return sa;
    },
    endPointDegree: function (contect, startAngle) {
      var ed = this.endDiag.toString();
      var ea;
      if (this.orient === "^") {
        ea = this.diagToAngleACW(ed, startAngle);
      } else {
        ea = this.diagToAngleCW(ed, startAngle);
      }
      return ea;
    },
    diagToAngleACW: function (diag, angle) {
      switch (diag) {
        case "l": return 90;
        case "r": return -90;
        case "d": return 180;
        case "u": return 0;
        case "dl":
        case "ld":
          return 135;
        case "dr":
        case "rd":
          return -135;
        case "ul":
        case "lu":
          return 45;
        case "ur":
        case "ru":
          return -45;
        default:
          if (angle !== undefined) {
            return angle + 180;
          } else {
            return 0;
          }
      }
    },
    diagToAngleCW: function (diag, angle) {
      switch (diag) {
        case "l": return -90;
        case "r": return 90;
        case "d": return 0;
        case "u": return 180;
        case "dl":
        case "ld":
          return -45;
        case "dr":
        case "rd":
          return 45;
        case "ul":
        case "lu":
          return -135;
        case "ur":
        case "ru":
          return 135;
        default:
          if (angle !== undefined) {
            return angle + 180;
          } else {
            return 0;
          }
      }
    }
  });
  AST.ObjectBox.Cir.Cir.Full.Augment({
    toDropShape: function (context, x, y, r) {
      var fullCircleShape = xypic.Shape.FullCircleShape(x, y, r);
      context.appendShapeToFront(fullCircleShape);
      return fullCircleShape;
    }
  });
  
  AST.ObjectBox.Frame.Augment({
    toDropShape: function (context) {
      var env = context.env;
      env.originalReferencePoint = env.c;
      return this.toDropFilledShape(context, "currentColor", false)
    },
    toDropFilledShape: function (context, color, convertToEllipse) {
      var env = context.env;
      var c = env.c;
      if (c === undefined) {
        return xypic.Shape.none;
      }
      
      var t = AST.xypic.thickness;
      var x = c.x;
      var y = c.y;
      var left = c.l;
      var right = c.r;
      var up = c.u;
      var down = c.d;
      var shape = xypic.Shape.none;
      switch (this.main) {
        case '--':
          var dash = 3 * t;
          if (convertToEllipse) {
            var xy = this.radius.xy(context);
            shape = xypic.Shape.EllipseShape(x + (right - left) / 2, y + (up - down) / 2, xy.x, xy.y, false, color, xypic.em2px(dash) + " " + xypic.em2px(dash));
          } else {
            var radius = this.radius.radius(context);
            shape = xypic.Shape.RectangleShape(x, y, left, right, up, down, radius, false, color, xypic.em2px(dash) + " " + xypic.em2px(dash));
          }
          break;
          
        case '==':
          var dash = 3 * t;
          if (convertToEllipse) {
            var xy = this.radius.xy(context);
            shape = xypic.Shape.EllipseShape(x + (right - left) / 2, y + (up - down) / 2, xy.x, xy.y, true, color, xypic.em2px(dash) + " " + xypic.em2px(dash));
          } else {
            var radius = this.radius.radius(context);
            shape = xypic.Shape.RectangleShape(x, y, left, right, up, down, radius, true, color, xypic.em2px(dash) + " " + xypic.em2px(dash));
          }
          break;
          
        case 'o-':
          var dash = 3 * t;
          var radius = AST.xypic.lineElementLength;
          shape = xypic.Shape.RectangleShape(x, y, left, right, up, down, radius, false, color, xypic.em2px(dash) + " " + xypic.em2px(dash));
          break;
          
        case 'oo':
          var xy = this.radius.xy(context);
          var r = xy.x;
          shape = xypic.Shape.EllipseShape(x + (right - left) / 2, y + (up - down) / 2, r, r, true, color, undefined);
          break;
          
        case 'ee':
          var xy = this.radius.xy(context);
          shape = xypic.Shape.EllipseShape(x + (right - left) / 2, y + (up - down) / 2, xy.x, xy.y, true, color, undefined);
          break;
          
        case '-,':
          var depth = this.radius.depth(context);
          var radius = this.radius.radius(context);
          shape = xypic.Shape.CompositeShape(
            xypic.Shape.RectangleShape(x, y, left, right, up, down, radius, false, color, undefined),
            xypic.Shape.BoxShadeShape(x, y, left, right, up, down, depth)
          );
          break;
          
        case '.o':
          var xy = this.radius.xy(context);
          var r = xy.x;
          shape = xypic.Shape.EllipseShape(x + (right - left) / 2, y + (up - down) / 2, r, r, false, color, AST.xypic.dottedDasharray);
          break;
          
        case '-o':
          var dash = 3 * t;
          var xy = this.radius.xy(context);
          var r = xy.x;
          shape = xypic.Shape.EllipseShape(x + (right - left) / 2, y + (up - down) / 2, r, r, false, color, xypic.em2px(dash) + " " + xypic.em2px(dash));
          break;
          
        case '.e':
          var xy = this.radius.xy(context);
          shape = xypic.Shape.EllipseShape(x + (right - left) / 2, y + (up - down) / 2, xy.x, xy.y, false, color, AST.xypic.dottedDasharray);
          break;
          
        case '-e':
          var dash = 3 * t;
          var xy = this.radius.xy(context);
          shape = xypic.Shape.EllipseShape(x + (right - left) / 2, y + (up - down) / 2, xy.x, xy.y, false, color, xypic.em2px(dash) + " " + xypic.em2px(dash));
          break;
          
        case '-':
          if (convertToEllipse) {
            var xy = this.radius.xy(context);
            shape = xypic.Shape.EllipseShape(x + (right - left) / 2, y + (up - down) / 2, xy.x, xy.y, false, color, undefined);
          } else {
            var radius = this.radius.radius(context);
            shape = xypic.Shape.RectangleShape(x, y, left, right, up, down, radius, false, color, undefined);
          }
          break;
          
        case '=':
          if (convertToEllipse) {
            var xy = this.radius.xy(context);
            shape = xypic.Shape.EllipseShape(x + (right - left) / 2, y + (up - down) / 2, xy.x, xy.y, true, color, undefined);
          } else {
            var radius = this.radius.radius(context);
            shape = xypic.Shape.RectangleShape(x, y, left, right, up, down, radius, true, color, undefined);
          }
          break;
          
        case '.':
          if (convertToEllipse) {
            var xy = this.radius.xy(context);
            shape = xypic.Shape.EllipseShape(x + (right - left) / 2, y + (up - down) / 2, xy.x, xy.y, false, color, AST.xypic.dottedDasharray);
          } else {
            var radius = this.radius.radius(context);
            shape = xypic.Shape.RectangleShape(x, y, left, right, up, down, radius, false, color, AST.xypic.dottedDasharray);
          }
          break;
          
        case ',':
          var depth = this.radius.depth(context);
          shape = xypic.Shape.BoxShadeShape(x, y, left, right, up, down, depth, color);
          break;
          
        case 'o':
          var xy = this.radius.xy(context);
          var r = xy.x;
          shape = xypic.Shape.EllipseShape(x + (right - left) / 2, y + (up - down) / 2, r, r, false, color, undefined);
          break;
          
        case 'e':
          var xy = this.radius.xy(context);
          shape = xypic.Shape.EllipseShape(x + (right - left) / 2, y + (up - down) / 2, xy.x, xy.y, false, color, undefined);
          break;
          
        case '\\{':
          shape = xypic.Shape.LeftBrace(x - left, y, up, down, 0, color);
          break;
          
        case '\\}':
          shape = xypic.Shape.LeftBrace(x + right, y, down, up, 180, color);
          break;
          
        case '^\\}':
        case '^\\{':
          shape = xypic.Shape.LeftBrace(x, y + up, right, left, 270, color);
          break;
          
        case '_\\{':
        case '_\\}':
          shape = xypic.Shape.LeftBrace(x, y - down, left, right, 90, color);
          break;
          
        case '(':
          shape = xypic.Shape.LeftParenthesis(x - left, y + (up - down) / 2, up + down, 0, color);
          break;
          
        case ')':
          shape = xypic.Shape.LeftParenthesis(x + right, y + (up - down) / 2, up + down, 180, color);
          break;
          
        case '^(':
        case '^)':
          shape = xypic.Shape.LeftParenthesis(x + (right - left) / 2, y + up, left + right, 270, color);
          break;
          
        case '_(':
        case '_)':
          shape = xypic.Shape.LeftParenthesis(x + (right - left) / 2, y - down, left + right, 90, color);
          break;
          
        case '*':
          if (c.isCircle()) {
            var xy = this.radius.xy(context);
            shape = xypic.Shape.EllipseShape(x + (right - left) / 2, y + (up - down) / 2, xy.x, xy.y, false, "currentColor", undefined, color, true);
          } else {
            var radius = this.radius.radius(context);
            shape = xypic.Shape.RectangleShape(x, y, left, right, up, down, radius, false, "currentColor", undefined, color, true);
          }
          break;
        
        case '**':
          if (c.isCircle()) {
            var xy = this.radius.xy(context);
            shape = xypic.Shape.EllipseShape(x + (right - left) / 2, y + (up - down) / 2, xy.x, xy.y, false, "currentColor", undefined, color, false);
          } else {
            var radius = this.radius.radius(context);
            shape = xypic.Shape.RectangleShape(x, y, left, right, up, down, radius, false, "currentColor", undefined, color, false);
          }
          break;
          
        default:
          return xypic.Shape.none;
      }
      
      context.appendShapeToFront(shape);
      
      return shape;
    },
    toConnectShape: function (context) {
      var env = context.env;
      var c = env.c;
      var p = env.p;
      if (c === undefined || p === undefined) {
        xypic.Shape.none;
      }
      env.originalReferencePoint = c;
      
      var tmpEnv = env.duplicate();
      tmpEnv.c = p.combineRect(c);
      
      var tmpContext = xypic.DrawingContext(xypic.Shape.none, tmpEnv);
      var shape = this.toDropShape(tmpContext);
      context.appendShapeToFront(shape);
      
      return shape;
    }
  });
  AST.ObjectBox.Frame.Radius.Vector.Augment({
    radius: function (context) {
      return this.vector.xy(context).x;
    },
    depth: function (context) {
      return this.vector.xy(context).x;
    },
    xy: function (context) {
      return this.vector.xy(context);
    }
  });
  AST.ObjectBox.Frame.Radius.Default.Augment({
    radius: function (context) {
      return 0;
    },
    depth: function (context) {
      return AST.xypic.thickness / 2;
    },
    xy: function (context) {
      var c = context.env.c;
      return { x:(c.l + c.r) / 2, y:(c.u + c.d) / 2 };
    }
  });
  
  AST.ObjectBox.Dir.Augment({
    toDropShape: function (context) {
      var env = context.env;
      var c = env.c;
      env.originalReferencePoint = c;
      var angle = env.angle;
      if (c === undefined) {
        return xypic.Shape.none;
      }
      env.c = xypic.Frame.Point(c.x, c.y);
      
      var t = AST.xypic.thickness;
      var shape = xypic.Shape.none;
      switch (this.main) {
        case "":
          return xypic.Shape.none;
        case ">":
          switch (this.variant) {
            case "2":
              shape = xypic.Shape.GT2ArrowheadShape(c, angle);
              var r = shape.getRadius();
              env.c = xypic.Frame.Ellipse(c.x, c.y, r, r, r, r);
              break;
            case "3":
              shape = xypic.Shape.GT3ArrowheadShape(c, angle);
              var r = shape.getRadius();
              env.c = xypic.Frame.Ellipse(c.x, c.y, r, r, r, r);
              break;
            default:
              if (this.variant === "^") {
                shape = xypic.Shape.UpperGTArrowheadShape(c, angle);
              } else if (this.variant === "_") {
                shape = xypic.Shape.LowerGTArrowheadShape(c, angle);
              } else {
                shape = xypic.Shape.GTArrowheadShape(c, angle);
              }
          }
          break;
        case "<":
          switch (this.variant) {
            case "2":
              shape = xypic.Shape.LT2ArrowheadShape(c, angle);
              var r = shape.getRadius();
              env.c = xypic.Frame.Ellipse(c.x, c.y, r, r, r, r);
              break;
            case "3":
              shape = xypic.Shape.LT3ArrowheadShape(c, angle);
              var r = shape.getRadius();
              env.c = xypic.Frame.Ellipse(c.x, c.y, r, r, r, r);
              break;
            default:
              if (this.variant === "^") {
                shape = xypic.Shape.UpperLTArrowheadShape(c, angle);
              } else if (this.variant === "_") {
                shape = xypic.Shape.LowerLTArrowheadShape(c, angle);
              } else {
                shape = xypic.Shape.LTArrowheadShape(c, angle);
              }
          }
          break;
        case "|":
          switch (this.variant) {
            case "^":
              shape = xypic.Shape.UpperColumnArrowheadShape(c, angle);
              break;
            case "_":
              shape = xypic.Shape.LowerColumnArrowheadShape(c, angle);
              break;
            case "2":
              shape = xypic.Shape.Column2ArrowheadShape(c, angle);
              break;
            case "3":
              shape = xypic.Shape.Column3ArrowheadShape(c, angle);
              break;
            default:
              shape = xypic.Shape.ColumnArrowheadShape(c, angle);
          }
          break;
        case "(":
          switch (this.variant) {
            case "^":
              shape = xypic.Shape.UpperLParenArrowheadShape(c, angle);
              break;
            case "_":
              shape = xypic.Shape.LowerLParenArrowheadShape(c, angle);
              break;
            default:
              shape = xypic.Shape.LParenArrowheadShape(c, angle);
          }
          break;
        case ")":
          switch (this.variant) {
            case "^":
              shape = xypic.Shape.UpperRParenArrowheadShape(c, angle);
              break;
            case "_":
              shape = xypic.Shape.LowerRParenArrowheadShape(c, angle);
              break;
            default:
              shape = xypic.Shape.RParenArrowheadShape(c, angle);
          }
          break;
        case "`":
          switch (this.variant) {
            case "_":
              shape = xypic.Shape.LowerBackquoteArrowheadShape(c, angle);
              break;
            case "^":
            default:
              shape = xypic.Shape.UpperBackquoteArrowheadShape(c, angle);
              break;
          }
          break;
        case "'":
          switch (this.variant) {
            case "_":
              shape = xypic.Shape.LowerQuoteArrowheadShape(c, angle);
              break;
            case "^":
            default:
              shape = xypic.Shape.UpperQuoteArrowheadShape(c, angle);
              break;
          }
          break;
        case '*':
          shape = xypic.Shape.AsteriskArrowheadShape(c, 0);
          break;
        case 'o':
          shape = xypic.Shape.OArrowheadShape(c, 0);
          break;
        case '+':
          shape = xypic.Shape.PlusArrowheadShape(c, angle);
          break;
        case 'x':
          shape = xypic.Shape.XArrowheadShape(c, angle);
          break;
        case '/':
          shape = xypic.Shape.SlashArrowheadShape(c, angle);
          break;
        case '-':
        case '--':
          var lineLen = AST.xypic.lineElementLength;
          if (this.variant === "3") {
            shape = xypic.Shape.Line3ArrowheadShape(c, angle);
          } else if (this.variant === "2") {
            shape = xypic.Shape.Line2ArrowheadShape(c, angle);
          } else {
            shape = xypic.Shape.LineArrowheadShape(c, angle);
          }
          break;
        case '=':
        case '==':
          shape = xypic.Shape.Line2ArrowheadShape(c, angle);
          break;
        case '.':
        case '..':
          if (this.variant === "3") {
            shape = xypic.Shape.Dot3ArrowheadShape(c, angle);
          } else if (this.variant === "2") {
            shape = xypic.Shape.Dot2ArrowheadShape(c, angle);
          } else {
            shape = xypic.Shape.DotArrowheadShape(c, angle);
          }
          break;
        case ':':
        case '::':
          shape = xypic.Shape.Dot2ArrowheadShape(c, angle);
          break;
        case '~':
        case '~~':
          if (this.variant === "3") {
            shape = xypic.Shape.Tilde3ArrowheadShape(c, angle);
          } else if (this.variant === "2") {
            shape = xypic.Shape.Tilde2ArrowheadShape(c, angle);
          } else {
            shape = xypic.Shape.TildeArrowheadShape(c, angle);
          }
          break;
        case '>>':
          switch (this.variant) {
            case "^":
              shape = xypic.Shape.UpperGTGTArrowheadShape(c, angle);
              break;
            case "_":
              shape = xypic.Shape.LowerGTGTArrowheadShape(c, angle);
              break;
            case "2":
              shape = xypic.Shape.GTGT2ArrowheadShape(c, angle);
              var r = shape.getRadius();
              env.c = xypic.Frame.Ellipse(c.x, c.y, r, r, r, r);
              break;
            case "3":
              shape = xypic.Shape.GTGT3ArrowheadShape(c, angle);
              var r = shape.getRadius();
              env.c = xypic.Frame.Ellipse(c.x, c.y, r, r, r, r);
              break;
            default:
              shape = xypic.Shape.GTGTArrowheadShape(c, angle);
              break;
          }
          break;
        case '<<':
          switch (this.variant) {
            case "^":
              shape = xypic.Shape.UpperLTLTArrowheadShape(c, angle);
              break;
            case "_":
              shape = xypic.Shape.LowerLTLTArrowheadShape(c, angle);
              break;
            case "2":
              shape = xypic.Shape.LTLT2ArrowheadShape(c, angle);
              var r = shape.getRadius();
              env.c = xypic.Frame.Ellipse(c.x, c.y, r, r, r, r);
              break;
            case "3":
              shape = xypic.Shape.LTLT3ArrowheadShape(c, angle);
              var r = shape.getRadius();
              env.c = xypic.Frame.Ellipse(c.x, c.y, r, r, r, r);
              break;
            default:
              shape = xypic.Shape.LTLTArrowheadShape(c, angle);
              break;
          }
          break;
        case '||':
          switch (this.variant) {
            case "^":
              shape = xypic.Shape.UpperColumnColumnArrowheadShape(c, angle);
              break;
            case "_":
              shape = xypic.Shape.LowerColumnColumnArrowheadShape(c, angle);
              break;
            case "2":
              shape = xypic.Shape.ColumnColumn2ArrowheadShape(c, angle);
              break;
            case "3":
              shape = xypic.Shape.ColumnColumn3ArrowheadShape(c, angle);
              break;
            default:
              shape = xypic.Shape.ColumnColumnArrowheadShape(c, angle);
              break;
          }
          break;
        case '|-':
          switch (this.variant) {
            case "^":
              shape = xypic.Shape.UpperColumnLineArrowheadShape(c, angle);
              break;
            case "_":
              shape = xypic.Shape.LowerColumnLineArrowheadShape(c, angle);
              break;
            case "2":
              shape = xypic.Shape.ColumnLine2ArrowheadShape(c, angle);
              break;
            case "3":
              shape = xypic.Shape.ColumnLine3ArrowheadShape(c, angle);
              break;
            default:
              shape = xypic.Shape.ColumnLineArrowheadShape(c, angle);
              break;
          }
          break;
        case '>|':
          shape = xypic.Shape.GTColumnArrowheadShape(c, angle);
          break;
        case ">>|":
          shape = xypic.Shape.GTGTColumnArrowheadShape(c, angle);
          break;
        case "|<":
          shape = xypic.Shape.ColumnLTArrowheadShape(c, angle);
          break;
        case "|<<":
          shape = xypic.Shape.ColumnLTLTArrowheadShape(c, angle);
          break;
        case "//":
          shape = xypic.Shape.SlashSlashArrowheadShape(c, angle);
          break;
        case "=>":
          shape = xypic.Shape.LineGT2ArrowheadShape(c, angle);
          break;
          
        default:
          var newdirObj = xypic.repositories.dirRepository.get(this.main);
          if (newdirObj !== undefined) {
            shape = newdirObj.toDropShape(context);
          } else {
            throw xypic.ExecutionError("\\dir " + this.variant + "{" + this.main + "} not defined.");
          }
      }
      
      context.appendShapeToFront(shape);
      return shape;
    },
    toConnectShape: function (context) {
      // 多重線の幅、点線・破線の幅の基準
      var env = context.env;
      env.originalReferencePoint = env.c;
      var t = AST.xypic.thickness;
      var s = env.p.edgePoint(env.c.x, env.c.y);
      var e = env.c.edgePoint(env.p.x, env.p.y);
      if (s.x !== e.x || s.y !== e.y) {
        var shape = xypic.Curve.Line(s, e).toShape(context, this, this.main, this.variant);
        return shape;
      } else {
        env.angle = 0;
        env.lastCurve = xypic.LastCurve.none;
        return xypic.Shape.none;
      }
    }
  });
  
  AST.ObjectBox.Curve.Augment({
    toDropShape: function (context) {
      var env = context.env;
      env.originalReferencePoint = env.c;
      return xypic.Shape.none;
    },
    toConnectShape: function (context) {
      var env = context.env;
      env.originalReferencePoint = env.c;
      // find object for drop and connect
      var objectForDrop = undefined;
      var objectForConnect = undefined;
      this.objects.foreach(function (o) {
        objectForDrop = o.objectForDrop(objectForDrop);
        objectForConnect = o.objectForConnect(objectForConnect);
      });
      if (objectForDrop === undefined && objectForConnect === undefined) {
        objectForConnect = AST.Object(FP.List.empty, AST.ObjectBox.Dir("", "-"));
      }
      
      var thickness = AST.xypic.thickness;
      
      var c = env.c;
      var p = env.p;
      var controlPoints = [];
      this.poslist.foreach(function (p) {
        p.addPositions(controlPoints, context);
//        svg.createSVGElement("circle", {
//          cx:xypic.em2px(env.c.x), cy:-xypic.em2px(env.c.y), r:xypic.em2px(thickness/2)
//        });
      });
      
      env.c = c;
      env.p = p;
      var shape = xypic.Shape.none;
      var s = p;
      var e = c;
      switch (controlPoints.length) {
        case 0:
          if (s.x === e.x && s.y === e.y) {
            env.lastCurve = xypic.LastCurve.none;
            env.angle = 0;
            return xypic.Shape.none;
          }
          if (objectForConnect !== undefined) {
            return objectForConnect.toConnectShape(context);
          } else {
            return objectForDrop.toConnectShape(context);
          }
          
        case 1:
          var origBezier = xypic.Curve.QuadBezier(s, controlPoints[0], e);
          var tOfShavedStart = origBezier.tOfShavedStart(s);
          var tOfShavedEnd = origBezier.tOfShavedEnd(e);
          if (tOfShavedStart === undefined || tOfShavedEnd === undefined || tOfShavedStart >= tOfShavedEnd) {
              env.angle = 0;
              env.lastCurve = xypic.LastCurve.none;
              return xypic.Shape.none;
          }
          shape = origBezier.toShape(context, objectForDrop, objectForConnect);
          env.lastCurve = xypic.LastCurve.QuadBezier(origBezier, tOfShavedStart, tOfShavedEnd, shape);
          env.angle = Math.atan2(e.y - s.y, e.x - s.x);
          break;
          
        case 2:
          var origBezier = xypic.Curve.CubicBezier(s, controlPoints[0], controlPoints[1], e);
          var tOfShavedStart = origBezier.tOfShavedStart(s);
          var tOfShavedEnd = origBezier.tOfShavedEnd(e);
          if (tOfShavedStart === undefined || tOfShavedEnd === undefined || tOfShavedStart >= tOfShavedEnd) {
              env.angle = 0;
              env.lastCurve = xypic.LastCurve.none;
              return xypic.Shape.none;
          }
          shape = origBezier.toShape(context, objectForDrop, objectForConnect);
          env.lastCurve = xypic.LastCurve.CubicBezier(origBezier, tOfShavedStart, tOfShavedEnd, shape);
          env.angle = Math.atan2(e.y - s.y, e.x - s.x);
          break;
          
        default:
          var spline = xypic.Curve.CubicBSpline(s, controlPoints, e);
          var origBeziers = xypic.Curve.CubicBeziers(spline.toCubicBeziers());
          var tOfShavedStart = origBeziers.tOfShavedStart(s);
          var tOfShavedEnd = origBeziers.tOfShavedEnd(e);
          if (tOfShavedStart === undefined || tOfShavedEnd === undefined || tOfShavedStart >= tOfShavedEnd) {
              env.angle = 0;
              env.lastCurve = xypic.LastCurve.none;
              return xypic.Shape.none;
          }
          shape = origBeziers.toShape(context, objectForDrop, objectForConnect);
          env.lastCurve = xypic.LastCurve.CubicBSpline(s, e, origBeziers, tOfShavedStart, tOfShavedEnd, shape);
          env.angle = Math.atan2(e.y - s.y, e.x - s.x);
          break;
      }
      
//        svg.createSVGElement("rect", {
//          x:xypic.em2px(box.x-box.l), y:xypic.em2px(-box.y-box.u), width:xypic.em2px(box.l+box.r), height:xypic.em2px(box.u+box.d),
//          "stroke-width":"0.02em", stroke:"green"
//        })
      return shape;
    }
  });
  
  AST.ObjectBox.Curve.Object.Drop.Augment({
    objectForDrop: function (object) {
      return this.object;
    },
    objectForConnect: function (object) {
      return object;
    }
  });
  
  AST.ObjectBox.Curve.Object.Connect.Augment({
    objectForDrop: function (object) {
      return object;
    },
    objectForConnect: function (object) {
      return this.object;
    }
  });
  
  AST.ObjectBox.Curve.PosList.CurPos.Augment({
    addPositions: function (controlPoints, context) {
      var env = context.env;
      controlPoints.push(env.c);
    }
  });
  
  AST.ObjectBox.Curve.PosList.Pos.Augment({
    addPositions: function (controlPoints, context) {
      var env = context.env;
      this.pos.toShape(context);
      controlPoints.push(env.c);
    }
  });
  
  AST.ObjectBox.Curve.PosList.AddStack.Augment({
    addPositions: function (controlPoints, context) {
      context.env.stack.reverse().foreach(function (p) {
        controlPoints.push(p);
      });
    }
  });
  
  AST.Coord.C.Augment({
    position: function (context) {
      return context.env.c;
    }
  });
  
  AST.Coord.P.Augment({
    position: function (context) {
      return context.env.p;
    }
  });
  
  AST.Coord.X.Augment({
    position: function (context) {
      var env = context.env;
      var p = env.p;
      var c = env.c;
      var o = env.origin;
      var b = env.xBase;
      var a0 = c.y - p.y, b0 = p.x - c.x, c0 = c.x * p.y - c.y * p.x;
      var a1 = b.y, b1 = -b.x, c1 = b.x * o.y - b.y * o.x;
      var d = a0 * b1 - a1 * b0;
      
      if (Math.abs(d) < AST.xypic.machinePrecision) {
        console.log("there is no intersection point.");
        return xypic.Env.originPosition;
      }
      var x = -(b1 * c0 - b0 * c1)/d;
      var y = (a1 * c0 - a0 * c1)/d;
      return xypic.Frame.Point(x, y);
    }
  });
  
  AST.Coord.Y.Augment({
    position: function (context) {
      var env = context.env;
      var p = env.p;
      var c = env.c;
      var o = env.origin;
      var b = env.yBase;
      var a0 = c.y - p.y, b0 = p.x - c.x, c0 = c.x * p.y - c.y * p.x;
      var a1 = b.y, b1 = -b.x, c1 = b.x * o.y - b.y * o.x;
      var d = a0 * b1 - a1 * b0;
      
      if (Math.abs(d) < AST.xypic.machinePrecision) {
        console.log("there is no intersection point.");
        return xypic.Env.originPosition;
      }
      var x = -(b1 * c0 - b0 * c1)/d;
      var y = (a1 * c0 - a0 * c1)/d;
      return xypic.Frame.Point(x, y);
    }
  });
  
  AST.Coord.Vector.Augment({
    position: function (context) {
      var xy = this.vector.xy(context);
      return xypic.Frame.Point(xy.x, xy.y);
    }
  });
  
  AST.Coord.Id.Augment({
    position: function (context) {
      return context.env.lookupPos(this.id).position(context);
    }
  });
  
  AST.Coord.Group.Augment({
    position: function (context) {
      var env = context.env;
      var origin = env.origin;
      var xBase = env.xBase;
      var yBase = env.yBase;
      var p = env.p;
      // side effect
      this.posDecor.toShape(context);
      env.p = p;
      env.origin = origin;
      env.xBase = xBase;
      env.yBase = yBase;
      return env.c;
    }
  });
  
  AST.Coord.StackPosition.Augment({
    position: function (context) {
      return context.env.stackAt(this.number);
    }
  });
  
  AST.Coord.DeltaRowColumn.Augment({
    position: function (context) {
      var env = context.env;
      var row = env.xymatrixRow;
      var col = env.xymatrixCol;
      if (row === undefined || col === undefined) {
        throw xypic.ExecutionError("xymatrix rows and columns not found for " + this.toSring());
      }
      var id = this.prefix + (row + this.dr) + "," + (col + this.dc);
      return context.env.lookupPos(id, 'in entry "' + env.xymatrixRow + "," + env.xymatrixCol + '": No ' + this + " (is " + id + ") from here.").position(context);
    }
  });
  
  AST.Coord.Hops.Augment({
    position: function (context) {
      var env = context.env;
      var row = env.xymatrixRow;
      var col = env.xymatrixCol;
      if (row === undefined || col === undefined) {
        throw xypic.ExecutionError("xymatrix rows and columns not found for " + this.toSring());
      }
      this.hops.foreach(function (hop) {
        switch (hop) {
          case 'u':
            row -= 1;
            break;
          case 'd':
            row += 1;
            break;
          case 'l':
            col -= 1;
            break;
          case 'r':
            col += 1;
            break;
        }
      });
      var id = this.prefix + row + "," + col;
      return context.env.lookupPos(id, 'in entry "' + env.xymatrixRow + "," + env.xymatrixCol + '": No ' + this + " (is " + id + ") from here.").position(context);
    }
  });
  
  AST.Coord.HopsWithPlace.Augment({
    position: function (context) {
      var env = context.env;
      var row = env.xymatrixRow;
      var col = env.xymatrixCol;
      if (row === undefined || col === undefined) {
        throw xypic.ExecutionError("xymatrix rows and columns not found for " + this.toSring());
      }
      this.hops.foreach(function (hop) {
        switch (hop) {
          case 'u':
            row -= 1;
            break;
          case 'd':
            row += 1;
            break;
          case 'l':
            col -= 1;
            break;
          case 'r':
            col += 1;
            break;
        }
      });
      var id = this.prefix + row + "," + col;
      var pos = context.env.lookupPos(id, 'in entry "' + env.xymatrixRow + "," + env.xymatrixCol + '": No ' + this + " (is " + id + ") from here.").position(context);
      var c = env.c;
      
      var tmpEnv = env.duplicate();
      tmpEnv.p = env.c;
      tmpEnv.c = pos;
      var dx = tmpEnv.c.x - tmpEnv.p.x;
      var dy = tmpEnv.c.y - tmpEnv.p.y;
      var angle;
      if (dx === 0 && dy === 0) {
        angle = 0;
      } else {
        angle = Math.atan2(dy, dx);
      }
      tmpEnv.angle = angle;
      var s = tmpEnv.p.edgePoint(tmpEnv.c.x, tmpEnv.c.y);
      var e = tmpEnv.c.edgePoint(tmpEnv.p.x, tmpEnv.p.y);
      tmpEnv.lastCurve = xypic.LastCurve.Line(s, e, tmpEnv.p, tmpEnv.c, undefined);
      var tmpContext = xypic.DrawingContext(xypic.Shape.none, tmpEnv);
      var t = this.place.toShape(tmpContext);
      
      return tmpEnv.lastCurve.position(t);
    }
  });
  
  AST.Vector.InCurBase.Augment({
    xy: function (context) {
      return context.env.absVector(this.x, this.y);
    },
    angle: function (context) {
      var xy = context.env.absVector(this.x, this.y);
      return Math.atan2(xy.y, xy.x);
    }
  });
  
  AST.Vector.Abs.Augment({
    xy: function (context) {
      return { x:xypic.length2em(this.x), y:xypic.length2em(this.y) };
    },
    angle: function (context) {
      var xy = this.xy(context);
      return Math.atan2(xy.y, xy.x);
    }
  });
  
  AST.Vector.Angle.Augment({
    xy: function (context) {
      var angle = Math.PI / 180 * this.degree;
      var xy = context.env.absVector(Math.cos(angle), Math.sin(angle));
      return xy;
    },
    angle: function (context) {
      return Math.PI / 180 * this.degree;
    }
  });
  
  AST.Vector.Dir.Augment({
    xy: function (context) {
      var l = xypic.length2em(this.dimen);
      var angle = this.dir.angle(context);
      return { x:l * Math.cos(angle), y:l * Math.sin(angle) };
    },
    angle: function (context) {
      return this.dir.angle(context);
    }
  });
  
  AST.Vector.Corner.Augment({
    xy: function (context) {
      var xy = this.corner.xy(context);
      return { x:xy.x*this.factor, y:xy.y*this.factor };
    },
    angle: function (context) {
      return this.corner.angle(context);
    }
  });
  
  AST.Corner.L.Augment({
    xy: function (context) {
      var c = context.env.c;
      return { x:-c.l, y:0 };
    },
    angle: function (context) {
      return Math.PI;
    }
  });
  
  AST.Corner.R.Augment({
    xy: function (context) {
      var c = context.env.c;
      return { x:c.r, y:0 };
    },
    angle: function (context) {
      return 0;
    }
  });
  
  AST.Corner.D.Augment({
    xy: function (context) {
      var c = context.env.c;
      return { x:0, y:-c.d };
    },
    angle: function (context) {
      return -Math.PI / 2;
    }
  });
  
  AST.Corner.U.Augment({
    xy: function (context) {
      var c = context.env.c;
      return { x:0, y:c.u };
    },
    angle: function (context) {
      return Math.PI / 2;
    }
  });
  
  AST.Corner.CL.Augment({
    xy: function (context) {
      var c = context.env.c;
      return { x:-c.l, y:(c.u - c.d) / 2 };
    },
    angle: function (context) {
      var xy = this.xy(context);
      return Math.atan2(xy.y, xy.x);
    }
  });
  
  AST.Corner.CR.Augment({
    xy: function (context) {
      var c = context.env.c;
      return { x:c.r, y:(c.u - c.d) / 2 };
    },
    angle: function (context) {
      var xy = this.xy(context);
      return Math.atan2(xy.y, xy.x);
    }
  });
  
  AST.Corner.CD.Augment({
    xy: function (context) {
      var c = context.env.c;
      return { x:(c.r-c.l)/2, y:-c.d };
    },
    angle: function (context) {
      var xy = this.xy(context);
      return Math.atan2(xy.y, xy.x);
    }
  });
  
  AST.Corner.CU.Augment({
    xy: function (context) {
      var c = context.env.c;
      return { x:(c.r-c.l)/2, y:c.u };
    },
    angle: function (context) {
      var xy = this.xy(context);
      return Math.atan2(xy.y, xy.x);
    }
  });
  
  AST.Corner.LU.Augment({
    xy: function (context) {
      var c = context.env.c;
      return { x:-c.l, y:c.u };
    },
    angle: function (context) {
      var xy = this.xy(context);
      return Math.atan2(xy.y, xy.x);
    }
  });
  
  AST.Corner.LD.Augment({
    xy: function (context) {
      var c = context.env.c;
      return { x:-c.l, y:-c.d };
    },
    angle: function (context) {
      var xy = this.xy(context);
      return Math.atan2(xy.y, xy.x);
    }
  });
  
  AST.Corner.RU.Augment({
    xy: function (context) {
      var c = context.env.c;
      return { x:c.r, y:c.u };
    },
    angle: function (context) {
      var xy = this.xy(context);
      return Math.atan2(xy.y, xy.x);
    }
  });
  
  AST.Corner.RD.Augment({
    xy: function (context) {
      var c = context.env.c;
      return { x:c.r, y:-c.d };
    },
    angle: function (context) {
      var xy = this.xy(context);
      return Math.atan2(xy.y, xy.x);
    }
  });
  
  AST.Corner.NearestEdgePoint.Augment({
    xy: function (context) {
      var env = context.env;
      var c = env.c;
      var e = c.edgePoint(env.p.x, env.p.y);  
      return { x:e.x - c.x, y:e.y - c.y };
    },
    angle: function (context) {
      var xy = this.xy(context);
      return Math.atan2(xy.y, xy.x);
    }
  });
  
  AST.Corner.PropEdgePoint.Augment({
    xy: function (context) {
      var env = context.env;
      var c = env.c;
      var e = c.proportionalEdgePoint(env.p.x, env.p.y);
      return { x:e.x - c.x, y:e.y - c.y };
    },
    angle: function (context) {
      var xy = this.xy(context);
      return Math.atan2(xy.y, xy.x);
    }
  });
  
  AST.Corner.Axis.Augment({
    xy: function (context) {
      return { x:0, y:AST.xypic.axisHeightLength };
    },
    angle: function (context) {
      return Math.PI / 2;
    }
  });
  
  AST.Modifier.Augment({
    proceedModifyShape: function (context, objectShape, restModifiers) {
      if (restModifiers.isEmpty) {
        return objectShape;
      } else {
        return restModifiers.head.modifyShape(context, objectShape, restModifiers.tail);
      }
    }
  });
  
  AST.Modifier.Vector.Augment({
    preprocess: function (context, reversedProcessedModifiers) {
    },
    modifyShape: function (context, objectShape, restModifiers) {
      var d = this.vector.xy(context);
      var env = context.env;
      env.c = env.c.shiftFrame(-d.x, -d.y);
      objectShape = xypic.Shape.TranslateShape(-d.x, -d.y, objectShape);
      return this.proceedModifyShape(context, objectShape, restModifiers);
    }
  });
  
  AST.Modifier.RestoreOriginalRefPoint.Augment({
    preprocess: function (context, reversedProcessedModifiers) {
    },
    modifyShape: function (context, objectShape, restModifiers) {
      var env = context.env;
      var origRefPoint = env.originalReferencePoint;
      if (origRefPoint !== undefined) {
        var dx = env.c.x - origRefPoint.x;
        var dy = env.c.y - origRefPoint.y;
        env.c = env.c.shiftFrame(dx, dy);
        objectShape = xypic.Shape.TranslateShape(dx, dy, objectShape);
      }
      return this.proceedModifyShape(context, objectShape, restModifiers);
    }
  });
  
  AST.Modifier.Shape.Point.Augment({
    preprocess: function (context, reversedProcessedModifiers) {
    },
    modifyShape: function (context, objectShape, restModifiers) {
      var c = context.env.c;
      context.env.c = xypic.Frame.Point(c.x, c.y);
      return this.proceedModifyShape(context, objectShape, restModifiers);
    }
  });
  
  AST.Modifier.Shape.Rect.Augment({
    preprocess: function (context, reversedProcessedModifiers) {
    },
    modifyShape: function (context, objectShape, restModifiers) {
      var c = context.env.c;
      context.env.c = xypic.Frame.Rect(c.x, c.y, { l:c.l, r:c.r, u:c.u, d:c.d });
      return this.proceedModifyShape(context, objectShape, restModifiers);
    }
  });
  
  AST.Modifier.Shape.Circle.Augment({
    preprocess: function (context, reversedProcessedModifiers) {
    },
    modifyShape: function (context, objectShape, restModifiers) {
      var c = context.env.c;
      context.env.c = xypic.Frame.Ellipse(c.x, c.y, c.l, c.r, c.u, c.d);
      return this.proceedModifyShape(context, objectShape, restModifiers);
    }
  });
  
  AST.Modifier.Shape.L.Augment({
    preprocess: function (context, reversedProcessedModifiers) {
    },
    modifyShape: function (context, objectShape, restModifiers) {
      var env = context.env;
      var c = env.c;
      if (c !== undefined) {
        var width = c.r + c.l;
        var height = c.u + c.d;
        var dx, dy;
        if (width < height) {
          dx = (c.l - c.r) / 2;
          dy = (c.d - c.u) / 2;
        } else {
          dx = -c.r + height / 2;
          dy = (c.d - c.u) / 2;
        }
        env.c = env.c.shiftFrame(dx, dy);
        objectShape = xypic.Shape.TranslateShape(dx, dy, objectShape);
      }
      return this.proceedModifyShape(context, objectShape, restModifiers);
    }
  });
  
  AST.Modifier.Shape.R.Augment({
    preprocess: function (context, reversedProcessedModifiers) {
    },
    modifyShape: function (context, objectShape, restModifiers) {
      var env = context.env;
      var c = env.c;
      if (c !== undefined) {
        var width = c.r + c.l;
        var height = c.u + c.d;
        var dx, dy;
        if (width < height) {
          dx = (c.l - c.r) / 2;
          dy = (c.d - c.u) / 2;
        } else {
          dx = c.l - height / 2;
          dy = (c.d - c.u) / 2;
        }
        env.c = env.c.shiftFrame(dx, dy);
        objectShape = xypic.Shape.TranslateShape(dx, dy, objectShape);
      }
      return this.proceedModifyShape(context, objectShape, restModifiers);
    }
  });
  
  AST.Modifier.Shape.U.Augment({
    preprocess: function (context, reversedProcessedModifiers) {
    },
    modifyShape: function (context, objectShape, restModifiers) {
      var env = context.env;
      var c = env.c;
      if (c !== undefined) {
        var width = c.r + c.l;
        var height = c.u + c.d;
        var dx, dy;
        if (width > height) {
          dx = (c.l - c.r) / 2;
          dy = (c.d - c.u) / 2;
        } else {
          dx = (c.l - c.r) / 2;
          dy = c.d - width / 2;
        }
        env.c = env.c.shiftFrame(dx, dy);
        objectShape = xypic.Shape.TranslateShape(dx, dy, objectShape);
      }
      return this.proceedModifyShape(context, objectShape, restModifiers);
    }
  });
  
  AST.Modifier.Shape.D.Augment({
    preprocess: function (context, reversedProcessedModifiers) {
    },
    modifyShape: function (context, objectShape, restModifiers) {
      var env = context.env;
      var c = env.c;
      if (c !== undefined) {
        var width = c.r + c.l;
        var height = c.u + c.d;
        var dx, dy;
        if (width > height) {
          dx = (c.l - c.r) / 2;
          dy = (c.d - c.u) / 2;
        } else {
          dx = (c.l - c.r) / 2;
          dy = -c.u + width / 2;
        }
        env.c = env.c.shiftFrame(dx, dy);
        objectShape = xypic.Shape.TranslateShape(dx, dy, objectShape);
      }
      return this.proceedModifyShape(context, objectShape, restModifiers);
    }
  });
  
  AST.Modifier.Shape.C.Augment({
    preprocess: function (context, reversedProcessedModifiers) {
    },
    modifyShape: function (context, objectShape, restModifiers) {
      var env = context.env;
      var c = env.c;
      if (c !== undefined) {
        var dx, dy;
        dx = (c.l - c.r) / 2;
        dy = (c.d - c.u) / 2;
        env.c = env.c.shiftFrame(dx, dy);
        objectShape = xypic.Shape.TranslateShape(dx, dy, objectShape);
      }
      return this.proceedModifyShape(context, objectShape, restModifiers);
    }
  });
  
  AST.Modifier.Shape.ChangeColor.Augment({
    preprocess: function (context, reversedProcessedModifiers) {
    },
    modifyShape: function (context, objectShape, restModifiers) {
      objectShape = this.proceedModifyShape(context, objectShape, restModifiers);
      return xypic.Shape.ChangeColorShape(this.colorName, objectShape);
    }
  });
  
  AST.Modifier.Shape.Alphabets.Augment({
    preprocess: function (context, reversedProcessedModifiers) {
      var modifier = xypic.repositories.modifierRepository.get(this.alphabets);
      if (modifier !== undefined) {
        return modifier.preprocess(context, reversedProcessedModifiers);
      } else {
        // TODO 存在しないshape名が指定されたらエラーを発生させる。
      }
    },
    modifyShape: function (context, objectShape, restModifiers) {
      var modifier = xypic.repositories.modifierRepository.get(this.alphabets);
      if (modifier !== undefined) {
        return modifier.modifyShape(context, objectShape, restModifiers);
      }
    }
  });
  
  AST.Modifier.Shape.DefineShape.Augment({
    preprocess: function (context, reversedProcessedModifiers) {
      var processedModifiers = reversedProcessedModifiers.reverse();
      xypic.repositories.modifierRepository.put(this.shape, AST.Modifier.Shape.CompositeModifiers(processedModifiers));
    },
    modifyShape: function (context, objectShape, restModifiers) {
      return this.proceedModifyShape(context, objectShape, restModifiers);
    }
  });
  
  // ユーザ定義されたshape
  AST.Modifier.Shape.CompositeModifiers.Augment({
    preprocess: function (context, reversedProcessedModifiers) {
      this.modifiers.foreach(function (m) {
        m.preprocess(context, reversedProcessedModifiers);
        reversedProcessedModifiers = reversedProcessedModifiers.prepend(m);
      });
    },
    modifyShape: function (context, objectShape, restModifiers) {
      objectShape = this.proceedModifyShape(context, objectShape, this.modifiers);
      return this.proceedModifyShape(context, objectShape, restModifiers);
    }
  });
  
  AST.Modifier.Invisible.Augment({
    preprocess: function (context, reversedProcessedModifiers) {
    },
    modifyShape: function (context, objectShape, restModifiers) {
      objectShape = this.proceedModifyShape(context, objectShape, restModifiers);
      return xypic.Shape.none;
    }
  });
  
  AST.Modifier.Hidden.Augment({
    preprocess: function (context, reversedProcessedModifiers) {
    },
    modifyShape: function (context, objectShape, restModifiers) {
      // TODO implement hidden modifier
      return this.proceedModifyShape(context, objectShape, restModifiers);
    }
  });
  
  AST.Modifier.Direction.Augment({
    preprocess: function (context, reversedProcessedModifiers) {
      context.env.angle = this.direction.angle(context);
    },
    modifyShape: function (context, objectShape, restModifiers) {
      context.env.angle = this.direction.angle(context);
      return this.proceedModifyShape(context, objectShape, restModifiers);
    }
  });
  
  AST.Modifier.AddOp.Augment({
    preprocess: function (context, reversedProcessedModifiers) {
    },
    modifyShape: function (context, objectShape, restModifiers) {
      var c = context.env.c;
      context.env.c = this.op.apply(this.size, c, context);
      context.appendShapeToFront(xypic.Shape.InvisibleBoxShape(context.env.c));
      return this.proceedModifyShape(context, objectShape, restModifiers);
    }
  });
  AST.Modifier.AddOp.Grow.Augment({
    apply: function (size, c, context) {
      var env = context.env;
      var margin = (size.isDefault?
        { x:2 * env.objectmargin, y:2 * env.objectmargin }:
        size.vector.xy(context));
      var xMargin = Math.abs(margin.x / 2);
      var yMargin = Math.abs(margin.y / 2);
      return c.grow(xMargin, yMargin);
    },
    applyToDimen: function (lhsEm, rhsEm) {
      return lhsEm + rhsEm;
    }
  });
  AST.Modifier.AddOp.Shrink.Augment({
    apply: function (size, c, context) {
      var env = context.env;
      var margin = (size.isDefault?
        { x:2 * env.objectmargin, y:2 * env.objectmargin }:
        size.vector.xy(context));
      var xMargin = -Math.abs(margin.x / 2);
      var yMargin = -Math.abs(margin.y / 2);
      return c.grow(xMargin, yMargin);
    },
    applyToDimen: function (lhsEm, rhsEm) {
      return lhsEm - rhsEm;
    }
  });
  AST.Modifier.AddOp.Set.Augment({
    apply: function (size, c, context) {
      var env = context.env;
      var margin = (size.isDefault?
        { x:env.objectwidth, y:env.objectheight }:
        size.vector.xy(context));
      var width = Math.abs(margin.x);
      var height = Math.abs(margin.y);
      return c.toSize(width, height);
    },
    applyToDimen: function (lhsEm, rhsEm) {
      return rhsEm;
    }
  });
  AST.Modifier.AddOp.GrowTo.Augment({
    apply: function (size, c, context) {
      var l = Math.max(c.l + c.r, c.u + c.d);
      var margin = (size.isDefault? { x:l, y:l } : size.vector.xy(context));
      var width = Math.abs(margin.x);
      var height = Math.abs(margin.y);
      return c.growTo(width, height);
    },
    applyToDimen: function (lhsEm, rhsEm) {
      return Math.max(Math.max(lhsEm, rhsEm), 0);
    }
  });
  AST.Modifier.AddOp.ShrinkTo.Augment({
    apply: function (size, c, context) {
      var l = Math.min(c.l + c.r, c.u + c.d);
      var margin = (size.isDefault? { x:l, y:l } : size.vector.xy(context));
      var width = Math.abs(margin.x);
      var height = Math.abs(margin.y);
      return c.shrinkTo(width, height);
    },
    applyToDimen: function (lhsEm, rhsEm) {
      return Math.max(Math.min(lhsEm, rhsEm), 0);
    }
  });
  
  AST.Modifier.Shape.Frame.Augment({
    preprocess: function (context, reversedProcessedModifiers) {
    },
    modifyShape: function (context, objectShape, restModifiers) {
      var env = context.env;
      if (env.c !== undefined) {
        var main = this.main;
        var radius = AST.ObjectBox.Frame.Radius.Default();
        var colorName = "currentColor";
        this.options.foreach(function (op) { radius = op.getRadius(radius); });
        this.options.foreach(function (op) { colorName = op.getColorName(colorName); });
        
        var dummyEnv = env.duplicate();
        var dummyContext = xypic.DrawingContext(xypic.Shape.none, dummyEnv);
        var frameObject = AST.ObjectBox.Frame(radius, this.main);
        var frameShape = frameObject.toDropFilledShape(dummyContext, colorName, env.c.isCircle());
        objectShape = xypic.Shape.CompositeShape(objectShape, frameShape);
      }
      return this.proceedModifyShape(context, objectShape, restModifiers);
    }
  });
  AST.Modifier.Shape.Frame.Radius.Augment({
    getRadius: function (radius) {
      return AST.ObjectBox.Frame.Radius.Vector(this.vector);
    },
    getColorName: function (colorName) {
      return colorName;
    }
  });
  AST.Modifier.Shape.Frame.Color.Augment({
    getRadius: function (radius) {
      return radius;
    },
    getColorName: function (colorName) {
      return this.colorName;
    }
  });
  
  AST.Direction.Compound.Augment({
    angle: function (context) {
      var angle = this.dir.angle(context);
      this.rots.foreach(function (rot) { angle = rot.rotate(angle, context); });
      return angle;
    }
  });
  
  AST.Direction.Diag.Augment({
    angle: function (context) {
      return this.diag.angle(context);
    }
  });
  
  AST.Direction.Vector.Augment({
    angle: function (context) {
      return this.vector.angle(context);
    }
  });
  
  AST.Direction.ConstructVector.Augment({
    angle: function (context) {
      var env = context.env;
      var origin = env.origin;
      var xBase = env.xBase;
      var yBase = env.yBase;
      var p = env.p;
      var c = env.c;
      // side effect
      this.posDecor.toShape(context);
      var angle = Math.atan2(env.c.y - env.p.y, env.c.x - env.p.x);
      env.c = c;
      env.p = p;
      env.origin = origin;
      env.xBase = xBase;
      env.yBase = yBase;
      return angle;
    }
  });
  
  AST.Direction.RotVector.Augment({
    rotate: function (angle, context) {
      return angle + this.vector.angle(context);
    }
  });
  
  AST.Direction.RotCW.Augment({
    rotate: function (angle, context) {
      return angle + Math.PI /2;
    }
  });
  
  AST.Direction.RotAntiCW.Augment({
    rotate: function (angle, context) {
      return angle - Math.PI / 2;
    }
  });
  
  AST.Diag.Default.Augment({
    isEmpty: true,
    angle: function (context) {
      return context.env.angle;
    }
  });
    
  AST.Diag.Angle.Augment({
    isEmpty: false,
    angle: function (context) {
      return this.ang;
    }
  });
  
  AST.Decor.Augment({
    toShape: function (context) {
      this.commands.foreach(function (c) {
        c.toShape(context);
      });
    }
  });
  
  AST.Command.Save.Augment({
    toShape: function (context) {
      context.env.saveState();
      this.pos.toShape(context);
    }
  });
  
  AST.Command.Restore.Augment({
    toShape: function (context) {
      context.env.restoreState();
    }
  });
  
  AST.Command.Pos.Augment({
    toShape: function (context) {
      this.pos.toShape(context);
    }
  });
  
  AST.Command.AfterPos.Augment({
    toShape: function (context) {
      this.pos.toShape(context);
      this.decor.toShape(context);
    }
  });
  
  AST.Command.Drop.Augment({
    toShape: function (context) {
      this.object.toDropShape(context);
    }
  });
  
  AST.Command.Connect.Augment({
    toShape: function (context) {
      this.object.toConnectShape(context);
    }
  });
  
  AST.Command.Relax.Augment({
    toShape: function (context) {
      // do nothing
    }
  });
  
  AST.Command.Ignore.Augment({
    toShape: function (context) {
      // do nothing
    }
  });
  
  AST.Command.ShowAST.Augment({
    toShape: function (context) {
      console.log(this.pos.toString() + " " + this.decor);
    }
  });
  
  AST.Command.Ar.Augment({
    toShape: function (context) {
      var env = context.env;
      var origin = env.origin;
      var xBase = env.xBase;
      var yBase = env.yBase;
      var p = env.p;
      var c = env.c;
      
      env.pathActionForBeforeSegment = FP.Option.empty;
      env.pathActionForAfterSegment = FP.Option.empty;
      env.labelsForNextSegmentOnly = FP.Option.empty;
      env.labelsForLastSegmentOnly = FP.Option.empty;
      env.labelsForEverySegment = FP.Option.empty;
      env.segmentSlideEm = FP.Option.empty;
      env.lastTurnDiag = FP.Option.empty;
      
      env.arrowVariant = "";
      env.tailTip = AST.Command.Ar.Form.Tip.Tipchars("");
      env.headTip = AST.Command.Ar.Form.Tip.Tipchars(">");
      env.stemConn = AST.Command.Ar.Form.Conn.Connchars("-");
      env.reverseAboveAndBelow = false;
      env.arrowObjectModifiers = FP.List.empty;
      
      this.forms.foreach(function (f) { f.toShape(context); });
      
      if (!env.pathActionForBeforeSegment.isDefined) {
      // the following AST means **\dir{stem}.
        env.pathActionForBeforeSegment = FP.Option.Some(
          AST.PosDecor(
            AST.Pos.Coord(
              AST.Coord.C(),
              FP.List.empty.append(
                AST.Pos.ConnectObject(
                  AST.Object(
                    env.arrowObjectModifiers, 
                    env.stemConn.getObject(context)
                  )
                )
              )
            ),
            AST.Decor(FP.List.empty)
          )
        );
      }
      
      env.labelsForNextSegmentOnly = FP.Option.Some(
        AST.Command.Path.Labels(
          FP.List.empty.append(
            AST.Command.Path.Label.At(
              AST.Pos.Place(AST.Place(1, 1, AST.Place.Factor(0), AST.Slide(FP.Option.empty))),
              env.tailTip.getObject(context),
              FP.Option.empty
            )
          )
        )
      );
      
      // arrow head
      env.labelsForLastSegmentOnly = FP.Option.Some(
        AST.Command.Path.Labels(
          FP.List.empty.append(
            AST.Command.Path.Label.At(
              AST.Pos.Place(AST.Place(1, 1, AST.Place.Factor(1), AST.Slide(FP.Option.empty))),
              env.headTip.getObject(context),
              FP.Option.empty
            )
          )
        )
      );
      
      this.path.toShape(context);
      
      env.c = c;
      env.p = p;
      env.origin = origin;
      env.xBase = xBase;
      env.yBase = yBase;
    }
  });
  
  AST.Command.Ar.Form.BuildArrow.Augment({
    toShape: function (context) {
      var env = context.env;
      env.arrowVariant = this.variant;
      env.tailTip = this.tailTip;
      env.stemConn = this.stemConn;
      env.headTip = this.headTip;
    }
  });
  
  AST.Command.Ar.Form.ChangeVariant.Augment({
    toShape: function (context) {
      var env = context.env;
      env.arrowVariant = this.variant;
    }
  });
  
  AST.Command.Ar.Form.ChangeStem.Augment({
    toShape: function (context) {
      var env = context.env;
      env.stemConn = AST.Command.Ar.Form.Conn.Connchars(this.connchar);
    }
  });
  
  AST.Command.Ar.Form.DashArrowStem.Augment({
    toShape: function (context) {
      // TODO impl
    }
  });
  
  AST.Command.Ar.Form.CurveArrow.Augment({
    toShape: function (context) {
      var env = context.env;
      var cpDist = xypic.em2length(xypic.length2em(this.dist) * 2);
      // the following AST means **\crv{{**@{} ?+/d 2l/}}. too long...
      env.pathActionForBeforeSegment = FP.Option.Some(
        AST.PosDecor(
          AST.Pos.Coord(
            AST.Coord.C(),
            FP.List.empty.append(
              AST.Pos.ConnectObject(AST.Object(env.arrowObjectModifiers, AST.ObjectBox.Curve(
                FP.List.empty,
                FP.List.empty.append(
                  AST.ObjectBox.Curve.Object.Connect(
                    env.stemConn.getObject(context)
                  )
                ),
                FP.List.empty.append(
                  AST.ObjectBox.Curve.PosList.Pos(
                    AST.Pos.Coord(
                      AST.Coord.Group(
                        AST.PosDecor(
                          AST.Pos.Coord(
                            AST.Coord.C(),
                            FP.List.empty.append(
                              AST.Pos.ConnectObject(
                                AST.Object(
                                  FP.List.empty,
                                  AST.ObjectBox.Dir("", "")
                                )
                              )
                            ).append(
                              AST.Pos.Place(
                                AST.Place(0, 0, undefined, AST.Slide(FP.Option.empty))
                              )
                            ).append(
                              AST.Pos.Plus(
                                AST.Coord.Vector(
                                  AST.Vector.Dir(this.direction, cpDist)
                                )
                              )
                            )
                          ),
                          AST.Decor(FP.List.empty)
                        )
                      ),
                      FP.List.empty
                    )
                  )
                )
              )))
            )
          ),
          AST.Decor(FP.List.empty)
        )
      );
    }
  });
  
  AST.Command.Ar.Form.CurveFitToDirection.Augment({
    toShape: function (context) {
      // the following AST means **\crv{;+/outdir 3pc/ & ;+/indir 3pc/}.
      var env = context.env;
      env.pathActionForBeforeSegment = FP.Option.Some(
        AST.PosDecor(
          AST.Pos.Coord(
            AST.Coord.C(),
            FP.List.empty.append(
              AST.Pos.ConnectObject(AST.Object(env.arrowObjectModifiers, AST.ObjectBox.Curve(
                FP.List.empty,
                FP.List.empty.append(
                  AST.ObjectBox.Curve.Object.Connect(
                    env.stemConn.getObject(context)
                  )
                ),
                FP.List.empty.append(
                  AST.ObjectBox.Curve.PosList.Pos(
                    AST.Pos.Coord(
                      AST.Coord.C(),
                      FP.List.empty.append(
                        AST.Pos.SwapPAndC(
                          AST.Coord.C()
                        )
                      ).append(
                        AST.Pos.Plus(
                          AST.Coord.Vector(AST.Vector.Dir(this.outDirection, "3pc"))
                        )
                      )
                    )
                  )
                ).append(
                  AST.ObjectBox.Curve.PosList.Pos(
                    AST.Pos.Coord(
                      AST.Coord.C(),
                      FP.List.empty.append(
                        AST.Pos.SwapPAndC(
                          AST.Coord.C()
                        )
                      ).append(
                        AST.Pos.Plus(
                          AST.Coord.Vector(AST.Vector.Dir(this.inDirection, "3pc"))
                        )
                      )
                    )
                  )
                )
              )))
            )
          ),
          AST.Decor(FP.List.empty)
        )
      );
    }
  });
  
  AST.Command.Ar.Form.CurveWithControlPoints.Augment({
    toShape: function (context) {
      var env = context.env;
      tmpEnv = env.duplicate();
      tmpEnv.startCapturePositions();
      var tmpContext = xypic.DrawingContext(xypic.Shape.none, tmpEnv);
      this.coord.position(tmpContext);
      var positions = tmpEnv.endCapturePositions();
      positions = positions.append(tmpEnv.c);
      
      var points = FP.List.empty;
      positions.reverse().foreach(function (pos) {
        var xy = env.inverseAbsVector(pos.x, pos.y);
        points = points.prepend(AST.ObjectBox.Curve.PosList.Pos(
                    AST.Pos.Coord(
                      AST.Coord.Vector(AST.Vector.InCurBase(xy.x, xy.y)),
                      FP.List.empty
                    )
                  ));
      });
      
      // the following AST means **\crv{ control points }.
      env.pathActionForBeforeSegment = FP.Option.Some(
        AST.PosDecor(
          AST.Pos.Coord(
            AST.Coord.C(),
            FP.List.empty.append(
              AST.Pos.ConnectObject(AST.Object(env.arrowObjectModifiers, AST.ObjectBox.Curve(
                FP.List.empty,
                FP.List.empty.append(
                  AST.ObjectBox.Curve.Object.Connect(
                    env.stemConn.getObject(context)
                  )
                ),
                points
              )))
            )
          ),
          AST.Decor(FP.List.empty)
        )
      );
    }
  });
  
  AST.Command.Ar.Form.AddShape.Augment({
    toShape: function (context) {
      context.env.arrowObjectModifiers = FP.List.empty.append(this.shape);
    }
  });
  
  AST.Command.Ar.Form.AddModifiers.Augment({
    toShape: function (context) {
      context.env.arrowObjectModifiers = this.modifiers;
    }
  });
  
  AST.Command.Ar.Form.Slide.Augment({
    toShape: function (context) {
      context.env.segmentSlideEm = FP.Option.Some(xypic.length2em(this.slideDimen));
    }
  });
  
  AST.Command.Ar.Form.LabelAt.Augment({
    toShape: function (context) {
      var env = context.env;
      env.labelsForEverySegment = FP.Option.Some(
        AST.Command.Path.Labels(
          FP.List.empty.append(
            AST.Command.Path.Label.At(
              AST.Pos.Place(this.anchor), this.it, FP.Option.empty
            )
          )
        )
      );
    }
  });
  
  AST.Command.Ar.Form.LabelAbove.Augment({
    toShape: function (context) {
      var env = context.env;
      var label;
      if (env.reverseAboveAndBelow) {
        label = AST.Command.Path.Label.Below(
              AST.Pos.Place(this.anchor), this.it, FP.Option.empty
            );
      } else {
        label = AST.Command.Path.Label.Above(
              AST.Pos.Place(this.anchor), this.it, FP.Option.empty
            );
      }
      env.labelsForEverySegment = FP.Option.Some(
        AST.Command.Path.Labels(FP.List.empty.append(label))
      );
    }
  });
  
  AST.Command.Ar.Form.LabelBelow.Augment({
    toShape: function (context) {
      var env = context.env;
      var label;
      if (env.reverseAboveAndBelow) {
        label = AST.Command.Path.Label.Above(
              AST.Pos.Place(this.anchor), this.it, FP.Option.empty
            );
      } else {
        label = AST.Command.Path.Label.Below(
              AST.Pos.Place(this.anchor), this.it, FP.Option.empty
            );
      }
      env.labelsForEverySegment = FP.Option.Some(
        AST.Command.Path.Labels(FP.List.empty.append(label))
      );
    }
  });
  
  AST.Command.Ar.Form.ReverseAboveAndBelow.Augment({
    toShape: function (context) {
      context.env.reverseAboveAndBelow = true;
    }
  });
  
  AST.Command.Ar.Form.Conn.Connchars.Augment({
    getObject: function (context) {
      var env = context.env;
      var dir = AST.ObjectBox.Dir(env.arrowVariant, this.connchars);
      return AST.Object(env.arrowObjectModifiers, dir);
    }
  });
  
  AST.Command.Ar.Form.Conn.Object.Augment({
    getObject: function (context) {
      var modifiers = context.env.arrowObjectModifiers.concat(this.object.modifiers);
      return AST.Object(modifiers, this.object.object);
    }
  });
  
  AST.Command.Ar.Form.Conn.Dir.Augment({
    getObject: function (context) {
      var env = context.env;
      var thisDir = this.dir;
      var dir = thisDir;
      if (thisDir.variant === "" && env.arrowVariant !== "") {
        dir = AST.ObjectBox.Dir(env.arrowVariant, thisDir.main);
      }
      return AST.Object(env.arrowObjectModifiers, dir);
    }
  });
  
  AST.Command.Ar.Form.Tip.Tipchars.Augment({
    getObject: function (context) {
      var env = context.env;
      var dir = AST.ObjectBox.Dir(env.arrowVariant, this.tipchars);
      return AST.Object(env.arrowObjectModifiers, dir);
    }
  });
  
  AST.Command.Ar.Form.Tip.Object.Augment({
    getObject: function (context) {
      var modifiers = context.env.arrowObjectModifiers.concat(this.object.modifiers);
      return AST.Object(modifiers, this.object.object);
    }
  });
  
  AST.Command.Ar.Form.Tip.Dir.Augment({
    getObject: function (context) {
      var env = context.env;
      var thisDir = this.dir;
      var dir = thisDir;
      if (thisDir.variant === "" && env.arrowVariant !== "") {
        dir = AST.ObjectBox.Dir(env.arrowVariant, thisDir.main);
      }
      return AST.Object(env.arrowObjectModifiers, dir);
    }
  });
  
  
  
  AST.Command.Path.Augment({
    toShape: function (context) {
      var env = context.env;
      var origin = env.origin;
      var xBase = env.xBase;
      var yBase = env.yBase;
      var p = env.p;
      var c = env.c;
      
      env.pathActionForBeforeSegment = FP.Option.empty;
      env.pathActionForAfterSegment = FP.Option.empty;
      env.labelsForNextSegmentOnly = FP.Option.empty;
      env.labelsForLastSegmentOnly = FP.Option.empty;
      env.labelsForEverySegment = FP.Option.empty;
      env.segmentSlideEm = FP.Option.empty;
      env.lastTurnDiag = FP.Option.empty;
      
      this.path.toShape(context);
      
      env.c = c;
      env.p = p;
      env.origin = origin;
      env.xBase = xBase;
      env.yBase = yBase;
    }
  });
  
  AST.Command.AfterPath.Augment({
    toShape: function (context) {
      this.path.toShape(context);
      this.decor.toShape(context);
    }
  });
  
  AST.Command.Path.Path.Augment({
    toShape: function (context) {
      this.pathElements.foreach(function (e) {
        e.toShape(context);
      });
    }
  });
  
  AST.Command.Path.SetBeforeAction.Augment({
    toShape: function (context) {
      context.env.pathActionForBeforeSegment = FP.Option.Some(this.posDecor);
    }
  });
  
  AST.Command.Path.SetAfterAction.Augment({
    toShape: function (context) {
      context.env.pathActionForAfterSegment = FP.Option.Some(this.posDecor);
    }
  });
  
  AST.Command.Path.AddLabelNextSegmentOnly.Augment({
    toShape: function (context) {
      context.env.labelsForNextSegmentOnly = FP.Option.Some(this.labels);
    }
  });
  
  AST.Command.Path.AddLabelLastSegmentOnly.Augment({
    toShape: function (context) {
      context.env.labelsForLastSegmentOnly = FP.Option.Some(this.labels);
    }
  });
  
  AST.Command.Path.AddLabelEverySegment.Augment({
    toShape: function (context) {
      context.env.labelsForEverySegment = FP.Option.Some(this.labels);
    }
  });
  
  AST.Command.Path.StraightSegment.Augment({
    toShape: function (context) {
      var env = context.env;
      this.segment.setupPositions(context);
      var c = env.c;
      env.pathActionForBeforeSegment.foreach(function (action) {
        action.toShape(context);
      });
      env.labelsForNextSegmentOnly.foreach(function (labels) {
        labels.toShape(context);
        env.labelsForNextSegmentOnly = FP.Option.empty;
      });
      env.labelsForEverySegment.foreach(function (labels) {
        labels.toShape(context);
      });
      env.c = c;
      env.pathActionForAfterSegment.foreach(function (action) {
        action.toShape(context);
      });
      this.segment.toLabelsShape(context);
    }
  });
  
  AST.Command.Path.LastSegment.Augment({
    toShape: function (context) {
      var env = context.env;
      this.segment.setupPositions(context);
      var c = env.c;
      env.pathActionForBeforeSegment.foreach(function (action) {
        action.toShape(context);
      });
      env.labelsForNextSegmentOnly.foreach(function (labels) {
        labels.toShape(context);
        env.labelsForNextSegmentOnly = FP.Option.empty;
      });
      env.labelsForLastSegmentOnly.foreach(function (labels) {
        labels.toShape(context);
        env.labelsForNextSegmentOnly = FP.Option.empty;
      });
      env.labelsForEverySegment.foreach(function (labels) {
        labels.toShape(context);
      });
      env.c = c;
      env.pathActionForAfterSegment.foreach(function (action) {
        action.toShape(context);
      });
      this.segment.toLabelsShape(context);
    }
  });
  
  AST.Command.Path.TurningSegment.Augment({
    toShape: function (context) {
      var env = context.env;
      var p = env.c;
      this.segment.pos.toShape(context);
      env.p = p;
      var circle = this.turn.explicitizedCircle(context);
      var r = this.turn.radius.radius(context);
      env.lastTurnDiag = FP.Option.Some(circle.endDiag);
      
      var sv = circle.startVector(context);
      var ev = circle.endVector(context);
      
      var slideEm = env.segmentSlideEm.getOrElse(0);
      this.segment.slide.dimen.foreach(function (d) {
        slideEm = xypic.length2em(d);
        env.segmentSlideEm = FP.Option.Some(slideEm);
      });
      if (slideEm !== 0) {
        env.p = env.p.move(
          env.p.x - slideEm * sv.y,
          env.p.y + slideEm * sv.x);
        env.c = env.c.move(
          env.c.x - slideEm * ev.y,
          env.c.y + slideEm * ev.x);
        if (circle.orient === "^") {
          r = Math.max(0, r - slideEm);
        } else {
          r = Math.max(0, r + slideEm);
        }
      }
      
      var s = env.p.edgePoint(env.p.x + sv.x, env.p.y + sv.y);
      var e = env.c;
      
      var ds = circle.relativeStartPoint(context, r);
      var de = circle.relativeEndPoint(context, r);
      var deo = circle.relativeEndPoint(context, r + (circle.orient === "^"? slideEm : -slideEm));
      
      var t;
      var det = sv.x * ev.y - sv.y * ev.x;
      if (Math.abs(det) < AST.xypic.machinePrecision) {
        t = 0;
      } else {
        var dx = e.x - s.x + ds.x - de.x;
        var dy = e.y - s.y + ds.y - de.y;
        t = (ev.y * dx - ev.x * dy)/det;
        if (t < 0) { t = 0; }
      }
      var x = s.x - ds.x + t * sv.x;
      var y = s.y - ds.y + t * sv.y;
      
      var circleShape = circle.toDropShape(context, x, y, r);
      
      var c = xypic.Frame.Point(x + deo.x, y + deo.y);
      
      env.c = xypic.Frame.Point(x + ds.x, y + ds.y);
      env.pathActionForBeforeSegment.foreach(function (action) {
        action.toShape(context);
      });
      env.labelsForNextSegmentOnly.foreach(function (labels) {
        labels.toShape(context);
        env.labelsForNextSegmentOnly = FP.Option.empty;
      });
      env.labelsForEverySegment.foreach(function (labels) {
        labels.toShape(context);
      });
      env.c = c;
      env.pathActionForAfterSegment.foreach(function (action) {
        action.toShape(context);
      });
      
      this.segment.toLabelsShape(context);
    }
  });
  
  AST.Command.Path.Turn.Cir.Augment({
    explicitizedCircle: function (context) {
      var env = context.env;
      var startDiag, orient, endDiag;
      if (this.cir.startDiag.isEmpty) {
        startDiag = env.lastTurnDiag.getOrElse(AST.Diag.R());
      } else {
        startDiag = this.cir.startDiag;
      }
      orient = this.cir.orient;
      if (this.cir.endDiag.isEmpty) {
        endDiag = startDiag.turn(orient);
      } else {
        endDiag = this.cir.endDiag;
      }
      return AST.ObjectBox.Cir.Cir.Segment(startDiag, orient, endDiag);
    }
  });
  
  AST.ObjectBox.Cir.Cir.Segment.Augment({
    startVector: function (context) {
      var angle = this.startDiag.angle(context);
      return { x:Math.cos(angle), y:Math.sin(angle) };
    },
    endVector: function (context) {
      var angle = this.endDiag.angle(context);
      return { x:Math.cos(angle), y:Math.sin(angle) };
    },
    relativeStartPointAngle: function (context) {
      return this.startPointDegree(context) / 180 * Math.PI;
    },
    relativeStartPoint: function (context, r) {
      var angle = this.startPointDegree(context) / 180 * Math.PI;
      return { x:r * Math.cos(angle), y:r * Math.sin(angle) };
    },
    relativeEndPoint: function (context, r) {
      var angle;
      angle = this.endPointDegree(context, this.relativeStartPointAngle(context)) / 180 * Math.PI;
      return { x:r * Math.cos(angle), y:r * Math.sin(angle) };
    }
  });
  
  AST.Command.Path.Turn.Diag.Augment({
    explicitizedCircle: function (context) {
      var env = context.env;
      var startDiag, orient, endDiag;
      if (this.diag.isEmpty) {
        startDiag = env.lastTurnDiag.getOrElse(AST.Diag.R());
      } else {
        startDiag = this.diag;
      }
      var angle = startDiag.angle(context);
      var det = (env.c.x - env.p.x) * Math.sin(angle) - (env.c.y - env.p.y) * Math.cos(angle);
      orient = (det < 0? "^" : "_");
      endDiag = startDiag.turn(orient);
      return AST.ObjectBox.Cir.Cir.Segment(startDiag, orient, endDiag);
    }
  });
  
  AST.Command.Path.TurnRadius.Default.Augment({
    radius: function (context) {
      return AST.xypic.turnradius;
    }
  });
  
  AST.Command.Path.TurnRadius.Dimen.Augment({
    radius: function (context) {
      return xypic.length2em(this.dimen);
    }
  });
  
  AST.Command.Path.Segment.Augment({
    setupPositions: function (context) {
      var env = context.env;
      env.p = env.c;
      this.pos.toShape(context);
      var p = env.p;
      var c = env.c;
      
      var tx = c.x - p.x;
      var ty = c.y - p.y;
      var angle = Math.atan2(ty, tx) + Math.PI / 2;
      var slideEm = env.segmentSlideEm.getOrElse(0);
      this.slide.dimen.foreach(function (d) {
        slideEm = xypic.length2em(d);
        env.segmentSlideEm = FP.Option.Some(slideEm);
      });
      if (slideEm !== 0) {
        p = p.move(p.x + slideEm * Math.cos(angle), p.y + slideEm * Math.sin(angle));
        c = c.move(c.x + slideEm * Math.cos(angle), c.y + slideEm * Math.sin(angle));
      }
      
      env.p = p;
      env.c = c;
    },
    toLabelsShape: function (context) {
      var env = context.env;
      var c = env.c, p = env.p;
      this.labels.toShape(context);
      env.c = c;
      env.p = p;
    }
  });
  
  AST.Command.Path.Labels.Augment({
    toShape: function (context) {
      this.labels.foreach(function (label) {
        label.toShape(context);
      });
    }
  });
  
  AST.Command.Path.Label.Augment({
    toShape: function (context) {
      var env = context.env;
      var p = env.p;
      var c = env.c;
      var t = this.anchor.toShape(context);
      var labelmargin = this.getLabelMargin(context);
      if (labelmargin !== 0) {
        var lastCurve = env.lastCurve;
        var angle;
        if (!lastCurve.isNone) {
          angle = lastCurve.angle(t) + Math.PI/2 + (labelmargin > 0? 0 : Math.PI);
        } else {
          angle = Math.atan2(c.y - p.y, c.x - p.x) + Math.PI/2;
        }
        var c = env.c;
        var subcontext = xypic.DrawingContext(xypic.Shape.none, env);
        this.it.toDropShape(subcontext);
        var labelShape = subcontext.shape;
        var bbox = labelShape.getBoundingBox();
        if (bbox !== undefined) {
          var x = bbox.x - c.x;
          var y = bbox.y - c.y;
          var l = bbox.l;
          var r = bbox.r;
          var u = bbox.u;
          var d = bbox.d;
          
          var cos = Math.cos(angle);
          var sin = Math.sin(angle);
          var delta = Math.min(
            (x - l) * cos + (y - d) * sin,
            (x - l) * cos + (y + u) * sin,
            (x + r) * cos + (y - d) * sin,
            (x + r) * cos + (y + u) * sin
          );
          var margin = Math.abs(labelmargin) - delta;
          env.c = env.c.move(c.x + margin * cos, c.y + margin * sin);
          context.appendShapeToFront(xypic.Shape.TranslateShape(margin * cos, margin * sin, labelShape));
        }
      } else {
        this.it.toDropShape(context);
      }
      var lastCurve = env.lastCurve;
      
      if (this.shouldSliceHole && lastCurve.isDefined && t !== undefined) {
        lastCurve.sliceHole(env.c, t);
      }
      this.aliasOption.foreach(function (alias) {
        env.savePos(alias, xypic.Saving.Position(env.c));
      });
    }
  });
  
  AST.Command.Path.Label.Above.Augment({
    getLabelMargin: function (context) {
      return context.env.labelmargin;
    },
    shouldSliceHole: false
  });
  
  AST.Command.Path.Label.Below.Augment({
    getLabelMargin: function (context) {
      return -context.env.labelmargin;
    },
    shouldSliceHole: false
  });
  
  AST.Command.Path.Label.At.Augment({
    getLabelMargin: function (context) {
      return 0;
    },
    shouldSliceHole: true
  });
  
  AST.Command.Xymatrix.Augment({
    toShape: function (context) {
      var origEnv = context.env;
      if (origEnv.c === undefined) {
        return xypic.Shape.none;
      }
      
      var subEnv = origEnv.duplicate();
      var subcontext = xypic.DrawingContext(xypic.Shape.none, subEnv);
      subEnv.xymatrixPrefix = "";
      subEnv.xymatrixRowSepEm = xypic.length2em("2pc");
      subEnv.xymatrixColSepEm = xypic.length2em("2pc");
      subEnv.xymatrixPretendEntryHeight = FP.Option.empty;
      subEnv.xymatrixPretendEntryWidth = FP.Option.empty;
      subEnv.xymatrixFixedRow = false;
      subEnv.xymatrixFixedCol = false;
      subEnv.xymatrixOrientationAngle = 0;
      subEnv.xymatrixEntryModifiers = FP.List.empty;
      
      this.setup.foreach(function (sw) { sw.toShape(subcontext); });
      
      var orientation = subEnv.xymatrixOrientationAngle;
      
      var rowCount;
      var columnCount = 0;
      var rownum = 0, colnum;
      var matrix = xypic.Xymatrix(
        this.rows.map(function (row) {
          rownum += 1;
          colnum = 0;
          var rowModel = xypic.Xymatrix.Row(
            row.entries.map(function (entry) {
              colnum += 1;
              var localEnv = subEnv.duplicate();
              localEnv.origin = {x:0, y:0};
              localEnv.p = localEnv.c = xypic.Env.originPosition;
              localEnv.angle = 0;
              localEnv.lastCurve = xypic.LastCurve.none;
              localEnv.xymatrixRow = rownum; // = \the\Row
              localEnv.xymatrixCol = colnum; // = \the\Col
              var localContext = xypic.DrawingContext(xypic.Shape.none, localEnv);
              var shape = entry.toShape(localContext);
              var c = localEnv.c;
              var l, r, u, d;
              if (subEnv.xymatrixPretendEntryHeight.isDefined) {
                var h = subEnv.xymatrixPretendEntryHeight.get;
                u = h / 2;
                d = h / 2;
              } else {
                u = c.u;
                d = c.d;
              }
              if (subEnv.xymatrixPretendEntryWidth.isDefined) {
                var w = subEnv.xymatrixPretendEntryWidth.get;
                l = w / 2;
                r = w / 2;
              } else {
                l = c.l;
                r = c.r;
              }
              var frame = xypic.Frame.Rect(0, 0, { l:l, r:r, u:u, d:d });
              return xypic.Xymatrix.Entry(localEnv.c, shape, entry.decor, frame);
            }),
            orientation
          );
          columnCount = Math.max(columnCount, colnum);
          return rowModel;
        }),
        orientation
      );
      rowCount = rownum;
      
      if (rowCount === 0) {
        return xypic.Shape.none;
      }
      
      var colnum;
      matrix.rows.foreach(function (row) {
        colnum = 0;
        row.entries.foreach (function (entry) {
          colnum += 1;
          var column = matrix.getColumn(colnum);
          column.addEntry(entry);
        });
      });
      
      /*
      console.log(matrix.toString());
      
      var rownum = 0;
      matrix.rows.foreach(function (row) {
        rownum += 1;
        console.log("row[" + rownum + "] #" + row.entries.length() + " u:" + row.getU() + ", d:" + row.getD());
      })
      var colnum = 0;
      matrix.columns.foreach(function (col) {
        colnum += 1;
        console.log("column[" + colnum + "] #" + col.entries.length() + " l:" + col.getL() + ", r:" + col.getR());
      })
      */
      
      var colsep = subEnv.xymatrixColSepEm;
      var xs = [];
      var x = origEnv.c.x;
      xs.push(x);
      if (subEnv.xymatrixFixedCol) {
        var maxL = 0;
        var maxR = 0;
        matrix.columns.foreach(function (col) {
          maxL = Math.max(maxL, col.getL());
          maxR = Math.max(maxR, col.getR());
        });
        matrix.columns.tail.foreach(function (col) {
          x = x + maxR + colsep + maxL;
          xs.push(x);
        });
        l = maxL;
        r = xs[xs.length - 1] + maxR;
      } else {
        var prevCol = matrix.columns.head;
        matrix.columns.tail.foreach(function (col) {
          x = x + prevCol.getR() + colsep + col.getL();
          xs.push(x);
          prevCol = col;
        });
        l = matrix.columns.head.getL();
        r = x + matrix.columns.at(columnCount - 1).getR() - xs[0];
      }
      
      var rowsep = subEnv.xymatrixRowSepEm;
      var ys = [];
      var y = origEnv.c.y;
      ys.push(y);
      if (subEnv.xymatrixFixedRow) {
        var maxU = 0;
        var maxD = 0;
        matrix.rows.foreach(function (row) {
          maxU = Math.max(maxU, row.getU());
          maxD = Math.max(maxD, row.getD());
        });
        matrix.rows.tail.foreach(function (row) {
          y = y - (maxD + rowsep + maxU);
          ys.push(y);
        });
        u = maxU;
        d = ys[0] - ys[ys.length - 1] + maxD;
      } else {
        var prevRow = matrix.rows.head;
        matrix.rows.tail.foreach(function (row) {
          y = y - (prevRow.getD() + rowsep + row.getU());
          ys.push(y);
          prevRow = row;
        });
        u = matrix.rows.head.getU();
        d = ys[0] - y + matrix.rows.at(rowCount - 1).getD();
      }
      origEnv.c = xypic.Frame.Rect(origEnv.c.x, origEnv.c.y, { l:l, r:r, u:u, d:d });
      
      var prefix = subEnv.xymatrixPrefix;
      var cos = Math.cos(orientation);
      var sin = Math.sin(orientation);
      var rowIndex = 0;
      matrix.rows.foreach(function (row) {
        colIndex = 0;
        row.entries.foreach (function (entry) {
          var x0 = xs[colIndex];
          var y0 = ys[rowIndex];
          var x = x0 * cos - y0 * sin;
          var y = x0 * sin + y0 * cos;
          var colnum = colIndex + 1;
          var rownum = rowIndex + 1;
          var pos = xypic.Saving.Position(entry.c.move(x, y));
          subEnv.savePos("" + rownum + "," + colnum, pos);
          subEnv.savePos(prefix + rownum + "," + colnum, pos);
          colIndex += 1;
        });
        rowIndex += 1;
      });
      
      subcontext = xypic.DrawingContext(xypic.Shape.none, subEnv);
      var rowIndex = 0;
      matrix.rows.foreach(function (row) {
        colIndex = 0;
        row.entries.foreach (function (entry) {
          var x0 = xs[colIndex];
          var y0 = ys[rowIndex];
          var x = x0 * cos - y0 * sin;
          var y = x0 * sin + y0 * cos;
          var colnum = colIndex + 1;
          var rownum = rowIndex + 1;
          var objectShape = xypic.Shape.TranslateShape(x, y, entry.objectShape);
          subcontext.appendShapeToFront(objectShape);
          // draw decor
          subEnv.c = entry.c.move(x, y);
          subEnv.xymatrixRow = rownum; // = \the\Row
          subEnv.xymatrixCol = colnum; // = \the\Col
          entry.decor.toShape(subcontext);
          colIndex += 1;
        });
        rowIndex += 1;
      });
      var matrixShape = subcontext.shape;
      context.appendShapeToFront(matrixShape);
      origEnv.savedPosition = subEnv.savedPosition;
      
      return matrixShape;
    }
  });
  
  // xymatrix data models
  xypic.Xymatrix = MathJax.Object.Subclass({
    Init: function (rows, orientation) {
      this.rows = rows;
      this.columns = FP.List.empty;
      this.orientation = orientation;
    },
    getColumn: function (colnum /* >= 1 */) {
      if (this.columns.length() >= colnum) {
        return this.columns.at(colnum - 1);
      } else {
        var column = xypic.Xymatrix.Column(this.orientation);
        this.columns = this.columns.append(column);
        return column;
      }
    },
    toString: function () {
      return "Xymatrix{\n" + this.rows.mkString("\\\\\n") + "\n}";
    }
  });
  xypic.Xymatrix.Row = MathJax.Object.Subclass({
    Init: function (entries, orientation) {
      this.entries = entries;
      this.orientation = orientation;
      memoize(this, "getU");
      memoize(this, "getD");
    },
    getU: function () {
      var orientation = this.orientation;
      var maxU = 0;
      this.entries.foreach(function (e) { maxU = Math.max(maxU, e.getU(orientation)); })
      return maxU;
    },
    getD: function () {
      var orientation = this.orientation;
      var maxD = 0;
      this.entries.foreach(function (e) { maxD = Math.max(maxD, e.getD(orientation)); })
      return maxD;
    },
    toString: function () {
      return this.entries.mkString(" & ");
    }
  });
  xypic.Xymatrix.Column = MathJax.Object.Subclass({
    Init: function (orientation) {
      this.entries = FP.List.empty;
      this.orientation = orientation;
      memoize(this, "getL");
      memoize(this, "getR");
    },
    addEntry: function (entry) {
      this.entries = this.entries.append(entry);
      this.getL.reset;
      this.getR.reset;
    },
    getL: function () {
      var orientation = this.orientation;
      var maxL = 0;
      this.entries.foreach(function (e) { maxL = Math.max(maxL, e.getL(orientation)); })
      return maxL;
    },
    getR: function () {
      var orientation = this.orientation;
      var maxR = 0;
      this.entries.foreach(function (e) { maxR = Math.max(maxR, e.getR(orientation)); })
      return maxR;
    },
    toString: function () {
      return this.entries.mkString(" \\\\ ");
    }
  });
  xypic.Xymatrix.Entry = MathJax.Object.Subclass({
    Init: function (c, objectShape, decor, frame) {
      this.c = c;
      this.objectShape = objectShape;
      this.decor = decor;
      this.frame = frame;
    },
    getDistanceToEdgePoint: function (frame, angle) {
      var edgePoint = frame.edgePoint(frame.x + Math.cos(angle), frame.y + Math.sin(angle));
      var dx = edgePoint.x - frame.x;
      var dy = edgePoint.y - frame.y;
      return Math.sqrt(dx * dx + dy * dy);
    },
    getU: function (orientation) {
      if (orientation === 0) {
        return this.frame.u;
      }
      return this.getDistanceToEdgePoint(this.frame, orientation + Math.PI / 2);
    },
    getD: function (orientation) {
      if (orientation === 0) {
        return this.frame.d;
      }
      return this.getDistanceToEdgePoint(this.frame, orientation - Math.PI / 2);
    },
    getL: function (orientation) {
      if (orientation === 0) {
        return this.frame.l;
      }
      return this.getDistanceToEdgePoint(this.frame, orientation + Math.PI);
    },
    getR: function (orientation) {
      if (orientation === 0) {
        return this.frame.r;
      }
      return this.getDistanceToEdgePoint(this.frame, orientation);
    },
    toString: function () {
      return this.objectShape.toString() + " " + this.decor;
    }
  });
  
  
  AST.Command.Xymatrix.Setup.Prefix.Augment({
    toShape: function (context) {
      context.env.xymatrixPrefix = this.prefix;
    }
  });
  
  AST.Command.Xymatrix.Setup.ChangeSpacing.Row.Augment({
    toShape: function (context) {
      var env = context.env;
      env.xymatrixRowSepEm = this.addop.applyToDimen(env.xymatrixRowSepEm, xypic.length2em(this.dimen));
    }
  });
  
  AST.Command.Xymatrix.Setup.ChangeSpacing.Column.Augment({
    toShape: function (context) {
      var env = context.env;
      env.xymatrixColSepEm = this.addop.applyToDimen(env.xymatrixColSepEm, xypic.length2em(this.dimen));
    }
  });
  
  AST.Command.Xymatrix.Setup.ChangeSpacing.RowAndColumn.Augment({
    toShape: function (context) {
      var env = context.env;
      var sepEm = this.addop.applyToDimen(env.xymatrixRowSepEm, xypic.length2em(this.dimen));
      env.xymatrixRowSepEm = sepEm;
      env.xymatrixColSepEm = sepEm;
    }
  });
  
  AST.Command.Xymatrix.Setup.PretendEntrySize.Height.Augment({
    toShape: function (context) {
      context.env.xymatrixPretendEntryHeight = FP.Option.Some(xypic.length2em(this.dimen));
    }
  });
  
  AST.Command.Xymatrix.Setup.PretendEntrySize.Width.Augment({
    toShape: function (context) {
      context.env.xymatrixPretendEntryWidth = FP.Option.Some(xypic.length2em(this.dimen));
    }
  });
  
  AST.Command.Xymatrix.Setup.PretendEntrySize.HeightAndWidth.Augment({
    toShape: function (context) {
      var len = FP.Option.Some(xypic.length2em(this.dimen));
      context.env.xymatrixPretendEntryHeight = len;
      context.env.xymatrixPretendEntryWidth = len;
    }
  });
  
  AST.Command.Xymatrix.Setup.FixGrid.Row.Augment({
    toShape: function (context) {
      context.env.xymatrixFixedRow = true;
    }
  });
  
  AST.Command.Xymatrix.Setup.FixGrid.Column.Augment({
    toShape: function (context) {
      context.env.xymatrixFixedCol = true;
    }
  });
  
  AST.Command.Xymatrix.Setup.FixGrid.RowAndColumn.Augment({
    toShape: function (context) {
      context.env.xymatrixFixedRow = true;
      context.env.xymatrixFixedCol = true;
    }
  });
  
  AST.Command.Xymatrix.Setup.AdjustEntrySize.Margin.Augment({
    toShape: function (context) {
      var env = context.env;
      env.objectmargin = this.addop.applyToDimen(env.objectmargin, xypic.length2em(this.dimen));
    }
  });
  
  AST.Command.Xymatrix.Setup.AdjustEntrySize.Width.Augment({
    toShape: function (context) {
      var env = context.env;
      env.objectwidth = this.addop.applyToDimen(env.objectwidth, xypic.length2em(this.dimen));
    }
  });
  
  AST.Command.Xymatrix.Setup.AdjustEntrySize.Height.Augment({
    toShape: function (context) {
      var env = context.env;
      env.objectheight = this.addop.applyToDimen(env.objectheight, xypic.length2em(this.dimen));
    }
  });
  
  AST.Command.Xymatrix.Setup.AdjustLabelSep.Augment({
    toShape: function (context) {
      var env = context.env;
      env.labelmargin = this.addop.applyToDimen(env.labelmargin, xypic.length2em(this.dimen));
    }
  });
  
  AST.Command.Xymatrix.Setup.SetOrientation.Augment({
    toShape: function (context) {
      var env = context.env;
      env.xymatrixOrientationAngle = this.direction.angle(context);
    }
  });
  
  AST.Command.Xymatrix.Setup.AddModifier.Augment({
    toShape: function (context) {
      var env = context.env;
      env.xymatrixEntryModifiers = env.xymatrixEntryModifiers.prepend(this.modifier);
    }
  });
  
  AST.Command.Xymatrix.Entry.SimpleEntry.Augment({
    toShape: function (context) {
      var env = context.env;
      var defaultWidth = xypic.em2length(env.objectmargin + env.objectwidth);
      var defaultHeight = xypic.em2length(env.objectmargin + env.objectheight);
      var defaultSizeModifier = AST.Modifier.AddOp(AST.Modifier.AddOp.GrowTo(), AST.Modifier.AddOp.VactorSize(AST.Vector.Abs(
        defaultWidth, defaultHeight
      )));
      var margin = xypic.em2length(env.objectmargin);
      var marginModifier = AST.Modifier.AddOp(AST.Modifier.AddOp.Grow(), AST.Modifier.AddOp.VactorSize(AST.Vector.Abs(
        margin, margin
      )));
      var modifiers = this.modifiers.concat(env.xymatrixEntryModifiers).prepend(defaultSizeModifier).prepend(marginModifier);
      return AST.Object(modifiers, this.objectbox).toDropShape(context);
    }
  });
  
  AST.Command.Xymatrix.Entry.EmptyEntry.Augment({
    toShape: function (context) {
      var env = context.env;
      var defaultWidth = xypic.em2length(env.objectmargin + env.objectwidth);
      var defaultHeight = xypic.em2length(env.objectmargin + env.objectheight);
      var defaultSizeModifier = AST.Modifier.AddOp(AST.Modifier.AddOp.GrowTo(), AST.Modifier.AddOp.VactorSize(AST.Vector.Abs(
        defaultWidth, defaultHeight
      )));
      var margin = xypic.em2length(env.objectmargin);
      var marginModifier = AST.Modifier.AddOp(AST.Modifier.AddOp.Grow(), AST.Modifier.AddOp.VactorSize(AST.Vector.Abs(
        margin, margin
      )));
      var modifiers = env.xymatrixEntryModifiers.prepend(defaultSizeModifier).prepend(marginModifier);
      return AST.Object(modifiers, AST.ObjectBox.Empty()).toDropShape(context);
    }
  });
  
  AST.Command.Xymatrix.Entry.ObjectEntry.Augment({
    toShape: function (context) {
      return this.object.toDropShape(context);
    }
  });
  
  
  AST.Command.Twocell.Augment({
    toShape: function (context) {
      var origEnv = context.env;
      if (origEnv.c === undefined) {
        return xypic.Shape.none;
      }
      
      var subEnv = origEnv.duplicate();
      var subcontext = xypic.DrawingContext(xypic.Shape.none, subEnv);
      subEnv.twocellmodmapobject = origEnv.twocellmodmapobject || AST.Object(FP.List.empty, AST.ObjectBox.Dir("", "|"));
      subEnv.twocellhead = origEnv.twocellhead || AST.Object(FP.List.empty, AST.ObjectBox.Dir("", ">"));
      subEnv.twocelltail = origEnv.twocelltail || AST.Object(FP.List.empty, AST.ObjectBox.Dir("", ""));
      subEnv.twocellarrowobject = origEnv.twocellarrowobject || AST.Object(FP.List.empty, AST.ObjectBox.Dir("", "=>"));
      
      subEnv.twocellUpperCurveObjectSpacer = origEnv.twocellUpperCurveObjectSpacer;
      subEnv.twocellUpperCurveObject = origEnv.twocellUpperCurveObject;
      subEnv.twocellLowerCurveObjectSpacer = origEnv.twocellLowerCurveObjectSpacer;
      subEnv.twocellLowerCurveObject = origEnv.twocellLowerCurveObject;
      
      // temporary attributes
      subEnv.twocellUpperLabel = FP.Option.empty;
      subEnv.twocellLowerLabel = FP.Option.empty;
      subEnv.twocellCurvatureEm = FP.Option.empty;
      subEnv.twocellShouldDrawCurve = true;
      subEnv.twocellShouldDrawModMap = false;
      
      this.switches.foreach(function (sw) { sw.setup(subcontext); });
      this.twocell.toShape(subcontext, this.arrow);
      context.appendShapeToFront(subcontext.shape);
    }
  });
  
  AST.Command.Twocell.Hops2cell.Augment({
    toShape: function (context, arrow) {
      var env = context.env;
      var c = env.c;
      var angle = env.angle;
      
      var s = env.c;
      var e = this.targetPosition(context);
      if (s === undefined || e === undefined) {
        return;
      }
      
      var dx = e.x - s.x;
      var dy = e.y - s.y;
      if (dx === 0 && dy === 0) {
        return;
      }
      
      var m = xypic.Frame.Point(
          s.x + dx * 0.5,
          s.y + dy * 0.5
        );
      var tangle = Math.atan2(dy, dx);
      var antiClockwiseAngle = tangle + Math.PI / 2;
      
      var curvatureEm = env.twocellCurvatureEm.getOrElse(this.getDefaultCurvature());
      var ncos = Math.cos(antiClockwiseAngle);
      var nsin = Math.sin(antiClockwiseAngle);
      var ucp = this.getUpperControlPoint(s, e, m, curvatureEm, ncos, nsin);
      var lcp = this.getLowerControlPoint(s, e, m, curvatureEm, ncos, nsin);
      
      if (env.twocellShouldDrawCurve) {
        // upper curve
        var objectForDrop = env.twocellUpperCurveObjectSpacer;
        var objectForConnect;
        if (objectForDrop === undefined) {
          objectForConnect = AST.Object(FP.List.empty, AST.ObjectBox.Dir("", "-"));
        } else {
          if (env.twocellUpperCurveObject !== undefined) {
            objectForConnect = env.twocellUpperCurveObject.getOrElse(undefined);
          } else {
            objectForConnect = undefined;
          }
        }
        this.toUpperCurveShape(context, s, ucp, e, objectForDrop, objectForConnect);
        if (env.lastCurve.isDefined) {
          env.angle = tangle;
          var ucmp = this.getUpperLabelPosition(s, e, m, curvatureEm, ncos, nsin);
          var uangle = this.getUpperLabelAngle(antiClockwiseAngle, s, e, m, curvatureEm, ncos, nsin);
          env.twocellUpperLabel.foreach(function (l) {
            l.toShape(context, ucmp, Math.cos(uangle), Math.sin(uangle), tangle);
          });
          if (this.hasUpperTips) {
            arrow.toUpperTipsShape(context);
          }
        }
        
        // lower curve
        var objectForDrop = env.twocellLowerCurveObjectSpacer;
        var objectForConnect;
        if (objectForDrop === undefined) {
          objectForConnect = AST.Object(FP.List.empty, AST.ObjectBox.Dir("", "-"));
        } else {
          if (env.twocellLowerCurveObject !== undefined) {
            objectForConnect = env.twocellLowerCurveObject.getOrElse(undefined);
          } else {
            objectForConnect = undefined;
          }
        }
        this.toLowerCurveShape(context, s, lcp, e, objectForDrop, objectForConnect);
        if (env.lastCurve.isDefined) {
          env.angle = tangle;
          var lcmp = this.getLowerLabelPosition(s, e, m, curvatureEm, ncos, nsin);
          var langle = this.getLowerLabelAngle(antiClockwiseAngle, s, e, m, curvatureEm, ncos, nsin);
          env.twocellLowerLabel.foreach(function (l) {
            l.toShape(context, lcmp, Math.cos(langle), Math.sin(langle), tangle);
          });
          if (this.hasLowerTips) {
            arrow.toLowerTipsShape(context);
          }
        }
      }
      
      env.c = this.getDefaultArrowPoint(s, e, m, curvatureEm, ncos, nsin);
      env.angle = antiClockwiseAngle + Math.PI;
      var labelOrigin = m;
      arrow.toArrowShape(context, labelOrigin);
      
      env.c = c;
      env.angle = angle;
    },
    _toCurveShape: function (context, s, cp, e, objectForDrop, objectForConnect) {
      var env = context.env;
      var origBezier = xypic.Curve.QuadBezier(s, cp, e);
      var tOfShavedStart = origBezier.tOfShavedStart(s);
      var tOfShavedEnd = origBezier.tOfShavedEnd(e);
      if (tOfShavedStart === undefined || tOfShavedEnd === undefined || tOfShavedStart >= tOfShavedEnd) {
        env.lastCurve = xypic.LastCurve.none;
        return;
      }
      var curveShape = origBezier.toShape(context, objectForDrop, objectForConnect);
      env.lastCurve = xypic.LastCurve.QuadBezier(origBezier, tOfShavedStart, tOfShavedEnd, curveShape);
    },
    targetPosition: function (context) {
      var env = context.env;
      var row = env.xymatrixRow;
      var col = env.xymatrixCol;
      if (row === undefined || col === undefined) {
        throw xypic.ExecutionError("rows and columns not found for hops [" + this.hops + "]");
      }
      for (var i = 0; i < this.hops.length; i++) {
        switch (this.hops[i]) {
          case 'u':
            row -= 1;
            break;
          case 'd':
            row += 1;
            break;
          case 'l':
            col -= 1;
            break;
          case 'r':
            col += 1;
            break;
        }
      }
      var id = "" + row + "," + col;
      return context.env.lookupPos(id, 'in entry "' + env.xymatrixRow + "," + env.xymatrixCol + '": No ' + this + " (is " + id + ") from here.").position(context);
    }
  });
  
  AST.Command.Twocell.Twocell.Augment({
    getUpperControlPoint: function (s, e, midPoint, curvatureEm, ncos, nsin) {
      return xypic.Frame.Point(
        midPoint.x + curvatureEm * ncos,
        midPoint.y + curvatureEm * nsin
      );
    },
    getLowerControlPoint: function (s, e, midPoint, curvatureEm, ncos, nsin) {
      return xypic.Frame.Point(
        midPoint.x - curvatureEm * ncos,
        midPoint.y - curvatureEm * nsin
      );
    },
    getUpperLabelPosition: function (s, e, midPoint, curvatureEm, ncos, nsin) {
      return xypic.Frame.Point(
        midPoint.x + 0.5 * curvatureEm * ncos,
        midPoint.y + 0.5 * curvatureEm * nsin
      );
    },
    getLowerLabelPosition: function (s, e, midPoint, curvatureEm, ncos, nsin) {
      return xypic.Frame.Point(
        midPoint.x - 0.5 * curvatureEm * ncos,
        midPoint.y - 0.5 * curvatureEm * nsin
      );
    },
    getUpperLabelAngle: function (antiClockwiseAngle, s, e, midPoint, curvatureEm, ncos, nsin) {
      var rot = (curvatureEm < 0? Math.PI : 0);
      return antiClockwiseAngle + rot;
    },
    getLowerLabelAngle: function (antiClockwiseAngle, s, e, midPoint, curvatureEm, ncos, nsin) {
      var rot = (curvatureEm < 0? 0 : Math.PI);
      return antiClockwiseAngle + rot;
    },
    getDefaultArrowPoint: function (s, e, midPoint, curvatureEm, ncos, nsin) {
      return midPoint;
    },
    toUpperCurveShape: function (context, s, cp, e, objectForDrop, objectForConnect) {
      this._toCurveShape(context, s, cp, e, objectForDrop, objectForConnect);
    },
    toLowerCurveShape: function (context, s, cp, e, objectForDrop, objectForConnect) {
      this._toCurveShape(context, s, cp, e, objectForDrop, objectForConnect);
    },
    getDefaultCurvature: function () { return 3.5 * AST.xypic.lineElementLength; },
    hasUpperTips: true,
    hasLowerTips: true
  });
  
  AST.Command.Twocell.UpperTwocell.Augment({
    getUpperControlPoint: function (s, e, midPoint, curvatureEm, ncos, nsin) {
      return xypic.Frame.Point(
        midPoint.x + curvatureEm * ncos,
        midPoint.y + curvatureEm * nsin
      );
    },
    getLowerControlPoint: function (s, e, midPoint, curvatureEm, ncos, nsin) {
      return midPoint;
    },
    getUpperLabelPosition: function (s, e, midPoint, curvatureEm, ncos, nsin) {
      return xypic.Frame.Point(
        midPoint.x + 0.5 * curvatureEm * ncos,
        midPoint.y + 0.5 * curvatureEm * nsin
      );
    },
    getLowerLabelPosition: function (s, e, midPoint, curvatureEm, ncos, nsin) {
      return midPoint;
    },
    getUpperLabelAngle: function (antiClockwiseAngle, s, e, midPoint, curvatureEm, ncos, nsin) {
      var rot = (curvatureEm < 0? Math.PI : 0);
      return antiClockwiseAngle + rot;
    },
    getLowerLabelAngle: function (antiClockwiseAngle, s, e, midPoint, curvatureEm, ncos, nsin) {
      var rot = (curvatureEm < 0? 0 : Math.PI);
      return antiClockwiseAngle + rot;
    },
    getDefaultArrowPoint: function (s, e, midPoint, curvatureEm, ncos, nsin) {
      return xypic.Frame.Point(
        midPoint.x + 0.25 * curvatureEm * ncos,
        midPoint.y + 0.25 * curvatureEm * nsin
      );
    },
    toUpperCurveShape: function (context, s, cp, e, objectForDrop, objectForConnect) {
      this._toCurveShape(context, s, cp, e, objectForDrop, objectForConnect);
    },
    toLowerCurveShape: function (context, s, cp, e, objectForDrop, objectForConnect) {
      var shavedS = s.edgePoint(e.x, e.y);
      var shavedE = e.edgePoint(s.x, s.y);
      if (shavedS.x !== shavedE.x || shavedS.y !== shavedE.y) {
        context.env.lastCurve = xypic.LastCurve.Line(shavedS, shavedE, s, e, undefined);
      } else {
        context.env.lastCurve = xypic.LastCurve.none;
      }
    },
    getDefaultCurvature: function () { return 7 * AST.xypic.lineElementLength; },
    hasUpperTips: true,
    hasLowerTips: false
  });
  
  AST.Command.Twocell.LowerTwocell.Augment({
    getUpperControlPoint: function (s, e, midPoint, curvatureEm, ncos, nsin) {
      return midPoint;
    },
    getLowerControlPoint: function (s, e, midPoint, curvatureEm, ncos, nsin) {
      return xypic.Frame.Point(
        midPoint.x + curvatureEm * ncos,
        midPoint.y + curvatureEm * nsin
      );
    },
    getUpperLabelPosition: function (s, e, midPoint, curvatureEm, ncos, nsin) {
      return midPoint;
    },
    getLowerLabelPosition: function (s, e, midPoint, curvatureEm, ncos, nsin) {
      return xypic.Frame.Point(
        midPoint.x + 0.5 * curvatureEm * ncos,
        midPoint.y + 0.5 * curvatureEm * nsin
      );
    },
    getUpperLabelAngle: function (antiClockwiseAngle, s, e, midPoint, curvatureEm, ncos, nsin) {
      var rot = (curvatureEm < 0? 0 : Math.PI);
      return antiClockwiseAngle + rot;
    },
    getLowerLabelAngle: function (antiClockwiseAngle, s, e, midPoint, curvatureEm, ncos, nsin) {
      var rot = (curvatureEm < 0? Math.PI : 0);
      return antiClockwiseAngle + rot;
    },
    getDefaultArrowPoint: function (s, e, midPoint, curvatureEm, ncos, nsin) {
      return xypic.Frame.Point(
        midPoint.x + 0.25 * curvatureEm * ncos,
        midPoint.y + 0.25 * curvatureEm * nsin
      );
    },
    toUpperCurveShape: function (context, s, cp, e, objectForDrop, objectForConnect) {
      var shavedS = s.edgePoint(e.x, e.y);
      var shavedE = e.edgePoint(s.x, s.y);
      if (shavedS.x !== shavedE.x || shavedS.y !== shavedE.y) {
        context.env.lastCurve = xypic.LastCurve.Line(shavedS, shavedE, s, e, undefined);
      } else {
        context.env.lastCurve = xypic.LastCurve.none;
      }
    },
    toLowerCurveShape: function (context, s, cp, e, objectForDrop, objectForConnect) {
      this._toCurveShape(context, s, cp, e, objectForDrop, objectForConnect);
    },
    getDefaultCurvature: function () { return -7 * AST.xypic.lineElementLength; },
    hasUpperTips: false,
    hasLowerTips: true
  });
  
  AST.Command.Twocell.CompositeMap.Augment({
    getUpperControlPoint: function (s, e, midPoint, curvatureEm, ncos, nsin) {
      var midBoxSize = this.getMidBoxSize();
      return xypic.Frame.Ellipse(
        midPoint.x + curvatureEm * ncos,
        midPoint.y + curvatureEm * nsin,
        midBoxSize, midBoxSize, midBoxSize, midBoxSize
      );
    },
    getLowerControlPoint: function (s, e, midPoint, curvatureEm, ncos, nsin) {
      var midBoxSize = this.getMidBoxSize();
      return xypic.Frame.Ellipse(
        midPoint.x + curvatureEm * ncos,
        midPoint.y + curvatureEm * nsin,
        midBoxSize, midBoxSize, midBoxSize, midBoxSize
      );
    },
    getUpperLabelPosition: function (s, e, midPoint, curvatureEm, ncos, nsin) {
      var dx = midPoint.x + curvatureEm * ncos - e.x;
      var dy = midPoint.y + curvatureEm * nsin - e.y;
      var l = Math.sqrt(dx * dx + dy * dy);
      return xypic.Frame.Point(
        e.x + 0.5 * dx,
        e.y + 0.5 * dy
      );
    },
    getLowerLabelPosition: function (s, e, midPoint, curvatureEm, ncos, nsin) {
      var dx = midPoint.x + curvatureEm * ncos - s.x;
      var dy = midPoint.y + curvatureEm * nsin - s.y;
      var l = Math.sqrt(dx * dx + dy * dy);
      return xypic.Frame.Point(
        s.x + 0.5 * dx,
        s.y + 0.5 * dy
      );
    },
    getUpperLabelAngle: function (antiClockwiseAngle, s, e, midPoint, curvatureEm, ncos, nsin) {
      var dx = e.x - midPoint.x + curvatureEm * ncos;
      var dy = e.y - midPoint.y + curvatureEm * nsin;
      var angle = Math.atan2(dy, dx);
      var rot = (curvatureEm < 0? Math.PI : 0);
      return angle + Math.PI / 2 + rot;
    },
    getLowerLabelAngle: function (antiClockwiseAngle, s, e, midPoint, curvatureEm, ncos, nsin) {
      var dx = midPoint.x + curvatureEm * ncos - s.x;
      var dy = midPoint.y + curvatureEm * nsin - s.y;
      var angle = Math.atan2(dy, dx);
      var rot = (curvatureEm < 0? Math.PI : 0);
      return angle + Math.PI / 2 + rot;
    },
    getDefaultArrowPoint: function (s, e, midPoint, curvatureEm, ncos, nsin) {
      return midPoint;
    },
    toUpperCurveShape: function (context, s, cp, e, objectForDrop, objectForConnect) {
      var env = context.env;
      var start = s;
      var end = cp;
      var shavedS = start.edgePoint(end.x, end.y);
      var shavedE = end.edgePoint(start.x, start.y);
      var p = env.p;
      var c = env.c;
      env.p = start;
      env.c = end;
      xypic.Curve.Line(shavedS, shavedE).toShape(context, undefined, "-", "");
      env.p = p;
      env.c = c;
    },
    toLowerCurveShape: function (context, s, cp, e, objectForDrop, objectForConnect) {
      var env = context.env;
      var start = cp;
      var end = e;
      var shavedS = start.edgePoint(end.x, end.y);
      var shavedE = end.edgePoint(start.x, start.y);
      var p = env.p;
      var c = env.c;
      env.p = start;
      env.c = end;
      xypic.Curve.Line(shavedS, shavedE).toShape(context, undefined, "-", "");
      env.p = p;
      env.c = c;
    },
    getMidBoxSize: function () { return 0.5 * AST.xypic.lineElementLength; },
    getDefaultCurvature: function () { return 3.5 * AST.xypic.lineElementLength; },
    hasUpperTips: true,
    hasLowerTips: true
  });
  
  AST.Command.Twocell.Switch.UpperLabel.Augment({
    setup: function (context) {
      var env = context.env;
      env.twocellUpperLabel = FP.Option.Some(this);
    },
    toShape: function (context, curveMidPos, ncos, nsin, tangle) {
      this.label.toShape(context, curveMidPos, ncos, nsin, tangle);
    }
  });
  
  AST.Command.Twocell.Switch.LowerLabel.Augment({
    setup: function (context) {
      var env = context.env;
      env.twocellLowerLabel = FP.Option.Some(this);
    },
    toShape: function (context, curveMidPos, ncos, nsin, tangle) {
      this.label.toShape(context, curveMidPos, ncos, nsin, tangle);
    }
  });
  
  AST.Command.Twocell.Switch.SetCurvature.Augment({
    setup: function (context) {
      var env = context.env;
      if (this.nudge.isOmit) {
        env.twocellShouldDrawCurve = false;
      } else {
        env.twocellCurvatureEm = FP.Option.Some(this.nudge.number * AST.xypic.lineElementLength);
      }
    }
  });
  
  AST.Command.Twocell.Switch.DoNotSetCurvedArrows.Augment({
    setup: function (context) {
      var env = context.env;
      env.twocellShouldDrawCurve = false;
    }
  });
  
  AST.Command.Twocell.Switch.PlaceModMapObject.Augment({
    setup: function (context) {
      var env = context.env;
      env.twocellShouldDrawModMap = true;
    }
  });
  
  AST.Command.Twocell.Switch.ChangeHeadTailObject.Augment({
    setup: function (context) {
      var env = context.env;
      switch (this.what) {
        case '`':
          env.twocelltail = this.object;
          break;
        case "'":
          env.twocellhead = this.object;
          break;
      }
    }
  });
  
  AST.Command.Twocell.Switch.ChangeCurveObject.Augment({
    setup: function (context) {
      var env = context.env;
      switch (this.what) {
        case '':
          env.twocellUpperCurveObjectSpacer = this.spacer;
          env.twocellUpperCurveObject = this.maybeObject;
          env.twocellLowerCurveObjectSpacer = this.spacer;
          env.twocellLowerCurveObject = this.maybeObject;
          break;
        case '^':
          env.twocellUpperCurveObjectSpacer = this.spacer;
          env.twocellUpperCurveObject = this.maybeObject;
          break;
        case '_':
          env.twocellLowerCurveObjectSpacer = this.spacer;
          env.twocellLowerCurveObject = this.maybeObject;
          break;
      }
    }
  });
  
  AST.Command.Twocell.Label.Augment({
    toShape: function (context, curveMidPos, ncos, nsin, tangle) {
      var maybeNudge = this.maybeNudge;
      var offset;
      if (maybeNudge.isDefined) {
        var nudge = maybeNudge.get;
        if (nudge.isOmit) {
          return;
        } else {
          offset = nudge.number * AST.xypic.lineElementLength;
        }
      } else {
        offset = this.getDefaultLabelOffset();
      }
      
      var env = context.env;
      var c = env.c;
      env.c = xypic.Frame.Point(
        curveMidPos.x + offset * ncos,
        curveMidPos.y + offset * nsin
      );
      var labelObject = this.labelObject;
      labelObject.toDropShape(context);
      env.c = c;
      
    },
    getDefaultLabelOffset: function () { return AST.xypic.lineElementLength; }
  });
  
  AST.Command.Twocell.Nudge.Number.Augment({
    isOmit: false
  });
  
  AST.Command.Twocell.Nudge.Omit.Augment({
    isOmit: true
  });
  
  AST.Command.Twocell.Arrow.Augment({
    toTipsShape: function (context, reversed, doubleHeaded) {
      var env = context.env;
      var lastCurve = env.lastCurve;
      var c = env.c;
      var angle = env.angle;
      
      var rot = (reversed? Math.PI : 0);
      var t = lastCurve.tOfPlace(true, true, (reversed? 0 : 1), 0);
      env.c = lastCurve.position(t);
      env.angle = lastCurve.angle(t) + rot;
      env.twocellhead.toDropShape(context);
      
      var t = lastCurve.tOfPlace(true, true, (reversed? 1 : 0), 0);
      env.c = lastCurve.position(t);
      env.angle = lastCurve.angle(t) + rot;
      if (doubleHeaded) {
        env.twocellhead.toDropShape(context);
      } else {
        env.twocelltail.toDropShape(context);
      }
      
      if (env.twocellShouldDrawModMap) {
        var t = lastCurve.tOfPlace(false, false, 0.5, 0);
        env.c = lastCurve.position(t);
        env.angle = lastCurve.angle(t) + rot;
        env.twocellmodmapobject.toDropShape(context);
      }
      
      env.c = c;
      env.angle = angle;
    }
  });
  
  AST.Command.Twocell.Arrow.WithOrientation.Augment({
    toUpperTipsShape: function (context) {
      switch (this.tok) {
        case '':
        case '^':
        case '_':
        case '=':
        case '\\omit':
        case "'":
          this.toTipsShape(context, false, false);
          break;
        case '`':
          this.toTipsShape(context, true, false);
          break;
        case '"':
          this.toTipsShape(context, false, true);
          break;
        case '!':
          break;
      }
    },
    toLowerTipsShape: function (context) {
      switch (this.tok) {
        case '':
        case '^':
        case '_':
        case '=':
        case '\\omit':
        case '`':
          this.toTipsShape(context, false, false);
          break;
        case "'":
          this.toTipsShape(context, true, false);
          break;
        case '"':
          this.toTipsShape(context, false, true);
          break;
        case '!':
          break;
      }
    },
    toArrowShape: function(context, labelOrigin) {
      var env = context.env;
      var c = env.c;
      switch (this.tok) {
        case '^':
          var angle = env.angle;
          env.angle = angle + Math.PI;
          env.twocellarrowobject.toDropShape(context);
          env.c = xypic.Frame.Point(
            c.x + AST.xypic.lineElementLength * Math.cos(angle - Math.PI / 2),
            c.y + AST.xypic.lineElementLength * Math.sin(angle - Math.PI / 2)
          );
          this.labelObject.toDropShape(context);
          env.angle = angle;
          break;
        case '':
        case '_':
          var angle = env.angle;
          env.twocellarrowobject.toDropShape(context);
          env.c = xypic.Frame.Point(
            c.x + AST.xypic.lineElementLength * Math.cos(angle + Math.PI / 2),
            c.y + AST.xypic.lineElementLength * Math.sin(angle + Math.PI / 2)
          );
          this.labelObject.toDropShape(context);
          break;
        case '=':
          var angle = env.angle;
          var shape = xypic.Shape.TwocellEqualityArrowheadShape(env.c, env.angle);
          context.appendShapeToFront(shape);
          env.c = xypic.Frame.Point(
            c.x + AST.xypic.lineElementLength * Math.cos(angle + Math.PI / 2),
            c.y + AST.xypic.lineElementLength * Math.sin(angle + Math.PI / 2)
          );
          this.labelObject.toDropShape(context);
          break;
        default:
          this.labelObject.toDropShape(context);
          break;
      }
      env.c = c;
    }
  });
  
  AST.Command.Twocell.Arrow.WithPosition.Augment({
    toUpperTipsShape: function (context) {
      this.toTipsShape(context, false, false);
    },
    toLowerTipsShape: function (context) {
      this.toTipsShape(context, false, false);
    },
    toArrowShape: function(context, labelOrigin) {
      var env = context.env;
      var c = env.c;
      var angle = env.angle;
      var arrowPos;
      var nudge = this.nudge;
      if (nudge.isOmit) {
        arrowPos = c;
      } else {
        var offset = nudge.number * AST.xypic.lineElementLength;
        arrowPos = xypic.Frame.Point(
          labelOrigin.x + offset * Math.cos(angle),
          labelOrigin.y + offset * Math.sin(angle)
        );
      }
      
      env.c = arrowPos;
      env.twocellarrowobject.toDropShape(context);
      if (!nudge.isOmit) {
        env.c = xypic.Frame.Point(
          arrowPos.x + AST.xypic.lineElementLength * Math.cos(angle + Math.PI / 2),
          arrowPos.y + AST.xypic.lineElementLength * Math.sin(angle + Math.PI / 2)
        );
        this.labelObject.toDropShape(context);
      }
      env.c = c;
    }
  });
  
  AST.Pos.Xyimport.TeXCommand.Augment({
    toShape: function (context) {
      var origEnv = context.env;
      if (origEnv.c === undefined) {
        return xypic.Shape.none;
      }
      
      var subEnv = origEnv.duplicate();
      var subcontext = xypic.DrawingContext(xypic.Shape.none, subEnv);
      var shape = this.graphics.toDropShape(subcontext);
      
      var xyWidth = this.width;
      var xyHeight = this.height;
      if (xyWidth === 0 || xyHeight === 0) {
        throw xypic.ExecutionError("the 'width' and 'height' attributes of the \\xyimport should be non-zero.");
      }
      
      var c = subEnv.c;
      var imageWidth = c.l + c.r;
      var imageHeight = c.u + c.d;
      
      if (imageWidth === 0 || imageHeight === 0) {
        throw xypic.ExecutionError("the width and height of the graphics to import should be non-zero.");
      }
      
      var xOffset = this.xOffset;
      var yOffset = this.yOffset;
      
      origEnv.c = c.toRect({
        u:imageHeight / xyHeight * (xyHeight - yOffset),
        d:imageHeight / xyHeight * yOffset,
        l:imageWidth / xyWidth * xOffset,
        r:imageWidth / xyWidth * (xyWidth - xOffset)
      });
      
      origEnv.setXBase(imageWidth / xyWidth, 0);
      origEnv.setYBase(0, imageHeight / xyHeight);
      
      var dx = c.l - origEnv.c.l;
      var dy = c.d - origEnv.c.d;
      var shape = xypic.Shape.TranslateShape(dx, dy, subcontext.shape);
      context.appendShapeToFront(shape);
    }
  });
  
  AST.Pos.Xyimport.Graphics.Augment({
    toShape: function (context) {
      var origEnv = context.env;
      if (origEnv.c === undefined) {
        return xypic.Shape.none;
      }
      
      var subEnv = origEnv.duplicate();
      var subcontext = xypic.DrawingContext(xypic.Shape.none, subEnv);
      
      var xyWidth = this.width;
      var xyHeight = this.height;
      if (xyWidth === 0 || xyHeight === 0) {
        throw xypic.ExecutionError("the 'width' and 'height' attributes of the \\xyimport should be non-zero.");
      }
      
      var graphics = this.graphics;
      graphics.setup(subcontext);
      if (!subEnv.includegraphicsWidth.isDefined || !subEnv.includegraphicsHeight.isDefined) {
        throw xypic.ExecutionError("the 'width' and 'height' attributes of the \\includegraphics are required.");
      }
      var imageWidth = subEnv.includegraphicsWidth.get;
      var imageHeight = subEnv.includegraphicsHeight.get;
      
      if (imageWidth === 0 || imageHeight === 0) {
        throw xypic.ExecutionError("the 'width' and 'height' attributes of the \\includegraphics should be non-zero.");
      }
      
      var xOffset = this.xOffset;
      var yOffset = this.yOffset;
      
      origEnv.c = subEnv.c.toRect({
        u:imageHeight / xyHeight * (xyHeight - yOffset),
        d:imageHeight / xyHeight * yOffset,
        l:imageWidth / xyWidth * xOffset,
        r:imageWidth / xyWidth * (xyWidth - xOffset)
      });
      
      origEnv.setXBase(imageWidth / xyWidth, 0);
      origEnv.setYBase(0, imageHeight / xyHeight);
      
      var imageShape = xypic.Shape.ImageShape(origEnv.c, graphics.filepath);
      context.appendShapeToFront(imageShape);
    }
  });
  
  AST.Command.Includegraphics.Augment({
    setup: function (context) {
      var env = context.env;
      env.includegraphicsWidth = FP.Option.empty;
      env.includegraphicsHeight = FP.Option.empty;
      
      this.attributeList.foreach(function (attr) {
        attr.setup(context);
      });
    }
  });
  
  AST.Command.Includegraphics.Attr.Width.Augment({
    setup: function (context) {
      var env = context.env;
      env.includegraphicsWidth = FP.Option.Some(xypic.length2em(this.dimen));
    }
  });
  
  AST.Command.Includegraphics.Attr.Height.Augment({
    setup: function (context) {
      var env = context.env;
      env.includegraphicsHeight = FP.Option.Some(xypic.length2em(this.dimen));
    }
  });
  
  MathJax.Hub.Startup.signal.Post("Device-Independent Xy-pic Ready");
});


MathJax.Hub.Register.StartupHook("HTML-CSS Xy-pic Require",function () {
  var FP = MathJax.Extension.fp;
  var MML = MathJax.ElementJax.mml;
  var HTMLCSS = MathJax.OutputJax["HTML-CSS"];
  var HUB = MathJax.Hub;
  var xypic = MathJax.Extension.xypic;
  var AST = xypic.AST;
  
  var SVGNS = "http://www.w3.org/2000/svg";
  var XHTMLNS = "http://www.w3.org/1999/xhtml";
  var XLINKNS = "http://www.w3.org/1999/xlink";
  
  var setupHTMLCSSMeasure = function () {
    xypic.length2em = function (len) { return HTMLCSS.length2em(len); }
    xypic.oneem = xypic.length2em("1em");
    xypic.em2length = function (len) { return (len / xypic.oneem) + "em"; }
    xypic.Em = function (x) { return HTMLCSS.Em(x); }
    xypic.em = HTMLCSS.em;
    xypic.em2px = function (n) { return Math.round(n * HTMLCSS.em * 100) / 100; }
    xypic.axis_height = HTMLCSS.TeX.axis_height;
    
    AST.xypic.strokeWidth = xypic.length2em("0.04em");
    AST.xypic.thickness = xypic.length2em("0.15em");
    AST.xypic.jot = xypic.length2em("3pt");
    AST.xypic.objectmargin = xypic.length2em("3pt");
    AST.xypic.objectwidth = xypic.length2em("0pt");
    AST.xypic.objectheight = xypic.length2em("0pt");
    AST.xypic.labelmargin = xypic.length2em("2.5pt");
    AST.xypic.turnradius = xypic.length2em("10pt");
    AST.xypic.lineElementLength = xypic.length2em("5pt");
    AST.xypic.axisHeightLength = xypic.axis_height * xypic.length2em("10pt");
    
    AST.xypic.dottedDasharray = "" + xypic.oneem + " " + xypic.em2px(AST.xypic.thickness);
  };
  
  AST.xypic.Augment({
    toHTML: function (span) {
      if (!xypic.useSVG) {
        return span;
      }
      
      setupHTMLCSSMeasure();
      
      // HTML-CSS Text Objects
      var textObjects = [];
      
      var p = xypic.length2em("0.2em");
      var t = AST.xypic.strokeWidth;
      
      span = this.HTMLcreateSpan(span);
      var svgStack = HTMLCSS.createStack(span);
      
      xypic.Shape.TextShape.Augment({
        _draw: function (svg, test) {
          var math = this.math;
          var span, stack, base;
          math.setTeXclass();
          
          // padding
          var p = xypic.length2em("0.1em");
          var mathSpan = HTMLCSS.Element("span", {
            className:"MathJax", 
            style:{ "text-align":"center", "role":"textbox", "aria-readonly":"true", "position":"absolute", color:svg.getCurrentColor() /*, "border":"0.1px dashed" */ }
          });
          
          svgStack.appendChild(mathSpan);
          
          // clear spanID for connecting objects.
          var clearSpanId = function (mml) {
            if (mml) {
              if (mml.hasOwnProperty("spanID")) { delete mml.spanID; }
              if (mml.data) {
                for (var i = 0, n = mml.data.length; i < n; i++) {
                  clearSpanId(mml.data[i]);
                }
              }
            }
          }
          
          clearSpanId(math);
          var span = math.HTMLcreateSpan(mathSpan);
          stack = HTMLCSS.createStack(span);
          base = HTMLCSS.createBox(stack);
          math.HTMLmeasureChild(0, base);
          var H = base.bbox.h + p, D = base.bbox.d + p, W = base.bbox.w + 2 * p;
          var frame = HTMLCSS.createFrame(stack, H + D, 0, W, 0, "none");
          frame.id = "MathJax-frame-" + math.spanID + HTMLCSS.idPostfix;
    //      stack.style.border = "solid 0.1px pink";
    //      base.style.border = "solid 0.1px pink";
    //      frame.style.border = "solid 0.1px pink";
          HTMLCSS.addBox(stack, frame);
          stack.insertBefore(frame, base);
          frame.style.width = xypic.em2px(W);
          frame.style.height = xypic.em2px(H + D);
          HTMLCSS.placeBox(frame, 0, -D, true);
          HTMLCSS.placeBox(base, p, 0);
          math.HTMLhandleSpace(span);
          math.HTMLhandleColor(span);
          
          var spanHeight = span.offsetHeight;
          var halfHD = (H + D) / 2;
          var halfW = W / 2;
          
          var c = this.c;
          this.originalBBox = { H:H, D:D, W:W };
          
          if (!test) {
            var origin = svg.getOrigin();
            mathSpan.setAttribute("x", c.x - halfW - origin.x);
            mathSpan.setAttribute("y", -c.y - halfHD - origin.y - stack.offsetTop / HTMLCSS.em + H);
            textObjects.push(mathSpan);
            
    /*        
            svg.createSVGElement("rect", {
              x:xypic.em2px(c.x - halfW),
              y:-xypic.em2px(c.y - (H - D) / 2),
              width:xypic.em2px(W),
              height:0.1,
              stroke:"green", "stroke-width":0.3
            });
            
            console.log("span.top:" + span.offsetTop + ", " + (span.offsetTop / HTMLCSS.em) + "em");
            console.log("span.height:" + span.offsetHeight + ", " + (span.offsetHeight / HTMLCSS.em) + "em");
            console.log("stack.top:" + stack.offsetTop + ", " + (stack.offsetTop / HTMLCSS.em) + "em");
            console.log("stack.height:" + stack.offsetHeight + ", " + (stack.offsetHeight / HTMLCSS.em) + "em");
            console.log("frame.top:" + frame.offsetTop + ", " + (frame.offsetTop / HTMLCSS.em) + "em");
            console.log("frame.height:" + frame.offsetHeight + ", " + (frame.offsetHeight / HTMLCSS.em) + "em");
            console.log("base.top:" + base.offsetTop + ", " + (base.offsetTop / HTMLCSS.em) + "em");
            console.log("base.height:" + base.offsetHeight + ", " + (base.offsetHeight / HTMLCSS.em) + "em");
            console.log("p:" + xypic.em2px(p) + ", " + p + "em");
            console.log("D:" + xypic.em2px(D) + ", " + D + "em");
            console.log("H:" + xypic.em2px(H) + ", " + H + "em");
            console.log("d:" + xypic.em2px(base.bbox.d) + ", " + base.bbox.d + "em");
            console.log("h:" + xypic.em2px(base.bbox.h) + ", " + base.bbox.h + "em");
            
            svg.createSVGElement("rect", {
              x:xypic.em2px(c.x - halfW),
              y:-xypic.em2px(c.y + halfHD),
              width:xypic.em2px(W),
              height:xypic.em2px(H + D),
              stroke:"green", "stroke-width":0.5
            });
         */
          } else {
            svgStack.removeChild(mathSpan);
          }
          
          return c.toRect({ u:halfHD, d:halfHD, l:halfW, r:halfW });
        }
      });
      
      var bbox = { h:1, d:0, w:1, lw:0, rw:1 };
      var H = bbox.h, D = bbox.d, W = bbox.w;
      var frame = HTMLCSS.createFrame(svgStack, H + D, 0, W, t, "none");
      frame.id = "MathJax-frame-" + this.spanID + HTMLCSS.idPostfix;
      
      var svg;
      var color = "black";
      svg = xypic.Graphics.createSVG(H, D, W, t, color, {
        viewBox:[0, -xypic.em2px(H + D), xypic.em2px(W), xypic.em2px(H + D)].join(" "),
        overflow:"visible"
      });
      xypic.svgForDebug = svg;
      xypic.svgForTestLayout = svg;
      var scale = HTMLCSS.createBox(svgStack);
      scale.appendChild(svg.svg);
      
      var xypicData = this.cmd;
      if (xypicData) {
        var env = xypic.Env();
        
        var context = xypic.DrawingContext(xypic.Shape.none, env);
        xypicData.toShape(context);
        var shape = context.shape;
        shape.draw(svg);
        
        var box = shape.getBoundingBox();
        if (box !== undefined) {
          box = xypic.Frame.Rect(
            0, 0,
            {
              l:Math.max(0, -(box.x - box.l)),
              r:Math.max(0, box.x + box.r),
              u:Math.max(0, box.y + box.u),
              d:Math.max(0, -(box.y - box.d))
            }
          );
          
          svg.setWidth(box.l + box.r + 2 * p);
          svg.setHeight(box.u + box.d + 2 * p);
          svg.setAttribute("viewBox", [ xypic.em2px(box.x - box.l - p), -xypic.em2px(box.y + box.u + p), xypic.em2px(box.l + box.r + 2 * p), xypic.em2px(box.u + box.d + 2 * p) ].join(" "));
          var c = textObjects.length;
          for (var i = 0; i < c; i++) {
            var to = textObjects[i];
            var x = parseFloat(to.getAttribute("x"));
            var y = parseFloat(to.getAttribute("y"));
            
            to.style.left = "" + xypic.em2px(x + box.l + p * xypic.oneem) + "px";
            to.style.top = "" + xypic.em2px(y - xypic.axis_height) + "px";
          }
          
          bbox = { h:(box.u + p), d:(box.d + p), w:(box.l + box.r + 2 * p), lw:0, rw:(box.l + box.r + 2 * p)}
          span.bbox = bbox;
          D = box.d + p;
          W = box.l + box.r + 2 * p;
          H = box.h + p;
          
          HTMLCSS.placeBox(scale, 0, xypic.axis_height - D, true);
          frame.style.width = xypic.Em(W);
          frame.style.height = xypic.Em(H + D);
          HTMLCSS.addBox(svgStack, frame); 
          HTMLCSS.placeBox(frame, W - 1, -D, true);
          this.HTMLhandleSpace(span);
          this.HTMLhandleColor(span);
        } else {
          // there is no contents
          span = span.parentNode;
          span.removeChild(span.firstChild);
        }
      } else {
        // there is no contents
        span = span.parentNode;
        span.removeChild(span.firstChild);
      }
      
      return span;
    }
  });
  
  AST.xypic.newdir.Augment({
    toHTML: function (span) {
      var newdir = this.cmd;
      xypic.repositories.dirRepository.put(newdir.dirMain, newdir.compositeObject);
      return span;
    }
  });
  
  AST.xypic.includegraphics.Augment({
    toHTML: function (span) {
      setupHTMLCSSMeasure();
      
      var graphics = this.cmd;
      
      var env = xypic.Env();
      var context = xypic.DrawingContext(xypic.Shape.none, env);
      
      graphics.setup(context);
      if (!env.includegraphicsWidth.isDefined || !env.includegraphicsHeight.isDefined) {
        throw xypic.ExecutionError("the 'width' and 'height' attributes of the \\includegraphics are required.");
      }
      
      var imageWidth = env.includegraphicsWidth.get;
      var imageHeight = env.includegraphicsHeight.get;
      
      span = this.HTMLcreateSpan(span);
      var stack = HTMLCSS.createStack(span);
      var base = HTMLCSS.createBox(stack);
      
      var img = new Image();
      img.src = graphics.filepath;
      img.style.width = HTMLCSS.Em(imageWidth);
      img.style.height = HTMLCSS.Em(imageHeight);
      base.appendChild(img);
      
      var bbox = {h:imageHeight, d:0, w:imageWidth, rw:imageWidth, lw:0, exactW:true};
      img.bbox = bbox;
      var H = imageHeight, D = 0, W = imageWidth;
      
      HTMLCSS.Measured(img);
      
      var frame = HTMLCSS.createFrame(stack, H+D, 0, W, 0, "none");
      frame.id = "MathJax-frame-" + this.spanID;
      HTMLCSS.addBox(stack, frame);
      stack.insertBefore(frame, base);
      var T = 0, B = 0, R = 0, L = 0, dx = 0, dy = 0;
      frame.style.width = HTMLCSS.Em(W-L-R);
      frame.style.height = HTMLCSS.Em(H+D-T-B);
      HTMLCSS.placeBox(frame, 0, dy-D, true);
      HTMLCSS.placeBox(base, dx, 0);
      this.HTMLhandleSpace(span);
      this.HTMLhandleColor(span);
      
      return span;
    }
  });
  
  MathJax.Hub.Startup.signal.Post("HTML-CSS Xy-pic Ready");
});


MathJax.Hub.Register.StartupHook("SVG Xy-pic Require",function () {
  var FP = MathJax.Extension.fp;
  var MML = MathJax.ElementJax.mml;
  var SVG = MathJax.OutputJax.SVG;
  var BBOX = SVG.BBOX;
  var HUB = MathJax.Hub;
  var xypic = MathJax.Extension.xypic;
  var AST = xypic.AST;
  
  var SVGNS = "http://www.w3.org/2000/svg";
  var XHTMLNS = "http://www.w3.org/1999/xhtml";
  var XLINKNS = "http://www.w3.org/1999/xlink";
  
  var memoize = xypic.memoize;
  
  BBOX.PPATH = BBOX.Subclass({
    type: "path", removeable: false,
    Init: function (h,d,w,p,t,color,def) {
      if (def == null) {def = {}}; def.fill = "none";
      if (color) {def.stroke = color}
      def["stroke-width"] = t.toFixed(2).replace(/\.?0+$/,"");
      def.d = p;
      this.SUPER(arguments).Init.call(this,def);
      this.w = this.r = w; this.h = this.H = h+d;
      this.d = this.D = this.l = 0; this.y = -d;
    }
  });
  
  BBOX.XYPIC = BBOX.Subclass({
    type: "g", removeable: false,
    Init: function (bbox, x, y, svg) {
      this.element = svg;
      
      this.x = x;
      this.y = y;
      this.r = bbox.r;
      this.l = bbox.l;
      this.h = bbox.h;
      this.d = bbox.d;
      this.w = bbox.w;
      this.H = bbox.h;
      this.D = bbox.d;
      
      this.scale = 1;
      this.n = 1;
    }
  });
  
  var setupSVGMeasure = function (mu, scale) {
    xypic.length2em = function (len) { return SVG.length2em(len, mu, 1/SVG.em) * scale; }
    xypic.oneem = xypic.length2em("1em");
    xypic.em2length = function (len) { return (len / xypic.oneem) + "em"; }
    
    xypic.Em = function (x) { return SVG.Em(x); }
    xypic.em = SVG.em;
    xypic.em2px = function (n) { return Math.round(n * SVG.em * 100) / 100; }
    xypic.axis_height = SVG.TeX.axis_height;
    
    AST.xypic.strokeWidth = xypic.length2em("0.04em");
    AST.xypic.thickness = xypic.length2em("0.15em");
    AST.xypic.jot = xypic.length2em("3pt");
    AST.xypic.objectmargin = xypic.length2em("3pt");
    AST.xypic.objectwidth = xypic.length2em("0pt");
    AST.xypic.objectheight = xypic.length2em("0pt");
    AST.xypic.labelmargin = xypic.length2em("2.5pt");
    AST.xypic.turnradius = xypic.length2em("10pt");
    AST.xypic.lineElementLength = xypic.length2em("5pt");
    AST.xypic.axisHeightLength = xypic.axis_height * xypic.length2em("1em") / 1000;
    
    AST.xypic.dottedDasharray = "" + xypic.oneem + " " + xypic.em2px(AST.xypic.thickness);
  };
  
  AST.xypic.Augment({
    toSVG: function (HW, DD) {
      this.SVGgetStyles();
      
      var svg = this.SVG();
      this.SVGhandleSpace(svg);
      
      var mu = this.SVGgetMu(svg);
      var scale = this.SVGgetScale();
      setupSVGMeasure(mu, scale);
      
      var p = xypic.length2em("0.2em");
      var t = AST.xypic.strokeWidth;
      
      var jaxSVG = svg;
      
      xypic.Shape.TextShape.Augment({
        _draw: function (svg, test) {
          var math = this.math;
          
          // padding
          var p = xypic.length2em("0.1em");
          var c = this.c;
          
          math.setTeXclass();
          math.SVGgetStyles();
          
          math.SVGhandleSpace(jaxSVG);
          var box = math.data[0].toSVG();
          var x = c.x - box.w / 2;
          var y = c.y - (box.h + box.d) / 2 + box.d + xypic.axis_height;
          var H = box.h + p;
          var D = box.d + p;
          var W = box.w + 2 * p;
          this.originalBBox = { H:H, D:D, W:W };
          var halfHD = (H + D) / 2;
          var halfW = W / 2;
          
          if (!test) {
            var origin = svg.getOrigin();
            var color = svg.getCurrentColor();
            var localSVG = BBOX.G({ stroke:color, fill:color, "stroke-thickness":0, transform:"scale(" + SVG.em + ") matrix(1 0 0 -1 0 0) translate(" + xypic.em2px(x / SVG.em) + ", " + xypic.em2px((c.y - (H - D) / 2) / SVG.em) + ")" }).With({removeable: false});
            localSVG.Add(box, 0, 0, true, true);
            localSVG.ic = box.ic;
            localSVG.Clean();
            math.SVGhandleColor(localSVG);
            math.SVGsaveData(localSVG);
            
            svg.appendChild(localSVG.element);
          }
          
          return c.toRect({ u:halfHD, d:halfHD, l:halfW, r:halfW });
        }
      });
      
      var bbox = { h:xypic.oneem, d:0, w:xypic.oneem, lw:0, rw:xypic.oneem };
      var H = bbox.h, D = bbox.d, W = bbox.w;
      var color = "black";
      var xypicSVG = xypic.Graphics.createSVG(H, D, W, t, color, {
        viewBox:[0, -xypic.em2px(H + D), xypic.em2px(W), xypic.em2px(H + D)].join(" "),
        overflow:"visible"
      });
      xypic.svgForDebug = xypicSVG;
      xypic.svgForTestLayout = xypicSVG;
      
      var xypicData = this.cmd;
      if (xypicData) {
        var env = xypic.Env();
        
        var context = xypic.DrawingContext(xypic.Shape.none, env);
        xypicData.toShape(context);
        var shape = context.shape;
        shape.draw(xypicSVG);
        
        var shapeBBox = shape.getBoundingBox();
        if (shapeBBox !== undefined) {
          var box = xypic.Frame.Rect(
            0, 0,
            {
              l:Math.max(0, -(shapeBBox.x - shapeBBox.l)),
              r:Math.max(0, shapeBBox.x + shapeBBox.r),
              u:Math.max(0, shapeBBox.y + shapeBBox.u),
              d:Math.max(0, -(shapeBBox.y - shapeBBox.d))
            }
          );
          bbox = { h:(box.u + p + xypic.axis_height), d:(box.d + p - xypic.axis_height), w:(box.r + box.l + 2*p), l:(- box.l - p), r:(box.r + p)}
          
          this.SVGhandleSpace(svg);
          var xypicBBOX = BBOX.XYPIC(bbox, 0, 0, xypicSVG.drawArea);
          xypicBBOX.element.setAttribute("transform", "scale(" + (1 / SVG.em) + ") matrix(1 0 0 -1 0 0) translate(0," + xypic.em2px(- xypic.axis_height) + ")");
          svg.Add(xypicBBOX);
          
          
          // FIXME
          svg.x += box.l + p;
          svg.w -= box.l + p;
          
          
          this.SVGhandleColor(svg);
          this.SVGsaveData(svg);
        }
      }
      
      return svg;
    }
  });
  
  AST.xypic.newdir.Augment({
    toSVG: function () {
      var newdir = this.cmd;
      xypic.repositories.dirRepository.put(newdir.dirMain, newdir.compositeObject);
      return this.SVG();
    }
  });
  
  AST.xypic.includegraphics.Augment({
    toSVG: function (HW, DD) {
      this.SVGgetStyles();
      
      var svg = this.SVG();
      this.SVGhandleSpace(svg);
      
      var mu = this.SVGgetMu(svg);
      var scale = this.SVGgetScale();
      setupSVGMeasure(mu, scale);
      var t = AST.xypic.strokeWidth;
      
      var bbox = { h:xypic.oneem, d:0, w:xypic.oneem, lw:0, rw:xypic.oneem };
      var H = bbox.h, D = bbox.d, W = bbox.w;
      var color = "black";
      var xypicSVG = xypic.Graphics.createSVG(H, D, W, t, color, {
        viewBox:[0, -xypic.em2px(H + D), xypic.em2px(W), xypic.em2px(H + D)].join(" "),
        overflow:"visible"
      });
      xypic.svgForDebug = xypicSVG;
      xypic.svgForTestLayout = xypicSVG;
      
      var env = xypic.Env();
      var context = xypic.DrawingContext(xypic.Shape.none, env);
      
      var graphics = this.cmd;
      graphics.setup(context);
      if (!env.includegraphicsWidth.isDefined || !env.includegraphicsHeight.isDefined) {
        throw xypic.ExecutionError("the 'width' and 'height' attributes of the \\includegraphics are required.");
      }
      var imageWidth = env.includegraphicsWidth.get;
      var imageHeight = env.includegraphicsHeight.get;
      
      var c = env.c;
      c = c.toRect({ u:imageHeight - xypic.axis_height, d:xypic.axis_height, l:0, r:imageWidth });
      var imageShape = xypic.Shape.ImageShape(c, graphics.filepath);
      imageShape.draw(xypicSVG);
      
      var shapeBBox = imageShape.getBoundingBox();
      var box = xypic.Frame.Rect(
        0, 0,
        {
          l:Math.max(0, -(shapeBBox.x - shapeBBox.l)),
          r:Math.max(0, shapeBBox.x + shapeBBox.r),
          u:Math.max(0, shapeBBox.y + shapeBBox.u),
          d:Math.max(0, -(shapeBBox.y - shapeBBox.d))
        }
      );
      
      var bbox = { h:(box.u + xypic.axis_height), d:(box.d - xypic.axis_height), w:(box.r + box.l), l:(- box.l), r:(box.r)}
      
      this.SVGhandleSpace(svg);
      var xypicBBOX = BBOX.XYPIC(bbox, 0, 0, xypicSVG.drawArea);
      xypicBBOX.element.setAttribute("transform", "scale(" + (1 / SVG.em) + ") matrix(1 0 0 -1 0 0) translate(0," + xypic.em2px(- xypic.axis_height) + ")");
      svg.Add(xypicBBOX);
      svg.x += box.l;
      svg.w -= box.l;
      this.SVGhandleColor(svg);
      this.SVGsaveData(svg);
      
      return svg;
    }
  });
  
  MathJax.Hub.Startup.signal.Post("SVG Xy-pic Ready");
});

MathJax.Ajax.loadComplete("[MathJax]/extensions/TeX/xypic.js");