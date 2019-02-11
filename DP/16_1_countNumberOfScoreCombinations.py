'''
Given a set of tokens and an integer n, return the count of the number of combinations there are when adding up any number of tokens to be equal to n.
Assume each token in tokens is greater than 0 and n is also greater than 0.

Example: American football scoring combinations.
You can either score 2, 3, or 7 when scoring points. How many combinations of points can you make for some score n?

if n == 12, then output 4
combinations:
2 2 2 2 2 2 
2 2 2 3 3 
3 3 3 3 
2 3 7
'''

class Solution: 
  def countNumSolutions(self, tokens, n):
    counts_tokens_numbers = [[1] + [0] * n for _ in len(tokens)]


    for i in range(len(tokens)):
      for j in range(1, n+1, 1): 
        if i == 0: 
          





scoring = [2,3,7]
num_to_score = 12 

