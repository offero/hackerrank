package main

/*
https://www.hackerrank.com/challenges/fibonacci-modified

Tn+2 = (Tn+1)^2 + Tn

Input: 3 space-separated integers on 1 line.
Output: 1 integer. The N'th term of the series.
*/

import (
	"fmt"
	"log"
	"math/big"
)

func fibmod(a, b, n int64) (ans *big.Int) {
	// while n > 2 ; b/c the first 2 are provided.
	ans = big.NewInt(0)
	A := big.NewInt(a)
	B := big.NewInt(b)
	N := big.NewInt(n)
	max := big.NewInt(2)
	decr := big.NewInt(1)

	// While N > max
	for N.Cmp(max) == 1 {
		ans.Mul(B, B).Add(ans, A) // ans = b*b + a
		A.Set(B)                  // a = b
		B.Set(ans)                // b = ans
		N.Sub(N, decr)            // n--
	}
	return
}

func main() {
	var a, b, n int64

	_, err := fmt.Scanln(&a, &b, &n)

	if err != nil {
		log.Fatal("Bad input")
	}

	fmt.Println(fibmod(a, b, n))
}
