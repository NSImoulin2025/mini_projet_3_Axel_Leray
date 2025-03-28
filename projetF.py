
import creation_image as ci
from flask import Flask, render_template, request
import os

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

app = Flask(__name__)

ci.dessiner_grille()


@app.route("/", methods=["GET"])
def site_image():

    btn = request.args.get("btn")
    if btn:
        btn = int(btn) - 1
        if (btn % 2) == 0:
            ci.dessiner_croix_rouge("morpion.png", coordinates_list[btn], "morpion.png")
        else:
            ci.dessiner_rond_bleu("morpion.png", coordinates_list[btn], "morpion.png")

    return render_template("index.html", btn=btn)


if __name__ == "__main__":
    app.run(port=8080, debug=True)
