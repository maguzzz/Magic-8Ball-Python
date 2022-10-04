#Adding "random" number generator thats predictable over time 
import random

#Set your name
name = "Markus"
#Ask a question
question = "Did i just programm this project? \n"
#Empty answer for the conditional statement
answer = ""

#Generating Random number from 1-9
randomNumber = random.randint(1,11)

#prints the name if (var name) has a value
if name == "":
  print("Question: " + question)
else:
  print(name + " asks: " + question)

#selects answer by number generated 
if randomNumber == 1:
  answer ="Yes - definitely."
elif randomNumber == 2:
  answer ="It is decidedly so."
elif randomNumber == 3:
  answer ="Without a doubt."
elif randomNumber == 4:
  answer ="Reply hazy, try again."
elif randomNumber == 5:
  answer ="Ask again later."
elif randomNumber == 6:
  answer ="Better not tell you now."
elif randomNumber == 7:
  answer ="My sources say no."
elif randomNumber == 8:
  answer ="Outlook not so good."
elif randomNumber == 9:
  answer ="Very doubtful."
elif randomNumber == 10:
  answer ="No."
elif randomNumber == 11:
  answer ="Yes."
else:
  answer ="Looks like something went wrong"

#prints final output
print("Magic 8-Ball's answer: " + answer)