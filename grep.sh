#!/bin/bash
grep --color=always -r "$1" --exclude-dir={_site,.*} --exclude=*.svg
