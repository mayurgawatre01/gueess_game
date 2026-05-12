x = [1, 6, 3, 8]
largest=float("-inf")
second=float("-inf")
for i in range(len(x)):
    if x[i]>largest:
        largest=x[i]
    if x[i]>second and x[i]!=largest:
        second=x[i]
print(largest,second)