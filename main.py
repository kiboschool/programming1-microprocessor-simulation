# Microprocessor simulation
# supports a small set of simulated operations
# prints the output for each operation
import sys

# You need to update the process function to actually handle the operations. To
# start, it just prints out each line of the input.
def process(line):
    op, *args = line.split(' ')
    if len(args) == 2:
        a = int(args[0])
        b = int(args[1])
    if op == 'noop':
        noop()
    elif op == 'add':
        add(a,b)
    elif op == 'mul':
        mul(a,b)
    elif op == 'gt':
        gt(a,b)
    elif op == 'or':
        log_or(a,b)
    elif op == 'nand':
        nand(a,b)
    elif op == 'min':
        minm(a,b)
    elif op == 'shift':
        shift(a,b)
    else:
        print("invalid operation", line)

def noop():
    print()

def add(a,b):
    print(a + b)

def mul(a,b):
    print(a * b)

def gt(a,b):
    if a > b:
        print(1)
    else:
        print(0)

def log_or(a,b):
    if a or b:
        print(1)
    else:
        print(0)

def nand(a,b):
    if a and b:
        print(0)
    else:
        print(1)

def minm(*args):
    smallest = args[0]
    for arg in args:
        if arg < smallest:
            smallest = arg
    print(smallest)

def shift(a, b):
    if a > 0 and b > 0:
        print(a << b)

# The run function is provided, you don't need to change it.
# It reads all the lines from a file, then calls the process function
#   for each line 
def run(filename):
    with open(filename, 'r') as file:
        for operation in file.readlines():
            process(operation.strip())

# This code will call the run function with a filename, if it's provided on the 
# command line. It would pass samples/sample2.txt with this invocation:
# python3 main.py samples/sample2.txt
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python main.py [path/to/sample]")
    else:
        run(sys.argv[1])
