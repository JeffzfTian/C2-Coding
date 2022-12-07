#Code that lets you make blinking text
from termcolor import colored, cprint

#It's a module that can modify the terminal
import sys
import time

cprint("""\

█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█   █▀▄▀█ █▄█   █▀▀ ▄▀█ █▀▄▀█ █▀▀
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█   █░▀░█ ░█░   █▄█ █▀█ █░▀░█ ██▄
""",'red',attrs=['blink'])

def typeString(string):
    for char in string:
        time.sleep(0.02)
        sys.stdout.write(char)
        sys.stdout.flush()

# This line imports the random package so that we can create random numbers
import random

#This keeps the score, it will add 1 to the original score 0 after you get a question right
score = 0

def question1MQ():
    global score

    print ("\u001b[33m Question #1: Where does this book take place?\u001b[0m")

    print("")
    print("1. Jabari's house")
    print("2. Swimming pool")
    print("3. Random asian supermarket")
    print("")
  
    response1 = str(input("Please Type 1, 2, or 3 to select one of the options\n"))

    if response1 == "1":
        print("Please Try Again")
        print("")
        question1MQ()
   
  
    elif response1 == "2":
        
        print("Great Job!")
        print("")
        score = score + 1
        print("\u001b[32m Your CURRENT score is:\u001b[0m " + str(score))
        print("")
        print("Now we will move on to question number 2!")
        print("")
        question2MQ()
    
  
    elif response1 == "3":
        print ("Please Try Again")
        print ("")
        question1MQ()
   
    
    else:
        print("This is not a valid choice, please try again")
        print("")
        question1MQ()


def question2MQ():
    global score

    print ("\u001b[33m Question #2: Who is Jabari with at the pool?\u001b[0m")

    print("")
    print("1. His dad and sister")
    print("2. His gold fish")
    print("3. His dad")
    print("")
  
    response2 = str(input("Please Type 1, 2, or 3 to select one of the options\n"))

    if response2 == "1":
        print("Please Try Again")
        print("")
        question2MQ()
   
    elif response2 == "2":
        print ("Please Try Again")
        print ("")
        question2MQ()

    elif response2 == "3":
        print("Amazing!")
        print("")
        score = score + 1
        print("\u001b[32m Your CURRENT score is:\u001b[0m " + str(score))
        print("")
        print("Now we will move on to question number 3!")
        question3MQ()
        print("")
    
    else:
        print("This is not a valid choice, please try again")
        print("")
        question2MQ()

def question3MQ():
    global score

    print ("\u001b[33m Question #3: What does Jabari want to do the most at the pool?\u001b[0m")

    print("")
    print("1. Go swimming ")
    print("2. Jump of the diving board")
    print("3. Get ice-sream")
    print("")
  
    response3 = str(input("Please Type 1, 2, or 3 to select one of the options\n"))

    if response3 == "1":
        print("Please Try Again")
        print("")
        question3MQ()
   
    elif response3 == "2":
        print("Fantastic!")
        print("")
        score = score + 1
        print("\u001b[32m Your CURRENT score is:\u001b[0m " + str(score))
        print("")
        print("Now we will move on to question number 4!")
        question4MQ()
        print("")

    elif response3 == "3":
        print ("Please Try Again")
        print ("")
        question3MQ()
    
    else:
        print("This is not a valid choice, please try again")
        print("")
        question3MQ()

def question4MQ():
    global score
  
    print ("\u001b[33m Question #4: What did Jabri do before jumping off the diving board?\u001b[0m")

    print("")
    print("1. Stretch ")
    print("2. Dance and Sing")
    print("3. Eat")
    print("")
  
    response3 = str(input("Please Type 1, 2, or 3 to select one of the options\n"))

    if response3 == "1":
        print("Keep up the good work!")
        print("")
        score = score + 1
        print("\u001b[32m Your CURRENT score is:\u001b[0m " + str(score))
        print("")
        print("Now we will move on to question number 5!")
        question5MQ()
        print("")        
   
    elif response3 == "2":
        print("Please Try Again")
        print("")
        question4MQ()

    elif response3 == "3":
        print ("Please Try Again")
        print ("")
        question4MQ()
    
    else:
        print("This is not a valid choice, please try again")
        print("")
        question4MQ()

def question5MQ():
    global score
  
    print ("\u001b[33m Question #5: How does his dad encourage him to jump?\u001b[0m")

    print("")
    print("1. Push him off the diving board")
    print("2. Show him how it's done")
    print("3. Encourage him verbally")
    print("")
  
    response3 = str(input("Please Type 1, 2, or 3 to select one of the options\n"))

    if response3 == "1":
        print("Please Try Again")
        print("")
        question5MQ()    
    elif response3 == "2":
        print("Please Try Again")
        print("")
        question5MQ()
    elif response3 == "3":
        print("Your acing it!!")
        print("")
        score = score + 1
        print("\u001b[32m Your CURRENT score is:\u001b[0m " + str(score))
        print("")
        print("Now we will move on to question number 5!")
        question6MQ()
        print("")
    
    else:
        print("This is not a valid choice, please try again")
        print("")
        question5MQ()


