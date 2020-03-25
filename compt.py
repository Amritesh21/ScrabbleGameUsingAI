import hplay as hp
import scrabblePg as sci
class computerTurn:
    def __init__(self,arg):
        self.ob2=arg
        self.sd=0
        self.hst=0
        self.wordlen=0
        self.recurs=0
        self.rc1=[]
        self.tripleWord = [0, 7, 14, 105, 119, 210, 217, 224]
        self.doubleWord = [16, 28, 32, 42, 48, 56, 64, 70, 154, 160, 168, 176, 182, 192, 196, 208]
        self.doubleLetter = [3, 11, 36, 38, 45, 52, 59, 92, 96, 98, 102, 108, 116, 122, 126, 128, 132, 165, 172, 179, 186, 188, 213, 221]
        self.tripleLetter = [20, 24, 76, 80, 84, 88, 136, 140, 144, 148, 200, 204]
    def cturn(self):
        text_file = open("scD.txt", "r")
        lines = text_file.readlines()
        sg=""
        for key in (self.ob2.done):
                    sg=str(key)
        def calheurist():
            self.recurs=self.recurs+1
            if(self.recurs >1):
                return 1
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ",self.recurs," >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(self.rc1)
            availoption=self.ob2.temptile
            print("the value of availopt is",availoption[0])
            #self.listobfilled=availoption[0]
            #hrt=0
            self.cscore=0
            compscore=0
            for j in self.ob2.temptile:
                lds=[]
                i=j
                wlen=0
                heurist=0
                print(wlen)
                while( i<=255):
                    if((i-1) in self.tripleWord):
                        heurist=heurist+6
                        #compscore=compscore*3
                    elif((i-1) in self.doubleWord):
                        heurist=heurist+4
                        #compscore=compscore*2
                    elif((i-1) in self.doubleLetter):
                        heurist=heurist+2
                        #compscore=compscore+i*2
                    elif((i-1) in self.tripleLetter):
                        heurist=heurist+3
                        #compscore=compscore+i*3
                    elif( i in  self.ob2.temptile  and heurist>0):
                        break
                    else:
                        heurist=heurist+1
                    wlen=wlen+1
                    print(heurist)   
                    i=i+15
                if(heurist > self.hst):
                        self.hst=heurist
                        self.listobfilled=j
                        self.wordlen=wlen
            print("Value of path is ",heurist)
                #calheurist()
            tempwidget=[]
            ctile=self.listobfilled
            fword=""
            cout=0
            z=0
            sg=""
            cget=0
            #self.cscore=compscore
            for widget in self.ob2.top.winfo_children():
                        cout=cout+1
                        #print(cout)
                        if((widget in self.ob2.finalt) and cget!=0 and ctile==cout):#if widget encountered is in the list of filled widgets then break the loop
                            print(cout," ",z," terminated")
                            availoption.remove(self.listobfilled)
                            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Inside the terminator >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.")
                            calheurist()
                        elif(cout==self.listobfilled and fword==""):
                            cget=cget+1
                            sg=widget['text']
                            print(sg)
                            ctile=self.listobfilled+15
                            bn=0
                            for word in lines:
                                if(word[0] == sg[0] and len(word)<=self.wordlen and (word.strip() not in (self.ob2.wordused)) and widget['text']!="____"):
                                    bn=bn+1
                                    #print("wlen .............",self.wordlen)
                                    fword1=word.strip()
                                    if(bn==1):
                                        fword=fword1
                                    #print(len(word))
                                    #self.ob2.wordused.append(fword)
                                    #text_file.close()
                                    
                                    if(len(fword1)> len(fword)):
                                        fword=fword1
                                        print(fword)
                                    else:
                                        continue
                                elif(ord(word[0]) >ord(sg[0])):
                                    z=z+1
                                    print("Word not found")
                                    text_file.close()
                                    break
                        elif(fword !="" and ctile==cout and z<len(fword)):
                                for alp in fword:
                                    for alp in sci.cbag:
                                        if sci.cbag[alp]!=0:
                                            sci.cbag[alp]=(sci.cbag[alp]-1)
                                widget['text']=fword[z]
                                widget['bg']="lightgreen"
                                print("checking>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                if((ctile-1) in self.tripleWord):
                                    #heurist=heurist+6
                                    compscore=compscore+len(fword)*3
                                elif((ctile-1) in self.doubleWord):
                                    #heurist=heurist+4
                                    compscore=compscore+len(fword)*2
                                elif((ctile-1) in self.doubleLetter):
                                    #heurist=heurist+2
                                    compscore=compscore+2
                                elif((ctile-1) in self.tripleLetter):
                                    #heurist=heurist+3
                                    compscore=compscore+3
                                else:
                                    compscore=compscore+1
                                tempwidget.append(widget)
                                z=z+1
                                ctile=ctile+15
                                self.cscore=compscore
                                #self.ob2.finalt.append(widget)
                                if(z ==len(fword)): #or fword[z]==""):
                                    self.ob2.compscore=self.ob2.compscore+compscore
                                    print(" Comp score:  is ",compscore)
                                    #self.ob2.scoreC['text']=(self.ob2.compscore)
                                    print("self.listobfilled  :",self.listobfilled)
                                    (self.ob2.temptile).remove(self.listobfilled)
                                    print("self.ob2.temptile:  ",self.ob2.temptile)
                                    print("checking>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                                    self.ob2.wordused.append(fword)
                                    #updwid()
                                    fword=""
                                    cout=0
                                    z=0
                                    sg=""
                                    return 1
        h=calheurist()
        print(" Comp score:  is ",self.cscore)
        print("*************************   ",h,"    ****************************")
        (self.ob2.temptile).remove(self.listobfilled)
        self.rc1=self.ob2.temptile
        self.ob2.compscore=self.ob2.compscore+self.cscore
        print("-----------------",self.ob2.compscore)
        self.ob2.scoreC['text']=(self.ob2.compscore)
        if(h==None):
            #self.ob2.compscore=self.ob2.compscore+compscore
            #self.ob2.scoreC['text']=(self.ob2.compscore)
            return (self.listobfilled)
         #checking the word from word dictionary
        '''fword=""
        chk=0
        for word in lines:
                   if(word[0] == sg[0]):
                                fword=word
                                print(fword)
                                chk+1
                                break
                   elif(ord(word[0]) >ord(sg[0])):
                                print("Word not found")
                                break
                                #breakpoint'''
        
