package main

import (
	"fmt"
	"time"
)

func main() {
	start := time.Now()

	for i := 0; i < 50000000; i++ {
	}

	elapsed := time.Since(start)
	fmt.Printf("El bucle for tomó %s\n", elapsed)
}
