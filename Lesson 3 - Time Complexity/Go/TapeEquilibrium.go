package solution

func Solution(A []int) int {
    sumLeft := A[0]
    sumRight := sum(A[1:])
    minSum := abs(sumLeft - sumRight)
    for i := 1; i < len(A) - 1; i++ {
        sumLeft += A[i]
        sumRight -= A[i]
        diff := abs(sumLeft - sumRight)
        if diff < minSum {
            minSum = diff
        }
    }
    return minSum
}

func sum(array []int) int {
    sum := 0
    for _, num := range array {
        sum += num
    }
    return sum
}

func abs(x int) int {
    if x < 0 {
        return -1 * x
    }
    return x
}
