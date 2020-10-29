#Importations
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from time import sleep
from random import randint

#on indique toutes les images à utiliser
images_path=["Tableau.png","Mainpage.png","Play.png","Bulle.png","Petitebulle.png",
             "Bruel0.jpg","Bruel1.jpg","Bruel2.jpg","Bruel3.jpg","Petitbruel0.jpg",
             "Petitbruel1.jpg","Petitbruel2.jpg","Petitbruel3.jpg","Stonks.jpg","Bruel_bye_bye.jpg"]

#Variable d'argent
argent=100

#Variable de mise
mise=0

#Variable du nombre choisi
nombre=0

#Variable permettant de tricher et de gagner
triche=False

#on créé la fenêtre  
mywindow = Tk()

#fonction qui s'active à chaque double click
def on_double_click(event):
    #on récupère la variable triche
    global triche
    #verification que le double click à été fait dans la zone approprié
    if(264<event.x<288 and 117<event.y<143):
        #on active la triche
        triche = True


#fonction qui créé la page principale
def mainpage(mywindow,canvas):
    #on ajoute une image 
    canvas.create_image(0, 0, anchor=NW, image=images_path[1])
    #on ajoute un boutton avec une commande éxécutant la fonction main
    bouttonstart = Button(mywindow,width=330,height=90,image=images_path[2],command=lambda: main(mywindow,canvas))
    #on rajoute le boutton à notre canvas
    canvas.create_window(600,700, window=bouttonstart)
    #on consolide le canvas avant de l'afficher
    canvas.pack(expand=False)

#fonction permettant de faire parler bruel
#text référencie le bloc text; bruel référencie le bloc image à changer; phrases correspond à une liste de phrase à dire; bruel_image correspond à une liste d'image pour faire une animation
def parle(mywindow,text,bruel,phrases,bruel_image):
    #correspond à l'indice de la photo à utiliser
    bruelindice=0
    
    #boucle pour chaque phrases
    for phrase in phrases:
        #boucle pour faire un effet machine à eccrire (on rajoute une lattre à chaque fois que la boucle s'éxécute)
        for lettre in range(len(phrase)):
            #on change le text
            canvas.itemconfig(text,text=phrase[:lettre+1])
            #1/3 on change l'image à l'image suivante
            if(lettre%3==0):
                #on vérifie que l'on est pas arrivé à la fin de la liste d'image pour l'animation
                if(bruelindice==len(bruel_image)-1):
                    #si oui on repart du début
                    bruelindice=0
                else:
                    #si non on avance d'une image
                    bruelindice+=1
            #on modifie l'image pour qu'elle soit celle correspondante à bruelindice
            canvas.itemconfig(bruel,image=bruel_image[bruelindice])
            #on met à jour la page pour appliquer les changement
            mywindow.update()
            #temps entre chaque affichage de lettre 0.06secondes
            sleep(0.06)
        #on revient à l'image de départ
        canvas.itemconfig(bruel,image=bruel_image[0])
        #on met à jour
        mywindow.update()
        #petit temp pour laisser le lecteur finir sa lecture
        sleep(1.5)

#fonction qui met en place la canvas quand on joue 
def jeu(mywindow,canvas):
    #on met la canvas à blanc
    canvas.delete("all")
    #on ajoute une image de bruel que l'on référencie dans une variable
    bruel = canvas.create_image(0, 0, anchor=NW, image=images_path[9])
    #on ajoute une image de bulle de texte
    canvas.create_image(0, 300, anchor=NW, image=images_path[4])
    #on ajoute une image de la table de jeu
    canvas.create_image(600, 0, anchor=NW, image=images_path[0])
    #on ajoute l'espace de texte
    text = canvas.create_text(300, 360, text="", font="Arial", fill="white")
    #on affiche L'argent du joueur
    textargent = canvas.create_text(300, 500, text=f"Tu possèdes actuellement cette somme d'argent (pas ouf): \n{argent}", font="Arial", fill="white")
    #Easter Eggs (zone clickable)
    mywindow.bind("<Double-Button-1>", on_double_click)
    #on met à jour la fenetre 
    canvas.update()
    #on apelle la fonction mise
    miser(mywindow,canvas,bruel,text,textargent)

