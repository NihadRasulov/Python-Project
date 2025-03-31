l = []
start = ord('a') - 1
for i in range(4):
    a = []
    for j in range(4):
        if i == 0:  # First row (header row)
            if j == 0:
                a.append(format('*','>2'))  # First element in first row is '*'
            else:
                a.append(format(str(j),'>2'))  # Add numbers 1, 2, 3
        else:  # Other rows
            if j == 0:
                a.append(format(chr(start + i),'>2'))  # First column is 'a', 'b', 'c'
            else:
                a.append(format('x','>2'))
    l.append(a)

for i in l:
    print(' '.join(i))