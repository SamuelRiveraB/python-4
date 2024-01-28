import random

pierre = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papier = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

ciseaux = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = input("Pierre, Papier, Ciseaux ")
choice2 = random.randint(0,2)
print("Votre choix:")
if(choice == "pierre"):
    print(pierre)
    print("Choix d'ordinateur:")
    if(choice2 == 0):
        print(pierre)
        print("Pas de gagnant")
    elif(choice2 == 1):
        print(papier)
        print("Tu as perdu")
    elif(choice2 == 2):
        print(ciseaux)
        print("Tu as gagné")
if(choice == "papier"):
    print(papier)
    print("Choix d'ordinateur:")
    if(choice2 == 1):
        print(papier)
        print("Pas de gagnant")
    elif(choice2 == 2):
        print(ciseaux)
        print("Tu as perdu")
    elif(choice2 == 0):
        print(pierre)
        print("Tu as gagné")
if(choice == "ciseaux"):
    print(ciseaux)
    print("Choix d'ordinateur:")
    if(choice2 == 2):
        print(ciseaux)
        print("Pas de gagnant")
    elif(choice2 == 0):
        print(pierre)
        print("Tu as perdu")
    elif(choice2 == 1):
        print(papier)
        print("Tu as gagné")
