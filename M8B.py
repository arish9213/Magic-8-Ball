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
             "Very doubtful.”"]

#set variable for playing the game
play = True

#welcome statement for users
print("✨🎱🔮 Welcome to my Magic 8 Ball game!🔮🎱✨ \n\n Start thinking of a yes or no question, but first... \n")

#ask for users name
name = input("What is your name?: ")

#greet user
print("Hello",name," , Have you thought of your question yet? Time is ticking...\n")

#set up while loop
while play == True:

    #ask and print out user question
    question = input("Ask your yes or no question:")
    print(name, "asks: ",question)
    print("\n🎱🔮 *Shaking the ball * 🔮🎱    ...concentrate on your question!\n")

    #give user reponse message
    responses = random.choice(responses)
    print("Response: It seems to me...",(responses))

    #Ask user if they have another question
    more_qs = input("Do you have another question? Yes/No: \n")

    #if/elif/else loops
    if more_qs == "Yes":
        play == True

    elif more_qs == "No":
        print("Thanks for playing,", name,".\n✨ Have a magical day! ✨")
        play = False
    
    # error messge
    else:
        print("\nSorry, I don't understand that, please try again.")