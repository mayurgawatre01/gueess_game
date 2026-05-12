import random
jackpot=random.randint(0,1000)
guess=int(input("enter the number"))
count=1
while guess != jackpot:
    if guess <jackpot :
        print("guess higher")
    else:
        print("guess lowwer")
    guess=int(input("guess again"))
    count+=1
print("correct")
print(count)
    
    
    
    