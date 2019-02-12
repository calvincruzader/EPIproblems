
class Solution: 

  def str_to_int(self, my_s):
    output = 0 
    isNegative = my_s[0] == '-'

    startingIdx = 1 if isNegative else 0 
    running_val = 0
    while startingIdx < len(my_s): 
      running_val = running_val * 10 + (ord(my_s[startingIdx]) - ord('0'))
      startingIdx += 1 

    return running_val 

  def int_to_str(self, my_int): 
    if my_int == 0: 
      return '0'
    output = [] 
    isNegative = my_int < 0 

    if isNegative:
      my_int *= -1

    while my_int > 0: 
      digit = my_int % 10 
      output.append(digit)
      my_int //= 10

    for i in range(len(output)): 
      output[i] = chr(ord('0') + output[i]) # this was trippin you up!!! 

    if isNegative:
      output.append('-')

    output = ''.join(reversed(output))

    return output

s = Solution() 

print(s.str_to_int("314"))
print(s.int_to_str(314))
'''
Problem:
implement 2 functions: 
def str_to_int:  turn string to an int 
def int_to_str: turn int to a string

Solution: straightforward 
pain points! 
turning an int into a char, needed to do chr(ord('0') + my_digit) to do it properly
'''

