x = 0
y = 0

def setup():
    size(800,600)
    frameRate(60)
    
def draw():
    noStroke()
    background(0,0,64)
    global x,y
    translate(400,300)
    fill(0,64,0)
    rect(-400,200,800,100)
    fill(192,192,192)
    ellipse(355,-250,200,200)
    fill(128,128,128)
    rect(-50,205,300,80)
    fill(0,0,0)
    rect(180,39,25,230)
    rect(130,85,150,25)
    fill(255,255,255)
    ellipse(mouseX-400,mouseY-300,75,150)
    fill(0,0,0)
    ellipse(mouseX-415,mouseY-315,15,15)
    ellipse(mouseX-390,mouseY-315,15,15)
    ellipse(mouseX-402,mouseY-275,20,40)
    fill(128,128,128)
    ellipse(350,-200,15,15)
