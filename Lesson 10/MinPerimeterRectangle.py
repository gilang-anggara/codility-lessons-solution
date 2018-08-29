# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    
    factorCandidate = 1
    minPerimeter = 4_000_000_000

    while factorCandidate*factorCandidate <= N:
        if N % factorCandidate == 0:
            minPerimeter = min(minPerimeter, 2*(factorCandidate + N//factorCandidate))
        factorCandidate += 1
    
    return minPerimeter