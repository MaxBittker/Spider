import random
import sys
import time

Web = 0
Energy = 100
Captured = 0
Day = 0 
Age = 0
location = 0;

firstnames = ['Paula', 'Cyrus', 'Irenka', 'Arawn', 'Aleksander', 'Mario', 'Simona','Aaliyah','Izabelle','Tertius', 'Spider', 'Redips']
spideryAdjs = ['black', 'red','brown','bright', 'dark','green', 'strong', 'many', 'quick', 'long', 'sailing','descending','spinning', 'thousand','silken', 'webbed','chittering']
spideryNouns = ['web', 'thorax', 'fang', 'venom', 'legs', 'leg', 'fly','eyes','bite','thread']
spideryPlaces = ['tree', 'branch', 'fence', 'barn', 'cow', 'rock', 'roof','windowsill','dock']


def status():
    print '\nStatus: \nWeb:            ', Web
    print 'Energy:         ', Energy
    print 'Captured:       ', Captured
    print 'Day:            ', Day
    print 'Location:       ', location
    print '\n'

def ParseAction(action):
    action = action.lower()
    if('check' in action):
        CheckWeb()
    elif('web' in action or ('spin' in action) or ('weave' in action)):
        SpinWeb()
    elif(('wait' in action) or ('sleep' in action) or ( 'rest' in action)):
        Wait()
    elif('status' in action):
        status()
    else:
        HelpScript()
    
def HelpSript():
    print 'Available actions:'
    print 'spin [web],\n[check] web,\n[wait]'

def SpinWeb():
    print '\nYou work your hardest to spin a Web'
    global Web 
    global Energy
    Web = int(Web+(Energy*.5))
    Energy = int(Energy *.5)
    time.sleep(3)

    print 'Your Web looks beautiful, you did a really great job.\n Web: ',Web 
    time.sleep(3)

    print 'However, it took a lot out of you.\n Energy:', Energy
    print '\n'
    time.sleep(3)

def CheckWeb():
    global Web 
    global Energy
    global Captured
    print 'You check your web...\n'
    time.sleep(3)
    Energy = Energy - 5
    Energy = int(Energy + (Captured * 15))
    if(Captured>0):
        print 'You are delighted to find {0} flys ensnared in your web. \n'.format(Captured)
        time.sleep(2)
        print 'You eat them immediatly. Energy: {0}'.format(Energy)
        Captured = 0; 
        time.sleep(3)
    else:
        print 'You find no flys. You should be more Patient. Energy: {0}'.format(Energy)
    print 'Web Quality:',Web
     
    time.sleep(3)

def Wait():
    global Web
    global Captured
    print 'Time goes by...\n' 
    time.sleep(3)
    print 'You dream a spidery dream...\n' 
    time.sleep(3)
    print 'You are awoken by a twitch on your web\n' 
    Captured =int(random.randint(0,5) * (Web/100.0))
    Web = int(Web - (Captured * 10))


random.shuffle(firstnames)
random.shuffle(spideryAdjs)
random.shuffle(spideryNouns)
random.shuffle(spideryPlaces)

print 'You have just been born. Your name is {0} {1}-{2}. \n'.format(firstnames[1],spideryAdjs[1],spideryNouns[1] )
time.sleep(5)

print'You are a spider.\n'
time.sleep(3)
print 'You are surrounded by thousands of your kin\n'
time.sleep(3)

print'You are hungry\n'
time.sleep(2)
action = raw_input('What do you do?\n')
action = action.lower()

Cation = "eat"
if('eat' in action):
    print '\n!!You burst through the wall into a bright world'
else:
    print 'Your siblings eat their way out, you are left behind'
    sys.exit("You have died")

time.sleep(1)
print '\nThe breeze picks you up...'
time.sleep(4)
print '\n   And you float over the countryside...'
time.sleep(4)
print '\n       You wonder where are you going...'
time.sleep(4)
print '\n           You feel perfectly calm, suspended in the wind like a mote of dust...'
time.sleep(4)
print '\n               and you fall asleep...'
time.sleep(11)
Day = Day+1


while Energy > 0:
    
    print 'Good Morning. It is Day ', Day
    time.sleep(1) 

    if(location == 0):
        print 'You find yourself on a', spideryPlaces[1]
    else:
        location = spideryPlaces[1]

    action = raw_input('What do you want to do this Morning?\n')
    ParseAction(action)

    action = raw_input('What do you do this Afternoon?\n')
    ParseAction(action)

    action = raw_input('What do you do this Evening?\n')
    ParseAction(action)
    Energy = Energy - 12;
    Day = Day + 1

    # guess = int(raw_input('Take a guess: '))

    # guesses_made += 1

    # if guess < number:
    #     print 'Your guess is too low.'

    # if guess > number:
    #     print 'Your guess is too high.'

    # if guess == number:
    #break





# number = random.randint(1, 20)
# print 'Well, {0}, I am thinking of a number between 1 and 20.'.format(name)


# if guess == number:
#     print 'Good job, {0}! You guessed my number in {1} guesses!'.format(name, guesses_made)
# else:
#     print 'Nope. The number I was thinking of was {0}'.format(number)

