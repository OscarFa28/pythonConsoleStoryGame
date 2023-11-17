import time

from player import Player
from actions import Actions
        

print("-- WorldyLife --")
time.sleep(4)
print("**God: Hi there!")
time.sleep(2)
print("**God: Wtf youre ugly")
time.sleep(2)
print("**God: Whatever, the point here is that...")
time.sleep(4)
print("**God: I created you, and now you're heading to Earth.")
time.sleep(4)
print("**God: To proceed, please choose a name.")
time.sleep(2)
print("**God: Don't take too long; I'm busy.")
time.sleep(2)

name = input("++You: ")
act = Actions(name)

time.sleep(2)
print(f"**God: Hahahaha! '{name}'? That name is the biggest piece of sh**t I've ever heard.")
time.sleep(6)
print("**God: But there is not second options, so let's proceed with your birth country.")
time.sleep(4)
print("**God: Choose it... well, actually, that's my job.")
time.sleep(4)
print("**God: mmm.. Let me think")
time.sleep(8)
act.set_country()
print("**God: Okay, I've got it.")
time.sleep(2)

type = act.return_difficulty_type
if type == "Easy":
    print("**God: You caught me at a good time, so I'm going to help you. Your country is: ")
    time.sleep(2)
elif type == "Impossible":
    print("**God: I've been annoyed with you since we met, so your country is going to be: ")
    time.sleep(2)
    
print(act.return_country()+"!!")
time.sleep(4)

input("__Press enter to continue__")
print("--Borned in "+(act.return_country())+"--")

