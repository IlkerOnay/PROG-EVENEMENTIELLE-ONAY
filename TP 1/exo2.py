from tkinter import *

###############################################################################################
#                       DERNIERE MODIFICATION 11/11/2022 à 1h29                               #
#      COPYRIGHT : ONAY ILKER RT2 A1 de groupe sanguin B+ (c'est une blague)                  #
#                                                                                             #
#                                TP PROG EVENMENTIELLE                                        #
#                                       BON JEUX                                              #
###############################################################################################


#//// fonction validation du mail
def Valider():
    print( "Votre Email :" + mail.get()) 
    gui.destroy()

    
# /// création gui
gui = Tk()


# //// Création du boutton et du label state= disabled pour désactiver un boutton
varmail = StringVar()
label = Label(text="Veuillez entrer votre Email:")
label.pack()
mail = Entry(textvariable=varmail )
mail.focus_set()         #//// Permet de lancer une saissie directe
mail.pack()
        
button = Button(text="Valider", command=Valider,state=DISABLED)
button.pack()

# //// optionel taille et titre
gui.geometry( "300x80" )
gui.title( "Email check" )
        





#//// Fonction pour check 

def check(key):
    # //////////// MES FLAGS DE VERIFICATIONS POUR LE @ ;" " ; .
    flag_a= 0
    flag_point=0
    flag_espace=1
    texte = mail.get()
    if "@" in texte :
        flag_a = 1
    if "." in texte:
        flag_point = 1
    if " " in texte :
        flag_espace = 0    
    if flag_a == 1 and flag_point == 1 and flag_espace == 1 :   
         button.configure(state=NORMAL)
    if flag_a == 0 or flag_point ==0 or flag_espace == 0 :
        button.configure(state=DISABLED)


gui.bind("<Key>", check)
gui.mainloop()
