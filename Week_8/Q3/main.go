package main

import "fmt"

func letter(score int) string {
	var grade string

	if score >= 90 {
		grade = "A"
	} else if score >= 80 {
		grade = "B"
	} else if score >= 70 {
		grade = "C"
	} else {
		grade = "F"
	}
	if score%10 >= 7 && grade != "A" && grade != "F" {
		grade += "+"
	} else if score%10 <= 3 && grade != "F" {
		grade += "-"
	}
	return grade
}

func main() {
	// Example usage
	score := 91
	fmt.Printf("The grade for score %d is: %s\n", score, letter(score))
}
