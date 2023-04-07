pers1 = {'HP': 7000, 'YR' : 400,  'CP' : 500+500, 'BR': "Его способность заключается в том что если Джагернаут убил 5 врагов он входит в режим берсерка его урон увеличивается на 500 единиц.Режим действует 10 секунд"}
pers2 = {'HP': 6700, 'YR' : 1000, 'CP' : 0+1, 'ACH': "Вы получаете ачивку Дэн в ярости если убьёте 100 врагов за одну игру и его фото утерянно"}
pers4 = {'HP': 1000, 'YR' : 200, 'CP' : 0}#'OP': 100 "Зелёные твари которые вырвались из лаборотории и собираются захватить мир"}    
pers3 = {'HP': 6700, 'YR' : 700,  'CP' : 700, 'HL' : "Восстанавливает 700 здоровья себе если нажать английскую е"}
photos = []
x=810 
e=10
a=550  
k=30
y=100
p=1
l=30
t=-10
prijok = 0
h=0 
n=0
o=0
q=0
pula1=x-15
pula2=x+15
vrag1x=-5
pula1x=63
vrag2x=805
pula2x=748
vrag3x=-5
pula3x=63
job1=0
job2=0
job3=0
#image(photos[0], 200, 100)
g=1
i=0
m=0
d=1
f=150
w=14400
j=0
def de():
    global x,a,g,l,t,prijok,h,e,n,k,job1,job2,job3,pula1,pula2,o,q,d
    strokeWeight(10)
    text(w,750,100)
    line(0,130,800,130)
    line(0,290,800,290)
    line(0,450,800,450)
    line(0,600,800,600)

    strokeWeight(1)
 #   
    rect(pula1,a,15,5)
    rect(pula2,a,15,5)
    rect(x,a,50,110)
    rect(pula1,a,15,5)
    rect(pula2,a,15,5)
    #if pula1 <= vrag1x and a == 70:
    if pula1 <= vrag1x and a == 70:              
        pers4['HP'] = pers1['HP'] - pers1['YR']
        pers4['HP'] = pers2['HP'] - pers2['YR']
        pers4['HP'] = pers3['HP'] - pers3['YR']
        
 #  if pula1 <= vrag3x and a == 390:
    if pula1 <= vrag3x and a == 390:              
        pers4['HP'] = pers4['HP'] - pers1['YR']
        pers4['HP'] = pers4['HP'] - pers2['YR']
        pers4['HP'] = pers4['HP'] - pers3['YR']
  #  if pula2 >= vrag2x and a == 230:
    if pula2 >= vrag2x and a == 230:              
        pers4['HP'] = pers4['HP'] - pers1['YR']
        pers4['HP'] = pers4['HP'] - pers2['YR']
        pers4['HP'] = pers4['HP'] - pers3['YR']    
  #  if k == 1:
   #     fill (0)
   #     strokeWeight(1) 
   #     rect(x,a,50,110)

     #   t=-10
    
    if prijok == 1:
        if a > 70:
                
                
            a=a+t
        
            l=l-1
        if l == 7:
            t = - t
        if l == 0:
       #    k = 0
       #    h=1 
            prijok = 0 
            t = - t
            l=30
    if a < 550:
        if n == 1:    
            a=a+e
        
            k=k-1
        if k == 7:
            e = - e
        if k == 0:
        #   k = 0
       #    h=1 
            n = 0 
            e = 10
            k=30    
