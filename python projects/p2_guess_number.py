import random
n = random.randint(1,50)
print("<-guess the number between 1 to 50->")
count =0
a =-1
while(a!=n):
    a=int(input("enter the number :"))
    if(a==n):
        count +=1 
        break
    elif(a>n):
        count +=1 
        print("lower number plzz")
    else:
        count +=1 
        print("higer number plzz")

print(f"you guess the number {a} after {count} times")