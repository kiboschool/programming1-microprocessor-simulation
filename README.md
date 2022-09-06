# Microprocessor Simulation

A microprocessor performs different operations on its inputs, based on a signal
that tells it which operation to perform.

In this exercise, you'll write code to simulate what a processor does.

A program, from the view of a microprocessor, is a set of operations and values.
The processor will perform each operation on the values, one by one. For our simplified
example, it might look like:

```txt
add 8 16
mul 10 3
or 1 0
and 1 0
```

At each step, our model of a processor outputs a value. For this
pretend program, the output at each step would be:

```txt
32
30
1
0
```


## Processor Operations

Below are the processor operations that you should support, and what they should
do. If the processor encounters an invalid operation, it should print an error message and stop.

| Operation 	| Description                           	| Sample       	| Output 	|
|-----------	|---------------------------------------	|--------------	|--------	|
| noop      	| Do nothing, print empty line          	| noop         	|        	|
| add       	| Add arguments                         	| add 3 140    	| 143    	|
| mul       	| Multiply arguments                    	| mul 10 21    	| 210    	|
| gt        	| Check if first is greater than second 	| gt 3 10      	| 0      	|
| min       	| Find the minimum value of arguments   	| min 14 8 103 	| 8      	|
| or        	| Logical or                            	| or 6 0       	| 1      	|
| nand      	| Logical nand ("not and")              	| nand 1 1     	| 0      	|
| shift     	| Shift left by a number of bits        	| shift 8 2    	| 32     	|
| invalid     | Any non-valid operations                | not an op     | invalid operation "not an op" |

Note that the logical `or` and `nand` operations should always print out a `0` or
`1`, no matter their inputs. Non-zero numbers are treated as true, 0 is treated
as false.

## Starter Code

`main.py` has the function `run` already written for you. It reads a file
containing a program and calls the `process` function on each line.

There is also a `__name__ == "__main__"` module guard, to call the run function if
the file is executed on the command line.

Your task is to implement the `process` function (right now it just prints each line) and any helper functions you need.

## Testing

As you develop your program, try running your helper functions with sample
inputs, to check that they are returning the results you expect. To run the
first whole sample program, enter `python main.py sample1.txt` in the terminal.
You can use the same pattern for the other samples, or write your own sample.

The automated tests will call your main function with some sample processor 
programs, and check that it prints the correct result. How you organize your
code is up to you -- your helper functions are not tested in the automated
tests.

## Hints

First, you'll need to turn the line of input into an operation and its
arguments. All of the values in the programs will be ints, so you should convert
the values from strings.

In order to write this program effectively, you should split the problem into
lots of small functions, and then use a single function to decides which other 
function to call.
