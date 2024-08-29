let editor50 = initializeCodeMirror('codeMirrorEditor50', 'pythonCode50', 
    `class Student: 
    def __init__(self, name): 
        self.__name = name 
  
s1 = Student("Santhosh") 
s1.__name = "see"
s1.age = 20
print(s1.__name, s1._Student__name, s1.age)`,
    true);

let editor51 = initializeCodeMirror('codeMirrorEditor51', 'pythonCode51', 
    `class ML:
    data = {'x': [0, 1, 2, 3, 4],
            'y': [1, 2, 3, 4, 5]}
    
    def __init__(self, method):
        self.method = method

    def run(self):
        # you can access class attribute with self. A better way is to wrap self with type()
        print(f'{self.method}, a={self.data["x"]}, {id(self.data)}')
        
pca = ML('PCA')
pca.run()`,
    true);


let editor52 = initializeCodeMirror('codeMirrorEditor52', 'pythonCode52', 
    `def func():
    pass
    
print(dir(func))

class A:
    def __call__():
        print("called from A")

a = A()
    
print(A.__call__)`,
    true);


let editor53 = initializeCodeMirror('codeMirrorEditor53', 'pythonCode53', 
    `class Counter():
    def __init__(self):
        self.count = 0
    
    def __call__(self):
        self.count += 1
        
Counter()
c1 = Counter()
c2 = Counter()
print(c1.count, c2.count)
c1()

print(c1.count, c2.count)`,
    true);

let editor54 = initializeCodeMirror('codeMirrorEditor54', 'pythonCode54', 
    `@Counter
def timed_func():
    pass

timed_func()
timed_func()

timed_func.count`,
    true);

let editor55 = initializeCodeMirror('codeMirrorEditor55', 'pythonCode55', 
    `class Weather:
    def __init__(self, temp):
        self.temp = temp
        
w1 = Weather(-300)
print(f"today's temperature is {w1.temp} degrees")`,
    true);

let editor56 = initializeCodeMirror('codeMirrorEditor56', 'pythonCode56', 
    `class Weather:
    def __init__(self):
        pass
    
    def getter(self):
        try:
            return self.z
        except AttributeError:
            print("temperature not set")
    
    def setter(self, y):
        print("entering setter")
        if y > -275:
            self.z = y
        else:
            raise ValueError("too low")
            print('not allowed')
            
    temperature = property(getter, setter)`,
    true);


let editor57 = initializeCodeMirror('codeMirrorEditor57', 'pythonCode57', 
    `import time

class TimeDesc:
    def __get__(self, obj, objtype=None):
        return time.time()

class UseCase:
    size = TimeDesc()
    def __init__(self):
        pass`,
true);

let editor58 = initializeCodeMirror('codeMirrorEditor58', 'pythonCode58', 
    `class TempDesc:
    def __get__(self, instance, owner):
        try:
            return instance.z
        except Exception:
            print("Haven't set temperature.")
            
    def __set__(self, instance, value):
        if value > -273:
            instance.z = value
        else:
            print("not allowed.")
            
class NewTemp:
    temperature = TempDesc()`,
true);

let editor59 = initializeCodeMirror('codeMirrorEditor59', 'pythonCode59', 
    `import time

class LazyProperty:
    def __init__(self, function):
        self.function = function
        self.name = function.__name__

    def __get__(self, obj, type=None) -> object:
        print("here")
        obj.__dict__[self.name] = self.function(obj)
        return obj.__dict__[self.name]

class DeepThought:
    @LazyProperty
    def meaning_of_life(self):
        time.sleep(1)
        return 42`,
true);

let editor510 = initializeCodeMirror('codeMirrorEditor510', 'pythonCode510', 
    `class Student:
    def __init__(self):
        self.score = []
        
    def score_input(self, value):
        self.score.append(value)
        
    @staticmethod
    def grade(value):
        if 0 <= value < 60:
            return "fail"
        elif 60 <= value <90:
            return "pass"
        else:
            return "great"`,
true);

let editor511 = initializeCodeMirror('codeMirrorEditor511', 'pythonCode511', 
    `class Student:
    def __init__(self):
        self.score = []
        
    def score_input(self, value):
        self.score.append(value)
        
    @staticmethod
    def read(name, score):
        s = Student()
        s.score = score
        return s
    
class FirstYear(Student):
    pass`,
true);

let editor512 = initializeCodeMirror('codeMirrorEditor512', 'pythonCode512', 
    `import time
class Example:
    def __init__(self, ML):
        self.ML = ML
        
    @staticmethod
    def decor(func):
        def wrapper(*args, **kwargs):
            print(f"starting time: {time.time()}")
            func(*args, **kwargs)
            print(f"end execution, {time.time()}")
        return wrapper
        
    @decor
    def run(self):
        print(f'calling {self.ML}')
        time.sleep(1)
        return 0`,
true);

let editor513 = initializeCodeMirror('codeMirrorEditor513', 'pythonCode513', 
    `class A:
    def func():
        pass
    
    print(func)
    
print(A.func)
print(A().func)`,
true);

let editor514 = initializeCodeMirror('codeMirrorEditor514', 'pythonCode514', 
    `def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)`,
true);

let editor515 = initializeCodeMirror('codeMirrorEditor515', 'pythonCode515', 
    `class MLClass:
    def __init__(self, data):
        self.data = data
        
    def build_model(self):
        pass`,
true);

let editor516 = initializeCodeMirror('codeMirrorEditor516', 'pythonCode516', 
    `class NeuralNet():
    def __init__(self):
        super().__init__()

    def forward(self, x):
        pass
    
    def train_model(self, data, labels):
        pass`,
true);

let editor517 = initializeCodeMirror('codeMirrorEditor517', 'pythonCode517', 
    `class Parent:
    def __init__(self, x):
        print("this is", id(self))
        self.x = x

    def pmethod(self):
        print("from parent class")
        
class Child(Parent):
    def __init__(self, x, y):
        A = super()
        B = super()
        B.pmethod()
        print(id(A), id(B))
        A.__init__(x)
        self.y = y
        
B = Child(1, 2)
B.pmethod()
id(B)`,
true);

let editor518 = initializeCodeMirror('codeMirrorEditor518', 'pythonCode518', 
    `from abc import ABC, abstractmethod
class NeuralNet(ABC):
    @abstractmethod
    def __init__(self):
        super().__init__()

    @abstractmethod
    def forward(self, x):
        pass
    
    def train_model(self, data, labels):
        pass`,
true);

let editor519 = initializeCodeMirror('codeMirrorEditor519', 'pythonCode519', 
    `class DNN(NeuralNet):
    def __init__(self, input_size, hidden_size, output_size):
        super(DNN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x`,
true);

let editor520 = initializeCodeMirror('codeMirrorEditor520', 'pythonCode520', 
    `class MLClass:
    def __init__(self, data):
        self.data = data

class NeuralNet(MLClass):
    def __init__(self, data):
        super().__init__(data)

    def forward(self, x):
        pass

class Predictor(MLClass):
    def __init__(self, data, model=""):
        super().__init__(data)
        self.model = model
        
    def pred(self, x):
        print(f"{self.model} predicts at {x}")
        
class DNN(NeuralNet, Predictor):
    def __init__(self, data):
        super().__init__(data)


d1 = DNN(1, "model1")
d1.model`,
true);