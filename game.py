# ILTPWC - Python Tutorial
# please consider to like and subscribe

import pgzrun
from world import world

########## Variables - pygame zero ##########

WIDTH = 800
HEIGHT = 750
TITLE = "ILTPWC - My first Game"


########## Variables - Game #################

robot_speed = 200
robot_jump_speed = -200

my_world = world(400)

robot = Actor('robot_idle', (400, 500))
robot.vy = 0
robot.vx = 0
ground = Rect(0, 556, WIDTH, 200)

########## Functions - Game Engine ##########


def draw():
    screen.clear()
    screen.blit("bg_castle",(0,-150))
    screen.draw.filled_rect(ground, (18,92,32))
    robot.draw()

def update(dt):
    if keyboard.A:
        robot.x -= robot_speed * dt
    elif keyboard.D:
        robot.x += robot_speed * dt

    # Apply gravity to the robot
    robot.vy += my_world.gravity * dt

    # check player jump
    if keyboard.W and robot.bottom >= ground.top:
        robot.vy = robot_jump_speed

    robot.y += robot.vy *dt

    # check if the robot is on ground
    if robot.bottom >= ground.top:
        robot.bottom = ground.top
        robot.vy = 0

pgzrun.go()