#fonction qui ouvre une fenetre qui demande la mise
def miser(mywindow,canvas,bruel,text,textargent):
    #on récupère quelques variables global
    global argent
    global mise
    global nombre
    #on créé une fenetre de mise
    misewindow = Tk()
    #on attribue des options à notre fenêtre de mise
    # - nom de la fenetre
    misewindow.wm_title("Mise")
    # - couleur du fond
    misewindow.configure(bg="white")
    #On rajoute un text pour le nombre 
    Label(misewindow, text="Tu comptes parier sur quel nombre ?").pack()
    #On rajoute un input du nombre choisit allant de 0 à 49
    nombre=Spinbox(misewindow, from_=0, to=49)
    #on consolide la variable et l'élément
    nombre.pack()
    #On rajoute un text pour la mise 
    Label(misewindow, text="Tu comptes perdre combien chacal  ?").pack()
    #On rajoute un input de mise allant de 1 à l'argent possédé par le joueur
    mise=Spinbox(misewindow, from_=1, to=argent)
    #on consolide la variable et l'élément
    mise.pack()
    #On rajoute un boutton pour valider son entré qui nous ramène vers la fonction apresmise
    Button(misewindow,text="Miser",command=lambda: apresmise(misewindow,mywindow,canvas,bruel,text,textargent)).pack()
    #on fait rentrer la fenetre dans un état pacif
    misewindow.mainloop() 
    
#Après avoir clické sur le boutton Miser 
def apresmise(misewindow,mywindow,canvas,bruel,text,textargent):
    #on récupère quelques variables global
    global nombre
    global mise
    global argent
    global triche
    
    #au cas où l'on rentrerai une donné non valable
    try:
        #On récupère les valeurs des inputs
        # - Nombre choisit
        nombre=int(nombre.get())
        # - La mise
        mise=int(mise.get())
        #on ferme la fenetre mise
        misewindow.destroy()
    except Exception:
        #on ferme la fenetre mise
        misewindow.destroy()
        #et on la relance
        miser(mywindow,canvas,bruel,text,textargent)
    
    #si le nombre choisi n'est pas dans la plage de donné
    if not(nombre<=49 and nombre>=0):
        #je relance mise
        miser(mywindow,canvas,bruel,text,textargent)
    
    #si la mise est valide
    if not(mise<=argent and mise>0):
        #je relance mise
        miser(mywindow,canvas,bruel,text,textargent)
        
    #on enlève l'argent misé au joueur
    argent-=mise
    #On affiche l'argent du joueur
    canvas.itemconfig(textargent,text=f"Tu possèdes actuellement cette somme d'argent (pas ouf): \n{argent}")
    
    #on prend le nombre aléatoire
    nombrandome=randint(0,49)
    
    #x tableau nombre choisit
    x=nombre%5 *120
    #y tableau nombre choisit
    y=nombre//5 *80
    #x tableau nombre gagnant
    xrand=nombrandome%5 *120
    #y tableau nombre gagnant
    yrand=nombrandome//5 *80
        
    #on créé un rectangle qui va entourer le nombre choisit sur l'image du tableau
    canvas.create_rectangle(600+x,y,720+x,80+y,fill="",outline="blue",width=4)
    
    #on fait annoncer le numéro choisit par Bruel
    parle(mywindow,text,bruel,[f"Tu as choisi le numéro {nombre}"],[images_path[9]])
    
    #on verifie si le nombre tiré est égale au nombre auquel on a misé
    if(nombrandome==nombre or triche):
        #on ajoute 3fois la mise
        argent+=mise*3
        #On fait parler Bruelimage stonks 
        parle(mywindow,text,bruel,["C'était le numéro gagnant !!!!","Je suis impressionné"],[images_path[13]])
        #on d&sactive la triche
        triche=False
    #on verifie si les deux nombres sont de meme couleur
    elif(nombrandome%2==nombre%2):
        #on donne la moitié de  la mise 
        argent+=int(mise/2)
        #on créé un rectangle qui va entourer le nombre gagnant sur l'image du tableau
        canvas.create_rectangle(600+xrand,yrand,720+xrand,80+yrand,fill="",outline="yellow",width=4)
        #On fait parler Bruel
        parle(mywindow,text,bruel,["T'as perdu !",f"Mais le numero gagnant, le {nombrandome},\nétait de la même couleur que le tien !"],[images_path[9]])
    #si rien de tout ça 
    else:
        #on créé un rectangle qui va entourer le nombre gagnant sur l'image du tableau
        canvas.create_rectangle(600+xrand,yrand,720+xrand,80+yrand,fill="",outline="yellow",width=4)
        #on fait parler Bruel image triste
        parle(mywindow,text,bruel,["T'as perdu !", f"Le numero gagant etait le {nombrandome}","Vraiment pas ouf !\n Pas ma faute si t'es mauvais"],[images_path[14]])
    
    #On met a jour l'argent deu joueur
    canvas.itemconfig(textargent,text=f"Tu possèdes actuellement cette somme d'argent (pas ouf): \n{argent}")
    #on met à jour la fenetre
    canvas.update()
    
    #on verifie que le joueur à encore de l'argent 
    if(argent<1):
        #on appelle la fonction fin
        fin(mywindow,canvas,True)
    elif not(messagebox.askyesno('', "Voulez vous arretez de perdre de l'argent et garder une vie sociale et professionnelle stable ?")):
        #On appelle la fonction jeu pour recommencer
        jeu(mywindow,canvas)
    else:
        #on appelle la fonction fin
        fin(mywindow,canvas,False)
    

    
