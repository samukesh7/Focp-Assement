import random

def answer(question, name):
    if "library" in question:
        print("The library is closed today.")
    elif "wifi" in question.lower():
        print("WiFi is excellent across the campus.")
    elif "deadline" in question.lower():
        print("Your deadline has been extended by two working days.")
    elif "contact" in question.lower():
        print("Our contact number is 0195000.")
    elif "class" in question.lower():
        print("Your class is finished.")
    elif "coffee" in question.lower():
        print("We have Cafe.")
    elif any(char in question.lower() for char in ["bye", "exit", "goodbye", "help"]):
        print(f"Thanks! ",name," for using PopChat. See you again soon!")
        exit()
    else:
        print(random.choice(["Hmm.", "Oh, yes, I see", "Tell me more.", "I like it.", "Yes."]))

print("Welcome to Pop Chat System! \nOne of Our Operators will be pleased to help you today.")

email = input("Enter your email address : ")
#checking the email address
if (email.count("@") != 1) or (email.split('@')[1]!= "pop.ac.uk") or (len(email.split('@')[0])<3):
    exit("Invalid Email Format! \nExiting..... \nThank you....") 


name = email.split('@')[0].capitalize()
Operator = random.choice(['Jimmy', 'Joe', 'Lisa', 'Fed', 'Friday', 'Siri'])
print(f"Hi, {name}! Thank you, and Welcome to PopChat! \nMy name is {Operator}, and it will be my pleasure to help you.")
if random.choice([i for i in range(10)]) == 1: # creating network error with 10% probability
        print("*** NETWORK ERROR ***")
else:
    while True:
        question = input("--->")
        answer(question, name)
print("Thanks ",name," for using PopChat. See you again soon!")
      