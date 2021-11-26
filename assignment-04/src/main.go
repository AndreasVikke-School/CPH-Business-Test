package main

import (
	"errors"
)

func Hello(name string) (string, error) {
	if name == "" {
		return "", errors.New("empty name")
	}

	return `Hello("` + name + `")`, nil
}

// func main() {
// 	_ = fmt.Println
// }
