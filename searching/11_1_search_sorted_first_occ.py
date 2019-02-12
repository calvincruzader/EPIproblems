'''
Problem: 
Given a sorted array of integers, with possible repeated items, 
return the index of thefirst occurrence of a specified element k
'''

class Solution: 

  def bin_search_dupes_considered(self, arr, k): 

    if not arr or not k: 
      return -1 

    lowIdx = 0
    highIdx = len(arr)-1

    result = -1

    while lowIdx <= highIdx:
      mid = lowIdx + ((highIdx - lowIdx) / 2)
      if arr[mid] > k: 
        highIdx = mid - 1 
      elif arr[mid] == k: 
        result = mid 
        highIdx = mid - 1
      else: 
        lowIdx = mid + 1 
    return result





s = Solution()
print(s.bin_search_dupes_considered([0,1,2,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,6,7,8,9], 4))

'''
paint point: 
- doesn't matter about the while condition lowIdx <= highIdx considering whether it would go on forever 
if we put an equals sign on it... we're always getting rid of a portion of the array with each iteration 
so we shouldn't mind doing a <= over a more restrictive <. Also, < or > will fail because it will not 
consider the case where lowIdx == highIdx when the lowIdx was not considered previously
'''