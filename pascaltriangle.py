"""
Guna is learning about pascal's traingle.Pascal’s triangle is a triangular array of the binomial coefficients.The task is as follows .

Write a function that takes an integer value n as input and prints first n lines of the Pascal’s triangle.

constraints:

1<=n<=1000

Input Format:

The input indicates the integer n

Output Format:

print n lines of pascal's traingle

Example:

Input:
5

Output:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1

Example 2:

Input:
6

Output:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1

"""

def printPascal(n):  
  
    for line in range(1, n + 1):
        l=[]
        C = 1
        for i in range(1, line + 1):
            l.append(C)
            C = int(C * (line - i) / i)  
        print(*l)
n=int(input())
printPascal(n)
