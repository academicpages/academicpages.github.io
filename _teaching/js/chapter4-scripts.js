let editor40 = initializeCodeMirror('codeMirrorEditor40', 'pythonCode40', 
`# function signature
def function_name([formal_parameters]):
# function body
    pass | return expr | yield expr
    
function_name([formal_parameters = arguments])`,
true);

let editor41 = initializeCodeMirror('codeMirrorEditor41', 'pythonCode41', 
`print(max(1, 2))
max = min
print(max(1, 2))`,
    true);

let editor42 = initializeCodeMirror('codeMirrorEditor42', 'pythonCode42', 
``,
true);

let editor43 = initializeCodeMirror('codeMirrorEditor43', 'pythonCode43', 
`def append_to(element, to=[]):
    to.append(element)
    return to
    
my_list = append_to(12)
print(my_list)

my_other_list = append_to(42)
print(my_other_list)`,
true);

let editor44 = initializeCodeMirror('codeMirrorEditor44', 'pythonCode44', 
`def f(x, y):
    return x + y

def g(x, y):
    return x * y
    
x1, x2, y1, y2 = 1, 2, 3, 4

print(g(f(x1, x2), f(y1, y2)))`,
true);

let editor45 = initializeCodeMirror('codeMirrorEditor45', 'pythonCode45', 
`import time

# late binding
def g():
    print(f'generator computing: gi_state: {g1.gi_running}')
    time.sleep(3)
    yield 1
    
g1 = g()
next(g1)
print("after, gi_state:", g1.gi_running)`,
true);

let editor46 = initializeCodeMirror('codeMirrorEditor46', 'pythonCode46', 
`# module.py
# define several algorithms and call them with a common function
def algo1(x):
	print("algorithm 1 computing")
	if x == 1:
		yhat = 1.1
	else:
		yhat = 1.2
	print("yhat1=", yhat)
	return
    
def algo2(x):
	print("algorithm 1 computing")
	if x == 1:
		yhat = 2.1
	else:
		yhat = 2.2
	print("yhat1=", yhat)
	return
    
def algo3(x):
    print("algorithm 1 computing")
    if x == 1:
    	yhat = 3.1
    else:
    	yhat = 3.2
    print("yhat1=", yhat)
    return

# main.py
x = 0
def ml(f):
	print(f"{f.__name__} invoked")
	ans = f(x)
	print("answer is", ans)
	return
    
ml(algo1)`,
true);

let editor47 = initializeCodeMirror('codeMirrorEditor47', 'pythonCode47', 
`# example from CS61A of UCB
def make_adder(n):
    def adder(k):
        return k + n
    return adder
    
add_three = make_adder(3)
print(add_three(5))`,
true);

let editor48 = initializeCodeMirror('codeMirrorEditor48', 'pythonCode48', 
`def print_all(x):
    print(x)
    return print_all`,
true);

let editor49 = initializeCodeMirror('codeMirrorEditor49', 'pythonCode49', 
`def corodecor(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs):
        cr.next()
        return cr
    return start

@corodecor
def genfunc():
    pass`,
true);

let editor410 = initializeCodeMirror('codeMirrorEditor410', 'pythonCode410', 
`from typing import NamedTuple
class Result(NamedTuple):
    count: int
    average: float

class Sentinel:
    def __repr__(self):
        return f'<Sentinel>'

STOP = Sentinel()

def average2():
    total = 0.0
    count = 0
    average = 0.0
    while True:
        term = yield
        print('received', term)
        if isinstance(term, Sentinel):
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)`,
true);

let editor411 = initializeCodeMirror('codeMirrorEditor411', 'pythonCode411', 
`# how yield works`,
true);

let editor412 = initializeCodeMirror('codeMirrorEditor412', 'pythonCode412', 
`def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = 5
result = factorial(number)
print(f"Factorial of {number} is {result}")`,
true);

let editor413 = initializeCodeMirror('codeMirrorEditor413', 'pythonCode413', 
`def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
number = 6
result = fibonacci(number)
print(f"Fibonacci number at position {number} is {result}")`,
true);

let editor414 = initializeCodeMirror('codeMirrorEditor414', 'pythonCode414', 
``,
true);