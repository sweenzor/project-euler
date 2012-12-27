package main

import "fmt"
import "math/big"

func main() {

    a := big.NewInt(0)
    b := big.NewInt(1)
    count := 1

    for len(b.String()) < 1000 {

        b = big.NewInt(0).Add(a, b)
        a = big.NewInt(0).Sub(b, a)
        count += 1

    }

    fmt.Printf("%v\n", count)

}
