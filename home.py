from tkinter import *
import scrabblePg as sp
import compt as ct
import hplay as hp
root=Tk()
root.configure(bg='skyblue')
root.geometry('1300x900+0+0')
root.resizable(False,True)
root.title("Scrabble Game")
ob1=sp.Home(root)
#ob1.creatwstr()
ob2=hp.humanplayer(ob1)
ob3=ct.computerTurn(ob1)
ob2.turn(ob3)
count=0
#while(True):
 #   if(count%2 ==0):
  #          ob2.turn()

root.mainloop()
