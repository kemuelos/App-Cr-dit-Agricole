import tkinter as tk 
from tkinter import * 
from tkinter import font 

#fonction pour passer à la page 2
def page_2():
    frame_1.pack_forget()
    frame_2.pack()


def retour_page_1():
    frame_2.pack_forget()
    frame_1.pack()


#crer fenetre
window = Tk()
window.title("Qr Generateur")
window.geometry("1080x720")
window.minsize(480, 360)
window.config(background="#1BB221")
window.iconbitmap("ca.ico")


#creer frame (boite)
frame_1 = Frame(window, background="#1BB221")
frame_2 = Frame(window,background="#1BB221")



#affichage de la frame
frame_1.pack()



#creer les widgets (contenus dans la frame 1)
label_title = Label(frame_1, text="Générateur de QR Code du crédit agricole", font=("Arial", 27), background='#1BB221', fg='white')
label_title.pack()

label_subtitle = Label(frame_1, text="Bienvenue sur le générateur de Qr Code, choisissez une option : ", font=("Arial", 15), bg='#1BB221', fg='white')
label_subtitle.pack()




#boutons
bouton_1 = Button(frame_1, text="Générer un QR Code", font=("Arial"), bg ='#FFFFFF', fg='black', command=page_2)
bouton_1.pack()

bouton_2 = Button(frame_2, text="Générer un Qr code pour un agent", font=("Arial"), bg ='#FFFFFF', fg='black')
bouton_2.pack()

bouton_3 = Button(frame_2, text="Générer un Qr code en sélectionnant une agence", font=("Arial"), bg ='#FFFFFF', fg='black')
bouton_3.pack()

bouton_4 = Button(frame_2, text="Retour", font=("Arial"), bg ='#FFFFFF', fg='black', command=retour_page_1)
bouton_4.pack()


#affichage de la fenetre 
window.mainloop()
