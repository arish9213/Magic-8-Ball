#import random module
import random

#create list of responses
responses = ["It is certain.",
             "It is decidedly so.",
             "Without a doubt.",
             "Yes definitely.",
             "You may rely on it.",
             "As I see it, yes.",
             "Most likely.",
             "Out look good.",
             "Yes.",
             "Signs point to yes.",
             "Reply hazy, try again.",
             "Ask again later.",
             "Better not tell you now.",
             "Cannot predict now.",
             "Concentrate and ask again.",
             "Don't count on it.",
             "My reply is no.",
             "My sources say no.",
             "Outlook not so good.",
             "Very doubtful.”]

# set up variable for asking
question == True

#welcome statement for users
print("Welcome to my M8B game! Start thinking of a yes or no question, but first... \n")

#ask for users name
name = input("What's your name?: ")

#greet user
print("Hello", name, " , Have you thought of your question yet? Times a ticking...")

#set up while loop
while question == True:
    #ask and print out user question
    question = input("Ask your yes or no question: ")
    print(name, "asks: ", question)

    #give user reponse message
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



























# variable for starting
question1 = True

#set up while loop
while question1 == True:
    input("Ask a yes or no question: /n")
    
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
