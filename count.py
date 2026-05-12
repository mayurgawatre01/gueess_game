x=[2,7,3,8,1]
count=0
for i in range(len(x)):
    if x[i]<5:
        count+=1
print(count)


x=[4,6,8,3,7]
sum=0
for i in range(len(x)):
    if x[i]%1==0:
        sum+=x[i]
    
print(sum)