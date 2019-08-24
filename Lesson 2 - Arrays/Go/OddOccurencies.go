package solution

// idea
// doing bitwise xor on the same value will return 0
// doing bitwise xor on 0 and X will always return X,
// which is the number we're looking for
func Solution(A []int) int {
	unpaired := 0
    for _, num := range A {
        unpaired ^= num
    }
    return unpaired
}
