import sys

for line in sys.stdin:
    line = line.rstrip()
    if line.isnumeric():
        print("integer")
    elif line[0] == '[' and line.endswith(']') and isinstance(line.split(','), list):
    #isinstance(line, list):
            print("list")
    else:
        print("string")