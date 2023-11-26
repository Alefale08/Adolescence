print("Welcome to my computer quiz!")

playing = input("Do you want play? ").lower()

if playing != "yes":
    quit()

print("Okay! Let's play:)")
score=0

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does Gpu stand for? ").lower()
if answer == "graphic processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does Ram stand for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ").lower()
if answer == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " question correct!" )
print("You got " + str((score/4 * 100)) + " %." )