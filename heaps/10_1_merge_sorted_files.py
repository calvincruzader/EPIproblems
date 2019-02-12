'''
Problem: 
Given a list of sorted arrays, return the union of all these arrays, UA, such that UA is also sorted.

Solution: 
Throw an iterable of each individual array into a min-heap / min-priority queue with size k such that we grab 
the smallestVal in the heap and go to the next() element in the iterable with the smallestVal

This will run in O(n log k) time where n is all of the elements and k is the number sorted arrays. Pretty gooooood

'''
import heapq 

class Solution: 

  def merge_k_sorted_arrays(self, sorted_arrays): 
    output_arr = []

    sorted_arrays_iterables = [iter(arr) for arr in sorted_arrays]

    # now we have push all these iterables into a min heap, we'll need to keep an index of the iterable,
    # so enumerate() is appropriate. We need the index so we can reference the iterable array as we're 
    # putting iterated values onto the heap

    min_heap = []

    for idx, sorted_array in enumerate(sorted_arrays_iterables): 
      sorted_arr_val = next(sorted_array, None) # prevent a runtime error by catching empty iterables 
      if sorted_arr_val: 
        heapq.heappush(min_heap, (sorted_arr_val, idx))

    while min_heap:
      sorted_arr_val, sorted_arr_idx = heapq.heappop(min_heap)
      output_arr.append(sorted_arr_val)

      sorted_arr_next_val = next(sorted_arrays_iterables[sorted_arr_idx], None) # grab the next element in that ith sArray

      if sorted_arr_next_val: 
        heapq.heappush(min_heap, (sorted_arr_next_val, sorted_arr_idx))

    return output_arr

s = Solution()

print(s.merge_k_sorted_arrays([[1,2,3], [2,3,4], [3,4,5]]))

'''
So, lessons learned: 
- keep track of the array through a tuple 
- get rid of the need for pointers by using iterables for each sorted array. This is something to consider
- next(iter, default) - chooses a default value should the iter be exhausted
'''