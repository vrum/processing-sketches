angle = 0
x = 0
def setup():
    size(640, 360)
    noStroke()
    background(0)
    global angle
    i = 0
    len = 40
    for x in range(0,width,len):
        for y in range(0,height,len):
            i += 1
            if i%2 == 0:
                fill(20,20,20)
            else:
                fill(20,240,240)
                
            rect(x, y, len,len)
    fill(255, 204, 0)


def draw():
    global angle
    global x
    x+=1
    if x >= 640:
        x = 0
    y = sin(angle) * 100
    ellipse(x, y+180, 5, 5)
    y = cos(angle+PI/2) * 100
    ellipse(x, y+180, 5, 5)
    angle += 0.02
