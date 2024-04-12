package main

import "fmt"

func gameOfLife(board [][]int) [][]int {
	var height = len(board)
	var width = len(board[0])

	board_ := make([][]int, height)
	copy(board_, board_)
	for h := 0; h < height; h++ {
		for w := 0; w < width; w++ {
			summ := 0
			rows := make([]int, 9)
			cols := make([]int, 9)
			if h == 0 {
				rows = append(rows, []int{h, h + 1}...)
			} else if h == height-1 {
				rows = append(rows, []int{h - 1, h}...)
			} else {
				rows = append(rows, []int{h - 1, h, h + 1}...)
			}
			if w == 0 {
				cols = append(cols, []int{w, w + 1}...)
			} else if w == width-1 {
				cols = append(cols, []int{w - 1, w}...)
			} else {
				cols = append(cols, []int{w - 1, w, w + 1}...)
			}
			for row := range rows {
				for col := range cols {
					if row != h || col != w {

					}
				}
			}
		}
	}
}

func main() {
	var arr [][]int = [][]int{
		{0, 1, 0},
		{0, 0, 1},
		{1, 1, 1},
		{0, 0, 0},
	}
	fmt.Println(gameOfLife(arr))
}
