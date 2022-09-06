# Microprocessor simulation
# supports a small set of simulated operations
# prints the output for each operation
import sys

def get_args(stringargs):
    args = [] 
    for arg in stringargs:
        args.append(int(arg))
    return args

# You need to update the process function to actually handle the operations. To
# start, it just prints out each line of the input.
def process(line):
    op, *stringargs = line.split(' ')
    try:
        args = get_args(stringargs)
    except:
        op = 'invalid'

    if op == 'noop' and len(args) == 0:
        noop()
    elif op == 'add' and len(args) == 2:
        add(*args)
    elif op == 'mul' and len(args) == 2:
        mul(*args)
    elif op == 'gt' and len(args) == 2:
        gt(*args)
    elif op == 'or' and len(args) == 2:
        logical_or(*args)
    elif op == 'nand' and len(args) == 2:
        nand(*args)
    elif op == 'min' and len(args) >= 2:
        minimum(*args)
    elif op == 'shift' and len(args) == 2 and args[0] > 0 and args[1] > 0:
        shift(*args)
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

def logical_or(a,b):
    if a or b:
        print(1)
    else:
        print(0)

def nand(a,b):
    if a and b:
        print(0)
    else:
        print(1)

def minimum(*args):
    smallest = args[0]
    for arg in args:
        if arg < smallest:
            smallest = arg
    print(smallest)

def shift(a, b):
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
