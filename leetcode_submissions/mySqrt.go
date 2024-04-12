package main

import (
	"fmt"
	"math"
)

// func mySqrt(x int) int {
// 	if x == 1 {
// 		return 1
// 	}
// 	if x == 0 {
// 		return 0
// 	}
// 	var num float64 = float64(x)
// 	var root float64 = num / 2 
// 	var eps float64 = 0.000000001
// 	var half float64 = 0.5
// 	for (root - num/root) > eps {
// 		root =  half * (root + num / root)
// 	}
// 	return int(math.Floor(root))
// }



func mySqrt(x int) int {
	if x < 0 {
		return 0
	}
	if x == 1 {
		return 1
	}
	wholePart := 1.0
	for {
		var squared float64 = wholePart * wholePart
		if squared == float64(x) {
			return int(math.Floor(wholePart))
		}
		if squared >  float64(x) {
			wholePart = wholePart - 1
			break
		}
		wholePart += 1
	}

	var lower = wholePart
	var upper = wholePart + 1
	var mid = (lower + upper) / 2
	for i := 0; i < 1000; i++ {
		if mid*mid > float64(x) {
			upper = mid
		} else if mid*mid < float64(x) {
			lower = mid
		}
		mid = float64(lower+upper) / 2
	}
	return int(math.Floor(mid))
}

func Sqrt(x float64) float64 {
	if x < 0 {
		return 0
	}
	if x == 1 {
		return 1
	}
	wholePart := 1.0
	for {
		var squared float64 = wholePart * wholePart
		if squared == x {
			return wholePart
		}
		if squared > x {
			wholePart = wholePart - 1
			break
		}
		wholePart += 1
	}

	var lower = wholePart
	var upper = wholePart + 1
	var mid = (lower + upper) / 2
	for i := 0; i < 1000; i++ {
		if mid*mid > float64(x) {
			upper = mid
		} else if mid*mid < float64(x) {
			lower = mid
		}
		mid = float64(lower+upper) / 2
	}
	return mid
}

func main() {
	fmt.Println(Sqrt(90010))
}