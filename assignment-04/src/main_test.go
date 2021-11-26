package main

import (
	"regexp"
	"testing"
)

func TestHelloName(t *testing.T) {
	name := "Gladys"
	want := regexp.MustCompile(`\b` + name + `\b`)
	msg, err := Hello("Gladys")
	if msg != "" && err != nil {
		t.Fatalf("test")
	}

	if !want.MatchString(msg) || err != nil {
		t.Fatalf(`Hello("Gladys") = %q, %v, want match for %#q, nil`, msg, err, want)
	}
}

func TestHelloNameEmpty(t *testing.T) {
	_, err := Hello("")
	if err == nil {
		t.Fatalf("test")
	}
}
