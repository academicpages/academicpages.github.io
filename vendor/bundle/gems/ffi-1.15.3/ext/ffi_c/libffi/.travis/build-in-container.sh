#!/bin/bash

cd /opt

export QEMU_LD_PREFIX=/usr/${HOST}

./configure ${HOST+--host=$HOST --disable-shared}
make
make dist
make check RUNTESTFLAGS="-a $RUNTESTFLAGS" || true


