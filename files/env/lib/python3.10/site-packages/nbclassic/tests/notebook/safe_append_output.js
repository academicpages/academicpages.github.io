//
// Test validation in append_output
//
// Invalid output data is stripped and logged.
//

casper.notebook_test(function () {
    // this.printLog();
    var messages = [];
    this.on('remote.message', function (msg) {
        messages.push(msg);
    });
    
    this.evaluate(function () {
        var cell = IPython.notebook.get_cell(0);
        cell.set_text( "dp = get_ipython().display_pub\n" +
                       "dp.publish({'text/plain' : '5', 'image/png' : 5})"
        );
        cell.execute();
    });

    this.wait_for_output(0);
    this.on('remote.message', function () {});

    this.then(function () {
        var output = this.get_output_cell(0);
        this.test.assert(messages.length > 0, "Captured log message");
        this.test.assertEquals(messages[messages.length-1].substr(0,26), "Invalid type for image/png", "Logged Invalid type message");
        this.test.assertEquals(output.data['image/png'], undefined, "Non-string png data was stripped");
        this.test.assertEquals(output.data['text/plain'], '5', "text data is fine");
    });
});
