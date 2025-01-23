Date: 10/10/2021 <br />
Name: Brady Johnson <br />
IDE: IntelliJ IDEA <br />
Language version: JDK 23 <br />

For the most part C++ and Java are very similar. They are both strongly typed language and the number handling is very 
similar. The syntax is slightly different by easy enough to convert. However, the cin vs scanner behavior was frustrating.
Further, I am not sure why, but I was running the C++ code in CLion and all the "errors" or odd behavior created by overflows and 
type mismatches were being swallowed. Even after I removed return(0) from the end of the do-while loop I still was not 
seeing error logging anywhere. I find this to be bizarre behavior. IDK if this is normal behavior or my editor. Anyways I 
did some readying and through experimenting and testing figured out some things described in the paragraphs below.

Java value overflow and C++ value overflow fail differently. When C++ value
overflow happens it defaults returns the max integer value and the object goes into a failed state. This
failed state persists in the FOR loop and does not allow new values to be read. Since the number variable
is declared outside the cin object the number value persists as the initial default from the initial
failed read. The final result is an infinite loop in the main function.

From my reading and observation about the Java Scanner object. It will throw the error up to the calling function to be dealt with.
In my opinion this is fantastic. However, I need to mimic C++ and to do this I need to create an infinite
 loop based on the criteria of the value overflow in C++.