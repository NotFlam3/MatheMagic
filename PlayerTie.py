import turtle as t
import time
t.clear()
def finalscores(ts,ts2):
 t.goto(0,0)
 t.write("The Game was a Tie! Well Played!",font=("Arial",20))
 time.sleep(2)
 name1=t.textinput("Scoreboard","Enter Player 1 Name:")
 time.sleep(2)
 name2=t.textinput("Scoreboard","Enter Player 2 Name:")
 f=open(r"score.txt","a")
 f.write("Highscores")
 Scores=name1+" "+str(ts)+"/t"+name2+" "+str(ts2)
 f.close()
