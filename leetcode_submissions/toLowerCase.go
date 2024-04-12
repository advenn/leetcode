package main

import "fmt"

func toLowerCase(s string) string {
	byteArrayData := []byte(s)
	for index, value := range byteArrayData {
		if value >= 65 && value <= 90 {
			byteArrayData[index] += 32
		}
	}
	return string(byteArrayData)
}

func main() {

	fmt.Println(toLowerCase("Asadbek, LOVELY, HAmas, Israel"))
}
