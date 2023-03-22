
//
// Kernel tests
//
casper.notebook_test(function () {
    // test that the kernel is running
    this.then(function () {
        this.test.assert(this.kernel_running(), 'kernel is running');
    });

    // test list
    this.thenEvaluate(function () {
        IPython._kernels = null;
        IPython.notebook.kernel.list(function (data) {
            IPython._kernels = data;
        });
    });
    this.waitFor(function () {
        return this.evaluate(function () {
            return IPython._kernels !== null;
        });
    });
    this.then(function () {
        var num_kernels = this.evaluate(function () {
            return IPython._kernels.length;
        });
        this.test.assertEquals(num_kernels, 1, 'one kernel running');
    });
    
    // test get_info
    var kernel_info = this.evaluate(function () {
        return {
            name: IPython.notebook.kernel.name,
            id: IPython.notebook.kernel.id
        };
    });
    this.thenEvaluate(function () {
        IPython._kernel_info = null;
        IPython.notebook.kernel.get_info(function (data) {
            IPython._kernel_info = data;
        });
    });
    this.waitFor(function () {
        return this.evaluate(function () {
            return IPython._kernel_info !== null;
        });
    });
    this.then(function () {
        var new_kernel_info = this.evaluate(function () {
            return IPython._kernel_info;
        });
        this.test.assertEquals(kernel_info.name, new_kernel_info.name, 'kernel: name correct');
        this.test.assertEquals(kernel_info.id, new_kernel_info.id, 'kernel: id correct');
    });

    // test interrupt
    this.thenEvaluate(function () {
        IPython._interrupted = false;
        IPython.notebook.kernel.interrupt(function () {
            IPython._interrupted = true;
        });
    });
    this.waitFor(function () {
        return this.evaluate(function () {
            return IPython._interrupted;
        });
    });
    this.then(function () {
        var interrupted = this.evaluate(function () {
            return IPython._interrupted;
        });
        this.test.assert(interrupted, 'kernel was interrupted');
    });

    // test restart
    this.thenEvaluate(function () {
        IPython.notebook.kernel.restart();
    });
    this.waitFor(this.kernel_disconnected);
    this.wait_for_kernel_ready();
    this.then(function () {
        this.test.assert(this.kernel_running(), 'kernel restarted');
    });

    // test reconnect
    this.thenEvaluate(function () {
        IPython.notebook.kernel.stop_channels();
    });
    this.waitFor(this.kernel_disconnected);
    this.thenEvaluate(function () {
        IPython.notebook.kernel.reconnect();
    });
    this.wait_for_kernel_ready();
    this.then(function () {
        this.test.assert(this.kernel_running(), 'kernel reconnected');
    });

    // test kernel_info_request
    this.evaluate(function () {
        IPython.notebook.kernel.kernel_info(
            function(msg){
                IPython._kernel_info_response = msg;
            });
    });
    this.waitFor(
        function () {
            return this.evaluate(function(){
                return IPython._kernel_info_response;
        });
    });
    this.then(function () {
        var kernel_info_response =  this.evaluate(function(){
            return IPython._kernel_info_response;
        });
        this.test.assertTrue( kernel_info_response.msg_type === 'kernel_info_reply', 'Kernel info request return kernel_info_reply');
        this.test.assertTrue( kernel_info_response.content !== undefined, 'Kernel_info_reply is not undefined');
    });

    // test kill
    this.thenEvaluate(function () {
        IPython.notebook.kernel.kill();
    });
    this.waitFor(this.kernel_disconnected);
    this.then(function () {
        this.test.assert(!this.kernel_running(), 'kernel is not running');
    });

    // test start
    var url, base_url;
    this.then(function () {
        base_url = this.evaluate(function () {
            return IPython.notebook.base_url;
        });
        url = this.evaluate(function () {
            return IPython.notebook.kernel.start();
        });
    });
    this.then(function () {
        this.test.assertEquals(url, base_url + "api/kernels", "start url is correct");
    });
    this.wait_for_kernel_ready();
    this.then(function () {
        this.test.assert(this.kernel_running(), 'kernel is running');
    });

    // test start with parameters
    this.thenEvaluate(function () {
        IPython.notebook.kernel.kill();
    });
    this.waitFor(this.kernel_disconnected);
    this.then(function () {
        url = this.evaluate(function () {
            return IPython.notebook.kernel.start({foo: "bar"});
        });
    });
    this.then(function () {
        this.test.assertEquals(url, base_url + "api/kernels?foo=bar", "start url with params is correct");
    });
    this.wait_for_kernel_ready();
    this.then(function () {
        this.test.assert(this.kernel_running(), 'kernel is running');
    });

    // check for events in kill/start cycle
    this.event_test(
        'kill/start',
        [
            'kernel_killed.Kernel',
            'kernel_starting.Kernel',
            'kernel_created.Kernel',
            'kernel_connected.Kernel',
            'kernel_ready.Kernel'
        ],
        function () {
            this.thenEvaluate(function () {
                IPython.notebook.kernel.kill();
            });
            this.waitFor(this.kernel_disconnected);
            this.thenEvaluate(function () {
                IPython.notebook.kernel.start();
            });
        }
    );
    // wait for any last idle/busy messages to be handled
    this.wait_for_kernel_ready();

    // check for events in disconnect/connect cycle
    this.event_test(
        'reconnect',
        [
            'kernel_reconnecting.Kernel',
            'kernel_connected.Kernel',
        ],
        function () {
            this.thenEvaluate(function () {
                IPython.notebook.kernel.stop_channels();
                IPython.notebook.kernel.reconnect(1);
            });
        }
    );
    // wait for any last idle/busy messages to be handled
    this.wait_for_kernel_ready();

    // check for events in the restart cycle
    this.event_test(
        'restart',
        [
            'kernel_restarting.Kernel',
            'kernel_created.Kernel',
            'kernel_connected.Kernel',
            'kernel_ready.Kernel'
        ],
        function () {
            this.thenEvaluate(function () {
                IPython.notebook.kernel.restart();
            });
        }
    );
    // wait for any last idle/busy messages to be handled
    this.wait_for_kernel_ready();

    // check for events in the interrupt cycle
    this.event_test(
        'interrupt',
        [
            'kernel_interrupting.Kernel',
            'kernel_busy.Kernel',
            'kernel_idle.Kernel'
        ],
        function () {
            this.thenEvaluate(function () {
                IPython.notebook.kernel.interrupt();
            });
        }
    );
    this.wait_for_kernel_ready();

    // check for events after ws close
    this.event_test(
        'ws_closed_ok',
        [
            'kernel_disconnected.Kernel',
            'kernel_reconnecting.Kernel',
            'kernel_connected.Kernel',
            // note: there will be a 'busy' in here, too,
            // but we can't guarantee which will come first
            'kernel_idle.Kernel',
        ],
        function () {
            this.thenEvaluate(function () {
                IPython.notebook.kernel._ws_closed("", false);
            });
        }
    );
    // wait for any last idle/busy messages to be handled
    this.wait_for_kernel_ready();

    // check for events after ws close (error)
    this.event_test(
        'ws_closed_error',
        [
            'kernel_disconnected.Kernel',
            'kernel_connection_failed.Kernel',
            'kernel_reconnecting.Kernel',
            'kernel_connected.Kernel',
            'kernel_idle.Kernel',
        ],
        function () {
            this.thenEvaluate(function () {
                IPython.notebook.kernel._ws_closed("", true);
            });
        }
    );
    // wait for any last idle/busy messages to be handled
    this.wait_for_kernel_ready();

    // start the kernel back up
    this.thenEvaluate(function () {
        IPython.notebook.kernel.restart();
    });
    this.waitFor(this.kernel_running);
    this.wait_for_kernel_ready();

    // test handling of autorestarting messages
    this.event_test(
        'autorestarting',
        [
            'kernel_restarting.Kernel',
            'kernel_autorestarting.Kernel',
        ],
        function () {
            this.thenEvaluate(function () {
                var cell = IPython.notebook.get_cell(0);
                cell.set_text('import os\n' + 'os._exit(1)');
                cell.execute();
            });
        }
    );
    this.wait_for_kernel_ready();

    // test handling of failed restart
    this.event_test(
        'failed_restart',
        [
            'kernel_restarting.Kernel',
            'kernel_autorestarting.Kernel',
            'kernel_dead.Kernel'
        ],
        function () {
            this.thenEvaluate(function () {
                var cell = IPython.notebook.get_cell(0);
                cell.set_text("import os\n" +
                              "from ipykernel.connect import get_connection_file\n" +
                              "with open(get_connection_file(), 'w') as f:\n" +
                              "    f.write('garbage')\n" +
                              "os._exit(1)");
                cell.execute();
            });
        }, 

        // need an extra-long timeout, because it needs to try
        // restarting the kernel 5 times!
        20000
    );
});
