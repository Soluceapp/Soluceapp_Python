#coding:utf-8
import customtkinter
import tkinter
import time
from tkinter import messagebox
#from PIL import Image, ImageTk
from tkinter import END

from pickle import TRUE



customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()
root.geometry("500x500")
root.title("Les difficultés en Python")
root.iconbitmap('./bouton.ico')


# Classe difficulté--------------------------------------------------------------


class Dif:
    """
    Classe des difficultés à exposer par un exemple (lu par help(Dif))
    """
    def __init__(self, quest, numdif, var1, var2,var3):
        self.quest = quest
        self.numdif = numdif
        self.var1= var1
        self._var2= var2
        self.var3= var3
    def dif_10():
        entry_2.insert(0,"J'utilise une méthode static")
    dif_10 = staticmethod(dif_10)
    def _getvar2(self):
        if self._var2>1:
            return str(self._var2)+" ans"
        else:
            return str(self._var2)+" an"
    var2 = property(_getvar2)
    
class Dif_2(Dif):
    """
    Classe Dif spécialisée pour illustrer héritage
    """
    def __ini__(self,a,b,c,d,e,var4):
        Dif.__init__(self,a,b,c,d,e)
        self.var4 = var4
    def _getvar2(self):
        if self._var2>1:
            return str(self._var2)+" pouet"
        else:
            return str(self._var2)+" prout"
h0= Dif_2("0",1,1,1,"coco")
        
h1 = Dif("1/ Variables : Quel est le prix HT ? \n","1","essai","1",False)
h2 = Dif("2/ Opérations : indiquez un chiffre pair. \n","2","Auto-formation : Difficultés en Python","1",False)
h3 = Dif("3/ Conditions : Quel est votre âge ? \n","3","1","1",False)
h4 = Dif("4/ Boucles : Combien de boucles ? \n","4","1","1",False)
h5 = Dif("5/ Fonctions : Quel est ton nom ?  \n","5","1","1",False)
h6 = Dif("6/ Modularité : Chiffre à mettre \n à la racine carré ? ","6","1","1",False)
h7 = Dif("7/ Gestion erreurs : crée une erreur chiffre <=25 ?\n","7","1","1",False)
h8 = Dif("8/ POO : Afficher nature de l'attribut 5 oui/non ? ","8","1","1",False)
h9 = Dif("9/ Classes attributs : nombre d'objets créés oui/non ?\n","9","1","1",False)
h10 = Dif("10/ Méthodes : méthode static oui/non\n","10","1","1",False)
h11 = Dif("11/ Propriétés : Quel âge as-tu ?","11","1"," ans",False)
h12 = Dif("12/ Héritage : Affiche l'héritage oui/non ?","12","1","1",False)
h13 = Dif("13/ Chaînes caractères : indiquez mot de la question","13","1","1",False)
h14 = Dif("14/ Listes : indiquez le numéro d'inventaire 1 à 5","14","1","1",False)
h15 = Dif("15/ Tuples : Que mets-tu dans ta constante tuple ?","15","1","1",False)
h16 = Dif("16/ Dictionnaires : quel mot ? chien dans dico","16","1","1",False)
h17 = Dif("17/ Fichiers : mot à ajouter au fichier ?","17","1","1",False)
h18 = Dif("18/ Introduction tkinter : affiche widgets oui/non","18","1","1",False)
h19 = Dif("19/ Widgets (utilise configure) : choisir message ? ","19","1","1",False)
h20 = Dif("20/ Widgets avancés : déclancher alerte ? oui/non","20","1","1",False)
h21 = Dif("21/ Variables contrôle : changer un label ?","21","Boum !","",False)
h22 = Dif("22/ Positionnement widgets : change taille ? oui/non","22","1","1",False)
h23 = Dif("23/ Supprimer le menu ? oui/non","23","1","1",False)
h24 = Dif("24/ Temps : combien de secondes entre affichage ? ","24","1","1",False)
h25 = Dif("25/ Date d'aujourd'hui ? oui/non","25","1","1",False)
h26 = Dif("26/ Affiche thread avec Lock ? oui/non","26","1","1",False)
h27 = Dif("27/ Ouvrir le serveur (port 85) ? oui/non","27","1","1",False)
h28 = Dif("28/ Affiche données du formulaire ? oui/non","28","1","1",False)
h29 = Dif("29/ Affiche cookies ? oui/non","29","1","1",False)
h30 = Dif("30/ Voir en console la base ? oui/non","30","1","1",False)
h31 = Dif("31/ Constater un client/Serveur ? oui/non","31","1","1",False)
h32 = Dif("32/ Ouvrir une fenêtre pygame ? oui/non","32","1","1",False)
h33 = Dif("33/ Faire apparaitre un rond ? oui/non","33","1","1",False)
h34 = Dif("34/ Afficher un trait sur pygame ? oui/non","34","1","1",False)
h35 = Dif("35/ Afficher un rond ? oui/non","35","1","1",False)
h36 = Dif("36/ Bouger un rectangle gygame ? oui/non : \n","36","1","1",False)
h37 = Dif("37/ Afficher du texte pygame ? oui/non","37","1","1",False)
h38 = Dif("38/ Afficher la liste d'évènements ? oui/non","38","1","1",False)
h39 = Dif("39/ Afficher la mesure du temps ? oui/non","39","1","1",False)
h40 = Dif("40/ Jouer du son ? oui/non","40","1","1",False)


