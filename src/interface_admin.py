#coding:utf-8
import customtkinter
import tkinter


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()
root.geometry("500x500")
root.title("Soluceapp_Python_interface_admin")
root.iconbitmap('./bouton.ico')


# Zone d'évènements--------------------------------------------------------------


# Zone d'affichage --------------------------------------------------------------


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame, text="Interface administrateur", font = ("Roboto",20))
label_1.pack(pady=12, padx=10)


entry_3=customtkinter.CTkEntry(master=frame, width=300, height=40, justify="center", placeholder_text="Choisissez le paramètre à modifier de l'application", fg_color="transparent", border_width=0)
entry_3.pack(pady=10, padx=10)
   
entry_1=customtkinter.CTkEntry(master=frame, width=300, height=40, justify="center", placeholder_text="")
entry_1.pack(pady=10, padx=10)

button_2 = customtkinter.CTkButton(master=frame, text="Validez votre modification", )
button_2.pack(pady=5, padx=5)


entry_2=customtkinter.CTkEntry(master=frame, width=300, height=200, justify="center")
entry_2.pack(pady=20, padx=10)

mainmenu = tkinter.Menu(root)
first_menu=tkinter.Menu(mainmenu,tearoff=0)
first_menu.add_command(label="Effacer tout", )
first_menu.add_command(label="Quitter l'application",)
second_menu=tkinter.Menu(mainmenu,tearoff=0)
second_menu.add_command(label="Liste des utilisateurs", )
second_menu.add_command(label="Ajouter un utilisateur", )
second_menu.add_command(label="Modifier un utilisateur", )
second_menu.add_command(label="Supprimer un utilisateur", )
second_menu.add_command(label="Réaliser un test unitaire",)

mainmenu.add_cascade(label="File", menu=first_menu)
mainmenu.add_cascade(label="Services d'administration", menu=second_menu)

root.config(menu=mainmenu)

#Loop---------------------------------------------------------------------

root.mainloop()