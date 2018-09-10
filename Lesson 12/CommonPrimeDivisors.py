# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def gcd(x, y, res):
    if x == y:
        return x * res
    elif x % 2 == 0 and y % 2 == 0:
        return gcd(x//2, y//2, 2 * res)
    elif x % 2 == 0:
        return gcd(x//2, y, res)
    elif y % 2 == 0:
        return gcd(x, y//2, res)
    elif x > y:
        return gcd(x-y, y, res)
    else:
        return gcd(x, y-x, res)
        
def hasCommonDivisors(x, y):
    if x == y:
        return True
        
    z = gcd(x, y, 1)
    
    if z == 1:
        return False
    
    if z == y:
        return True
    
    return hasCommonDivisors(z, y//z)
    
def solution(A, B):
    # write your code in Python 3.6
    Z = len(A)
    
    count = 0
    for i in range(Z):
        x = A[i]
        y = B[i]
            
        if hasCommonDivisors(x, y) and hasCommonDivisors(y,x):
            count += 1

    return count