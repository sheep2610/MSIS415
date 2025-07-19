#program to generate am random number between 0 and 9
import random

# two random numbers between 0 and 9
x = random.randint(0, 9)
print(x)
y = random.randint(0, 9)
print(y)

#ask the answer of user
your_answer = int(input("What is your answer of product? "))

#correct answer
correct_answer= x*y

# check the answer
if your_answer == correct_answer:
    print("Congratulation! Your answer is correct!")
else:
    print("Sorry! Your answer is incorrect. The correct answer is", correct_answer,"!") 



