"""
Checks if an n-digit number is pandigital
A n-digit number is pandigital if it makes use of all the digits 1 to n exactly once
For e.g. the 5-digit number 15234 is 1 through 5 pandigital
"""

def is_n_pandigital(n: int) -> bool:
    digits = [ch for ch in str(n)]
    nums = {str(k):1 for k in range(1,len(digits)+1)}
    for ch in digits:
        nums[ch] = nums.get(ch, 0) - 1
        if nums[ch] < 0:
            return False
    return all(x == 0 for x in nums.values())