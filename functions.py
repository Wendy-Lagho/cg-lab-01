import cairo

def create_surface(width, height, background_color):
    surface = cairo.ImageSurface(cairo.FORMAT_RGB24, width, height)
    context = cairo.Context(surface)
    context.set_source_rgb(*background_color)
    context.paint()

    return surface, context

def draw_line(context, x1, y1, x2, y2, color, width):
    context.set_source_rgb(*color)
    context.set_line_width(width)
    context.move_to(x1, y1)
    context.line_to(x2, y2)
    context.stroke()

def draw_arc(context, x1, y1, radius, a1, a2, colour, width):
    context.set_source_rgb(*colour)
    context.set_line_width(width)
    context.arc(x1, y1, radius, a1, a2)
    context.stroke()

def write_to_surface(surface, context, filename):
    surface.write_to_png(filename)
