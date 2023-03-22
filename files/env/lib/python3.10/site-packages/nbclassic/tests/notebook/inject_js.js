//
// Test robustness about JS injection in different place
//
// This assume malicious document arrive to the frontend.
//

casper.notebook_test(function () {
    var messages = [];
    this.on('remote.alert', function (msg) {
        messages.push(msg);
    });
    
    this.evaluate(function () {
        var cell = IPython.notebook.get_cell(0);
        var json = cell.toJSON();
        json.execution_count = "<script> alert('hello from input prompts !')</script>";
        cell.fromJSON(json);
    });

    this.then(function () {
        this.test.assert(messages.length == 0, "Captured log message from script tag injection !");
    });
});
