/* some troubles with vows
   here is some mocha test

 npm install  
 mocha tests/netmask.js
*/
var assert = require('assert');

var Netmask = require('../').Netmask;

var block = new Netmask('10.1.2.0/24');
var b1 = new Netmask('10.1.2.10/29');
var b2 = new Netmask('10.1.2.10/31');
var b3 = new Netmask('10.1.2.20/32');

 console.log('first : '+b2.base);
 console.log('broadcast : '+b2.broadcast);
 console.log('last : ' + b2.last);

describe("Netmask contains bug", function() {
  assert.equal(block.contains(b1),true);
  assert.equal(block.contains(b2),true);
  assert.equal(block.contains(b3),true);
});
