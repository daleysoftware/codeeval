package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	dat, _ := ioutil.ReadFile(os.Args[1])
	for _, line := range strings.Split(strings.TrimSpace(string(dat)), "\n") {
		stringArray := strings.Split(line, " ")
		var floatSlice = make([]float64, len(stringArray))

		for i, s := range stringArray {
			f, _ := strconv.ParseFloat(s, 64)
			floatSlice[i] = f
		}

		sort.Sort(sort.Float64Slice(floatSlice))

		for i, v := range floatSlice {
			fmt.Printf("%.3f", v)
			if i+1 != len(floatSlice) {
				fmt.Print(" ")
			} else {
				fmt.Println()
			}
		}
	}
}
