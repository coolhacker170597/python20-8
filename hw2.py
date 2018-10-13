import sys

num_steps = int(sys.argv[1])

i = 1
while i <= num_steps:
    print(" " * (num_steps-i) + "#" * i)
    i += 1
