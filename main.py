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
print(f"**God: Hahahaha! {name}? That name is the biggest piece of sh**t I've ever heard.")
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

type = act.return_difficulty_type()
if type == "Easy":
    print("**God: You caught me at a good time, so I'm going to help you. Your country is going to be good, trust me")
    time.sleep(2)
elif type == "Impossible":
    print("**God: I've been annoyed with you since we met, so your country is going to be awful, sorry")
    time.sleep(2)
    

input("__Press enter to continue__")
time.sleep(2)
print("--Borned in "+(act.return_country())+"--")
time.sleep(2)
act.show_status()
time.sleep(1)
print("If you ever want to see your actual status again just type 'show status' in any input")
time.sleep(2)
print("If you ever want to get ot of the game just type 'stop game' in any input")
time.sleep(2)

print("**Narrator: You have just been born into a beautiful family.")
age = 0
time.sleep(2)

if act.return_difficulty() > 60:
    print("**Narrator: Actually, no. Your father left before your birth.")
    time.sleep(2)

print("**Narrator: Everything in your life has been normal, like any other baby. Now, you are 1 year old.")
age = 1
time.sleep(2)

print("**Narrator: Look here, it's your first decision.")
time.sleep(2)

print("**Narrator: You are in your house playing, then you need to decide.")
time.sleep(2)
act.ask_question(age)

print("**Narrator: Remember that what you choose now, will affect your future.")
time.sleep(2)

print("**Narrator: I hope you make the right decisions.")
time.sleep(2)

print("**Narrator: You've grown a bit. Now, you're 2 years old.")
age = 2
time.sleep(2)

print("**Narrator: You're beginning to explore more.")
time.sleep(2)

print("**Narrator: You're at home resting. What would you like to do?")
time.sleep(2)
act.ask_question(age)

print("**Narrator: Really? Why? Okay, let's continue.")
time.sleep(2)

print("**Narrator: Time flies! You're 3 years old now.")
age = 3
time.sleep(2)

print("**Narrator: Another day, another choice.")
time.sleep(2)

print("**Narrator: You're at school, and they invite you to start playing a sport.")
time.sleep(2)

print("**Narrator: So, they ask you...")
time.sleep(2)
act.ask_question(age)

print("**Narrator: Hmm... okay?")
time.sleep(2)

print("**Narrator: Wow, you're 4 years old already.")
age = 4
time.sleep(2)

print("**Narrator: Another normal day, but with an important decision.")
time.sleep(2)

print("**Narrator: You're in a new school. Do you want to...")
time.sleep(2)
act.ask_question(age)

print("**Narrator: It's okay; it's your decision.")
time.sleep(2)

print("**Narrator: Time is passing by. Now, you're 5 years old.")
age = 5
time.sleep(2)

print("**Narrator: Here comes one of the most important decisions in your life.")
time.sleep(2)

print("**Narrator: You're going to the beach!")
time.sleep(2)

print("**Narrator: But before that, you need to spend a 4-hour car ride...")
time.sleep(2)
act.ask_question(age)

time.sleep(4)

#End Child stage

age = 9
print("**Narrator: Your life as a child had been like any other kid's in your country.")
time.sleep(2)
print("**Narrator: Some days were for play, some for joy, and some for tears.")
time.sleep(2)
print("**Narrator: But at 9, something different happened. Let's see.")
time.sleep(2)

if act.return_difficulty() < 33:  # EASY
    print("**Narrator: You got a bad grade at school. Are you going to...")
    time.sleep(2)
    act.ask_question(age)

elif act.return_difficulty() >= 33 and act.return_difficulty() < 66:  # NORMAL
    print("**Narrator: A kid is laughing about your past car accident. Do you want to...")
    time.sleep(2)
    act.ask_question(age)

else:  # HARD
    print("**Narrator: An adolescent stole some things from your backpack.")
    time.sleep(2)
    act.ask_question(age)

