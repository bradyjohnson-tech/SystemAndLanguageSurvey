Date: 11/19/2021 <br />
Name: Brady Johnson <br />
IDE: IntelliJ GOLAND <br />
Language version: go version go1.23.3 darwin/arm64 <br />

Becuase GO is statically typed it took a bit of snooping around the internet to find out how
to create a way to pass multiple types into a method. There is a slight difference in the behavior 
however. My GO version returns an array of bigInt while python can return int or long. The other
slight difference is a lack of comma between numbers in the array when printing. I thought about 
returning an array of type string to rectify this but decided it would be a very major change in the 
method signature. If I was a service calling this method, I would expect a return of an array numbers
not an array of sting. This was my thinking in making this decision. I hope you agree.  
