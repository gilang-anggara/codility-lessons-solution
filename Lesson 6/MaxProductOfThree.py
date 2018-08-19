# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    A.sort()
    
    N = len(A)
    
    # Two negative and one positive
    twoNegOnePosProduct = A[N-1]*A[0]*A[1]
    
    # Three positive
    threePositiveProduct = A[N-1]*A[N-2]*A[N-3]
    
    return threePositiveProduct if threePositiveProduct >= twoNegOnePosProduct else twoNegOnePosProduct