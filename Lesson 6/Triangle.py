# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    A.sort()
    N = len(A)
    
    for i in range(N-2):
        if (
            A[i] + A[i+1] > A[i+2]
            and A[i] + A[i+2] > A[i+1]
            and A[i+1] + A[i+2] > A[i]
        ):
            return 1
    
    return 0