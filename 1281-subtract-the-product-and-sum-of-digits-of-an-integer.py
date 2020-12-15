'''
Given an integer number n, return the difference between the product
of its digits and the sum of its digits.

Example 1:

Input: n = 234
Output: 15
Explanation:
Product of digits = 2 * 3 * 4 = 24
Sum of digits = 2 + 3 + 4 = 9
Result = 24 - 9 = 15
Example 2:

Input: n = 4421
Output: 21
Explanation:
Product of digits = 4 * 4 * 2 * 1 = 32
Sum of digits = 4 + 4 + 2 + 1 = 11
Result = 32 - 11 = 21

Constraints:

1 <= n <= 10^5
'''

def subtractProductAndSum(n: int) -> int:
    s = str(n)
    product = int(s[0])
    sum = int(s[0])
    for element in range(1, len(s)):
        product *= int(s[element])
        sum += int(s[element])
    return product - sum


print(subtractProductAndSum(234))