# Zone d'évènements--------------------------------------------------------------

def dif1():
    set_text2(h1.quest)
    h1.var3=TRUE
    
def dif2():
    set_text2(h2.quest) 
    h2.var3=TRUE
    
def dif3():
    set_text2(h3.quest) 
    h3.var3=TRUE
    
def dif4():
    set_text2(h4.quest) 
    h4.var3=TRUE
    
def dif5():
    set_text2(h5.quest) 
    h5.var3=TRUE
    
def dif6():
    set_text2(h6.quest) 
    h6.var3=TRUE
    
def dif7():
    set_text2(h7.quest) 
    h7.var3=TRUE
    
def dif8():
    set_text2(h8.quest) 
    h8.var3=TRUE
    
def dif9():
    set_text2(h9.quest) 
    h9.var3=TRUE
    
def dif10():
    set_text2(h10.quest) 
    h10.var3=TRUE
    
def dif11():
    set_text2(h11.quest) 
    h11.var3=TRUE
    
def dif12():
    set_text2(h12.quest) 
    h12.var3=TRUE
    
def dif13():
    set_text2(h13.quest) 
    h13.var3=TRUE
    
def dif14():
    set_text2(h14.quest) 
    h14.var3=TRUE
    
def dif15():
    set_text2(h15.quest) 
    h15.var3=TRUE
    
def dif16():
    set_text2(h16.quest) 
    h16.var3=TRUE
    
def dif17():
    set_text2(h17.quest) 
    h17.var3=TRUE
    
def dif18():
    set_text2(h18.quest) 
    h18.var3=TRUE
    
def dif19():
    set_text2(h19.quest) 
    h19.var3=TRUE
    
def dif20():
    set_text2(h20.quest) 
    h20.var3=TRUE
    
def dif21():
    set_text2(h21.quest) 
    h21.var3=TRUE
    
def dif22():
    set_text2(h22.quest) 
    h22.var3=TRUE
    
def dif23():
    set_text2(h23.quest) 
    h23.var3=TRUE
    
def dif24():
    set_text2(h24.quest) 
    h24.var3=TRUE
    entry_2.insert(0,"Affichage permier texte")
        
def dif25():
    set_text2(h25.quest) 
    h25.var3=TRUE
  
def dif26():
    set_text2(h26.quest) 
    h26.var3=TRUE
    
def dif27():
    set_text2(h27.quest) 
    h27.var3=TRUE
    
def dif28():
    set_text2(h28.quest) 
    h28.var3=TRUE
    
def dif29():
    set_text2(h29.quest) 
    h29.var3=TRUE
    
def dif30():
    set_text2(h30.quest) 
    h30.var3=TRUE
    
def dif31():
    set_text2(h31.quest) 
    h31.var3=TRUE
    
def dif32():
    set_text2(h32.quest) 
    h32.var3=TRUE
    
def dif33():
    set_text2(h33.quest) 
    h33.var3=TRUE
    
def dif34():
    set_text2(h34.quest) 
    h34.var3=TRUE

def dif35():
    set_text2(h35.quest) 
    h35.var3=TRUE
    
def dif36():
    set_text2(h36.quest) 
    h36.var3=TRUE
    
def dif37():
    set_text2(h37.quest) 
    h37.var3=TRUE

def dif38():
    set_text2(h38.quest) 
    h38.var3=TRUE
    
def dif39():
    set_text2(h39.quest) 
    h39.var3=TRUE
    
def dif40():
    set_text2(h40.quest) 
    h40.var3=TRUE


