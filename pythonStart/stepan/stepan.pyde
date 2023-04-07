s5=0
c=random(400)
v=random(400)
x=200
y=200
s=0
m=10
def setup():
    size(400,400)
    background(150)
def draw():
    global x,y,s,c,v,m,s5
    if s5==0:
        fill(255,255,255)
        rect(190,185,130,30)
        textSize(20)
        fill(0,0,0)
        text(u"играть",200,200)
    if s5==1:
        background(150)
        textSize(20)
        fill(255)
        text(u"счёт=",50,50)
        text(s,110,50)
        ellipse(x,y,m,m)
        fill(random (255),random (255), random (255))
        ellipse(c,v,40,40)
        if x<c+20 and x>c-20 and y>v-20 and y<v+20:
            s=s+1
            if s>5:
                s5=2
            m=m+5
            c=random(400)
            v=random(400)
        if keyPressed:
            if keyCode==UP:
                y=y-1
                if y<m/2:
                    y=m/2
            if keyCode==DOWN:
                y=y+1
                if y>400-m/2:
                    y=400-m/2
            if keyCode==LEFT:
                x=x-1
                if x<m/2:
                    x=m/2
            if keyCode==RIGHT:
                x=x+1
                if x>400-m/2:
                    x=400-m/2
                
    
    if mousePressed:
        if mouseX>190 and mouseX<320 and mouseY>185 and mouseY<215:
               s5=1

           
