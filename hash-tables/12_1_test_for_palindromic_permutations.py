'''
Problem: 
Write a program to test whether the letters forming a string can be permuted to form a palindrome. 

Solution: 
Throw the string into a hash table. Each character is a key and the value is the counts of each char.
We will have a palindrome if there is at most one odd-count character 
'''
from collections import Counter

class Solution:

  def is_palindromic(self, s): 
    c_counts = Counter()

    for c in s: 
      c_counts[c] += 1 

    num_odd_counts = 0 

    for c_count in c_counts.values():
      if c_count % 2 != 0: 
        num_odd_counts += 1 

    if num_odd_counts > 1:
      return False 
    return True


s = Solution() 

print(s.is_palindromic("edified"))