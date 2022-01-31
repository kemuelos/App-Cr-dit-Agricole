from ast import Return
from cProfile import label
from cgitb import text
from dataclasses import fields
import email
from fileinput import filename
from heapq import heappush
from os import sep
from re import A
from select import select
from sqlite3 import Row
from textwrap import fill
import tkinter as tk 
from tkinter import * 
from tkinter import font
from turtle import bgcolor, heading, left, right, width
from webbrowser import get
from matplotlib import lines
from matplotlib.pyplot import title
from numpy import left_shift, pad, place
from pyparsing import line 
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
from tkinter import filedialog


    

#fonction QR évenementiel
def QR_code():
    lien = champ_lien.get()
    logo_link = 'ca_guadeloupe.png'
    logo = Image.open(logo_link)
    E = champ_E.get()
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
    champ_E.delete(0, "end")   
    


#fonction pour passer à la page suivante

def page_ouvrir():
    frame_open.place(x=200, y=100, width= 800, height=550)
    frame_1.pack_forget()
    frame_quitter.pack_forget()

def page_ouvrir_to1():
    frame_open.place_forget()
    frame_1.pack()
    frame_quitter.pack()


def page_2():
    frame_open.place_forget()
    frame_2.pack()
    frame_csv.pack()
    frame_4.pack()
    

def page_3():
    frame_1.pack_forget()
    frame_quitter.pack_forget()
    frame_3.place(x=200, y=100, width= 800, height=550)
    

#revenir à la page précédente     
def page_2to1():
    frame_2.pack_forget()
    frame_4.pack_forget()
    frame_csv.pack_forget()
    frame_1.pack()
    frame_quitter.pack()
    
    

def page_3to1():
    frame_3.place_forget()
    frame_1.pack()
    frame_quitter.pack()


def page_4():
    frame_1.pack_forget()
    frame_quitter.pack_forget()
    frame_5.pack()
    frame_5.place(x=200, y=100, width= 800, height=550)


def page_4to1():
    frame_5.pack_forget()
    frame_5.place_forget()
    frame_1.pack()
    frame_quitter.pack()


  
    


def QR_auto():
    line = tab_info.item(tab_info.selection())
    Nom = line['values'][1] +' ' + line['values'][2]
    Email = line['values'][6]
    

    
    qr_auto = helpers.make_mecard(name = Nom, email= Email)
    qr_auto.designator
    qr_auto.save(Nom + '_qrcode_auto.png', scale=4, data_dark='#006C50', dark='#006C50')
    


def QR_manuel():
    name_info = champ_NOM.get() + ' ' + champ_PRENOM.get()
    mail1_info = champ_MAIL.get()
    mail2_info = champ_MAIL_2.get()
    numero1_info = champ_NUMERO.get()
    numero2_info = champ_NUMERO_2.get()
    fax_info = champ_FAX.get()
    adresse_info = champ_ADRESSE.get()
    localisation_info = champ_LATITUDE.get() + ' ' + champ_LONGITUDE.get()
    
    qr_manu =  helpers.make_vcard(name = name_info, displayname=name_info, email=(mail1_info, mail2_info), phone=(numero1_info, numero2_info),
                                  fax=fax_info, street=adresse_info, pobox=localisation_info , url='https://www.credit-agricole.fr/ca-guadeloupe/particulier.html', org='Crédit Agricole')
    qr_manu.designator
    qr_manu.save(name_info + '_qrcode_manuel.png', scale=4, data_dark='#006C50', dark='#006C50')
    
    
    champ_NOM.delete(0,"end")
    champ_PRENOM.delete(0,"end")  
    champ_MAIL.delete(0,"end")
    champ_MAIL_2.delete(0,"end")
    champ_NUMERO.delete(0,"end")
    champ_NUMERO_2.delete(0,"end")
    champ_FAX.delete(0, "end")
    champ_ADRESSE.delete(0,"end")
    champ_LATITUDE.delete(0, "end")
    champ_LONGITUDE.delete(0, "end")
    


    

