import inspect
import os
import sys
import traceback
import unittest

start_dir = sys.argv[1]
pattern = sys.argv[2]
top_level_dir = sys.argv[3] if len(sys.argv) >= 4 else None
sys.path.insert(0, os.getcwd())


def get_sourceline(obj):
    try:
        s, n = inspect.getsourcelines(obj)
    except:
        try:
            # this handles `tornado` case we need a better
            # way to get to the wrapped function.
            # This is a temporary solution
            s, n = inspect.getsourcelines(obj.orig_method)
        except:
            return "*"

    for i, v in enumerate(s):
        if v.strip().startswith(("def", "async def")):
            return str(n + i)
    return "*"


def generate_test_cases(suite):
    for test in suite:
        if isinstance(test, unittest.TestCase):
            yield test
        else:
            for test_case in generate_test_cases(test):
                yield test_case


try:
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir, pattern=pattern, top_level_dir=top_level_dir)

    print("start")  # Don't remove this line
    loader_errors = []
    for s in generate_test_cases(suite):
        tm = getattr(s, s._testMethodName)
        testId = s.id()
        if testId.startswith("unittest.loader._FailedTest"):
            loader_errors.append(s._exception)
        else:
            print(testId.replace(".", ":") + ":" + get_sourceline(tm))
except:
    print("=== exception start ===")
    traceback.print_exc()
    print("=== exception end ===")


for error in loader_errors:
    try:
        print("=== exception start ===")
        print(error.msg)
        print("=== exception end ===")
    except:
        pass
