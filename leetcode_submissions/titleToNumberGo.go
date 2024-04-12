package main

import (
	"fmt"
	"math"
)

func titleToNumber(columnTitle string) int {
	summ := 0
	length := len(columnTitle)
	for index, letter := range columnTitle {
		summ += int(float64(letter-64) * math.Pow(26, float64(length-index-1)))
	}
	return summ
}

func main() {
	fmt.Println(titleToNumber("ZY")) // Expected output: 701
}
