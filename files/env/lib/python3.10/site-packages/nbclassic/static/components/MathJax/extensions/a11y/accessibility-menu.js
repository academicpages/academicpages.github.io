!function(i, e) {
    var s, u, a = i.config.menuSettings, t = Function.prototype.bind ? function(e, t) {
        return e.bind(t);
    } : function(e, t) {
        return function() {
            e.apply(t, arguments);
        };
    }, o = Object.keys || function(e) {
        var t = [];
        for (var n in e) e.hasOwnProperty(n) && t.push(n);
        return t;
    }, n = MathJax.Ajax.config.path;
    n.a11y || (n.a11y = i.config.root + "/extensions/a11y");
    var l = e["accessibility-menu"] = {
        version: "1.6.0",
        prefix: "",
        defaults: {},
        modules: [],
        MakeOption: function(e) {
            return l.prefix + e;
        },
        GetOption: function(e) {
            return a[l.MakeOption(e)];
        },
        AddDefaults: function() {
            for (var e, t = o(l.defaults), n = 0; e = t[n]; n++) {
                var i = l.MakeOption(e);
                void 0 === a[i] && (a[i] = l.defaults[e]);
            }
        },
        AddMenu: function() {
            for (var e, t = Array(this.modules.length), n = 0; e = this.modules[n]; n++) t[n] = e.placeHolder;
            var i, a, o = u.FindId("Accessibility");
            o ? (t.unshift(s.RULE()), o.submenu.items.push.apply(o.submenu.items, t)) : ((i = (u.FindId("Settings", "Renderer") || {}).submenu) && (t.unshift(s.RULE()), 
            t.unshift(i.items.pop()), t.unshift(i.items.pop())), t.unshift("Accessibility"), 
            o = s.SUBMENU.apply(s.SUBMENU, t), (a = u.IndexOfId("Locale")) ? u.items.splice(a, 0, o) : u.items.push(s.RULE(), o));
        },
        Register: function(e) {
            l.defaults[e.option] = !1, l.modules.push(e);
        },
        Startup: function() {
            s = MathJax.Menu.ITEM, u = MathJax.Menu.menu;
            for (var e, t = 0; e = this.modules[t]; t++) e.CreateMenu();
            this.AddMenu();
        },
        LoadExtensions: function() {
            for (var e, t = [], n = 0; e = this.modules[n]; n++) a[e.option] && t.push(e.module);
            return t.length ? i.Startup.loadArray(t) : null;
        }
    }, r = MathJax.Extension.ModuleLoader = MathJax.Object.Subclass({
        option: "",
        name: [ "", "" ],
        module: "",
        placeHolder: null,
        submenu: !1,
        extension: null,
        Init: function(e, t, n, i, a) {
            this.option = e, this.name = [ t.replace(/ /g, ""), t ], this.module = n, this.extension = i, 
            this.submenu = a || !1;
        },
        CreateMenu: function() {
            var e = t(this.Load, this);
            this.submenu ? this.placeHolder = s.SUBMENU(this.name, s.CHECKBOX([ "Activate", "Activate" ], l.MakeOption(this.option), {
                action: e
            }), s.RULE(), s.COMMAND([ "OptionsWhenActive", "(Options when Active)" ], null, {
                disabled: !0
            })) : this.placeHolder = s.CHECKBOX(this.name, l.MakeOption(this.option), {
                action: e
            });
        },
        Load: function() {
            i.Queue([ "Require", MathJax.Ajax, this.module, [ "Enable", this ] ]);
        },
        Enable: function(e) {
            var t = MathJax.Extension[this.extension];
            t && (t.Enable(!0, !0), MathJax.Menu.saveCookie());
        }
    });
    l.Register(r("collapsible", "Collapsible Math", "[a11y]/collapsible.js", "collapsible")), 
    l.Register(r("autocollapse", "Auto Collapse", "[a11y]/auto-collapse.js", "auto-collapse")), 
    l.Register(r("explorer", "Explorer", "[a11y]/explorer.js", "explorer", !0)), l.AddDefaults(), 
    i.Register.StartupHook("End Extensions", function() {
        i.Register.StartupHook("MathMenu Ready", function() {
            l.Startup(), i.Startup.signal.Post("Accessibility Menu Ready");
        }, 5);
    }, 5), MathJax.Hub.Register.StartupHook("End Cookie", function() {
        MathJax.Callback.Queue([ "LoadExtensions", l ], [ "loadComplete", MathJax.Ajax, "[a11y]/accessibility-menu.js" ]);
    });
}(MathJax.Hub, MathJax.Extension);