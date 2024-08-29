let editor61 = initializeCodeMirror('codeMirrorEditor61', 'pythonCode61', 
    `import numpy as np
import pandas as pd

# index
arrays = [
   ["First", "First", "Second", "Second", "Third", "Third", "Fourth", "Fourth"],
   ["one", "two", "one", "two", "one", "two", "one", "two"],
]

index_arrays = [
    [1,1,1,2,2,2,2,3,3,4,4,4], # grade
    [1,2,3,1,2,3,4,1,2,1,2,3]  # class
]

myindex = pd.MultiIndex.from_arrays(arrays,
                                    names=["grade", "class"])

# data
data_class = np.arange(0, 16).reshape(8, 2)

df1 = pd.DataFrame(data_class,
                   index=myindex,
                   columns=["height", "weight"])`,
    true);


let editor62 = initializeCodeMirror('codeMirrorEditor62', 'pythonCode62', 
    `stacked = df1.stack()
print(stacked)

stacked.index

stacked.unstack(level=0)`,
    true);

let editor63 = initializeCodeMirror('codeMirrorEditor63', 'pythonCode63', 
    `from sklearn import datasets
import pandas as pd

iris = datasets.load_iris()

df2 = pd.DataFrame(iris.data, columns=iris.feature_names)

# dplyr pipeline
(
    irisdata
    .assign(
        sepal_ratio=irisdata["sepal_width"] / irisdata["sepal_length"],
        petal_ratio=lambda df: df.petal_width / df.petal_length,
    )
    .plot(kind="scatter", x="sepal_ratio", y="petal_ratio")
)`,
    true);

let editor64 = initializeCodeMirror('codeMirrorEditor64', 'pythonCode64', 
`data = {
   "value": range(12),
   "variable": ["A"] * 3 + ["B"] * 3 + ["C"] * 3 + ["D"] * 3,
   "date": pd.to_datetime(["2020-01-03","2020-01-04","2020-01-05"] * 4)
}

df3 = pd.DataFrame(data)

pivoted = df3.pivot_table(index="variable",
                          columns="date",
                          values="value")

pivoted = df3.pivot_table(index="date",
                          columns="variable",
                          values="value")
`,
true);

let editor65 = initializeCodeMirror('codeMirrorEditor65', 'pythonCode65', 
`messydata1 = pd.DataFrame({"name": ["John", "Jane", "Mary"],
                            "treatment1": [1, 4, 6],
                            "treatment2": [18, 1, 7]})

messydata1.melt(id_vars=["name"])`,
true);

let editor66 = initializeCodeMirror('codeMirrorEditor66', 'pythonCode66', 
`df4 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}, index=['a', 'b', 'c'])

df5 = pd.DataFrame({
    'B': [7, 8, 9],
    'C': [10, 11, 12]
}, index=['b', 'c', 'd'])

result = df4 + df5
print(result)`,
true);


let editor67 = initializeCodeMirror('codeMirrorEditor67', 'pythonCode67', 
`import pandas as pd

df6 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}, index=['a', 'b', 'c'])

print("Original DataFrame:")
print(df6)

df6.loc['b', ['A', 'C']] = [10, 30]

print("After misaligned assignment:")
print(df6)`,
true);


let editor68 = initializeCodeMirror('codeMirrorEditor68', 'pythonCode68', 
`data = {'A': ['foo', 'foo', 'bar', 'bar', 'baz'],
        'B': [1, 2, 3, 4, 5]}
df7 = pd.DataFrame(data)

df7.loc[:, ['B', 'A']] = df7[['A', 'B']]`,
true);