def vragi():      
    global g,i,x,a,g,l,t,prijok,h,e,n,m,p,vrag1x,pula1x,vrag2x,pula2x,vrag3x,pula3x,job1,job2,job3,pula1,pula2,o,q,d,f,w
    fill(0)
    rect(pula1x,70,15,5)
    rect(pula2x,230,15,5)
    rect(pula3x,390,15,5)
    
    fill(86,188,78)
    rect(vrag1x,70,50,110)
    rect(vrag2x,230,50,110)
    rect(vrag3x,390,50,110)
  #  vrag1x= vrag1x + 1
  #  vrag2x= vrag2x - 1
  #  vrag3x= vrag3x + 1
    if d == 0:
        if f > 0:
           if vrag1x >= -50:
              vrag1x= vrag1x - 1
           if vrag2x <= 850:
              vrag2x= vrag2x + 1
           if vrag3x >= -50:
              vrag3x= vrag3x - 1
        if f < 0:
           d=1
           pers4['HP']= 1000
           f = 150
        f = f -1
    else:
        if vrag1x <= 45:
           vrag1x= vrag1x + 1
        if vrag2x >= 765:
           vrag2x= vrag2x - 1
        if vrag3x <= 45:
           vrag3x= vrag3x + 1 
        
        
    
    if a == 70:
        job1=1 
    if a == 230:
        job2=1
    if a == 390:
        job3=1
    if job1 == 1:
        pula1x=pula1x+7 
    if job2 == 1:
        pula2x=pula2x-7
    if job3 == 1:
        pula3x=pula3x+7
    if pula1x >= 815:
        pula1x = 63
        job1=0
    if pula2x <= -15:
        pula2x = 748
        job2=0
    if pula3x >= 815:
        pula3x = 63
        job3=0
    if pula1x == x and 70 == a:
        if  g == 1:      
           pers1['HP'] = pers1['HP'] - pers4['YR']
        if  g == 2:
           pers2['HP']= pers2['HP'] - pers4['YR'] 
        if  g == 3:
           pers3['HP']= pers3['HP'] - pers4['YR'] 
    if pula2x == x and 230 == a:
        if  g == 1:      
           pers1['HP'] = pers1['HP'] - pers4['YR']
        if  g == 2:
           pers2['HP']= pers2['HP'] - pers4['YR'] 
        if  g == 3:
           pers3['HP']= pers3['HP'] - pers4['YR']
    if pula3x == x and 390 == a:
        if  g == 1:      
           pers1['HP'] = pers1['HP'] - pers4['YR']
        if  g == 2:
           pers2['HP']= pers2['HP'] - pers4['YR'] 
        if  g == 3:
           pers3['HP']= pers3['HP'] - pers4['YR']


def setup():
    size(800,600)
    background(255)
    frameRate(60)
    photos.append(loadImage("DJ.jpg"))
    photos.append(loadImage("GJ.jpg"))
    photos.append(loadImage("PJ.png"))

