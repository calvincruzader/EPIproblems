'''
Problem: 
Write a program that validates the BST property
'''
from collections import namedtuple

class TreeNode: 
  def __init__(self, val):
    self.val, self.left, self.right = val, None, None

class Solution: 

  def check_BST_property(self, root): 
    isBST_and_maxVal = namedtuple('isBST_and_maxVal', ('isBST', 'maxVal'))

    def check_BST_property_helper(node): 

      if not node: 
        return isBST_and_maxVal(True, None)
      # print("hmmmm")
      left_subtree = check_BST_property_helper(node.left)
      right_subtree = check_BST_property_helper(node.right)

      if not (left_subtree.isBST if left_subtree else False) or \
      not (right_subtree.isBST if right_subtree else False):
        return isBST_and_maxVal(False, -1)

      # print(node.val)
      print("{} {} {}".format(node.val, left_subtree.maxVal, right_subtree.maxVal))
      if ((left_subtree.maxVal > node.val) if left_subtree.maxVal else False) or \
      ((right_subtree.maxVal < node.val) if right_subtree.maxVal else False):
        print("should get here once at node 2. node val: {}".format(node.val))
        return isBST_and_maxVal(False, -1)

      outputVal = right_subtree.maxVal if right_subtree else node.val 

      return isBST_and_maxVal(True, outputVal)

    return check_BST_property_helper(root)

my_root = TreeNode(5)
my_root.left = TreeNode(3)
my_root.left.left = TreeNode(1)
my_root.left.right = TreeNode(4)
my_root.right = TreeNode(7)
my_root.right.right = TreeNode(2)

s = Solution()
print(s.check_BST_property(my_root))

