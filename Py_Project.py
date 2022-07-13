print("Welcome user :) !  This project contains three games. The first one is a simple, too simple one; A calculator\n\n")


#Taking the input together using comma
a,b= eval(input("Enter two numbers separated by comma: "))

#Choice for performing the desired operation
n= eval(input("Enter ur choice: 1-add, 2- sub, 3- mul, 4- div: "))

#The operation corresponding to each choice
if (n==1):
    print("The sum is:", a+b)
elif (n==2):
    print("The difference is:", a-b)
elif (n==3):
    print("The product is:", a*b)
else:
    res= a/b
    print("The result of division is: %0.2f"%res)
#Here 0.2f is used to print the value upto 2 decimal points    
print("Very good! Get ready for the next game\n\n\n")

#Game of rock paper and scissors 

#Program for game of stone paper and scissors

print("Welcome to the game of rock paper and scissors!! (❁◡❁)\n")
from random import randint, choice

import random

k = randint(0, 2)

n= eval(input("Enter 0,1,2 for scissor, rock, paper\n"))

if(k==0):
      print("Computer has chosen scissor!")
elif(k==1):
      print("Computer has chosen rock!")
else:
      print("Computer has chosen paper!")


if(n==0):
      print("You have chosen scissor!")
elif(n==1):
      print("You have chosen rock!")
else:
      print("You have chosen paper!")

if(k==n):
    print("It is a draw")
elif(k==0):
    if(n==1):
          print("YOU WON")
    elif(n==2):
          print("Computer won")

elif(k==1):
    if(n==2):
          print("YOU WON")
    elif(n==0):
          print("Computer won")

elif(k==2):
    if(n==0):
          print("YOU WON")
    elif(n==1):
          print("Computer won")

print("Well played!! Now lets move forward to our next game. \n\n\n")

#QUIZ Game
def intro_message():
        """
        Introduces user to the quiz and rules, and takes an input from customer to start the quiz.
        Returns true regardless of any key pressed.
        """
        print("Welcome to this fun quiz! \nAre you ready to have some fun?\n")
        print("This game contains 3 different types of quizes,each containing 10 questions. You can skip a question anytime by typing 'skip' and quit the game anytime by typing 'quit' \n")
        input("Press any key to start the fun 😃\n")
        return True

intro_message()
choice= int(input("Enter ur quiz choice\n1-Avengers Quiz   2-Bollywood Quiz    3-Cricket Quiz\n"))

if(choice==1):
    from questions import avengers



    def check_ans(question, ans, attempts, score):
        """
        Takes the arguments, and confirms if the answer provided by user is correct.
        Converts all answers to lower case to make sure the quiz is not case sensitive.
        """
        if avengers[question]['answer'].lower() == ans.lower():
            print(f"Correct Answer! 🤩 \nYour score is {score + 1}!")
            return True
        else:
            print(f"Wrong Answer 🙁")
            print("The correct answer is: ", avengers[question]['answer'].lower())
            return False


    def print_dictionary():
        for question_id, ques_answer in avengers.items():
            for key in ques_answer:
                print(key + ':', ques_answer[key])



    # python project.py
    while True:
        score = 0
        for question in  avengers:
            attempts = 1
            while attempts > 0:
                print(avengers[question]['question'])
                answer = input("Enter Answer (To move to the next question, type 'skip') : ")
                if answer == "skip":
                    break
                if answer== "quit":
                    print("Disheartened to see you go :(....  \nYour score is:",score)
                    exit()
                check = check_ans(question, answer, attempts, score)
                if check:
                    score += 1
                    break
                attempts -= 1

        break

    print(f"Your final score is {score}!\n\n")
    print_dictionary()
    print("Thanks for playing!")

elif(choice==2):
    from questions import bollywood



    def check_ans(question, ans, attempts, score):
        """
        Takes the arguments, and confirms if the answer provided by user is correct.
        Converts all answers to lower case to make sure the quiz is not case sensitive.
        """
        if bollywood[question]['answer'].lower() == ans.lower():
            print(f"Correct Answer! 🤩 \nYour score is {score + 1}!")
            return True
        else:
            print(f"Wrong Answer 🙁")
            print("The correct answer is: ", bollywood[question]['answer'].lower())
            return False


    def print_dictionary():
        for question_id, ques_answer in bollywood.items():
            for key in ques_answer:
                print(key + ':', ques_answer[key])


    # python project.py
    while True:
        score = 0
        for question in  bollywood:
            attempts = 1
            while attempts > 0:
                print(bollywood[question]['question'])
                answer = input("Enter Answer (To move to the next question, type 'skip') : ")
                if answer == "skip":
                    break
                if answer== "quit":
                    print("Disheartened to see you go :(....  \nYour score is:",score)
                    exit()
                check = check_ans(question, answer, attempts, score)
                if check:
                    score += 1
                    break
                attempts -= 1

        break

    print(f"Your final score is {score}!\n\n")
    print_dictionary()
    print("Thanks for playing!")

elif(choice==3):
    from questions import cricket



    def check_ans(question, ans, attempts, score):
        """
        Takes the arguments, and confirms if the answer provided by user is correct.
        Converts all answers to lower case to make sure the quiz is not case sensitive.
        """
        if cricket[question]['answer'].lower() == ans.lower():
            print(f"Correct Answer! 🤩 \nYour score is {score + 1}!")
            return True
        else:
            print(f"Wrong Answer 🙁")
            print("The correct answer is: ", cricket[question]['answer'].lower())
            return False


    def print_dictionary():
        for question_id, ques_answer in cricket.items():
            for key in ques_answer:
                print(key + ':', ques_answer[key])


    def intro_message():
        """
        Introduces user to the quiz and rules, and takes an input from customer to start the quiz.
        Returns true regardless of any key pressed.
        """
        print("Welcome to this fun quiz! \nAre you ready to have some fun?")
        print("There are a total of 2]10 questions, you can skip a question anytime by typing 'skip' and quit the game anytime by typing 'quit' ")
        input("Press any key to start the fun ;) ")
        return True


    # python project.py
    while True:
        score = 0
        for question in  cricket:
            attempts = 1
            while attempts > 0:
                print(cricket[question]['question'])
                answer = input("Enter Answer (To move to the next question, type 'skip') : ")
                if answer == "skip":
                    break
                if answer== "quit":
                    print("Disheartened to see you go 😞...  \nYour score is:",score)
                    exit()
                check = check_ans(question, answer, attempts, score)
                if check:
                    score += 1
                    break
                attempts -= 1

        break

    print(f"Your final score is {score}!\n\n")
    print_dictionary()
    print("Thanks for playing!")

else:
    print("Oops!! wrong choice...")

