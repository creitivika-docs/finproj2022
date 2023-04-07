add_library("sound")
p=1
suma=0
kilik=0
pik=100000000
w=0
z=0
x=400
y=300
o=''
l=1
def setup():
    global c,w,x,y,suma,kilik,pik,t,u,p,ca1,e,m,o,b,l,sound
    m=loadImage('e.jpg') #пелемени(не используются)
    c=loadImage('SpiritBoom.png')#шлёпа
    ca1=loadImage('SpiritBoomupd.png')#шлёпа палучше
    w=loadImage('1locate.png')#локация1
    t=loadImage('2locate.png')#локация2
    u=loadImage('locate3.png')#локация3
    b=loadImage('backRooms.jpg')#бакрумы
    sound=SoundFile(this,"t.mp3")
    sound.play()
    size(800,600)
def draw():
    global c,sound,w,x,y,suma,kilik,pik,t,u,p,ca1,e,m,o,b,l

    if kilik>100000 and kilik<10000000:
        image(t,0,0,800,600)
    elif kilik>10000000:
        image(u,0,0,800,600)
    else:
        image(w,0,0,800,600)

    if p==1:
        image(c,x,y,100,100)
    if p==2:
        image(ca1,x,y,100,100)
    text(suma,10,10)
    text(kilik,10,300)
    text(o,600,600)

    

def keyPressed():
    global c,w,x,y,suma,kilik,pik,t,u,p,ca1,e,m,o,b,l
    o=o+key
    if o=='backroom':
        image(b,0,0,800,600)
    if key=='d':
        x=x+5
    if key=='a':
        x=x-5
    if key=='s':
        y=y+5
    if key=='w':
        y=y-5
    if key==' ':
        suma=suma+pik
        kilik=kilik+pik
    if key=='1'and suma>99:
        suma=suma-100 
        pik=pik+1
    if key=='2'and suma>999:
        suma=suma-1000
        pik=pik+10
    if key=='3' and suma>99999999:
        suma=suma-100000000
        p=2
        
