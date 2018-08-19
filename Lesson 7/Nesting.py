# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    A = []
    
    for index in range(len(S)):
        if S[index] == '(':
            A.append(S[index])
        else:
            if not A:
                return 0
            else:
                A.pop()
    
    if A:
        return 0
    else:
        return 1