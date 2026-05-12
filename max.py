x = [3, 7, 2, 9, 4]
largest=x[0]

for i in range(len(x)):
    if x[i]>largest:
        largest=x[i]
print(largest)