#
# Tcl package index file
#
# Note sqlite*3* init specifically
#
if {[package vsatisfies [package provide Tcl] 9.0-]} {
    package ifneeded sqlite3 3.36.0 \
	    [list load [file join $dir libtcl9sqlite3.36.0.dylib] Sqlite3]
} else {
    package ifneeded sqlite3 3.36.0 \
	    [list load [file join $dir libsqlite3.36.0.dylib] Sqlite3]
}
