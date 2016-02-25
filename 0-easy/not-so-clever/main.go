package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strconv"
	"strings"
)

func stringArrayToIntArray(s []string) (result []int) {
	for _, i := range s {
		j, _ := strconv.Atoi(i)
		result = append(result, j)
	}
	return
}

func main() {

	dat, _ := ioutil.ReadFile(os.Args[1])
	for _, line := range strings.Split(strings.TrimSpace(string(dat)), "\n") {
		array := stringArrayToIntArray(
			strings.Split(strings.TrimSpace(strings.Split(line, "|")[0]), " "))

		iterations, _ := strconv.Atoi(
			strings.TrimSpace(strings.Split(line, "|")[1]))

		for i := 0; i < iterations; i++ {
			for j := 0; j < len(array)-1; j++ {
				if array[j] > array[j+1] {
					tmp := array[j]
					array[j] = array[j+1]
					array[j+1] = tmp
					break
				}
			}
		}

		for i, dat := range array {
			if i == len(array)-1 {
				fmt.Println(dat)
			} else {
				fmt.Print(dat, " ")
			}
		}
	}
}
