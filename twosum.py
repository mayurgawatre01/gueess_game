x = [2, 7, 11, 15]
target=9
for i in range(len(x)):
    for j in range(i+1,len(x)):
        if x[i]+x[j]==target:
            print(x[i],x[j])
            print(i,j)
        
        
