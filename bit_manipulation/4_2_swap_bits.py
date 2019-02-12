class Solution: 
  def swapBits(self, num, i, j):
    # grab the bits at indices i and j, see if they differ
    ithBit = (num >> (i-1)) & 1  
    jthBit = (num >> (j-1)) & 1 
    # if they don't, then return
    # if they do differ, then use XOR on each of them aaaaand PUSH them onto the ith and jth index
    if(ithBit != jthBit): 
      # bit_mask = ( (i -1) << (ithBit ^ 1)) | ((j - 1) << (jthBit ^ 1)) # WRONG 
      bit_mask = 1 << (i-1) | 1 << (j-1)
      print("bit mask for the given i and j value: {}".format(bin(bit_mask)))
      num ^= bit_mask 

    return num


s = Solution() 
print(bin(73))
processed_val = s.swapBits(73, 2, 7)
print(processed_val)
print(bin(processed_val))

# your logic is flawed, analyze before you throw in an XOR there, 
# XOR works irregardless of what the existing values were, this is similar and opposite to the AND (&) operator. 
# Thus, we only detect differnces between the bits, not the actual values of the bits themselves! Wow. Very cool.