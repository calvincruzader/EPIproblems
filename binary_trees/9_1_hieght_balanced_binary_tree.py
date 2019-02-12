'''
Problem: 
Given the root of a binary tree, check if the tree is height-balanced
Height-balanced: heights of the left and right subtree is at most one
'''
import collections

class TreeNode: 
  def __init__(self, val):
    self.val, self.left, self.right = val, None, None

class Solution:

  # good structure for storing multiple values within a node without having to store in memory
  def is_balanced_binary_tree(self, node):
    BalancedStatusWithHeight = collections.namedtuple('BalancedStatusWithHeight', ('is_balanced','height')) 

    def check_balanced(node):
      if not node:
        return BalancedStatusWithHeight("True", -1) # base case 

      # subtle interaction here between the nested function and the provided struct 
      # we reference the values of height AND the solution to our problem in this structure,
      # then forget about the value when we're done with it, subtle. but amazing.
      left_result = check_balanced(node.left)
      if not left_result.is_balanced: 
        return BalancedStatusWithHeight("False", 0)

      right_result = check_balanced(node.right)
      if not right_result.is_balanced:
        return BalancedStatusWithHeight("False", 0)

      height_result = abs(left_result.height - right_result.height) 
      print("height_result: {}".format(height_result))
      if height_result > 1: 
        return BalancedStatusWithHeight("False", height_result + 1)
      else: 
        return BalancedStatusWithHeight("True", height_result + 1)


    return check_balanced(node).is_balanced


root = TreeNode(1)

root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(3)

root.right = TreeNode(5)
root.right.left = TreeNode(9)
root.right.right = TreeNode(10)
root.right.right.right = TreeNode(234)
root.right.right.right.right = TreeNode(5455)
# root.right.right.right.right.right = TreeNode(45)

s = Solution()
print(s.is_balanced_binary_tree(root))


'''
Learning something new every day about developing stuff for data structures like trees and junk lol
Given this info, I can figure out how to solve from here optimally. 
  - Get the correct thought pattern first with hints given and then implement a solution ! 
'''