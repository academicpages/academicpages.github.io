
//
// Miscellaneous javascript tests
//
casper.notebook_test(function () {
    var jsver = this.evaluate(function () {
        var cell = IPython.notebook.get_cell(0);
        cell.set_text('import nbclassic; print(nbclassic.__version__)');
        cell.execute();
        return IPython.version;
    });

    this.wait_for_output(0);

    // refactor this into  just a get_output(0)
    this.then(function () {
        var result = this.get_output_cell(0);
        this.test.assertEquals(result.text.trim(), jsver, 'IPython.version in JS matches server-side.');
    });
    
    // verify that requirejs loads the same CodeCell prototype at runtime as build time
    this.thenEvaluate(function () {
        require(['notebook/js/codecell'], function (codecell) {
            codecell.CodeCell.prototype.test = function () {
                return 'ok';
            }
            window._waitForMe = true;
        })
    })

    this.waitFor(function () {
        return this.evaluate(function () {
            return window._waitForMe;
        });
    })

    this.then(function () {
        var result = this.evaluate(function () {
            var cell = Jupyter.notebook.get_cell(0);
            return cell.test();
        });
        this.test.assertEquals(result, 'ok', "runtime-requirejs loads the same modules")
    })

});
