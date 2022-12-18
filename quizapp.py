#Quizapp- Aleksa Veličković Uroš Srbovan i Janka Ivan R41
#--------------------------------------------------------
#Unos biblioteka:
import tkinter
import time
from functools import partial
import threading

def spavaj():
    #drugi deo funkcije change koji je odgovoran za resetovanje boja tastera u belo i labele resenje kao i postavljanja sledećeg pitanja

    global resenje
    global button1
    global button2
    global button3
    global button4
    global window1
    global brtac
    global brnetac
    global i
    # čekamo 2 sekunde tokom koje je prikazano rešenje
    time.sleep(2)
    # prestajemo da ispisujemo labelu rešenje
    resenje.pack_forget()
    # bojimo dugmiće u belo
    button1.config(background = "white")
    button2.config(background = "white")
    button3.config(background = "white")
    button4.config(background = "white")
    # ako kviz idalje traje (igrač je na pitanju 0-6) posle prikazanog rezultata njihovog odgovora, ažuriraju se objekti prozora sa novim pitanjima i odgovorima:
    if i <=5:

        i+=1
        pitanje.config(text =lista_pitanja[i])
        button1.config(text =lista_button1[i])
        button2.config(text =lista_button2[i])
        button3.config(text =lista_button3[i])
        button4.config(text =lista_button4[i])
    # ako kviz ne traje više ispisuje se statistika kviza:
    if i >=6:
        # prestajemo da ispisujemo dugmiće
        button1.place_forget()
        button2.place_forget()
        button3.place_forget()
        button4.place_forget()
        #sastavljamo string sa porukom:
        poruka = "Čestitam!\nBroj tačnih odgovora: "+ str(brtac) +"\nBroj netačnih odgovora: "+ str(brnetac)
        #u labelu pitanje stavljamo statistiku kviza
        pitanje.configure(text=poruka)
def exit_prog():
    #funkcija za izlaz iz programa
    window.destroy()
def main_menu():
    #funkcija za main menu:
    global window
    window =tkinter.Tk()
    window.title("Kvizz!")
    window.geometry("852x480")
    window.configure(bg="grey") # namestanje samog prozora
    naslov =tkinter.Label(text="Dobrodosli u Kviz!!!1!", font=("Comic Sans MS", 24))
    start =tkinter.Button(text="Zapocni avanturu!", width=25, background = "white", font = ("Comic Sans MS",18), command = quiz)

    end =tkinter.Button(text="izlazak iz programa", width=25, background = "white", font = ("Comic Sans MS",18),command = exit_prog)
    #set-up labela i dugmića


    #postavljanje naslova i dugmića
    naslov.pack()
    start.place(x=247, y =160)
    end.place(x=247, y =225)
    window.mainloop() #mainloop prozora
def change(button_pressed):
    #funkcija change gleda resenje i zajedno sa spavaj() posle vremenskog intervala od 2 sekunde menja pitanje na sledeće
    global i
    global pitanje
    global resenje
    global button1
    global button2
    global button3
    global button4

    global brtac
    global brnetac

    #pokretanje f-je spavaj() na drugom thread-u
    t1 =threading.Thread(target = spavaj)
    t1.start()

    # provera rešenja, ako je tačno rešenje, brtac++, ako nije brnetac++.
    # labela resenje dobija vrednost "Tačno" ili "Netačno"
    # tačni tasteri postaju zeleni, a u funkciji spavaj() postaju ponovo beli, isto tako i za netačne- postaju crveni (boja #B22222	u hex-u)
    if i == 0:
        if button_pressed == 1:
            resenje.pack()
            resenje.config(text="Tačno!")
            button1.config(background = "green")
            brtac +=1
                                
        else: 
            resenje.pack()
            resenje.config(text="Netačno!")
            ## racunar koji koristim podrzava stariju verziju Pythona-> koristim if-else umesto match-case -Janka
            if button_pressed == 2:
                button2.config(bg="#B22222")  
            if button_pressed == 3:
                button3.config(bg="#B22222")  
            if button_pressed == 4:
                button4.config(bg="#B22222") 
            brnetac +=1
    if i == 1:
        if button_pressed == 4:
            resenje.pack()
            resenje.config(text="Tačno!")
            button4.config(background = "green")
            brtac +=1
                                
        else: 
            resenje.pack()
            resenje.config(text="Netačno!")
            ## racunar koji koristim podrzava stariju verziju Pythona- koristim if-else umesto match-case
            if button_pressed == 1:
                button1.config(bg="#B22222")  
            if button_pressed == 2:
                button2.config(bg="#B22222")  
            if button_pressed == 3:
                button3.config(bg="#B22222") 
            brnetac +=1
    if i == 2:
        if button_pressed == 3:
            resenje.pack()
            resenje.config(text="Tačno!")
            button3.config(background = "green")
            brtac +=1
                                
        else: 
            resenje.pack()
            resenje.config(text="Netačno!")
            ## racunar koji koristim podrzava stariju verziju Pythona- koristim if-else umesto match-case
            if button_pressed == 1:
                button1.config(bg="#B22222")  
            if button_pressed == 2:
                button2.config(bg="#B22222")  
            if button_pressed == 4:
                button4.config(bg="#B22222") 
            brnetac +=1
    if i == 3:
        if button_pressed == 3:
            resenje.pack()
            resenje.config(text="Tačno!")
            button3.config(background = "green")
            brtac +=1
                                
        else: 
            resenje.pack()
            resenje.config(text="Netačno!")
            ## racunar koji koristim podrzava stariju verziju Pythona- koristim if-else umesto match-case
            if button_pressed == 1:
                button1.config(bg="#B22222")  
            if button_pressed == 2:
                button2.config(bg="#B22222")  
            if button_pressed == 4:
                button4.config(bg="#B22222") 
            brnetac +=1
    if i == 4:
        if button_pressed == 4:
            resenje.pack()
            resenje.config(text="Tačno!")
            button4.config(background = "green")
            brtac +=1
                                
        else: 
            resenje.pack()
            resenje.config(text="Netačno!")
            ## racunar koji koristim podrzava stariju verziju Pythona- koristim if-else umesto match-case
            if button_pressed == 1:
                button1.config(bg="#B22222")  
            if button_pressed == 2:
                button2.config(bg="#B22222")  
            if button_pressed == 3:
                button3.config(bg="#B22222") 

            brnetac +=1
    if i == 5:
        if button_pressed == 2:
            resenje.pack()
            resenje.config(text="Tačno!")
            button2.config(background = "green")
            brtac +=1
                                
        else: 
            resenje.pack()
            resenje.config(text="Netačno!")
            ## racunar koji koristim podrzava stariju verziju Pythona- koristim if-else umesto match-case
            if button_pressed == 1:
                button1.config(bg="#B22222")  
            if button_pressed == 3:
                button3.config(bg="#B22222")  
            if button_pressed == 4:
                button4.config(bg="#B22222") 
            brnetac +=1
