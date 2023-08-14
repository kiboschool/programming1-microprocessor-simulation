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
nand 1 1
```

At each step, our model of a processor outputs a value. For this
pretend program, the output at each step would be:

```txt
24
30
1
0
```

## Processor Operations

Below are the processor operations that you should support, and what they should do.

| Operation 	| Description                           	| Sample       	| Output 	|
|-----------	|---------------------------------------	|--------------	|--------	|
| noop      	| Do nothing, print empty line          	| noop         	|        	|
| add       	| Add arguments                         	| add 3 140    	| 143    	|
| mul       	| Multiply arguments                    	| mul 10 21    	| 210    	|
| gt        	| Check if first is greater than second 	| gt 3 10      	| 0      	|
| or        	| Logical or                            	| or 6 0       	| 1      	|
| nand      	| Logical nand ("not and")              	| nand 1 1     	| 0      	|
| min       	| Find the minimum value of arguments   	| min 14 8 103 	| 8      	|
| shift     	| Shift left by a number of bits        	| shift 8 2    	| 32     	|
| invalid     | Any non-valid operations                | not an op     | invalid operation not an op |

**Notes:**

* All of the operations are defined for integer arguments. Floats or other 
    arguments are invalid.
* Most operations take exactly two arguments.
* `noop` takes no arguments (it should be invalid if there are any arguments). 
    `min` should work with 2 or more arguments.
* The logical `or` and `nand` operations always print out a `0` or `1`, no matter
    their inputs. 0 is treated as false, any other number is treated as true.
* `shift` takes the bit representation of its argument, and moves the bits left,
    with the number of places to shift given by the second argument. So, 8
    (00001000) gets shifted left by 2 to become 32 (00100000).
* `shift` is only defined for positive arguments. It is invalid for negative numbers or zero.
* For our processor, numbers have arbitrarily many bits. Don't worry about
    overflow or truncation for `add`, `mul`, or `shift`.
* If the processor encounters an invalid operation, it should print an error 
    message and stop.

## Explanation
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/HadN-JODWnE/0.jpg)](https://www.youtube.com/watch?v=HadN-JODWnE)


## Starter Code

`main.py` has the function `run` already written for you. It reads a file
containing a program and calls the `process` function on each line.

There is also a `__name__ == "__main__"` module guard, to call the run function 
if the file is executed on the command line.

Your task is to implement the `process` function (right now it just prints each 
line) and any helper functions you need.

## Testing

As you develop your program, try running your helper functions with sample
inputs, to check that they are returning the results you expect. To run the
first whole sample program, enter `python main.py sample1.txt` in the terminal.
You can use the same pattern for the other samples, or write your own sample.

The automated tests will call the `process` or `run` function with some sample 
operations or programs, and check that the functions print the correct result. 
How you organize your code is up to you -- your helper functions are not tested 
directly in the automated tests.

## Hints

First, you'll need to turn the line of input into an operation and its
arguments. All of the values in the programs will be ints, so you should convert
the values from strings.

In order to write this program effectively, you should split the problem into
lots of small functions, and then use a single function to decides which other 
function to call.

Note: Python has built-in functions called `or` and `min`, so you can't use
those as names of functions in your code. Rename the functions to something
else.

## Communicate Project Status

Your manager, Nancy, would like a status update describing your work on developing the microprocessor simulation.  Write an email message (in the file called `ProjectSummary.txt`) to Nancy that provides a high-level description of how the program functions, and outlines the portion of the work that you found most challenging and how you overcame that challenge.  Remember that Nancy is busy!  She is managing a team of 15 people and will be reviewing everyone's status update each week.  Nancy is a technical manager, so she understands software development; however, she probably doesn't need a line-by-line explanation of your code. It's important that your message is clearly and concisely addresses the above two points as efficiently as possible. 

### Assessment

A key component of being successful as a Software Engineer (or, more generally, in a technical field) is being able to communicate effectively about the work that you are doing.  This includes clearly conveying details about the complexities of the problems that you're working on, and explaining how your solution works.  Therefore, we will use the 7Cs of Communication (remember this from Communicating for Success?) to assess your message to Nancy:


| Criteria    | Proficient (3)      | Competent (2)     | Developing (1)   |
|-------------|--------------------|-------------------|------------------|
| Clarity     | The email is exceptionally clear and easy to understand, utilizing straightforward language tailored for Nancy. | The email is clear, though minor instances of unnecessary complexity or ambiguity may be present. | The email lacks clarity, with convoluted language that might hinder Nancy's understanding. |
| Conciseness | The email efficiently addresses both points, providing a high-level description of the program's function and addressing the challenging portion succinctly. | The email is mostly concise, though some areas could be more succinct while still covering the required information. | The email tends to be wordy, potentially overwhelming Nancy with unnecessary details. |
| Concreteness| The email includes specific examples or details to illustrate the program's function and the challenging portion, aiding Nancy's comprehension. | The email provides some concrete details, but further elaboration and examples could enhance clarity. | The email lacks specific examples or specifics, making it challenging for Nancy to visualize the content. |
| Correctness | The email is accurate and error-free, maintaining a professional tone and polished language. | The email contains minor errors that do not significantly affect the overall accuracy and professionalism. | The email has noticeable errors in grammar, spelling, or tone that detract from the message's credibility. |
| Coherence   | The email is well-organized, presenting information in a logical sequence that aligns with the task's requirements. | The email is structured logically, though some areas might benefit from improved organization. | The email lacks a clear structure, making it challenging for Nancy to follow the flow of information. |
| Completeness| The email fully addresses both points, offering a comprehensive high-level description and explanation of the challenging portion. | The email covers both points but might lack depth in either the program's function or the explanation of the challenge. | The email omits significant aspects of either the program's function or the challenge, impacting Nancy's understanding. |
| Courtesy    | The email demonstrates consideration for Nancy's busy schedule and technical understanding, using a respectful and considerate tone. | The email acknowledges Nancy's role and technical understanding, though some sections might be overly casual or unintentionally insensitive. | The email lacks consideration for Nancy's perspective, potentially coming across as dismissive or inconsiderate. |
