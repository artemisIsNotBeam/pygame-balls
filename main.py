import pygame,sys,random

(width, height) = (300, 200)
screen = pygame.display.set_mode((width, height))

cyxBalls=[]

for i in range(6):
	ball = "images/images/sphere-0"+str(i)+".png"
	cyxBalls.append(ball)
print(cyxBalls)


bg_color = (0, 0, 0)
global min_y,state;


def initialize(balls, dots, current_ball):
    global min_y, state
    state = "aiming"
    balls.empty()
    for i in range(6):
        if i % 2 == 0:
            for j in range(11):
                balls.add(Ball((7+34*j, 10+30*i), random.choice(ball_images)))
        else:
            for j in range(10):
                balls.add(Ball((24+34*j, 10+30*i), random.choice(ball_images)))
    min_y = 10
    current_ball.add(Ball((200 - 17, 650 - 17), random.choice(ball_images)))
    if len(dots) == 0:
        for i in range(3):
            dots.add(AimingDot(30+35*i))


for i in range(6):
	if i%2 == 0:
		print("its even")
	else:
		print("even")