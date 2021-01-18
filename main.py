#Created by Cesar Sanchez on 12/28/2020
#Copyright ©2020 cesarsanchez1. All rights reserved.
import turtle
import random
import time

gameScreen = turtle.Screen()
gameScreen.title("1 MINUTE TO THE MOON")
gameScreen.bgcolor("teal")
gameScreen.setup(width=800, height=700)
gameScreen.tracer(0)
gameScreen.listen()

title1 = turtle.Turtle()
title1.color("silver")
title1.penup()
title1.hideturtle()
title1.goto(0, 200)
title1.write("1 MINUTE TO THE MOON", align="center", font=("futura", 48, "bold" and "italic"))

title2 = turtle.Turtle()
title2.color("midnightblue")
title2.penup()
title2.hideturtle()
title2.goto(-2, 199)
title2.write("1 MINUTE TO THE MOON", align="center", font=("futura", 48, "bold" and "italic"))

description = turtle.Turtle()
description.color("midnightblue")
description.penup()
description.hideturtle()
description.goto(0, 50)

key_description = turtle.Turtle()
key_description.color("midnightblue")
key_description.penup()
key_description.hideturtle()
key_description.goto(-89, -140)

instructions = turtle.Turtle()
instructions.color("midnightblue")
instructions.penup()
instructions.hideturtle()
instructions.goto(0, -220)
instructions.write("Instructions", align="center", font=("futura", 20, "bold"))

instructions_button = turtle.Turtle()       #displays instructions when clicked on
instructions_button.color("midnightblue")
instructions_button.penup()
instructions_button.shape("square")
instructions_button.goto(0, -240)

symbols = turtle.Turtle()
symbols.color("midnightblue")
symbols.penup()
symbols.hideturtle()
symbols.goto(-120, -140)

button_trigger = 0


def instructions_push(x, y):
    global button_trigger
    description.write("     NAVIGATE THROUGH THE ASTEROID BELT\nUNTIL YOU REACH THE MOON IN 60 SECONDS\n",
                      align="center", font=("futura", 18, "bold" and "italic"))
    key_description.write("\n▢\n▢\n▢\n▢", align="center", font=("futura", 24, "bold"))
    symbols.write("Controls:\nUp     ↑\nDown ↓\nRight  ←\nLeft    →", align="center", font=("futura", 24))
    button_trigger += 1
    if button_trigger % 2 == 0:
        key_description.clear()
        description.clear()
        symbols.clear()


instructions_button.onclick(instructions_push)

play = turtle.Turtle()
play.color("midnightblue")
play.penup()
play.goto(2, -75)
play.write("PLAY", align="center", font=("futura", 28, "bold"))
play.hideturtle()
play.speed(0)

playButton = turtle.Turtle()
playButton.color("midnightblue")
playButton.penup()
playButton.shape("triangle")
playButton.goto(0, -100)
playButton.shapesize(stretch_wid=1.5, stretch_len=1.5)
playButton.speed(0)

animationCircle = turtle.Turtle()
animationCircle.speed(0)
animationCircle.color("teal")
animationCircle.shape("circle")
animationCircle.goto(0, 0)
animationCircle.shapesize(stretch_wid=2, stretch_len=2)

health = turtle.Turtle()
health.speed(0)
health.color("teal")
health.penup()
health.hideturtle()
health.goto(255, 275)
global healthScore
healthScore = 10
health_str = str(healthScore)
health.write("Health: " + health_str, align="center", font=("futura", 28, "bold"))

gameLostAlert = turtle.Turtle()
gameLostAlert.speed(0)
gameLostAlert.penup()
gameLostAlert.hideturtle()

playAgain = turtle.Turtle()
playAgain.speed(0)
playAgain.penup()
playAgain.color("teal")
playAgain.goto(0, -200)
playAgain.hideturtle()

playAgainButton = turtle.Turtle()
playAgainButton.color("darkred")
playAgainButton.penup()
playAgainButton.shape("triangle")
playAgainButton.goto(0, -230)
playAgainButton.hideturtle()

playAgainButton.shapesize(stretch_wid=1.5, stretch_len=1.5)
playAgainButton.speed(0)


