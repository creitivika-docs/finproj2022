y = 10
x = 0
x2 = 0
kamen = 0
amogus = 0
skala = 0
def setup():
    global amogus,kamen,skala
    size(800,600)
    #background(20,100,20)
    skala = loadImage("skala.jpg")
    amogus = loadImage("amogus.png")
    kamen = loadImage("kamen.jpg")
def draw():
    
    global x,  y, amogus , kamen
   # background(20,100,20)
    image(skala,0,0,800,600)
    image(kamen,x,y,300,100)
    strokeWeight(100)
    fill(225)
    
    image(amogus,x2,500,100,100)
    
  #  point(x2,550)
    if (y > 800):
        x = random(0,800)
        y = -10
    y = y + 20
    
    if (y + 100 > 500) and (x2 > x-3 and x2 < x + 300):
        noLoop()
        background(0,0,0)
        fill(255,0,0)
        textSize(100)
        text(u"GAME OVER",150,300)
def keyPressed():
    global x2
    #point(x2,100)
    if key == CODED:
        if keyCode ==  RIGHT: 
            x2 = 700
        elif keyCode ==  LEFT:
            x2 = 0
            x2 = -10
            x2 = x2 + 10
