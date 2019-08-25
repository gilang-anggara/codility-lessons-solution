package solution

func Solution(X int, A []int) int {
    filled := make([]int, X)
    positionFilled := 0
    for time, position := range A {
        if filled[position-1] > 0 {
            continue
        }
        filled[position-1]++
        positionFilled += 1
        if positionFilled == X {
            return time
        }
    }
    return -1
}
