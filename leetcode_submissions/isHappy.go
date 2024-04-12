package main

import (
	"fmt"
	"strconv"
)

func intToDigitsSlice(n int) []int {
	str := strconv.Itoa(n)
	digits := make([]int, len(str))

	for i, char := range str {
		digit, _ := strconv.Atoi(string(char))
		digits[i] = digit
	}

	return digits
}
func sum(arr []int) int {
	sum := 0
	for _, valueInt := range arr {
		sum += valueInt
	}
	return sum
}
func contains(s []int, target int) bool {
	for _, value := range s {
		if value == target {
			return true
		}
	}
	return false
}
func squareElements(nums []int) []int {
	squared := make([]int, len(nums))
	for i, value := range nums {
		squared[i] = value * value
	}
	return squared
}

func isHappy(n int) bool {
	var used []int
	for {
		var nums = intToDigitsSlice(n)
		n = sum(squareElements(nums))
		if n < 10 && n == 1 {
			return true
		}
		if contains(used, n) {
			return false
		}
		used = append(used, n)
	}
}

func main() {
	fmt.Println(isHappy(7))
	fmt.Println(isHappy(1_111_111))
}
