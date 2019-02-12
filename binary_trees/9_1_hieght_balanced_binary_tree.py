'''
Problem: 
Given the root of a binary tree, check if the tree is height-balanced
Height-balanced: heights of the left and right subtree is at most one
'''
import collections

class Solution:

  # good structure for storing multiple values within a node without having to store in memory
  def is_balanced_binary_tree(self, node):
    BalancedStatusWithHeight = collections.namedtuple('BalancedStatusWithHeight', ('is_balanced','height')) 

    def check_balanced(node):
      if not node:
        return BalancedStatusWithHeight("True", -1) # base case 



    return check_balanced(node).is_balanced

s = Solution()
print(s.is_balanced_binary_tree(None))

'''
Learning something new every day about developing stuff for data structures like trees and junk lol
'''