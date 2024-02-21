n = (input("Enter numbers seperated by spaces "))
nlist = [int(num) for num in n.split()]

if not nlist:
    print('list is empty')
else:
    largest = nlist[0]
    for i in nlist:
        if i > largest:
            largest = i
        
print(largest)
