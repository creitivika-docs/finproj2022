r=['']
xard=340
yard=70
xsv=0
ysv=0
o=620
a=0
yd=200
xd=80
def setup():
    imageMode(CENTER)
    global st,sy,su,si,so
    size(1000,1000)
    st=loadImage('1.png')
    sy=loadImage('2.png')
    su=loadImage('3.png')
    si=loadImage('4.png')
    so=loadImage('5.png')
    image(st,200,250)
    image(sy,80,200)    
    image(su,340,70)
    image(si,130,50)
    image(so,50,50,50,50)
    ellipse (xd+25,yd-55,8,8)
    ellipse (xd+36,yd-55,8,8)
    ellipse (xd+16,yd-55,8,8)
    ellipse (xd+6,yd-55,8,8)
    ellipse (xd-4,yd-55,8,8)
    ellipse (xd-14,yd-55,8,8)
    ellipse (xd-24,yd-55,8,8)
    ellipse (xd-34,yd-55,8,8)
    
    ellipse (xard+77,yard-53,8,8)
def draw():
    imageMode(CENTER)
    global st,sy,su,si,so,a,o,xard,yard,xsv,ysv
    o=620
    rect(600,0,400,1000)
    push()
    fill(1)
    textSize(30)
    for q in r:
        text(q,o,30)
        o=o+20
    pop()
    xsv=200
    ysv=250
    xard=340
    yard=70

    

    
def keyPressed():
    global a,xard,yard,xsv,ysv
    if key=="q":   
        ellipse (xsv+6,ysv+66,10,10)
        line (xard+77,yard-53,xsv+6,ysv+66) 

    r.append(key)
    a=a+1
    
    
