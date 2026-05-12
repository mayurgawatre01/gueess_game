'''a=90
b=89
c=34
x=min(a,b,c)
print(c)
if a<b and a<c:
    print("a is smaller ")
elif b<a and b<c:
    print(" b is smaller")
else:
    print("c is smaller")'''
    
'''n=int(input("enter the year to check leap year : "))
if n%4==0 and n%100 !=0 or n%400==0:
    print("it is a leap year ")
else:
    print("not a leap year")'''

'''n=int(input())
for i in range(1,n+1):
    print(i)'''


'''n=int(input())
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)'''


'''n=int(input())
for i in range(1,n+1):
    if i%2==0:
        print(i)'''
    

n=int(input())
count=0
for i in range(1,n+1):
    if i%3==0:
        count+=1
print(count)

        