#Системы: 0-NO_SYSTEM 1-Win10 2-Win8 3-Win7 4-WinXP 5-Win200 6-Win95 7-Win11 8-Win12 9-Win20 10-MS_DOS_GRAPHIC
sys=0
bios=0
sel=0
win10boot=0
win10logon=0
win10login=0
win7boot=0
win7logon=0
win7login=0
win7=0
win7wallp=0
win7s=0
def setup():
    size(1000,800)
    background(0)
    if sys==0:
        stroke(255)
        textAlign(CENTER,CENTER)
        textSize(15)
        text("Operating system not detected. To solve this, go to BIOS and select system.",275,10)
        text("ENTER - Enter BIOS Options",100,30)
        global win7,win7wallp,win7s
        win7=loadImage("Win7.png")
        win7wallp=loadImage("win7wallp.jpg")
        win7s=loadImage("win7s.png")
def draw():
    global bios,sys,sel,win10boot,win7,win7boot
    print(sys)
    if sys==0 and keyPressed and key==ENTER:
        bios=1
        background(100)
        fill(0,0,200)
        stroke(0,0,200)
        rect(0,0,1000,30)
        stroke(0)
        fill(255)
        textAlign(CENTER,CENTER)
        textSize(15)
        text(u"0-NO_SYSTEM 1-Win10 2-Win8 3-Win7 4-WinXP 5-Win200 6-Win95 7-Win11 8-Win12 9-Win20 10-MS_DOS_GRAPHIC",500,12)
        text(u"System",30,50)
    if bios==1 and sel==0 and keyPressed and key=="c":
        sel=1
        background(100)
        fill(0,0,200)
        stroke(0,0,200)
        rect(0,0,1000,30)
        stroke(0)
        fill(255)
        textAlign(CENTER,CENTER)
        textSize(15)
        text(u"0-NO_SYSTEM 1-Win10 2-Win8 3-Win7 4-WinXP 5-Win200 6-Win95 7-Win11 8-Win12 9-Win20 10-MS_DOS_GRAPHIC",500,12)
        text(u"System",30,50)
        rectMode(CENTER)
        fill(0)
        stroke(0)
        rect(550,450,500,400)
        stroke(0,0,200)
        fill(0,0,200)
        rect(500,400,500,400)
        rectMode(CORNER)
        textAlign(CORNER,CORNER)
        fill(255)
        text(u"[0]",260,220)
        text(u"[1]",260,240)
        text(u"[2]",260,260)
        text(u"[3]",260,280)
        text(u"[4]",260,300)
        text(u"[5]",260,320)
        text(u"[6]",260,340)
        text(u"[7]",260,360)
        text(u"[8]",260,380)
        text(u"[9]",260,400)
        text(u"[10]",260,420)
        textAlign(CENTER,CENTER)
    if sys==1 and bios==0 and key==ENTER and win10logon==0 and win10login==0:
        background(0)
        fill(255)
        quad(600,200,400,300,400,500,600,600)
        stroke(0)
        strokeWeight(10)
        line(480,200,480,600)
        line(0,400,800,400)
        textSize(30)
        textAlign(CENTER,CENTER)
        text(u"Press 'B' to boot up the system",500,700)
        win10boot=1
    if sys==3 and bios==0 and key==ENTER and win7logon==0 and win7login==0:
        background(0)
        image(win7,0,0,1000,800)
        win7boot=1
