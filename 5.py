def fib(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fib(i-2) + fib(i-1)
    

n = 12
li = []
for i in range(12):
    li.append(fib(i))

print(li)