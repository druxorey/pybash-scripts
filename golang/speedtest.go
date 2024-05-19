package main

import (
	"fmt"
	"time"
)

func main() {
	start := time.Now()
	number := 50000000	

	for i := 0; i < number; i++ {
	}

	elapsed := time.Since(start)
	fmt.Printf("Counting to %d in Go took %s\n",number , elapsed)
}
