from random import randrange
import time
import sqlite3

def banque():
    a = int(input("Combien d'argent souhaitez-vous déposer ? "))
    return a

def nom_joueur():
    p = str(input("Quel est votre nom? "))
    return p


def save_donnee(nomjoueur, gain):
    try:
        conn = sqlite3.connect('BDD_argent_joueur.db')
        cur = conn.cursor()
    
        cur.execute("""INSERT INTO total_argent(nom, argent) VALUES(?, ?)""", (nomjoueur, gain))
    
        conn.commit()
        cur.close()
    except IOError:
        # Erreur d'écriture
        print("Impossible d'écrire.")



def roulette():
    rand_num = randrange(50)
    return rand_num
  
def pair_impair(numero_mise, numero_roulette):
    if ((numero_mise % 2 == 0) and (numero_roulette % 2 == 0)) or ((numero_mise % 2 != 0) and (numero_roulette % 2 != 0)):
        return True
    else:
        return False
  
def jeu():
    jouer=True #La variable "jouer" est à True, le programme se lance
    print('---------------------------------------------')
    print('Bienvenue au EKE Casino - Jeu de la roulette')
    print('---------------------------------------------')
    #--------------------------------------------------------------------------------
    
    sqliteCon = sqlite3.connect('BDD_argent_joueur.db')
    cursor = sqliteCon.cursor()
    query_select_all = "SELECT * FROM total_argent"
    cursor.execute(query_select_all)
    tablerows = cursor.fetchall()
    for row in tablerows:
        jr = row[1]
        ar = row[2]
    if jr == "aucunjoueur":
        joueur = nom_joueur()
    else:
        joueur= jr
    
    if ar == 0.0:
        if jr != "aucunjoueur":
           print('Bonjour ' + joueur + "!")     
           argent = banque()
        else:
            argent = banque()
    else:
        argent = ar
      
    #---------------------------------------------------------------------------------
    indent="chat"  
    while jouer==True:
        if indent == "chien":
            break
        else :
            print('Bonjour ' + joueur + "!")
            print('Vous disposez de {} €'.format(argent))
            while True :
                mise_numero = int(input('Sur quel numéro misez vous ? (0-49)\n'))
                if mise_numero in range (0, 50):
                    break
                else:
                    print("Le numéro saisie n'est pas compris entre 0 et 49")
            while True:
                mise_argent = int(input("Combien d'argent voulez vous misez ?\n"))
                if argent - mise_argent < 0:
                    print("Vous n'avez pas assez d'argent !")
                else:
                    break
            print('Vous avez misé {} € sur le numéro {}'.format(mise_argent, mise_numero))
          
            num_roulette = roulette()
            time.sleep(2)
            print('La roulette tombe sur le numéro : {}'.format(num_roulette))

      
        if mise_numero != num_roulette:
            if pair_impair(mise_numero, num_roulette):
                argent += mise_argent * 0.5
                save_donnee(joueur, argent)
                print('Le numéro misé ({}) et le numéro gagnant ({}) sont de la même couleur, vous gagnez la moitié de votre mise'.format(mise_numero, num_roulette))
                print('Vous disposez maintenant de {} €'.format(argent))
                jouer=False
                rejouer()
                
            else:
                argent -= mise_argent
                save_donnee(joueur, argent)
                print('Perdu ! Vous disposez maintenant de {} €'.format(argent))
                if argent == 0:
                    depot = input("Souhaitez-vous déposer de l'argent ? (O/N)")
                    if depot == "N":
                        print("Vigile : Vous êtes à sec, rentrez chez vous !")
                        jouer=False
                        break
                    else:
                        argent = banque()
                else:
                    jouer=False
                    rejouer()
        else:
            argent += mise_argent * 3
            save_donnee(joueur, argent)
            print('Bravo ! Vous avez gagné {} €'.format(mise_argent*3))
            print('Vous disposez maintenant de {} €'.format(argent))
            jouer=False
            rejouer()

def rejouer():
    choix = input ("Souhaitez vous rejouer ? (O/N)")
    if (choix !="o" and choix !="O"):
        print("Caissière : À bientôt!")
    else:
        jeu()

def affichage():      
    sqliteCon = sqlite3.connect('BDD_argent_joueur.db')
    cursor = sqliteCon.cursor()
    query_select_all = "SELECT * FROM total_argent"
    cursor.execute(query_select_all)
    tablerows = cursor.fetchall()
    print("Nombre de parties: ", len(tablerows))
    print("Voici toutes les parties jouées : ")
    
    for row in tablerows:
        print("Partie: ", row[0])
        print("Nom: ", row[1]) 
        print("Argent: ", row[2])
        print("------\n")
    
    cursor.close()
    sqliteCon.close()

jeu()
affichage()
