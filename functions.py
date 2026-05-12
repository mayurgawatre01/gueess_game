def greet():
    print("hello")
greet()

def add(a,b):
    print(a+b)
add(24,4)

def add(a,b):
    return a+b
result=add(34,45)
print(result)


def list_sum(x):
    total=0
    for i in  x:
        total+=i
    return total
print(list_sum([5689,79,678]))


def list_sum(x):
    total=0
    for i in x:
        total=total+i
    return total
print(list_sum([6978,7898,1003]))


def even_count(x):
    count=0
    for i in x:
        if i%2==0:
            count+=1
    return count
print(even_count([787,334,3,43,42,4,4]))

def max_num(x):
    max_val=float("-inf")
    for num in x:
        if num>max_val:
            max_val=num
            
    return max_val
print(max_num([67,56,45,78,90]))


def sum_list(x):
    total=0
    for num in x:
        total+=num
    return total
print(sum_list([344,5,5,6,7,78]))


def count_odd(x):
    count=0
    for num in x:
        if num%2!=0:
            count+=1
    return count
print(count_odd([90,9,8,7,6,5,4,3,21,56]))
        
        
f=lambda a:a*3
print(f(10))


def three_sum(x):
    sum=0
    for num in x:
        sum=sum+num
    return sum
print(three_sum([34,56,10]))

def three_pro(x,y,z):
    return x*y*z
print(three_pro(34,56,10))
        
        
def f(a, b):
    return a + b

print(f([1,2], [3,4]))

x = [1, 2, 3, 4]
print(x[0])
x.append(5)
for num in x:
    print(num)

d = {"name": "Mayur", "marks": 90}
print(d["name"])

for key in d:
    print(key,d[key])
    
d["age"]=20

for key in d:
    print(key,d[key])
    
x = [1, 2, 3, 4]
x[0]=9
print(x)


s = {1,2,2,3,555,555,6,6,6,5,5,5,4,3,3,2,1,1,2,3,3,5}
print(s)   # {1,2,3}

d = {"a":10, "b":20}
for i in d:
    print(i,d[i])
    
x = [1,2,3,4,5]
count=0
for num in x:
    count+=1
    
print(count)

x = [1,2,2,3,3,4]
x=set(x)
print(x)

