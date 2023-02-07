package main

import (
	"fmt"
	"net/http"
	"sync"
	"time"
)

func main() {
	var wg sync.WaitGroup
	wg.Add(1000)

	stop := make(chan struct{})
	go func() {
		time.Sleep(time.Minute)
		close(stop)
	}()

	start := time.Now()
	var requestCount int
	for i := 0; i < 1000; i++ {
		go func() {
			defer wg.Done()

			for {
				select {
				case <-stop:
					return
				default:
					res, err := http.Get("http://localhost:8080/health")
					if err != nil {
						fmt.Println(err)
						return
					}

					if res.StatusCode != http.StatusOK {
						fmt.Println("Unexpected status code:", res.StatusCode)
					}

					requestCount++
				}
			}
		}()
	}

	wg.Wait()
	elapsed := time.Since(start)
	rps := float64(requestCount) / float64(time.Minute/time.Second)
	fmt.Printf("Sent %d requests in %s\n", requestCount, elapsed)
	fmt.Printf("Requests per second: %.2f\n", rps)
}