def mouseClicked():
    global bios,sys,sel,win10boot,win7boot
    rectMode(CENTER)
    if bios==1 and sel==1 and mouseY>=200 and mouseY<=220:
        sys=0
        fill(100)
        stroke(100)            
        rect(500,400,600,500)
        sel=0
    if bios==1 and sel==1 and mouseY>=221 and mouseY<=240:
        sys=1
        fill(100)
        stroke(100)
        rect(500,400,600,500)
        sel=0
    if bios==1 and sel==1 and mouseY>=241 and mouseY<=260:
        sys=2
        fill(100)
        stroke(100)
        rect(500,400,600,500)
        sel=0
    if bios==1 and sel==1 and mouseY>=261 and mouseY<=280:
        sys=3
        fill(100)
        stroke(100)
        rect(500,400,600,500)
        sel=0
    if bios==1 and sel==1 and mouseY>=281 and mouseY<=300:
        sys=4
        fill(100)
        stroke(100)
        rect(500,400,600,500)
        sel=0
    if bios==1 and sel==1 and mouseY>=301 and mouseY<=320:
        sys=5
        fill(100)
        stroke(100)
        rect(500,400,600,500)
        sel=0
    if bios==1 and sel==1 and mouseY>=321 and mouseY<=340:
        sys=6
        fill(100)
        stroke(100)
        rect(500,400,600,500)
        sel=0
    if bios==1 and sel==1 and mouseY>=341 and mouseY<=360:
        sys=7
        fill(100)
        stroke(100)
        rect(500,400,600,500)
        sel=0
    if bios==1 and sel==1 and mouseY>=361 and mouseY<=380:
        sys=8
        fill(100)
        stroke(100)
        rect(500,400,600,500)
        sel=0
    if bios==1 and sel==1 and mouseY>=381 and mouseY<=400:
        sys=9
        fill(100)
        stroke(100)
        rect(500,400,600,500)
        sel=0
    if bios==1 and sel==1 and mouseY>=401 and mouseY<=420:
        sys=10
        fill(100)
        stroke(100)
        rect(500,400,600,500)
        sel=0
    rectMode(CORNER)
    if mouseX>=0 and mouseX<=50 and mouseY>=750 and mouseY<=800:
        stroke(20)
        fill(20)
        rect(0,400,300,350)
        textAlign(CORNER,CORNER)
        fill(255)
        text(u"Вырубить комп",0,700)
    if mouseX>=0 and mouseX<=300 and mouseY>=650 and mouseY<=750:
        sys=0
        bios=0
        sel=0
        win10boot=0
        win10logon=0
        win10login=0
        background(0)
        stroke(255)
        textAlign(CENTER,CENTER)
        textSize(15)
        text("Coputer is disabled. Press the CROSS on the window to shutdown your coputer",375,10)
def keyPressed():
    global sys,bios,sel,win10boot,win10logon,win10login,win7boot,win7logon,win7login,win7wallp,win7s
    if key=="b" and sys==0 and bios==1:
        bios=0
        background(0)
        stroke(255)
        fill(255)
        textAlign(CENTER,CENTER)
        textSize(15)
        text("Operating system not detected. To solve this, go to BIOS and select system.",275,10)
        text("ENTER - Enter BIOS Options",100,30)
    if key=="b" and sys==3 and bios==1:
        bios=0
        background(0)
        stroke(255)
        fill(255)
        textAlign(CENTER,CENTER)
        textSize(15)
        text("Is your selected system is 3 (Win7, 'Windows 7 Pro')",275,10)
        text("ENTER - Continue startup",100,30)
    if key=="b" and sys==1 and bios==1:
        bios=0
        background(0)
        stroke(255)
        fill(255)
        textAlign(CENTER,CENTER)
        textSize(15)
        text("Is your selected system is 1 (Win10, 'Windows 10')",275,10)
        text("ENTER - Continue startup",100,30)
    
    if key=="b" and win10boot==1:
        background(9,180,147)
        fill(100)
        circle(500,300,100)
        textSize(30)
        textAlign(CENTER,CENTER)
        text(u"Богдан",500,430)
        win10logon=1
        stroke(255)
        strokeWeight(5)
        fill(127,183,172)
        rectMode(CENTER)
        rect(500,470,100,30)
    if win10logon==1 and key==ENTER:
        win10logon=0
        win10login=1
    if sys==1 and win10login==1:
        background(113,12,232)
        rectMode(CORNER)
        fill(0)
        strokeWeight(1)
        rect(-10,750,1010,50)
        fill(255)
        stroke(255)
        rect(0,750,50,50)
    if key=="b" and win10boot==1:
        background(9,180,147)
        fill(100)
        circle(500,300,100)
        textSize(30)
        textAlign(CENTER,CENTER)
        text(u"Богдан",500,430)
        win10logon=1
        stroke(255)
        strokeWeight(5)
        fill(127,183,172)
        rectMode(CENTER)
        rect(500,470,100,30)
    if key=="b" and win7boot==1:
        background(19,139,229)
        fill(19,139,229)
        stroke(85,163,222)
        strokeWeight(10)
        rectMode(CENTER)
        rect(500,400,100,100)
        rectMode(CORNER)
        textSize(30)
        textAlign(CENTER,CENTER)
        fill(0)
        text(u"Богдан",500,500)
        win7logon=1
        stroke(255)
        strokeWeight(5)
        fill(127,183,172)
        rectMode(CENTER)
        rect(500,600,100,30)
    if win7logon==1 and key==ENTER:
        win7logon=0
        win7login=1
    if sys==3 and win7login==1:
        image(win7wallp,0,0,1000,800)
        fill(130,182,222)
        stroke(130,182,222)
        rectMode(CORNER)
        rect(0,750,1000,50)
        image(win7s,0,750,50,50)
