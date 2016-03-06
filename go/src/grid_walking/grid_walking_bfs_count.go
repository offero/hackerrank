package main

/*
https://www.hackerrank.com/challenges/grid-walking
*/

import (
	"fmt"
	"log"
	"math"
)

func getPossibleNextPositions(position []int, dimensions []int) chan []int {
	coordinatesChannel := make(chan []int)
	go func() {
		for dimension, dimensionPosition := range position {
			if dimensionPosition > 0 {
				newPosition := make([]int, len(position))
				copy(newPosition, position)
				newPosition[dimension] = dimensionPosition - 1
				coordinatesChannel <- newPosition
			}

			if dimensionPosition < dimensions[dimension]-1 {
				newPosition := make([]int, len(position))
				copy(newPosition, position)
				newPosition[dimension] = dimensionPosition + 1
				coordinatesChannel <- newPosition
			}
		}
		close(coordinatesChannel)
	}()
	return coordinatesChannel
}

type PositionAndSteps struct {
	position []int
	steps    int
}

func PopPosition(queue *[]PositionAndSteps) (val PositionAndSteps) {
	last := len(*queue) - 1
	val = (*queue)[last]
	*queue = (*queue)[:last]
	return val
}

func PushPosition(queue *[]PositionAndSteps, val PositionAndSteps) {
	(*queue) = append(*queue, val)
}

func findNumberOfPaths(position []int, dimensions []int, steps int) int {
	var count int
	positions := make([]PositionAndSteps, 1)
	positions[0] = PositionAndSteps{position, steps}
	// fmt.Println("Starting with position ", positions[0])

	for len(positions) > 0 {
		// fmt.Println("N Positions: ", len(positions))
		currentPositionAndStep := PopPosition(&positions)

		if currentPositionAndStep.steps == 0 {
			count = int(math.Mod(float64(count+1), 1000000007))
			continue
		}

		positionsChan := getPossibleNextPositions(currentPositionAndStep.position, dimensions)
		for newPosition := range positionsChan {
			newPositionAndSteps := PositionAndSteps{newPosition, currentPositionAndStep.steps - 1}
			// fmt.Println("Pushing new position ", newPositionAndSteps)
			PushPosition(&positions, newPositionAndSteps)
		}
	}
	return count
}

func main() {
	// read in row/col pair of pacman
	var numberOfTestCases int
	_, err := fmt.Scanln(&numberOfTestCases)
	if err != nil {
		log.Fatal("Bad input: numberOfTestCases")
	}

	for testCaseNumber := 0; testCaseNumber < numberOfTestCases; testCaseNumber++ {
		var numberOfDimensions, numberOfSteps int
		_, err = fmt.Scanln(&numberOfDimensions, &numberOfSteps)
		if err != nil {
			log.Fatal("Bad input: numberOfDimensions, numberOfSteps")
		}

		position := make([]int, numberOfDimensions)
		dimensions := make([]int, numberOfDimensions)

		for i, _ := range position {
			_, err = fmt.Scan(&position[i])
			if err != nil {
				log.Fatal("Error scanning position. ", err)
			}
			position[i] = position[i] - 1
		}

		for i, _ := range dimensions {
			_, err = fmt.Scan(&dimensions[i])
			if err != nil {
				log.Fatal("Error scanning dimensions. ", err)
			}
		}

		numberOfPaths := findNumberOfPaths(position, dimensions, numberOfSteps)
		fmt.Println(numberOfPaths)
	}
}
