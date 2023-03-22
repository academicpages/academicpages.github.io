casper.notebook_test(function () {
    this.on('remote.callback', function(data){
        if(data.error_expected){
            that.test.assertEquals(
                data.error,
                true,
                "!highlight: " + data.provided + " errors"
            );
        }else{
            that.test.assertEquals(
                data.observed,
                data.expected,
                "highlight: " + data.provided + " as " + data.expected
            );
        }
    });
    
    var that = this;
    // syntax highlighting
    [
        {to: "gfm"},
        {to: "python"},
        {to: "ipython"},
        {to: "ipythongfm"},
        {to: "text/x-markdown", from: [".md"]},
        {to: "text/x-python", from: [".py", "Python"]},
        {to: "application/json", from: ["json", "JSON"]},
        {to: "text/x-ruby", from: [".rb", "ruby", "Ruby"]},
        {to: "application/ld+json", from: ["json-ld", "JSON-LD"]},
        {from: [".pyc"], error: true},
        {from: ["../"], error: true},
        {from: ["//"], error: true},
    ].map(function (mode) {
        (mode.from || []).concat(mode.to || []).map(function(from){
            casper.evaluate(function(from, expected, error_expected){
                IPython.utils.requireCodeMirrorMode(from, function(observed){
                    window.callPhantom({
                        provided: from,
                        expected: expected,
                        observed: observed,
                        error_expected: error_expected
                    });
                }, function(error){
                    window.callPhantom({
                        provided: from,
                        expected: expected,
                        error: true,
                        error_expected: error_expected
                    });
                });
            }, {
                from: from,
                expected: mode.to,
                error_expected: mode.error
            });
        });
    });
});