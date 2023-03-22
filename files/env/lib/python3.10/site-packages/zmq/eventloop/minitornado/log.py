"""minimal subset of tornado.log for zmq.eventloop.minitornado"""

import logging

app_log = logging.getLogger("tornado.application")
gen_log = logging.getLogger("tornado.general")
