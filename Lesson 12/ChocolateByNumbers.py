# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def gcd(a,b,res):
    if a == b:
        return a * res
    elif a % 2 == 0 and b % 2 == 0:
        return gcd(a//2, b//2, 2*res)
    elif a % 2 == 0 and b % 2 != 0:
        return gcd(a//2, b, res)
    elif a % 2 != 0 and b % 2 == 0:
        return gcd(a, b//2, res)
    elif a > b:
        return gcd(a-b, b, res)
    else:
        return gcd(a, b-a, res)
            
def solution(N, M):
    # write your code in Python 3.6
    return N//gcd(N, M, 1)