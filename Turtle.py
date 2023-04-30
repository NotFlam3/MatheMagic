import time
import turtle as t
import random
import mysql.connector as sql
import msvcrt
from threading import Timer
import Player1Wins
import Player2Wins
import PlayerTie




#Board Generation
t.tracer(0,0)
def turt(x,y):
 b=x
 c=0
 j=0
 di2={}
 while True:
   l=list(range(1,101))
   t.penup()
   t.goto(x,y)
   t.pendown()
   t.speed(0)
   if (j+1) in [1,2,3,4,17,19,23,29,31,34,37,77,46,41,51,53,59]:
       t.fillcolor('tomato')
       t.begin_fill()
       di2['tomato']=[1,2,3,4,17,19,23,29,31,34,37,77,46,41,51,53,59]
   if (j+1) in [5,15,22,26,33,39,44,63,78,82,94,92,80]:
       t.fillcolor('cyan')
       t.begin_fill()
       di2['cyan']=[5,15,22,26,33,39,44,63,78,82,94,92,80]
   if (j+1) in [6,11,14,21,27,28,36,42,47,49,73,69,95]:
       t.fillcolor('green')
       t.begin_fill()
       di2['green']=[6,11,14,21,27,28,36,42,47,49,73,69,95]
   if (j+1) in [7,10,12,15,91,24,100,30,38,43,52,97,84,71]:
        t.fillcolor('yellow')
        t.begin_fill()
        di2['yellow']=[7,10,12,15,91,24,100,30,38,43,52,97,84,71]
   if (j+1) in [8,9,13,25,99,89,81,66,65,58,72,76,57,87,83]:
        t.fillcolor('orchid')
        t.begin_fill()
        di2['orchid']=[8,9,13,25,99,89,81,66,65,58,72,76,57,87,83]
   if (j+1) in [40,50,60,61,62,90,70,74,75,85,86,88,93,96,98]:
       t.fillcolor('orange')
       t.begin_fill()
       di2['orange']=[40,50,60,61,62,90,70,74,75,85,86,88,93,96,98]
   if (j+1) in [16,18,20,32,35,45,48,54,55,56,64,67,68,79]:
       t.fillcolor('wheat')
       t.begin_fill()
       di2['wheat']=[16,18,20,32,35,45,48,54,55,56,64,67,68,79]
   if j==(len(l)):
       break
   for i in range(4):  
     if y<-250:
         break
     t.forward(50)
     t.left(90)
   t.write(l[j],align="left",font=('Arial Bold',12))
   x+=50
   j+=1
   t.end_fill()
   if x==280:
      x=-220
      y=y-50
 return di2
global maindict
maindict=turt(-220,200)
t.penup()
t.goto(-220,200)

t2=t.Turtle()


def Die(x,y):
    n=random.randint(1,6)
    t2.color('Red')
    if n==1:
        t2.goto(x+20,y-20)
        t2.pendown()
        t2.dot(15)
        t2.penup()
        t2.hideturtle()
    elif n==2:
        t2.goto(x,y-20)
        t2.pendown()
        t2.dot(15)
        t2.penup()
        t2.goto(x+40,y)
        t2.pendown()
        t2.dot(15)
        t2.penup()
        t2.hideturtle()
    elif n==3:
        t2.goto(x,y)
        t2.pendown()
        t2.dot(15)
        t2.penup()
        t2.goto(x+20,y-20)
        t2.pendown()
        t2.dot(15)
        t2.penup()
        t2.goto(x+40,y-40)
        t2.pendown()
        t2.dot(15)
        t2.penup()
        t2.hideturtle()
    elif n==4:
        t2.goto(x,y)
        t2.pendown()
        t2.dot(15)
        t2.penup()
        t2.goto(x+40,y)
        t2.pendown()
        t2.dot(15)
        t2.penup()
        t2.goto(x,y-40)
        t2.pendown()
        t2.dot(15)
        t2.penup()
        t2.goto(x+40,y-40)
        t2.pendown()
        t2.dot(15)
        t2.penup()
        t2.hideturtle()
    elif n==5:
        t2.goto(x,y)
        t2.pendown()
        t2.dot(15)
        t2.penup()
        t2.goto(x+40,y)
        t2.pendown()
        t2.dot(15)
        t2.penup()
        t2.goto(x+20,y-20)
        t2.pendown()
        t2.dot(15)
        t2.penup()
        t2.goto(x,y-40)
        t2.pendown()
        t2.dot(15)
        t2.penup()
        t2.goto(x+40,y-40)
        t2.pendown()
        t2.dot(15)
        t2.penup()
        t2.hideturtle()
    elif n==6:
        t2.goto(x,y)
        t2.pendown()
        t2.dot(15)
        t2.penup()
        t2.goto(x+40,y)
        t2.pendown()
        t2.dot(15)
        t2.penup()
        t2.goto(x,y-20)
        t2.pendown()
        t2.dot(15)
        t2.penup()
        t2.goto(x+40,y-20)
        t2.pendown()
        t2.dot(15)
        t2.penup()
        t2.goto(x,y-40)
        t2.pendown()
        t2.dot(15)
        t2.penup()
        t2.goto(x+40,y-40)
        t2.pendown()
        t2.dot(15)
        t2.penup()
        t2.hideturtle()
    return n  

        
        
