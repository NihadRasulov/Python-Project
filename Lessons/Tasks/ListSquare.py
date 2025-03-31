def square(num):
    arr = []
    for i in range(1,num+1):
        if i <= num:
            arr.append(i*i)
    return arr
print(square(20))