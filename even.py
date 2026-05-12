x = [2, 4, 6, 8]
is_true=False
for i in range(len(x)):
    if x[i]>5:
        is_true=True
        print(x[i])
    
    
x = [2, 4, 6, 8]
is_true=True
for i in range(0,4,1):
    if x[i]%2!=0:
        is_true=False
        break
    else:
        is_true=True
        print(x[i])