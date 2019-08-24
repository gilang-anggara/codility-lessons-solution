package solution

func Solution(A []int) int {
    max := len(A) + 1
    arithmeticSum := (max + 1) * max / 2
    actualSum := 0
    for _, num := range A {
        actualSum += num
    }
    return arithmeticSum - actualSum
}
