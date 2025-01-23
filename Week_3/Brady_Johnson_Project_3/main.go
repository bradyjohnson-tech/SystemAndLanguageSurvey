package main

import (
	"fmt"
	"math/big"
	"reflect"
)

func tribonacci(n interface{}) []*big.Int {
	var bigN *big.Int

	switch v := n.(type) {
	case int:
		bigN = big.NewInt(int64(v))
	case int64:
		bigN = big.NewInt(v)
	case *big.Int:
		bigN = v
	default:
		panicMsg := fmt.Sprintf("Unsupported type: %v", reflect.TypeOf(n))
		panic(panicMsg)
	}
	return tribonacciBig(bigN)
}

func tribonacciBig(n *big.Int) []*big.Int {
	zero := big.NewInt(0)
	one := big.NewInt(1)
	two := big.NewInt(2)
	three := big.NewInt(3)

	if n.Cmp(zero) <= 0 {
		return []*big.Int{}
	} else if n.Cmp(one) == 0 {
		return []*big.Int{big.NewInt(0)}
	} else if n.Cmp(two) == 0 {
		return []*big.Int{big.NewInt(0), big.NewInt(1)}
	} else if n.Cmp(three) == 0 {
		return []*big.Int{big.NewInt(1), big.NewInt(1), big.NewInt(1)}
	}

	fibSeq := []*big.Int{big.NewInt(1), big.NewInt(1), big.NewInt(1)}
	i := big.NewInt(3)
	for i.Cmp(n) == -1 {
		nextNum := new(big.Int).Add(fibSeq[len(fibSeq)-1], fibSeq[len(fibSeq)-2])
		nextNum.Add(nextNum, fibSeq[len(fibSeq)-3])
		fibSeq = append(fibSeq, nextNum)
		i.Add(i, one)
	}
	return fibSeq
}

func main() {
	fmt.Println(tribonacci(20))
	//fmt.Println(tribonacci(-20))
	//fmt.Println(tribonacci(0))
	//fmt.Println(tribonacci(1))
	//fmt.Println(tribonacci(3))
	//fmt.Println(tribonacci(4))
	//fmt.Println(tribonacci(5))
	////fmt.Println(tribonacci(2.2))
	////fmt.Println(tribonacci("hello"))
	//fmt.Println(tribonacci(6))
	//fmt.Println(tribonacci(7))
	//fmt.Println(tribonacci(1000))
	//fmt.Println(tribonacci(10000))
}
