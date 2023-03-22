//
// Test binary messages on websockets.
// Only works on slimer for now, due to old websocket impl in phantomjs.
//

casper.notebook_test(function () {
    // create EchoBuffers target on js-side.
    // it just captures and echos comm messages.
    this.then(function () {
        var success = this.evaluate(function () {
            IPython._msgs = [];
        
            var EchoBuffers = function(comm) {
                this.comm = comm;
                this.comm.on_msg($.proxy(this.on_msg, this));
            };

            EchoBuffers.prototype.on_msg = function (msg) {
                IPython._msgs.push(msg);
                this.comm.send(msg.content.data, {}, {}, msg.buffers);
            };

            IPython.notebook.kernel.comm_manager.register_target("echo", function (comm) {
                return new EchoBuffers(comm);
            });
        
            return true;
        });
        this.test.assertEquals(success, true, "Created echo comm target");
    });

    // Create a similar comm that captures messages Python-side
    this.then(function () {
        var index = this.append_cell([
            "import os",
            "from ipykernel.comm.comm import Comm",
            "comm = Comm(target_name='echo')",
            "msgs = []",
            "def on_msg(msg):",
            "    msgs.append(msg)",
            "comm.on_msg(on_msg)"
        ].join('\n'), 'code');
        this.execute_cell(index);
    });
    
    // send a message with binary data
    this.then(function () {
        var index = this.append_cell([
            "buffers = [b'\\xFF\\x00', b'\\x00\\x01\\x02']",
            "comm.send(data='message 0', buffers=buffers)",
            "comm.send(data='message 1')",
            "comm.send(data='message 2', buffers=buffers)",
        ].join('\n'), 'code');
        this.execute_cell(index);
    });
    
    // wait for capture
    this.waitFor(function () {
        return this.evaluate(function () {
            return IPython._msgs.length >= 3;
        });
    });
    
    // validate captured buffers js-side
    this.then(function () {
        var msgs = this.evaluate(function () {
            return IPython._msgs;
        });
        this.test.assertEquals(msgs.length, 3, "Captured three comm messages");



        // check the messages came in the right order
        this.test.assertEquals(msgs[0].content.data, "message 0", "message 0 processed first");
        this.test.assertEquals(msgs[0].buffers.length, 2, "comm message 0 has two buffers");
        this.test.assertEquals(msgs[1].content.data, "message 1", "message 1 processed second");
        this.test.assertEquals(msgs[1].buffers.length, 0, "comm message 1 has no buffers");
        this.test.assertEquals(msgs[2].content.data, "message 2", "message 2 processed third");
        this.test.assertEquals(msgs[2].buffers.length, 2, "comm message 2 has two buffers");
        
        // extract attributes to test in evaluate,
        // because the raw DataViews can't be passed across
        var buf_info = function (message, index) {
            var buf = IPython._msgs[message].buffers[index];
            var data = {};
            data.byteLength = buf.byteLength;
            data.bytes = [];
            for (var i = 0; i < data.byteLength; i++) {
                data.bytes.push(buf.getUint8(i));
            }
            return data;
        };
        
        var msgs_with_buffers = [0, 2];
        for (var i = 0; i < msgs_with_buffers.length; i++) {
            msg_index = msgs_with_buffers[i];
            buf0 = this.evaluate(buf_info, msg_index, 0);
            buf1 = this.evaluate(buf_info, msg_index, 1);
            this.test.assertEquals(buf0.byteLength, 2, 'buf[0] has correct size in message '+msg_index);
            this.test.assertEquals(buf0.bytes, [255, 0], 'buf[0] has correct bytes in message '+msg_index);
            this.test.assertEquals(buf1.byteLength, 3, 'buf[1] has correct size in message '+msg_index);
            this.test.assertEquals(buf1.bytes, [0, 1, 2], 'buf[1] has correct bytes in message '+msg_index);
        }
    });
    
    // validate captured buffers Python-side
    this.then(function () {
        var index = this.append_cell([
            "assert len(msgs) == 3, len(msgs)",
            "bufs = msgs[0]['buffers']",
            "assert len(bufs) == len(buffers), bufs",
            "assert bufs[0].tobytes() == buffers[0], bufs[0]",
            "assert bufs[1].tobytes() == buffers[1], bufs[1]",
            "1",
        ].join('\n'), 'code');
        this.execute_cell(index);
        this.wait_for_output(index);
        this.then(function () {
            var out = this.get_output_cell(index);
            this.test.assertEquals(out.data['text/plain'], '1', "Python received buffers");
        });
    });
});
