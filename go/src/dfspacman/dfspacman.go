package main

/*
https://www.hackerrank.com/challenges/pacman-dfs
*/

import (
	"fmt"
	"log"
)

func Pop(stack *[][2]int) (r [2]int) {
	x := len(*stack) - 1
	r = (*stack)[x]
	*stack = (*stack)[:x]
	return
}

var nope = [2]int{-1, -1}
var wall = '%'

func isWall(x uint8) bool {
	return rune(x) == wall
}

func neighbors(a, b int, board *[]string) (u, l, r, d [2]int) {
	rows := len((*board))
	cols := len((*board)[0])

	if b-1 < 0 || isWall((*board)[a][b-1]) {
		l = nope
	} else {
		l = [2]int{a, b - 1}
	}

	if b+1 >= cols || isWall((*board)[a][b+1]) {
		r = nope
	} else {
		r = [2]int{a, b + 1}
	}

	if a-1 < 0 || isWall((*board)[a-1][b]) {
		u = nope
	} else {
		u = [2]int{a - 1, b}
	}

	if a+1 >= rows || isWall((*board)[a+1][b]) {
		d = nope
	} else {
		d = [2]int{a + 1, b}
	}
	return
}

type PredMap map[[2]int][2]int

func printPredMap(node [2]int, pred *PredMap) {
	nodes := [][2]int{}
	for node != nope {
		// fmt.Println(node[0], node[1])
		nodes = append(nodes, node)
		node = (*pred)[node]
	}
	fmt.Println(len(nodes) - 1)
	for i := len(nodes) - 1; i >= 0; i-- {
		fmt.Println(nodes[i][0], nodes[i][1])
	}
}

func play(pr, pc, fr, fc int, board *[]string) {
	// fmt.Println(*board)

	pacman := [2]int{pr, pc}
	food := [2]int{fr, fc}

	// predecesor map
	pred := PredMap{}
	pred[pacman] = nope

	// stack of nodes
	stack := [][2]int{}
	stack = append(stack, pacman)

	record := [][2]int{}

	for len(stack) > 0 {
		// traverse to the next node
		node := Pop(&stack)
		a, b := node[0], node[1]
		record = append(record, node)

		if node == food {
			// found, now just print predecesors from food
			fmt.Println(len(record))
			for i := 0; i < len(record); i++ {
				fmt.Println(record[i][0], record[i][1])
			}
			printPredMap(node, &pred)
			return
		}

		up, left, right, down := neighbors(a, b, board)
		// for each neighbor, update pred map
		for _, dir := range [4][2]int{up, left, right, down} {
			_, ok := pred[dir]
			if !ok && dir != nope {
				pred[dir] = node
				stack = append(stack, dir)
			}
		}
	}

	// if we get here, we didn't find the food
	fmt.Println("Food not found")
}

func main() {
	// read in row/col pair of pacman
	var pr, pc int
	_, err := fmt.Scanln(&pr, &pc)
	if err != nil {
		log.Fatal("Bad input 1")
	}

	// read in row/col pair of food
	var fr, fc int
	_, err = fmt.Scanln(&fr, &fc)
	if err != nil {
		log.Fatal("Bad input 2")
	}

	// read in # rows/# cols
	var r, c int
	_, err = fmt.Scanln(&r, &c)
	if err != nil {
		log.Fatal("Bad input 3")
	}

	rows := make([]string, r)

	for i, _ := range rows {
		fmt.Scanln(&rows[i])
		if len(rows[i]) != c {
			log.Fatal("Not a valid row:", rows[i])
		}
	}

	play(pr, pc, fr, fc, &rows)
}
