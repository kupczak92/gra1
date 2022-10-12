import random
import tkinter as tk
from cProfile import label
from tkinter import *
from turtle import bgcolor
from tkinter.messagebox import showinfo



window = tk.Tk()
window.title("")
window.geometry('607x335+607+335')


lines = open('10.txt').read().splitlines()

counter = 0
counter2 = 0
counter3 = 0
counter4 = 0
counter5 = 0
counter6 = 0
counter7 = 0
szanse = 3
pytanie= "  "
odpowiedzPopr = "  "
odpowiedzNPopr = "  "
odpowiedzA = " "
odpowiedzB = "  "
iloscGraczy =[]
listaZwyciezcow ={}


def dodaj1Gracza():
    szanse = 3
    szanseilosc = tk.Label(text=szanse, bg= "green", font=("Arial bold", 50)).place(x=0, y=200)
def dodaj2Gracza():
    global szanse2
    szanse2 = 3
    gracz2 = tk.Label(text=szanse2, bg= "green", font=("Arial bold", 50)).place(x=100, y=200)
    dodaj1Gracza()
def dodaj3Gracza():
    dodaj2Gracza()
    global szanse3
    szanse3 = 3
    gracz3 = tk.Label(text=szanse3, bg= "green", font=("Arial bold", 50)).place(x=200, y=200)
def dodaj4Gracza():
    dodaj3Gracza()
    global szanse4
    szanse4 = 3
    gracz4 = tk.Label(text=szanse4, bg= "green", font=("Arial bold", 50)).place(x=300, y=200)
def dodaj5Gracza():
    dodaj4Gracza()
    global szanse5
    szanse5 = 3
    gracz5 = tk.Label(text=szanse5, bg= "green", font=("Arial bold", 50)).place(x=400, y=200)
def dodaj6Gracza():
    dodaj5Gracza()
    global szanse6
    szanse6 = 3
    gracz6 = tk.Label(text=szanse6, bg= "green", font=("Arial bold", 50)).place(x=500, y=200)
def nowaGRA():
    window4 = tk.Toplevel()
    window4.title("Nowa gra")
    window4.geometry('425x130+425+130')
    label = tk.Button(window4, text="Ile osób?", bg="green",font=("Arial bold", 20)).place(x=10, y=20)
    gracz1 = tk.Button(window4, text="1 gracz", command = dodaj1Gracza).place(x=0,y=30)
    gracz2 = tk.Button(window4, text="2 graczy", command = dodaj2Gracza).place(x=80,y=30)
    gracz3 = tk.Button(window4, text="3 graczy", command = dodaj3Gracza).place(x=160,y=30)
    gracz4 = tk.Button(window4, text="4 graczy", command = dodaj4Gracza).place(x=240,y=30)
    gracz5 = tk.Button(window4, text="5 graczy", command = dodaj5Gracza).place(x=320,y=30)
    gracz6 = tk.Button(window4, text="6 graczy", command = dodaj6Gracza).place(x=400,y=30)
    global szanseilosc
    szanseilosc = tk.Label(text="                                                                   ",font=("Arial bold", 50)).place(x=0, y=200)
    global szanse
    butonClose3 = tk.Button(window4, text="Nowa gra", command = window4.destroy)
    butonClose3.pack()

def nowagra():
    window3 = tk.Toplevel()
    window3.title("Koniec gry")
    window3.geometry('425x130+425+130')
    butonClose2 = tk.Button(window3, text="koniec", command = window.destroy)
    butonClose2.pack()


def tymczasowaNG():
    global szanse
    szanse = 3
    global counter
    counter = 0
    pustePOLe1 = tk.Label(text="      ", font=("Arial bold", 30)).place(x=90, y=40)
    odppole2 = tk.Label(text="                                                                                                                                                                                            ",font=("Arial bold",50)).place(x=90, y=200)
    pktilosc = tk.Label(text=counter, font=("Arial bold", 30)).place(x=90, y=40)
    szanseilosc = tk.Label(text=szanse, font=("Arial bold",50)).place(x=90, y=200)


def odblokowaniePytania():
    buttonPytanie['state'] = NORMAL
def koniecGry(event):
    window3 = tk.Toplevel()
    window3.title("Koniec gry")
    window3.geometry('445x130+445+130')
    label = tk.Label(window3, text="koniec gry", bg="red",font=("Arial bold", 70)).place(x=10, y=20)
    global counter
    counter = 3
    #NG = tk.Button(window3, text = "nowa gra", command=nowaGRA)
    NG = tk.Button(window3, text = "nowa gra", command= tymczasowaNG)
    NG.pack()
    if szanse >= 3:
        window3.destroy()
    butonClose2 = tk.Button(window3, text="koniec", command = window.destroy)
    butonClose2.pack()
    buttonPytanie['state'] = NORMAL

def zlaOdpowiedz():
    window2 = tk.Toplevel()
    window2.title("zła odpowiedź")
    window2.geometry('835x150+835+150')
    label = tk.Label(window2, text="Błędna odpowiedź!!", bg="red",font=("Arial bold", 70)).place(x=0, y=0)
    butonClose = tk.Button(window2, text="graj dalej", command = window2.destroy)
    butonClose.pack()
    
