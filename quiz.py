import random

def generateProblem(lower, upper):

    #set both integers to a random number in-between the range given
    int1 = random.randint(lower, upper)
    int2 = random.randint(lower, upper)

    #store correct answer into a variable
    correct_answer = int1 + int2

    #ask the user for his answer, and store it in a variable
    user_answer = input(f"What is {int1} + {int2}?: ")

    #check if input is an integer
    try:
       type = int(user_answer)
    except ValueError:
       print("Error! Input must be a number, please try again.")
       user_answer = input(f"What is {int1} + {int2}?: ")

    #check if the user_answer is equal to the correct_answer

    if int(user_answer) == correct_answer:
        return True
    else:
        return False

#introduction to quiz game
def intro():
    print("****** Addition Quiz ******")
    print("Choose the Difficulty Level.")

    #ask user for Difficulty level and store it in a variable
    level = input("(E)asy, (I)ntermediate, (H)ard: ")

    #check which level they chose, and call generateProblem 3 times with appropiate parameters,
    #storing the True or False values into variables
    if level == "E" or level == "e":
        question1 = generateProblem(0,10)
        question2 = generateProblem(0,10)
        question3 = generateProblem(0,10)
        checkScore(question1, question2, question3)


    elif level == "I" or level == "i":
        question1 = generateProblem(0,20)
        question2 = generateProblem(0,20)
        question3 = generateProblem(0,20)
        checkScore(question1, question2, question3)


    elif level == "H" or level == "h":
        question1 = generateProblem(-20,20)
        question2 = generateProblem(-20,20)
        question3 = generateProblem(-20,20)
        checkScore(question1, question2, question3)

    else:
        #if the level chosen is invalid, run this function again
        print("Invalid Level! Try again.")
        print()
        intro()

def checkScore(question1, question2, question3):
        #start calculating final scores
        score = 0

        if question1 == True:
            print("Question 1: Correct")
            score += 1
        else:
            print("Question: 1: Incorrect")

        if question2 == True:
            print("Question 2: Correct")
            score += 1
        else:
            print("Question: 2: Incorrect")


        if question3 == True:
            print("Question 3: Correct")
            score += 1
        else:
            print("Question: 3: Incorrect")

        print("Final Results:")
        print(f"{score}/3 == {score/3 * 100}%")


intro()
