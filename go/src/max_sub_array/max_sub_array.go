package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	// "strings"
)

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
func maxSubArray(arr IntArr) (IntArr, Int) {
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
	return arr[max_idx[0] : max_idx[1]+1], arr[max_idx[0] : max_idx[1]+1].sum()
}

/* Maximum-Sum Contiguous Sub-Array.
Memory efficient array version.
*/
func maxSubArray2(arr IntArr) (IntArr, Int) {
	//       We only really need 2 rows and to save the slice that contains
	//       the max.
	max_sum := Int(MinInt)

	n := len(arr)
	var max_arr, cur, prev IntArr

	cur = make(IntArr, n) // Initialized to 0
	prev = make(IntArr, n)

	cur[n-1] = arr[n-1]
	max_sum = cur[n-1]  // just the last element
	max_arr = cur[n-1:] // just the last element as a 1 element slice
	// Up from bottom
	for i := n - 2; i >= 0; i-- {
		copy(prev, cur)
		// TODO: limit copy to only the required values
		cur[i] = arr[i]
		for j := i + 1; j < n; j++ {
			cur[j] = cur[i] + prev[j]
			if cur[j] > max_sum {
				max_sum = cur[j]
				max_arr = cur[:j+1]
			}
		}
	}
	return max_arr, max_sum
}

/* Maximum-Sum Non-Contiguous Sub-Array.
This is just all positive numbers in the array.
If there are all negative numbers, it is just an array
of 1 element, the largest negative number.
*/
func maxNCSubArray(arr IntArr) (IntArr, Int) {
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
	return ans, ans.sum()
}

func main2() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan() // read a line
	t, _ := strconv.Atoi(scanner.Text())

	for i := 0; i < t; i++ {
		scanner.Scan() // read a line
		n, _ := strconv.Atoi(scanner.Text())

		arr := make(IntArr, n)
		scanner.Split(bufio.ScanWords)
		for j := 0; j < n; j++ {
			scanner.Scan()
			x, _ := strconv.Atoi(scanner.Text())
			arr[j] = Int(x)
		}
		scanner.Split(bufio.ScanLines)
		// do processing here
		// ms_sum, mncs_sum := maxSumOfSubArray(arr)
		// fmt.Printf("%d %d\n", ms_sum, mncs_sum)
	}
}

/*
// line := strings.NewReader(scanner.Text())
// arr, _ := ReadInts(line)
// fmt.Println(len(arr))

func main1() {
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
		// fmt.Println("making slice")
		arr := make(IntArr, n, n)
		// fmt.Println("made slice")

		for j := 0; j < n; j++ {
			_, err = fmt.Scan(&(arr[j]))
			if err != nil {
				log.Fatal("Bad input (3)")
			}
		}

		// Contiguous
		// _, ms_sum := maxSubArray2(arr)
		// ms_sum, mncs_sum := maxSumOfSubArray(arr)
		// ms.printArr()
		// Non-contiguous
		// _, mncs_sum := maxNCSubArray(arr)

		// ms_sum, mncs_sum := maxSumOfSubArray(arr)
		// fmt.Printf("%d %d\n", ms_sum, mncs_sum)
	}
}
*/