def button_push(x, y):
    gameScreen.tracer(2)
    playButton.color("silver")
    for i in range(55):
        animationCircle.color("midnightblue")
        animationCircle.shapesize(stretch_wid=2+i, stretch_len=2+i)
    title1.clear()
    title2.clear()
    playButton.hideturtle()
    gameScreen.bgcolor("midnightblue")
    animationCircle.hideturtle()
    gameScreen.tracer(0)
    global game_in_session
    game_in_session = True


playButton.onclick(button_push)


def replay_button_push(x, y):
    global healthScore
    global game_in_session
    global total_time
    gameScreen.tracer(2)
    playAgainButton.color("silver")
    animationCircle.showturtle()
    total_time = 60
    for i in range(55):
        animationCircle.color("midnight Blue")
        animationCircle.shapesize(stretch_wid=2+i, stretch_len=2+i)

    animationCircle.hideturtle()
    gameScreen.tracer(0)
    restart_asteroid_loop()
    game_in_session = True
    playAgainButton.hideturtle()
    playAgainButton.color("darkred")
    playAgain.clear()
    gameLostAlert.clear()
    healthScore = 10
    health_str = str(healthScore)
    health.clear()
    health.write("Health: " + health_str, align="center", font=("futura", 28, "bold"))


playAgainButton.onclick(replay_button_push)

#Generates Stars to be looped
starNum = 10
star_array = []
xStarCoordinate = []
yStarCoordinate = []
yStar = 900
for j in range(starNum):
    a = random.randint(1, 2)
    star_array.append(turtle.Turtle())
    star_array[j].shape("circle")
    star_array[j].penup()
    star_array[j].color("palegoldenrod")
    b = random.uniform(.3, .6)
    star_array[j].shapesize(stretch_wid=b, stretch_len=b)
    xStar = 0
    xStar += random.randint(-350, 350)
    if a % 2 == 0:
        yStar += random.randint(150, 325)
        #yStar += 50
    else:
        yStar -= random.randint(50, 150)
    star_array[j].goto(xStar, yStar)
    xStarCoordinate.append(xStar)
    yStarCoordinate.append(yStar)
    star_array[j].dy = -3

#Generates Asteroids to be looped
asteroidNum = 30
asteroid_array = []
xStart = 0
yStart = 500
xCoordinate = []
yCoordinate = []
for k in range(asteroidNum):
    asteroid_array.append(turtle.Turtle())
    asteroid_array[k].shape("circle")
    asteroid_array[k].penup()
    asteroid_array[k].color("orangered")
    asteroid_array[k].goto(xStart, yStart)
    a = random.randint(1, 3)
    xCoordinate.append(xStart)
    yCoordinate.append(yStart)
    xStart += random.randint(-40, 40)
    yStart += random.randint(40, 80)
    asteroid_array[k].dx = random.uniform(-3, 3)
    asteroid_array[k].dy = -1 * random.uniform(7, 14)

moon = turtle.Turtle()
moon.speed(0)
moon.shape("circle")
moon.color("aliceblue")
moon.shapesize(stretch_wid=45, stretch_len=45)
moon.penup()
moon.goto(0, 800)
moon.dy = -1

num_craters = 9
craters = []
for a in range(10):
    craters.append(turtle.Turtle())
    craters[a].speed(0)
    craters[a].shape("circle")
    craters[a].color("lightsteelblue")
    craters[a].penup()

craters[0].shapesize(stretch_wid=2, stretch_len=6)
craters[0].right(30)
craters[0].goto(-245, moon.ycor() - 310)

craters[1].shapesize(stretch_wid=2, stretch_len=6)
craters[1].right(15)
craters[1].goto(-90, moon.ycor() - 380)

craters[2].shapesize(stretch_wid=2, stretch_len=6)
craters[2].right(-15)
craters[2].goto(90, moon.ycor() - 380)

craters[3].shapesize(stretch_wid=2, stretch_len=6)
craters[3].right(-30)
craters[3].goto(245, moon.ycor() - 310)

craters[4].shapesize(stretch_wid=2.3, stretch_len=6)
craters[4].right(-25)
craters[4].goto(160, moon.ycor() - 260)

