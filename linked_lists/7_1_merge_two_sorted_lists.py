'''
Problem:
Write a function that takes in two sorted linked lists and returns a merged, sorted linked list
'''

class ListNode:
  def __init__(self, val):
    self.val = val
    self.next = None

class Solution: 

  def merge_two_sorted_linked_lists(self, root1, root2):
    if not root1: 
      return root2 
    elif not root2:
      return root1

    mergedRoot = None 

    if root1.val > root2.val: 
      mergedRoot = ListNode(root2.val)
      root2 = root2.next 
    else:
      mergedRoot = ListNode(root1.val)
      root1 = root1.next 

    mergedNode = mergedRoot

    while root1 or root2: 
      if not root1: 
        while root2: 
          mergedNode.next = ListNode(root2.val)
          mergedNode = mergedNode.next 
          root2 = root2.next 
        break
      if not root2:
        while root1:
          mergedNode.next = ListNode(root1.val)
          mergedNode = mergedNode.next 
          root1 = root1.next
        break
      if root1.val > root2.val: 
        mergedNode.next = ListNode(root2.val)
        mergedNode = mergedNode.next 
        root2 = root2.next 
      else:
        mergedNode.next = ListNode(root1.val)
        mergedNode = mergedNode.next 
        root1 = root1.next 

    return mergedRoot 

root1 = ListNode(2)
root1.next = ListNode(5)
root1.next.next = ListNode(7)

root2 = ListNode(3)
root2.next = ListNode(11)

mRoot = Solution().merge_two_sorted_linked_lists(root1, root2) 
while mRoot: 
  print(mRoot.val)
  mRoot = mRoot.next

'''
Watch out for necessary BREAKS and incrementing after INITIALIZATION. Otherwise, good job!
'''