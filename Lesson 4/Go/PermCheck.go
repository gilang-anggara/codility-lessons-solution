package solution

func Solution(A []int) int {
    n := len(A)
    counter := make([]bool, n)
    for _, num := range A {
        if num > n || counter[num-1] == true {
            return 0
        } else {
            counter[num-1] = true
        }
    }
    return 1
}
