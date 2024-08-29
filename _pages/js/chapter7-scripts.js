let editor71 = initializeCodeMirror('codeMirrorEditor71', 'pythonCode71', 
`import time
def lazy_property(fn):
    attr_name = '_lazy_' + fn.__name__

    @property
    def _lazy_property(self):
        if not hasattr(self, attr_name): # if self has attr_name
            setattr(self, attr_name, fn(self)) # self[attr_name] = fn(self) self."abc"
        return getattr(self, attr_name) # return self[attr_name]

    return _lazy_property

class Country:
    def __init__(self, name, capital):
        self.name = name
        self.capital = capital
        # self.attr_name = "test"
    
    @lazy_property
    def cities(self):
        # expensive operation to get all the city names (API call)
        time.sleep(5)
        print("cities property is called")
        return ["city1", "city2"]


China = Country("China", "Beijing")
print(China.capital)
# beijing
print(China.cities)
# cities property is called
# ['city1', 'city2']`,
true);

let editor72 = initializeCodeMirror('codeMirrorEditor72', 'pythonCode72', 
`def square_numbers_with_loop(n):
    result = []
    for i in range(n):
        result.append(i * i)
    return result

%timeit square_numbers_with_loop(1000000)


def square_numbers_with_comprehension(n):
    return [i * i for i in range(n)]

%timeit square_numbers_with_comprehension(1000000)`,
true);