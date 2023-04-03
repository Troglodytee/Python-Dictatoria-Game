from pathlib import *
import os
import contextlib
with contextlib.redirect_stdout(None) :
    import pygame
from pygame.locals import *
from random import *

def initialisation() :
    global ecran
    global ecrire
    global nom
    global nom_pays
    global code
    global etat_code
    global code1
    global code2
    global popularite
    global argent
    global nourriture
    global date
    global temps
    global cooldown
    global vitesse
    global map
    global deplacements
    global russell2
    global record
    global tcarre
    global carre_im
    global cafe2
    ecran = 0
    ecrire = 0
    nom = ""
    nom_pays = ""
    code = ""
    etat_code = 0
    code1 = 0
    code2 = 0
    popularite = 100
    argent = 100
    nourriture = 0
    date = [4,5,2020]
    temps = 0
    cooldown = 4
    vitesse = 1
    russell2 = 0
    record = 0
    tcarre = 0
    carre_im = 1
    cafe2 = 0
    map = []
    for loop in range (1000) :
        map += ["e"]
    for loop in range (80) :
        for loop in range (10) :
            map += ["e"]
        for loop in range (80) :
            map += ["ter"]
        for loop in range (10) :
            map += ["e"]
    for loop in range (1000) :
        map += ["e"]

    map[2939] = "tar"
    map[2940] = "tac0"
    map[2941] = "tar"
    map[3039] = "tam4"
    map[3040] = "taq"
    map[3041] = "tah2"
    map[3139] = "tar"
    map[3140] = "tau2"
    map[3141] = "tar"

    for i in range (len(map)) :
        if i//100 >= 14 and i//100 <= 85 and i-100*(i//100) >= 14 and i-100*(i//100) <= 85 :
            non = 0
            for j in range (-600,700,100) :
                for k in range (-6,7,1) :
                    if not map[i+j+k] == "ter" :
                        non = 1
            if non == 0 and randint(1,20) == 1 :
                map[i] = "teq"
                nb_batiments = randint(3,24)
                a = "hhuuc"
                map[i-100] = "te"+a[randint(0,4)]
                map[i-99] = "te"+a[randint(0,4)]
                map[i+1] = "te"+a[randint(0,4)]
                if nb_batiments > 3 :
                    map[i+101] = "te"+a[randint(0,4)]
                if nb_batiments > 4 :
                    map[i+100] = "te"+a[randint(0,4)]
                if nb_batiments > 5 :
                    map[i+99] = "te"+a[randint(0,4)]
                if nb_batiments > 6 :
                    map[i-1] = "te"+a[randint(0,4)]
                if nb_batiments > 7 :
                    map[i-101] = "te"+a[randint(0,4)]
                if nb_batiments > 8 :
                    map[i-200] = "te"+a[randint(0,4)]
                if nb_batiments > 9 :
                    map[i-199] = "te"+a[randint(0,4)]
                if nb_batiments > 10 :
                    map[i-198] = "te"+a[randint(0,4)]
                if nb_batiments > 11 :
                    map[i-98] = "te"+a[randint(0,4)]
                if nb_batiments > 12 :
                    map[i+2] = "te"+a[randint(0,4)]
                if nb_batiments > 13 :
                    map[i+102] = "te"+a[randint(0,4)]
                if nb_batiments > 14 :
                    map[i+202] = "te"+a[randint(0,4)]
                if nb_batiments > 15 :
                    map[i+201] = "te"+a[randint(0,4)]
                if nb_batiments > 16 :
                    map[i+200] = "te"+a[randint(0,4)]
                if nb_batiments > 17 :
                    map[i+199] = "te"+a[randint(0,4)]
                if nb_batiments > 18 :
                    map[i+198] = "te"+a[randint(0,4)]
                if nb_batiments > 19 :
                    map[i+98] = "te"+a[randint(0,4)]
                if nb_batiments > 20 :
                    map[i-2] = "te"+a[randint(0,4)]
                if nb_batiments > 21 :
                    map[i-102] = "te"+a[randint(0,4)]
                if nb_batiments > 22 :
                    map[i-202] = "te"+a[randint(0,4)]
                if nb_batiments > 23 :
                    map[i-201] = "te"+a[randint(0,4)]

    deplacements = []

def cinematique_deb() :
    global ecran
    global nom
    global nom_pays
    fenetre.blit(fond_noir,(-500,-719))
    phrase = "Vous êtes "+nom+", jadis gouverneur de la nation la plus puissante au monde. Mais celle-ci sombra dans le chaos et la guerre et disparu. Vous vous relevez à présent pour rebâtir une nouvelle nation du nom de "+nom_pays+"."
    pos = (50,50)
    for a in range (len(phrase)) :
        if a%50 == 0 :
            pos = (50,pos[1]+50)
        if not phrase[a] == " " :
            if not phrase[a] == "0" and not phrase[a] == "1" and not phrase[a] == "2" and not phrase[a] == "3" and not phrase[a] == "4" and not phrase[a] == "5" and not phrase[a] == "6" and not phrase[a] == "7" and not phrase[a] == "8" and not phrase[a] == "9" and not phrase[a] == "," and not phrase[a] == "." and not phrase[a] == "-" and not phrase[a] == "â" :
                if phrase[a] == phrase[a].upper() :
                    lettre = pygame.image.load(raccourci+"sprite\\alphabet\\"+phrase[a].lower()+"2.png").convert()
                else :
                    lettre = pygame.image.load(raccourci+"sprite\\alphabet\\"+phrase[a]+".png").convert()
            else :
                lettre = pygame.image.load(raccourci+"sprite\\alphabet\\"+phrase[a]+".png").convert()
            fenetre.blit(lettre,pos)
        pos = (pos[0]+18,pos[1])

    pygame.display.flip()

    pygame.time.wait(10000)

    ecran = 1

    pygame.mixer.music.load(raccourci+"son\\infire_theme.mp3")
    pygame.mixer.music.play()

    change_ecran()

def reponse_oui() :
    fenetre.blit(fond8,(0,0))
    fenetre.blit(russell,(380,33))
    pos = 366
    for i in range (3) :
        if i == 0 :
            phrase = "As-tu entendu parler du Dabou ? Cette sale bête"
        elif i == 1 :
            phrase = "passe son temps à fouiner dans mes bureaux."
        elif i == 2 :
            phrase = "Pourrais-tu m'en débarrasser ?"
        for a in range (len(phrase)) :
            if not phrase[a] == " " and not phrase[a] == ":" and not phrase[a] == "?" :
                if not phrase[a] == "0" and not phrase[a] == "1" and not phrase[a] == "2" and not phrase[a] == "3" and not phrase[a] == "4" and not phrase[a] == "5" and not phrase[a] == "6" and not phrase[a] == "7" and not phrase[a] == "8" and not phrase[a] == "9" and not phrase[a] == "," and not phrase[a] == "." and not phrase[a] == "-" and not phrase[a] == "'" and not phrase[a] == "%" :
                    if phrase[a] == phrase[a].upper() :
                        lettre = pygame.image.load(raccourci+"sprite\\alphabet\\"+phrase[a].lower()+"2.png").convert()
                    else :
                        lettre = pygame.image.load(raccourci+"sprite\\alphabet\\"+phrase[a]+".png").convert()
                else :
                    lettre = pygame.image.load(raccourci+"sprite\\alphabet\\"+phrase[a]+".png").convert()
                lettre.set_colorkey((0,0,0))
                fenetre.blit(lettre,(50+a*18,pos))
            elif phrase[a] == ":" :
                lettre = pygame.image.load(raccourci+"sprite\\alphabet\\deux_points.png").convert()
                lettre.set_colorkey((0,0,0))
                fenetre.blit(lettre,(50+a*18,pos))
            elif phrase[a] == "?" :
                lettre = pygame.image.load(raccourci+"sprite\\alphabet\\point_interrogation.png").convert()
                lettre.set_colorkey((0,0,0))
                fenetre.blit(lettre,(50+a*18,pos))
        pos += 30

    pygame.display.flip()
    pygame.time.wait(10000)

    fenetre.blit(fond8,(0,0))
    fenetre.blit(russell,(380,33))
    phrase = "Je m'en charge !"
    for a in range (len(phrase)) :
        if not phrase[a] == " " and not phrase[a] == ":" and not phrase[a] == "?" :
            if not phrase[a] == "0" and not phrase[a] == "1" and not phrase[a] == "2" and not phrase[a] == "3" and not phrase[a] == "4" and not phrase[a] == "5" and not phrase[a] == "6" and not phrase[a] == "7" and not phrase[a] == "8" and not phrase[a] == "9" and not phrase[a] == "," and not phrase[a] == "." and not phrase[a] == "-" and not phrase[a] == "'" and not phrase[a] == "%" and not phrase[a] == "!" :
                if phrase[a] == phrase[a].upper() :
                    lettre = pygame.image.load(raccourci+"sprite\\alphabet\\"+phrase[a].lower()+"2.png").convert()
                else :
                    lettre = pygame.image.load(raccourci+"sprite\\alphabet\\"+phrase[a]+".png").convert()
            else :
                lettre = pygame.image.load(raccourci+"sprite\\alphabet\\"+phrase[a]+".png").convert()
            lettre.set_colorkey((0,0,0))
            fenetre.blit(lettre,(50+a*18,366))
        elif phrase[a] == ":" :
            lettre = pygame.image.load(raccourci+"sprite\\alphabet\\deux_points.png").convert()
            lettre.set_colorkey((0,0,0))
            fenetre.blit(lettre,(50+a*18,366))
        elif phrase[a] == "?" :
            lettre = pygame.image.load(raccourci+"sprite\\alphabet\\point_interrogation.png").convert()
            lettre.set_colorkey((0,0,0))
            fenetre.blit(lettre,(50+a*18,366))

    pygame.display.flip()
    pygame.time.wait(3000)

def game_over() :
    global mort
    global nom
    global nom_pays
    global date
    pygame.mixer.music.load(raccourci+"son\\game_over.mp3")
    pygame.mixer.music.play()
    pygame.time.wait(6000)
    fenetre.blit(gameover_background,(0,0))
    pygame.display.flip()
    pygame.time.wait(3000)
    fenetre.blit(gameover1_background,(0,0))
    if mort == 1 :
        liste_mois = ["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre","Décembre"]
        phrase = "Le "+str(date[0])+" "+liste_mois[date[1]-1]+" "+str(date[2])+", Mr "+nom+", gouverneur de "+nom_pays+", est mort. Il est passé à travers la fenêtre de son bureau se situant au dernier étage de son building. Personne ne connait véritablement les raisons qui l'ont poussé à se jeter par sa fenêtre. Certains pense qu'elle a juste cédé lorsque que le gouverneur s'est appuyé dessus mais d'autre pense qu'il se serait donné la mort car il aurait découvert que nous sommes tous prisonniers d'un jeu vidéo stupide."

    elif mort == 2 :
        phrase = "Le pays de "+nom_pays+" a sombré dans l'anarchie depuis que Mr "+nom+" a cessé de le gouverner sans prévenir pour se plonger dans un jeu vidéo."

    elif mort == 3 :
        phrase = "Le pays de "+nom_pays+" a été détruit suite à une attaque. Il n'existe désormais plus et son gouverneur a été capturé."

    elif mort == 4 :
        phrase = "Un coup d'état a eu lieu dans le pays de "+nom_pays+", le gouvernement a été renversé car selon les habitants, ils n'étaient pas assez payés."

    elif mort == 5 :
        phrase = "Le pays de "+nom_pays+" ne compte plus aucun habitant, Son existance a désormais prit fin."

    elif mort == 6 :
        phrase = "Le gouverneur de "+nom_pays+" a été retrouvé mort devant une machine à café. Il a fait une overdose de caféine."

    pos = (50,200)
    for a in range (len(phrase)) :
        if a%50 == 0 :
            pos = (50,pos[1]+30)
        if not phrase[a] == " " :
            if not phrase[a] == "0" and not phrase[a] == "1" and not phrase[a] == "2" and not phrase[a] == "3" and not phrase[a] == "4" and not phrase[a] == "5" and not phrase[a] == "6" and not phrase[a] == "7" and not phrase[a] == "8" and not phrase[a] == "9" and not phrase[a] == "," and not phrase[a] == "." and not phrase[a] == "-" and not phrase[a] == "â" and not phrase[a] == "é" and not phrase[a] == "ê" and not phrase[a] == "'"  :
                if phrase[a] == phrase[a].upper() :
                    lettre = pygame.image.load(raccourci+"sprite\\alphabet\\"+phrase[a].lower()+"2.png").convert()
                else :
                    lettre = pygame.image.load(raccourci+"sprite\\alphabet\\"+phrase[a]+".png").convert()
            else :
                lettre = pygame.image.load(raccourci+"sprite\\alphabet\\"+phrase[a]+".png").convert()
            fenetre.blit(lettre,pos)
        pos = (pos[0]+18,pos[1])
    pygame.display.flip()

    if mort == 1 :
        pygame.time.wait(30000)
    elif mort == 2 or mort == 3 or mort == 4 or mort == 5 or mort == 6 :
        pygame.time.wait(10000)

    for i in range (1,5,1) :
        credit = pygame.image.load(raccourci+"sprite\\credit"+str(i)+".png").convert()
        fenetre.blit(credit,(0,0))
        pygame.display.flip()
        pygame.time.wait(3000)
    initialisation()
    change_ecran()

