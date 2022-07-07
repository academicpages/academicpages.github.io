---
date: 2022-06-19
tags:
- stream
- tools
title: Print item keys with jq
---

I can use `jq` to print the keys in an array of JSON objects quickly.
```bash
jq '.[0] | keys[]' $filename
```

I sometimes want to know the names of the keys on the objects in a dataset stored in JSON format, but if the JSON file is very large, it can be slow+consume lots of memory to read the whole with e.g. Python.

For example, when I download a dataset in the following format:

```json
[
	{
		"id": 1,
		"feat1": "foo",
		"feat2": "bar",
		"feat3": "baz",
	},
	{
		"id": 2,
		"feat1": "foo",
		"feat2": "bar",
		"feat3": "baz",
	},
	// 1,000,000,000 more items...
]
```

The tool will print out:
```bash
"id"
"feat1"
"feat2"
"feat3"
```

This comes in handy when I'm reproducing ML research code, where the implementation is mostly complete but needs some glue code to read the dataset and spit it into a different format. Enjoy!