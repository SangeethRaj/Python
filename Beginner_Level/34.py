fname = input()
num_lines = 0
with open(fname, 'r') as f:
    for line in f:
        num_lines += 1
print(num_lines)
