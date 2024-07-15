# Creating a Therapy Journal Madlib

import time

# Prompt user for the current date and journal entry number
date = input("Today's date: ")
number_entry = input("Jounral Entry #")

# Introduction message for the journal entry
introduction = f"Today's Date is {date} and this is my #{number_entry} entry in this journal.\
 The purpose of thsis madlib is to help me describe what I am feeling and how I can handle my emotions responsibly, \
ranging from very slight to intense emotions. Now let us begin."

# Welcoming message to help the user focus on their state of mind
welcoming = f"Welcome to my coding therapy madlibs journal. Start off by taking some deep breaths \
in and out to help stablize your heart rate and to truly focus on your state of mind."

# Generic message to prompt user to press Enter to continue
enter = f"Press Enter to continue..."


# Creating a method that detects the user's answer. Converts answer into lowercase to determine the input 
# regardless of capitalization. Allows for a variable {prompt} so that it could be used in different prompts. 
def get_yes_or_no(prompt):
    while True: 
        user_input = input(prompt.lower())
        if user_input == "yes":
            return True
        elif user_input == "no":
            return False
        else: 
            print("Invalid input. Please enter 'yes' or 'no'. ")

# Simulate a breathing exercise for the user as a prerequisite, in rounds of 5
def breathing_exercise(breaths): 
    while breaths > 0:
        print(f"Breathe # {breaths}")
        time.sleep(2)
        breaths -= 1
    print("Breathes are done.")

# Ask if the user wants to do another round of 5 breaths
    if get_yes_or_no("would you like to do another round of breaths? (yes/no): "):
        breathing_exercise(5)
    else: print("Breathing exercise complete.")

def detect_emotion(user_input):
    # Convert user input to lowercase for case-insensitive comparison
    user_input = user_input.lower()

    # Define keywords and their corresponding responses
    emotions_responses = {
        'happy': "It's great to hear you're happy!",
        'sad': "I'm sorry you're feeling sad.",
        'frustrated': "It's understandable to feel frustrated sometimes.",
        'mad': "Take a deep breath. It's okay to feel mad.",
        'anxious': "Feeling anxious can be tough. Let's try to work through it."
        # Add more emotions and responses as needed
    }

    # Function to detect the user's emotion from their input
    for emotion, response in emotions_responses.items():
        if emotion in user_input:
            return response
        else: 
         # Have the user try again
          return "I'm not sure how you're feeling. Please try again :)"

   

# Function to ask follow-up questions based on the detected emotion
def ask_follow_up_questions(emotion):
    questions = {
        'sad': [
            "Can you think of anything that might help you feel better? ",
            "Is there someone you can talk to about your feelings? Do not be afriad to reach out to loved ones :) ",
            "What self-care activities could you do today? Try to take a walk and get off your phone for a minute to help calm your mind. "
        ],
        'frustrated': [
            "What exactly is causing you to feel frustrated? ",
            "Have you faced a similar situation before? How did you handle it? ",
            "Is there something you can do to address the cause of your frustration? "
        ],
        'mad': [
            "What triggered your anger? ",
            "What can you do to cool down right now? ",
            "Would taking a break or going for a walk help? "
        ],
        'anxious': [
            "Can you identify what is making you feel anxious? ",
            "Have you tried any relaxation techniques? ",
            "What can you do to distract yourself and reduce your anxiety? "
        ],
        'happy': [
            "What is making you feel do happy? ", 
            "What are your plans for continuing to be happy? "
        ]
    }

     # Ask each question related to the detected emotion and prompt the user to press Enter
    if emotion in questions:
        for question in questions[emotion]:
            input(question)
            print("Thank you for sharing.")
            input(enter)

# Function to provide a concluding message based on the detected emotion
def conclude_journal(emotion):
    conclusions = {
        'sad': "It's important to acknowledge your feelings and seek support when needed. Remember, it's okay to ask for help.",
        'frustrated': "Frustration is a natural response to obstacles. Take it one step at a time and focus on solutions.",
        'mad': "Anger can be powerful. Use it as a signal to make positive changes and practice patience with yourself.",
        'anxious': "Anxiety can be overwhelming, but there are many ways to manage it. Keep practicing relaxation techniques.",
        'happy': "Happiness is a wonderful emotion. Keep doing what makes you feel good and spread your joy to others."
    }
    
    if emotion in conclusions:
        print(conclusions[emotion])
    else:
        print("Thank you for completing today's journal entry. Take care!")

# Beginning body of the journal entry
beginning_body = f"Lets begin. Now that we have calmed your mind. Remember to not overwhelm youself."
question_one = f"How are you feeling today? "

# Display the introduction and wait for the user to press Enter
print(introduction)
input(enter)

# Display the welcoming message and wait for the user to press Enter
print(welcoming)
input(enter)

# Guide the user through the breathing exercise
breathing_exercise(5)

# Display the beginning body of the journal entry
print(beginning_body)
input_text = input(question_one)

# Detect the user's emotion from their input
output = detect_emotion(input_text)

# Display the response based on the detected emotion
print(output)

# If the detected emotion is not happy, ask follow-up questions
print(ask_follow_up_questions(input_text))

# Conclude the journal entry with a tailored message
conclude_journal(input_text)