def quiz():
    #telo quizapp-a, ovo je skelet gde se otvara prozor, i inicializuje prvo pitanje
    global i
    i = 0 # brojac za liste pitanja i odgovora
    window.destroy() #zatvaranje main-menu prozora
    global window1
    global pitanje
    global resenje
    global button1
    global button2
    global button3
    global button4

    #otvaranje novog prozora

    window1 =tkinter.Tk()
    window1.geometry("852x480")
    window1.configure(bg="grey")
    window1.title("Kvizz!")

    #postavljanje teksta s pitanjima i dugmice sa odgovorima, koristi se modul partial da bi preneli argument koje smo dugme pritisnuli u funkciju change()

    pitanje =tkinter.Label(text=lista_pitanja[i], font = ("Comic Sans MS", 24), justify ="center", wraplength=700) #justify- center je zbog centriranja prilikom word wrapping-a
    resenje =tkinter.Label(font=("Comic Sans MS",24)) #setovaje labele s porukom "Tačno" ili "Netačno", ali je nećemo crtati sada
    button1 =tkinter.Button(text=lista_button1[i], width =25, background ="white", font=("Comic Sans MS",18),command = partial(change,button_pressed =1))
    button2 =tkinter.Button(text=lista_button2[i], width =25, background ="white", font=("Comic Sans MS",18),command = partial(change, button_pressed =2))
    button3 =tkinter.Button(text=lista_button3[i], width =25, background ="white", font=("Comic Sans MS",18),command = partial(change, button_pressed =3))
    button4 =tkinter.Button(text=lista_button4[i], width =25, background ="white", font=("Comic Sans MS",18),command = partial(change, button_pressed =4))

        
    #crtanje tih objekata i pokretanja petlje

    pitanje.pack()
    button1.place(x= 25, y= 160)
    button2.place(x= 25, y= 225)
    button3.place(x= 439, y= 160)
    button4.place(x= 439, y= 225)
    window1.mainloop()



#liste sa pitanjima i mogućim odgovorima, plan je da ažuriramo prozor umesto zatvaranja postojećeg i otvaranja novog
lista_pitanja =["Kada je bio Kosovski boj?","Koliko kalorija ima u banani?", "Gde je odigrano prvo Svetsko prvenstvo u fudbalu 1930. godine", "Glavni grad Švajcarske je?:",'Ko je prvi uveo termin "Sociologija"', 'Šta znači reč "Apopleksija?"',""]
lista_button1 =["28.6.1389.","134.5","Brazil","Bazel","Fridrif Engels","Kreativnost",""]
lista_button2 =["28.7.1389.","254","Italija","Cirih","Maks Veber","Slog",""]
lista_button3 =["27.6.1389.", "75","Urugvaj","Bern","Džordž Mid","Zaboravnost",""]
lista_button4 =["24.7.1389.","dovoljno","Argentina","Nošatel","Ogist Kont","Povišen Pritisak",""]

#inicializujemo broj tacnih i netacnih odgovora na 0
global brtac
global brnetac
brtac = 0
brnetac = 0
main_menu()