def jeu() :
    global temps
    global date
    global map
    global argent
    global nourriture
    global popularite
    global deplacements
    global cooldown
    global vitesse
    global mort
    global cafe2
    if cooldown < 0 :
        cooldown = vitesse
        # mouvement des soldats alliés
        for i in range (0,len(deplacements),2) :
            if len(deplacements) > 1 :
                if deplacements[i]//100 > deplacements[i+1]//100 :
                    direction = "1"
                elif deplacements[i]//100 < deplacements[i+1]//100 :
                    direction = "2"
                else :
                    direction = "0"
                if deplacements[i]-(deplacements[i]//100)*100 > deplacements[i+1]-(deplacements[i+1]//100)*100 :
                    direction += "1"
                elif deplacements[i]-(deplacements[i]//100)*100 < deplacements[i+1]-(deplacements[i+1]//100)*100 :
                    direction += "2"
                else :
                    direction += "0"

                oui = 0

                if direction[0] == "1" :
                    if map[deplacements[i]-100] == "tar" or map[deplacements[i]-100] == "ter" or map[deplacements[i]-100][0:3] == "tac" :
                        if not map[deplacements[i]-100][0:3] == "tac" :
                            map[deplacements[i]-100] = "tar"+map[deplacements[i]][3]
                            if map[deplacements[i]][0:3] == "tac" :
                                map[deplacements[i]] = map[deplacements[i]][0:3]+"0"
                            else :
                                map[deplacements[i]] = "tar"
                            deplacements[i] -= 100
                            oui = 1
                        elif deplacements[i]-100 == deplacements[i+1] :
                            if int(map[deplacements[i+1]][3])+int(map[deplacements[i]][3]) <= 9 :
                                map[deplacements[i]-100] = map[deplacements[i]-100][0:3]+str(int(map[deplacements[i+1]][3])+int(map[deplacements[i]][3]))
                                map[deplacements[i]] = "tar"
                            deplacements[i] -= 100
                            oui = 1

                elif direction[0] == "2" :
                    if map[deplacements[i]+100] == "tar" or map[deplacements[i]+100] == "ter" or map[deplacements[i]+100][0:3] == "tac" :
                        if not map[deplacements[i]+100][0:3] == "tac" :
                            map[deplacements[i]+100] = "tar"+map[deplacements[i]][3]
                            if map[deplacements[i]][0:3] == "tac" :
                                map[deplacements[i]] = map[deplacements[i]][0:3]+"0"
                            else :
                                map[deplacements[i]] = "tar"
                            deplacements[i] += 100
                            oui = 1
                        elif deplacements[i]+100 == deplacements[i+1] :
                            if int(map[deplacements[i+1]][3])+int(map[deplacements[i]][3]) <= 9 :
                                map[deplacements[i]+100] = map[deplacements[i]+100][0:3]+str(int(map[deplacements[i+1]][3])+int(map[deplacements[i]][3]))
                                map[deplacements[i]] = "tar"
                            deplacements[i] += 100
                            oui = 1

                if oui == 0 :
                    if direction[1] == "1" :
                        if map[deplacements[i]-1] == "tar" or map[deplacements[i]-1] == "ter" or map[deplacements[i]-1][0:3] == "tac" :
                            if not map[deplacements[i]-1][0:3] == "tac" :
                                map[deplacements[i]-1] = "tar"+map[deplacements[i]][3]
                                if map[deplacements[i]][0:3] == "tac" :
                                    map[deplacements[i]] = map[deplacements[i]][0:3]+"0"
                                else :
                                    map[deplacements[i]] = "tar"
                                deplacements[i] -= 1
                            elif deplacements[i]-1 == deplacements[i+1] :
                                if int(map[deplacements[i+1]][3])+int(map[deplacements[i]][3]) <= 9 :
                                    map[deplacements[i]-1] = map[deplacements[i]-1][0:3]+str(int(map[deplacements[i+1]][3])+int(map[deplacements[i]][3]))
                                    map[deplacements[i]] = "tar"
                                deplacements[i] -= 1

                    elif direction[1] == "2" :
                        if map[deplacements[i]+1] == "tar" or map[deplacements[i]+1] == "ter" or map[deplacements[i]+1][0:3] == "tac" :
                            if not map[deplacements[i]+1][0:3] == "tac" :
                                map[deplacements[i]+1] = "tar"+map[deplacements[i]][3]
                                if map[deplacements[i]][0:3] == "tac" :
                                    map[deplacements[i]] = map[deplacements[i]][0:3]+"0"
                                else :
                                    map[deplacements[i]] = "tar"
                                deplacements[i] += 1
                            elif deplacements[i]+1 == deplacements[i+1] :
                                if int(map[deplacements[i+1]][3])+int(map[deplacements[i]][3]) <= 9 :
                                    map[deplacements[i]+1] = map[deplacements[i]+1][0:3]+str(int(map[deplacements[i+1]][3])+int(map[deplacements[i]][3]))
                                    map[deplacements[i]] = "tar"
                                deplacements[i] += 1

                if deplacements[i] == deplacements[i+1] :
                    del deplacements[i:i+2]

            if i == len(deplacements)-2 or i == len(deplacements)-3 :
                break

        # mouvement des soldats ennemis
        for i in range (len(map)) :
            if map[i][0:3] == "ter" and len(map[i]) == 4 :
                if map[i-100][0:2] == "te" or map[i-100] == "tar" :
                    if map[i+1][0:2] == "te" or map[i+1] == "tar" :
                        if map[i+100][0:2] == "te" or map[i+100] == "tar" :
                            if map[i-1][0:2] == "te" or map[i-1] == "tar" :
                                if i//100 < 30 :
                                    direction = "2"
                                elif i//100 > 30 :
                                    direction = "1"
                                else :
                                    direction = "0"
                                if i-(i//100)*100 < 40 :
                                    direction += "2"
                                elif i-(i//100)*100 > 40 :
                                    direction += "1"
                                else :
                                    direction += "0"

                                oui = 0
                                if direction[0] == "1" :
                                    if map[i-100] == "ter" or map[i-100] == "tar" :
                                        map[i-100] = map[i]+"1"
                                        map[i] = "ter"
                                        oui = 1
                                elif direction[0] == "2" :
                                    if map[i+100] == "ter" or map[i+100] == "tar" :
                                        map[i+100] = map[i]+"1"
                                        map[i] = "ter"
                                        oui = 1

                                if oui == 0 :
                                    if direction[1] == "1" :
                                        if map[i-1] == "ter" or map[i-1] == "tar" :
                                            map[i-1] = map[i]+"1"
                                            map[i] = "ter"
                                    elif direction[1] == "2" :
                                        if map[i+1] == "ter" or map[i+1] == "tar" :
                                            map[i+1] = map[i]+"1"
                                            map[i] = "ter"
        for i in range (len(map)) :
            if len(map[i]) == 5 :
                map[i] = map[i][0:4]

        # attaque des soldats alliés
        for i in range (len(map)) :
            if not map[i] == "e" :
                if map[i][0:3] == "tar" and len(map[i]) > 3 :
                    if map[i-100][0:3] == "ter" and len(map[i-100]) > 3 :
                        if map[i-100][3] == "1" :
                            map[i-100] = "ter"
                        else :
                            if int(map[i-100][3]) <= int(map[i][3]) :
                                map[i-100] = map[i-100][0:3]+str(int(map[i-100][3])-1)
                            elif randint(1,10) <= 10-(int(map[i-100][3])-int(map[i][3])) :
                                map[i-100] = map[i-100][0:3]+str(int(map[i-100][3])-1)

                    elif map[i+1][0:3] == "ter" and len(map[i+1]) > 3 :
                        if map[i+1][3] == "1" :
                            map[i+1] = "ter"
                        else :
                            if int(map[i+1][3]) <= int(map[i][3]) :
                                map[i+1] = map[i+1][0:3]+str(int(map[i+1][3])-1)
                            elif randint(1,10) <= 10-(int(map[i+1][3])-int(map[i][3])) :
                                map[i+1] = map[i+1][0:3]+str(int(map[i+1][3])-1)

                    elif map[i+100][0:3] == "ter" and len(map[i+100]) > 3 :
                        if map[i+100][3] == "1" :
                            map[i+100] = "ter"
                        else :
                            if int(map[i+100][3]) <= int(map[i][3]) :
                                map[i+100] = map[i+100][0:3]+str(int(map[i+100][3])-1)
                            elif randint(1,10) <= 10-(int(map[i+100][3])-int(map[i][3])) :
                                map[i+100] = map[i+100][0:3]+str(int(map[i+100][3])-1)

                    elif map[i-1][0:3] == "ter" and len(map[i-1]) > 3 :
                        if map[i-1][3] == "1" :
                            map[i-1] = "ter"
                        else :
                            if int(map[i-1][3]) <= int(map[i][3]) :
                                map[i-1] = map[i-1][0:3]+str(int(map[i-1][3])-1)
                            elif randint(1,10) <= 10-(int(map[i-1][3])-int(map[i][3])) :
                                map[i-1] = map[i-1][0:3]+str(int(map[i-1][3])-1)

                    elif map[i-100][0:2] == "te" and not map[i-100] == "ter" :
                        map[i-100] = "ter"

                    elif map[i+1][0:2] == "te" and not map[i+1] == "ter" :
                        map[i+1] = "ter"

                    elif map[i+100][0:2] == "te" and not map[i+100] == "ter" :
                        map[i+100] = "ter"

                    elif map[i-1][0:2] == "te" and not map[i-1] == "ter" :
                        map[i-1] = "ter"

        # attaque des soldats ennemis
        for i in range (len(map)) :
            if not map[i] == "e" :
                if map[i][0:3] == "ter" and len(map[i]) > 3 :

                    oui = 0

                    if map[i-100][0:3] == "tar" and len(map[i-100]) > 3 :
                        if map[i-100][3] == "1" :
                            map[i-100] = "tar"
                        else :
                            if int(map[i-100][3]) <= int(map[i][3]) :
                                map[i-100] = map[i-100][0:3]+str(int(map[i-100][3])-1)
                            elif randint(1,10) <= 10-(int(map[i-100][3])-int(map[i][3])) :
                                map[i-100] = map[i-100][0:3]+str(int(map[i-100][3])-1)
                        oui = 1

                    elif map[i+1][0:3] == "tar" and len(map[i+1]) > 3 :
                        if map[i+1][3] == "1" :
                            map[i+1] = "tar"
                        else :
                            if int(map[i+1][3]) <= int(map[i][3]) :
                                map[i+1] = map[i+1][0:3]+str(int(map[i+1][3])-1)
                            elif randint(1,10) <= 10-(int(map[i+1][3])-int(map[i][3])) :
                                map[i+1] = map[i+1][0:3]+str(int(map[i+1][3])-1)
                        oui = 2

                    elif map[i+100][0:3] == "tar" and len(map[i+100]) > 3 :
                        if map[i+100][3] == "1" :
                            map[i+100] = "tar"
                        else :
                            if int(map[i+100][3]) <= int(map[i][3]) :
                                map[i+100] = map[i+100][0:3]+str(int(map[i+100][3])-1)
                            elif randint(1,10) <= 10-(int(map[i+100][3])-int(map[i][3])) :
                                map[i+100] = map[i+100][0:3]+str(int(map[i+100][3])-1)
                        oui = 3

                    elif map[i-1][0:3] == "tar" and len(map[i-1]) > 3 :
                        if map[i-1][3] == "1" :
                            map[i-1] = "tar"
                        else :
                            if int(map[i-1][3]) <= int(map[i][3]) :
                                map[i-1] = map[i-1][0:3]+str(int(map[i-1][3])-1)
                            elif randint(1,10) <= 10-(int(map[i-1][3])-int(map[i][3])) :
                                map[i-1] = map[i-1][0:3]+str(int(map[i-1][3])-1)
                        oui = 4

                    elif map[i-100][0:2] == "ta" and not map[i-100] == "tar" :
                        if not map[i-100] == "taq" :
                            nb = int(map[i-100][3])
                        map[i-100] = "tar"
                        if map[i-100][0:3] == "tam" :
                            oui = 5

                    elif map[i+1][0:2] == "ta" and not map[i+1] == "tar" :
                        if not map[i+1] == "taq" :
                            nb = int(map[i+1][3])
                        map[i+1] = "tar"
                        if map[i+1][0:3] == "tam" :
                            oui = 6

                    elif map[i+100][0:2] == "ta" and not map[i+100] == "tar" :
                        if not map[i+100] == "taq" :
                            nb = int(map[i+100][3])
                        map[i+100] = "tar"
                        if map[i+100][0:3] == "tam" :
                            oui = 7

                    elif map[i-1][0:2] == "ta" and not map[i-1] == "tar" :
                        if not map[i-1] == "taq" :
                            nb = int(map[i-1][3])
                        map[i-1] = "tar"
                        if map[i-1][0:3] == "tam" :
                            oui = 8

                    if oui > 4 :
                        i = 0
                        while nb > 0 and i < len(map) :
                            if map[i][0:3] == "tah" and int(map[i][3]) > 0 or map[i][0:3] == "tau" and int(map[i][3]) > 0 :
                                if nb < int(map[i][3]) :
                                    map[i] = map[i][0:3]+str(int(map[i][3])-nb)
                                    nb = 0
                                else :
                                    nb -= int(map[i][3])
                                    map[i] = map[i][0:3]+"0"
                            i += 1
                        if nb > 0 :
                            i = 0
                            while nb > 0 and i < len(map) :
                                if map[i][0:3] == "tac" and int(map[i][3]) > 0 :
                                    if nb < int(map[i][3]) :
                                        map[i] = map[i][0:3]+str(int(map[i][3])-nb)+str(int(map[i][4])-nb)
                                        nb = 0
                                    else :
                                        nb -= int(map[i][3])
                                        map[i] = map[i][0:3]+"0"
                                i += 1
                            if nb > 0 :
                                i = 0
                                while i < len(map) :
                                    if map[i][0:3] == "tar" and len(map[i]) > 3 :
                                        if int(map[i][3]) > 0 :
                                            if nb < int(map[i][3]) :
                                                map[i] = map[i][0:3]+str(int(map[i][3])-nb)
                                                nb = 0
                                            else :
                                                nb -= int(map[i][3])
                                                map[i] = map[i][0:3]+"0"
                                    i += 1

                    elif oui > 0 :
                        for i in range (len(map)) :
                            if map[i][0:3] == "tam" and int(map[i][3]) > 0 :
                                map[i] = "tam"+str(int(map[i][3])-1)
                                break

        total = 0
        for i in range (len(map)) :
            if map[i][0:3] == "tam" :
                total += int(map[i][3])

        if total == 0 :
            mort = 5
            change_ecran()
            game_over()
        elif not map[3040] == "taq" :
            mort = 3
            change_ecran()
            game_over()

    if int(temps) > 10*vitesse :
        # changement date
        cafe2 = 0
        temps = 0
        date[0] += 1
        if date[0] == 32 and date[1] == 12 :
            date[0] = 1
            date[1] = 1
            date[2] += 1
        elif date[0] == 29 and date[1] == 2 and not date[2]%4 == 0 or date[0] == 30 and date[1] == 2 and date[2]%4 == 0 or date[0] == 32 and date[1] == 1 or date[0] == 32 and date[1] == 3 or date[0] == 32 and date[1] == 5 or date[0] == 32 and date[1] == 7 or date[0] == 32 and date[1] == 8 or date[0] == 32 and date[1] == 10 or date[0] == 32 and date[1] == 12 or date[0] == 31 and date[1] == 4 or date[0] == 31 and date[1] == 6 or date[0] == 31 and date[1] == 9 or date[0] == 31 and date[1] == 11 :
            date[0] = 1
            date[1] += 1

        # récolte des champs et des usines
        for i in range (len(map)) :
            if map[i][0:3] == "tah" :
                nourriture += 5*int(map[i][3])
            elif map[i][0:3] == "tau" :
                argent += 5*int(map[i][3])

        # repas de tous les habitants
        for i in range (len(map)) :
            if map[i][0:3] == "tam" :
                if nourriture >= int(map[i][3]) :
                    nourriture -= int(map[i][3])
                else :
                    map[i] = map[i][0:3]+str(int(map[i][3])-(int(map[i][3])-nourriture))
                    nourriture = 0

        total = 0
        for i in range (len(map)) :
            if map[i][0:3] == "tam" :
                total += int(map[i][3])

        # paie des habitants
        for i in range (len(map)) :
            if map[i][0:3] == "tah" or map[i][0:3] == "tau" :
                if argent >= int(map[i][3]) :
                    argent -= int(map[i][3])
                else :
                    popularite -= 100-(total/100)*(int(map[i][3])-(int(map[i][3])-argent))
                    argent = 0
            elif map[i][0:3] == "tac" or map[i][0:3] == "tar" and len(map[i]) > 3 :
                if int(argent/2) >= int(map[i][3]) :
                    argent -= 2*int(map[i][3])
                else :
                    popularite -= 100-(total/100)*(int(map[i][3])-(int(map[i][3])-argent/2))
                    if argent/2 == int(argent/2) :
                        argent = 0
                    else :
                        argent = 1
        popularite = int(popularite)

        total2 = 0
        for i in range (len(map)) :
            if map[i][0:3] == "tah" or map[i][0:3] == "tau" or map[i][0:3] == "tac" or map[i][0:3] == "tar" and len(map[i]) > 3 :
                total2 += int(map[i][3])

        # peuplage des champs et des usines
        total2 = total-total2
        i = 0
        while total2 > 0 and i < len(map) :
            if map[i][0:3] == "tah" or map[i][0:3] == "tau" :
                if int(map[i][3]) < 4 :
                    total2 -= 1
                    map[i] = map[i][0:3]+str(int(map[i][3])+1)
            i += 1

        # peuplage des casernes
        i = 0
        while total2 > 0 and i < len(map) :
            if map[i][0:3] == "tac" :
                if int(map[i][3]) < 9 :
                    total2 -= 1
                    map[i] = map[i][0:3]+str(int(map[i][3])+1)
            i += 1

        # peuplage des maisons
        for i in range (len(map)) :
            if not map[i] == "e" :
                if map[i][0:3] == "tam" and len(map[i]) > 3 :
                    if int(map[i][3]) < 4 :
                        map[i] = map[i][0:3]+str(int(map[i][3])+1)

        # attaque ?
        total = 0
        for i in range (len(map)) :
            if not map[i] == "e" and map[i][1] == "a" :
                if map[i][2] == "r" :
                    total += 1
                else :
                    total += 2
        if total >= 60 and randint(1,20) == 1 :
            attaque(1+((total-60)//20))

        if popularite <= 0 :
            mort = 4
            change_ecran()
            game_over()

    change_ecran()

def attaque(nb_attaquants) :
    global map
    attaquants_haut = 0
    attaquants_droite = 0
    attaquants_bas = 0
    attaquants_gauche = 0
    non = 0
    while non == 0 :
        attaquants_haut += 1
        nb_attaquants -= 1
        if nb_attaquants == 0 :
            non = 1
        else :
            attaquants_droite += 1
            nb_attaquants -= 1
            if nb_attaquants == 0 :
                non = 1
            else :
                attaquants_bas += 1
                nb_attaquants -= 1
                if nb_attaquants == 0 :
                    non = 1
                else :
                    attaquants_gauche += 1
                    nb_attaquants -= 1
                    if nb_attaquants == 0 :
                        non = 1

    i = 3040
    while not map[i] == "ter" :
        i -= 100
    i -= 300
    while not map[i] == "ter" :
        i -= 100
    map[i] = "ter9"
    j = 1
    while attaquants_haut > 1 and j < 59 :
        if map[i+j] == "ter" and j < 59 :
            map[i+j] = "ter9"
            attaquants_haut -= 1
        if map[i-j] == "ter" and j < 39 :
            map[i-j] = "ter9"
            attaquants_haut -= 1
        j += 1
    if attaquants_haut == 1 and map[i-j] == "ter" :
        map[i-j] = "ter9"

    i = 3040
    while not map[i] == "ter" :
        i += 1
    i += 3
    while not map[i] == "ter" :
        i += 1
    map[i] = "ter9"
    j = 1
    while attaquants_droite > 1 and j < 69 :
        if map[i+j*100] == "ter" and j < 69 :
            map[i+j*100] = "ter9"
            attaquants_droite -= 1
        if map[i-j*100] == "ter" and j < 29 :
            map[i-j*100] = "ter9"
            attaquants_droite -= 1
        j += 1
    if attaquants_droite == 1 and map[i-j*100] == "ter" :
        map[i-j*100] = "ter9"

    i = 3040
    while not map[i] == "ter" :
        i += 100
    i += 300
    while not map[i] == "ter" :
        i += 100
    map[i] = "ter9"
    j = 1
    while attaquants_haut > 1 and j < 59 :
        if map[i+j] == "ter" and j < 59 :
            map[i+j] = "ter9"
            attaquants_haut -= 1
        if map[i-j] == "ter" and j < 39 :
            map[i-j] = "ter9"
            attaquants_haut -= 1
        j += 1
    if attaquants_haut == 1 and map[i-j] == "ter" :
        map[i-j] = "ter9"

    i = 3040
    while not map[i] == "ter" :
        i -= 1
    i -= 3
    while not map[i] == "ter" :
        i -= 1
    map[i] = "ter9"
    j = 1
    while attaquants_droite > 1 and j < 69 :
        if map[i+j*100] == "ter" and j < 69 :
            map[i+j*100] = "ter9"
            attaquants_droite -= 1
        if map[i-j*100] == "ter" and j < 29 :
            map[i-j*100] = "ter9"
            attaquants_droite -= 1
        j += 1
    if attaquants_droite == 1 and map[i-j*100] == "ter" :
        map[i-j*100] = "ter9"

def cafe() :
    global coord_perso
    global dim_perso
    global cafe2
    global mort
    fenetre.blit(fond11,(0,0))
    perso = pygame.transform.scale(perso_dos_statique,(int(dim_perso[0]),dim_perso[1]))
    fenetre.blit(perso,(int(coord_perso[0]-dim_perso[0]/2),coord_perso[1]-dim_perso[1]))
    pygame.display.flip()
    pygame.time.wait(2000)
    fenetre.blit(fond11,(0,0))
    perso = pygame.transform.scale(perso_cafe,(int(dim_perso[0]),dim_perso[1]))
    fenetre.blit(perso,(int(coord_perso[0]-dim_perso[0]/2),coord_perso[1]-dim_perso[1]))
    pygame.display.flip()
    pygame.mixer.music.load(raccourci+"son\\Coffee.mp3")
    pygame.mixer.music.play()
    pygame.time.wait(3000)
    pygame.mixer.music.load(raccourci+"son\\Jazz_In_the_Gas.mp3")
    pygame.mixer.music.play()
    cafe2 += 1
    if cafe2 == 9 :
        mort = 6
        game_over()

def mouve_asteroide() :
    global ecran
    global coord_vaisseau
    global asteroides
    global record
    global score
    global mort
    fenetre.blit(fond_noir,(-500,-719))
    fenetre.blit(fond14,(219,0))
    fenetre.blit(vaisseau,(coord_vaisseau,496))
    fenetre.blit(texte_score,(10,10))
    for i in range (len(str(score))) :
        lettre = pygame.image.load(raccourci+"sprite\\alphabet\\"+str(score)[i]+".png").convert()
        lettre.set_colorkey((0,0,0))
        fenetre.blit(lettre,(146+i*18,10))

    for i in range (1,len(asteroides),2) :
        asteroides[i] += 5

    if asteroides[-1] >= 100 :
        asteroides += [229+randint(0,4)*110,-100]

    if asteroides[1] >= 562 :
        del asteroides[0:2]
        score += 1

    for i in range (0,len(asteroides)-1,2) :
        fenetre.blit(asteroide,(asteroides[i],asteroides[i+1]))

    i = 0
    for i in range (0,len(asteroides)-1,2) :
        if coord_vaisseau > asteroides[i] and coord_vaisseau < asteroides[i]+100 and 496 > asteroides[i+1] and 496 < asteroides[i+1]+92 or coord_vaisseau+52 > asteroides[i] and coord_vaisseau+52 < asteroides[i]+100 and 496 > asteroides[i+1] and 496 < asteroides[i+1]+92 or coord_vaisseau+52 > asteroides[i] and coord_vaisseau+52 < asteroides[i]+100 and 552 > asteroides[i+1] and 552 < asteroides[i+1]+92 or coord_vaisseau > asteroides[i] and coord_vaisseau < asteroides[i]+100 and 552 > asteroides[i+1] and 552 < asteroides[i+1]+92 :
            fenetre.blit(explosion,(coord_vaisseau+1,504))
            pygame.display.flip()
            pygame.time.wait(100)
            explosion2 = pygame.transform.scale(explosion,(60,46))
            fenetre.blit(explosion2,(coord_vaisseau-4,501))
            pygame.display.flip()
            pygame.time.wait(100)
            explosion3 = pygame.transform.scale(explosion,(70,54))
            fenetre.blit(explosion3,(coord_vaisseau-7,497))
            pygame.display.flip()
            pygame.time.wait(100)
            fenetre.blit(background_you_lose,(0,0))
            pygame.display.flip()
            pygame.time.wait(2000)
            if score > record :
                record = score
            ecran = 13
            pygame.key.set_repeat(300,100)
            change_ecran()
            break

    if score == 100 :
        for i in range (57) :
            fenetre.blit(fond_noir,(-500,-719))
            fenetre.blit(fond14,(219,0))
            fenetre.blit(vaisseau,(coord_vaisseau,496-i*10))
            fenetre.blit(texte_score,(10,10))
            for i in range (len(str(score))) :
                lettre = pygame.image.load(raccourci+"sprite\\alphabet\\"+str(score)[i]+".png").convert()
                lettre.set_colorkey((0,0,0))
                fenetre.blit(lettre,(146+i*18,10))
            pygame.display.flip()
            pygame.time.wait(40)
        pygame.key.set_repeat(300,100)
        mort = 2
        game_over()

    pygame.display.flip()

def change_ecran() :
    global ecran
    global nom
    global nom_pays
    global code
    global map
    global x
    global y
    global argent
    global nourriture
    global popularite
    global coord_perso
    global dim_perso
    global position
    global repetition
    global repetition2
    global son
    global code
    global etat_code
    global code1
    global code2
    global russell2
    global coord_info_case
    global mort
    global vitesse
    global tcarre
    global carre_im

    if not ecran == 3 :
        fenetre.blit(fond_noir,(-500,-719))

    # début
    if ecran == 0 :
        fenetre.blit(deb_background,(0,0))
        fenetre.blit(fleche3,(946,508))
        pos = 324
        for i in range (len(nom)) :
            if not nom[i] == " " :
                if not nom[i] == "0" and not nom[i] == "1" and not nom[i] == "2" and not nom[i] == "3" and not nom[i] == "4" and not nom[i] == "5" and not nom[i] == "6" and not nom[i] == "7" and not nom[i] == "8" and not nom[i] == "9" :
                    if nom[i] == nom[i].upper() :
                        lettre = pygame.image.load(raccourci+"sprite\\alphabet\\"+nom[i].lower()+"2.png").convert()
                    else :
                        lettre = pygame.image.load(raccourci+"sprite\\alphabet\\"+nom[i]+".png").convert()
                else :
                    lettre = pygame.image.load(raccourci+"sprite\\alphabet\\"+nom[i]+".png").convert()
                fenetre.blit(lettre,(pos,161))
            pos += 18
        pos = 324
        for i in range (len(nom_pays)) :
            if not nom_pays[i] == " " :
                if not nom_pays[i] == "0" and not nom_pays[i] == "1" and not nom_pays[i] == "2" and not nom_pays[i] == "3" and not nom_pays[i] == "4" and not nom_pays[i] == "5" and not nom_pays[i] == "6" and not nom_pays[i] == "7" and not nom_pays[i] == "8" and not nom_pays[i] == "9" :
                    if nom_pays[i] == nom_pays[i].upper() :
                        lettre = pygame.image.load(raccourci+"sprite\\alphabet\\"+nom_pays[i].lower+"2.png")
                    else :
                        lettre = pygame.image.load(raccourci+"sprite\\alphabet\\"+nom_pays[i]+".png")
                else :
                    lettre = pygame.image.load(raccourci+"sprite\\alphabet\\"+nom_pays[i]+".png")
                fenetre.blit(lettre,(pos,274))
                pos += 18
            else :
                pos += 18

    # menu
    elif ecran == 1 or ecran == "1b" or ecran == "1c" :
        fenetre.blit(fond,(90,0))
        fenetre.blit(titre,(140,60))
        fenetre.blit(start,(454,400))
        fenetre.blit(selection,coord_selection)
        fenetre.blit(bouton_ouvrir,(880,502))
        fenetre.blit(bouton_sauvegarder,(940,502))

        if ecran == "1b" :
            fenetre.blit(page_sauvegarde,(365,206))
        elif ecran == "1c" :
            fenetre.blit(page_sauvegarde2,(365,206))

        if ecran == "1b" or ecran == "1c" :
            sauvegarde = open(raccourci+"sauvegardes\\sauvegarde1.txt","r")
            if sauvegarde.read() == "" :
                fenetre.blit(texte_vide,(385,326))
            else :
                fenetre.blit(texte_plein,(385,326))
            sauvegarde.close()
            sauvegarde = open(raccourci+"sauvegardes\\sauvegarde2.txt","r")
            if sauvegarde.read() == "" :
                fenetre.blit(texte_vide,(475,326))
            else :
                fenetre.blit(texte_plein,(475,326))
            sauvegarde.close()
            sauvegarde = open(raccourci+"sauvegardes\\sauvegarde3.txt","r")
            if sauvegarde.read() == "" :
                fenetre.blit(texte_vide,(565,326))
            else :
                fenetre.blit(texte_plein,(565,326))
            sauvegarde.close()

    # bureau
    elif ecran == 2 :
        fenetre.blit(fond2,(0,0))
        fenetre.blit(bouton_pause,(950,10))
        fenetre.blit(pause_sur,coord_pause)
        fenetre.blit(selec_dossier,coord_dossier)
        fenetre.blit(selec_ecran,coord_ecran)
        fenetre.blit(fleche,(946,508))
        fenetre.blit(texte_se_lever,coord_texte_lever)

    # pause
    elif ecran == 3 :
        if son == 1 :
            fenetre.blit(fond_pause1,(400,81))
        else :
            fenetre.blit(fond_pause2,(400,81))
        if vitesse == 4 :
            fenetre.blit(selection_vitesse,(413,344))
        elif vitesse == 2 :
            fenetre.blit(selection_vitesse,(453,344))
        elif vitesse == 1 :
            fenetre.blit(selection_vitesse,(493,344))
        elif vitesse == 0.5 :
            fenetre.blit(selection_vitesse,(533,344))
        elif vitesse == 0.25 :
            fenetre.blit(selection_vitesse,(573,344))

    # aide
    elif ecran == "3c" :
        fenetre.blit(fond9,(100,100))

    # codes
    elif ecran == "3b" :
        fenetre.blit(fond7,(0,0))
        fenetre.blit(fleche3,(946,508))
        fenetre.blit(fleche2,(10,10))
        fenetre.blit(texte_retour,coord_retour)
        pos = 324
        for i in range (len(code)) :
            lettre = pygame.image.load(raccourci+"sprite\\alphabet\\"+code[i]+".png")
            fenetre.blit(lettre,(pos,274))
            pos += 18
        if etat_code == 1 :
            fenetre.blit(texte_code_bon,(419,312))
        elif etat_code == 2 :
            fenetre.blit(texte_code_faux,(409,312))

    # dossier
    elif ecran == 4 :
        fenetre.blit(fond3,(0,0))
        fenetre.blit(fleche2,(10,10))

        pos = 31
        for i in range (14) :
            if i == 0 :
                phrase = "Pays :"
            elif i == 1 :
                phrase = nom_pays
            elif i == 2 :
                phrase = "Nom :"
            elif i == 3 :
                phrase = nom
            elif i == 4 :
                phrase = "Popularité :"
            elif i == 5 :
                phrase = str(popularite)+"%"
            elif i == 6 :
                phrase = "Nombre de bâtiments :"
            elif i == 7 :
                total = 0
                for i in range (len(map)) :
                    if map[i][0:2] == "ta" and not map[i][2] == "r" :
                        total += 1
                phrase = str(total)
            elif i == 8 :
                phrase = "Nombre d'habitants :"
            elif i == 9 :
                total = 0
                for i in range (len(map)) :
                    if map[i][0:3] == "tam" :
                        total += int(map[i][3])
                phrase = str(total)
            elif i == 10 :
                phrase = "Revenu par jour :"
            elif i == 11 :
                total = 0
                for i in range (len(map)) :
                    if map[i][0:3] == "tau" :
                        total += 5*int(map[i][3])
                phrase = str(total)
            elif i == 12 :
                phrase = "Salaires à payer :"
            elif i == 13 :
                total = 0
                for i in range (len(map)) :
                    if map[i][0:3] == "tah" or map[i][0:3] == "tau" :
                        total += int(map[i][3])
                    elif map[i][0:3] == "tac" :
                        total += 2*int(map[i][3])
                phrase = str(total)
            for a in range (len(phrase)) :
                if not phrase[a] == " " and not phrase[a] == ":" :
                    if not phrase[a] == "0" and not phrase[a] == "1" and not phrase[a] == "2" and not phrase[a] == "3" and not phrase[a] == "4" and not phrase[a] == "5" and not phrase[a] == "6" and not phrase[a] == "7" and not phrase[a] == "8" and not phrase[a] == "9" and not phrase[a] == "," and not phrase[a] == "." and not phrase[a] == "-" and not phrase[a] == "'" and not phrase[a] == "%" :
                        if phrase[a] == phrase[a].upper() :
                            lettre = pygame.image.load(raccourci+"sprite\\alphabet\\"+phrase[a].lower()+"2.png").convert()
                        else :
                            lettre = pygame.image.load(raccourci+"sprite\\alphabet\\"+phrase[a]+".png").convert()
                    else :
                        lettre = pygame.image.load(raccourci+"sprite\\alphabet\\"+phrase[a]+".png").convert()
                    lettre.set_colorkey((0,0,0))
                    fenetre.blit(lettre,(320+a*18,pos))
                elif phrase[a] == ":" :
                    lettre = pygame.image.load(raccourci+"sprite\\alphabet\\deux_points.png").convert()
                    lettre.set_colorkey((0,0,0))
                    fenetre.blit(lettre,(320+a*18,pos))
            pos += 30

        fenetre.blit(texte_retour_bureau,coord_texte_bureau)

    # jeu
    elif ecran == 5 or ecran == 7 or ecran == 8 or ecran == "5b" :
        fenetre.blit(fond4,(0,0))

        for a in range (11) :
            for b in range (20) :
                if map[(y+a)*100+(x+b)][0] == "e" :
                    fenetre.blit(eau,(b*50,a*50+6))
                else :
                    if map[(y+a)*100+(x+b)][1] == "a" :
                        if map[(y+a)*100+(x+b)][2] == "m" :
                            fenetre.blit(maison,(b*50,a*50+6))
                        elif map[(y+a)*100+(x+b)][2] == "h" :
                            fenetre.blit(champ,(b*50,a*50+6))
                        elif map[(y+a)*100+(x+b)][2] == "u" :
                            fenetre.blit(usine,(b*50,a*50+6))
                        elif map[(y+a)*100+(x+b)][2] == "c" :
                            fenetre.blit(caserne,(b*50,a*50+6))
                        elif map[(y+a)*100+(x+b)][2] == "q" :
                            fenetre.blit(qg,(b*50,a*50+6))
                        elif map[(y+a)*100+(x+b)][2] == "r" and len(map[(y+a)*100+(x+b)]) == 3 :
                            fenetre.blit(terrain_vide,(b*50,a*50+6))
                        else :
                            soldat = pygame.image.load(raccourci+"sprite\\soldat"+map[(y+a)*100+(x+b)][3]+".png").convert()
                            fenetre.blit(soldat,(b*50,a*50+6))
                    else :
                        if map[(y+a)*100+(x+b)][2] == "m" :
                            fenetre.blit(maison2,(b*50,a*50+6))
                        elif map[(y+a)*100+(x+b)][2] == "h" :
                            fenetre.blit(champ2,(b*50,a*50+6))
                        elif map[(y+a)*100+(x+b)][2] == "u" :
                            fenetre.blit(usine2,(b*50,a*50+6))
                        elif map[(y+a)*100+(x+b)][2] == "c" :
                            fenetre.blit(caserne2,(b*50,a*50+6))
                        elif map[(y+a)*100+(x+b)][2] == "q" :
                            fenetre.blit(qg2,(b*50,a*50+6))
                        elif len(map[(y+a)*100+(x+b)]) > 3 :
                            soldat = pygame.image.load(raccourci+"sprite\\soldat"+map[(y+a)*100+(x+b)][3]+".png").convert()
                            soldat.set_colorkey((255,127,39))
                            fenetre.blit(soldat,(b*50,a*50+6))

        fenetre.blit(bouton_magasin,(857,512))
        fenetre.blit(magasin_sur,coord_magasin)
        fenetre.blit(bouton_supprimer,(813,512))
        fenetre.blit(supprimer_sur,coord_supprimer)
        fenetre.blit(fleche2,(10,16))
        fenetre.blit(texte_retour_bureau,coord_texte_bureau)
        fenetre.blit(mouv_ecran_haut,coord_mouv_haut)
        fenetre.blit(mouv_ecran_bas,coord_mouv_bas)
        fenetre.blit(mouv_ecran_gauche,coord_mouv_gauche)
        fenetre.blit(mouv_ecran_droite,coord_mouv_droite)

        fenetre.blit(piece,(974,20))
        for i in range (len(str(argent))) :
            lettre = pygame.image.load(raccourci+"sprite\\alphabet\\"+str(argent)[i]+".png").convert()
            lettre.set_colorkey((0,0,0))
            fenetre.blit(lettre,(951-len(str(argent))*18+18*(i+1),18))

        fenetre.blit(carotte,(974,50))
        for i in range (len(str(nourriture))) :
            lettre = pygame.image.load(raccourci+"sprite\\alphabet\\"+str(nourriture)[i]+".png").convert()
            lettre.set_colorkey((0,0,0))
            fenetre.blit(lettre,(951-len(str(nourriture))*18+18*(i+1),48))

        fenetre.blit(tete_habitant,(974,80))
        total = 0
        for i in range (len(map)) :
            if len(map[i]) > 3 and map[i][0:2] == "ta" :
                if map[i][2] == "m" :
                    total += int(map[i][3])
        for i in range (len(str(total))) :
            lettre = pygame.image.load(raccourci+"sprite\\alphabet\\"+str(total)[i]+".png").convert()
            lettre.set_colorkey((0,0,0))
            fenetre.blit(lettre,(951-len(str(total))*18+18*(i+1),78))

        fenetre.blit(pouce,(974,110))
        phrase = str(popularite)+"%"
        for i in range (len(phrase)) :
            lettre = pygame.image.load(raccourci+"sprite\\alphabet\\"+phrase[i]+".png").convert()
            lettre.set_colorkey((0,0,0))
            fenetre.blit(lettre,(951-len(phrase)*18+18*(i+1),108))

        fenetre.blit(calendrier,(974,140))
        phrase = str(date[0])+"/"+str(date[1])+"/"+str(date[2])
        if len(str(date[1])) == 1 :
            phrase = phrase[0:len(str(date[0]))+1]+"0"+phrase[len(str(date[0]))+1:len(phrase)]
        if len(str(date[0])) == 1 :
            phrase = "0"+phrase
        for i in range (10) :
            if not phrase[i] == "/" :
                lettre = pygame.image.load(raccourci+"sprite\\alphabet\\"+phrase[i]+".png").convert()
            else :
                lettre = pygame.image.load(raccourci+"sprite\\alphabet\\slash.png").convert()
            lettre.set_colorkey((0,0,0))
            fenetre.blit(lettre,(951-len(phrase)*18+18*(i+1),138))

        if ecran == 5 :
            if not map[(y+int((coord_info_case[1]-6)/50))*100+x+int(coord_info_case[0]/50)] == "e" :
                if map[(y+int((coord_info_case[1]-6)/50))*100+x+int(coord_info_case[0]/50)][0:2] == "ta" and not map[(y+int((coord_info_case[1]-6)/50))*100+x+int(coord_info_case[0]/50)][2] == "q" and not map[(y+int((coord_info_case[1]-6)/50))*100+x+int(coord_info_case[0]/50)][2] == "r" :
                    if map[(y+int((coord_info_case[1]-6)/50))*100+x+int(coord_info_case[0]/50)][2] == "c" :
                        info = map[(y+int((coord_info_case[1]-6)/50))*100+x+int(coord_info_case[0]/50)][3]+"9"
                    else :
                        info = map[(y+int((coord_info_case[1]-6)/50))*100+x+int(coord_info_case[0]/50)][3]+"4"
                    lettre = pygame.image.load(raccourci+"sprite\\alphabet\\"+info[0]+".png").convert()
                    lettre.set_colorkey((0,0,0))
                    fenetre.blit(lettre,(coord_info_case[0]-2,coord_info_case[1]+12))
                    lettre = pygame.image.load(raccourci+"sprite\\alphabet\\slash.png").convert()
                    lettre.set_colorkey((0,0,0))
                    fenetre.blit(lettre,(coord_info_case[0]+16,coord_info_case[1]+12))
                    lettre = pygame.image.load(raccourci+"sprite\\alphabet\\"+info[1]+".png").convert()
                    lettre.set_colorkey((0,0,0))
                    fenetre.blit(lettre,(coord_info_case[0]+34,coord_info_case[1]+12))

        if ecran == 7 or ecran == 8 :
            fenetre.blit(selection_supprimer,coord_selection_supprimer)
        elif ecran == "5b" :
            fenetre.blit(selection_deplacement,coord_selection_supprimer)

        if vitesse == 4 :
            a = 16
        elif vitesse == 2 :
            a = 8
        elif vitesse == 1 :
            a = 4
        elif vitesse == 0.5 :
            a = 2
        elif vitesse == 0.25 :
            a = 1

        tcarre += 1
        if tcarre > a :
            tcarre = 0
        if tcarre == a :
            carre_im += 1
            if carre_im == 17 :
                carre_im = 1

        carre = pygame.image.load(raccourci+"sprite\\carre\\carre"+str(carre_im)+".png").convert()
        fenetre.blit(carre,(10,526))

    # magasin
    elif ecran == 6 :
        fenetre.blit(fond5,(0,0))
        fenetre.blit(fleche2,(10,508))
        fenetre.blit(texte_retour,coord_retour)

    # bureau pièce
    elif ecran == 9 :
        fenetre.blit(fond6,(0,0))

        if repetition == 0 :
            if position == 2 or position == 3 :
                position = 1
            elif position == 5 or position == 6 :
                position == 4
            elif position == 8 or position == 9 :
                position = 7
            elif position == 11 or position == 12 :
                position = 10

        perso = pygame.transform.scale(conseille,(int(54+(9/17)),102))
        fenetre.blit(perso,(826,72))

        if repetition2 == 20 :
            fenetre.blit(fenetre_casse1,(42,9))

        if position == 1 or position == 13 :
            perso = pygame.transform.scale(perso_face_statique,(int(dim_perso[0]),dim_perso[1]))
        elif position == 2 :
            perso = pygame.transform.scale(perso_face_marche1,(int(dim_perso[0]),dim_perso[1]))
        elif position == 3 :
            perso = pygame.transform.scale(perso_face_marche2,(int(dim_perso[0]),dim_perso[1]))
        elif position == 4 or position == 14 :
            perso = pygame.transform.scale(perso_dos_statique,(int(dim_perso[0]),dim_perso[1]))
        elif position == 5 :
            perso = pygame.transform.scale(perso_dos_marche1,(int(dim_perso[0]),dim_perso[1]))
        elif position == 6 :
            perso = pygame.transform.scale(perso_dos_marche2,(int(dim_perso[0]),dim_perso[1]))
        elif position == 7 or position == 15 :
            perso = pygame.transform.scale(perso_gauche_statique,(int(dim_perso[0]),dim_perso[1]))
        elif position == 8 :
            perso = pygame.transform.scale(perso_gauche_marche1,(int(dim_perso[0]),dim_perso[1]))
        elif position == 9 :
            perso = pygame.transform.scale(perso_gauche_marche2,(int(dim_perso[0]),dim_perso[1]))
        elif position == 10 or position == 16 :
            perso = pygame.transform.scale(perso_droite_statique,(int(dim_perso[0]),dim_perso[1]))
        elif position == 11 :
            perso = pygame.transform.scale(perso_droite_marche1,(int(dim_perso[0]),dim_perso[1]))
        elif position == 12 :
            perso = pygame.transform.scale(perso_droite_marche2,(int(dim_perso[0]),dim_perso[1]))

        fenetre.blit(perso,(int(coord_perso[0]-dim_perso[0]/2),coord_perso[1]-dim_perso[1]))

        if coord_perso[1] < 503 :
            fenetre.blit(presentoir,(9,357))
        if coord_perso[1] < 343 :
            fenetre.blit(table,(306,159))
            fenetre.blit(sac_or,(71,224))
        if coord_perso[1] == 174 and coord_perso[0] > 185 and coord_perso[0] < 290 :
            fenetre.blit(texte_regarder,(175,0))
        elif coord_perso[1] == 414 and coord_perso[0] > 284 and coord_perso[0] < 804 or coord_perso[1] == 342 and coord_perso[0] > 284 and coord_perso[0] < 804 or coord_perso[0] == 804 and coord_perso[1] > 342 and coord_perso[1] < 414 or coord_perso[0] == 284 and coord_perso[1] > 342 and coord_perso[1] < 414 :
            fenetre.blit(texte_asseoir,(463,130))
        elif coord_perso[1] == 174 and coord_perso[0] > 905 and coord_perso[0] < 987 :
            fenetre.blit(texte_sortir,(894,0))
        elif coord_perso[1] == 174 and coord_perso[0] > 826 and coord_perso[0] < 880 :
            fenetre.blit(texte_parler,(800,25))
        fenetre.blit(panneau,coord_panneau)

        if repetition2 == 20 :
            fenetre.blit(fenetre_casse2,(42,9))
            pygame.display.flip()
            pygame.time.wait(300)
            fenetre.blit(fenetre_casse1,(42,9))
            pygame.display.flip()
            pygame.time.wait(500)
            mort = 1
            game_over()

    # couloir
    elif ecran == 10 :
        fenetre.blit(fond8,(0,0))
        fenetre.blit(russell,(380,33))
        if code1 == 0 :
            fenetre.blit(bouton_non,(452,512))
        elif code1 == 1 :
            fenetre.blit(bouton_non,(384,512))
            fenetre.blit(bouton_oui,(531,512))
        fenetre.blit(selection,coord_selection)
        pos = 366
        for i in range (4) :
            if i == 0 :
                phrase = "Bonjour madame monsieur, je m'appelle Russell, et"
            elif i == 1 :
                phrase = "je suis un explorateur de la tribu des wapitis"
            elif i == 2 :
                phrase = "section 54 12e campement. Est-ce que je peux faire"
            elif i == 3 :
                phrase = "quelque chose pour vous aidez ?"
            for a in range (len(phrase)) :
                if not phrase[a] == " " and not phrase[a] == ":" and not phrase[a] == "?" :
                    if not phrase[a] == "0" and not phrase[a] == "1" and not phrase[a] == "2" and not phrase[a] == "3" and not phrase[a] == "4" and not phrase[a] == "5" and not phrase[a] == "6" and not phrase[a] == "7" and not phrase[a] == "8" and not phrase[a] == "9" and not phrase[a] == "," and not phrase[a] == "." and not phrase[a] == "-" and not phrase[a] == "'" and not phrase[a] == "%" :
                        if phrase[a] == phrase[a].upper() :
                            lettre = pygame.image.load(raccourci+"sprite\\alphabet\\"+phrase[a].lower()+"2.png").convert()
                        else :
                            lettre = pygame.image.load(raccourci+"sprite\\alphabet\\"+phrase[a]+".png").convert()
                    else :
                        lettre = pygame.image.load(raccourci+"sprite\\alphabet\\"+phrase[a]+".png").convert()
                    lettre.set_colorkey((0,0,0))
                    fenetre.blit(lettre,(50+a*18,pos))
                elif phrase[a] == ":" :
                    lettre = pygame.image.load(raccourci+"sprite\\alphabet\\deux_points.png").convert()
                    lettre.set_colorkey((0,0,0))
                    fenetre.blit(lettre,(50+a*18,pos))
                elif phrase[a] == "?" :
                    lettre = pygame.image.load(raccourci+"sprite\\alphabet\\point_interrogation.png").convert()
                    lettre.set_colorkey((0,0,0))
                    fenetre.blit(lettre,(50+a*18,pos))
            pos += 30

    # couloir 2
    elif ecran == 11 :
        fenetre.blit(fond10,(0,0))

        if repetition == 0 :
            if position == 2 or position == 3 :
                position = 1
            elif position == 5 or position == 6 :
                position == 4
            elif position == 8 or position == 9 :
                position = 7
            elif position == 11 or position == 12 :
                position = 10

        if position == 1 or position == 13 :
            perso = pygame.transform.scale(perso_face_statique,(int(dim_perso[0]),dim_perso[1]))
        elif position == 2 :
            perso = pygame.transform.scale(perso_face_marche1,(int(dim_perso[0]),dim_perso[1]))
        elif position == 3 :
            perso = pygame.transform.scale(perso_face_marche2,(int(dim_perso[0]),dim_perso[1]))
        elif position == 4 or position == 14 :
            perso = pygame.transform.scale(perso_dos_statique,(int(dim_perso[0]),dim_perso[1]))
        elif position == 5 :
            perso = pygame.transform.scale(perso_dos_marche1,(int(dim_perso[0]),dim_perso[1]))
        elif position == 6 :
            perso = pygame.transform.scale(perso_dos_marche2,(int(dim_perso[0]),dim_perso[1]))
        elif position == 7 or position == 15 :
            perso = pygame.transform.scale(perso_gauche_statique,(int(dim_perso[0]),dim_perso[1]))
        elif position == 8 :
            perso = pygame.transform.scale(perso_gauche_marche1,(int(dim_perso[0]),dim_perso[1]))
        elif position == 9 :
            perso = pygame.transform.scale(perso_gauche_marche2,(int(dim_perso[0]),dim_perso[1]))
        elif position == 10 or position == 16 :
            perso = pygame.transform.scale(perso_droite_statique,(int(dim_perso[0]),dim_perso[1]))
        elif position == 11 :
            perso = pygame.transform.scale(perso_droite_marche1,(int(dim_perso[0]),dim_perso[1]))
        elif position == 12 :
            perso = pygame.transform.scale(perso_droite_marche2,(int(dim_perso[0]),dim_perso[1]))

        fenetre.blit(perso,(int(coord_perso[0]-dim_perso[0]/2),coord_perso[1]-dim_perso[1]))

        if coord_perso[1] == 418 and coord_perso[0] > 43 and coord_perso[0] < 169 :
            fenetre.blit(texte_entrer,(53,156))
        elif coord_perso[1] == 418 and coord_perso[0] > 404 and coord_perso[0] < 530 :
            fenetre.blit(texte_entrer,(414,156))
        elif coord_perso[1] == 418 and coord_perso[0] > 752 and coord_perso[0] < 878 :
            fenetre.blit(texte_entrer,(762,156))

    # salle d'arcade
    elif ecran == 12 :
        fenetre.blit(fond11,(0,0))

        if repetition == 0 :
            if position == 2 or position == 3 :
                position = 1
            elif position == 5 or position == 6 :
                position == 4
            elif position == 8 or position == 9 :
                position = 7
            elif position == 11 or position == 12 :
                position = 10

        if position == 1 or position == 13 :
            perso = pygame.transform.scale(perso_face_statique,(int(dim_perso[0]),dim_perso[1]))
        elif position == 2 :
            perso = pygame.transform.scale(perso_face_marche1,(int(dim_perso[0]),dim_perso[1]))
        elif position == 3 :
            perso = pygame.transform.scale(perso_face_marche2,(int(dim_perso[0]),dim_perso[1]))
        elif position == 4 or position == 14 :
            perso = pygame.transform.scale(perso_dos_statique,(int(dim_perso[0]),dim_perso[1]))
        elif position == 5 :
            perso = pygame.transform.scale(perso_dos_marche1,(int(dim_perso[0]),dim_perso[1]))
        elif position == 6 :
            perso = pygame.transform.scale(perso_dos_marche2,(int(dim_perso[0]),dim_perso[1]))
        elif position == 7 or position == 15 :
            perso = pygame.transform.scale(perso_gauche_statique,(int(dim_perso[0]),dim_perso[1]))
        elif position == 8 :
            perso = pygame.transform.scale(perso_gauche_marche1,(int(dim_perso[0]),dim_perso[1]))
        elif position == 9 :
            perso = pygame.transform.scale(perso_gauche_marche2,(int(dim_perso[0]),dim_perso[1]))
        elif position == 10 or position == 16 :
            perso = pygame.transform.scale(perso_droite_statique,(int(dim_perso[0]),dim_perso[1]))
        elif position == 11 :
            perso = pygame.transform.scale(perso_droite_marche1,(int(dim_perso[0]),dim_perso[1]))
        elif position == 12 :
            perso = pygame.transform.scale(perso_droite_marche2,(int(dim_perso[0]),dim_perso[1]))

        fenetre.blit(perso,(int(coord_perso[0]-dim_perso[0]/2),coord_perso[1]-dim_perso[1]))

        if coord_perso[1] <= 310 :
            fenetre.blit(canape_rouge,(385,253))
        if coord_perso[1] <= 510 :
            fenetre.blit(plante,(879,358))
        if coord_perso[1] == 174 and coord_perso[0] > 23 and coord_perso[0] < 109 :
            fenetre.blit(texte_sortir,(13,10))
        elif coord_perso[1] == 182 and coord_perso[0] > 441 and coord_perso[0] < 512 :
            fenetre.blit(texte_utiliser,(414,10))
        elif coord_perso[1] == 182 and coord_perso[0] > 778 and coord_perso[0] < 848 :
            fenetre.blit(texte_utiliser,(750,10))

    # mini-jeu menu
    elif ecran == 13 :
        if code2 == 0 :
            fenetre.blit(fond12,(0,0))
        else :
            fenetre.blit(fond13,(219,0))

            for i in range (len(str(record))) :
                lettre = pygame.image.load(raccourci+"sprite\\alphabet\\"+str(record)[i]+".png").convert()
                lettre.set_colorkey((0,0,0))
                fenetre.blit(lettre,(507+18*i,232))

            fenetre.blit(selection,coord_selection)

    # mini-jeu jeu
    elif ecran == 14 :
        fenetre.blit(fond14,(219,0))
        fenetre.blit(vaisseau,(coord_vaisseau,496))

    pygame.display.flip()

pygame.init()

raccourci = __file__
raccourci = raccourci[0:-8]

# fenêtre
fenetre = pygame.display.set_mode((1000,562))
pygame.display.set_caption("Dictatoria")

icone = pygame.image.load(raccourci+"sprite\\icone.png")
pygame.display.set_icon(icone)

# sprite
fond_noir = pygame.image.load(raccourci+"sprite\\fond_noir.png").convert()

# game over
gameover_background = pygame.image.load(raccourci+"sprite\\game_over.png").convert()
gameover1_background = pygame.image.load(raccourci+"sprite\\gameover1_background.png").convert()

# deb
deb_background = pygame.image.load(raccourci+"sprite\\deb_background.png").convert()

fleche3 = pygame.image.load(raccourci+"sprite\\flèche3.png").convert()
fleche3.set_colorkey((0,0,0))

# menu
fond = pygame.image.load(raccourci+"sprite\\menu_background.png").convert()

titre = pygame.image.load(raccourci+"sprite\\titre.png").convert()
titre.set_colorkey((255,255,255))

start = pygame.image.load(raccourci+"sprite\\start.png").convert()
start.set_colorkey((0,0,0))

selection = pygame.image.load(raccourci+"sprite\\selection.png").convert()
selection.set_colorkey((0,0,0))
coord_selection = (1000,400)

bouton_ouvrir = pygame.image.load(raccourci+"sprite\\bouton_ouvrir.png").convert()
bouton_sauvegarder = pygame.image.load(raccourci+"sprite\\bouton_sauvegarder.png").convert()

# sauvegarde
page_sauvegarde = pygame.image.load(raccourci+"sprite\\page_sauvegarde.png").convert()

page_sauvegarde2 = pygame.image.load(raccourci+"sprite\\page_sauvegarde2.png").convert()

texte_vide = pygame.image.load(raccourci+"sprite\\texte_vide.png").convert()
texte_vide.set_colorkey((0,0,0))

texte_plein = pygame.image.load(raccourci+"sprite\\texte_plein.png").convert()
texte_plein.set_colorkey((0,0,0))

# bureau
fond2 = pygame.image.load(raccourci+"sprite\\bureau.png").convert()

bouton_pause = pygame.image.load(raccourci+"sprite\\pause.png").convert()

pause_sur = pygame.image.load(raccourci+"sprite\\pause_sur.png").convert()
pause_sur.set_colorkey((0,0,0))
coord_pause = (1000,10)

selec_dossier = pygame.image.load(raccourci+"sprite\\selec_dossier.png").convert()
selec_dossier.set_colorkey((255,255,255))
coord_dossier = (1000,126)

selec_ecran = pygame.image.load(raccourci+"sprite\\selec_ecran.png").convert()
selec_ecran.set_colorkey((255,255,255))
coord_ecran = (216,145)

fleche = pygame.image.load(raccourci+"sprite\\flèche.png").convert()

texte_se_lever = pygame.image.load(raccourci+"sprite\\texte_se_lever.png").convert()
texte_se_lever.set_colorkey((255,255,255))
coord_texte_lever = (1000,518)

# pause
fond_pause1 = pygame.image.load(raccourci+"sprite\\fond_pause1.png").convert()
fond_pause2 = pygame.image.load(raccourci+"sprite\\fond_pause2.png").convert()

selection_vitesse = pygame.image.load(raccourci+"sprite\\selection_vitesse.png").convert()
selection_vitesse.set_colorkey((0,0,0))

# codes
fond7 = pygame.image.load(raccourci+"sprite\\codes_background.png").convert()

texte_code_bon = pygame.image.load(raccourci+"sprite\\texte_code_bon.png").convert()

texte_code_faux = pygame.image.load(raccourci+"sprite\\texte_code_faux.png").convert()

# aide
fond9 = pygame.image.load(raccourci+"sprite\\aide_background.png").convert()

# dossier
fond3 = pygame.image.load(raccourci+"sprite\\dossier_background.png").convert()

# jeu
fond4 = pygame.image.load(raccourci+"sprite\\jeu_background.png").convert()

fleche2 = pygame.image.load(raccourci+"sprite\\flèche2.png").convert()

texte_retour_bureau = pygame.image.load(raccourci+"sprite\\texte_retour_bureau.png").convert()
texte_retour_bureau.set_colorkey((255,255,255))
coord_texte_bureau = (1000,20)

bouton_magasin = pygame.image.load(raccourci+"sprite\\bouton_magasin.png").convert()

magasin_sur = pygame.image.load(raccourci+"sprite\\bouton_magasin_sur.png").convert()
magasin_sur.set_colorkey((0,0,0))
coord_magasin = (1000,512)

bouton_supprimer = pygame.image.load(raccourci+"sprite\\bouton_supprimer.png").convert()

supprimer_sur = pygame.image.load(raccourci+"sprite\\bouton_supprimer_sur.png").convert()
supprimer_sur.set_colorkey((0,0,0))
coord_supprimer = (813,512)

selection_supprimer = pygame.image.load(raccourci+"sprite\\selection_supprimer.png").convert()
selection_supprimer.set_colorkey((255,255,255))

selection_deplacement = pygame.image.load(raccourci+"sprite\\selection_déplacement.png").convert()
selection_deplacement.set_colorkey((255,255,255))

piece = pygame.image.load(raccourci+"sprite\\piece.png").convert()
piece.set_colorkey((255,255,255))

carotte = pygame.image.load(raccourci+"sprite\\nourriture.png").convert()
carotte.set_colorkey((255,255,255))

tete_habitant = pygame.image.load(raccourci+"sprite\\habitant.png").convert()
tete_habitant.set_colorkey((255,255,255))

pouce = pygame.image.load(raccourci+"sprite\\pouce.png").convert()
pouce.set_colorkey((255,255,255))

calendrier = pygame.image.load(raccourci+"sprite\\calendrier.png").convert()

mouv_ecran_haut = pygame.image.load(raccourci+"sprite\\mouv_ecran_haut.png").convert()
mouv_ecran_haut.set_colorkey((255,255,255))
coord_mouv_haut = (1000,6)
mouv_ecran_bas = pygame.image.load(raccourci+"sprite\\mouv_ecran_bas.png").convert()
mouv_ecran_bas.set_colorkey((255,255,255))
coord_mouv_bas = (1000,516)
mouv_ecran_gauche = pygame.image.load(raccourci+"sprite\\mouv_ecran_gauche.png").convert()
mouv_ecran_gauche.set_colorkey((255,255,255))
coord_mouv_gauche = (1000,231)
mouv_ecran_droite = pygame.image.load(raccourci+"sprite\\mouv_ecran_droite.png").convert()
mouv_ecran_droite.set_colorkey((255,255,255))
coord_mouv_droite = (1000,231)

eau = pygame.image.load(raccourci+"sprite\\eau.png").convert()

maison = pygame.image.load(raccourci+"sprite\\maison.png").convert()
champ = pygame.image.load(raccourci+"sprite\\champ.png").convert()
usine = pygame.image.load(raccourci+"sprite\\usine.png").convert()
caserne = pygame.image.load(raccourci+"sprite\\caserne.png").convert()
qg = pygame.image.load(raccourci+"sprite\\qg.png").convert()
terrain_vide = pygame.image.load(raccourci+"sprite\\terrain_vide.png").convert()

maison2 = pygame.image.load(raccourci+"sprite\\maison.png").convert()
maison2.set_colorkey((255,127,39))
champ2 = pygame.image.load(raccourci+"sprite\\champ.png").convert()
champ2.set_colorkey((255,127,39))
usine2 = pygame.image.load(raccourci+"sprite\\usine.png").convert()
usine2.set_colorkey((255,127,39))
caserne2 = pygame.image.load(raccourci+"sprite\\caserne.png").convert()
caserne2.set_colorkey((255,127,39))
qg2 = pygame.image.load(raccourci+"sprite\\qg.png").convert()
qg2.set_colorkey((255,127,39))

# magasin
fond5 = pygame.image.load(raccourci+"sprite\\magasin_background.png").convert()

texte_retour = pygame.image.load(raccourci+"sprite\\texte_retour.png").convert()
texte_retour.set_colorkey((255,255,255))
coord_retour = (1000,508)

# bureau pièce
fond6 = pygame.image.load(raccourci+"sprite\\background_bureau.png").convert()

table = pygame.image.load(raccourci+"sprite\\table.png").convert()
table.set_colorkey((255,255,255))

sac_or = pygame.image.load(raccourci+"sprite\\sac_or.png").convert()
sac_or.set_colorkey((255,255,255))

presentoir = pygame.image.load(raccourci+"sprite\\présentoir.png").convert()
presentoir.set_colorkey((255,255,255))

panneau = pygame.image.load(raccourci+"sprite\\panneau.png").convert()
coord_panneau = (1000,118)

fenetre_casse1 = pygame.image.load(raccourci+"sprite\\fenêtre_cassée.png").convert()
fenetre_casse2 = pygame.image.load(raccourci+"sprite\\fenêtre_cassée.png").convert()
fenetre_casse2.set_colorkey((0,162,232))

texte_regarder = pygame.image.load(raccourci+"sprite\\texte_regarder.png").convert()
texte_regarder.set_colorkey((0,0,0))

texte_asseoir = pygame.image.load(raccourci+"sprite\\texte_asseoir.png").convert()
texte_asseoir.set_colorkey((0,0,0))

texte_sortir = pygame.image.load(raccourci+"sprite\\texte_sortir.png").convert()
texte_sortir.set_colorkey((0,0,0))

texte_parler = pygame.image.load(raccourci+"sprite\\texte_parler.png").convert()
texte_parler.set_colorkey((0,0,0))

perso_face_statique = pygame.image.load(raccourci+"sprite\\perso\\perso_face_statique.png").convert()
perso_face_statique.set_colorkey((255,255,255))
perso_face_marche1 = pygame.image.load(raccourci+"sprite\\perso\\perso_face_marche1.png").convert()
perso_face_marche1.set_colorkey((255,255,255))
perso_face_marche2 = pygame.image.load(raccourci+"sprite\\perso\\perso_face_marche2.png").convert()
perso_face_marche2.set_colorkey((255,255,255))

perso_dos_statique = pygame.image.load(raccourci+"sprite\\perso\\perso_dos_statique.png").convert()
perso_dos_statique.set_colorkey((255,255,255))
perso_dos_marche1 = pygame.image.load(raccourci+"sprite\\perso\\perso_dos_marche1.png").convert()
perso_dos_marche1.set_colorkey((255,255,255))
perso_dos_marche2 = pygame.image.load(raccourci+"sprite\\perso\\perso_dos_marche2.png").convert()
perso_dos_marche2.set_colorkey((255,255,255))

perso_gauche_statique = pygame.image.load(raccourci+"sprite\\perso\\perso_gauche_statique.png").convert()
perso_gauche_statique.set_colorkey((255,255,255))
perso_gauche_marche1 = pygame.image.load(raccourci+"sprite\\perso\\perso_gauche_marche1.png").convert()
perso_gauche_marche1.set_colorkey((255,255,255))
perso_gauche_marche2 = pygame.image.load(raccourci+"sprite\\perso\\perso_gauche_marche2.png").convert()
perso_gauche_marche2.set_colorkey((255,255,255))

perso_droite_statique = pygame.image.load(raccourci+"sprite\\perso\\perso_droite_statique.png").convert()
perso_droite_statique.set_colorkey((255,255,255))
perso_droite_marche1 = pygame.image.load(raccourci+"sprite\\perso\\perso_droite_marche1.png").convert()
perso_droite_marche1.set_colorkey((255,255,255))
perso_droite_marche2 = pygame.image.load(raccourci+"sprite\\perso\\perso_droite_marche2.png").convert()
perso_droite_marche2.set_colorkey((255,255,255))

conseille = pygame.image.load(raccourci+"sprite\\perso\\conseillé.png").convert()
conseille.set_colorkey((255,255,255))

conseil1 = pygame.image.load(raccourci+"sprite\\conseil1.png").convert()
conseil1.set_colorkey((127,127,127))
conseil2 = pygame.image.load(raccourci+"sprite\\conseil2.png").convert()
conseil2.set_colorkey((127,127,127))
conseil3 = pygame.image.load(raccourci+"sprite\\conseil3.png").convert()
conseil3.set_colorkey((127,127,127))
conseil4 = pygame.image.load(raccourci+"sprite\\conseil4.png").convert()
conseil4.set_colorkey((127,127,127))
conseil5 = pygame.image.load(raccourci+"sprite\\conseil5.png").convert()
conseil5.set_colorkey((127,127,127))

# couloir
fond8 = pygame.image.load(raccourci+"sprite\\couloir_background.png").convert()

russell = pygame.image.load(raccourci+"sprite\\russell.png").convert()
russell.set_colorkey((255,255,255))

bouton_non = pygame.image.load(raccourci+"sprite\\non.png").convert()

bouton_oui = pygame.image.load(raccourci+"sprite\\oui.png").convert()

# couloir 2
fond10 = pygame.image.load(raccourci+"sprite\\couloir2_background.png").convert()

texte_entrer = pygame.image.load(raccourci+"sprite\\texte_entrer.png").convert()
texte_entrer.set_colorkey((0,0,0))

bulle = pygame.image.load(raccourci+"sprite\\bulle.png").convert()
bulle.set_colorkey((127,127,127))

# salle d'arcade
fond11 = pygame.image.load(raccourci+"sprite\\background_salle_arcade.png").convert()

canape_rouge = pygame.image.load(raccourci+"sprite\\canapé_rouge.png").convert()
canape_rouge.set_colorkey((255,255,255))

plante = pygame.image.load(raccourci+"sprite\\plante.png").convert()
plante.set_colorkey((255,255,255))

texte_utiliser = pygame.image.load(raccourci+"sprite\\texte_utiliser.png").convert()
texte_utiliser.set_colorkey((0,0,0))

perso_cafe = pygame.image.load(raccourci+"sprite\\perso\\perso_cafe.png").convert()
perso_cafe.set_colorkey((255,255,255))

# mini-jeu
fond12 = pygame.image.load(raccourci+"sprite\\background_code_requit.png").convert()

fond13 = pygame.image.load(raccourci+"sprite\\background_minijeu.png").convert()

fond14 = pygame.image.load(raccourci+"sprite\\espace.png").convert()

background_you_lose = pygame.image.load(raccourci+"sprite\\background_you_lose.png").convert()

vaisseau = pygame.image.load(raccourci+"sprite\\vaisseau.png").convert()
vaisseau.set_colorkey((255,255,255))

asteroide = pygame.image.load(raccourci+"sprite\\astéroïde.png").convert()
asteroide.set_colorkey((255,255,255))

explosion = pygame.image.load(raccourci+"sprite\\explosion.png").convert()
explosion.set_colorkey((0,0,0))

texte_score = pygame.image.load(raccourci+"sprite\\texte_score.png").convert()
texte_score.set_colorkey((0,0,0))

alphabet_qwerty = "1234567890qwertyuiopasdfghjkl;zxcvbnm "
alphabet_azerty = "1234567890azertyuiopqsdfghjklmwxcvbn, "

initialisation()
change_ecran()

son = 1
pygame.mixer.music.set_volume(1)
pygame.mixer.music.load(raccourci+"son\\play.mp3")
pygame.mixer.music.play()

pygame.key.set_repeat(300,100)

b = 1
while b == 1 :
    for event in pygame.event.get() :
        if pygame.mixer.music.get_busy() == False :
                if ecran == 1 :
                    pygame.mixer.music.load(raccourci+"son\\infire_theme.mp3")
                elif ecran == 2 or ecran == 3 or ecran == 4 :
                    pygame.mixer.music.load(raccourci+"son\\harpe.mp3")
                elif ecran == 5 or ecran == 7 or ecran == 8 :
                    pygame.mixer.music.load(raccourci+"son\\Country_Control.mp3")
                elif ecran == 6 :
                    pygame.mixer.music.load(raccourci+"son\\shop.mp3")
                elif ecran == 9 or ecran == 10 or ecran == 11 or ecran == 12 :
                    pygame.mixer.music.load(raccourci+"son\\Jazz_In_the_Gas.mp3")
                elif ecran == 13 or ecran == 14 :
                    pygame.mixer.music.load(raccourci+"son\\Highscore14.mp3")
                if not ecran == 0 :
                    pygame.mixer.music.play()

        if event.type == QUIT :
            b = 0
            pygame.quit()

        elif event.type == MOUSEMOTION :
            if ecran == 1 :
                if event.pos[0] > 430 and event.pos[0] < 570 and event.pos[1] > 400 and event.pos[1] < 436 :
                    coord_selection = (430,400)
                else :
                    coord_selection = (1000,400)

            elif ecran == 2 :
                if event.pos[0] > 950 and event.pos[0] < 990 and event.pos[1] > 10 and event.pos[1] < 50 :
                    coord_pause = (950,10)
                else :
                    coord_pause = (1000,10)
                if event.pos[0] > 808 and event.pos[0] < 1000 and event.pos[1] > 130 and event.pos[1] < 274 :
                    coord_dossier = (760,126)
                else :
                    coord_dossier = (1000,126)
                if event.pos[0] > 216 and event.pos[0] < 585 and event.pos[1] > 145 and event.pos[1] < 328 :
                    coord_ecran = (216,145)
                else :
                    coord_ecran = (1000,145)
                if event.pos[0] > 946 and event.pos[0] < 990 and event.pos[1] > 508 and event.pos[1] < 552 :
                    coord_texte_lever = (723,508)
                else :
                    coord_texte_lever = (1000,508)

            elif ecran == "3b" :
                if event.pos[0] > 10 and event.pos[0] < 54 and event.pos[1] > 10 and event.pos[1] < 54 :
                    coord_retour = (64,10)
                else :
                    coord_retour = (1000,10)

            elif ecran == 4 :
                if event.pos[0] > 10 and event.pos[0] < 54 and event.pos[1] > 10 and event.pos[1] < 54 :
                    coord_texte_bureau = (64,14)
                else :
                    coord_texte_bureau = (1000,14)

            elif ecran == 5 :
                if event.pos[0] > 10 and event.pos[0] < 54 and event.pos[1] > 16 and event.pos[1] < 60 :
                    coord_texte_bureau = (64,20)
                else :
                    coord_texte_bureau = (1000,20)
                if event.pos[0] > 857 and event.pos[0] < 990 and event.pos[1] > 512 and event.pos[1] < 546 :
                    coord_magasin = (857,512)
                else :
                    coord_magasin = (1000,512)
                if event.pos[0] > 813 and event.pos[0] < 847 and event.pos[1] > 512 and event.pos[1] < 546 :
                    coord_supprimer = (813,512)
                else :
                    coord_supprimer = (1000,512)
                if event.pos[0] > 54 and event.pos[0] < 1000 and event.pos[1] > 6 and event.pos[1] < 46 :
                    coord_mouv_haut = (450,6)
                else :
                    coord_mouv_haut = (1000,6)
                if event.pos[0] > 0 and event.pos[0] < 813 and event.pos[1] > 516 and event.pos[1] < 556 :
                    coord_mouv_bas = (450,516)
                else :
                    coord_mouv_bas = (1000,516)
                if event.pos[0] > 0 and event.pos[0] < 40 and event.pos[1] > 60 and event.pos[1] < 556 :
                    coord_mouv_gauche = (0,231)
                else :
                    coord_mouv_gauche = (1000,231)
                if event.pos[0] > 960 and event.pos[0] < 1000 and event.pos[1] > 0 and event.pos[1] < 512 :
                    coord_mouv_droite = (960,231)
                else :
                    coord_mouv_droite = (1000,231)

                coord_info_case = ((event.pos[0]//50)*50,((event.pos[1]-6)//50)*50+6)

            elif ecran == 6 :
                if event.pos[0] > 10 and event.pos[0] < 54 and event.pos[1] > 508 and event.pos[1] < 552 :
                    coord_retour = (64,508)
                else :
                    coord_retour = (1000,508)

            elif ecran == 7 or ecran == 8 :
                coord_selection_supprimer = ((event.pos[0]//50)*50,((event.pos[1]-6)//50)*50+6)

            elif ecran == 10 :
                if code1 == 0 :
                    if event.pos[0] > 452 and event.pos[0] < 549 and event.pos[1] > 512 and event.pos[1] < 548 :
                        coord_selection = (428,512)
                    else :
                        coord_selection = (1000,512)
                elif code1 == 1 :
                    if event.pos[0] > 384 and event.pos[0] < 481 and event.pos[1] > 512 and event.pos[1] < 548 :
                        coord_selection = (360,512)
                    elif event.pos[0] > 531 and event.pos[0] < 617 and event.pos[1] > 512 and event.pos[1] < 548 :
                        coord_selection = (507,512)
                    else :
                        coord_selection = (1000,512)

            elif ecran == 13 :
                if code2 == 1 :
                    if event.pos[0] > 427 and event.pos[0] < 558 and event.pos[1] > 363 and event.pos[1] < 391 :
                        coord_selection = (397,359)
                    else :
                        coord_selection = (1000,363)

            if not ecran == 14 :
                change_ecran()

        elif event.type == MOUSEBUTTONDOWN :
            if event.button == 1 :
                if ecran == 0 :
                    if event.pos[0] > 320 and event.pos[0] < 688 and event.pos[1] > 151 and event.pos[1] < 189 :
                        ecrire = 1
                    elif event.pos[0] > 320 and event.pos[0] < 688 and event.pos[1] > 264 and event.pos[1] < 302 :
                        ecrire = 2
                    elif event.pos[0] > 946 and event.pos[0] < 990 and event.pos[1] > 508 and event.pos[1] < 552 :
                        if len(nom) > 0 and len(nom_pays) > 0 or len(code) > 0 :
                            cinematique_deb()

                elif ecran == 1 :
                    if coord_selection == (430,400) :
                        ecran = 2
                        pygame.mixer.music.load(raccourci+"son\\enter_song.mp3")
                        pygame.mixer.music.play()
                        pygame.time.wait(4000)
                        pygame.mixer.music.load(raccourci+"son\\harpe.mp3")
                        pygame.mixer.music.play()
                        coord_selection = (1000,400)
                    elif event.pos[0] > 940 and event.pos[0] < 990 and event.pos[1] > 502 and event.pos[1] < 552 :
                        ecran = "1b"
                    elif event.pos[0] > 880 and event.pos[0] < 930 and event.pos[1] > 502 and event.pos[1] < 552 :
                        ecran = "1c"

                elif ecran == "1b" :
                    if event.pos[0] > 384 and event.pos[0] < 434 and event.pos[1] > 265 and event.pos[1] < 316 or event.pos[0] > 474 and event.pos[0] < 524 and event.pos[1] > 265 and event.pos[1] < 316 or event.pos[0] > 564 and event.pos[0] < 614 and event.pos[1] > 265 and event.pos[1] < 316 :
                        if event.pos[0] > 384 and event.pos[0] < 434 and event.pos[1] > 265 and event.pos[1] < 316 :
                            sauvegarde = open(raccourci+"sauvegardes\\sauvegarde1.txt","w")
                        elif event.pos[0] > 474 and event.pos[0] < 524 and event.pos[1] > 265 and event.pos[1] < 316 :
                            sauvegarde = open(raccourci+"sauvegardes\\sauvegarde2.txt","w")
                        elif event.pos[0] > 564 and event.pos[0] < 614 and event.pos[1] > 265 and event.pos[1] < 316 :
                            sauvegarde = open(raccourci+"sauvegardes\\sauvegarde3.txt","w")
                        texte = ""
                        for i in range (len(map)) :
                            texte += map[i]+"/"
                        sauvegarde.write(nom+"/"+nom_pays+"/"+str(code1)+"/"+str(code2)+"/"+str(popularite)+"/"+str(argent)+"/"+str(nourriture)+"/"+str(date[0])+"/"+str(date[1])+"/"+str(date[2])+"/"+str(russell2)+"/"+str(record)+"/"+texte)
                        sauvegarde.close()
                        ecran = 1
                    elif event.pos[0] < 365 or event.pos[0] > 635 or event.pos[1] < 206 or event.pos[1] > 356 :
                        ecran = 1

                elif ecran == "1c" :
                    if event.pos[0] > 384 and event.pos[0] < 434 and event.pos[1] > 265 and event.pos[1] < 316 or event.pos[0] > 474 and event.pos[0] < 524 and event.pos[1] > 265 and event.pos[1] < 316 or event.pos[0] > 564 and event.pos[0] < 614 and event.pos[1] > 265 and event.pos[1] < 316 :
                        if event.pos[0] > 384 and event.pos[0] < 434 and event.pos[1] > 265 and event.pos[1] < 316 :
                            sauvegarde = open(raccourci+"sauvegardes\\sauvegarde1.txt","r")
                            texte = sauvegarde.read()
                        elif event.pos[0] > 474 and event.pos[0] < 524 and event.pos[1] > 265 and event.pos[1] < 316 :
                            sauvegarde = open(raccourci+"sauvegardes\\sauvegarde2.txt","r")
                            texte = sauvegarde.read()
                        elif event.pos[0] > 564 and event.pos[0] < 614 and event.pos[1] > 265 and event.pos[1] < 316 :
                            sauvegarde = open(raccourci+"sauvegardes\\sauvegarde3.txt","r")
                            texte = sauvegarde.read()

                        if not texte == "" :
                            sauvegarde.close()

                            nb = 0
                            mot = ""
                            date = []
                            map = []
                            for i in range (len(texte)) :
                                if texte[i] == "/" :
                                    if nb == 0 :
                                        nom = mot
                                    elif nb == 1 :
                                        nom_pays = mot
                                    elif nb == 2 :
                                        code1 = int(mot)
                                    elif nb == 3 :
                                        code2 = int(mot)
                                    elif nb == 4 :
                                        popularite = int(mot)
                                    elif nb == 5 :
                                        argent = int(mot)
                                    elif nb == 6 :
                                        nourriture = int(mot)
                                    elif nb == 7 or nb == 8 or nb == 9 :
                                        date += [int(mot)]
                                    elif nb == 10 :
                                        russell2 = int(mot)
                                    elif nb == 11 :
                                        record = int(mot)
                                    else :
                                        map += [mot]
                                    mot = ""
                                    nb += 1
                                else :
                                    mot += texte[i]

                            ecran = 1

                        else :
                            sauvegarde.close()
                            initialisation()
                    elif event.pos[0] < 365 or event.pos[0] > 635 or event.pos[1] < 206 or event.pos[1] > 356 :
                        ecran = 1

                elif ecran == 2 :
                    if coord_pause == (950,10) :
                        ecran = 3
                        coord_pause = (1000,10)
                    elif coord_dossier == (760,126) :
                        ecran = 4
                        coord_dossier = (1000,126)
                    elif coord_ecran == (216,145) :
                        ecran = 5
                        x = 31
                        y = 25
                        pygame.mixer.music.load(raccourci+"son\\Country_Control.mp3")
                        pygame.mixer.music.play()
                        coord_ecran = (1000,145)
                        coord_info_case = (0,0)
                    elif coord_texte_lever == (723,508) :
                        ecran = 9
                        dim_perso = (54+(9/17)*43,144)
                        coord_perso = (384,342)
                        position = 1
                        repetition = 0
                        repetition2 = 0
                        coord_texte_lever = (1000,508)
                        pygame.mixer.music.load(raccourci+"son\\Jazz_In_the_Gas.mp3")
                        pygame.mixer.music.play()

                elif ecran == 3 :
                    if event.pos[0] > 403 and event.pos[0] < 597 and event.pos[1] > 84 and event.pos[1] < 119 :
                        ecran = 2
                    elif event.pos[0] > 403 and event.pos[0] < 597 and event.pos[1] > 119 and event.pos[1] < 154 :
                        ecran = 1
                        pygame.mixer.music.load(raccourci+"son\\infire_theme.mp3")
                        pygame.mixer.music.play()
                    elif event.pos[0] > 441 and event.pos[0] < 474 and event.pos[1] > 191 and event.pos[1] < 211 :
                        pygame.mixer.music.set_volume(1)
                        son = 1
                    elif event.pos[0] > 495 and event.pos[0] < 545 and event.pos[1] > 191 and event.pos[1] < 211 :
                        pygame.mixer.music.set_volume(0)
                        son = 0
                    elif event.pos[0] > 449 and event.pos[0] < 534 and event.pos[1] > 231 and event.pos[1] < 250 :
                        ecran = "3b"
                        ecrire = 0
                        code = ""
                        etat_code = 0
                    elif event.pos[0] > 455 and event.pos[0] < 525 and event.pos[1] > 265 and event.pos[1] < 284 :
                        ecran = "3c"
                    elif event.pos[0] > 411 and event.pos[0] < 429 and event.pos[1] > 343 and event.pos[1] < 360 :
                        vitesse = 4
                    elif event.pos[0] > 451 and event.pos[0] < 469 and event.pos[1] > 343 and event.pos[1] < 360 :
                        vitesse = 2
                    elif event.pos[0] > 491 and event.pos[0] < 509 and event.pos[1] > 343 and event.pos[1] < 360 :
                        vitesse = 1
                    elif event.pos[0] > 531 and event.pos[0] < 549 and event.pos[1] > 343 and event.pos[1] < 360 :
                        vitesse = 0.5
                    elif event.pos[0] > 571 and event.pos[0] < 589 and event.pos[1] > 343 and event.pos[1] < 360 :
                        vitesse = 0.25

                elif ecran == "3b" :
                    if event.pos[0] > 320 and event.pos[0] < 688 and event.pos[1] > 264 and event.pos[1] < 302:
                        ecrire = 1
                    elif event.pos[0] > 946 and event.pos[0] < 990 and event.pos[1] > 508 and event.pos[1] < 552 and len(code) > 0 :
                        if code == "617473142857" :
                            code1 = 1
                            etat_code = 1
                        elif code == "1183145" :
                            code2 = 1
                            etat_code = 1
                        else :
                            etat_code = 2
                    elif coord_retour == (64,10) :
                        ecran = 2
                        coord_retour = (1000,10)

                elif ecran == "3c" :
                    ecran = 2

                elif ecran == 4 :
                    if coord_texte_bureau == (64,14) :
                        ecran = 2
                        coord_texte_bureau = (1000,14)

                elif ecran == 5 :
                    if coord_texte_bureau == (64,20) :
                        ecran = 2
                        coord_texte_bureau = (1000,20)
                        pygame.mixer.music.load(raccourci+"son\\harpe.mp3")
                        pygame.mixer.music.play()
                    elif coord_magasin == (857,512) :
                        ecran = 6
                        pygame.mixer.music.load(raccourci+"son\\shop.mp3")
                        pygame.mixer.music.play()
                        coord_magasin = (1000,512)
                    elif coord_supprimer == (813,512) :
                        ecran = 7
                        coord_selection_supprimer = ((event.pos[0]//50)*50,((event.pos[1]-6)//50)*50+6)
                    elif coord_mouv_haut == (450,6) and y > 0 :
                        y -= 1
                    elif coord_mouv_bas == (450,516) and y < 89 :
                        y += 1
                    elif coord_mouv_gauche == (0,231) and x > 0 :
                        x -= 1
                    elif coord_mouv_droite == (960,231) and x < 89 :
                        x += 1
                    elif event.pos[0] > 40 and event.pos[0] < 960 and event.pos[1] > 46 and event.pos[1] < 516 :
                        coord_selection_supprimer = ((event.pos[0]//50)*50,((event.pos[1]-6)//50)*50+6)
                        if len(deplacements) % 2 == 0 :
                            if map[(y+int((coord_selection_supprimer[1]-6)/50))*100+x+int(coord_selection_supprimer[0]/50)][0:3] == "tar" and len(map[(y+int((coord_selection_supprimer[1]-6)/50))*100+x+int(coord_selection_supprimer[0]/50)]) == 4 or map[(y+int((coord_selection_supprimer[1]-6)/50))*100+x+int(coord_selection_supprimer[0]/50)][0:3] == "tac" and int(map[(y+int((coord_selection_supprimer[1]-6)/50))*100+x+int(coord_selection_supprimer[0]/50)][3]) > 0 :
                                for i in range (0,len(deplacements),2) :
                                    if i > len(deplacements)-2 :
                                        break
                                    elif deplacements[i] == (y+int((coord_selection_supprimer[1]-6)/50))*100+x+int(coord_selection_supprimer[0]/50) :
                                        del deplacements[i:i+2]
                                ecran = "5b"
                                deplacements += [(y+int((coord_selection_supprimer[1]-6)/50))*100+x+int(coord_selection_supprimer[0]/50)]

                elif ecran == "5b" :
                    if event.pos[0] > 40 and event.pos[0] < 960 and event.pos[1] > 46 and event.pos[1] < 516 :
                        coord_selection_supprimer = ((event.pos[0]//50)*50,((event.pos[1]-6)//50)*50+6)
                        if len(deplacements) % 2 == 1 and map[(y+int((coord_selection_supprimer[1]-6)/50))*100+x+int(coord_selection_supprimer[0]/50)] == "tar" or len(deplacements) % 2 == 1 and map[(y+int((coord_selection_supprimer[1]-6)/50))*100+x+int(coord_selection_supprimer[0]/50)] == "ter" or len(deplacements) % 2 == 1 and map[(y+int((coord_selection_supprimer[1]-6)/50))*100+x+int(coord_selection_supprimer[0]/50)][0:3] == "tac" :
                            deplacements += [(y+int((coord_selection_supprimer[1]-6)/50))*100+x+int(coord_selection_supprimer[0]/50)]
                            if deplacements[-1] == deplacements[-2] :
                                deplacements == deplacements[0:-2]
                            ecran = 5

                elif ecran == 6 :
                    if coord_retour == (64,508) :
                        ecran = 5
                        pygame.mixer.music.load(raccourci+"son\\Country_Control.mp3")
                        pygame.mixer.music.play()
                        coord_retour = (1000,508)
                    elif event.pos[0] > 88 and event.pos[0] < 159 and event.pos[1] > 485 and event.pos[1] < 510 and argent > 49 :
                        achat = "m"
                        ecran = 8
                        coord_selection_supprimer = ((event.pos[0]//50)*50,((event.pos[1]-6)//50)*50+6)
                    elif event.pos[0] > 339 and event.pos[0] < 410 and event.pos[1] > 486 and event.pos[1] < 511 and argent > 99 :
                        achat = "h"
                        ecran = 8
                        coord_selection_supprimer = ((event.pos[0]//50)*50,((event.pos[1]-6)//50)*50+6)
                    elif event.pos[0] > 589 and event.pos[0] < 660 and event.pos[1] > 486 and event.pos[1] < 511 and argent > 149 :
                        achat = "u"
                        ecran = 8
                        coord_selection_supprimer = ((event.pos[0]//50)*50,((event.pos[1]-6)//50)*50+6)
                    elif event.pos[0] > 839 and event.pos[0] < 910 and event.pos[1] > 485 and event.pos[1] < 510 and argent > 199 :
                        achat = "c"
                        ecran = 8
                        coord_selection_supprimer = ((event.pos[0]//50)*50,((event.pos[1]-6)//50)*50+6)

                elif ecran == 7 :
                    if not map[(y+int((coord_selection_supprimer[1]-6)/50))*100+x+int(coord_selection_supprimer[0]/50)][0] == "e" :
                        if map[(y+int((coord_selection_supprimer[1]-6)/50))*100+x+int(coord_selection_supprimer[0]/50)][1] == "a" :
                            if not map[(y+int((coord_selection_supprimer[1]-6)/50))*100+x+int(coord_selection_supprimer[0]/50)][2] == "r" and not map[(y+int((coord_selection_supprimer[1]-6)/50))*100+x+int(coord_selection_supprimer[0]/50)][2] == "q" :
                                if map[(y+int((coord_selection_supprimer[1]-6)/50))*100+x+int(coord_selection_supprimer[0]/50)][0:3] == "tam" :
                                    nb = int(map[(y+int((coord_selection_supprimer[1]-6)/50))*100+x+int(coord_selection_supprimer[0]/50)][3])
                                    i = 0
                                    while nb > 0 and i < len(map) :
                                        if map[i][0:3] == "tah" and int(map[i][3]) > 0 or map[i][0:3] == "tau" and int(map[i][3]) > 0 :
                                            if nb < int(map[i][3]) :
                                                map[i] = map[i][0:3]+str(int(map[i][3])-nb)
                                                nb = 0
                                            else :
                                                nb -= int(map[i][3])
                                                map[i] = map[i][0:3]+"0"
                                        i += 1
                                    if nb > 0 :
                                        i = 0
                                        while nb > 0 and i < len(map) :
                                            if map[i][0:3] == "tac" and int(map[i][3]) > 0 :
                                                if nb < int(map[i][3]) :
                                                    map[i] = map[i][0:3]+str(int(map[i][3])-nb)+str(int(map[i][4])-nb)
                                                    nb = 0
                                                else :
                                                    nb -= int(map[i][3])
                                                    map[i] = map[i][0:3]+"0"
                                            i += 1
                                        if nb > 0 :
                                            i = 0
                                            while i < len(map) :
                                                if map[i][0:3] == "tar" and len(map[i]) > 3 :
                                                    if int(map[i][3]) > 0 :
                                                        if nb < int(map[i][3]) :
                                                            map[i] = map[i][0:3]+str(int(map[i][3])-nb)
                                                            nb = 0
                                                        else :
                                                            nb -= int(map[i][3])
                                                            map[i] = map[i][0:3]+"0"
                                                i += 1

                                map[(y+int((coord_selection_supprimer[1]-6)/50))*100+x+int(coord_selection_supprimer[0]/50)] = map[(y+int((coord_selection_supprimer[1]-6)/50))*100+x+int(coord_selection_supprimer[0]/50)][0:2] + "r"

                elif ecran == 8 :
                    if not map[(y+int((coord_selection_supprimer[1]-6)/50))*100+x+int(coord_selection_supprimer[0]/50)][0] == "e" :
                        if map[(y+int((coord_selection_supprimer[1]-6)/50))*100+x+int(coord_selection_supprimer[0]/50)][1] == "a" :
                            if map[(y+int((coord_selection_supprimer[1]-6)/50))*100+x+int(coord_selection_supprimer[0]/50)][2] == "r" :
                                map[(y+int((coord_selection_supprimer[1]-6)/50))*100+x+int(coord_selection_supprimer[0]/50)] =  "ta"+achat+"0"
                                if achat == "m" :
                                    argent -= 50
                                elif achat == "h" :
                                    argent -= 100
                                elif achat == "u" :
                                    argent -= 150
                                elif achat == "c" :
                                    argent -= 200
                                ecran = 5
                                pygame.mixer.music.load(raccourci+"son\\Country_Control.mp3")
                                pygame.mixer.music.play()

                elif ecran == 10 :
                    if coord_selection == (428,512) or coord_selection == (360,512) :
                        repetition2 = 0
                        ecran = 9
                        coord_selection = (1000,512)
                    elif coord_selection == (507,512) :
                        reponse_oui()
                        russell2 = 1
                        ecran = 11
                        coord_selection == (1000,512)
                        dim_perso = (81,153)
                        coord_perso = (109,418)
                        position = 1
                        repetition = 0

                elif ecran == 13 :
                    if coord_selection == (397,359) :
                        score = 0
                        coord_vaisseau = 474
                        asteroides = [229+randint(0,4)*110,-692]
                        pygame.key.set_repeat(15,15)
                        ecran = 14

                change_ecran()

            elif event.button == 3 :
                if ecran == 7 or ecran == 8 :
                    ecran = 5

                change_ecran()

        elif event.type == KEYDOWN :
            if ecran == 0 :
                if ecrire == 1 :
                    if event.key == K_BACKSPACE and len(nom) > 0 :
                        nom = nom[0:len(nom)-1]
                        change_ecran()
                    else :
                        i = 0
                        non = 0
                        while i < len(alphabet_qwerty) and non == 0 :
                            if alphabet_qwerty[i] == chr(event.key) :
                                non = 1
                            i += 1
                        if non == 1 and not alphabet_azerty[i-1] == "," and len(nom) < 20 :
                            nom += alphabet_azerty[i-1]
                            change_ecran()

                elif ecrire == 2 :
                    if event.key == K_BACKSPACE and len(nom_pays) > 0 :
                        nom_pays = nom_pays[0:len(nom_pays)-1]
                        change_ecran()
                    else :
                        i = 0
                        non = 0
                        while i < len(alphabet_qwerty) and non == 0 :
                            if alphabet_qwerty[i] == chr(event.key) :
                                non = 1
                            i += 1
                        if non == 1 and not alphabet_azerty[i-1] == "," and len(nom_pays) < 20 :
                            nom_pays += alphabet_azerty[i-1]
                            change_ecran()

            elif ecran == "3b" and ecrire == 1 :
                if event.key == K_BACKSPACE and len(code) > 0 :
                    code = code[0:len(code)-1]
                    change_ecran()
                else :
                    if len(code) < 20 :
                        if event.key == K_0 or event.key == K_1 or event.key == K_2 or event.key == K_3 or event.key == K_4 or event.key == K_5 or event.key == K_6 or event.key == K_7 or event.key == K_8 or event.key == K_9 or event.key == K_KP0 or event.key == K_KP1 or event.key == K_KP2 or event.key == K_KP3 or event.key == K_KP4 or event.key == K_KP5 or event.key == K_KP6 or event.key == K_KP7 or event.key == K_KP8 or event.key == K_KP9 :
                            if chr(event.key) == "Ā" :
                                code += "0"
                            elif chr(event.key) == "ā" :
                                code += "1"
                            elif chr(event.key) == "Ă" :
                                code += "2"
                            elif chr(event.key) == "ă" :
                                code += "3"
                            elif chr(event.key) == "Ą" :
                                code += "4"
                            elif chr(event.key) == "ą" :
                                code += "5"
                            elif chr(event.key) == "Ć" :
                                code += "6"
                            elif chr(event.key) == "ć" :
                                code += "7"
                            elif chr(event.key) == "Ĉ" :
                                code += "8"
                            elif chr(event.key) == "ĉ" :
                                code += "9"
                            else :
                                code += chr(event.key)
                            change_ecran()

            elif ecran == 9 :
                repetition = 1
                if event.key == K_UP and coord_perso[1] > 174 :
                    if coord_perso[1] == 550 and coord_perso[0] > -16 and coord_perso[0] < 164 or coord_perso[1] == 358 and coord_perso[0] > 44 and coord_perso[0] < 224 or coord_perso[1] == 414 and coord_perso[0] > 284 and coord_perso[0] < 804 :
                        coord_perso = coord_perso
                    else :
                        coord_perso = (coord_perso[0],coord_perso[1]-8)
                        dim_perso = (dim_perso[0]-(9/17)*2,dim_perso[1]-2)
                        if not position == 4 and not position == 5 and not position == 6 :
                            position = 5
                        elif position == 5 :
                            position = 4
                        elif position == 4 :
                            position = 6
                        elif position == 6 :
                            position = 14
                elif event.key == K_UP and coord_perso[1] == 174 and coord_perso[0] > 50 and coord_perso[0] < 170 :
                    repetition2 += 1
                elif event.key == K_DOWN and coord_perso[1] < 564 :
                    if coord_perso[1] == 502 and coord_perso[0] > -16 and coord_perso[0] < 164 or coord_perso[1] == 342 and coord_perso[0] > 44 and coord_perso[0] < 224 or coord_perso[1] == 342 and coord_perso[0] > 284 and coord_perso[0] < 804 :
                        coord_perso = coord_perso
                    else :
                        coord_perso = (coord_perso[0],coord_perso[1]+8)
                        dim_perso = (dim_perso[0]+(9/17)*2,dim_perso[1]+2)
                        if not position == 1 and not position == 2 and not position == 3 :
                            position = 2
                        elif position == 2 :
                            position = 1
                        elif position == 1 :
                            position = 3
                        elif position == 3 :
                            position = 13
                elif event.key == K_LEFT and coord_perso[0] > 0 :
                    if coord_perso[0] == 164 and coord_perso[1] > 502 and coord_perso[1] < 550 or coord_perso[0] == 224 and coord_perso[1] > 342 and coord_perso[1] < 358 or coord_perso[0] == 804 and coord_perso[1] > 342 and coord_perso[1] < 414 :
                        coord_perso = coord_perso
                    else :
                        coord_perso = (coord_perso[0]-20,coord_perso[1])
                        if not position == 7 and not position == 8 and not position == 9 :
                            position = 8
                        elif position == 8 :
                            position = 7
                        elif position == 7 :
                            position = 9
                        elif position == 9 :
                            position = 15
                elif event.key == K_RIGHT and coord_perso[0] < 1000 :
                    if coord_perso[0] == -16 and coord_perso[1] > 502 and coord_perso[1] < 550 or coord_perso[0] == 44 and coord_perso[1] > 342 and coord_perso[1] < 358 or coord_perso[0] == 284 and coord_perso[1] > 342 and coord_perso[1] < 414 :
                        coord_perso = coord_perso
                    else :
                        coord_perso = (coord_perso[0]+20,coord_perso[1])
                        if not position == 10 and not position == 11 and not position == 12 :
                            position = 11
                        elif position == 11 :
                            position = 10
                        elif position == 10 :
                            position = 12
                        elif position == 12 :
                            position = 16

                elif event.key == K_SPACE :
                    if coord_perso[1] == 174 and coord_perso[0] > 185 and coord_perso[0] < 290 :
                        coord_panneau = (300,118)
                    elif coord_perso[1] == 414 and coord_perso[0] > 284 and coord_perso[0] < 804 or coord_perso[1] == 342 and coord_perso[0] > 284 and coord_perso[0] < 804 or coord_perso[0] == 804 and coord_perso[1] > 342 and coord_perso[1] < 414 or coord_perso[0] == 284 and coord_perso[1] > 342 and coord_perso[1] < 414 :
                        ecran = 2
                        pygame.mixer.music.load(raccourci+"son\\harpe.mp3")
                        pygame.mixer.music.play()
                    elif coord_perso[1] == 174 and coord_perso[0] > 905 and coord_perso[0] < 987 :
                        if russell2 == 0 :
                            ecran = 10
                        else :
                            ecran = 11
                            coord_selection == (1000,512)
                            dim_perso = (81,153)
                            coord_perso = (109,418)
                            position = 1
                            repetition = 0
                    elif coord_perso[1] == 174 and coord_perso[0] > 826 and coord_perso[0] < 880 :
                        if russell2 == 0 :
                            a = randint(1,5)
                        else :
                            a = randint(1,4)
                        if a == 1 :
                            fenetre.blit(conseil1,(747,10))
                        elif a == 2 :
                            fenetre.blit(conseil2,(759,10))
                        elif a == 3 :
                            fenetre.blit(conseil3,(770,10))
                        elif a == 4 :
                            fenetre.blit(conseil4,(759,10))
                        elif a == 5 :
                            fenetre.blit(conseil5,(703,10))
                        pygame.display.flip()
                        pygame.time.wait(3000)

                if not event.key == K_SPACE :
                    coord_panneau = (1000,118)

                change_ecran()

            elif ecran == 11 :
                repetition = 1
                if event.key == K_UP and coord_perso[1] > 418 :
                    coord_perso = (coord_perso[0],coord_perso[1]-8)
                    dim_perso = (dim_perso[0]-(9/17)*2,dim_perso[1]-2)
                    if not position == 4 and not position == 5 and not position == 6 :
                        position = 5
                    elif position == 5 :
                        position = 4
                    elif position == 4 :
                        position = 6
                    elif position == 6 :
                        position = 14
                elif event.key == K_DOWN and coord_perso[1] < 562 :
                    coord_perso = (coord_perso[0],coord_perso[1]+8)
                    dim_perso = (dim_perso[0]+(9/17)*2,dim_perso[1]+2)
                    if not position == 1 and not position == 2 and not position == 3 :
                        position = 2
                    elif position == 2 :
                        position = 1
                    elif position == 1 :
                        position = 3
                    elif position == 3 :
                        position = 13
                elif event.key == K_LEFT and coord_perso[0] > 0 :
                    coord_perso = (coord_perso[0]-20,coord_perso[1])
                    if not position == 7 and not position == 8 and not position == 9 :
                        position = 8
                    elif position == 8 :
                        position = 7
                    elif position == 7 :
                        position = 9
                    elif position == 9 :
                        position = 15
                elif event.key == K_RIGHT and coord_perso[0] < 1000 :
                    coord_perso = (coord_perso[0]+20,coord_perso[1])
                    if not position == 10 and not position == 11 and not position == 12 :
                        position = 11
                    elif position == 11 :
                        position = 10
                    elif position == 10 :
                        position = 12
                    elif position == 12 :
                        position = 16

                elif event.key == K_SPACE :
                    if coord_perso[1] == 418 and coord_perso[0] > 43 and coord_perso[0] < 169 :
                        ecran = 9
                        coord_perso = (944,174)
                        dim_perso = (54+(9/17),102)
                    elif coord_perso[1] == 418 and coord_perso[0] > 404 and coord_perso[0] < 530 :
                        ecran = 12
                        coord_perso = (65,174)
                        dim_perso = (54+(9/17),102)
                    elif coord_perso[1] == 418 and coord_perso[0] > 752 and coord_perso[0] < 878 :
                        fenetre.blit(bulle,(coord_perso[0]-48,coord_perso[1]-200))
                        pygame.display.flip()
                        pygame.time.wait(2000)

                change_ecran()

            elif ecran == 12 :
                repetition = 1
                if event.key == K_UP and coord_perso[1] > 174 :
                    if coord_perso[1] == 182 and coord_perso[0] > 441 and coord_perso[0] < 512 or coord_perso[1] == 182 and coord_perso[0] > 778 and coord_perso[0] < 848 or coord_perso[1] == 494 and coord_perso[0] > 339 and coord_perso[0] < 653 :
                        coord_perso = coord_perso
                    else :
                        coord_perso = (coord_perso[0],coord_perso[1]-8)
                        dim_perso = (dim_perso[0]-(9/17)*2,dim_perso[1]-2)
                        if not position == 4 and not position == 5 and not position == 6 :
                            position = 5
                        elif position == 5 :
                            position = 4
                        elif position == 4 :
                            position = 6
                        elif position == 6 :
                            position = 14
                elif event.key == K_DOWN and coord_perso[1] < 564 :
                    if coord_perso[1] == 310 and coord_perso[0] > 339 and coord_perso[0] < 653 or coord_perso[1] == 510 and coord_perso[0] > 880 and coord_perso[0] < 1001 :
                        coord_perso = coord_perso
                    else :
                        coord_perso = (coord_perso[0],coord_perso[1]+8)
                        dim_perso = (dim_perso[0]+(9/17)*2,dim_perso[1]+2)
                        if not position == 1 and not position == 2 and not position == 3 :
                            position = 2
                        elif position == 2 :
                            position = 1
                        elif position == 1 :
                            position = 3
                        elif position == 3 :
                            position = 13
                elif event.key == K_LEFT and coord_perso[0] > 0 :
                    if coord_perso[0] == 545 and coord_perso[1] == 174 or coord_perso[0] == 865 and coord_perso[1] == 174 or coord_perso[0] == 665 and coord_perso[1] > 310 and coord_perso[1] < 494 :
                        coord_perso = coord_perso
                    else :
                        coord_perso = (coord_perso[0]-20,coord_perso[1])
                        if not position == 7 and not position == 8 and not position == 9 :
                            position = 8
                        elif position == 8 :
                            position = 7
                        elif position == 7 :
                            position = 9
                        elif position == 9 :
                            position = 15
                elif event.key == K_RIGHT and coord_perso[0] < 1000 :
                    if coord_perso[0] == 425 and coord_perso[1] == 174 or coord_perso[0] == 765 and coord_perso[1] == 174 or coord_perso[0] == 325 and coord_perso[1] > 310 and coord_perso[1] < 494 or coord_perso[0] == 845 and coord_perso[1] > 510 and coord_perso[1] < 562 :
                        coord_perso = coord_perso
                    else :
                        coord_perso = (coord_perso[0]+20,coord_perso[1])
                        if not position == 10 and not position == 11 and not position == 12 :
                            position = 11
                        elif position == 11 :
                            position = 10
                        elif position == 10 :
                            position = 12
                        elif position == 12 :
                            position = 16

                elif event.key == K_SPACE :
                    if coord_perso[1] == 174 and coord_perso[0] > 23 and coord_perso[0] < 109 :
                        ecran = 11
                        coord_perso = (469,418)
                        dim_perso = (81,153)
                    elif coord_perso[1] == 182 and coord_perso[0] > 441 and coord_perso[0] < 512 :
                        ecran = 13
                        coord_selection = (1000,363)
                        pygame.mixer.music.load(raccourci+"son\\Highscore14.mp3")
                        pygame.mixer.music.play()
                    elif coord_perso[1] == 182 and coord_perso[0] > 778 and coord_perso[0] < 848 :
                        cafe()
                        change_ecran()

                change_ecran()

            elif ecran == 13 :
                if code2 == 0 or code2 == 1 and event.key == K_SPACE :
                    ecran = 12
                    pygame.mixer.music.load(raccourci+"son\\Jazz_In_the_Gas.mp3")
                    pygame.mixer.music.play()

                change_ecran()

            elif ecran == 14 :
                if event.key == K_LEFT and coord_vaisseau > 224 :
                    coord_vaisseau -= 10
                elif event.key == K_RIGHT and coord_vaisseau < 724 :
                    coord_vaisseau += 10

        elif event.type == KEYUP :
            repetition = 0
            repetition2 = 0
            change_ecran()

    if ecran == 5 :
        pygame.time.wait(1)
        temps += 0.005
        cooldown -= 0.005
        jeu()
    elif ecran == 14 :
        mouve_asteroide()