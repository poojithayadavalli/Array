"""

Amar is a student and he hate the digit 0.So he always prefer Zero to be at last place.

Given an array A, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Constraints:

1<=A.length<=1000

Input:

Input indicates array A

Output:

Print the resultant array

Example:

Input:

0 1 0 3 12

Output:

1 3 12 0 0



"""
nums = list(map(int,input().split()))
i = j = 0
while j < len(nums):
    if nums[j] != 0:
        nums[j], nums[i] = nums[i], nums[j]
        i += 1
        j += 1
    else:
        j += 1
print(*nums)