def question6MQ():
    global score
  
    print ("\u001b[33m Question #6: What kind of a jump does Jabri want to do next?\u001b[0m")

    print("")
    print("1. Double backflip")
    print("2. Triple frontflip")
    print("3. 360 rotation clockwise")
    print("")
  
    response3 = str(input("Please Type 1, 2, or 3 to select one of the options\n"))

    if response3 == "1":
        print("Superb!")
        print("")
        score = score + 1
        print("\u001b[32m Your FINAL score is:\u001b[0m " + str(score))
        print("Now we will move on to Reflection Questions.")
    
        #Based on a random number we will choose a RQ question
        myNum = random.randint(0,3)
        print ("Here is the random number: " + str(myNum))
        if myNum == 0:
            question1RQ()

        elif myNum == 1:
            question2RQ()

        elif myNum == 2:
            question3RQ()

        elif myNum == 3:
            question4RQ()      
   
    elif response3 == "2":
        print("Please Try Again")
        print("")
        question6MQ()

    elif response3 == "3":
        print ("Please Try Again")
        print ("")
        question6MQ()
    
    else:
        print("This is not a valid choice, please try again")
        print("")
        question6MQ()


def question1SM():

    print ("\u001b[33m You just finished school, where would you like to go?\u001b[0m")

    print("")
    print("1. Go home")
    print("2. Go to the swimming pool")
    print("3. Go to get ice-cream")
    print("")
  
    response1 = str(input("Please Type 1, 2, or 3 to select one of the options\n"))

    if response1 == "1":
        print("You go home.")
        question2SM()
  
    elif response2 == "2":
        print("You go to the swimming pool ")
        question3SM()
    
  
    elif response1 == "3":

        print ("You go buy ice-cream at the convenience store")
        question4SM()
   
    
    else:
        print("This is not a valid choice, please try again")
        print("")
        question1SM()

def question2SM():

    print ("\u001b[33m You're at home, what would you like to do\u001b[0m")

    print("")
    print("1. Play videogames")
    print("2. Go to the swimming pool")
    print("3. Go to get ice-cream")
    print("")
  
    response1 = str(input("Please Type 1, 2, or 3 to select one of the options\n"))

    if response1 == "1":
        print("You play videogames on your new PS5.")
        question5SM()
  
    elif response2 == "2":
        print("You go to the swimming pool ")
        question3SM()
    
  
    elif response1 == "3":
        print ("You go buy ice-cream at the convenience store")
        question4SM()
   
    
    else:
        print("This is not a valid choice, please try again")
        print("")
        question2SM()

def question3SM():

    print ("\u001b[33m You go to the swimming pool, what do you want to do?\u001b[0m")

    print("")
    print("1. Start swimming")
    print("2. Go straight to the diving board")
    print("3. Go get ice-cream first then choose what to do")
    print("")
  
    response1 = str(input("Please Type 1, 2, or 3 to select one of the options\n"))

    if response1 == "1":
        print("You start swimming freestyle")
        question6SM()
  
    elif response2 == "2":
        print("You go up to the ladder")
        question7SM()
    
  
    elif response1 == "3":
        print ("You go to the ice-cream store")
        question4SM()
    
    else:
        print("This is not a valid choice, please try again")
        print("")
        question3SM()

def question4SM():

    print ("\u001b[33m You had your favourite flavour of ice-cream\u001b[0m")

    print("")
    print("1. Go home")
    print("2. Go to the swimming pool")
    print("3. Go to the playground next to your house")
    print("")
  
    response1 = str(input("Please Type 1, 2, or 3 to select one of the options\n"))

    if response1 == "1":
        print("You go home.")
        question2SM()
  
    elif response2 == "2":
        print("You go to the swimming pool ")
        question3SM()
    
  
    elif response1 == "3":
        print ("You walk to the playground and find your finds there")
        question8SM()
   
    
    else:
        print("This is not a valid choice, please try again")
        print("")
        question4SM()

def question5SM():

    print ("\u001b[33m You get bored of playing NBA2k23\u001b[0m")

    print("")
    print("1. Go to sleep")
    print("2. Go to the swimming pool")
    print("3. Go to the playground next to your house")
    print("")
  
    response1 = str(input("Please Type 1, 2, or 3 to select one of the options\n"))

    if response1 == "1":
        print("zzzzzzzzzzzz.")
        print("Congratulations! You have completed the story mode questions!")
        print("Now we will move on the the Reflection Questions.")

        #Based on a random number we will choose a RQ question
        myNum = random.randint(0,3)
        print ("Here is the random number: " + str(myNum))

        if myNum == 0:
            question1RQ()

        elif myNum == 1:
            question2RQ()

        elif myNum == 2:
            question3RQ()

        elif myNum == 3:
            question4RQ()

  
    elif response2 == "2":
        print("You go to the swimming pool ")
        question3SM()
    
  
    elif response1 == "3":
        print ("You walk to the playground and find your finds there")
        question8SM()
   
    
    else:
        print("This is not a valid choice, please try again")
        print("")
        question5SM()