def wskazgracza(event):
    window5 = tk.Toplevel()
    window5.title("wskaż gracza")
    window5.geometry('425x200+425+200')
    label = tk.Button(window5, text="Ile osób?", bg="green",font=("Arial bold", 20)).place(x=10, y=20)
    gracz1 = tk.Button(window5, text="1 gracz", command = Gracza1).place(x=0,y=100)
    gracz2 = tk.Button(window5, text="2 gracz", command = Gracza2).place(x=80,y=100)
    gracz3 = tk.Button(window5, text="3 gracz", command = Gracza3).place(x=160,y=100)
    gracz4 = tk.Button(window5, text="4 gracz", command = Gracza4).place(x=240,y=100)
    gracz5 = tk.Button(window5, text="5 gracz", command = Gracza5).place(x=320,y=100)
    gracz6 = tk.Button(window5, text="6 gracz", command = Gracza6).place(x=400,y=100)


def poprawnaODP(event):
    if odp1['state'] == NORMAL:
        if odpowiedzA == odpowiedzPopr:
            global counter
            counter= counter  + 10
            pktilosc = tk.Label(text=counter, bg= "green", font=("Arial bold", 30)).place(x=90, y=40)
            odp1['state'] = DISABLED
            odp2['state'] = DISABLED
            odp3 = tk.Label(text=odpowiedzA, bg="green").place(x=370, y=50)
           # wskazgracza()
        else:
            global szanse
            szanse = szanse-1
            szanseilosc = tk.Label(text=szanse, font=("Arial bold",50)).place(x=90, y=200)
            pktilosc = tk.Label(text=counter, bg= "orange", font=("Arial bold", 30)).place(x=90, y=40)
            odp2['state'] = DISABLED
            odp1['state'] = DISABLED
            odp4 = tk.Label(text=odpowiedzA, bg="red").place(x=370, y=50)
            
            if szanse==0:  
                szanseilosc = tk.Label(text="game over", font=("Arial bold",50)).place(x=90, y=200)
                koniecGry(event)
            ##else:
                #zlaOdpowiedz()
        odblokowaniePytania()


                
  

def NpoprawnaODP(event):
    if odp1['state'] == NORMAL:
        if odpowiedzB == odpowiedzPopr:
            global counter
            counter= counter  + 10
            pktilosc = tk.Label(text=counter, bg= "green", font=("Arial bold", 30)).place(x=90, y=40)
            odp1['state'] = DISABLED
            odp2['state'] = DISABLED
            odp3 = tk.Label(text=odpowiedzB, bg="green").place(x=370, y=80)
            

        else:
            global szanse
            szanse = szanse-1
            szanseilosc = tk.Label(text=szanse, font=("Arial bold",50)).place(x=90, y=200)
            pktilosc = tk.Label(text=counter, bg= "orange", font=("Arial bold", 30)).place(x=90, y=40)
            odp2['state'] = DISABLED
            odp1['state'] = DISABLED
            odp4 = tk.Label(text=odpowiedzB, bg="red").place(x=370, y=80)

            if szanse==0:  
                szanseilosc = tk.Label(text="game over", font=("Arial bold",50)).place(x=90, y=200)
                koniecGry(event)
            #else:
               # zlaOdpowiedz()
        odblokowaniePytania()
            

def nowePytanie(event):
    if szanse <=0:
        nowagra()
    if buttonPytanie['state'] == NORMAL:
        pustePOLe1 = tk.Label(text="                                                                                                                                                                                                                                                                                 ").place(x=370, y=50)
        odppole2 = tk.Label(text="                                                                                                                                                                                                                                                                                                       ").place(x=370, y=80)
        label1 = tk.Label(text="                                                                                                                                                                                   ", font=("Arial", 30)).place(x=0, y=130)
        odp1['state'] = NORMAL
        odp2['state'] = NORMAL
        lines = open('10.txt').read().splitlines()
        global myline
        myline =random.choice(lines)
        global pytanie
        pytanie = myline.split(";")
        global pytanie1
        pytanie1 = pytanie[-3]
        pytanie1 = pytanie1.upper()
        global odpowiedzPopr
        odpowiedzPopr = pytanie[-2]
        odpowiedzPopr = odpowiedzPopr.upper()
        global odpowiedzA
        odpowiedzA = random.choice(pytanie[-2:])
        odpowiedzA = odpowiedzA.upper()
        global odpowiedzB
        odpowiedzB = random.choice(pytanie[-2:])
        odpowiedzB = odpowiedzB.upper()
        while odpowiedzB == odpowiedzA:
            odpowiedzB = random.choice(pytanie[-2:])
            odpowiedzB = odpowiedzB.upper()
        global odpowiedzNPopr
        odpowiedzNPopr = pytanie[-1]
        odpowiedzNPopr = odpowiedzNPopr.upper()
        pytanie2 = str(pytanie)
        label1 = tk.Label(text=pytanie1).place(x=0, y=130)
        odp3 = tk.Label(text=odpowiedzA).place(x=370, y=50)
        odp4 = tk.Label(text=odpowiedzB).place(x=370, y=80)
        buttonPytanie['state'] = DISABLED
        


pytanieTXT = tk.Label(text="    ")
pytanieTXT.pack()
buttonPytanie = tk.Button(text="zadaj pytanie")
buttonPytanie.bind("<Button-1>", nowePytanie)
buttonPytanie.pack()
szanseLabel = tk.Label(text="szanse", font=("Arial bold",10)).place(x=90, y=180)
szanseilosc = tk.Label(text=szanse, font=("Arial bold",50)).place(x=90, y=200)

punkty2 = tk.Label(text="PKT").place(x=90, y=10)

odp1 = tk.Button(text="wybierz odpowiedź : ")
odp1.bind("<Button-1>", poprawnaODP)
odp1.pack()
odp2 = tk.Button(text="wybierz odpowiedź : ")
odp2.bind("<Button-1>", NpoprawnaODP)
odp2.pack()

window.mainloop() 