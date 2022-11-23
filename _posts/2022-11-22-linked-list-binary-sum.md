---
title: '#1290'
date: 2022-11-22
permalink: /posts/2022/11/linked-list-binary-sum/
tags:
  - LeetCode
  - LinkedList
  - Easy
  - Python
---

# #1290
## <font color='green'>**Find the sums of binary in the linked list.**</font>

```python
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
```

## <u>Assume there are a linked list given that contains binary numbers.</u>

```python
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        sums = 0 # sums that will be return of sums

        while head: # iterate through the linked list
            sums = sums * 2 + head.val # update sums each value of binary and multiply 2
            head = head.next # update the head to next head

        return sums
```

## It was a good time to learn how to handle the linked list in Python from this problem.