connector5=sql.connect(user='root',host='localhost',passwd='mysql',database='test')
cursor1=connector5.cursor()
cursor1.execute("Delete from score")
cursor1.execute("Delete from scoretwo")
cursor1.execute("Insert into score VALUES(0)")
cursor1.execute("Insert into scoretwo VALUES(0)")
connector5.commit()


t.goto(-500,0)
t.write('Dice 2',font=('Arial Bold',12))
t.goto(-520,-70)
t.pendown()
t.fillcolor('Black')
t.begin_fill()
for k in range(4):
 t.forward(88)
 t.left(90)
t.end_fill()
t.penup()
t.goto(-500,-200)
t.write('Dice 3',font=('Arial Bold',12))
t.goto(-520,-270)
t.pendown()
t.begin_fill()
for k2 in range(4):
    t.forward(88)
    t.left(90)
t.end_fill()    
t.penup()    
t.goto(-500,230)
t.write('Dice 1',font=('Arial Bold',12))
t.goto(-520,160)
t.pendown()
t.begin_fill()
for k3 in range(4):
    t.forward(88)
    t.left(90)
t.end_fill()    
t.penup()


def locate(num,clr):
 t.penup()   
 val=num%10
 if num==10:
     xl=230
     yl=200
 if num<10:  
  xl=(-220+((val-1)*50))
  yl=200
 if num>10:
    num=num//10
    if val==0:
        val=10
        xl=(-220+((val-1)*50))
        yl=(200-((num-1)*50))
    else:        
     xl=(-220+((val-1)*50))
     yl=(200-((num)*50))    
 t.goto(xl,yl)
 t.pendown()
 t.fillcolor(clr)
 t.begin_fill()
 for s in range(4):
    t.forward(50)
    t.left(90)
 t.end_fill()
 t.penup()
global color
global points
color=['tomato','cyan','green','yellow','orchid','orange','wheat']
points=[5,10,15,20,25,30,50]
t.penup()
global rolled
rolled='yes'

t5=t.Turtle()
t.goto(340,220)
t.write("Player1",font=("Times New Roman",14))
t.goto(410,220)
t.write("Player2",font=("Times New Roman",14))




def showscore():
    t5.clear()
    totalscore=[]
    totalscore2=[]
    connector2=sql.connect(user='root',host='localhost',passwd='mysql',database='test')
    connector3=sql.connect(user='root',host='localhost',passwd='mysql',database='test')
    cursor2=connector2.cursor(buffered=True)
    cursor3=connector3.cursor(buffered=True)
    cursor3.execute("Select * from scoretwo")
    data2=cursor3.fetchall()
    cursor2.execute("Select * from score")
    data=cursor2.fetchall()
    for blah in data:
        totalscore.append(int(blah[0]))
    for blah2 in data2:
        totalscore2.append(int(blah2[0]))    
    print(totalscore,totalscore2)   
    ts=sum(totalscore)
    ts2=sum(totalscore2)
    ts=str(ts)
    ts2=str(ts2)
    print(cursor3.rowcount)
    if cursor3.rowcount==6:
        if ts>ts2:
            Player1Wins.finalscores(ts,ts2)
        if ts2>ts:
            Player2Wins.finalscores(ts,ts2)
        else:
            PlayerTie.finalscores(ts,ts2)
            
    t5.goto(350,200)
    t5.write(ts,font=('Arial Bold',14))
    t5.goto(415,200)
    t5.write(ts2,font=('Arial Bold',14))
    connector2.commit()
    connector3.commit()
    connector3.close()
    connector2.close()

 
def scoreboard(r):   
 t.penup()
 connector=sql.connect(user="root",host="Localhost",passwd="mysql",database='test')
 cursor=connector.cursor()
 cursor2=connector.cursor()
 t.color('Black')
 di={}
 if r=='yes':
  cc=0
  xc=0
  emp=points.copy()
  for p in range(7):  
   t.begin_fill()   
   t.goto(-220+xc,-330)
   t.pendown()
   t.fillcolor(color[cc])
   xc+=70
   ran=str(random.choice(emp))
   di[color[cc]]=ran
   cc+=1
   t.write(ran+'pts',align='left',font=('Arial Bold',12))
   emp.remove(int(ran))
   for o in range(4):   
    t.forward(55)
    t.left(90) 
   t.end_fill()
 t.penup()
 if r=='yes':
  choice=t.textinput("Number Chosing","Enter Pno and choice: ")
  nch=choice.split()
  playerno=nch[0]
  playerchoice=nch[1]
  if playerno=='P1' or playerno=='p1':
      clrch='Dark Red'
  if playerno=='P2' or playerno=='p2':
      clrch='Dark Blue'
  playerchoice=int(playerchoice)
  t.penup()
  locate(playerchoice,clrch)
  for smv in maindict:
     if playerchoice in maindict[smv]:
         scre=di[smv]
         query=''
         if playerno=='P1' or playerno=='p1':
          query='Insert into score VALUES({})'.format(scre)
         elif playerno=='P2'or playerno=='p2':
          query='Insert into scoretwo VALUES({})'.format(scre)
         cursor.execute(query)
 connector.commit()        
 connector.close()
 showscore()


    
         
             
  


         
         


     
