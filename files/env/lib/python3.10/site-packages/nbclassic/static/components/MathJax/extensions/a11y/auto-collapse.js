!function(c) {
    var s = c.config.menuSettings, r = {}, t = MathJax.Ajax.config.path;
    t.a11y || (t.a11y = c.config.root + "/extensions/a11y");
    var l = MathJax.Extension["auto-collapse"] = {
        version: "1.6.0",
        config: c.CombineConfig("auto-collapse", {
            disabled: !1
        }),
        dependents: [],
        Enable: function(t, e) {
            s.autocollapse = !0, e && (r.autocollapse = !0), this.config.disabled = !1, MathJax.Extension.collapsible.Enable(!1, e), 
            t && c.Queue([ "Reprocess", c ], [ "CollapseWideMath", this ]);
        },
        Disable: function(t, e) {
            s.autocollapse = !1, e && (r.autocollapse = !1), this.config.disabled = !0;
            for (var n = this.dependents.length - 1; 0 <= n; n--) {
                var o = this.dependents[n];
                o.Disable && o.Disable(!1, e);
            }
            t && c.Queue([ "Rerender", c ]);
        },
        Dependent: function(t) {
            this.dependents.push(t);
        },
        Startup: function() {
            var t = MathJax.Extension.collapsible;
            t && t.Dependent(this), c.postInputHooks.Add([ "Filter", l ], 150), c.Queue(function() {
                return l.CollapseWideMath();
            }), window.addEventListener ? window.addEventListener("resize", l.resizeHandler, !1) : window.attachEvent ? window.attachEvent("onresize", l.resizeHandler) : window.onresize = l.resizeHandler;
        },
        Filter: function(t, e, n) {
            t.enriched && !this.config.disabled && ("block" === t.root.Get("display") || n.parentNode.childNodes.length <= 3) && (t.root.SRE = {
                action: this.Actions(t.root)
            });
        },
        Actions: function(t) {
            var e = [];
            return this.getActions(t, 0, e), this.sortActions(e);
        },
        getActions: function(t, e, n) {
            if (!t.isToken && t.data) {
                e++;
                for (var o, i = 0, a = t.data.length; i < a; i++) {
                    t.data[i] && ((o = t.data[i]).collapsible ? (n[e] || (n[e] = []), n[e].push(o), 
                    this.getActions(o.data[1], e, n)) : this.getActions(o, e, n));
                }
            }
        },
        sortActions: function(t) {
            for (var e = [], n = 0, o = t.length; n < o; n++) t[n] && (e = e.concat(t[n].sort(this.sortActionsBy)));
            return e;
        },
        sortActionsBy: function(t, e) {
            return (t = t.data[1].complexity) < (e = e.data[1].complexity) ? -1 : e < t ? 1 : 0;
        },
        CollapseWideMath: function(t) {
            if (!this.config.disabled) {
                this.GetContainerWidths(t);
                var e = c.getAllJax(t), n = {
                    collapse: [],
                    jax: e,
                    m: e.length,
                    i: 0,
                    changed: !1
                };
                return this.collapseState(n);
            }
        },
        collapseState: function(t) {
            for (var e = t.collapse; t.i < t.m; ) {
                var n = t.jax[t.i], o = n.root.SRE;
                if (t.changed = !1, o && o.action.length && (o.cwidth < o.m || o.cwidth > o.M)) {
                    var i = this.getActionWidths(n, t);
                    if (i) return i;
                    this.collapseActions(o, t), t.changed && e.push(n.SourceElement());
                }
                t.i++;
            }
            if (0 !== e.length) return 1 === e.length && (e = e[0]), c.Rerender(e);
        },
        collapseActions: function(t, e) {
            for (var n = t.width, o = n, i = 1e6, a = t.action.length - 1; 0 <= a; a--) {
                var s = t.action[a], r = s.selection;
                n > t.cwidth ? (s.selection = 1, o = s.SREwidth, i = n) : s.selection = 2, n = s.SREwidth, 
                t.DOMupdate ? document.getElementById(s.id).setAttribute("selection", s.selection) : s.selection !== r && (e.changed = !0);
            }
            t.m = o, t.M = i;
        },
        getActionWidths: function(t, e) {
            if (!t.root.SRE.actionWidths) {
                MathJax.OutputJax[t.outputJax].getMetrics(t);
                try {
                    this.computeActionWidths(t);
                } catch (t) {
                    if (!t.restart) throw t;
                    return MathJax.Callback.After([ "collapseState", this, e ], t.restart);
                }
                e.changed = !0;
            }
            return null;
        },
        computeActionWidths: function(t) {
            var e, n = t.root.SRE, o = n.action, i = {};
            for (n.width = t.sreGetRootWidth(i), e = o.length - 1; 0 <= e; e--) o[e].selection = 2;
            for (e = o.length - 1; 0 <= e; e--) {
                var a = o[e];
                null == a.SREwidth && (a.selection = 1, a.SREwidth = t.sreGetActionWidth(i, a));
            }
            n.actionWidths = !0;
        },
        GetContainerWidths: function(t) {
            for (var e, n, o, i = c.getAllJax(t), a = MathJax.HTML.Element("span", {
                style: {
                    display: "block"
                }
            }), s = [], r = 0, l = i.length; r < l; r++) o = (n = i[r]).root, SRE = o.SRE, SRE && SRE.action.length && (null == SRE.width && (n.sreGetMetrics(), 
            SRE.m = SRE.width, SRE.M = 1e6), (e = n.SourceElement()).previousSibling.style.display = "none", 
            e.parentNode.insertBefore(a.cloneNode(!1), e), s.push([ n, e ]));
            for (r = 0, l = s.length; r < l; r++) n = s[r][0], (e = s[r][1]).previousSibling.offsetWidth && (n.root.SRE.cwidth = e.previousSibling.offsetWidth * n.root.SRE.em);
            for (r = 0, l = s.length; r < l; r++) n = s[r][0], (e = s[r][1]).parentNode.removeChild(e.previousSibling), 
            e.previousSibling.style.display = "";
        },
        timer: null,
        running: !1,
        retry: !1,
        saved_delay: 0,
        resizeHandler: function(t) {
            l.config.disabled || (l.running ? l.retry = !0 : (l.timer && clearTimeout(l.timer), 
            l.timer = setTimeout(l.resizeAction, 100)));
        },
        resizeAction: function() {
            l.timer = null, l.running = !0, c.Queue(function() {
                l.saved_delay = c.processSectionDelay, c.processSectionDelay = 0;
            }, [ "CollapseWideMath", l ], [ "resizeCheck", l ]);
        },
        resizeCheck: function() {
            l.running = !1, c.processSectionDelay = l.saved_delay, l.retry && (l.retry = !1, 
            setTimeout(l.resizeHandler, 0));
        }
    };
    c.Register.StartupHook("End Extensions", function() {
        null == s.autocollapse ? s.autocollapse = !l.config.disabled : l.config.disabled = !s.autocollapse, 
        c.Register.StartupHook("MathMenu Ready", function() {
            r = MathJax.Menu.cookie;
            var t, e = MathJax.Menu.ITEM, n = MathJax.Menu.menu, o = e.CHECKBOX([ "AutoCollapse", "Auto Collapse" ], "autocollapse", {
                action: function(t) {
                    l[s.autocollapse ? "Enable" : "Disable"](!0, !0), MathJax.Menu.saveCookie();
                }
            }), i = (n.FindId("Accessibility") || {}).submenu;
            i ? null !== (t = i.IndexOfId("AutoCollapse")) ? i.items[t] = o : (t = i.IndexOfId("CollapsibleMath"), 
            i.items.splice(t + 1, 0, o)) : (t = n.IndexOfId("CollapsibleMath"), n.items.splice(t + 1, 0, o));
            function a() {
                l[s.autocollapse ? "Enable" : "Disable"]();
            }
            MathJax.Extension.collapse ? a() : MathJax.Hub.Register.StartupHook("Auto Collapse Ready", a);
        }, 25);
    }, 25);
}(MathJax.Hub), MathJax.ElementJax.Augment({
    sreGetMetrics: function() {
        MathJax.OutputJax[this.outputJax].sreGetMetrics(this, this.root.SRE);
    },
    sreGetRootWidth: function(t) {
        return MathJax.OutputJax[this.outputJax].sreGetRootWidth(this, t);
    },
    sreGetActionWidth: function(t, e) {
        return MathJax.OutputJax[this.outputJax].sreGetActionWidth(this, t, e);
    }
}), MathJax.OutputJax.Augment({
    getMetrics: function() {},
    sreGetMetrics: function(t, e) {
        e.cwidth = 1e6, e.width = 0, e.em = 12;
    },
    sreGetRootWidth: function(t, e) {
        return 0;
    },
    sreGetActionWidth: function(t, e, n) {
        return 0;
    }
}), MathJax.Hub.Register.StartupHook("HTML-CSS Jax Ready", function() {
    MathJax.OutputJax["HTML-CSS"].Augment({
        sreGetMetrics: function(t, e) {
            e.width = t.root.data[0].HTMLspanElement().parentNode.bbox.w, e.em = 1 / t.HTMLCSS.em / t.HTMLCSS.scale;
        },
        sreGetRootWidth: function(t, e) {
            var n = t.root.data[0].HTMLspanElement();
            return e.box = n.parentNode, e.box.bbox.w;
        },
        sreGetActionWidth: function(t, e, n) {
            return t.root.data[0].toHTML(e.box).bbox.w;
        }
    });
}), MathJax.Hub.Register.StartupHook("SVG Jax Ready", function() {
    MathJax.OutputJax.SVG.Augment({
        getMetrics: function(t) {
            this.em = MathJax.ElementJax.mml.mbase.prototype.em = t.SVG.em, this.ex = t.SVG.ex, 
            this.linebreakWidth = t.SVG.lineWidth, this.cwidth = t.SVG.cwidth;
        },
        sreGetMetrics: function(t, e) {
            e.width = t.root.SVGdata.w / 1e3, e.em = 1 / t.SVG.em;
        },
        sreGetRootWidth: function(t, e) {
            return e.span = document.getElementById(t.inputID + "-Frame"), t.root.SVGdata.w / 1e3;
        },
        sreGetActionWidth: function(t, e, n) {
            this.mathDiv = e.span, e.span.appendChild(this.textSVG);
            try {
                t.root.data[0].toSVG();
            } catch (t) {
                var o = t;
            }
            if (e.span.removeChild(this.textSVG), o) throw o;
            return t.root.data[0].SVGdata.w / 1e3;
        }
    });
}), MathJax.Hub.Register.StartupHook("CommonHTML Jax Ready", function() {
    MathJax.OutputJax.CommonHTML.Augment({
        sreGetMetrics: function(t, e) {
            e.width = t.root.CHTML.w, e.em = 1 / t.CHTML.em / t.CHTML.scale;
        },
        sreGetRootWidth: function(t, e) {
            return e.span = document.getElementById(t.inputID + "-Frame").firstChild, e.tmp = document.createElement("span"), 
            e.tmp.className = e.span.className, t.root.CHTML.w / t.CHTML.scale;
        },
        sreGetActionWidth: function(t, e, n) {
            e.span.parentNode.replaceChild(e.tmp, e.span), MathJax.OutputJax.CommonHTML.CHTMLnode = e.tmp;
            try {
                t.root.data[0].toCommonHTML(e.tmp);
            } catch (t) {
                var o = t;
            }
            if (e.tmp.parentNode.replaceChild(e.span, e.tmp), o) throw o;
            return t.root.data[0].CHTML.w / t.CHTML.scale;
        }
    });
}), MathJax.Hub.Register.StartupHook("NativeMML Jax Ready", function() {
    MathJax.OutputJax.NativeMML.Augment({
        sreGetMetrics: function(t, e) {
            var n = document.getElementById(t.inputID + "-Frame");
            e.width = n.offsetWidth, e.em = 1, e.DOMupdate = !0;
        },
        sreGetRootWidth: function(t, e) {
            return e.span = document.getElementById(t.inputID + "-Frame").firstChild, e.span.offsetWidth;
        },
        sreGetActionWidth: function(t, e, n) {
            return document.getElementById(n.id).setAttribute("selection", 1), e.span.offsetWidth;
        }
    });
}), MathJax.Ajax.Require("[a11y]/collapsible.js"), MathJax.Hub.Register.StartupHook("Collapsible Ready", function() {
    MathJax.Extension["auto-collapse"].Startup(), MathJax.Hub.Startup.signal.Post("Auto Collapse Ready"), 
    MathJax.Ajax.loadComplete("[a11y]/auto-collapse.js");
});