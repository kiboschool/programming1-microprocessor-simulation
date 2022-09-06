# Microprocessor Simulation

A microprocessor performs different operations on its inputs, based on a signal
that tells it which operation to perform.

A program, from the view of a microprocessor, is a set of operations and values.
It will perform each operation on the values, one by one. For our simplified
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

In this exercise, you'll write a function that pretends to be a processor.

In order to write this program effectively, you should split the problem into
lots of small functions, and then use a single 'dispatcher' function that 
decides which other function to call.

## Processor Operations

Here are the processor operations that you should support, and what they should
do:

- noop
- add
- mul
- min
- greater
- or
- and
- invert
- bitshift

## Testing

As you develop your program, try running your helper functions with sample
inputs, to check that they are returning the results you expect. To run the
first whole sample program, enter `python main.py sample1.txt` in the terminal.
You can use the same pattern for the other samples, or write your own sample.

The automated tests will call your main function with some sample processor 
programs, and check that it prints the correct result. How you organize your
code is up to you -- your helper functions are not tested in the automated
tests.