t.penup()
t.goto(-350,-320)
t.color('Red')
t.pendown()
t.write("Scoring Key:",font=('Arial',14))
t.penup()
t.color('Black')



t3=t.Turtle()      
t.penup() 
def ee():
 t3.clear()   
 efg=t.numinput('HintBox','What numbers did you Roll? /n Enter like <num1><num2><num3>')
 myl=(str(efg))
 tup=(int(myl[0]),int(myl[1]),int(myl[2]))
 aa=tup[0]
 ab=tup[1]
 ac=tup[2]
 print(tup)
 pos1=aa+ab+ac
 pos2=aa+ab-ac
 pos3=aa-ab+ac
 pos4=aa+(ab*ac)
 pos5=(aa*ab)+ac
 pos6=aa*ab*ac
 pos7=(aa-ab)*ac
 pos8=aa*(ab-ac)
 pos9=(aa**2)+ab+ac
 pos10=aa+(ab**2)+ac
 pos11=aa+ab+(ac**2)
 pos12=aa-ab-ac
 pos13=-aa+ab-ac
 pos14=(aa**2)+ab+ac
 pos15=(aa**2)-ab+ac
 pos16=(aa**2)+ab-ac
 pos17=(aa**2)*ab*ac
 pos18=((aa**2)*ab)+ac
 pos19=((aa**2)+ab)*ac
 pos20=((aa**2)*ab)-ac
 pos21=((aa**2)-ab)*ac
 pos22=(ab**2)+ab+ac
 pos23=(ab**2)-aa+ac
 pos24=(ab**2)+aa-ac
 pos25=(ab**2)*aa*ac
 pos26=((ab**2)*aa)+ac
 pos27=((ab**2)+aa)*ac
 pos28=((ab**2)*aa)-ac
 pos29=((ab**2)-aa)*ac
 pos30=(aa**2)+ab+ac
 pos31=(aa**2)-ab+ac
 pos32=(aa**2)+ab-ac
 pos33=(aa**2)*ab*ac
 pos34=((aa**2)*ab)+ac
 pos35=((aa**2)+ab)*ac
 pos36=((aa**2)*ab)-ac
 pos37=((aa**2)-ab)*ac
 li=[pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos8,pos9,pos10,pos11,pos12,pos13,pos14,pos15,pos16,pos17,pos18,pos19,pos20,pos21,pos22,pos23,pos24,pos25,pos26,pos27,pos28,pos29,pos30,pos31,pos32,pos33,pos34,pos35,pos36,pos37]   
 bleh=[]
 t3.goto(550,20)
 t3.write("Possibilities: ",font=('Arial Bold',12))
 t3.goto(550,0)
 inc=0
 for something in li:
         if something>0 and something<=100 and something not in bleh:
           bleh.append(something)
 for smth in bleh:
         t3.color('Black')
         smth=str(smth)
         t3.write(smth,font=('Arial',12))
         inc=inc-20
         t3.goto(550,0+inc)
        


                   
t.goto(300,80)
t.fillcolor('Light Blue')
t.pendown()
t.begin_fill()
t.write("Show Prev")
t.goto(300,65)
t.write('  Possbs')
t.goto(300,60)
for fl in range(4):
    t.forward(60)
    t.left(90)
t.end_fill()                     
t.penup()

                                 
       
t.onkey(ee,"h")
t.listen()




def roll(x_loc,y_loc):
    if x_loc<331 and x_loc>300 and y_loc>0 and y_loc<40:
     t2.penup() 
     print('rolling dice')
     t2.clear()
     value1=Die(-500,220)
     value2=Die(-500,-10)
     value3=Die(-500,-210)
     rolled='yes'
     scoreboard(rolled)
    if x_loc<360 and x_loc>300 and y_loc<120 and y_loc>60:
       ee()
     
t.penup()    
t.goto(300,0)
t.fillcolor('Light Blue')
t.begin_fill()
for sm in range(4):
    t.pendown()
    t.forward(50)
    t.left(90)
    t.penup()
t.end_fill()    
t.goto(310,20)
t.color('Blue')
t.write('Roll',font=("Arial Bold",12))
t.onscreenclick(roll,1)
t.penup()


    


  

