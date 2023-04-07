photos =0
photos1 =0
photos2 =0
b1=0
a1=0
dialog=0
dialog1=0
bip1=0
bi=0
gus=0
gus1=0
bi1=0
sol=0
sps=0
def setup():
    global photos,photosb,photos2,photosa
    size(800,600)
    background(255)
    photosa= (loadImage("bar.jpg"))
    photosb = (loadImage("b3.png"))
    photos2 = (loadImage("n.png"))
    photos = (loadImage("v2.png"))
    
    fill(0)
    
def draw():
    global photos,photosb,photos2,a1,b1,photosa,dialog,bip,gus1,bi1,sol
    point(200,200) 
    image(photosa,0,0,800,600)
    image(photosb,200,400,100,100)
    image(photos2,400,200,110,100)
    image(photos,b1,a1,100,100)
    if dialog==1:
        rect(00,00,600,70)
        rect(650,00,120,30)
        rect(650,50,120,30)
        fill(0)
        text(u"Привет! Сможешь пожалуйста посадить семена?А то у меня лапка болит.",30,30)
        text(u"Привет! Да смогу.",675,20)
        text(u"Пока.",675,71)
        fill(255)
    if dialog1==1:
        rect(00,00,600,70)
        rect(650,00,120,30)
        rect(650,50,120,30)
        fill(0)
        text(u"Привет! Сможешь пожалуйста принести сонлце?А ой но и так тут",30,30)
        text(u"Ок.",675,20)
        text(u"Пока.",675,71)
        fill(255)
    if sol == 1:
        fill(255,255,0)
        ellipse(500,00,70,70)
        fill(255)
        stroke(0)
    if gus == 1 :
        fill(112,56,56)
        rect(400,300,150,150)
        fill(255)
    
        
    if bip1==1:
        fill(0)
        text(u"*Вам выдан предмет ДИАЛоГИ БРАВЛ СТАРС*.",300,300)
        fill(255)
    
    if bi==1:
        rect(00,00,600,70)
        fill(0)
        text(u"Пока.",30,30)
        image(photosa,0,0,800,600)
        image(photosb,200,400,100,100)
        image(photos2,400,200,110,100)
        image(photos,b1,a1,100,100)
        fill(255)
        
    if bi1==1:
        rect(00,00,600,70)
        fill(0)
        text(u"Пока.",30,30)
        image(photosa,0,0,800,600)
        image(photosb,200,400,100,100)
        image(photos2,400,200,110,100)
        image(photos,b1,a1,100,100)
        fill(255)
    if sps==1:

        rect(40,60,100,40)
        fill(0)
        text(u"Спасибо!",80,80)
        fill(255)

def mouseClicked():
    global dialog,bip,bi,gus,dialog1,sol,sps
    if b1 > 300 and b1 < 500 and a1 > 100 and a1 < 300:
        if mouseX > 300 and mouseX < 500 and mouseY > 100 and mouseY < 500:
            rect(00,00,600,70)
            rect(650,00,120,30)
            rect(650,50,120,30)
    if b1 > 100 and b1 < 300 and a1 > 300 and a1 < 500:
        if mouseX > 100 and mouseX < 300 and mouseY > 300 and mouseY < 500:
            dialog=dialog+1
            gus=gus+1
    if mouseX > 550 and mouseX < 750 and mouseY > 0 and mouseY < 10:
        sps=sps+1
    if mouseX > 550 and mouseX < 750 and mouseY > 40 and mouseY < 60:
        bi=bi+1
    if b1 > 300 and b1 < 500 and a1 > 100 and a1 < 300:
        if mouseX > 300 and mouseX < 500 and mouseY > 100 and mouseY < 300:
            rect(00,00,600,70)
            rect(650,00,120,30)
            rect(650,50,120,30)
            dialog1=dialog1+1
            sol=sol+1
def keyPressed():
    if key == CODED:
        if keyCode == ALT:
            fill(0,128,0)
            rect(400,300,150,150)
def keyPressed():
    global a1, b1
    if key == CODED:
        if keyCode == DOWN:
            a1=a1+4
        
        if keyCode == UP:
            a1=a1-4
    
        if keyCode == LEFT:
            b1=b1-4
        
        if keyCode == RIGHT:
            b1=b1+4
        if keyCode == ALT:
            fill(0,128,0)
            rect(400,300,150,150)

        
            
    
