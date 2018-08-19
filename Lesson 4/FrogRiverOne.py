def solution(X, A):
    N = len(A)

    leaves = [0]*X
    counter = 0
    
    for time in range(len(A)):
        if not A[time] > X:
            if leaves[A[time]-1] == 0:
                leaves[A[time]-1] = 1
                counter += 1
            if counter == X:
                return time
    return -1