def C1():
    if h1.var3==TRUE:
        prixht=entry_1.get()
        prixht=float(prixht)
        prixht=float(prixht)+1
        texte= "le prix HT est de {} euros."
        entry_2.insert(0,texte.format(prixht))
        entry_1.delete(0,END)
        h1.var3=False
    if h2.var3==TRUE:
        info=entry_1.get()
        info=int(info)
        nombre = info % 2
        if nombre == 0 :
            entry_2.insert(0,"Le chiffre est pair")
        else: entry_2.insert(0,"Le chiffre est impair")
        h2.var3=False
    if h3.var3==TRUE:
        info=entry_1.get()
        age=int(info)
        if 0 < age <= 100:
            entry_2.insert(0,"Votre âge est situé entre 0 et 100 ans")
        else: entry_2.insert(0,"Vous avez plus de 100 ans")
        h3.var3=False
    if h4.var3==TRUE:
        info=entry_1.get()
        k=int(info)
        i = 0
        while i < k:
            entry_2.insert(0,"Boucle \n")
            i +=1 
        h3.var3=False
    if h5.var3==TRUE:
        info=entry_1.get()
        nom=str(info)
        def dire(nom="", message=""):
            entry_2.insert(0,"{} dit {}".format(nom,message))
        dire(nom, "salut par une fonction")
        h5.var3=False
    if h6.var3==TRUE:
        from math import sqrt 
        info=int(entry_1.get())
        result=sqrt(info)
        entry_2.insert(0,result)
        h6.var3=False    
    if h7.var3==TRUE:
        info=int(entry_1.get())
        if info<=25:
            raise ZeroDivisionError
            entry_2.insert(0,ZeroDivisionError)
        else: entry_2.insert(0,"Pas d'erreurs soulevées")
        h7.var3=False
    if h8.var3==TRUE:
        info=str(entry_1.get())
        if info=="oui":
            info2=type(h8.var3)
            entry_2.insert(0,info2)
        else: entry_2.insert(0,"ok")
        h8.var3=False 
    if h9.var3==TRUE:
        info=str(entry_1.get())
        if info=="oui":
            entry_2.insert(0,20)
        else: entry_2.insert(0,"ok")
        h9.var3=False 
    if h10.var3==TRUE:
        info=str(entry_1.get())
        if info=="oui":
            Dif.dif_10()
        else: entry_2.insert(0,"ok")
        h10.var3=False
    if h11.var3==TRUE:
        info=str(entry_1.get())
        entry_2.insert(0,info+h11._var2)
        h11.var3=False
    if h12.var3==TRUE:
        info=str(entry_1.get())
        if info=="oui":
            entry_2.insert(0,h0.var3)
        else: entry_2.insert(0,"ok")
        h12.var3=False
    if h13.var3==TRUE:
        info=str(entry_1.get())
        if info in h13.quest:
            entry_2.insert(0,"Le mot {} est bien dans la question".format(info))
        else: entry_2.insert(0,"Le mot n'est pas dans la question")
        h13.var3=False
    if h14.var3==TRUE:
        info=int(entry_1.get())-1
        inventaire = ["chose", "truc", "machin", "bitonio","bidule"]
        if 1<=info<=5:
            entry_2.insert(0,inventaire[info])
        else: entry_2.insert(0,"ce n'est pas un index correct")
        h14.var3=False
    if h15.var3==TRUE:
        info=str(entry_1.get())
        mon_tuple=(info,"immuable","constant")
        try:  
            entry_2.insert(0,"Ton tuple est {}.".format(mon_tuple))
        except: entry_2.insert(0,"Ce n'est pas le bon tuple")
        h15.var3=False
    if h16.var3==TRUE:
        info=str(entry_1.get())
        mon_dico = {"prénom":"tom", "chien":"danae"} 
        if info in mon_dico:
                entry_2.insert(0,"Oui {} est dans le dico".format(info))
        else: entry_2.insert(0,"Non,ce mot n'est pas dans le dico")
        h16.var3=False 
    if h17.var3==TRUE:
        info=str(entry_1.get())
        with open("donnees.txt", "a") as fic:
                animal = "\n"+info
                fic.write(animal)
        with open("donnees.txt", "r") as fic:
            entry_2.insert(0,fic.read())
        h17.var3=False  
    if h18.var3==TRUE:
        info=str(entry_1.get())
        if info=="oui":
            entry_2.insert(0,"Tada !!")
        else: entry_2.insert(0,"ok")
        h18.var3=False
    if h19.var3==TRUE:
        info=str(entry_1.get())
        entry_2.configure(placeholder_text=info)  
        h19.var3=False
    if h20.var3==TRUE:
        info=str(entry_1.get())
        if info=="oui":
            messagebox.showinfo("Alerte !", "Alerte ! Explosion !")
        else: entry_2.insert(0,"ok")
        h20.var3=False
    if h21.var3==TRUE:
        info=str(entry_1.get())
        if info=="oui":
            label_1.configure(text="Label changé !")  
        else: entry_2.insert(0,"ok")
        h21.var3=False
    if h22.var3==TRUE:
        info=str(entry_1.get())
        if info=="oui":
            root.geometry("1000x1000")
        else: entry_2.insert(0,"ok")
        h22.var3=False
    if h23.var3==TRUE:
        info=str(entry_1.get())
        if info=="oui":
            mainmenu.destroy()
        else: entry_2.insert(0,"ok")
        h23.var3=False
    if h24.var3==TRUE:
        entry_2.delete(0,END)
        info=int(entry_1.get())
        time.sleep(info)
        entry_2.delete(0,END)
        entry_2.insert(0,"Affichage deuxième texte")
        h24.var3=False
    if h25.var3==TRUE:
        info=str(entry_1.get())
        if info=="oui":
            entry_2.insert(0,time.strftime("%d/%m/%Y"))
        else: entry_2.insert(0,"ok")
        h25.var3=False 
    if h26.var3==TRUE:
        info=str(entry_1.get())
        if info=="oui":
            fic = open("donnees.txt","r")
            entry_2.insert(0,fic.read())  
        else: entry_2.insert(0,"ok")
        h26.var3=False
   
                          
