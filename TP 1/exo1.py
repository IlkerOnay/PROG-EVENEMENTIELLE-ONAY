from tkinter import *
 ###############################################################################################
#                       DERNIERE MODIFICATION 11/11/2022 à 1h29                               #
#      COPYRIGHT : ONAY ILKER RT2 A1 de groupe sanguin B+ (c'est une blague)                  #
#                                                                                             #
#                                TP PROG EVENMENTIELLE                                        #
#                                                                                             #
###############################################################################################



def plus ():                            #//// Fonction ajout
    nbr.set(nbr.get() + 1)              #//// Permet de récupérer la valeur et de +1 
    v= 'Valeur ' + str(nbr.get())       #//// Variable v devient une phrase "Valeur " + la nouvelle valeur de nbr
    label['text'] = v                   #//// Réatribution d'un nouveau texte "v" au label

def moins ():                           #//// Fonction retirer
    nbr.set(nbr.get() - 1)              #//// Permet de récupérer la valeur et de -1 
    v= 'Valeur ' + str(nbr.get())       #//// Variable v devient une phrase "Valeur " + la nouvelle valeur de nbr
    label['text'] = v                   #//// Réatribution d'un nouveau texte "v" au label

fenetre= Tk()
 
nbr = IntVar()
  
bouton1 = Button(fenetre,text='+', command=plus)        #//// Button qui permet d'apeller dessus la commande (fonction) nommée plus
bouton1.pack()

bouton2 = Button(fenetre,text='-', command=moins)       #//// Button qui permet d'apeller dessus la commande (fonction) nommée moin
bouton2.pack()

label =Label(fenetre, text='Valeur 0')                  #//// Création du label initial
label.pack()
 
fenetre.mainloop()