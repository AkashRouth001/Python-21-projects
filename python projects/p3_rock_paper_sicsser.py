import random
'''1 -> rock 
2 -> paper 
3 -> scissors '''
computer = random.choice([1, 2, 3])
youinp = input("enter your input(r,p,s) :")
yourDict = {"r": 1, "p": 2, "s": 3}
revyourDict = {1: "rock", 2: "paper", 3: "scissors"}
you = yourDict[youinp]
print(f"you chose {revyourDict[you]}\n computer {revyourDict[computer]}")
if (computer == you):
  print("match is draw")
else:
  if (computer == 1 and you == 2) or (computer == 2
                                      and you == 3) or (computer == 3
                                                        and you == 1):
    print("you win")
  else:
    print("computer win")
