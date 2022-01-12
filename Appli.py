import tkinter as tk 
from tkinter import * 
from tkinter import font 

#crer fenetre
window = Tk()
window.title("Qr Generateur")
window.geometry("1080x720")
window.minsize(480, 360)
window.config(background="#FFFFFF")
window.iconbitmap("ca.ico")


#creer frame (boite)
frame_1 = Frame(window, background="#FFFFFF")
frame_2 = Frame(window,background="#FFFFFF")

#creer les widgets (contenus dans la frame 1)
label_title = Label(frame_1, text="Générateur de QR Code du crédit agricole", font=("Arial", 27), background='#FFFFFF', fg='black')
label_title.pack()

label_subtitle = Label(frame_1, text="Bienvenue sur le générateur de Qr Code, choisissez une option : ", font=("Arial", 15), bg='#FFFFFF', fg='black')
label_subtitle.pack()

#affichage de la frame
frame_1.pack()

#bouton qui passe à la page suivante 
bouton_1 = Button(text="Générer un QR Code", font=("Arial"), bg ='#FFFFFF', fg='black')
bouton_1.pack()

#affichage de la fenetre 
window.mainloop()
