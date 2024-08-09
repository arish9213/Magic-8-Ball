# import Random module
import random

#create dictionary of answers
answer_dict = {
    1: "It is certain.",
    2: "It is decidedly so.",
    3: "Without a doubt.",
    4: "Yes definitely.",
    5: "You may rely on it.",
    6: "As I see it, yes.",
    7: "Most likely.",
    8: "Out look good.",
    9: "Yes.",
    10: "Signs point to yes.",
    11: "Reply hazy, try again.",
    12: "Ask again later.",
    13: "Better not tell you now.",
    14: "Cannot predict now.",
    15: "Concentrate and ask again.",
    16: "Don't count on it.",
    17: "My reply is no.",
    18: "My sources say no."
    19: "Outlook not so good.",
    20: "Very doubtful."
    }

#declare variables (min & max)
min = 1
max = 20

#variable to continue loop running
shake_again = "yes"

#loop to run program
while shake_again == "yes":

    #inform user of what's happening w/print statement
    print("Concentrate on your question...I'm shaking the magic 8 ball.")

    #declare variable using random module
    M8B_value = (random.randint(min,max))

    #print value of magic 8 ball
    print("The value is: ", M8B_value)

    #if, elif, else
    if M8B_value == 
