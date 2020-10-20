# Eric Browne
import sys
def main():
    sum = 0
    for arg in sys.argv:
        sum += int(arg)
    return sum
print(main())
