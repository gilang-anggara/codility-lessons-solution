package solution

func Solution(A []int) int {
    exists := map[int]bool{}
    for _, num := range A {
        exists[num-1] = true
    }
    candidate := 0
    for true {
        if !exists[candidate] {
            break
        }
        candidate++
    }
    return candidate+1
}
