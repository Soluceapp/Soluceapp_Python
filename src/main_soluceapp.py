#coding:utf-8
import customtkinter


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()
root.geometry("500x500")
root.title("Soluceapp_Python")
root.iconbitmap('./bouton.ico')


# Zone d'évènements--------------------------------------------------------------


# Zone d'affichage --------------------------------------------------------------

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label_01 = customtkinter.CTkLabel(master=frame, text="Soluceapp_Python", font = ("Roboto",20))
label_01.pack(pady=25, padx=10)

label_01 = customtkinter.CTkLabel(master=frame, text="Indentification :", font = ("Arial",15))
label_01.pack(pady=0, padx=10)

entry_1=customtkinter.CTkEntry(master=frame, width=300, height=40, justify="center", placeholder_text="Nom d'utilisateur (mail)")
entry_1.pack(pady=12, padx=10)

entry_2=customtkinter.CTkEntry(master=frame, width=300, height=40, justify="center", placeholder_text="Mot de passe*")
entry_2.pack(pady=6, padx=10)

label_02 = customtkinter.CTkLabel(master=frame, text="* 12 caractères mini, 1 majuscule mini, 1 minuscule mini.", font = ("Arial",10))
label_02.pack(pady=0, padx=10)

button_1 = customtkinter.CTkButton(master=frame, text="Valider",)
button_1.pack(pady=12, padx=5)

button_2 = customtkinter.CTkButton(master=frame, text="Créer un compte",)
button_2.pack(pady=12, padx=5)

button_3 = customtkinter.CTkButton(master=frame, text="Modifier le mot de passe",)
button_3.pack(pady=12, padx=5)

#Loop---------------------------------------------------------------------

root.mainloop()