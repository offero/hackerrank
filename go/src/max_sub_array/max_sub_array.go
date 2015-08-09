package main

import (
	"fmt"
	"log"
	"math"
)

type Int int64
type IntArr []Int

// type PIntArr *IntArr

const MaxInt int64 = math.MaxInt64
const MinInt int64 = math.MinInt64

func newMat(r, c int) *[][]Int {
	mat := make([][]Int, r)
	for i, _ := range mat {
		mat[i] = make(IntArr, c)
	}
	return &mat
}

func printMat(mat *[][]Int) {
	for i, _ := range *mat {
		fmt.Printf("[")
		for _, v := range (*mat)[i] {
			fmt.Printf(" %2d ", v)
		}
		fmt.Printf("]\n")
	}
}

func (self IntArr) printArr() {
	for i, v := range self {
		if i > 0 {
			fmt.Printf(" ")
		}
		fmt.Printf("%d", v)
	}
	fmt.Println("")
}

func (self IntArr) sum() Int {
	t := Int(0)
	for _, v := range self {
		t += v
	}
	return t
}

/* Maximum-Sum Contiguous Sub-Array
 */
func maxSubArray(arr IntArr) IntArr {
	n := len(arr)
	mat := newMat(n, n)
	max_idx := [2]int{0, 0}

	// Fill the diagonals
	for i := 0; i < n; i++ {
		(*mat)[i][i] = arr[i]
		max_sum := (*mat)[max_idx[0]][max_idx[1]]
		if (*mat)[i][i] > max_sum {
			max_idx = [2]int{i, i}
		}
	}

	// Fill in the rest
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			(*mat)[i][j] = (*mat)[i][j-1] + arr[j]
			max_sum := (*mat)[max_idx[0]][max_idx[1]]
			if (*mat)[i][j] > max_sum {
				max_idx = [2]int{i, j}
				// fmt.Printf("Setting max: %d idx: %v \n", (*mat)[i][j], max_idx)
			}
		}
	}

	// printMat(mat)
	// fmt.Printf("Max sum: %d Index: %v\n", (*mat)[max_idx[0]][max_idx[1]], max_idx)
	return arr[max_idx[0] : max_idx[1]+1]
}

/* Maximum-Sum Non-Contiguous Sub-Array.
This is just all positive numbers in the array.
If there are all negative numbers, it is just an array
of 1 element, the largest negative number.
*/
func maxNCSubArray(arr IntArr) IntArr {
	ans := make(IntArr, 0)
	lgNeg := Int(MinInt)
	for _, v := range arr {
		// This includes 0's
		if v >= Int(0) {
			ans = append(ans, v)
		}
		if v < Int(0) && v > lgNeg {
			lgNeg = v
		}
	}
	if len(ans) == 0 {
		ans = append(ans, lgNeg)
	}
	return ans
}

func main() {
	var t, n int
	_, err := fmt.Scanln(&t)
	if err != nil {
		log.Fatal("Bad input (1)")
	}

	// For each test case
	for i := 0; i < t; i++ {
		_, err := fmt.Scanln(&n)
		if err != nil {
			log.Fatal("Bad input (2)")
		}
		// Make the array
		arr := make(IntArr, n)
		for j := 0; j < n; j++ {
			_, err = fmt.Scan(&(arr[j]))
			if err != nil {
				log.Fatal("Bad input (3)")
			}
		}

		// Contiguous
		ms := maxSubArray(arr)
		// ms.printArr()
		// Non-contiguous
		mncs := maxNCSubArray(arr)

		fmt.Printf("%d %d\n", ms.sum(), mncs.sum())

	}
	// Contiguous
	// ms := maxSubArray([]Int{1, 2, -5, 3, 4})
	// Non-contiguous
	// mncs := maxNCSubArray([]Int{1, 2, -5, 3, 4})
	// fmt.Printf("%d %d\n", ms.sum(), mncs.sum())
}
