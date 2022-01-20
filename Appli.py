from ast import Return
from cProfile import label
from cgitb import text
import email
from heapq import heappush
from os import sep
from re import A
from select import select
from sqlite3 import Row
from textwrap import fill
import tkinter as tk 
from tkinter import * 
from tkinter import font
from turtle import bgcolor, heading, left, right
from webbrowser import get 
import qrcode
from PIL import Image
import csv
import tkinter
import tkinter as ttk
from tkinter import ttk
import pandas as pd
import vobject
import segno
from segno import helpers
import io



    

#fonction QR évenementiel
def QR_code():
    lien = champ_lien.get()
    logo_link = 'ca_guadeloupe.png'
    E = champ_E.get()
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

    QRimg.save('qr_' + E +'.jpeg')
    champ_lien.delete(0,"end")    
    


#fonction pour passer à la page suivante
def page_2():
    frame_1.pack_forget()
    frame_quitter.pack_forget()
    frame_2.pack()
    frame_csv.pack()
    frame_4.pack()
    

def page_3():
    frame_1.pack_forget()
    frame_quitter.pack_forget()
    frame_3.pack()
    

#revenir à la page précédente     
def page_2to1():
    frame_2.pack_forget()
    frame_4.pack_forget()
    frame_csv.pack_forget()
    frame_1.pack()
    frame_quitter.pack()
    
    

def page_3to1():
    frame_3.pack_forget()
    frame_1.pack()
    frame_quitter.pack()


def page_4():
    frame_1.pack_forget()
    frame_quitter.pack_forget()
    frame_5.pack()


def page_4to1():
    frame_5.pack_forget()
    frame_1.pack()
    frame_quitter.pack()


def QR_auto():
    line = tab_info.item(tab_info.selection())
    item = tab_info.selection()[0]
    # print(tab_info.item(item)['values'])
    # print(line['values'][1])
    Nom = line['values'][1] +' ' + line['values'][2]
    Email = line['values'][6]
    

    
    qr_auto = helpers.make_mecard(name = Nom, email= Email)
    qr_auto.designator
    qr_auto.save(Nom + '_qrcode_auto.png', scale=4, data_dark='#006C50', dark='#006C50')
    


def QR_manu():
    name2 = champ_NOM.get() + ' ' + champ_PRENOM.get()
    mail2 = champ_MAIL.get()
    
    qr_manu =  helpers.make_mecard(name = name2, email= mail2)
    qr_manu.designator
    qr_manu.save(name2 + '_qrcode_manuel.png', scale=4, data_dark='#006C50', dark='#006C50')
    
    
    champ_NOM.delete(0,"end")
    champ_PRENOM.delete(0,"end")  
    champ_MAIL.delete(0,"end") 
    



    


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
frame_2 = Frame(window,background="#006C50")
frame_3 = Frame(window,background="#FFFFFF")
frame_4 = Frame(window,background="#FFFFFF")
frame_5 = Frame(window,background="#FFFFFF")
frame_quitter = Frame(window,background="#FFFFFF")



#frame qui affiche le csv
frame_csv = Frame(window, bd=3,relief= GROOVE, bg="#FFFFFF", width=1080, height=550)
frame_csv.pack_propagate(False)


#Tableau qui stock le csv

scroll_y = Scrollbar(frame_csv, orient=VERTICAL)
tab_info = ttk.Treeview(frame_csv, columns=("id" , "nom", "prenom", "eds", "service", "domaine", "mail"), yscrollcommand=scroll_y.set)
scroll_y.config(command=tab_info.yview)
scroll_y.pack(side=RIGHT, fill=Y)


tab_info.heading("id", text="Login")
tab_info.heading("nom", text="Nom")
tab_info.heading("prenom", text="Prenom")
tab_info.heading("eds", text="EDS")
tab_info.heading("service", text="Service/Agence")
tab_info.heading("domaine", text="Domaine/Metier")
tab_info.heading("mail", text="Mail")

tab_info.column("#0", minwidth=0,width=0)
tab_info.column('#1', width=100) #id
tab_info.column('#2', minwidth=0,width=120) #nom
tab_info.column('#3', minwidth=0,width=100) #prenom
tab_info.column('#4', minwidth=0,width=100) #eds
tab_info.column('#5', minwidth=0,width=150) #service
tab_info.column('#6', minwidth=0,width=150) #domaine
tab_info.column('#7', minwidth=0,width=320) #mail
tab_info.pack(expand=YES, fill=BOTH)
tab_info.bind("<ButtonRelease-1>")


with open('base.csv') as f:
    reader = csv.DictReader(f, delimiter = ';')
    for row in reader:
        login = row['Login']
        name = row['Nom']
        firstname = row['Prenom']
        eds = row['EDS']
        service = row['SERVICE/AGENCE']
        domaine = row['Domaine_metier']
        mail = row['Mail']
        tab_info.insert("", 0, values=(login, name, firstname, eds, service, domaine, mail))








#affichage de la frame
frame_1.pack()
frame_quitter.pack()



