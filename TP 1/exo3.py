###############################################################################################
#                       DERNIERE MODIFICATION 11/11/2022 à 1h29                               #
#      COPYRIGHT : ONAY ILKER RT2 A1 de groupe sanguin B+ (c'est une blague)                  #
#                                                                                             #
#                                TP PROG EVENMENTIELLE                                        #
#                                       BON JEUX                                              #
###############################################################################################


# import variable global resized de l'image 
from tkinter import *
from PIL import Image,ImageTk

erreur=0
espace = ", "
gui = Tk()
gui.title("Eight Queen")
pion_encours=[]
nbrdepion=0
img=(Image.open("TP 1/dame.png"))
resized_image= img.resize((60,65))
new_image= ImageTk.PhotoImage(resized_image)




###############################################################################################
#         FONCTION QUI ANNONCE LA DEFAITE (vous le verez pas si vous êtes fort au jeu)        #
###############################################################################################

def perdu():
    gui.destroy()
    gui_loose = Tk()
    label= Label(gui_loose,text="Vous avez perdu ! :(",bg="red",width=50,height=25).pack()

###############################################################################################


###############################################################################################
#         FONCTION QUI ANNONCE LA VICTOIRE (POUR LES PGM)                                     #
###############################################################################################

def victoire():
    gui.destroy()
    gui_victoire = Tk()
    label= Label(gui_victoire,text="Vous avez gagné !!!!!!!!! :)",bg="green",width=50,height=25).pack()

###############################################################################################




###############################################################################################
#               FONCTION ET BIND POUR QUITTER LORS DE L'APPUIE SUR LA TOUCHE ECHAP            #
###############################################################################################

def destroy(event):
    gui.destroy()

gui.bind("<Escape>",destroy)                #//// touche échap pour quitter

###############################################################################################



###############################################################################################
#               FONCTION POUR AFFICHER LE DAMIER EN CREANT LES CANVAS                         #
###############################################################################################

def damier_un():
    largeur,hauteur= 75,75
    num=[1,2,3,4,5,6,7,8]
    numb=[2,4,6,8]
    for i in range(len(num)):
        for j in range(len(numb)):
            if (i % 2) == 0 :
                color = "black"
            else:
                color= "white"
            canvas= Canvas(gui, bg=[color],width=largeur,height=hauteur,border=False).grid(row=numb[j],column=num[i])

def damier_deux():
    largeur,hauteur= 75,75
    num=[1,2,3,4,5,6,7,8]
    numb=[1,3,5,7]
    for i in range(len(num)):
        for j in range(len(numb)):
            if (i % 2) == 0 :
                color = "white"
            else:   
                color= "black"
            canvas= Canvas(gui, bg=[color],width=largeur,height=hauteur).grid(row=numb[j],column=num[i])

###############################################################################################



###############################################################################################
#                               FONCTION PRINCIPAL                                            #
#      IL PERMETS DE CAPTER SI UN PION A DEJA ETAIT POSER LA OU L'ON CLIQUE                   #
#  PERMET DE METTRE 8 PION MAX, PERMET DE SAVOIR SI LA COULEUR DOIT ETRE NOIR OU BLANC        #
#                                DERRIERE L'IMAGE                                             #
#                  VERIFIER LES DIAGONALES, LE VERTICALE ET LE HORIZONTALE DE CHAQUE PION     #
#                           D'ANNONCER VICTOIRE OU DEFAITE                                    #
###############################################################################################

