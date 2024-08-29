let editor1 = initializeCodeMirror('codeMirrorEditor1', 
    'pythonCode1', 
    `#%%
def print_sum(x):
    print(x)
    def next_sum(y):
        return print_sum(x+y)
    return next_sum1

print_sum(1)(3)(5)`,
    true);

let editor2 = initializeCodeMirror('codeMirrorEditor2', 
    'pythonCode2', 
    `-----------------------------------------------------------------------
NameError                             Traceback (most recent call last)
File \\Python bootcamp\\exception_example.py:8
      5         return print_sum(x+y)
      6     return next_sum1
----> 8 print_sum(1)(3)(5)

File \\Python bootcamp\\exception_example.py:6
      4 def next_sum(y):
      5     return print_sum(x+y)
----> 6 return next_sum1

NameError: name 'next_sum1' is not defined`,
    false);

let editor11 = initializeCodeMirror('codeMirrorEditor11', 
    'pythonCode11', 
    `#%%
class Exception1(Exception):
    pass

class Exception2(Exception):
    pass

class Exception3(Exception):
    pass

for cls in [Exception1, Exception2, Exception3]:
    try:
        raise cls()
    except Exception3:
        print("Exception 3 occured! What'd I do???")
    except Exception2:
        print("Exception 2 occured! What'd I do???")
    except Exception1:
        print("Exception 1 occured! What'd I do???")`,
    true);