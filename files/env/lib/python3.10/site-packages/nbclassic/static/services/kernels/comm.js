// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

define([
    'jquery',
    'base/js/utils',
], function($, utils) {
    "use strict";

    //-----------------------------------------------------------------------
    // CommManager class
    //-----------------------------------------------------------------------
    
    var CommManager = function (kernel) {
        this.comms = {};
        this.targets = {};
        if (kernel !== undefined) {
            this.init_kernel(kernel);
        }
    };
    
    CommManager.prototype.init_kernel = function (kernel) {
        /**
         * connect the kernel, and register message handlers
         */
        this.kernel = kernel;
        var msg_types = ['comm_open', 'comm_msg', 'comm_close'];
        for (var i = 0; i < msg_types.length; i++) {
            var msg_type = msg_types[i];
            kernel.register_iopub_handler(msg_type, $.proxy(this[msg_type], this));
        }
    };

    CommManager.prototype.new_comm = function (target_name, data, callbacks, metadata, comm_id, buffers) {
        /**
         * Create a new Comm, register it, and open its Kernel-side counterpart
         * Mimics the auto-registration in `Comm.__init__` in the Jupyter Comm.
         *
         * argument comm_id is optional
         */
        var comm = new Comm(target_name, comm_id);
        this.register_comm(comm);
        comm.open(data, callbacks, metadata, buffers);
        return comm;
    };
    
    CommManager.prototype.register_target = function (target_name, f) {
        /**
         * Register a target function for a given target name
         */
        this.targets[target_name] = f;
    };
    
    CommManager.prototype.unregister_target = function (target_name, f) {
        /**
         * Unregister a target function for a given target name
         */
        delete this.targets[target_name];
    };
    
    CommManager.prototype.register_comm = function (comm) {
        /**
         * Register a comm in the mapping
         */
        this.comms[comm.comm_id] = Promise.resolve(comm);
        comm.kernel = this.kernel;
        return comm.comm_id;
    };
    
    CommManager.prototype.unregister_comm = function (comm) {
        /**
         * Remove a comm from the mapping
         */
        delete this.comms[comm.comm_id];
    };
    
    // comm message handlers
    
    CommManager.prototype.comm_open = function (msg) {
        var content = msg.content;
        var that = this;
        var comm_id = content.comm_id;

        this.comms[comm_id] = utils.load_class(content.target_name, content.target_module, 
            this.targets).then(function(target) {
                var comm = new Comm(content.target_name, comm_id);
                comm.kernel = that.kernel;
                try {
                    var response = target(comm, msg);
                } catch (e) {
                    comm.close();
                    that.unregister_comm(comm);
                    var wrapped_error = new utils.WrappedError("Exception opening new comm", e);
                    console.error(wrapped_error);
                    return Promise.reject(wrapped_error);
                }
                // Regardless of the target return value, we need to
                // then return the comm
                return Promise.resolve(response).then(function() {return comm;});
            }, utils.reject('Could not open comm', true));
        return this.comms[comm_id];
    };
    
    CommManager.prototype.comm_close = function(msg) {
        var content = msg.content;
        if (this.comms[content.comm_id] === undefined) {
            console.error('Comm promise not found for comm id ' + content.comm_id);
            return;
        }
        var that = this;
        this.comms[content.comm_id] = this.comms[content.comm_id].then(function(comm) {
            that.unregister_comm(comm);
            try {
                comm.handle_close(msg);
            } catch (e) {
                console.log("Exception closing comm: ", e, e.stack, msg);
            }
            // don't return a comm, so that further .then() functions
            // get an undefined comm input
        });
        return this.comms[content.comm_id];
    };
    
    CommManager.prototype.comm_msg = function(msg) {
        var content = msg.content;
        if (this.comms[content.comm_id] === undefined) {
            console.error('Comm promise not found for comm id ' + content.comm_id);
            return;
        }

        this.comms[content.comm_id] = this.comms[content.comm_id].then(function(comm) {
            return (Promise.resolve(comm.handle_msg(msg))
                .catch(utils.reject('Exception handling comm message'))
                .then(function() {return comm;}));
        });
        return this.comms[content.comm_id];
    };
    
    //-----------------------------------------------------------------------
    // Comm base class
    //-----------------------------------------------------------------------
    
    var Comm = function (target_name, comm_id) {
        this.target_name = target_name;
        this.comm_id = comm_id || utils.uuid();
        this._msg_callback = this._close_callback = null;
    };
    
    // methods for sending messages
    Comm.prototype.open = function (data, callbacks, metadata, buffers) {
        var content = {
            comm_id : this.comm_id,
            target_name : this.target_name,
            data : data || {},
        };
        return this.kernel.send_shell_message("comm_open", content, callbacks, metadata, buffers);
    };
    
    Comm.prototype.send = function (data, callbacks, metadata, buffers) {
        var content = {
            comm_id : this.comm_id,
            data : data || {},
        };
        return this.kernel.send_shell_message("comm_msg", content, callbacks, metadata, buffers);
    };

    Comm.prototype.close = function (data, callbacks, metadata, buffers) {
        var content = {
            comm_id : this.comm_id,
            data : data || {},
        };
        return this.kernel.send_shell_message("comm_close", content, callbacks, metadata, buffers);
    };
    
    // methods for registering callbacks for incoming messages
    Comm.prototype._register_callback = function (key, callback) {
        this['_' + key + '_callback'] = callback;
    };
    
    Comm.prototype.on_msg = function (callback) {
        this._register_callback('msg', callback);
    };
    
    Comm.prototype.on_close = function (callback) {
        this._register_callback('close', callback);
    };
    
    // methods for handling incoming messages
    
    Comm.prototype._callback = function (key, msg) {
        var callback = this['_' + key + '_callback'];
        if (callback) {
            try {
                return callback(msg);
            } catch (e) {
                console.log("Exception in Comm callback", e, e.stack, msg);
            }
        }
    };
    
    Comm.prototype.handle_msg = function (msg) {
        return this._callback('msg', msg);
    };
    
    Comm.prototype.handle_close = function (msg) {
        this._callback('close', msg);
    };
    
    return {
        'CommManager': CommManager,
        'Comm': Comm
    };
});
