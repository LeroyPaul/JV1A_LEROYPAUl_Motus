#MOTUS

from colorama import init
init()
from colorama import Back, Style, Fore

import random
listemots = ['castor', 'cinema', 'cypres', 'citron', 'joyeux', 'sphynx', 'pyjama', 'bijoux', 'voyage', 'viking', 'bidule', 'graine', 'numero', 'animal']

def selectRandom(mot):
  return random.choice(listemots)
mot=selectRandom(listemots)

print(Fore.RED + "Bonjour et bienvenue dans MOTUS !!\nLe but du jeu est de trouver un mot mystère de 6 lettre en proposant d'autres mots de 6 lettres !\nVous avez 8 essais pour trouver le mot mystère.\nBonne chance ! ")
print(Style.RESET_ALL)

lettrebienplace=False
lettrepresente=False
tour=0

for t in range (8):
  tour = tour+1
  lettre = input("Choisis un mot de 6 lettres : ")

  for i in range (len(mot)):
    
    if mot[i] == lettre[i]:                           # Vérification si la lettre est présente et bien placée
      print(Back.RED + lettre[i], end=" ")
      lettrebienplace=True   
    
    elif mot[i] != lettre[i]:                         # Vérification si la lettre est présente mais mal placée
      for f in range (len(mot)):                      # J'ai remplacé le jaune par du vert car sinon c'était illisible 
        if mot[f]==lettre[i]:
          lettrepresente=True
    
    if lettrepresente==True and lettrebienplace==False:     
      print(Back.GREEN + lettre[i], end=" ")
    
    if lettrepresente==False and lettrebienplace==False:           # Vérification si la lettre n'est pas présente 
      print(Back.BLUE + lettre[i], end=" ")
    lettrebienplace=False
    lettrepresente=False

  print(Style.RESET_ALL)

  if lettre == mot:                                                
    print(Fore.RED +"Félicitation ! Vosu avez trouvé le mot mystère !")
    print(Style.RESET_ALL)
    break

  if tour == 7:
    print (Fore.RED +"Vous n'avez plus qu'un essai.")
    print(Style.RESET_ALL)
  if tour == 8:
    print (Fore.RED +"C'est fini. Vous avez perdu.\nLe mot à trouver était",mot,"\nVous ferrez mieux la prochaine fois")
    print(Style.RESET_ALL)

  


  
  
      