craters[5].shapesize(stretch_wid=2.3, stretch_len=6)
craters[5].right(25)
craters[5].goto(-160, moon.ycor() - 260)

craters[6].shapesize(stretch_wid=2.3, stretch_len=6)
craters[6].goto(0, moon.ycor() - 300)

craters[7].shapesize(stretch_wid=3, stretch_len=7)
craters[7].goto(0, moon.ycor() - 220)

craters[8].shapesize(stretch_wid=2.2, stretch_len=6)
craters[8].right(-42)
craters[8].goto(320, moon.ycor() - 200)

craters[9].shapesize(stretch_wid=2.2, stretch_len=6)
craters[9].right(42)
craters[9].goto(-320, moon.ycor() - 200)

core = turtle.Turtle()
core.shape("square")
core.color("silver")
core.shapesize(stretch_wid=1, stretch_len=1.5)
core.penup()
core.goto(0, -500)

craft = turtle.Turtle()
craft.shape("square")
craft.color("silver")
craft.shapesize(stretch_wid=1, stretch_len=1.5)
craft.penup()
craft.goto(core.xcor(), core.ycor())

head = turtle.Turtle()
head.shape("triangle")
head.color("silver")
head.shapesize(stretch_wid=2, stretch_len=2.5)
head.penup()
head.goto(core.xcor(), core.ycor()+15)
head.right(-90)

tail1 = turtle.Turtle()
tail1.shape("triangle")
tail1.color("silver")
tail1.shapesize(stretch_wid=1.5, stretch_len=1)
tail1.penup()
tail1.goto(core.xcor(), core.ycor()-15)
tail1.right(90)

leftWing = turtle.Turtle()
leftWing.shape("triangle")
leftWing.right(180)
leftWing.color("silver")
leftWing.shapesize(stretch_wid=1.2, stretch_len=2)
leftWing.penup()
leftWing.goto(core.xcor()-25, core.ycor())

rightWing = turtle.Turtle()
rightWing.shape("triangle")
rightWing.color("silver")
rightWing.shapesize(stretch_wid=1.2, stretch_len=2)
rightWing.penup()
rightWing.goto(core.xcor()+25, core.ycor())

aileronLeft = turtle.Turtle()
aileronLeft.shape("triangle")
aileronLeft.color("steelblue")
aileronLeft.shapesize(stretch_wid=1.2, stretch_len=.5)
aileronLeft.penup()
aileronLeft.goto(core.xcor()-37, core.ycor()-3)
aileronLeft.right(90)

aileronRight = turtle.Turtle()
aileronRight.shape("triangle")
aileronRight.color("steelblue")
aileronRight.shapesize(stretch_wid=1.2, stretch_len=.5)
aileronRight.penup()
aileronRight.goto(core.xcor()+37, core.ycor()-3)
aileronRight.right(90)

window = turtle.Turtle()
window.shape("circle")
window.color("steelblue")
window.shapesize(stretch_wid=1, stretch_len=1)
window.penup()
window.goto(core.xcor(), core.ycor()+10)


def core_up():          #keyboard bindings that control the spacecraft
    y = core.ycor()
    y += 25
    core.sety(y)


def core_down():
    y = core.ycor()
    y -= 25
    core.sety(y)


def core_right():
    x = core.xcor()
    x += 25
    core.setx(x)


def core_left():
    x = core.xcor()
    x -= 25
    core.setx(x)


gameScreen.listen()
gameScreen.onkeypress(core_up, "Up")
gameScreen.onkeypress(core_down, "Down")
gameScreen.onkeypress(core_right, "Right")
gameScreen.onkeypress(core_left, "Left")


def reposition_core():          #repositions spacecraft
    craft.goto(core.xcor(), core.ycor())
    head.goto(core.xcor(), core.ycor() + 15)
    tail1.goto(core.xcor(), core.ycor() - 10)
    leftWing.goto(core.xcor() - 25, core.ycor())
    rightWing.goto(core.xcor() + 25, core.ycor())
    aileronLeft.goto(core.xcor() - 37, core.ycor() - 3)
    aileronRight.goto(core.xcor() + 37, core.ycor() - 3)
    window.goto(core.xcor(), core.ycor() + 10)


