class Solution: 
  def pivotingAtIdx(self, A, i): 
    pivot_val = A[i]
    low_ptr, equal_ptr, high_ptr = 0, 0, len(A)-1
    while equal_ptr < high_ptr: 

      if A[equal_ptr] < pivot_val: 
        A[low_ptr], A[equal_ptr] = A[equal_ptr], A[low_ptr]
        low_ptr, equal_ptr = low_ptr + 1, equal_ptr + 1 
      elif A[equal_ptr] == pivot_val:
        equal_ptr += 1 
      else: 
        high_ptr -= 1 
        A[equal_ptr], A[high_ptr] = A[high_ptr], A[equal_ptr]
        # equal_ptr, high_ptr = equal_ptr + 1
    return A 

'''
Problem: 
Write a problem that takes an array A and and index i into A, and rearranges
 the elements such that all elements less than A[i] (the "pivot")  APPEAR FIRST, followed by elements equal to the pivot,
 then elements greater than the pivot. 

Solution: 
- start with 3 pointers, low_ptr, equal_ptr, high_ptr
- put elements less than the pivot to a low_ptr via swap with it and current pointer (equal_ptr). then, low_ptr++ and equal_ptr++
- if element is equal to pivot, equal_ptr++
- if element is larger than the pivot, swap val at high_ptr with val at equal_pt. then, equal_ptr++ and high_ptr--
'''
s = Solution() 
x = [0,1,2,0,2,1,1]

print(s.pivotingAtIdx(x, 3))

# look at edge cases and make sure that you think through every subproblem to a solution... You've been tripped up