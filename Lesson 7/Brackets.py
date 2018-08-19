# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
        
def solution(S):
    # write your code in Python 3.6
    A = []
    
    for index in range(len(S)):
        if S[index] in '{[(':
            A.append(S[index])
        elif S[index] == ')':
            if not A:
                return 0
            elif A[-1] != '(':
                return 0
            else:
                A.pop()
        elif S[index] == ']':
            if not A:
                return 0
            elif A[-1] != '[':
                return 0
            else:
                A.pop()
        elif S[index] == '}':
            if not A:
                return 0
            elif A[-1] != '{':
                return 0
            else:
                A.pop()
    
    return 0 if A else 1