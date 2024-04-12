package main

import (
	"math"
	"sort"
)

func threeSumClosest(nums []int, target int) int {
	sort.Ints(nums)
	length := len(nums)
	closestSum := math.MaxFloat32
	closestDiff := math.MaxFloat32

	for i := 0; i < length-2; i++ {
		left, right := i+1, length-1
		for left < right {
			currentSum := nums[i] + nums[left] + nums[right]
			currentDiff := math.Abs(float64(target) - float64(currentSum))

			if currentDiff < closestDiff {
				closestSum = float64(currentSum)
				closestDiff = currentDiff
			}

			if currentSum < target {
				left++
			} else {
				right--
			}
		}

	}
	return int(closestSum)
}
