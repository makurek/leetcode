"""
Write a function that takes an unsigned integer and returns the number of '1'
bits it has (also known as the Hamming weight).

Note:

Note that in some languages such as Java, there is no unsigned integer type.
In this case, the input will be given as a signed integer type. It should not affect
your implementation, as the integer's internal binary representation is the same,
whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation.
Therefore, in Example 3 above, the input represents the signed integer. -3.

Follow up: If this function is called many times, how would you optimize it?

Constraints:

The input must be a binary string of length 32
"""

""" 
Complexity analysis
--------------------

The runtime depends on the number of 1-bits in n. In the worst case, all bits in n are 1-bits.
In case of a 32-bit integer, the runtime is O(1).

The space complexity is O(1), since no additional space is allocated.
"""

def hammingWeight(n: int) -> int:
    count = 0
    for i in range(0,32):
        if n & 0x01 == 1:
            count += 1
        n >>= 1
    return count

print(hammingWeight(0b00000000000000000000000000001011))
