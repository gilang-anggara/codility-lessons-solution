# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    stack = []
    N = len(A)
    predator = -1
    
    for index in range(N):
        if B[index] == 0:
            if A[index] > predator:
                if stack and predator != -1:
                    stack.pop()
                    predator = -1
                stack.append(A[index])
        else:
            if A[index] > predator:
                predator = A[index]
                stack.append(predator)
    return len(stack)