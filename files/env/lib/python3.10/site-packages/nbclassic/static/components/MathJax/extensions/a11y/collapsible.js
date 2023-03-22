!function(s) {
    var n, l = s.config.menuSettings, o = {}, r = "data-semantic-complexity", t = MathJax.Ajax.config.path;
    t.a11y || (t.a11y = s.config.root + "/extensions/a11y");
    var h = MathJax.Extension.collapsible = {
        version: "1.6.0",
        config: s.CombineConfig("collapsible", {
            disabled: !1
        }),
        dependents: [],
        COMPLEXATTR: r,
        COMPLEXITY: {
            TEXT: .5,
            TOKEN: .5,
            CHILD: 1,
            SCRIPT: .8,
            SQRT: 2,
            SUBSUP: 2,
            UNDEROVER: 2,
            FRACTION: 2,
            ACTION: 2,
            PHANTOM: 0,
            XML: 2,
            GLYPH: 2
        },
        COLLAPSE: {
            identifier: 3,
            number: 3,
            text: 10,
            infixop: 15,
            relseq: 15,
            multirel: 15,
            fenced: 18,
            bigop: 20,
            integral: 20,
            fraction: 12,
            sqrt: 9,
            root: 12,
            vector: 15,
            matrix: 15,
            cases: 15,
            superscript: 9,
            subscript: 9,
            subsup: 9,
            punctuated: {
                endpunct: 1e7,
                startpunct: 1e7,
                value: 12
            }
        },
        MARKER: {
            identifier: "x",
            number: "#",
            text: "...",
            appl: {
                "limit function": "lim",
                value: "f()"
            },
            fraction: "/",
            sqrt: "\u221a",
            root: "\u221a",
            superscript: "\u25fd\u02d9",
            subscript: "\u25fd.",
            subsup: "\u25fd:",
            vector: {
                binomial: "(:)",
                determinant: "|:|",
                value: "\u27e8:\u27e9"
            },
            matrix: {
                squarematrix: "[::]",
                rowvector: "\u27e8\u22ef\u27e9",
                columnvector: "\u27e8\u22ee\u27e9",
                determinant: "|::|",
                value: "(::)"
            },
            cases: "{:",
            infixop: {
                addition: "+",
                subtraction: "\u2212",
                multiplication: "\u22c5",
                implicit: "\u22c5",
                value: "+"
            },
            punctuated: {
                text: "...",
                value: ","
            }
        },
        Enable: function(t, i) {
            l.collapsible = !0, i && (o.collapsible = !0), this.config.disabled = !1, MathJax.Extension["semantic-enrich"].Enable(!1, i), 
            t && s.Queue([ "Reprocess", s ]);
        },
        Disable: function(t, i) {
            l.collapsible = !1, i && (o.collapsible = !1), this.config.disabled = !0;
            for (var e = this.dependents.length - 1; 0 <= e; e--) {
                var a = this.dependents[e];
                a.Disable && a.Disable(!1, i);
            }
            t && s.Queue([ "Reprocess", s ]);
        },
        Dependent: function(t) {
            this.dependents.push(t);
        },
        Startup: function() {
            n = MathJax.ElementJax.mml;
            var t = MathJax.Extension["semantic-enrich"];
            t && t.Dependent(this), s.postInputHooks.Add([ "Filter", h ], 100);
        },
        Filter: function(t, i, e) {
            t.enriched && !this.config.disabled && (t.root = t.root.Collapse(), t.root.inputID = e.id);
        },
        Marker: function(t) {
            return n.mtext("\u25c2" + t + "\u25b8").With({
                mathcolor: "blue",
                attr: {},
                attrNames: []
            });
        },
        MakeAction: function(t, i) {
            var e = n.maction(t).With({
                id: this.getActionID(),
                actiontype: "toggle",
                complexity: t.getComplexity(),
                collapsible: !0,
                attrNames: [ "id", "actiontype", "selection", r ],
                attr: {},
                selection: 2
            });
            if (e.attr[r] = e.complexity, "math" === i.type) {
                var a = n.mrow().With({
                    complexity: i.complexity,
                    attrNames: [],
                    attr: {}
                });
                a.Append.apply(a, i.data[0].data), i.data[0].data = [];
                for (var s, l = i.attrNames.length - 1; s = i.attrNames[l]; l--) "data-semantic-" === s.substr(0, 14) && (a.attr[s] = i.attr[s], 
                a.attrNames.push(s), delete i.attr[s], i.attrNames.splice(l, 1));
                a.complexity = i.complexity, e.Append(a), i.Append(e), i.complexity = e.complexity, 
                e = i;
            } else e.Append(i);
            return e;
        },
        actionID: 1,
        getActionID: function() {
            return "MJX-Collapse-" + this.actionID++;
        },
        Collapse: function(t) {
            t.getComplexity();
            var i, e, a, s = (t.attr || {})["data-semantic-type"];
            return s && (this["Collapse_" + s] ? t = this["Collapse_" + s](t) : this.COLLAPSE[s] && this.MARKER[s] && (i = t.attr["data-semantic-role"], 
            "number" != typeof (e = this.COLLAPSE[s]) && (e = e[i] || e.value), t.complexity > e && ("string" != typeof (a = this.MARKER[s]) && (a = a[i] || a.value), 
            t = this.MakeAction(this.Marker(a), t)))), t;
        },
        UncollapseChild: function(t, i, e) {
            if (null == e && (e = 1), this.SplitAttribute(t, "children").length === e) {
                var a = 1 === t.data.length && t.data[0].inferred ? t.data[0] : t;
                if (a && a.data[i] && a.data[i].collapsible) return a.SetData(i, a.data[i].data[1]), 
                t.complexity = a.complexity = null, t.getComplexity(), 1;
            }
            return 0;
        },
        FindChildText: function(t, i) {
            var e = this.FindChild(t, i);
            return e ? (e.CoreMO() || e).data.join("") : "?";
        },
        FindChild: function(t, i) {
            if (t) {
                if (t.attr && t.attr["data-semantic-id"] === i) return t;
                if (!t.isToken) for (var e = 0, a = t.data.length; e < a; e++) {
                    var s = this.FindChild(t.data[e], i);
                    if (s) return s;
                }
            }
            return null;
        },
        SplitAttribute: function(t, i) {
            return (t.attr["data-semantic-" + i] || "").split(/,/);
        },
        Collapse_fenced: function(t) {
            var i;
            return this.UncollapseChild(t, 1), t.complexity > this.COLLAPSE.fenced && "leftright" === t.attr["data-semantic-role"] && (i = t.data[0].data.join("") + t.data[t.data.length - 1].data.join(""), 
            t = this.MakeAction(this.Marker(i), t)), t;
        },
        Collapse_appl: function(t) {
            var i;
            return this.UncollapseChild(t, 2, 2) && (i = (i = this.MARKER.appl)[t.attr["data-semantic-role"]] || i.value, 
            t = this.MakeAction(this.Marker(i), t)), t;
        },
        Collapse_sqrt: function(t) {
            return this.UncollapseChild(t, 0), t.complexity > this.COLLAPSE.sqrt && (t = this.MakeAction(this.Marker(this.MARKER.sqrt), t)), 
            t;
        },
        Collapse_root: function(t) {
            return this.UncollapseChild(t, 0), t.complexity > this.COLLAPSE.sqrt && (t = this.MakeAction(this.Marker(this.MARKER.sqrt), t)), 
            t;
        },
        Collapse_enclose: function(t) {
            var i, e;
            return 1 !== this.SplitAttribute(t, "children").length || (i = 1 === t.data.length && t.data[0].inferred ? t.data[0] : t).data[0] && i.data[0].collapsible && (e = i.data[0], 
            i.SetData(0, e.data[1]), e.SetData(1, t), t = e), t;
        },
        Collapse_bigop: function(t) {
            var i, e;
            return (t.complexity > this.COLLAPSE.bigop || "mo" !== t.data[0].type) && (i = this.SplitAttribute(t, "content").pop(), 
            e = h.FindChildText(t, i), t = this.MakeAction(this.Marker(e), t)), t;
        },
        Collapse_integral: function(t) {
            var i, e;
            return (t.complexity > this.COLLAPSE.integral || "mo" !== t.data[0].type) && (i = this.SplitAttribute(t, "content")[0], 
            e = h.FindChildText(t, i), t = this.MakeAction(this.Marker(e), t)), t;
        },
        Collapse_relseq: function(t) {
            var i, e;
            return t.complexity > this.COLLAPSE.relseq && (i = this.SplitAttribute(t, "content"), 
            e = h.FindChildText(t, i[0]), 1 < i.length && (e += "\u22ef"), t = this.MakeAction(this.Marker(e), t)), 
            t;
        },
        Collapse_multirel: function(t) {
            var i, e;
            return t.complexity > this.COLLAPSE.multirel && (i = this.SplitAttribute(t, "content"), 
            e = h.FindChildText(t, i[0]) + "\u22ef", t = this.MakeAction(this.Marker(e), t)), 
            t;
        },
        Collapse_superscript: function(t) {
            return this.UncollapseChild(t, 0, 2), t.complexity > this.COLLAPSE.superscript && (t = this.MakeAction(this.Marker(this.MARKER.superscript), t)), 
            t;
        },
        Collapse_subscript: function(t) {
            return this.UncollapseChild(t, 0, 2), t.complexity > this.COLLAPSE.subscript && (t = this.MakeAction(this.Marker(this.MARKER.subscript), t)), 
            t;
        },
        Collapse_subsup: function(t) {
            return this.UncollapseChild(t, 0, 3), t.complexity > this.COLLAPSE.subsup && (t = this.MakeAction(this.Marker(this.MARKER.subsup), t)), 
            t;
        }
    };
    s.Register.StartupHook("End Extensions", function() {
        null == l.collapsible ? l.collapsible = !h.config.disabled : h.config.disabled = !l.collapsible, 
        s.Register.StartupHook("MathMenu Ready", function() {
            o = MathJax.Menu.cookie;
            var t, i = MathJax.Menu.ITEM, e = MathJax.Menu.menu, a = i.CHECKBOX([ "CollapsibleMath", "Collapsible Math" ], "collapsible", {
                action: function(t) {
                    h[l.collapsible ? "Enable" : "Disable"](!0, !0), MathJax.Menu.saveCookie();
                }
            }), s = (e.FindId("Accessibility") || {}).submenu;
            s ? null !== (t = s.IndexOfId("CollapsibleMath")) ? s.items[t] = a : s.items.push(i.RULE(), a) : (t = e.IndexOfId("About"), 
            e.items.splice(t, 0, a, i.RULE()));
        }, 15);
    }, 15);
}(MathJax.Hub), MathJax.Ajax.Require("[a11y]/semantic-enrich.js"), MathJax.Hub.Register.StartupHook("Semantic Enrich Ready", function() {
    var t = MathJax.ElementJax.mml, i = MathJax.Extension.collapsible, a = i.COMPLEXITY, s = i.COMPLEXATTR;
    i.Startup(), t.mbase.Augment({
        Collapse: function() {
            return i.Collapse(this);
        },
        getComplexity: function() {
            if (null == this.complexity) {
                var t = 0;
                if (this.isToken) t = a.TEXT * this.data.join("").length + a.TOKEN; else {
                    for (var i = 0, e = this.data.length; i < e; i++) this.data[i] && (this.SetData(i, this.data[i].Collapse()), 
                    t += this.data[i].complexity);
                    1 < e && (t += e * a.CHILD);
                }
                !this.attrNames || "complexity" in this || this.attrNames.push(s), this.attr && (this.attr[s] = t), 
                this.complexity = t;
            }
            return this.complexity;
        },
        reportComplexity: function() {
            !this.attr || !this.attrNames || s in this.attr || (this.attrNames.push(s), this.attr[s] = this.complexity);
        }
    }), t.mfrac.Augment({
        getComplexity: function() {
            return null == this.complexity && (this.SUPER(arguments).getComplexity.call(this), 
            this.complexity *= a.SCRIPT, this.complexity += a.FRACTION, this.attr[s] = this.complexity), 
            this.complexity;
        }
    }), t.msqrt.Augment({
        getComplexity: function() {
            return null == this.complexity && (this.SUPER(arguments).getComplexity.call(this), 
            this.complexity += a.SQRT, this.attr[s] = this.complexity), this.complexity;
        }
    }), t.mroot.Augment({
        getComplexity: function() {
            return null == this.complexity && (this.SUPER(arguments).getComplexity.call(this), 
            this.complexity -= (1 - a.SCRIPT) * this.data[1].getComplexity(), this.complexity += a.SQRT, 
            this.attr[s] = this.complexity), this.complexity;
        }
    }), t.msubsup.Augment({
        getComplexity: function() {
            var t;
            return null == this.complexity && (t = 0, this.data[this.sub] && (t = this.data[this.sub].getComplexity() + a.CHILD), 
            this.data[this.sup] && (t = Math.max(this.data[this.sup].getComplexity(), t)), t *= a.SCRIPT, 
            this.data[this.sub] && (t += a.CHILD), this.data[this.sup] && (t += a.CHILD), this.data[this.base] && (t += this.data[this.base].getComplexity() + a.CHILD), 
            this.complexity = t + a.SUBSUP, this.reportComplexity()), this.complexity;
        }
    }), t.munderover.Augment({
        getComplexity: function() {
            var t;
            return null == this.complexity && (t = 0, this.data[this.sub] && (t = this.data[this.sub].getComplexity() + a.CHILD), 
            this.data[this.sup] && (t = Math.max(this.data[this.sup].getComplexity(), t)), t *= a.SCRIPT, 
            this.data[this.base] && (t = Math.max(this.data[this.base].getComplexity(), t)), 
            this.data[this.sub] && (t += a.CHILD), this.data[this.sup] && (t += a.CHILD), this.data[this.base] && (t += a.CHILD), 
            this.complexity = t + a.UNDEROVER, this.reportComplexity()), this.complexity;
        }
    }), t.mphantom.Augment({
        getComplexity: function() {
            return this.complexity = a.PHANTOM, this.reportComplexity(), this.complexity;
        }
    }), t.ms.Augment({
        getComplexity: function() {
            return this.SUPER(arguments).getComplexity.call(this), this.complexity += this.Get("lquote").length * a.TEXT, 
            this.complexity += this.Get("rquote").length * a.TEXT, this.attr[s] = this.complexity, 
            this.complexity;
        }
    }), t.menclose.Augment({
        getComplexity: function() {
            return null == this.complexity && (this.SUPER(arguments).getComplexity.call(this), 
            this.complexity += a.ACTION, this.attr[s] = this.complexity), this.complexity;
        }
    }), t.maction.Augment({
        getComplexity: function() {
            return this.complexity = (this.collapsible ? this.data[0] : this.selected()).getComplexity(), 
            this.reportComplexity(), this.complexity;
        }
    }), t.semantics.Augment({
        getComplexity: function() {
            return null == this.complexity && (this.complexity = this.data[0] ? this.data[0].getComplexity() : 0, 
            this.reportComplexity()), this.complexity;
        }
    }), t["annotation-xml"].Augment({
        getComplexity: function() {
            return this.complexity = a.XML, this.reportComplexity(), this.complexity;
        }
    }), t.annotation.Augment({
        getComplexity: function() {
            return this.complexity = a.XML, this.reportComplexity(), this.complexity;
        }
    }), t.mglyph.Augment({
        getComplexity: function() {
            return this.complexity = a.GLYPH, this.reportComplexity(), this.complexity;
        }
    }), MathJax.Hub.Startup.signal.Post("Collapsible Ready"), MathJax.Ajax.loadComplete("[a11y]/collapsible.js");
});