# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    # N > 0
    
    factors = 0
    possibleDivider = 1
        
    while possibleDivider*possibleDivider < N:
        if N % possibleDivider == 0:
            factors += 2
        possibleDivider += 1
    
    if possibleDivider*possibleDivider == N:
        factors += 1
        
    return factors