def pion(event):
    global pion_encours,nbrdepion,erreur,pion
    x = event.x_root - gui.winfo_rootx()            #permet d'avoir les coordonnées
    y = event.y_root - gui.winfo_rooty()             
    z= gui.grid_location(y,x)                       
    x_new,y_new= str(z),str(z)                                
    x_new=int(x_new[1:2])                           # int row
    y_new=int(y_new[4:5])                           #int column
    #print("x_new =", x_new,"       y_new = ", y_new)
    tks=Canvas(gui,bg="black",width=75,height=75)       #couleur par défaut derrière la dame = noir
    for i in range(1,9):                                #permet de savoir si la case est blanche si oui derrière la dame la couleur sera blanc aussi
        if x_new % 2 == 0:
            if x_new == i and y_new == 2 or x_new == i and y_new == 4 or x_new == i and y_new == 6 or x_new == i and y_new == 8:
                tks=Canvas(gui,bg="white",width=75,height=75)
    for i in range(1,9):                     
        if x_new % 2 == 1:
            if x_new == i and y_new == 1 or x_new == i and y_new == 3 or x_new == i and y_new == 5 or x_new == i and y_new == 7:
                tks=Canvas(gui,bg="white",width=75,height=75)
    z=str(z)
    z=str(z[1:5])
    pion=len(pion_encours)
    if pion < 8 :                                   #PERMET DE SAVOIR SI LE PION ( dame ) a déjà était jouer a ces coordonnées
        if z in pion_encours:
            return
        else:                                       # si il n'a pas été jouer alors on le place
            tks.grid(row=x_new,column=y_new)
            nbrdepion+=1
            tks.create_image(10,10,anchor=NW,image=new_image)
            pion_encours.append(z)
    #############################
    # Diagonale bas gauche      #
    #############################
    for check in range(pion):
        for value in range(1,9):
            flag =0
            check_upx = pion_encours[check]
            check_upx = check_upx[:1]
            check_upx = int(check_upx) + value
            check_upy = pion_encours[check]
            check_upy = check_upy[3:4]
            check_upy = int(check_upy) - value
            check_up= str(check_upx) + espace + str(check_upy)
            if  pion_encours[check] == check_up :
                flag=-1
            if check_up in pion_encours :
                flag = flag +1
            if flag == 1:
                tks=Canvas(gui,bg="red",width=75,height=75)
                tks.grid(row=x_new,column=y_new)
                erreur+=1
                pion_encours.pop()
    #############################
    # Diagonale haut droite     #
    #############################
    for check in range(pion):
        for value in range(1,9):
            flag =0
            check_upx = pion_encours[check]
            check_upx = check_upx[:1]
            check_upx = int(check_upx) - value
            check_upy = pion_encours[check]
            check_upy = check_upy[3:4]
            check_upy = int(check_upy) + value
            check_up= str(check_upx) + espace + str(check_upy)
            if  pion_encours[check] == check_up :
                flag=-1
            if check_up in pion_encours :
                flag = flag +1
            if flag == 1:
                tks=Canvas(gui,bg="red",width=75,height=75)
                tks.grid(row=x_new,column=y_new)
                erreur +=1
                pion_encours.pop()
    #############################
    # Diagonale bas droite      #
    #############################
    for check in range(pion):
        for value in range(1,9):
            flag =0
            check_upx = pion_encours[check]
            check_upx = check_upx[:1]
            check_upx = int(check_upx) + value
            check_upy = pion_encours[check]
            check_upy = check_upy[3:4]
            check_upy = int(check_upy) + value
            check_up= str(check_upx) + espace + str(check_upy)
            if  pion_encours[check] == check_up :
                flag=-1
            if check_up in pion_encours :
                flag = flag +1
            if flag == 1:
                tks=Canvas(gui,bg="red",width=75,height=75)
                tks.grid(row=x_new,column=y_new)
                erreur +=1
                pion_encours.pop()
    #############################
    # Diagonale haut gauche     #
    #############################

    for check in range(pion):
        for value in range(1,9):
            flag =0
            check_upx = pion_encours[check]
            check_upx = check_upx[:1]
            check_upx = int(check_upx) - value
            check_upy = pion_encours[check]
            check_upy = check_upy[3:4]
            check_upy = int(check_upy) - value
            check_up= str(check_upx) + espace + str(check_upy)
            if  pion_encours[check] == check_up :
                flag=-1
            if check_up in pion_encours :
                flag = flag +1
            if flag == 1:
                tks=Canvas(gui,bg="red",width=75,height=75)
                tks.grid(row=x_new,column=y_new)
                erreur +=1
                pion_encours.pop()
    #############################
    # DE DROITE A GAUCHE        #
    #############################
    for check in range(pion):
        for column in range(1,9):
            flag =0
            check_up = pion_encours[check]
            check_up = check_up[:1]
            check_up = check_up + espace + str(column)
            if  pion_encours[check] == check_up :
                flag=-1
            if check_up in pion_encours :
                flag = flag +1
            if flag == 1:
                tks=Canvas(gui,bg="red",width=75,height=75)
                tks.grid(row=x_new,column=y_new)
                erreur +=1
                pion_encours.pop()
    #############################
    # DE BAS EN HAUT            #
    #############################
    for check in range(pion):
        for row in range(1,9):
            flag =0
            check_up = pion_encours[check]
            check_up = check_up[3:4]
            check_up = str(row) + espace + check_up
            if  pion_encours[check] == check_up :
                flag=-1
            if check_up in pion_encours :
                flag = flag +1
            if flag == 1:
                tks=Canvas(gui,bg="red",width=75,height=75)
                tks.grid(row=x_new,column=y_new)
                erreur = erreur +1
                pion_encours.pop()
    if pion == 8 :
        victoire()
    if erreur == 3 :
        perdu()

gui.bind("<Button 1>",pion)             #//// Appelle fonction principale

###############################################################################################







###############################################################################################
#                            BOUCLE POUR AFFICHER DE LA  GRILLE                               #
###############################################################################################

    #//// Affichage
for i in range(7):
    if (i % 2) == 0:
        damier_deux()
    else:
        damier_un()

###############################################################################################


gui.mainloop()



