# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    N = len(A)
    check = [0]*N
    
    for element in A:
        if element <= N and element > 0:
            check[element-1] = 1
    
    for index in range(N):
        if check[index] == 0:
            return index+1

    return N+1