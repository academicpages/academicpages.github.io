# tdbcConfig.sh --
#
# This shell script (for sh) is generated automatically by TDBC's configure
# script. It will create shell variables for most of the configuration options
# discovered by the configure script. This script is intended to be included
# by the configure scripts for TDBC extensions so that they don't have to
# figure this all out for themselves.
#
# The information in this file is specific to a single platform.
#
# RCS: @(#) $Id$

# TDBC's version number
tdbc_VERSION=1.1.3
TDBC_VERSION=1.1.3

# Name of the TDBC library - may be either a static or shared library
tdbc_LIB_FILE=libtdbc1.1.3.dylib
TDBC_LIB_FILE=libtdbc1.1.3.dylib

# String to pass to the linker to pick up the TDBC library from its build dir
tdbc_BUILD_LIB_SPEC="-L/private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_c011255d-355d-4e10-9d06-2a364b791019h2p45nxx/croots/recipe/tk_1654088770111/work/tcl8.6.12/unix/pkgs/tdbc1.1.3 -ltdbc1.1.3"
TDBC_BUILD_LIB_SPEC="-L/private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_c011255d-355d-4e10-9d06-2a364b791019h2p45nxx/croots/recipe/tk_1654088770111/work/tcl8.6.12/unix/pkgs/tdbc1.1.3 -ltdbc1.1.3"

# String to pass to the linker to pick up the TDBC library from its installed
# dir.
tdbc_LIB_SPEC="-L/Users/drew/siwelwerd.github.io/files/env/lib/tdbc1.1.3 -ltdbc1.1.3"
TDBC_LIB_SPEC="-L/Users/drew/siwelwerd.github.io/files/env/lib/tdbc1.1.3 -ltdbc1.1.3"

# Name of the TBDC stub library
tdbc_STUB_LIB_FILE="libtdbcstub1.1.3.a"
TDBC_STUB_LIB_FILE="libtdbcstub1.1.3.a"

# String to pass to the linker to pick up the TDBC stub library from its
# build directory
tdbc_BUILD_STUB_LIB_SPEC="-L/private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_c011255d-355d-4e10-9d06-2a364b791019h2p45nxx/croots/recipe/tk_1654088770111/work/tcl8.6.12/unix/pkgs/tdbc1.1.3 -ltdbcstub1.1.3"
TDBC_BUILD_STUB_LIB_SPEC="-L/private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_c011255d-355d-4e10-9d06-2a364b791019h2p45nxx/croots/recipe/tk_1654088770111/work/tcl8.6.12/unix/pkgs/tdbc1.1.3 -ltdbcstub1.1.3"

# String to pass to the linker to pick up the TDBC stub library from its
# installed directory
tdbc_STUB_LIB_SPEC="-L/Users/drew/siwelwerd.github.io/files/env/lib/tdbc1.1.3 -ltdbcstub1.1.3"
TDBC_STUB_LIB_SPEC="-L/Users/drew/siwelwerd.github.io/files/env/lib/tdbc1.1.3 -ltdbcstub1.1.3"

# Path name of the TDBC stub library in its build directory
tdbc_BUILD_STUB_LIB_PATH="/private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_c011255d-355d-4e10-9d06-2a364b791019h2p45nxx/croots/recipe/tk_1654088770111/work/tcl8.6.12/unix/pkgs/tdbc1.1.3/libtdbcstub1.1.3.a"
TDBC_BUILD_STUB_LIB_PATH="/private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_c011255d-355d-4e10-9d06-2a364b791019h2p45nxx/croots/recipe/tk_1654088770111/work/tcl8.6.12/unix/pkgs/tdbc1.1.3/libtdbcstub1.1.3.a"

# Path name of the TDBC stub library in its installed directory
tdbc_STUB_LIB_PATH="/Users/drew/siwelwerd.github.io/files/env/lib/tdbc1.1.3/libtdbcstub1.1.3.a"
TDBC_STUB_LIB_PATH="/Users/drew/siwelwerd.github.io/files/env/lib/tdbc1.1.3/libtdbcstub1.1.3.a"

# Location of the top-level source directories from which TDBC was built.
# This is the directory that contains doc/, generic/ and so on.  If TDBC
# was compiled in a directory other than the source directory, this still
# points to the location of the sources, not the location where TDBC was
# compiled.
tdbc_SRC_DIR="/private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_c011255d-355d-4e10-9d06-2a364b791019h2p45nxx/croots/recipe/tk_1654088770111/work/tcl8.6.12/pkgs/tdbc1.1.3"
TDBC_SRC_DIR="/private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_c011255d-355d-4e10-9d06-2a364b791019h2p45nxx/croots/recipe/tk_1654088770111/work/tcl8.6.12/pkgs/tdbc1.1.3"

# String to pass to the compiler so that an extension can find installed TDBC
# headers
tdbc_INCLUDE_SPEC="-I/Users/drew/siwelwerd.github.io/files/env/include"
TDBC_INCLUDE_SPEC="-I/Users/drew/siwelwerd.github.io/files/env/include"

# String to pass to the compiler so that an extension can find TDBC headers
# in the source directory
tdbc_BUILD_INCLUDE_SPEC="-I/private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_c011255d-355d-4e10-9d06-2a364b791019h2p45nxx/croots/recipe/tk_1654088770111/work/tcl8.6.12/pkgs/tdbc1.1.3/generic"
TDBC_BUILD_INCLUDE_SPEC="-I/private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_c011255d-355d-4e10-9d06-2a364b791019h2p45nxx/croots/recipe/tk_1654088770111/work/tcl8.6.12/pkgs/tdbc1.1.3/generic"

# Path name where .tcl files in the tdbc package appear at run time.
tdbc_LIBRARY_PATH="/Users/drew/siwelwerd.github.io/files/env/lib/tdbc1.1.3"
TDBC_LIBRARY_PATH="/Users/drew/siwelwerd.github.io/files/env/lib/tdbc1.1.3"

# Path name where .tcl files in the tdbc package appear at build time.
tdbc_BUILD_LIBRARY_PATH="/private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_c011255d-355d-4e10-9d06-2a364b791019h2p45nxx/croots/recipe/tk_1654088770111/work/tcl8.6.12/pkgs/tdbc1.1.3/library"
TDBC_BUILD_LIBRARY_PATH="/private/var/folders/nz/j6p8yfhx1mv_0grj5xl4650h0000gp/T/abs_c011255d-355d-4e10-9d06-2a364b791019h2p45nxx/croots/recipe/tk_1654088770111/work/tcl8.6.12/pkgs/tdbc1.1.3/library"

# Additional flags that must be passed to the C compiler to use tdbc
tdbc_CFLAGS=
TDBC_CFLAGS=