def question6SM():

    print ("\u001b[33m You get bored after swimming for a while, what do you want to do next?\u001b[0m")

    print("")
    print("1. Go home")
    print("2. Go to the diving board")
    print("3. Go to the playground")
    print("")
  
    response1 = str(input("Please Type 1, 2, or 3 to select one of the options\n"))

    if response1 == "1":
        print("You go home.")
        question2SM()
  
    elif response2 == "2":
        print("You go up the ladder, leading to the diving board")
        question7SM()
    
  
    elif response1 == "3":
        print ("You walk to the playground and find your finds there")
        question8SM()
   
    
    else:
        print("This is not a valid choice, please try again")
        print("")
        question6SM()

def question7SM():

    print ("\u001b[33m You are standing at the edge of the diving board, what type of dive do you want to perform?\u001b[0m")

    print("")
    print("1. Double blackflip")
    print("2. Double frontflip")
    print("3. Reverse 360 dive")
    print("")
  
    response1 = str(input("Please Type 1, 2, or 3 to select one of the options\n"))

    if response1 == "1":
        print("Fantastic jump!")
        question9SM()
  
    elif response2 == "2":
        print("Super clean dive!")
        question9SM()
    
  
    elif response1 == "3":
        print ("Wow! Amazing!")
        question9SM()
   
    
    else:
        print("This is not a valid choice, please try again")
        print("")
        question7SM()

def question8SM():

    print ("\u001b[33m You play with your friends for a while. You get tired and head home, what do you want to do?\u001b[0m")

    print("")
    print("1. Play videogames")
    print("2. Go to the swimming pool")
    print("3. Go to get ice-cream")
    print("")
  
    response1 = str(input("Please Type 1, 2, or 3 to select one of the options\n"))

    if response1 == "1":
        print("You play videogames on your new PS5.")
        question5SM()
  
    elif response2 == "2":
        print("You go to the swimming pool ")
        question3SM()
    
  
    elif response1 == "3":
        print ("You go buy ice-cream at the convenience store")
        question4SM()
   
    
    else:
        print("This is not a valid choice, please try again")
        print("")
        question8SM()

def question9SM():

    print ("\u001b[33m Question #9: You get tired and head home, what do you want to do?\u001b[0m")

    print("")
    print("1. Play videogames")
    print("2. Go to the swimming pool again")
    print("3. Go to get ice-cream")
    print("")
  
    response1 = str(input("Please Type 1, 2, or 3 to select one of the options\n"))

    if response1 == "1":
        print("You play videogames on your new PS5.")
        question5MQ()
  
    elif response2 == "2":
        print("You go to the swimming pool ")
        question3MQ()
    
  
    elif response1 == "3":
        print ("You go buy ice-cream at the convenience store")
        question4MQ()
   
    
    else:
        print("This is not a valid choice, please try again")
        print("")
        question9MQ()

def question1RQ():
    
    print ("\u001b[33m Question #1: What do you think is the lesson this story is trying to teach?\u001b[0m")

    response1 = str(input("Please answer in full sentences.\n"))


def question2RQ():

    print ("\u001b[33m Question #2: Do you think it was bad that Jabari lied about being scared?\u001b[0m")

    response1 = str(input("Please answer in full sentences.\n"))

def question3RQ():

    print ("\u001b[33m Question #3: Did you like the book? Why?\u001b[0m")

    response1 = str(input("Please answer in full sentences.\n"))

def question4RQ():

    print ("\u001b[33m Question #4: Do you every get scared? Give an example and state what you do when you get scarred.\u001b[0m")

    response1 = str(input("Please answer in full sentences.\n"))

validChoice = False
# global start

while (validChoice == False):
    #global validChoice
    #global start
    
    start = str(input("Please press I to view the instructions\n"))
    if start == "I":
        typeString("\033[1;3mThe ultimate goal of this game is to help you develope a better understanding of Jabari Jumps.\033[0m\n") 
        typeString("\nIt will consist of three different types of questions:\n")
        typeString("\n1. Multiple choice: there will be 3 options for each question and you will be required to type 1,2 or 3 as one of the answers. There will be only one right answer.\n ")
        typeString("\n2. Story mode: this option allows you to explore a similar template to Jabari Jumps. It will be grant you the chance to choose from 3 different options that lead to a unique scenario. The ULTIMEATE GOAL is to go to sleep and prepare for the next day!\n")
        typeString("\n3. Simple comprehension: this will be mandatory to complete, it  will be ask you to type a simple sentence regarding a reflection question. This will not be marked right or wrong.\n")
        typeString("\nWhether you choose Multiple Choice or Story Mode, after finishing the game, you will be taken to the Reflection Questions\n")
        typeString("\nWhich option would you like to begin with: 1: Multiple Choice or 2: Story Mode?")

        
        option = str(input("\nYour choice is:\n"))

        # This will take us to multiple choice questions
        if option == "1":
            validChoice = True
            question1MQ()
        
        # This will take us to the Story Mode questions
        elif option == "2":
            validChoice = True
            question1SM()

    else:
        # this will take us back to the beginning of the loop to see this menu again
        print("This is not a valid choice, please try again")
        print("")

          