print("-:welcome to the quize game:-")

play = input("do you wnat to play?(Yes/no) ")
if (play.lower() != "yes"):
    quit()
print("<-okk, baby lets play->")
num =0
ans=input("What is the capital of India?: ")
if(ans.lower()=="delhi"):
    print("Correct!")
    num = num+1
else:
    print("Incrrect")

ans=input("What is the currency of India?: ")
if(ans.lower()=="inr"):
    print("Correct!")
    num = num+1
else:
    print("Incrrect")

ans=input("India’s space agency acronym?")
if(ans.lower()=="isro"):
    print("Correct!")
    num = num+1
else:
    print("Incrrect")

ans=input("Premier tech institute in India?")
if(ans.lower()=="iit"):
    print("Correct!")
    num = num+1
else:
    print("Incrrect")

print(f"You get {num} out of 4")