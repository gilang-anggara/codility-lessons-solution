package solution

func Solution(A []int, K int) []int {
    actualRotations := getRotations(len(A), K)
    return rotated(A, actualRotations)
}

func getRotations(m, n int) int {
    if m == 0 {
        return 0
    }
    return n % m
}

func rotated(array []int, rotations int) []int {
    result := []int{}
    for i := len(array) - rotations; i < len(array); i++ {
        result = append(result, array[i])
    }
    for i := 0; i < len(array) - rotations; i++ {
        result = append(result, array[i])
    }
    return result
}
