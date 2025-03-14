l = []
start = ord('a') - 1
for i in range(4):
    a = []
    for j in range(4):
        if i == 0:
            if j == 0:
                j = '*'
            else:
                if j == 0:
                    j = chr(start)
                else:
                    j = format('x', '>2')
        a.append(str(format(j, '>2')))
    start += 1
    l.append(a)

for i in l:
    print(' '.join(i))