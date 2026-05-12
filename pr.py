x=[34,44,57,653]
largest=x[0]
for i in range(len(x)):
    if x[i]>largest:
        largest=x[i]
print(largest)