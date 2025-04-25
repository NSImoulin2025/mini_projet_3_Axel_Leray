import cairo
import colorsys


def dessiner_grille(output_file="morpion.png"):
    """
    Dessine une grille de morpion (tic-tac-toe) sur une image et sauvegarde celle-ci dans un fichier PNG.

    Paramètres:
        output_file (str): Le nom du fichier de sortie pour l'image (par défaut "morpion.png").
    """
    width, height = 650, 450
    margin = 15
    size = height - 2 * margin
    x_offset = (width - size) // 2

    # Couleur de fond (HSL à RGB)
    h, s, l = 43 / 360, 0.74, 0.49
    r, g, b = colorsys.hls_to_rgb(h, l, s)

    # Création de la surface d'image et du contexte de dessin
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)

    # Remplir l'arrière-plan avec la couleur calculée
    ctx.set_source_rgb(r, g, b)
    ctx.paint()

    # Dessiner la grille
    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_width(5)

    x1, x2 = x_offset + size // 3, x_offset + 2 * size // 3
    y1, y2 = margin + size // 3, margin + 2 * size // 3

    # Lignes verticales
    ctx.move_to(x1, margin)
    ctx.line_to(x1, margin + size)
    ctx.move_to(x2, margin)
    ctx.line_to(x2, margin + size)

    # Lignes horizontales
    ctx.move_to(x_offset, y1)
    ctx.line_to(x_offset + size, y1)
    ctx.move_to(x_offset, y2)
    ctx.line_to(x_offset + size, y2)
    ctx.stroke()

    # Sauvegarder l'image au format PNG
    surface.write_to_png(output_file)


def dessiner_croix_rouge(image_name, coordinates, output_file):
    """
    Dessine une croix rouge (X) sur une image existante de morpion à une position donnée 
    et sauvegarde l'image modifiée dans un fichier PNG.

    Paramètres:
        image_name (str): Le nom du fichier image de base (par exemple, "morpion.png").
        coordinates (tuple): La position (x, y) où la croix rouge doit être dessinée.
        output_file (str): Le nom du fichier de sortie pour l'image modifiée.
    """
    image_surface = cairo.ImageSurface.create_from_png(image_name)
    width = image_surface.get_width()
    height = image_surface.get_height()

    # Création de la surface d'image pour dessiner la croix
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)

    # Copier l'image existante
    ctx.set_source_surface(image_surface, 0, 0)
    ctx.paint()

    # Dessiner la croix rouge
    ctx.set_source_rgb(1, 0, 0)
    ctx.set_line_width(5)

    x, y = coordinates
    cross_size = 40

    # Tracer la croix (deux lignes diagonales)
    ctx.move_to(x - cross_size, y - cross_size)
    ctx.line_to(x + cross_size, y + cross_size)
    ctx.move_to(x + cross_size, y - cross_size)
    ctx.line_to(x - cross_size, y + cross_size)
    ctx.stroke()

    # Sauvegarder l'image avec la croix rouge
    surface.write_to_png(output_file)


def dessiner_rond_bleu(image_name, coordinates, output_file):
    """
    Dessine un rond bleu (O) sur une image existante de morpion à une position donnée 
    et sauvegarde l'image modifiée dans un fichier PNG.

    Paramètres:
        image_name (str): Le nom du fichier image de base (par exemple, "morpion.png").
        coordinates (tuple): La position (x, y) où le rond bleu doit être dessiné.
        output_file (str): Le nom du fichier de sortie pour l'image modifiée.
    """
    image_surface = cairo.ImageSurface.create_from_png(image_name)
    width = image_surface.get_width()
    height = image_surface.get_height()

    # Création de la surface d'image pour dessiner le rond
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)

    # Copier l'image existante
    ctx.set_source_surface(image_surface, 0, 0)
    ctx.paint()

    # Dessiner le rond bleu
    ctx.set_source_rgb(0, 0, 1)
    ctx.set_line_width(5)

    x, y = coordinates
    rayon = 40

    # Tracer un cercle (rond)
    ctx.arc(x, y, rayon, 0, 2 * 3.14159)
    ctx.stroke()

    # Sauvegarder l'image avec le rond bleu
    surface.write_to_png(output_file)


if __name__ == "__main__":
    """
    Point d'entrée principal pour dessiner la grille de morpion.
    Cette fonction est exécutée si le script est lancé directement.
    """
    dessiner_grille()
