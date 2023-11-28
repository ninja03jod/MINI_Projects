print("Welcome to Quizz game")
playing = input("Do you want to play!: ").lower()

if playing != "yes":
    quit()

print("Okay lets play :)")
score = 0

answer = input("what does IDE stands for?: ")
if answer.lower() == "integrated development environment":
    print("Correct!")
    score +=1
else:
    print("Incorrect")

answer = input("Capital of USA?: ")
if answer.lower() == "washington,d.c.":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does CPU stands for?: ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does GPU stands for?: ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does PSU stands for?: ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does RAM stands for?: ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

print("You got",score,"questions correct!")
print("You got",((score/6) *100),"%.")