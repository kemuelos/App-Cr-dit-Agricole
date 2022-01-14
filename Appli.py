from cProfile import label
import tkinter as tk 
from tkinter import * 
from tkinter import font
from tkinter.tix import COLUMN
from turtle import left, right
from webbrowser import get 
import qrcode
from PIL import Image

    

#fonction QR évenementiel
def QR_code():
    lien = champ_lien.get()
    logo_link = 'ca_guadeloupe.png'

    logo = Image.open(logo_link)

    basewidth = 100

    wpercent = (basewidth/float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
    QRcode = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )

    url = lien 

    QRcode.add_data(url)
    QRcode.make()


    QRimg = QRcode.make_image(fill_color='#006C50', back_color="white").convert('RGB')

    pos = ((QRimg.size[0] - logo.size[0]) // 2,
           (QRimg.size[1] - logo.size[1]) // 2)
    QRimg.paste(logo, pos)

    QRimg.save('code.jpeg')
    champ_lien.delete(0,"end")    
    


def supp():
    champ_lien.delete(0, END)

#fonction pour passer à la page suivante
def page_2():
    frame_1.pack_forget()
    frame_2.pack()

def page_3():
    frame_1.pack_forget()
    frame_3.pack()
    

#revenir à la page précédente     
def page_2to1():
    frame_2.pack_forget()
    frame_1.pack()

def page_3to1():
    frame_3.pack_forget()
    frame_1.pack()



            


#crer fenetre
window = Tk()
window.title("Qr Generateur")
window.geometry("1200x800")
window.minsize(480, 360)
window.config(background="#FFFFFF")
window.iconbitmap("ca.ico")

#banderole 
photo = PhotoImage(file='ca_banderole.png')
label = Label(window, image=photo)    
label.pack()
 

#creer frame (boite)
frame_1 = Frame(window, background="#FFFFFF")
frame_2 = Frame(window,background="#FFFFFF")
frame_3 = Frame(window,background="#FFFFFF")


#affichage de la frame
frame_1.pack()



#creer les widgets (contenus dans la frame 1)
label_title = Label(frame_1, text="Générateur de QR Code", font=("Arial", 27), background='#FFFFFF', fg='black')
label_title.pack()

label_subtitle = Label(frame_1, text="Bienvenue sur le générateur de Qr Code, choisissez une option : ", font=("Arial", 15), bg='#FFFFFF', fg='black')
label_subtitle.pack()




#boutons frame 1
bouton_1 = Button(frame_1, text="Générer un QR Code de contact", font=("Arial"), bg ='#006C50', fg='white', command=page_2)
bouton_1.pack()

bouton_2 = Button(frame_1, text="Générer un QR Code événementiel", font=("Arial"), bg ='#006C50', fg='white', command=page_3)
bouton_2.pack()

bouton_2 = Button(frame_1, text="Quitter", font=("Arial"), bg ='#ED1C24', fg='white', command=window.quit)
bouton_2.pack()



#boutons frame 2
txt_nom = Label(frame_2, text="Nom", font=("Arial"), bg="#FFFFFF", fg="black")
txt_nom.place(x=1000, y=220)
txt_nom.pack()

# txt_prenom = Label(frame_2, text="Prénom", font=("Arial"), bg="#FFFFFF", fg="black")
# txt_prenom.pack()

# txt_agence = Label(frame_2, text="Agence", font=("Arial"), bg="#FFFFFF", fg="black")
# txt_agence.pack()



bouton_5 = Button(frame_2, text="Retour", font=("Arial"), bg ='#ED1C24', fg='white', command=page_2to1)
bouton_5.pack()



#boutons frame 3
txt_lien = Label(frame_3, text="Entrez le lien  : ", font=("Arial"), bg ='#006C50', fg='black')
champ_lien = Entry(frame_3)
txt_lien.pack()
champ_lien.pack()




bouton_6 = Button(frame_3, text="Valider", font=("Arial"), bg ='#006C50', fg='black', command= QR_code)
bouton_6.pack()




bouton_7 = Button(frame_3, text="Retour", font=("Arial"), bg ='#ED1C24', fg='black', command=page_3to1)
bouton_7.pack()





#affichage de la fenetre 
window.mainloop()
