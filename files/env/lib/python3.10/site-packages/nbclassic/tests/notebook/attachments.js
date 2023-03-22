//
// Test cell attachments
//
var fs = require('fs');
casper.notebook_test(function () {
    // -- Test the Edit->Insert Image menu to insert new attachments
    "use strict";
    casper.test.info("Testing attachments insertion through the menuitem");

    this.viewport(1024, 768);

    // Click on menuitem
    var selector = '#insert_image > a';
    this.waitForSelector(selector);
    this.thenEvaluate(function(sel) {
        Jupyter.notebook.to_markdown();
        var cell = Jupyter.notebook.get_selected_cell();
        cell.set_text("");
        cell.unrender();

        $(sel).click();
    }, selector);
    // Wait for the dialog to be shown
    this.waitUntilVisible(".modal-body");
    this.wait(200);

    // Select the image file to insert

    // For some reason, this doesn't seem to work in a reliable way in
    // phantomjs. So we manually set the input's files attribute
    //this.page.uploadFile('.modal-body input[name=file]', 'test.png')
    this.then(function() {
        var fname = 'nbclassic/tests/_testdata/black_square_22.png';
        if (!fs.exists(fname)) {
            this.test.fail(
                " does not exist, are you running the tests " +
                "from the root directory ? "
            );
        }
        this.fill('form#insert-image-form', {'file': fname});
    });

    // Validate and render the markdown cell
    this.thenClick('#btn_ok');
    this.thenEvaluate(function() {
        Jupyter.notebook.get_cell(0).render();
    });
    this.wait(300);
    // Check that an <img> tag has been inserted and that it contains the
    // image
    this.then(function() {
        var img = this.evaluate(function() {
            var cell = Jupyter.notebook.get_cell(0);
            var img = $("div.text_cell_render").find("img");
            return {
                src: img.attr("src"),
                width: img.width(),
                height: img.height(),
            };
        });
        this.test.assertType(img, "object", "Image('image/png')");
        this.test.assertEquals(img.src.split(',')[0],
                               "data:image/png;base64",
                               "Image data-uri prefix");
        this.test.assertEquals(img.width, 2, "width == 2");
        this.test.assertEquals(img.height, 2, "height == 2");
    });

    //this.then(function() {
        //this.capture('test.png');
    //});

    // -- Use the Edit->Copy/Paste Cell Attachments menu items
    selector = '#copy_cell_attachments > a';
    this.waitForSelector(selector);
    this.thenClick(selector);

    // append a new cell
    this.append_cell('', 'markdown');
    this.thenEvaluate(function() {
        Jupyter.notebook.select_next();
    });

    // and paste the attachments into it
    selector = '#paste_cell_attachments > a';
    this.waitForSelector(selector);
    this.thenClick(selector);

    // check that the new cell has attachments
    this.then(function() {
        var cell_attachments = this.evaluate(function() {
            return Jupyter.notebook.get_selected_cell().attachments;
        });
        var orig_cell_attachments = this.evaluate(function() {
            return Jupyter.notebook.get_cell(0).attachments;
        });
        // Check that the two cells have the same attachments
        this.test.assertEquals(cell_attachments, orig_cell_attachments,
                               "pasted attachments ok");
    });

    // copy/paste cell includes attachments
    selector = '#copy_cell > a';
    this.waitForSelector(selector);
    this.thenClick(selector);

    selector = '#paste_cell_below > a';
    this.waitForSelector(selector);
    this.thenClick(selector);

    // check that the new cell has attachments
    this.then(function() {
        var cell_attachments = this.evaluate(function() {
            return Jupyter.notebook.get_selected_cell().attachments;
        });
        var orig_cell_attachments = this.evaluate(function() {
            return Jupyter.notebook.get_cell(0).attachments;
        });
        // Check that the two cells have the same attachments
        this.test.assertEquals(cell_attachments, orig_cell_attachments,
                               "pasted cell has attachments");
    });

    var nbname = 'attachments_test.ipynb';
    this.thenEvaluate(function(nbname) {
        Jupyter.notebook.set_notebook_name(nbname);
    }, {nbname:nbname});

    // -- Save the notebook. This should cause garbage collection for the
    // second cell (since we just pasted the attachments but there is no
    // markdown referencing them)
    this.thenEvaluate(function(nbname) {
        Jupyter._checkpoint_created = false;
        require(['base/js/events'], function (events) {
            events.on('checkpoint_created.Notebook', function (evt, data) {
                Jupyter._checkpoint_created = true;
            });
        });

        Jupyter.notebook.save_checkpoint();
    }, {nbname:nbname});

    this.waitFor(function () {
        return this.evaluate(function(){
            return Jupyter._checkpoint_created;
        });
    });

    this.then(function(){
        this.open_dashboard();
    });


    this.then(function(){
        var notebook_url = this.evaluate(function(nbname){
            var escaped_name = encodeURIComponent(nbname);
            var return_this_thing = null;
            $("a.item_link").map(function (i,a) {
                if (a.href.indexOf(escaped_name) >= 0) {
                    return_this_thing = a.href;
                    return;
                }
            });
            return return_this_thing;
        }, {nbname:nbname});
        this.test.assertNotEquals(notebook_url, null, "Escaped URL in notebook list");
        // open the notebook
        this.open(notebook_url);
    });

    // wait for the notebook
    this.waitFor(this.kernel_running);
    this.waitFor(function() {
        return this.evaluate(function () {
            return Jupyter && Jupyter.notebook && true;
        });
    });

    this.then(function() {
        var cell0 = this.evaluate(function() {
            return Jupyter.notebook.get_cell(0);
        });
        var cell1 = this.evaluate(function() {
            return Jupyter.notebook.get_cell(1);
        });
        this.test.assert('black_square_22.png' in cell0.attachments,
                         'cell0 has kept its attachments');
        this.test.assertEquals(Object.keys(cell1.attachments).length, 0,
                               'cell1 attachments have been garbage collected');
    });
});

