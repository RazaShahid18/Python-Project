def intro_message():
        """
        Introduces user to the quiz and rules, and takes an input from customer to start the quiz.
        Returns true regardless of any key pressed.
        """
        print("Welcome to this fun quiz! \nAre you ready to have some fun?")
        print("This game contains 3 different types of quizes,each containing 10 questions. You can skip a question anytime by typing 'skip' and quit the game anytime by typing 'quit' ")
        input("Press any key to start the fun 😃 ")
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
