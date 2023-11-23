import random

num1 = random.randint(1, 99)
num2 = random.randint(1, 99)
symbol = random.choice(["+", "-", "*", "/"])
answer = 0

if symbol == "+":
    answer = num1+num2
elif symbol == "-":
    answer = num1-num2
elif symbol == "*":
    answer = num1*num2
elif symbol == "/":
    answer = round(num1/num2, 2)
    if answer.is_integer():
        answer = num1//num2


print(f"What is {num1}{symbol}{num2}?")

response = input("Answer: ")
response = float(response)
if response == answer:
    print("Correct")
else:
    print("Wrong")
