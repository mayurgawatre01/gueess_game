x = [2, 7, 4, 9, 6]
is_true=False
for num in x:
    if num%2!=0 and num>5: 
        is_true=True
        break
if is_true:
    print("yes")
else:
    print("no")
        