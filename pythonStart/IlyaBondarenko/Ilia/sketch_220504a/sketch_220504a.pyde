x = 0
g = 0
y = 0
n = 0
z = 0
p = 40
c = 0
o = int(random(0,10))
i = int(random(0,10))
score = 0
time = 0

def setup():
    global a
    frameRate(1000000000)
    a = loadImage('1.png')
    size(400,400)
    background(24,56,234)
def draw():
    global n,z,a,p,c,score,o,i,time,x,y,g
    fill(255)
    if g == 0:
        rect(100,200,40,20)
        rect(200,200,40,20)
        rect(300,200,40,20)
        fill(0)
        text('easy',100,200,40,20)
        text('medium',200,200,50,20) 
        text('hard',300,200,40,20)
    if mousePressed:
        if mouseX>100 and mouseX<140 and mouseY>200 and mouseY<220:
            g = 1
    if g==1:
            z=0
            b = loadImage('ghost.png') 
            
                    
            for pole1 in range(10):
                for pole2 in range(10):
                    fill(random(0,20),random(0,40),random(0,30))
                    rect(n,z,40,40)
                    noStroke()
                    n = n + 40
                z = z + 40
                n = 0
            image(a,p,c,40,40)
            image(b,o*40,i*40,40,40)
            fill(255)
            textSize(20)
            text('score',20,20)
            text(score,40,40)
            time = time + 0.01
            textSize(20)
            text('time',340,20)
            text(time,320,40)
            if p==o*40 and c ==i*40:
                score = score + 1
                o = int(random(0,10))
                i = int(random(0,10))
                
                
def keyPressed():
            global c,p
            if keyCode == LEFT:
                p = p - 40
                if p<0:
                    p=360
                
            if keyCode == RIGHT:
                p = p + 40
                if p>380:
                    p=0
            if keyCode == DOWN:
                c = c + 40
                if c>380:
                    c=0
            if keyCode == UP:
                c = c - 40
                if c<0:
                    c=360
            
    
        
    
