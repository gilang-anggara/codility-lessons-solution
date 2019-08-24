package solution

func Solution(X int, Y int, D int) int {
    distance := Y - X
    if distance % D != 0 {
        return distance/D + 1
    }
    return distance/D
}
