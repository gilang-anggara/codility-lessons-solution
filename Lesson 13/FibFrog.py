# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from collections import deque

MAX_N = 100000

def solution(A):
    # write your code in Python 3.6
    n = len(A)
    
    # if length less than 3 than it can be jumped with 1, 2, or 3 steps
    if n < 3:
        return 1
    
    # create fibonacci sequence
    fiboSeq = [0, 1]
    
    i = 1
    
    while True:
        fibo = fiboSeq[i] + fiboSeq[i-1]
        
        if fibo > MAX_N:
            break
        
        fiboSeq.append(fibo)
        i += 1
    
    
    # search for jumpable spots from starting point
    jumpable = [0]*n
    jumpSpots = deque()
    jumpSpots.append(-1)
    
    for i in range(2, len(fiboSeq)):
        position = fiboSeq[i] - 1
        
        if position > n:
            break
        elif position == n:
            return 1
        elif A[position]:
            jumpable[position] = 1;
            jumpSpots.append(position)
    
    
    # search for minimum jumps
    minimumJumps = -1
    
    while jumpSpots: # while jumpSpots is not empty
        position = jumpSpots.popleft()
        
        for i in range (2, len(fiboSeq)):
            nextPosition = position + fiboSeq[i] # position to jump from the queued jumpSpots
            
            if nextPosition > n: # no jumping spot available
                break
            elif nextPosition == n: # reach end
                if minimumJumps == -1 or jumpable[position] + 1 < minimumJumps:
                    minimumJumps = jumpable[position] + 1
            elif A[nextPosition] and not jumpable[nextPosition]: # A has jumpable spots
                jumpable[nextPosition] = jumpable[position] + 1
                jumpSpots.append(nextPosition)
        
    return minimumJumps
    
    