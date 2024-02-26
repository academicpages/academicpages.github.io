declare function hasOwn<T extends {} = {}>(o: T, p: PropertyKey): p is keyof T;

export = hasOwn;