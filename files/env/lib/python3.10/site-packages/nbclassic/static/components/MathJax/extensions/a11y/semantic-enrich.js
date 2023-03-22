MathJax.Extension["semantic-enrich"] = {
    version: "1.6.0",
    config: MathJax.Hub.CombineConfig("semantic-enrich", {
        disabled: !1
    }),
    dependents: [],
    running: !1,
    mstyleLookup: {
        mi: [ "mathvariant" ],
        mo: [ "mathvariant", "accent", "largeop", "form", "fence", "separator", "movablelimits" ],
        mn: [ "mathvariant" ],
        mtext: [ "mathvariant" ],
        ms: [ "mathvariant" ],
        mfrac: [ "linethickness" ],
        mfenced: [ "open", "close", "separators" ],
        menclose: [ "notation" ],
        munder: [ "accentunder" ],
        mover: [ "accent" ],
        munderover: [ "accent", "accentunder" ]
    },
    Filter: function(t, a, e) {
        if (delete t.enriched, !this.config.disabled) try {
            this.running = !0;
            var n = sre.Enrich.semanticMathmlSync(t.root.toMathML());
            t.root = MathJax.InputJax.MathML.Parse.prototype.MakeMML(n), t.root.inputID = e.id, 
            t.enriched = !0, this.running = !1;
        } catch (t) {
            throw this.running = !1, t;
        }
    },
    Enable: function(t, a) {
        this.config.disabled = !1, t && MathJax.Hub.Queue([ "Reprocess", MathJax.Hub ]);
    },
    Disable: function(t, a) {
        this.config.disabled = !0;
        for (var e = this.dependents.length - 1; 0 <= e; e--) {
            var n = this.dependents[e];
            n.Disable && n.Disable(!1, a);
        }
        t && MathJax.Hub.Queue([ "Reprocess", MathJax.Hub ]);
    },
    Dependent: function(t) {
        this.dependents.push(t);
    }
}, function() {
    var t = MathJax.Ajax.config.path;
    t.a11y || (t.a11y = HUB.config.root + "/extensions/a11y"), t.SRE || (t.SRE = MathJax.Ajax.fileURL(t.a11y)), 
    MathJax.Ajax.Load("[SRE]/mathjax-sre.js"), MathJax.Hub.Register.StartupHook("Sre Ready", [ "loadComplete", MathJax.Ajax, "[SRE]/mathjax-sre.js" ]);
}(), MathJax.Callback.Queue([ "Require", MathJax.Ajax, "[MathJax]/jax/element/mml/jax.js" ], [ "Require", MathJax.Ajax, "[MathJax]/jax/input/MathML/config.js" ], [ "Require", MathJax.Ajax, "[MathJax]/jax/input/MathML/jax.js" ], [ "Require", MathJax.Ajax, "[MathJax]/extensions/toMathML.js" ], MathJax.Hub.Register.StartupHook("Sre Ready", function() {
    var l = MathJax.ElementJax.mml, c = MathJax.Extension["semantic-enrich"];
    l.mbase.Augment({
        toMathMLattributes: function() {
            var t = "mstyle" === this.type ? l.math.prototype.defaults : this.defaults, a = this.attrNames || l.copyAttributeNames, e = l.skipAttributes, n = l.copyAttributes, s = c.running && c.mstyleLookup[this.type] || [], i = [], h = this.attr || {};
            if ("math" !== this.type || this.attr && "xmlns" in this.attr || i.push('xmlns="http://www.w3.org/1998/Math/MathML"'), 
            !this.attrNames) for (var r in t) e[r] || n[r] || !t.hasOwnProperty(r) || null != this[r] && this[r] !== t[r] && this.Get(r, null, 1) !== this[r] && this.toMathMLaddAttr(i, r, this[r]);
            for (var o = 0, u = a.length; o < u; o++) 1 === n[a[o]] && !t.hasOwnProperty(a[o]) || (value = h[a[o]], 
            null == value && (value = this[a[o]]), null != value && this.toMathMLaddAttr(i, a[o], value));
            for (o = 0, u = s.length; o < u; o++) r = s[o], t.hasOwnProperty(r) && !i["_" + r] && (value = this.Get(r, 1), 
            null != value && this.toMathMLaddAttr(i, r, value));
            return this.toMathMLclass(i), i.length ? " " + i.join(" ") : "";
        },
        toMathMLaddAttr: function(t, a, e) {
            t.push(a + '="' + this.toMathMLquote(e) + '"'), t["_" + a] = 1;
        }
    });
    var a = l.mo.prototype.setTeXclass;
    l.mo.Augment({
        setTeXclass: function(t) {
            this.getValues("form", "lspace", "rspace");
            return this.useMMLspacing ? (this.texClass = l.TEXCLASS.NONE, this) : this.attr && this.attr["data-semantic-added"] ? (this.texClass = this.prevClass = l.TEXCLASS.NONE, 
            t) : a.apply(this, arguments);
        }
    });
}), function() {
    MathJax.Hub.postInputHooks.Add([ "Filter", MathJax.Extension["semantic-enrich"] ], 50), 
    MathJax.Hub.Startup.signal.Post("Semantic Enrich Ready"), MathJax.Ajax.loadComplete("[a11y]/semantic-enrich.js");
});