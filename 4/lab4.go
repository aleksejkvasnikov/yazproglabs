package main
import (
	"fmt"
	"time"
)

type Token struct {
	data string
	recipient int
}

func main() {
	token := Token{data: "token", recipient: 10}
	go thread(1, token)
	time.Sleep(100 * time.Millisecond)
}

func thread(i int, t Token) {
	if (t.recipient == i) {
		fmt.Println("data:", t.data," recipient:",i)
	} else {
		go thread(i+1, t)
	}
}