#fonction s'activant après avoir cliqué sur le boutton play
def main(mywindow,canvas):
    #on met la canvas à blanc
    canvas.delete("all")
    #on ajoute une image de bruel que l'on référencie dans une variable
    bruel = canvas.create_image(0, 0, anchor=NW, image=images_path[1])
    #on ajoute une image de bulle de texte
    canvas.create_image(0, 600, anchor=NW, image=images_path[3])
    #on consolide
    canvas.pack(expand=False)
    #on met à jour
    mywindow.update()
    #on rajoute un text dans la bulle 
    text = canvas.create_text(600, 700, text="", font="Arial", fill="white")
    #on fait parler bruel avec une liste de photo correspondant à son animation
    parle(mywindow,text,bruel,["Bonsoir, je suis Patrick Bruel !", "Bienvenue dans le casino Bruel, \ntu es ici dans l'unique but de perdre un maximum d'argent"," tu vas bien ?"],[images_path[5],images_path[6],images_path[7],images_path[8],images_path[6]])
    #pop up question tu vas bien
    messagebox.askyesno('', 'Tu vas bien ?')
    #on fait parler bruel avec une liste de photo correspondant à son animation
    parle(mywindow,text,bruel,["Cool ta vie, c'est passionnant !!"," Bon, commencons le jeu de la roulette qui casse la tête"],[images_path[5],images_path[6],images_path[7],images_path[8],images_path[6]])
    #on appelle la fonction jeu
    jeu(mywindow,canvas)

#fonction de fin
def fin(mywindow,canvas,pauvre):
    #on met la canvas à blanc
    canvas.delete("all")
    #on ajoute une image de bruel que l'on référencie dans une variable
    bruel = canvas.create_image(0, 0, anchor=NW, image=images_path[1])
    #on ajoute une image de bulle de texte
    canvas.create_image(0, 600, anchor=NW, image=images_path[3])
    #on consolide
    canvas.pack(expand=False)
    #on met à jour
    mywindow.update()
    #on rajoute un text dans la bulle 
    text = canvas.create_text(600, 700, text="", font="Arial", fill="white")
    #text en fonction de l'argent
    if(pauvre):
        #on fait parler bruel avec une liste de photo correspondant à son animation si joueur à 0 d'argent
        parle(mywindow,text,bruel,["T'as tout perdu, je te conseille de chercher des cartes google play si tu veux te refaire une somme d'argent convenable"],[images_path[5],images_path[6],images_path[7],images_path[8],images_path[6]])
    else:
        #on fait parler bruel avec une liste de photo correspondant à son animation si joueur n'a pas 0 d'argent
        parle(mywindow,text,bruel,["Bravo", "Vous avez perdu un max d'argent, \nvotre fils va sombrer dans la grenadine sans eau et mourir du diabète dans 3 jours","Bisous <3"],[images_path[5],images_path[6],images_path[7],images_path[8],images_path[6]])
    #on femre la denetre
    mywindow.destroy()
    
#################### D E B U T ####################
    
#on converti toutes les images en format pris en charge par tkinter
for i in range(len(images_path)):
    images_path[i] = ImageTk.PhotoImage(Image.open(images_path[i]))

#on attribue des options à notre fenêtre
# - nom de la fenetre
mywindow.wm_title("Casino Game")
# - taille de la fenêtre
mywindow.geometry("1200x800")
# - couleur du fond
mywindow.configure(bg="black")

#on attribue un espace de dessin à notre fenêtre 
canvas = Canvas(mywindow,width=1200, height=800, background='black')

#on lance la page de début
mainpage(mywindow,canvas)

#on fait rentrer la fenetre dans un état pacif
mywindow.mainloop()
