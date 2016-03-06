package main

/*
https://www.hackerrank.com/challenges/grid-walking
*/

import (
	"fmt"
	"log"
	"math"
)

type NDArray struct {
	dimensionRunningProduct []int
	values                  []int
}

func ComputeRunningProduct(dimensions *[]int) []int {
	dimensionRunningProduct := make([]int, len(*dimensions))
	dimensionRunningProduct[0] = 1
	for i := 1; i < len(*dimensions); i++ {
		dimensionRunningProduct[i] = dimensionRunningProduct[i-1] * (*dimensions)[i-1]
	}
	// fmt.Println("Running Product ", dimensionRunningProduct)
	return dimensionRunningProduct
}

func (ndarray *NDArray) GetCoodinateIndex(coordinates []int) int {
	coordinateIndex := 0
	for i, coordinate := range coordinates {
		coordinateIndex += ndarray.dimensionRunningProduct[i] * coordinate
	}
	// fmt.Println(coordinates, " idx: ", coordinateIndex)
	return coordinateIndex
}

func (ndarray *NDArray) SetValue(coordinates []int, value int) {
	idx := ndarray.GetCoodinateIndex(coordinates)
	ndarray.values[idx] = value
}

func (ndarray *NDArray) GetValue(coordinates []int) int {
	idx := ndarray.GetCoodinateIndex(coordinates)
	// fmt.Println(ndarray.values)
	return ndarray.values[idx]
}

func MakeNDArray(dimensions *[]int) *NDArray {

	var numberOfElements = 1
	for _, dim := range *dimensions {
		numberOfElements *= dim
	}

	allocatedSlice := make([]int, numberOfElements)
	for i := 0; i < numberOfElements; i++ {
		allocatedSlice[i] = 1
	}

	dimensionRunningProduct := ComputeRunningProduct(dimensions)
	ndarray := NDArray{dimensionRunningProduct, allocatedSlice}

	return &ndarray
}

func numberOfNeighbors(coordinates *[]int, dimensions *[]int) int {
	neighbors := 0
	for i, coordinate := range *coordinates {
		if coordinate-1 >= 0 {
			neighbors += 1
		}
		if coordinate+1 < (*dimensions)[i] {
			neighbors += 1
		}
	}
	return neighbors
}

func enumeratePositions(dimensions *[]int) chan *[]int {
	coordinatesChannel := make(chan *[]int)
	go func() {
		stack := make([]int, len(*dimensions))
		for {
			ptr := len(*dimensions) - 1
			coordinates := make([]int, len(*dimensions))
			copy(coordinates, stack)
			coordinatesChannel <- &coordinates
			stack[ptr] += 1
			for stack[ptr] >= (*dimensions)[ptr] {
				if ptr == 0 {
					close(coordinatesChannel)
					return
				}
				stack[ptr] = 0
				ptr -= 1
				stack[ptr] += 1
			}
		}
	}()
	return coordinatesChannel
}

func getNeighbors(position *[]int, dimensions *[]int) chan *[]int {
	coordinatesChannel := make(chan *[]int)
	go func() {
		for dimension, dimensionPosition := range *position {
			if dimensionPosition > 0 {
				newPosition := make([]int, len(*position))
				copy(newPosition, *position)
				newPosition[dimension] = dimensionPosition - 1
				coordinatesChannel <- &newPosition
			}

			if dimensionPosition < (*dimensions)[dimension]-1 {
				newPosition := make([]int, len(*position))
				copy(newPosition, *position)
				newPosition[dimension] = dimensionPosition + 1
				coordinatesChannel <- &newPosition
			}
		}
		close(coordinatesChannel)
	}()
	return coordinatesChannel
}

func findNumberOfPaths(position *[]int, dimensions *[]int, steps int) int {
	ndarray0 := MakeNDArray(dimensions)
	ndarray1 := MakeNDArray(dimensions)

	for step := 0; step < steps; step++ {
		for coordinates := range enumeratePositions(dimensions) {
			sum := 0
			for neighbor := range getNeighbors(coordinates, dimensions) {
				// fmt.Println(coordinates, " -> ", neighbor)
				sum += ndarray0.GetValue(*neighbor)
				// sum = int(math.Mod(float64(sum), 1000000007))
				// TODO: Mod logic check
			}
			ndarray1.SetValue(*coordinates, sum)
		}

		ndarray0, ndarray1 = ndarray1, ndarray0
	}

	return ndarray0.GetValue(*position)
}

func main() {
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

		numberOfPaths := findNumberOfPaths(&position, &dimensions, numberOfSteps)
		fmt.Println(int(math.Mod(float64(numberOfPaths), 1000000007)))
		// fmt.Println(numberOfPaths)
	}
}