def search():
    dict_info = {}
    id_search = champ_id.get()
    nom_search = champ_nom.get()
    prenom_search = champ_prenom.get()
    tab_info.delete(*tab_info.get_children())
    
    if len(id_search)!=0:
        for key in dict_info:
            if dict_info[key]["login"]==id_search:
                employe_search = dict_info[key]
                break
    
    elif len(nom_search)!=0 and len(prenom_search) != 0:
        employe_search = dict_info["-".join([nom_search, prenom_search])]
    
    print(employe_search)    
    
    tab_info.insert("", 0, values=(employe_search["login"],employe_search["name"],employe_search["firstname"],employe_search["eds"],employe_search["service"],employe_search["domaine"],employe_search["mail"])) 
    bouton_9.pack(padx=10, pady=15, side=LEFT)
 

def annuler_search():
    dict_info = {}
    bouton_9.pack_forget()
    afficher(dict_info, tab_info)
    

  


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
frame_3 = Frame(window,background="#D6D6D6")
frame_4 = Frame(window,background="#FFFFFF")
frame_5 = Frame(window,background="#D6D6D6")
frame_open = Frame(window, background="#D6D6D6")
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



def dialog_box():
    file = filedialog.askopenfilename()
    champ_source.insert(0, file)

    dict_info = {}
    title = ["login", "name", "firstname", "eds", "service", "domaine", "mail"]
    with open(file, newline='') as f:
        reader = csv.reader(f, delimiter = ' ')
        next(reader)
        for row in reader:
            tmp = row[0].split(';')
            if len(tmp)==1:
                tmp = row[0].split(',')
            if len(tmp)==7:
                employe = {}
                for i in range (7):
                    employe[title[i]] = tmp[i]
                dict_info['-'.join([tmp[1], tmp[2]])] = employe
                tab_info.insert("", 0, values=(employe["login"],employe["name"],employe["firstname"],employe["eds"],employe["service"],employe["domaine"],employe["mail"]))       


def afficher(dict_info, tab_info):
    for key in dict_info:
        tab_info.insert("", 0, values=(dict_info[key]["login"],dict_info[key]["name"],dict_info[key]["firstname"],dict_info[key]["eds"],dict_info[key]["service"],dict_info[key]["domaine"],dict_info[key]["mail"]))       
       


#affichage de la frame
frame_1.pack()
frame_quitter.pack()


#creer les widgets (contenus dans la frame 1)
label_title = Label(frame_1, text="Générateur de QR Code", font=("Arial", 27), background='#FFFFFF', fg='black')
label_title.pack()

label_subtitle = Label(frame_1, text="Bienvenue sur le générateur de Qr Code, choisissez une option : ", font=("Arial", 15), bg='#FFFFFF', fg='black')
label_subtitle.pack()




#boutons frame 1
bouton_1 = Button(frame_1, text="Générer un QR Code de contact   ", font=("Arial"), bg ='#006C50', fg='white', command=page_ouvrir)
bouton_1.pack(padx=10, pady=15, ipadx=20, ipady=30)

bouton_4 =Button(frame_1, text="Générer un QR Code par formulaire", font=("Arial"), bg='#006C50', fg='white', command=page_4)
bouton_4.pack(padx=10, pady=30,  ipadx=20, ipady=30)

bouton_2 = Button(frame_1, text="Générer un QR Code événementiel", font=("Arial"), bg ='#006C50', fg='white', command=page_3)
bouton_2.pack(padx=10, pady=40,  ipadx=20, ipady=30)



bouton_3 = Button(frame_quitter, text="Quitter", font=("Arial"), bg ='#ED1C24', fg='white', command=window.quit)
bouton_3.pack(ipadx=10, ipady=10)


#frame ouvrir fichier
champ_source = Entry(frame_open)
champ_source.pack()

bouton_ouvrir = Button(frame_open, text="Ouvrir fichier", font=("Arial"), bg ='#006C50', fg='white', command=dialog_box)
bouton_ouvrir.pack(side=BOTTOM)

bouton_continuer = Button(frame_open, text="Continuer", font=("Arial"), bg ='#006C50', fg='white', command=page_2)
bouton_continuer.pack(side=BOTTOM)

bouton_retour_2 = Button(frame_open, text="Retour menu", font=("Arial"), bg ='#ED1C24', fg='white', command=page_ouvrir_to1)
bouton_retour_2.pack(side=BOTTOM)



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

bouton_8 = Button(frame_2, text="Recherche", font=("Arial"), bg='#2BA640', fg='white', command=search)
bouton_8.pack(padx=10, pady=15, side=LEFT)

bouton_9 = Button(frame_2, text="Annuler", font=("Arial"), bg='#2BA640', fg='white', command=annuler_search)



