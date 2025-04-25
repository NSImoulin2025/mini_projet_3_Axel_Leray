# pour relancer la partie, il faut recharger la page web sans le '/?btn=1'

import creation_image as ci
from flask import Flask, render_template, request
import os

# Liste des coordonnées pour les cases du morpion
coordinates_list = [
    (175, 75),
    (325, 75),
    (475, 75),
    (175, 225),
    (325, 225),
    (475, 225),
    (175, 375),
    (325, 375),
    (475, 375),
]

# Création de l'application Flask
app = Flask(__name__)

# Initialisation de la grille du morpion
ci.dessiner_grille()

# Compteur pour suivre les tours de jeu
counter = 0

@app.route("/", methods=["GET"])
def site_image():
    """
    Fonction qui gère la route principale du site. Elle gère la logique 
    du jeu de morpion en fonction du bouton pressé et alterne entre 
    dessiner un 'X' ou un 'O' sur l'image du morpion.
    
    Elle met à jour l'état du jeu et renvoie le modèle HTML à afficher.
    
    Retourne:
        render_template: rend la page HTML avec les informations sur l'état actuel du jeu.
    """
    global counter  # Variable partagée entre les appels de la fonction
    btn = request.args.get("btn")  # Récupération de la valeur du bouton appuyé via la requête GET
    
    if btn:
        btn = int(btn) - 1  # Ajuste le bouton pour correspondre à l'index de la liste des coordonnées
        if counter % 2 == 0:
            # Dessiner un 'X' (croix rouge) si c'est le tour du joueur 1
            ci.dessiner_croix_rouge("morpion.png", coordinates_list[btn], "morpion.png")
        else:
            # Dessiner un 'O' (rond bleu) si c'est le tour du joueur 2
            ci.dessiner_rond_bleu("morpion.png", coordinates_list[btn], "morpion.png")
        counter += 1  # Incrémenter le compteur pour alterner les tours
    return render_template("index.html", btn=btn)  # Rendre la page HTML avec l'état du jeu


if __name__ == "__main__":
    """
    Point d'entrée principal du programme. Lance le serveur Flask 
    en mode debug et sur le port 8080.
    """
    app.run(port=8080, debug=True)
