from tkinter import *
#from tkinter.ttk import *
cbag = {'A':9, 'B':2, 'C':2, 'D':4, 'E':12, 'F':2,
              'G':3, 'H':2, 'I':9, 'J':1, 'K':1, 'L':4, 'M':2, 'N':6, 'O':8, 'P':2, 'Q':1, 'R':6, 'S':4, 'T':6,
              'U':4, 'V':2, 'W':2, 'X':1, 'Y':2, 'Z':1, '':2}
doubleWord=[(1,1),(2,2),(3,3),(4,4),(7,7),(13,13),(12,12),(11,11),(10,10),(1,13),(2,12),(3,11),(4,10),(13,1),(12,2),(11,3),(10,4)]
trippleWord=[(0,0),(14,14),(0,14),(14,0),(7,0),(0,7),(7,14),(14,7)]
doubleLetter=[(0,3),(0,11),(11,0),(3,0),(2,6),(2,8),(3,7),(3,14),(6,2),(8,2),(7,3),(14,3),(6,6),(6,8),(8,8),(8,6),(6,12),(7,11),(8,12),(11,14),(14,11),(12,6),(11,7),(12,8)]
trippleLetter=[(1,5),(1,9),(5,1),(9,1),(5,5),(9,9),(5,9),(9,5),(13,5),(5,13),(9,13),(13,9)]
class Home:
    def __init__(self,root):
        self.wordic={}
        self.finalt=[]
        self.temptile=[]
        self.wordused=[]
        self.compscore=0
        self.humscore=0
        tileno=1
        self.x=24
        self.done={}
        self.tit=Frame(root,width=700,height=50,bg="skyblue")
        self.tit.pack(side=TOP)
        lab=Label(self.tit,text="## SCRABBLE  ##",font=('Times_New_Roman 20 bold'),bg="skyblue",width=200,fg="red")
        lab.pack()
        self.top=Frame(root,width=750,height=800,bg="black")
        self.top.pack(side=LEFT)
        self.rightframe=Frame(root,height=500,width=550)
        self.rightframe.pack(side=RIGHT)
        self.rightframe2=Frame(root,height=500,width=550)
        self.rightframe2.pack(side=BOTTOM)
        self.val=0
        loc=0
        w=0
        lisid=[]
        h=0
        self.pick="____"
        count=0
        for i in range(0,15):
            w=0
            for j in range(0,15):
                tv="____"
                bt="B"
                bt=bt+str(tileno)
                tileno=tileno+1
                l1=[]
                l1.append(i)
                l1.append(j)
                l1=tuple(l1)
                v1=StringVar()
                colour="white"
                for var in doubleWord:
                    if(var == l1):
                        colour="lightsalmon1"
                        break
                for var in trippleWord:
                    if(var==l1):
                        colour="red"
                        tv="____"
                        break
                for var in doubleLetter:
                    if(var==l1):
                        colour="lightblue"
                for var in trippleLetter:
                    if(var==l1):
                        colour="blue"
                self.bt=Label(self.top,text=tv,height=2,width=5,bg=colour)
                self.bt.place(x=w,y=h)
                
                w=w+50
            h=h+50
        print(lisid)
        h=0
        w=0
        for i in range(0,7):
            lbs=""
            lbs=lbs+str(i)
            self.lbs=Label(self.rightframe,text="____",height=2,width=10,bg="pink")
            self.lbs.place(x=h,y=300)
            h=h+80
        self.play=Label(self.rightframe,text="PLAY",bg="yellow")
        self.play.place(x=100,y=450,width=100)
        #self.passb=Label(self.rightframe,text="PASS",bg="pink")
        #self.passb.place(x=200,y=450,width=100)
        self.switchb=Label(self.rightframe,text="SWITCH",bg="yellow")
        self.switchb.place(x=300,y=450,width=100)
        self.scoreBoardH=Label(self.rightframe,text="Human : ",font=('Times_New_Roman 12 bold'))
        self.scoreBoardH.place(x=50,y=200,width=100)
        self.scoreH=Label(self.rightframe,text="0")
        self.scoreH.place(x=150,y=200,width=100)
        self.scoreBoardC=Label(self.rightframe,text="Computer : ",font=('Times_New_Roman 12 bold'))
        self.scoreBoardC.place(x=300,y=200,width=100)
        self.scoreC=Label(self.rightframe,text="0 ")
        self.scoreC.place(x=400,y=200,width=50)
        self.InstrH=Label(self.rightframe,font=('Times_New_Roman 14 bold'),text="Instructions",fg="Red")
        self.InstrH.place(x=10,y=0,width=500)
        self.Instr=Label(self.rightframe,fg="blue",bg="yellow",text="1.Human player should arrange words horizontally. \n2.Computer will arrange the words vertically.\n3.After your turn press play and wait for your turn.\n4.Press switch to change present set of words\n5.Double click on pink tile\n6.Double click on desired board tile\n7.And your word is placed on board",font=('Times_New_Roman 12 bold'))
        self.Instr.place(x=10,y=50,width=500)
        
    def creatwstr(self):
            text_file = open("scD.txt", "r")
            lines = text_file.readlines()
            #print(lines)
            #print (lines)
            count=65
            for count in range(65,91):
                lis=[]
                for word in lines:
                    if(str(word[0]) == chr(count)):
                                    lis.append(word)
                self.wordic[chr(count)]=lis
            print(self.wordic)
            quit()
        
   
                
