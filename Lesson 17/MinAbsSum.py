# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    n = len(A)
    if n == 0:
        return 0
    if n == 1:
        return abs(A[0])
        
    A = [abs(element) for element in A]
    m = max(A)
    s = sum(A)
    
    count = [0] * (m + 1)
    
    for i in range(n):
        count[A[i]] += 1
    
    dp = [-1] * (s + 1)
    dp[0] = 0
    
    for i in range(1, m + 1):
        if count[i] > 0:
            for j in range(s):
                if dp[j] >= 0:
                    dp[j] = count[i]
                elif(j >= i and dp[j - i] > 0):
                    dp[j] = dp[j - i] - 1
    result = s
    
    for i in range(s // 2 + 1):
        if dp[i] >= 0:
            result = min(result, s - 2 * i)
    return result