def core_border_limits():       #sets spacecraft border limits
    if core.xcor() > 340:
        core.goto(340, core.ycor())
    if core.xcor() < -350:
        core.goto(-350, core.ycor())
    if core.ycor() > 305:
        core.goto(core.xcor(), 305)
    if core.ycor() < -320:
        core.goto(core.xcor(), -320)


def loop_stars():       #restarts star loop after they go off screen
    for m in range(starNum):
        star_array[m].setx(star_array[m].xcor())
        star_array[m].sety(star_array[m].ycor() + star_array[m].dy)
        if star_array[m].ycor() < -340:
            star_array[m].goto(xStarCoordinate[m], yStarCoordinate[m])


def restart_asteroid_loop():        #restarts asteroid loop if the player chooses to play again
    for n in range(asteroidNum):
        asteroid_array[n].goto(xCoordinate[n] + random.randint(5, 10), yCoordinate[n] + random.randint(5, 10))
        asteroid_array[n].dx = random.uniform(-3, 3)
        asteroid_array[n].dy = -1 * random.uniform(5, 14)


def loop_asteroids():           #restarts asteroid loop after they go off screen
    global healthScore
    global total_time
    for n in range(asteroidNum):    #updates asteroid movement
        asteroid_array[n].setx(asteroid_array[n].xcor() + asteroid_array[n].dx)
        asteroid_array[n].sety(asteroid_array[n].ycor() + asteroid_array[n].dy)
        # Loops asteroid movement
        if asteroid_array[n].ycor() < -340 or asteroid_array[n].xcor() > 400 or asteroid_array[n].xcor() < -410:
            asteroid_array[n].goto(xCoordinate[n] + random.randint(5, 10), yCoordinate[n] + random.randint(5, 10))
            if total_time < 5:      # stops asteroid movement within the final 5 seconds
                asteroid_array[n].dy = 0
                asteroid_array[n].dx = 0
            asteroid_array[n].dx *= -1
        #checks spacecraft asteroid collision
        if (core.ycor() + 45 > asteroid_array[n].ycor() > core.ycor() - 15) \
                and (core.xcor() - 25 < asteroid_array[n].xcor() < core.xcor() + 25) \
                or (core.ycor() - 15 < asteroid_array[n].ycor() < core.ycor() + 10) \
                and (core.xcor() - 60 < asteroid_array[n].xcor() < core.xcor() + 60):
            damage_visual(1)       #whenever a collision occurs
            asteroid_array[n].goto(xCoordinate[k] + random.randint(5, 10), yCoordinate[k] + random.randint(5, 10))
            healthScore -= 1
            health_str = str(healthScore)
            health.clear()
            health.write("Health: " + health_str, align="center", font=("futura", 28, "bold"))


def damage_visual(damage_level):        #a damage visual for asteroid collisions
    if damage_level == 10:
        gameScreen.tracer(3)
    else:
        gameScreen.tracer(10)
    for p in range(damage_level):
        if p % 2 == 1:
            core.color("orange")
            craft.color("orange")
            head.color("orange")
            window.color("orange")
            tail1.color("orange")
            leftWing.color("orange")
            rightWing.color("orange")
            aileronLeft.color("orange")
            aileronRight.color("orange")
        else:
            core.color("orangered")
            craft.color("orangered")
            head.color("orangered")
            window.color("orangered")
            tail1.color("orangered")
            leftWing.color("orangered")
            rightWing.color("orangered")
            aileronLeft.color("orangered")
            aileronRight.color("orangered")
        recolor_craft()
        gameScreen.tracer(0)


def spaceship_destroyed():
    damage_visual(10)
    cloud_colors = ["floralwhite", "oldlace", "cornsilk", "papayawhip", "blanchedalmond",
                    "antiquewhite", "bisque", "peachpuff", "sandybrown", "darkorange"]
    cloud_num = 10
    clouds = []
    start_size = .4
    i = 0
    gameScreen.tracer(0)
    for k in range(cloud_num):
        clouds.append(turtle.Turtle())
        clouds[k].hideturtle()
    gameScreen.tracer(3)
    for j in range(cloud_num-1, -1, -1):
        clouds[j].shape("circle")
        clouds[j].color(cloud_colors[i])
        clouds[j].penup()
        clouds[j].goto(craft.xcor(), craft.ycor())
        clouds[j].showturtle()
        turtle.hideturtle()
        clouds[j].shapesize(stretch_wid=start_size, stretch_len=start_size)
        start_size += .8
        i += 1
    core.goto(0, -500)
    craft.goto(0, -500)
    head.goto(0, -500)
    window.goto(0, -500)
    tail1.goto(0, -500)
    leftWing.goto(0, -500)
    rightWing.goto(0, -500)
    aileronLeft.goto(0, -500)
    aileronRight.goto(0, -500)
    for j in range(10):
        clouds[j].hideturtle()


