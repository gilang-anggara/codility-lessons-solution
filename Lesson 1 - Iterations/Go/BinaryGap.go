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
    startingIdx := 0
    for startingIdx < len(binary) {
        if binary[startingIdx] == '1' {
            startingIdx++
            break
        }
        startingIdx++
    }
    maxGap := 0
    gap := 0
    i := startingIdx
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
