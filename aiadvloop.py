'''i=10
while i>=1:
    if i%2==0:
        print(i)
    i-=1'''
    
#forloop

'''i=10
for i in range(10,0,-1):
    if i%2==0:
        print(i)


for i in range(1,21,1):
    if i%4==0:
        continue
    print(i)'''
    
count=0
for i in range(1,51,1):
    if i%3==0 and i%5==0:
        count+=1
print(count)