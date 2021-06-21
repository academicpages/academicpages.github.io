#
#
# Rules for verious lists.
# This file is just an example, you cannot compile this file.

class ExampleOnly
rule

# a list, which minimum number of items is 0
list0 :
          {
            result = []
          }
      | list0 item
          {
            result.push val[1]
          }

# a list, which minimum number of items is 1
list1 : item
          {
            result = val
          }
      | list1 item
          {
            result.push val[1]
          }

# a list, separated by comma
clist : item
          {
            result = val
          }
      | clist ',' item
          {
            result.push val[2]
          }

# a hash. see also "hash.y".
hash  : '{' hash_contents '}'
          {
            result = val[1]
          }
      | '{' '}'
          {
            result = {}
          }

hash_contents
      : item "=>" item
          {
            result = { val[0] => val[2] }
          }
      | hash_contents ',' item "=>" item
          {
            result[val[2]] = val[4]
          }
