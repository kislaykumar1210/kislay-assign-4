import random

# Set the number of questions
num_questions = 10

# Set the correct and incorrect counters
correct = 0
incorrect = 0

# Generate the questions
for i in range(num_questions):
  # Generate two random numbers
  x = random.randint(1, 9)
  y = random.randint(1, 9)
  
  # Calculate the correct answer
  answer = x * y
  
  # Print the question
  print("Question", i+1, ":", x, "x", y, "=", end=" ")
  
  # Get the user's answer
  user_answer = int(input())
  
  # Check the answer
  if user_answer == answer:
    print("Right!")
    correct += 1
  else:
    print("Wrong. The answer is", answer)
    incorrect += 1

# Print the final score
print("You got", correct, "questions correct and", incorrect, "questions incorrect.")