def set_text2(text):
    entry_3.delete(0,END)
    entry_1.delete(0,END)
    entry_3.insert(0,text)
    entry_2.delete(0,END)
    return

def efface():
    entry_1.delete(0,END) 
    entry_2.delete(0,END)
    entry_3.delete(0,END)


# Zone d'affichage --------------------------------------------------------------

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame, text="Panoplie des difficultés en Python", font = ("Roboto",20))
label_1.pack(pady=12, padx=10)


entry_3=customtkinter.CTkEntry(master=frame, width=300, height=40, justify="center", placeholder_text="Choisissez la difficulté exposée par le menu", fg_color="transparent", border_width=0)
entry_3.pack(pady=10, padx=10)
   
entry_1=customtkinter.CTkEntry(master=frame, width=300, height=40, justify="center", placeholder_text="")
entry_1.pack(pady=10, padx=10)

button_2 = customtkinter.CTkButton(master=frame, text="Validez votre réponse", command=C1)
button_2.pack(pady=5, padx=5)


entry_2=customtkinter.CTkEntry(master=frame, width=300, height=200, justify="center")
entry_2.pack(pady=20, padx=10)

mainmenu = tkinter.Menu(root)
first_menu=tkinter.Menu(mainmenu,tearoff=0)
first_menu.add_command(label="Effacer tout", command=efface)
first_menu.add_command(label="Quitter", command=root.quit)
second_menu=tkinter.Menu(mainmenu,tearoff=0)
second_menu.add_command(label="1/ Variables", command=dif1)
second_menu.add_command(label="2/ Opérations", command=dif2)
second_menu.add_command(label="3/ Conditions", command=dif3)
second_menu.add_command(label="4/ Boucles ", command=dif4)
second_menu.add_command(label="5/ Fonctions", command=dif5)
second_menu.add_command(label="6/ Modularité ", command=dif6)
second_menu.add_command(label="7/ Gestion erreurs", command=dif7)
second_menu.add_command(label="8/ La POO ", command=dif8)
second_menu.add_command(label="9/ Classes attributs", command=dif9)
second_menu.add_command(label="10/ Méthodes", command=dif10)
second_menu.add_command(label="11/ Propriétés", command=dif11)
second_menu.add_command(label="12/ Héritage ", command=dif12)
second_menu.add_command(label="13/ Chaînes caractères", command=dif13)
second_menu.add_command(label="14/ Listes", command=dif14)
second_menu.add_command(label="15/ Tuples", command=dif15)
second_menu.add_command(label="16/ Dictionnaires", command=dif16)
second_menu.add_command(label="17/ Fichiers", command=dif17)
second_menu.add_command(label="18/ Introduction tkinter", command=dif18)
second_menu.add_command(label="19/ Widgets (utilise configure)", command=dif19)
second_menu.add_command(label="20/ Widgets avancés", command=dif20)
trois_menu=tkinter.Menu(mainmenu,tearoff=0)
trois_menu.add_command(label="21/ Variables contrôle", command=dif21)
trois_menu.add_command(label="22/ Positionnement widgets ", command=dif22)
trois_menu.add_command(label="23/ Création menu", command=dif23)
trois_menu.add_command(label="24/ Gestion du temps", command=dif24)
trois_menu.add_command(label="25/ Gestion des dates", command=dif25)
trois_menu.add_command(label="26/ Programmation asynchrone", command=dif26)


mainmenu.add_cascade(label="File", menu=first_menu)
mainmenu.add_cascade(label="Difficultés 1 à 20", menu=second_menu)
mainmenu.add_cascade(label="Difficultés 21 à 40", menu=trois_menu)

root.config(menu=mainmenu)
           
#Loop---------------------------------------------------------------------

root.mainloop()