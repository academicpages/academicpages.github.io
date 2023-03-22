MathJax.Hub.Register.StartupHook("Sre Ready", function() {
    var o, r, s = MathJax.Hub.config.menuSettings, l = {};
    MathJax.Hub.Register.StartupHook("MathEvents Ready", function() {
        o = MathJax.Extension.MathEvents.Event.False, r = MathJax.Extension.MathEvents.Event.KEY;
    });
    var h = MathJax.Extension.explorer = {
        version: "1.6.0",
        dependents: [],
        defaults: {
            walker: "table",
            highlight: "none",
            background: "blue",
            foreground: "black",
            speech: !0,
            generation: "lazy",
            subtitle: !1,
            ruleset: "mathspeak-default"
        },
        eagerComplexity: 80,
        prefix: "Assistive-",
        hook: null,
        locHook: null,
        oldrules: null,
        addMenuOption: function(e, t) {
            s[h.prefix + e] = t;
        },
        addDefaults: function() {
            for (var e, t = MathJax.Hub.CombineConfig("explorer", h.defaults), a = Object.keys(t), i = 0; e = a[i]; i++) void 0 === s[h.prefix + e] && h.addMenuOption(e, t[e]);
            h.setSpeechOption(), u.Reset();
        },
        setOption: function(e, t) {
            s[h.prefix + e] !== t && (h.addMenuOption(e, t), u.Reset());
        },
        getOption: function(e) {
            return s[h.prefix + e];
        },
        speechOption: function(e) {
            h.oldrules !== e.value && (h.setSpeechOption(), u.Regenerate());
        },
        setSpeechOption: function() {
            var e = s[h.prefix + "ruleset"], t = e.split("-");
            sre.System.getInstance().setupEngine({
                locale: MathJax.Localization.locale,
                domain: h.Domain(t[0]),
                style: t[1]
            }), h.oldrules = e;
        },
        Domain: function(e) {
            switch (e) {
              case "chromevox":
                return "default";

              case "clearspeak":
                return "clearspeak";

              case "mathspeak":
              default:
                return "mathspeak";
            }
        },
        Enable: function(e, t) {
            s.explorer = !0, t && (l.explorer = !0), MathJax.Extension.collapsible.Enable(!1, t), 
            MathJax.Extension.AssistiveMML && (MathJax.Extension.AssistiveMML.config.disabled = !0, 
            s.assistiveMML = !1, t && (l.assistiveMML = !1)), this.DisableMenus(!1), this.hook || (this.hook = MathJax.Hub.Register.MessageHook("New Math", [ "Register", this.Explorer ])), 
            this.locHook || (this.locHook = MathJax.Hub.Register.MessageHook("Locale Reset", [ "RemoveSpeech", this.Explorer ])), 
            e && MathJax.Hub.Queue([ "Reprocess", MathJax.Hub ]);
        },
        Disable: function(e, t) {
            s.explorer = !1, t && (l.explorer = !1), this.DisableMenus(!0), this.hook && (MathJax.Hub.UnRegister.MessageHook(this.hook), 
            this.hook = null);
            for (var a = this.dependents.length - 1; 0 <= a; a--) {
                var i = this.dependents[a];
                i.Disable && i.Disable(!1, t);
            }
        },
        DisableMenus: function(e) {
            if (MathJax.Menu) {
                var t = MathJax.Menu.menu.FindId("Accessibility", "Explorer");
                if (t) {
                    for (var a, i = (t = t.submenu).items, n = 2; a = i[n]; n++) a.disabled = e;
                    e || !t.FindId("SpeechOutput") || s[h.prefix + "speech"] || (t.FindId("Subtitles").disabled = !0);
                }
            }
        },
        Dependent: function(e) {
            this.dependents.push(e);
        }
    }, n = MathJax.Object.Subclass({
        div: null,
        inner: null,
        Init: function() {
            this.div = n.Create("assertive"), this.inner = MathJax.HTML.addElement(this.div, "div");
        },
        Add: function() {
            n.added || (document.body.appendChild(this.div), n.added = !0);
        },
        Show: function(e, t) {
            this.div.classList.add("MJX_LiveRegion_Show");
            var a = e.getBoundingClientRect(), i = a.bottom + 10 + window.pageYOffset, n = a.left + window.pageXOffset;
            this.div.style.top = i + "px", this.div.style.left = n + "px";
            var o = t.colorString();
            this.inner.style.backgroundColor = o.background, this.inner.style.color = o.foreground;
        },
        Hide: function(e) {
            this.div.classList.remove("MJX_LiveRegion_Show");
        },
        Clear: function() {
            this.Update(""), this.inner.style.top = "", this.inner.style.backgroundColor = "";
        },
        Update: function(e) {
            h.getOption("speech") && n.Update(this.inner, e);
        }
    }, {
        ANNOUNCE: "Navigatable Math in page. Explore with enter or shift space and arrow keys. Expand or collapse elements hitting enter.",
        announced: !1,
        added: !1,
        styles: {
            ".MJX_LiveRegion": {
                position: "absolute",
                top: "0",
                height: "1px",
                width: "1px",
                padding: "1px",
                overflow: "hidden"
            },
            ".MJX_LiveRegion_Show": {
                top: "0",
                position: "absolute",
                width: "auto",
                height: "auto",
                padding: "0px 0px",
                opacity: 1,
                "z-index": "202",
                left: 0,
                right: 0,
                margin: "0 auto",
                "background-color": "white",
                "box-shadow": "0px 10px 20px #888",
                border: "2px solid #CCCCCC"
            }
        },
        Create: function(e) {
            var t = MathJax.HTML.Element("div", {
                className: "MJX_LiveRegion"
            });
            return t.setAttribute("aria-live", e), t;
        },
        Update: MathJax.Hub.Browser.isPC ? function(e, t) {
            e.textContent = "", setTimeout(function() {
                e.textContent = t;
            }, 100);
        } : function(e, t) {
            e.textContent = "", e.textContent = t;
        },
        Announce: function() {
            var e;
            h.getOption("speech") && (n.announced = !0, MathJax.Ajax.Styles(n.styles), e = n.Create("polite"), 
            document.body.appendChild(e), n.Update(e, n.ANNOUNCE), setTimeout(function() {
                document.body.removeChild(e);
            }, 1e3));
        }
    });
    MathJax.Extension.explorer.LiveRegion = n;
    var e = MathJax.Ajax.fileURL(MathJax.Ajax.config.path.a11y), u = MathJax.Extension.explorer.Explorer = {
        liveRegion: n(),
        walker: null,
        highlighter: null,
        hoverer: null,
        flamer: null,
        speechDiv: null,
        earconFile: e + "/invalid_keypress" + (-1 !== [ "Firefox", "Chrome", "Opera" ].indexOf(MathJax.Hub.Browser.name) ? ".ogg" : ".mp3"),
        expanded: !1,
        focusoutEvent: MathJax.Hub.Browser.isFirefox ? "blur" : "focusout",
        focusinEvent: "focus",
        ignoreFocusOut: !1,
        jaxCache: {},
        messageID: null,
        Reset: function() {
            u.FlameEnriched();
        },
        Register: function(e) {
            var t, a;
            !h.hook || (t = document.getElementById(e[1])) && t.id && ((a = MathJax.Hub.getJaxFor(t.id)) && a.enriched && (u.StateChange(t.id, a), 
            u.liveRegion.Add(), u.AddEvent(t)));
        },
        StateChange: function(e, t) {
            u.GetHighlighter(.2);
            var a = u.jaxCache[e];
            a && a === t.root || (a && sre.Walker.resetState(e + "-Frame"), u.jaxCache[e] = t.root);
        },
        AddAria: function(e) {
            e.setAttribute("role", "application"), e.setAttribute("aria-label", "Math");
        },
        AddHook: function(i) {
            u.RemoveHook(), u.hook = MathJax.Hub.Register.MessageHook("End Math", function(e) {
                var t = e[1].id + "-Frame", a = document.getElementById(t);
                i && t === u.expanded && (u.ActivateWalker(a, i), a.focus(), u.expanded = !1);
            });
        },
        RemoveHook: function() {
            u.hook && (MathJax.Hub.UnRegister.MessageHook(u.hook), u.hook = null);
        },
        AddMessage: function() {
            return MathJax.Message.Set("Generating Speech Output");
        },
        RemoveMessage: function(e) {
            e && MathJax.Message.Clear(e);
        },
        AddEvent: function(e) {
            var t, a = e.id + "-Frame", i = e.previousSibling;
            i && (t = i.id !== a ? i.firstElementChild : i, u.AddAria(t), u.AddMouseEvents(t), 
            "MathJax_MathML" === t.className && (t = t.firstElementChild), t && (t.onkeydown = u.Keydown, 
            u.Flame(t), t.addEventListener(u.focusinEvent, function(e) {
                h.hook && (n.announced || n.Announce());
            }), t.addEventListener(u.focusoutEvent, function(e) {
                h.hook && (u.ignoreFocusOut && (u.ignoreFocusOut = !1, "enter" === u.walker.moved) ? e.target.focus() : u.walker && u.DeactivateWalker());
            }), h.getOption("speech") && u.AddSpeech(t)));
        },
        AddSpeech: function(e) {
            var t = e.id, a = MathJax.Hub.getJaxFor(t).root.toMathML();
            if (e.getAttribute("haslabel") || u.AddMathLabel(a, t), !e.getAttribute("hasspeech")) switch (MathJax.Hub.config.explorer.generation) {
              case "eager":
                u.AddSpeechEager(a, t);
                break;

              case "mixed":
                e.querySelectorAll("[data-semantic-complexity]").length >= h.eagerComplexity && u.AddSpeechEager(a, t);
            }
        },
        AddSpeechLazy: function(e) {
            var t = new sre.TreeSpeechGenerator();
            t.setRebuilt(u.walker.getRebuilt()), t.getSpeech(u.walker.rootNode, u.walker.getXml()), 
            e.setAttribute("hasspeech", "true");
        },
        AddSpeechEager: function(e, t) {
            u.MakeSpeechTask(e, t, sre.TreeSpeechGenerator, function(e, t) {
                e.setAttribute("hasspeech", "true");
            }, 5);
        },
        AddMathLabel: function(e, t) {
            u.MakeSpeechTask(e, t, sre.SummarySpeechGenerator, function(e, t) {
                e.setAttribute("haslabel", "true"), e.setAttribute("aria-label", t);
            }, 5);
        },
        MakeSpeechTask: function(i, n, o, r, e) {
            var s = u.AddMessage();
            setTimeout(function() {
                var e = new o(), t = document.getElementById(n), a = new sre.DummyWalker(t, e, u.highlighter, i).speech();
                a && r(t, a), u.RemoveMessage(s);
            }, e);
        },
        Keydown: function(e) {
            var t = e.keyCode;
            if (t === r.ESCAPE) {
                if (!u.walker) return;
                return u.RemoveHook(), u.DeactivateWalker(), void o(e);
            }
            if (u.walker && u.walker.isActive()) {
                t = t === r.RETURN ? r.DASH : t, void 0 !== u.walker.modifier && (u.walker.modifier = e.shiftKey);
                var a = u.walker.move(t);
                if (null === a) return;
                if (a) {
                    if ("expand" === u.walker.moved) {
                        if (u.expanded = u.walker.node.id, MathJax.Hub.Browser.isEdge) return u.ignoreFocusOut = !0, 
                        void u.DeactivateWalker();
                        if (MathJax.Hub.Browser.isFirefox || MathJax.Hub.Browser.isMSIE) return void u.DeactivateWalker();
                    }
                    u.liveRegion.Update(u.walker.speech()), u.Highlight();
                } else u.PlayEarcon();
                o(e);
            } else {
                var i = e.target;
                if (t === r.SPACE && !e.shiftKey) return MathJax.Extension.MathEvents.Event.ContextMenu(e, i), 
                void o(e);
                if (h.hook && (t === r.RETURN || t === r.SPACE && e.shiftKey)) {
                    var n = MathJax.Hub.getJaxFor(i);
                    return u.ActivateWalker(i, n), u.AddHook(n), void o(e);
                }
            }
        },
        GetHighlighter: function(e) {
            u.highlighter = sre.HighlighterFactory.highlighter({
                color: h.getOption("background"),
                alpha: e
            }, {
                color: h.getOption("foreground"),
                alpha: 1
            }, {
                renderer: MathJax.Hub.outputJax["jax/mml"][0].id,
                browser: MathJax.Hub.Browser.name
            });
        },
        AddMouseEvents: function(e) {
            sre.HighlighterFactory.addEvents(e, {
                mouseover: u.MouseOver,
                mouseout: u.MouseOut
            }, {
                renderer: MathJax.Hub.outputJax["jax/mml"][0].id,
                browser: MathJax.Hub.Browser.name
            });
        },
        MouseOver: function(e) {
            var t;
            "none" !== h.getOption("highlight") && ("hover" === h.getOption("highlight") && (t = e.currentTarget, 
            u.GetHighlighter(.1), u.highlighter.highlight([ t ]), u.hoverer = !0), o(e));
        },
        MouseOut: function(e) {
            return u.hoverer && (u.highlighter.unhighlight(), u.hoverer = !1), o(e);
        },
        Flame: function(e) {
            if ("flame" === h.getOption("highlight")) return u.GetHighlighter(.05), u.highlighter.highlightAll(e), 
            void (u.flamer = !0);
        },
        UnFlame: function() {
            u.flamer && (u.highlighter.unhighlightAll(), u.flamer = null);
        },
        FlameEnriched: function() {
            u.UnFlame();
            for (var e, t = 0, a = MathJax.Hub.getAllJax(); e = a[t]; t++) u.Flame(e.SourceElement().previousSibling);
        },
        Walkers: {
            syntactic: sre.SyntaxWalker,
            table: sre.TableWalker,
            semantic: sre.SemanticWalker,
            none: sre.DummyWalker
        },
        ActivateWalker: function(e, t) {
            var a = h.getOption("speech"), i = h.getOption("walker") ? u.Walkers[MathJax.Hub.config.explorer.walker] : u.Walkers.none, n = a ? new sre.DirectSpeechGenerator() : new sre.DummySpeechGenerator(), o = sre.System.getInstance().engineSetup();
            n.setOptions({
                locale: o.locale,
                domain: o.domain,
                style: o.style,
                modality: "speech"
            }), u.GetHighlighter(.2), u.walker = new i(e, n, u.highlighter, t.root.toMathML()), 
            a && !e.getAttribute("hasspeech") && u.AddSpeechLazy(e), u.walker.activate(), a && (h.getOption("subtitle") && u.liveRegion.Show(e, u.highlighter), 
            u.liveRegion.Update(u.walker.speech())), u.Highlight(), u.ignoreFocusOut && setTimeout(function() {
                u.ignoreFocusOut = !1;
            }, 500);
        },
        DeactivateWalker: function() {
            var e = sre.System.getInstance().engineSetup(), t = "clearspeak" === e.domain ? "default" : e.style;
            h.setOption("ruleset", e.domain + "-" + t), u.liveRegion.Clear(), u.liveRegion.Hide(), 
            u.Unhighlight(), u.currentHighlight = null, u.walker.deactivate(), u.walker = null;
        },
        Highlight: function() {
            u.Unhighlight(), u.highlighter.highlight(u.walker.getFocus().getNodes());
        },
        Unhighlight: function() {
            u.highlighter.unhighlight();
        },
        PlayEarcon: function() {
            new Audio(u.earconFile).play();
        },
        SpeechOutput: function() {
            u.Reset();
            [ "Subtitles" ].forEach(function(e) {
                var t = MathJax.Menu.menu.FindId("Accessibility", "Explorer", e);
                t && (t.disabled = !t.disabled);
            }), u.Regenerate();
        },
        RemoveSpeech: function() {
            h.setSpeechOption();
            for (var e, t = 0, a = MathJax.Hub.getAllJax(); e = a[t]; t++) {
                var i = document.getElementById(e.inputID + "-Frame");
                i && (i.removeAttribute("hasspeech"), i.removeAttribute("haslabel"));
            }
        },
        Regenerate: function() {
            for (var e, t = 0, a = MathJax.Hub.getAllJax(); e = a[t]; t++) {
                var i = document.getElementById(e.inputID + "-Frame");
                i && (i.removeAttribute("hasspeech"), u.AddSpeech(i));
            }
        },
        Startup: function() {
            var e = MathJax.Extension.collapsible;
            e && e.Dependent(h), h.addDefaults();
        }
    };
    MathJax.Hub.Register.StartupHook("End Extensions", function() {
        h[!1 === s.explorer ? "Disable" : "Enable"](), MathJax.Hub.Startup.signal.Post("Explorer Ready"), 
        MathJax.Hub.Register.StartupHook("MathMenu Ready", function() {
            l = MathJax.Menu.cookie;
            var e, t = MathJax.Menu.ITEM, a = MathJax.Menu.menu, i = {
                action: u.Reset
            }, n = {
                action: h.speechOption
            }, o = t.SUBMENU([ "Explorer", "Explorer" ], t.CHECKBOX([ "Active", "Active" ], "explorer", {
                action: function(e) {
                    h[s.explorer ? "Enable" : "Disable"](!0, !0), MathJax.Menu.saveCookie();
                }
            }), t.RULE(), t.CHECKBOX([ "Walker", "Walker" ], "Assistive-walker"), t.SUBMENU([ "Highlight", "Highlight" ], t.RADIO([ "none", "None" ], "Assistive-highlight", i), t.RADIO([ "hover", "Hover" ], "Assistive-highlight", i), t.RADIO([ "flame", "Flame" ], "Assistive-highlight", i)), t.SUBMENU([ "Background", "Background" ], t.RADIO([ "blue", "Blue" ], "Assistive-background", i), t.RADIO([ "red", "Red" ], "Assistive-background", i), t.RADIO([ "green", "Green" ], "Assistive-background", i), t.RADIO([ "yellow", "Yellow" ], "Assistive-background", i), t.RADIO([ "cyan", "Cyan" ], "Assistive-background", i), t.RADIO([ "magenta", "Magenta" ], "Assistive-background", i), t.RADIO([ "white", "White" ], "Assistive-background", i), t.RADIO([ "black", "Black" ], "Assistive-background", i)), t.SUBMENU([ "Foreground", "Foreground" ], t.RADIO([ "black", "Black" ], "Assistive-foreground", i), t.RADIO([ "white", "White" ], "Assistive-foreground", i), t.RADIO([ "magenta", "Magenta" ], "Assistive-foreground", i), t.RADIO([ "cyan", "Cyan" ], "Assistive-foreground", i), t.RADIO([ "yellow", "Yellow" ], "Assistive-foreground", i), t.RADIO([ "green", "Green" ], "Assistive-foreground", i), t.RADIO([ "red", "Red" ], "Assistive-foreground", i), t.RADIO([ "blue", "Blue" ], "Assistive-foreground", i)), t.RULE(), t.CHECKBOX([ "SpeechOutput", "Speech Output" ], "Assistive-speech", {
                action: u.SpeechOutput
            }), t.CHECKBOX([ "Subtitles", "Subtitles" ], "Assistive-subtitle", {
                disabled: !s["Assistive-speech"]
            }), t.RULE(), t.SUBMENU([ "Mathspeak", "Mathspeak Rules" ], t.RADIO([ "mathspeak-default", "Verbose" ], "Assistive-ruleset", n), t.RADIO([ "mathspeak-brief", "Brief" ], "Assistive-ruleset", n), t.RADIO([ "mathspeak-sbrief", "Superbrief" ], "Assistive-ruleset", n)), t.RADIO([ "clearspeak-default", "Clearspeak Rules" ], "Assistive-ruleset", n), t.SUBMENU([ "Chromevox", "ChromeVox Rules" ], t.RADIO([ "chromevox-default", "Verbose" ], "Assistive-ruleset", n), t.RADIO([ "chromevox-alternative", "Alternative" ], "Assistive-ruleset", n))), r = (a.FindId("Accessibility") || {}).submenu;
            r ? null !== (e = r.IndexOfId("Explorer")) ? r.items[e] = o : (e = r.IndexOfId("CollapsibleMath"), 
            r.items.splice(e + 1, 0, o)) : (e = a.IndexOfId("CollapsibleMath"), a.items.splice(e + 1, 0, o)), 
            s.explorer || h.DisableMenus(!0);
        }, 20);
    }, 20);
}), MathJax.Hub.Register.StartupHook("SVG Jax Ready", function() {
    MathJax.Hub.Config({
        SVG: {
            addMMLclasses: !0
        }
    });
    var t, e = MathJax.OutputJax.SVG;
    parseFloat(e.version) < 2.7 && (t = e.getJaxFromMath, e.Augment({
        getJaxFromMath: function(e) {
            return e.parentNode.className.match(/MathJax_SVG_Display/) && (e = e.parentNode), 
            t.call(this, e);
        }
    }));
}), MathJax.Ajax.config.path.a11y || (MathJax.Ajax.config.path.a11y = MathJax.Hub.config.root + "/extensions/a11y"), 
MathJax.Ajax.Require("[a11y]/collapsible.js"), MathJax.Hub.Register.StartupHook("Collapsible Ready", function() {
    MathJax.Extension.explorer.Explorer.Startup(), MathJax.Ajax.loadComplete("[a11y]/explorer.js");
});