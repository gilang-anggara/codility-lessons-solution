package solution

func Solution(N int, A []int) []int {
    counter := make([]int, N)
    base := 0
    localMax := 0
    for _, num := range A {
        if num == N + 1 {
            base = localMax
            continue
        }
        counter[num-1] = max(base, counter[num-1]) + 1
        localMax = max(localMax, counter[num-1])
    }
    for i := range counter {
        counter[i] = max(counter[i], base)
    }
    return counter
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
