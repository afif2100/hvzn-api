package main

import (
	"math/rand"
	"net/http"
	"log"
	"time"
	"fmt"
	"runtime"
)

func main() {

	numCPUs := runtime.NumCPU()
	runtime.GOMAXPROCS(numCPUs)

	http.HandleFunc("/animal", func(w http.ResponseWriter, r *http.Request) {
		animals := []string{"Lion", "Tiger", "Elephant", "Giraffe", "Cheetah"}
		randomIndex := rand.Intn(len(animals))
		randomAnimal := animals[randomIndex]
		log.Println("Received request to /animals endpoint")
		w.Write([]byte(randomAnimal))
	})

	http.HandleFunc("/health", func(w http.ResponseWriter, r *http.Request) {
		log.Println("Received request to /health endpoint")
		w.Write([]byte("OK"))
	})

	go func() {
		for {
			currentTime := time.Now()
			fmt.Println("API status: Running :", currentTime.Format(time.RFC1123))
			time.Sleep(5 * time.Second)
		}
	}()

	http.ListenAndServe(":8080", nil)
}