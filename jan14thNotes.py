# Eric Browne
import sys
for val in "Stdout is cool!".split():
    sys.stdout.write(val + '\n')
for val in "Printing is cool!".split():
    print(val)
print("Noting went wrong")
print("Something went wrong", file = sys.stderr)
sys.stderr.write("Something went wrong\n")  #the same thing as line 8
def process_file(file):
    #Does something with the file.

def main():
    filenames = sys.argv[1:]
    if filenames:
        for name in filenames:
            with open(name) as f:
                process_file(f)
    else:
        process_file(sys.stdinn)
