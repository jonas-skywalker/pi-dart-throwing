import random


inside = 0
outside = 0

pointlist = []


def setup():
    #size(500, 500)
    fullScreen()
    background(51)
    colorMode(HSB, 100)
    translate(width/2, height/2)
    fill(color(40, 50, 50))
    circle(0, 0, height)


def draw():
    translate(width/2, height/2)
    stroke(color(0, 100, 100))
    global inside
    global outside
    
    for i in range(1000):
        rand_x = random.uniform(-height/2, height/2)
        rand_y = random.uniform(-height/2, height/2)
        point(rand_x, rand_y)
        if rand_x*rand_x + rand_y*rand_y >= (height/2)*(height/2):
            outside += 1
        else:
            inside += 1
    
    estimate = 4 * (float(inside)/(float(inside) + float(outside)))
    # print("Pi estimate is: " + str(estimate))
    
    push()
    rectMode(CENTER)
    fill(color(0, 0, 100))
    rect(0, -10, 320, 50)
    textAlign(CENTER)
    fill(color(0, 0, 0))
    textSize(32)
    text(str("{:8}".format(estimate)), 0, 0)
    pop()
