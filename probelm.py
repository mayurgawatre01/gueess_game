x=[1,2,3,4,5]
even_sum=0
odd_sum=0
for i in range(len(x)):
    if x[i]%2==0:
        even_sum+=x[i]
    else:
        odd_sum+=x[i]
print(even_sum,odd_sum)