//
// Various tagging
//

casper.notebook_test(function () {
    
    function get_tag_metadata () {
        return casper.evaluate(function () {
            return Jupyter.notebook.get_cell(0).metadata.tags;
        });
    }
    
    function get_tag_elements () {
        return casper.evaluate(function () {
            var cell = Jupyter.notebook.get_cell(0);
            return $.map(
                cell.element.find('.cell-tag'),
                function (el) {
                    return $(el.childNodes[0]).text();
                }
            );
        })
    }
    // wait for cell toolbar item to be present (necessary?)
    this.waitFor(function () {
        return this.evaluate(function() {
            return $('#menu-cell-toolbar-submenu')
                    .find('[data-name=Tags]')
                    .length;
        });
    });
    this.then(function () {
        var tag_items = this.evaluate(function() {
            return $('#menu-cell-toolbar-submenu')
                    .find('[data-name=Tags]')
                    .length;
        });
        this.test.assertEquals(
            tag_items,
            1,
            "Tag cell toolbar item is present");
    })
    
    // activate tags toolbar via menubar
    this.thenEvaluate(function () {
        $('#menu-cell-toolbar-submenu')
            .find('[data-name=Tags]')
            .find('a')
            .click();
    });
    
    // wait for one tag container
    this.waitForSelector('.tags_button_container');
    this.then(function () {
        var elements = this.evaluate(function () {
            var cell = Jupyter.notebook.get_cell(0);
            var tag_input = cell.element
                .find('.tags-input input');
            return tag_input.length;
        })
        this.test.assertEquals(
            elements,
            1,
            "tags-input element exists");
    })

    // apply some tags
    this.thenEvaluate(function () {
        var cell = Jupyter.notebook.get_cell(0);
        var tag_input = cell.element
            .find('.tags-input input');
        // add some tags separated by commas and spaces,
        // including duplicates
        tag_input.val('tag1, tüg2 tåg3,tag4,,,tag5 tag1');
        cell.element
            .find('.tags-input button')
            .click();
    });
    
    var all_tags = ['tag1', 'tüg2', 'tåg3', 'tag4', 'tag5'];
    // verify that tags are applied
    this.then(function () {
        var tags = get_tag_metadata();
        this.test.assertEquals(
            tags,
            all_tags,
            "tags have been applied to metadata"
        );

        var tag_elements = get_tag_elements();
        this.test.assertEquals(
            tag_elements,
            all_tags,
            "tags elements have been added"
        );
    });

    // remove first tag by clicking 'X'
    this.thenEvaluate(function () {
        var cell = Jupyter.notebook.get_cell(0);
        var X = cell.element
            .find('.tag-container .remove-tag-btn')
            .first();
        X.click();
    });

    this.then(function () {
        var expected_tags = all_tags.slice(1);
        var tags = get_tag_metadata();
        this.test.assertEquals(
            tags,
            expected_tags,
            "clicking X removes tags from metadata"
        );

        var tag_elements = get_tag_elements();
        this.test.assertEquals(
            tag_elements,
            expected_tags,
            "clicking X removes tags from UI"
        );
    })
});