def draw():
    global g,i,x,a,g,l,t,prijok,h,e,n,m,p,job1,job2,job3,pula1,pula2,o,q,vrag1x,vrag2x,vrag3x,d,w,f,j 
 #   pula1=x-15
 #   pula2=x+15
    background(255)
  #  text(pers4['HP'],200,200)
    fill(86,188,78)
    rectMode(CENTER)
    if w <= 0:
        i = 0
        w= 14400
    if pers4['HP'] <= 0:
        d=0
        
        
    #    vrag2x = vrag2x - 100
    
        
        
        
    
    if q == 1:
        pula1= pula1 - 10
    else:
        pula1=x-15
    if pula1 <= -30:
        
        q=0
    if o == 1:
        pula2 = pula2 + 10
    else:
        pula2=x+15
    if pula2 >= 830:
    
        o=0
    if p == 1:
        if p == -1:
            p = 2
            
        rect(400,300,400,600)
        fill(0)
        triangle(700,250,800,300,700,350)
        triangle(100,250,0,300,100,350)
        if g == 1:
        #   rect(400,300,400,600)
            image(photos[0], 200, 0)
            fill(0)
            text(u"Джаггернаут",450,100)
            text(u"Его здоровье:",250,275)
            text(pers1['HP'],330,275)
            text(u"Его урон:",250,300)
            text(pers1['YR'],305,300)
          #  text(u"Его защита:",250,325)
          #  text(pers1['3P'],317,325)
            text(u"Его способность:",250,350)
            text(pers1['CP'],345,350)
            text(u"Его способность заключается в том что он невероятно ",250,400)
            text(u"сильный и стойкий человек ",250,425)
     #   text(u"увеличивается на 500 единиц.Режим действует 10 секунд",250,450)
      
      
      #  triangle(700,250,800,300,700,350)
      #  triangle(100,250,0,300,100,350)
        if g == 2:
      #  rect(400,300,400,600)
            image(photos[1], 200, 0)
            fill(0)
            text(u"Дэн",450,100)
            text(u"Его здоровье:",250,275)
            text(pers2['HP'],330,275)
            text(u"Его урон:",250,300)
            text(pers2['YR'],305,300)
         #   text(u"Его защита:",250,325)
         #   text(pers2['3P'],317,325)
            text(u"Его способность:",250,350)
            text(pers2['CP'],345,350)
            text(u"Вы получаете ачивку Дэн в ярости если убьёте 100 врагов",250,400)
            text(u"за одну игру ,а также его фото утерянно ",250,425)
        #    triangle(700,250,800,300,700,350)
        #    triangle(100,250,0,300,100,350)
        if g == 3:
        #    rect(400,300,400,600)
             image(photos[2], 150, 0)
             fill(0)
             text(u"Елена",450,100)
             text(u"Её здоровье:",250,275)
             text(pers3['HP'],330,275)
             text(u"Её урон:",250,300)
             text(pers3['YR'],305,300)
           #  text(u"Её защита:",250,325)
           #  text(pers3['3P'],317,325)
           #  text(u"Её способность:",250,350)
          #   text(pers3['CP'],345,350)
       #      text(u"Восстанавливает 700 здоровья игроку  ",250,400)
        #     text(u" неподалёку если нажать английскую е ",250,425)
        #      triangle(700,250,800,300,700,350)
        #     triangle(100,250,0,300,100,350)
        
        
        
        
        if g == 4:
        #rect(400,300,400,600)
             fill(0)
             text(u"Гоблины",450,100)
             text(u"Их здоровье:",250,275)
             text(pers4['HP'],330,275)
             text(u"Их урон:",250,300)
             text(pers4['YR'],305,300)
            # text(u"Их защита:",250,325)
            # text(pers4['3P'],317,325)
       #      text(u"Их способность:",250,350)
      #  text(pers4['OP'],345,350)
             text(u"Зелёные твари которые вырвались из лаборотории",250,400)
             text(u" и собираются захватить мир ",250,425)
      # #      triangle(700,250,800,300,700,350)
       #     triangle(100,250,0,300,100,350)
        if g == 0:
             g=4
        if g == 5:
             g=1
    
    if i == 1:
        if g == 1:
            fill(250,30,30)
        if g == 2:
            fill(250,137,23)
        if g == 3:
            fill(23,134,250)
        if g == 4:
            i = 2 
        else:    
            de()
            vragi()
            p = 2
            w=w-1
         #   j=0
    if i == 2:
       # fill(0)
        strokeWeight(1)
        m=0
       # g=1
        i=0
        w=14400
    
   # if i == 3:
     #   i=0
      #  j=1
    if pers1['HP'] <= 0 or pers2['HP'] <= 0 or pers3['HP'] <= 0:
        text("GAME OVER",350,300)
        noLoop()
    if j == 1:
        text("GAME OVER",400,300)
        text(u"Нажмите Энтэр чтобы продолжить",400,400)    
    
    if keyPressed:
        if key == 'a' or key == 'A' or key == 'ф' or key == 'Ф':
            x=x-10
        if key == 'd' or key == 'D' or key == 'в' or key == 'В':
            x=x+10    
        if key == 'w' or key == 'W' or key == 'ц' or key == 'Ц':
        #    e=e-200
            prijok = 1
        if key == 's' or key == 'S' or key == 'ы' or key == 'Ы':
            n = 1
        
                                                    
    if x == 810:
        x = 0                                
    if x == -10:
        x = 800                                        
                                                    
                                                            
                                                                    
            
def keyPressed():
    global g,i,x,a,g,l,t,prijok,h,e,m,p,job1,job2,job3,pula1,pula2,o,q
    if key == CODED:
        if keyCode == RIGHT: 
            g=g+1
        elif keyCode == LEFT:
            g=g-1
    if key == ENTER:    
       # if g == 1:
       #     fill(250,30,30)
       # if g == 2:
       #     fill(250,137,23)
       # if g == 3:
       #     fill(23,134,250)
        i=i+1
     #   m = m + 1
        h=1
        p= p - 1 
    if key == 'q':
        q=1    
    if key == 'e':
        o=1
    
    
