
let editor31 = initializeCodeMirror('codeMirrorEditor31', 
    'pythonCode31', 
    `n = 1
print(id(n))
n += 1
print(id(n))`,
    true);

let editor32 = initializeCodeMirror('codeMirrorEditor32', 
        'pythonCode32', 
        `x = 5 # name 'x' refers to value 5`,
        true);

let editor33 = initializeCodeMirror('codeMirrorEditor33', 
    'pythonCode33', 
    `a = [1, 2, 3] # changes are visible through all names
b = a # how about x, y = 257, 257?
b[0] = 4 # mutate`,
    true);

let editor34 = initializeCodeMirror('codeMirrorEditor34', 
    'pythonCode34', 
    `x = 'hello' # changes that not apply inplace
y = x
print(id(x), id(y))
x = x + 'there' # rebind
print(id(x), id(y))`,
    true);

let editor35 = initializeCodeMirror('codeMirrorEditor35', 
        'pythonCode35', 
        `def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)`,
        true);

let editor36 = initializeCodeMirror('codeMirrorEditor36', 
    'pythonCode36', 
    `x, y = 1, 2
x += 2
x += y
print(x + y)
print(x.__radd__(y)) # int is immutable
print(x) # how about list?`,
    true);

let editor37 = initializeCodeMirror('codeMirrorEditor37', 
    'pythonCode37', 
    `x = 1
# in a for loop
for x in range(5):
    pass
# class definitions
class X:
    pass
# function names
def func():
    pass
# function arguments
def func(x):
    pass
# import statements
import numpy

from pandas import DataFrame # etc.`,
    true);

let freeeditor31 = initializeCodeMirror('codeMirrorEditor399', 
    'pythonCode399', 
    `for k, v in globals().items():
    print(k, ':', v)`,
    true);

let freeeditor32 = initializeCodeMirror('codeMirrorEditor398', 
    'pythonCode398', 
    `class A:
    a = 42
    b = a`,
    true);

let freeeditor33 = initializeCodeMirror('codeMirrorEditor397', 
    'pythonCode397', 
    `a
f.__name__
lst[1]
lst[1:3]
range(5)`,
    true);

let freeeditor34 = initializeCodeMirror('codeMirrorEditor396', 
    'pythonCode396', 
    `a, b, c = 1, 2, 1
a < b > c`,
    true);


let freeeditor35 = initializeCodeMirror('codeMirrorEditor395', 
    'pythonCode395', 
    `class Foo:
    def __eq__(self, other):
        return True
        
f = Foo()
print(f == None)
print(f is None)`,
    true);

let freeeditor38 = initializeCodeMirror('codeMirrorEditor38', 
'pythonCode38', 
`outer_list = ['a', 'b', 'c']
def func(lst):
    print(id(lst))
    lst.append('d')
    print(id(lst))`,
true);

let freeeditor39 = initializeCodeMirror('codeMirrorEditor39', 
'pythonCode39', 
`def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError as e:
        print("Caught a division by zero error.")
        # Re-raise the original exception
        raise

try:
    divide(10, 0)
except Exception as e:
    print(f"Exception re-raised: {e}")`,
true);