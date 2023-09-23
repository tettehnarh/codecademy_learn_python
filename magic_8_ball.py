# The Magic 8-Ball is a popular toy developed in the 1950s for fortune-telling or advice seeking.
# Write a magic8.py Python program that can answer any “Yes” or “No” question with a different fortune each time it executes.
# Magic 8-Ball, should I do this project?

# We’ll be using the following 9 possible answers for our Magic 8-Ball:

#     Yes - definitely
#     It is decidedly so
#     Without a doubt
#     Reply hazy, try again
#     Ask again later
#     Better not tell you now
#     My sources say no
#     Outlook not so good
#     Very doubtful

# The output of the program will have the following format:

# [Name] asks: [Question]
# Magic 8-Ball’s answer: [Answer]

# For example:

# Joe asks: Is this real life?
# Magic 8-Ball's answer: Better not tell you now

# Let’s get started!

# Module to generate a random number from a range
import random

name = "Tom"
question = "Would I win the lottery"
answer = ""

random_number = random.randint(1,9)
#print(random_number)

if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
else:
  answer = "Error"

if name:
  print(f"{name} asks: {question}")
else:
  print(f"Question: {question}")

if question:
  print(f"Magic 8-Ball's answer: {answer}")
else:
  print("No question asked")