package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func sum(arr []int) (agg int) {
	agg = 0
	for _, val := range arr {
		agg += val
	}
	return agg
}

func minCandies(scores []int) int {
	candies := make([]int, len(scores))
	for i := 0; i < len(scores); i++ {
		candies[i] = 1
	}

	for i := 0; i < len(scores)-1; i++ {
		if (scores[i] < scores[i+1]) && (candies[i] >= candies[i+1]) {
			candies[i+1] = candies[i] + 1
		}
		if (scores[i] > scores[i+1]) && (candies[i] <= candies[i+1]) {
			candies[i] = candies[i+1] + 1
		}
	}

	for i := len(scores) - 2; i >= 0; i-- {
		if scores[i] < scores[i+1] && candies[i] >= candies[i+1] {
			candies[i+1] = candies[i] + 1
		}
		if scores[i] > scores[i+1] && candies[i] <= candies[i+1] {
			candies[i] = candies[i+1] + 1
		}
	}

	// fmt.Println(candies)
	return sum(candies)
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	// read a token (n)
	scanner.Scan()
	_n, _ := strconv.Atoi(scanner.Text())
	n := int(_n)

	nums := make([]int, n)
	// read n tokens
	for i := 0; i < n; i++ {
		scanner.Scan()
		t, _ := strconv.Atoi(scanner.Text())
		nums[i] = t
	}

	fmt.Println(minCandies(nums))
}
