import random
import time

OPERANTORS =["+","-","/","*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEM = 10

def generate_problem():
    left = random.randint(MIN_OPERAND,MAX_OPERAND)
    right = random.randint(MIN_OPERAND,MAX_OPERAND)
    operator =random.choice(OPERANTORS)

    expr = str(left)+" "+operator+" "+str(right)
    ans = eval(expr)
    return expr , ans

wrong =0
input("press enter to start !!")
print("....................")

start_time = time.time()
for i in range(TOTAL_PROBLEM):
    expr , ans = generate_problem()
    while True:
        guess=input("problem #"+str(1+i)+": " + expr+"= ")
        if guess == str(ans):
            break
        else:
            wrong+=1
            break

end_time = time.time()
total_time = round(end_time-start_time,2)

print("<.....................>")
print("you finish the work in ",total_time,"sec!")
print("you curect the ans= ",10-wrong,", wrong the ans =",wrong)
