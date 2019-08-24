package solution

import "fmt"
import "bytes"

func Solution(N int) int {
    binary := intToBinary(N)
    return maxGap(binary)
}

func intToBinary(N int) string {
    var binary bytes.Buffer
    for N/2 != 0 {
        binary.WriteString(fmt.Sprint(N % 2))
        N = N/2
    }
    binary.WriteString("1")
    return binary.String()
}

func maxGap(binary string) int {
    i := 0
    for i < len(binary) {
        if binary[i] == '1' {
            i++
            break
        }
        i++
    }
    maxGap := 0
    gap := 0
    for i < len(binary) {
        if binary[i] == '1' {
            if gap > maxGap {
                maxGap = gap
            }
            gap = 0
        } else {
            gap += 1
        }
        i++
    }
    return maxGap
}
