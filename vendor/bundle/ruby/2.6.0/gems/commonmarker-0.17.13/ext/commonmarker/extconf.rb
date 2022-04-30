require 'mkmf'

$CFLAGS << " -std=c99"

create_makefile('commonmarker/commonmarker')
