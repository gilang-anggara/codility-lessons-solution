# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    
    UPSTREAM = 0
    # write your code in Python 3.6
    upstreamStack = []
    downstreamStack = []
    
    for element, flow in zip(A, B):
        if flow == UPSTREAM:
            upstreamStack.append(element)
            
            while downstreamStack:
                if downstreamStack[-1] < element:
                    downstreamStack.pop()
                else:
                    upstreamStack.pop()
                    break
        
        else:
            downstreamStack.append(element)
    
    return len(upstreamStack) + len(downstreamStack)