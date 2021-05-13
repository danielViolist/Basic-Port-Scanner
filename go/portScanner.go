package main

import (
	"fmt"
	"net"
	"os"
	"sort"
	"strconv"
)

func scan(ports, res chan int, address string) {
	for p := range ports {
		addr := fmt.Sprintf(address+":%d", p)
		conn, err := net.Dial("tcp", addr)
		if err != nil {
			res <- 0
			continue
		}
		conn.Close()
		res <- p
	}
}

func main() {
	if len(os.Args) != 3 {
		fmt.Println("Address argument required!")
		os.Exit(1)
	}
	address := os.Args[1]
	portRange, err := strconv.Atoi(os.Args[2])
	if err != nil {
		fmt.Println("Error with max port. String-to-int conversion failure.")
		os.Exit(2)
	}
	ports := make(chan int, 100)
	res := make(chan int)
	var open []int
	for i := 0; i < cap(ports); i++ {
		go scan(ports, res, address)
	}
	go func() {
		for i := 1; i <= portRange; i++ {
			ports <- i
		}
	}()
	for i := 0; i < portRange; i++ {
		port := <-res
		if port != 0 {
			open = append(open, port)
		}
	}
	close(ports)
	close(res)
	sort.Ints(open)
	for _, port := range open {
		fmt.Printf("%d open\n", port)
	}
}
