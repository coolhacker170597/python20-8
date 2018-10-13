import sys

digit_string = sys.argv[1]

sum = 0

for x in digit_string:
    sum += int(x)

print(sum)