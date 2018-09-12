# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(M, A):
    # write your code in Python 3.6
    N = len(A)
    
    # all element of A <= M
    count = 0
    j = 0
    mSet = set()
    for i in range(N):
        while j < N:
            if A[j] in mSet:
                mSet.remove(A[i])
                break
            
            mSet.add(A[j])
            j += 1
        count += j - i
        if count > 1_000_000_000:
            return 1_000_000_000
    return count