#creer les widgets (contenus dans la frame 1)
label_title = Label(frame_1, text="Générateur de QR Code", font=("Arial", 27), background='#FFFFFF', fg='black')
label_title.pack()

label_subtitle = Label(frame_1, text="Bienvenue sur le générateur de Qr Code, choisissez une option : ", font=("Arial", 15), bg='#FFFFFF', fg='black')
label_subtitle.pack()




#boutons frame 1
bouton_1 = Button(frame_1, text="Générer un QR Code de contact", font=("Arial"), bg ='#006C50', fg='white', command=page_2)
bouton_1.pack()

bouton_4 =Button(frame_1, text="Générer un QR code contact manuellement", font=("Arial"), bg='#006C50', fg='white', command=page_4)
bouton_4.pack()

bouton_2 = Button(frame_1, text="Générer un QR Code événementiel", font=("Arial"), bg ='#006C50', fg='white', command=page_3)
bouton_2.pack()



bouton_3 = Button(frame_quitter, text="Quitter", font=("Arial"), bg ='#ED1C24', fg='white', command=window.quit)
bouton_3.pack()



#boutons frame 2
txt_id= Label(frame_2, text="Id", font=("Arial"), bg="#FFFFFF", fg="black")
txt_id.pack(padx=5, pady=15, side=LEFT)
champ_id= Entry(frame_2)
champ_id.pack(padx= 10, pady=15, side=LEFT)

txt_nom = Label(frame_2, text="Nom", font=("Arial"), bg="#FFFFFF", fg="black")
txt_nom.pack(padx=5, pady=15, side=LEFT)
champ_nom = Entry(frame_2)
champ_nom.pack(padx= 10, pady=15, side=LEFT)

txt_prenom = Label(frame_2, text="Prénom", font=("Arial"), bg="#FFFFFF", fg="black")
txt_prenom.pack(padx=5, pady=15, side=LEFT)
champ_prenom = Entry(frame_2)
champ_prenom.pack(padx=10, pady=15, side=LEFT)


txt_agence = Label(frame_2, text="Agence", font=("Arial"), bg="#FFFFFF", fg="black")
txt_agence.pack(padx=5, pady=15, side=LEFT)
champ_agence = Entry(frame_2)
champ_agence.pack(padx= 10, pady= 15, side=LEFT)

txt_poste = Label(frame_2, text="Poste", font=("Arial"), bg="#FFFFFF", fg="black")
txt_poste.pack(padx= 5, pady= 15, side=LEFT)
champ_poste = Entry(frame_2)
champ_poste.pack(padx=10, pady= 15, side=LEFT)

bouton_8 = Button(frame_2, text="Recherche", font=("Arial"), bg='#2BA640', fg='white')
bouton_8.pack(padx=10, pady=15, side=LEFT)



# frame 4
bouton_5 = Button(frame_4, text="Retour", font=("Arial"), bg ='#ED1C24', fg='white', command=page_2to1)
bouton_5.pack(side=RIGHT)

bouton_creer = Button(frame_4, text="Creer", font=("Arial"), bg='#2BA640', fg='white', command=QR_auto)
bouton_creer.pack(side=LEFT)




# frame 3
txt_lien = Label(frame_3, text="Entrez le lien  : ", font=("Arial"), bg ='#006C50', fg='white')
champ_lien = Entry(frame_3)
txt_lien.pack()
champ_lien.pack()

txt_E = Label(frame_3, text="Entrez le nom de l'évènement : ", font=("Arial"), bg ='#006C50', fg='white')
champ_E = Entry(frame_3)
txt_E.pack()
champ_E.pack()


bouton_6 = Button(frame_3, text="Valider", font=("Arial"), bg ='#006C50', fg='white', command= QR_code)
bouton_6.pack()


bouton_7 = Button(frame_3, text="Retour", font=("Arial"), bg ='#ED1C24', fg='white', command=page_3to1)
bouton_7.pack()



# frame 5
txt_nom = Label(frame_5, text="NOM", font=("Arial"), bg="#FFFFFF", fg="black")
txt_nom.pack()
champ_NOM = Entry(frame_5)
champ_NOM.pack()

txt_prenom = Label(frame_5, text="PRENOM", font=("Arial"), bg="#FFFFFF", fg="black")
txt_prenom.pack()
champ_PRENOM = Entry(frame_5)
champ_PRENOM.pack()

txt_mail = Label(frame_5, text="MAIL", font=("Arial"), bg="#FFFFFF", fg="black")
txt_mail.pack()
champ_MAIL = Entry(frame_5)
champ_MAIL.pack()

bouton_creer2 = Button(frame_5, text="Creer", font=("Arial"), bg='#2BA640', fg='white', command=QR_manu)
bouton_creer2.pack()


bouton_7 = Button(frame_5, text="Retour", font=("Arial"), bg ='#ED1C24', fg='white', command=page_4to1)
bouton_7.pack()


#affichage de la fenetre 
window.mainloop()
