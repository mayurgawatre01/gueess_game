x = [3, 7, 2, 9, 4]
even_count=0
odd_total=0
for i in range(len(x)):
    if x[i]%2==0:
        even_count+=1
    else:
        odd_total=odd_total+x[i]
    
    
print(odd_total)
print(even_count)