def recolor_craft():
    core.color("silver")
    craft.color("silver")
    head.color("silver")
    window.color("steelblue")
    tail1.color("silver")
    leftWing.color("silver")
    rightWing.color("silver")
    aileronLeft.color("steelblue")
    aileronRight.color("steelblue")


def play_again_option():
    global game_in_session
    game_in_session = False
    gameLostAlert.color("darkred")
    gameLostAlert.write("You Lose", align="center", font=("futura", 36, "bold"))
    playAgain.color("darkred")
    playAgain.write("PLAY AGAIN", align="center", font=("futura", 36, "bold"))
    playAgainButton.showturtle()
    core.showturtle()
    recolor_craft()


pendulum = turtle.Turtle()
pendulum.shape("square")
pendulum.color("silver")
pendulum.shapesize(stretch_wid=1, stretch_len=1)
pendulum.penup()
pendulum.goto(400, 1)
pendulum.dy = -1

countdown = turtle.Turtle()
countdown.color("teal")
countdown.penup()
countdown.hideturtle()
countdown.goto(225, 225)

global total_time
total_time = 60


def timer():
    global total_time
    pendulum.goto(pendulum.xcor(), pendulum.ycor() + pendulum.dy)
    if pendulum.ycor() == -60:
        pendulum.goto(400, 1)
    if pendulum.ycor() == 0:
        statement = str(total_time)
        countdown.clear()
        countdown.write("Seconds left: " + statement, align="center", font=("futura", 28, "bold"))
        if total_time > 0:
            total_time -= 1


def reposition_moon():
    craters[0].goto(-245, moon.ycor() - 310)
    craters[1].goto(-90, moon.ycor() - 380)
    craters[2].goto(90, moon.ycor() - 380)
    craters[3].goto(245, moon.ycor() - 310)
    craters[4].goto(160, moon.ycor() - 260)
    craters[5].goto(-160, moon.ycor() - 260)
    craters[6].goto(0, moon.ycor() - 300)
    craters[7].goto(0, moon.ycor() - 220)
    craters[8].goto(320, moon.ycor() - 200)
    craters[9].goto(-320, moon.ycor() - 200)


def moon_motion():
    moon.goto(moon.xcor(), moon.ycor() + moon.dy)
    reposition_moon()
    if healthScore > 0:
        if moon.ycor() == 600:
            win_alert.write("        You Win!\nThanks for playing.", align="center", font=("futura", 28, "bold"))
        if moon.ycor() == 525:
            moon.dy = 0
        if moon.ycor() == 535:
            win_alert.clear()
            win_alert.write("Goodbye", align="center", font=("futura", 28, "bold"))


def spaceship_end_motion():
    global end_game
    core.goto(core.xcor(), core.ycor()+10)
    if core.ycor() > 400:
        time.sleep(1)
        end_game = True


win_alert = turtle.Turtle()
win_alert.color("gold")
win_alert.penup()
win_alert.hideturtle()
win_alert.goto(0, -20)

finished_game = False
game_in_session = False
end_game = False

while end_game is False:
    gameScreen.update()
    if healthScore > 0 and total_time >= 0 and finished_game is False:
        loop_stars()
    if healthScore == 0 and game_in_session is True:
        spaceship_destroyed()
        play_again_option()
    if healthScore > 0 and game_in_session is True:
        timer()
        reposition_core()
        loop_asteroids()
        core_border_limits()
    if healthScore > 0 and total_time == 0:
        moon_motion()
        reposition_core()
        if moon.ycor() == 525:
            spaceship_end_motion()
            finished_game = True
            game_in_session = False