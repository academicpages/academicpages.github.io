# We must redefine it in Py3k if it's not already there
def execfile(file, glob=None, loc=None):
    if glob is None:
        import sys
        glob = sys._getframe().f_back.f_globals
    if loc is None:
        loc = glob

    # It seems that the best way is using tokenize.open(): http://code.activestate.com/lists/python-dev/131251/
    # (but tokenize.open() is only available for python 3.2)
    import tokenize
    if hasattr(tokenize, 'open'):
        # version 3.2
        stream = tokenize.open(file)  # @UndefinedVariable
    else:
        # version 3.0 or 3.1
        detect_encoding = tokenize.detect_encoding(open(file, mode="rb").readline)
        stream = open(file, encoding=detect_encoding[0])
    try:
        contents = stream.read()
    finally:
        stream.close()

    # execute the script (note: it's important to compile first to have the filename set in debug mode)
    exec(compile(contents + "\n", file, 'exec'), glob, loc)