# frame 4
bouton_5 = Button(frame_4, text="Retour", font=("Arial"), bg ='#ED1C24', fg='white', command=page_2to1)
bouton_5.pack(side=RIGHT)

bouton_creer = Button(frame_4, text="Creer", font=("Arial"), bg='#2BA640', fg='white', command=QR_auto)
bouton_creer.pack(side=LEFT)


# frame 3
txt_lien = Label(frame_3, text="Entrez le lien  : ", font=("Arial", 15), bg ='#D6D6D6', fg='black').place(x=340, y=100)
champ_lien = Entry(frame_3)
champ_lien.place(x=250, y=150, width=300)

txt_E = Label(frame_3, text="Entrez le nom de l'évènement : ", font=("Arial", 15), bg ='#D6D6D6', fg='black').place(x=290, y=200)
champ_E = Entry(frame_3)
champ_E.place(x=250, y=250, width=300)

bouton_6 = Button(frame_3, text="Valider", font=("Arial"), bg ='#006C50', fg='white', command= QR_code).place(x=250, y=350, width=100, height=50)

bouton_7 = Button(frame_3, text="Retour", font=("Arial"), bg ='#ED1C24', fg='white', command=page_3to1).place(x=450, y=350, width=100, height=50)




# frame 5

txt_titre = Label(frame_5, text="Entrez vos coordonnées pour générer un QR Code  :", font=("Arial", 20), bg="#D6D6D6", fg="black").place(x=50, y=30)

txt_nom = Label(frame_5, text="Nom", font=("Arial"), bg="#D6D6D6", fg="black").place(x=50, y=90)
champ_NOM = Entry(frame_5)
champ_NOM.place(x= 180, y=90)

txt_prenom = Label(frame_5, text="Prénom", font=("Arial"), bg="#D6D6D6", fg="black").place(x=50, y=140)
champ_PRENOM = Entry(frame_5)
champ_PRENOM.place(x=180, y=140)

txt_mail = Label(frame_5, text="Mail", font=("Arial"), bg="#D6D6D6", fg="black").place(x=50, y=190)
champ_MAIL = Entry(frame_5)
champ_MAIL.place(x=180, y=190)

txt_mail_2 = Label(frame_5, text="second Mail", font=("Arial"), bg="#D6D6D6", fg="black").place(x=50, y= 240)
champ_MAIL_2 = Entry(frame_5)
champ_MAIL_2.place(x=180, y=240)

txt_numero = Label(frame_5, text="Numéro", font=("Arial"), bg="#D6D6D6", fg="black").place(x=50, y=290)
champ_NUMERO = Entry(frame_5)
champ_NUMERO.place(x=180, y=290)

txt_numero_2 = Label(frame_5, text="Second numéro", font=("Arial"), bg="#D6D6D6", fg="black").place(x=50, y=340)
champ_NUMERO_2 = Entry(frame_5)
champ_NUMERO_2.place(x=180, y=340)

txt_fax = Label(frame_5, text="FAX", font=("Arial"), bg="#D6D6D6", fg="black").place(x=480, y=90)
champ_FAX = Entry(frame_5)
champ_FAX.place(x=600, y=90)

txt_adresse = Label(frame_5, text="Adresse", font=("Arial"), bg="#D6D6D6", fg="black").place(x=480, y=140)
champ_ADRESSE = Entry(frame_5)
champ_ADRESSE.place(x=600, y=140)

txt_localisation = Label(frame_5, text="Localisation  :", font=("Arial"), bg="#D6D6D6", fg="black").place(x=480, y=190)
txt_latitude = Label(frame_5, text="Latitude", font=("Arial"), bg="#D6D6D6", fg="black").place(x=480, y=230)
champ_LATITUDE = Entry(frame_5)
champ_LATITUDE.place(x=600, y=230)
txt_longitude = Label(frame_5, text="Longitude", font=("Arial"), bg="#D6D6D6", fg="black").place(x=480, y=280)
champ_LONGITUDE = Entry(frame_5)
champ_LONGITUDE.place(x=600, y=280)

bouton_creer2 = Button(frame_5, text="Creer", font=("Arial"), bg='#2BA640', fg='white', command=QR_manuel).place(x=400, y=400, width=100, height=50)

bouton_7 = Button(frame_5, text="Retour", font=("Arial"), bg ='#ED1C24', fg='white', command=page_4to1).place(x=550, y=400, width=100, height=50)




#affichage de la fenetre 
window.mainloop()
