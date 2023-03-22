

var normalized_shortcuts = [
    'ctrl-shift-m',
    'alt-meta-p',
];

var to_normalize = [
    ['shift-%', 'shift-5'],
    ['ShiFT-MeTa-CtRl-AlT-m', 'alt-ctrl-meta-shift-m'],
];

var unshifted = "` 1 2 3 4 5 6 7 8 9 0 - = q w e r t y u i o p [ ] \\ a s d f g h j k l ; ' z x c v b n m , . /";
//  shifted   = '~ ! @ # $ % ^ & * ( ) _ + Q W E R T Y U I O P { } |  A S D F G H J K L : " Z X C V B N M < > ?';

var ambiguous_expect = function(ch){
    // `-` is ambiguous in shortcut context as a separator, so map it to `minus`
    if(ch === '-'){
        return 'minus';
    }
    return ch;
};

casper.notebook_test(function () {
    var that = this;

    this.then(function () {
        this.each(unshifted.split(' '), function (self, item) {
            var result = this.evaluate(function (sc) {
                var e = IPython.keyboard.shortcut_to_event(sc);
                var sc2 = IPython.keyboard.event_to_shortcut(e);
                return sc2;
            }, item);
            this.test.assertEquals(result, ambiguous_expect(item), 'Shortcut to event roundtrip: '+item);
        });
    });

    this.then(function () {
        this.each(to_normalize, function (self, item) {
            var result = this.evaluate(function (pair) {
                return IPython.keyboard.normalize_shortcut(pair[0]);
            }, item);
            this.test.assertEquals(result, item[1], 'Normalize shortcut: '+item[0]);
        });
    });

    this.then(function () {
        this.each(normalized_shortcuts, function (self, item) {
            var result = this.evaluate(function (sc) {
                var e = IPython.keyboard.shortcut_to_event(sc);
                var sc2 = IPython.keyboard.event_to_shortcut(e);
                return sc2;
            }, item);
            this.test.assertEquals(result, item, 'Shortcut to event roundtrip: '+item);
        });
    });

    this.then(function(){

        var shortcuts_test = {
            'i,e,e,e,e,e'                                 : '[[5E]]',
            'i,d,d,q,d'                                   : '[[TEST1]]',
            'i,d,d'                                       : '[[TEST1 WILL BE SHADOWED]]',
            'i,d,k'                                       : '[[SHOULD SHADOW TEST2]]',
            'i,d,k,r,q'                                   : '[[TEST2 NOT SHADOWED]]',
            ';,up,down,up,down,left,right,left,right,b,a' : '[[KONAMI]]',
            'ctrl-x,meta-c,meta-b,u,t,t,e,r,f,l,y'        : '[[XKCD]]'

        };

        that.msgs = [];
        that.on('remote.message', function(msg) {
          that.msgs.push(msg);
        });
        that.evaluate(function (obj) {
            for(var k in obj){
                if ({}.hasOwnProperty.call(obj, k)) {
                    IPython.keyboard_manager.command_shortcuts.add_shortcut(k, function(){console.log(obj[k]);});
                }
            }
        }, shortcuts_test);

        var longer_first = false;
        var longer_last = false;
        for(var m in that.msgs){
            if ({}.hasOwnProperty.call(that.msgs, m)) {
                longer_first = longer_first||(that.msgs[m].match(/you are overriting/)!= null);
                longer_last = longer_last  ||(that.msgs[m].match(/will be shadowed/) != null);
            }
        }
        this.test.assert(longer_first, 'no warning if registering shorter shortcut');
        this.test.assert(longer_last , 'no warning if registering longer shortcut');
    });

});
