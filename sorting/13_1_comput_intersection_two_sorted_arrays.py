'''
Problem: 
Write a program that takes in two sorted arrays, and returns a new array containing 
elements that are present in both input arrays. The input arrays may have dupes and the output array
must be free of dupes

Solution:
'''
class Solution: 

  def merge_2_sorted_arrays(self, arr1, arr2): 
    uniques_arr1 = set(arr1)
    uniques_arr2 = set(arr2) 

    output = [] 

    for val in uniques_arr1:
      if val in uniques_arr2:
        output.append(val)

    return output

  def merge_2_sorted_arrays_ptrs(self, arr1, arr2):
    ptr1, ptr2 = 0, 0
    output = []
    while ptr1 < len(arr1) and ptr2 < len(arr2):
      if arr1[ptr1] < arr2[ptr2]: 
        ptr1 += 1
      elif arr1[ptr1] == arr2[ptr2]:
        if not output: 
          output.append(arr1[ptr1])
        else:
          if output[-1] != arr1[ptr1]:
            output.append(arr1[ptr1])
      else: 
        ptr2 += 1 
    return output

s = Solution() 
print(s.merge_2_sorted_arrays([1,2,2,2,2,2,2,2,3,3,3,3,3,3,33,4,5],[2,3,4,5,6,7,7,7,7,7,7,7,7,7,7,7,7]))
