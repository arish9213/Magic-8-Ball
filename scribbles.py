#welcome statement for users
print("Welcome to my M8B game! Start thinking of a yes or no question, but first... \n")

#ask for users name
name = input("What's your name?: ")

#greet user
print("Hello", name, ", are you ready to ask a question?")

# variable for continuing loop
another_question = True

#set up while loop
while another_question == True:
    responses = random.choice(responses)
    print(reponses)
    more_qs = input("Do you have another question? Yes/No: ")

    #set up if statment
    if more_qs == "Yes":
        #ask user for another question
        next_q = input(name, "Ask another question...")
        print(next_q)
    elif more_qs == "No":
        print("Thanks for playing,", name, "Goodbye ")

