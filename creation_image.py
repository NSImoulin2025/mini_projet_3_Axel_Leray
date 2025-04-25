import cairo
import colorsys


def dessiner_grille(output_file="morpion.png"):
    width, height = 650, 450
    margin = 15
    size = height - 2 * margin
    x_offset = (width - size) // 2

    h, s, l = 43 / 360, 0.74, 0.49
    r, g, b = colorsys.hls_to_rgb(h, l, s)


    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)

    ctx.set_source_rgb(r, g, b)
    ctx.paint()

    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_width(5)

    x1, x2 = x_offset + size // 3, x_offset + 2 * size // 3
    y1, y2 = margin + size // 3, margin + 2 * size // 3

    ctx.move_to(x1, margin)
    ctx.line_to(x1, margin + size)
    ctx.move_to(x2, margin)
    ctx.line_to(x2, margin + size)

    ctx.move_to(x_offset, y1)
    ctx.line_to(x_offset + size, y1)
    ctx.move_to(x_offset, y2)
    ctx.line_to(x_offset + size, y2)
    ctx.stroke()

    surface.write_to_png(output_file)


def dessiner_croix_rouge(image_name, coordinates, output_file):
    image_surface = cairo.ImageSurface.create_from_png(image_name)
    width = image_surface.get_width()
    height = image_surface.get_height()

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)

    ctx.set_source_surface(image_surface, 0, 0)
    ctx.paint()

    ctx.set_source_rgb(1, 0, 0)
    ctx.set_line_width(5)

    x, y = coordinates
    cross_size = 40

    ctx.move_to(x - cross_size, y - cross_size)
    ctx.line_to(x + cross_size, y + cross_size)
    ctx.move_to(x + cross_size, y - cross_size)
    ctx.line_to(x - cross_size, y + cross_size)
    ctx.stroke()

    surface.write_to_png(output_file)


def dessiner_rond_bleu(image_name, coordinates, output_file):
    image_surface = cairo.ImageSurface.create_from_png(image_name)
    width = image_surface.get_width()
    height = image_surface.get_height()

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)

    ctx.set_source_surface(image_surface, 0, 0)
    ctx.paint()

    ctx.set_source_rgb(0, 0, 1)
    ctx.set_line_width(5)

    x, y = coordinates
    rayon = 40

    ctx.arc(x, y, rayon, 0, 2 * 3.14159)
    ctx.stroke()

    surface.write_to_png(output_file)

if __name__ == "__main__":
    dessiner_grille()
