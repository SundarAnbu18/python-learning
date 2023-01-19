# Recursive Python program to count
# number of digits in a number
 
 
def countDigit(n):
    if n//10 == 0:
        return 1
    return 1 + countDigit(n // 10)
 
 
# Driver Code
n = int(input())
print("Number of digits : % d" % (countDigit(n)))
 
# This code is contributed by Shreyanshi Arun
