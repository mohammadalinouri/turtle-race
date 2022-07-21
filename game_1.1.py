import time
import random
import turtle
WIDTH, HEIGHT=1000, 500

Colors=['blue', 'cyan', 'black', 'pink', 'purple', 'red', 'orange', 'yellow', 'brown', 'green']

def get_number():
    while True:
        racers= input('how many turtuls you want to race? (2 _ 10) '  )
        if racers.isdigit():
            racers=int(racers)
        else:
            print('please enter a valid number! ')
            continue
        if racers>=2 and racers<=10:
            return racers
        else:
            print('please enter a number between 2 and 10')


def init_turtul():
    screen=turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('turtul reacing')


def start(color):
    turtules=seting_turtuls(color)
    
    while True:
        for racer in turtules:
        
            racer.forward(random.randint(1, 20))

            x, y=racer.pos()
            if x>=WIDTH//2-10:
                return color[turtules.index(racer)]
 

def seting_turtuls(color):
    turtules=[]
    sety=HEIGHT//(racers+1)
    for i, c in enumerate(color):
        racer=turtle.Turtle()
        racer.shape('turtle')
        racer.color(c)
        racer.penup()
        racer.setpos((-WIDTH//2)+WIDTH//20, (-HEIGHT//2)+sety*(i+1))
        racer.pendown()
        turtules.append(racer)
    return turtules

            
        
racers=get_number()       #get the number of turtuls from user
random.shuffle(Colors)     #shuffle the colors
color=Colors[:racers]       #make a list with color for number of turtuls
init_turtul()               #game screen
print(start(color)+" just won the game! ")
time.sleep(5)
