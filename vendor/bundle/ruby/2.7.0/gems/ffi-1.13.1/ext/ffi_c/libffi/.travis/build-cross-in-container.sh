#!/bin/bash

cd /opt

echo $PATH
export PATH=/usr/local/bin:$PATH
echo $PATH

./configure --host=${HOST} || cat */config.log
make
make dist
make check RUNTESTFLAGS="-a $RUNTESTFLAGS" || true


