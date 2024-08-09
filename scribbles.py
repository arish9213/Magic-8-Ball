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

    #declare variable for continuing play
    more_qs = input("Do you have another question? Yes/No: ")

    #set up if/elif/else statments

    # set up yes
    if more_qs == "Yes":
        #ask user for another question
        next_q = input(name, "Ask another question...")
        print(next_q)

    # set up no     
    elif more_qs == "No":
        print("Thanks for playing,", name, "Goodbye")
        another_question == False
    
    # error messge
    else:
        print("Sorry, I don't understand that, please try again.")
