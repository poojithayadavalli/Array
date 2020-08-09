"""
Ganvika is learning about arrays and she got stuck in a binary array task.The task is given below

Given a binary array B with size n, find the maximum number of consecutive 1s in this array.

Contrainsts:

1<=B.length<=1000
array must contain only 0 and 1

Input Format:
Firstline indicates size of array n
Secondline indicates elements of binary array

Output:

print the count of maximum consecutive ones

Example 1:

Input: 
6
1 1 0 1 1 1

Output:
3

Explanation:

The first two digits or the last three digits are consecutive 1s.
The maximum number of consecutive 1s is 3.

"""
def maxConsecutive(nums):
    i=0
    s=""
    temp=""
    if len(nums)<2:
        return 1 if nums[0]==1 else 0
    while i < len(nums):
        if nums[i]!=1:
            if len(temp)>len(s):
                s=temp
            temp=""
            i+=1
        else:
            temp+="1"
            i+=1
    if len(temp)>len(s):
        s=temp
    return len(s)
nums=list(map(int,input().split()))
print(maxConsecutive(nums))
