# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    n = len(A)
    
    for i in range(1, n):
        A[i] += max(A[max(0, i - 6):i])
    
    return A[n - 1]