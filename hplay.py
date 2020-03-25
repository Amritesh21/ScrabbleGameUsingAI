from tkinter import *
import random
import scrabblePg as sg
import compt as compTurn
from tkinter import messagebox
bag = {'A':9, 'B':2, 'C':2, 'D':4, 'E':12, 'F':2,
              'G':3, 'H':2, 'I':9, 'J':1, 'K':1, 'L':4, 'M':2, 'N':6, 'O':8, 'P':2, 'Q':1, 'R':6, 'S':4, 'T':6,
              'U':4, 'V':2, 'W':2, 'X':1, 'Y':2, 'Z':1, '':2}
class humanplayer:
    def __init__(self,arg):
        self.ob2=arg
        self.strg=""
        self.taskp=[]
        self.taskf=[]
        self.til=[]
        ct=0
        text_file = open("scD.txt", "r")
        self.lines = text_file.readlines()
        self.used=[]
        self.tripleWord = [0, 7, 14, 105, 119, 210, 217, 224]
        self.doubleWord = [16, 28, 32, 42, 48, 56, 64, 70, 154, 160, 168, 176, 182, 192, 196, 208]
        self.doubleLetter = [3, 11, 36, 38, 45, 52, 59, 92, 96, 98, 102, 108, 116, 122, 126, 128, 132, 165, 172, 179, 186, 188, 213, 221]
        self.tripleLetter = [20, 24, 76, 80, 84, 88, 136, 140, 144, 148, 200, 204]
        for widget in self.ob2.rightframe.winfo_children():
                            ct=ct+1
                            if(ct<8 and widget['text']=="____"):
                                lettr, notile = random.choice(list(bag.items()))
                                if(notile ==0):
                                    while (notile !=0):
                                        lettr, notile = random.choice(list(bag.items()))
                                else:
                                    notile=notile-1
                                    bag[lettr]=notile
                                    widget['text']=lettr
    def turn(self,arg1):
        self.obj3=arg1
        for widget in self.ob2.top.winfo_children():
            def double_click(event):#command=lambda:self.prin()
                    print('Double clicked at x = % d, y = % d',event.widget)
                    tile=str(event.widget)
                    print((event.widget).cget("text"))
                    if(self.ob2.pick !="____" and (event.widget)['text']=="____" and (event.widget not in self.taskp)):
                        print(event.widget not in self.taskp)
                        (event.widget)['text']=self.ob2.pick
                        (event.widget)['bg']="yellow"
                        self.ob2.pick="____"
                        self.taskp.append(event.widget)
                        self.til.append(event.widget)
                    elif(self.ob2.pick =="____" and self.strg !="" and (event.widget not in self.taskf)):
                            self.ob2.pick=str((event.widget).cget("text"))
                            #self.strg=self.(self.ob2.pick)
                            (event.widget)['text']='____'
                            self.taskp.remove(event.widget)
                            self.til.remove(event.widget)
            widget.bind('<Double 1>', double_click)
        count=0
        for widget in self.ob2.rightframe.winfo_children():
            count=count+1
            if(count<8):
                def double_click(event):#command=lambda:self.prin()
                        print('Double clicked at x = % d, y = % d',event.widget)
                        print((event.widget).cget("text"))
                        if(self.ob2.pick =="____"):
                            self.ob2.pick=str((event.widget).cget("text"))
                            self.strg=self.strg+(self.ob2.pick)
                            (event.widget)['text']='____'
                        elif(self.ob2.pick !="____" and (event.widget)['text']=="____" and self.strg != ""):
                                    (event.widget)['text']=self.ob2.pick
                                    #(event.widget)['bg']="yellow"
                                    self.ob2.pick="____"
                widget.bind('<Double 1>', double_click)
            elif(count==8):
                def double_click(event):#command=lambda:self.prin()
                        ok=0
                        #if(strg==""):

                         #   messagebox.showinfo("ERROR","PLEASE MAKE A MOVE")
                        for word in self.lines:
                            if word.strip()==self.strg:
                                ok=ok+1
                                #self.strg="____"
                                break
                        if(ok==0 and self.strg !=""):
                             messagebox.showinfo("ERROR","PLEASE FILL A VALID WORD")
                             for widget in self.ob2.top.winfo_children():
                                 if(widget['text']!="____" and (widget in self.til)):
                                     widget['text']="____"
                                     self.taskp.remove(widget)
                             self.til=[]
                             mn=0
                             lr=list(self.strg)
                             idx=0
                             for widget in self.ob2.rightframe.winfo_children():
                                 mn=mn+1
                                 if(widget['text']=="____" and mn<8):
                                     widget['text']=lr[idx]
                             self.strg=""
                        else:
                            print('Double clicked at x = % d, y = % d',event.widget)
                            ct=0
                            gt=0
                            lds=[]
                            for i in self.taskp:
                                self.taskf.append(i)
                                #if i not in self.ob2.finalt:
                                self.ob2.finalt.append(i)#contains widget id
                                i=str(i)
                                cj=0
                                ld1=""
                                for j in i:
                                    if (j.isdigit()==True and cj>9):
                                            ld1=ld1+j
                                    cj=cj+1
                                    
                                print(ld1)
                                lds.append(eval(ld1))
                                if (eval(ld1) not in self.ob2.temptile  and eval(ld1) not in self.used):
                                    self.ob2.temptile.append(eval(ld1))#contains widget numbetr
                            print(self.ob2.temptile)
                            self.ob2.done[self.strg]=lds
                            self.ob2.wordused.append(self.strg)
                            self.til=[]
                            #self.strg=""
                            '''with open("scD.txt") as openfile:
                                
                                for line in openfile:

                                    for part in line.split():
                                        if self.strg in part:
                                            gt=gt+1
                                            print(gt)
                                            break'''
                            for h in self.ob2.temptile:
                                if(self.strg!= ""):
                                    if((h-1) in self.tripleWord):
                                        #heurist=heurist+6
                                        self.ob2.humscore=self.ob2.humscore+len(self.strg)*3
                                    elif((h-1) in self.doubleWord):
                                        #heurist=heurist+4
                                        self.ob2.humscore=self.ob2.humscore+len(self.strg)*2
                                    elif((h-1) in self.doubleLetter):
                                        #heurist=heurist+2
                                        self.ob2.humscore=self.ob2.humscore+2
                                    elif((h-1) in self.tripleLetter):
                                        #heurist=heurist+3
                                        self.ob2.humscore=self.ob2.humscore+3
                                    else:
                                        self.ob2.humscore=self.ob2.humscore+1
                            self.ob2.scoreH['text']=self.ob2.humscore
                            self.strg=""
                            for widget in self.ob2.rightframe.winfo_children():
                                ct=ct+1
                                if(ct<8 and widget['text']=="____"):
                                    lettr, notile = random.choice(list(bag.items()))
                                    if(notile ==0):
                                        while (notile !=0):
                                            lettr, notile = random.choice(list(bag.items()))
                                    else:
                                        notile=notile-1
                                        bag[lettr]=notile
                                        widget['text']=lettr
                            print(self.ob2.done)
                            r=self.obj3.cturn()
                            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^    ",r,"        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                            if(r != None):
                                print(self.ob2.temptile)
                                self.used.append(r)
                                #self.ob2.temptile.remove(r)
                                self.obj=compTurn.computerTurn(self.ob2)
                                self.turn(self.obj)
                widget.bind('<Double 1>', double_click)
            elif count==9:
                def double_click(event):
                    cst=0
                    for widget in self.ob2.rightframe.winfo_children():
                                #print("ok")
                                cst=cst+1
                                if(cst<8):
                                    lettr, notile = random.choice(list(bag.items()))
                                    if(notile ==0):
                                        while (notile !=0):
                                            lettr, notile = random.choice(list(bag.items()))
                                    else:
                                        bag[lettr]=notile
                                        widget['text']=lettr
                widget.bind('<Double 1>', double_click)
                
                
                
