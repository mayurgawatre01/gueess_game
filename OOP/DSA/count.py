'''n=-98765678
num=abs(n)

if num ==0:
    count=1
else:
    count=0
    while num >0:
        count+=1
        num=num//10
print(count)'''

#with list and without abs 

nums=-987656789
count=0

if nums<0:
    nums=-nums
if nums==0:
    count+=1
else:
    while nums>0:
        count+=1
        nums=nums//10
print(count)