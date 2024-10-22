import math
from functions import *

if __name__ == '__main__':

    surface, context = create_surface(500, 700, (0.8, 0.8, 0.8))

    draw_line(context, 50,300, 50, 350, (0, 0, 1), 2)
    draw_line(context, 50, 350, 100, 350, (0, 0, 1), 2)
    draw_line(context, 100, 350, 100, 650, (0, 0, 1), 2)
    draw_line(context, 100, 650, 400, 650, (0, 0, 1), 2)
    draw_line(context, 400, 650, 400, 350, (0, 0, 1), 2)
    draw_line(context, 400, 350, 450, 350, (0, 0, 1), 2)
    draw_line(context, 400, 350, 450, 350, (0, 0, 1), 2)
    draw_line(context, 450, 350, 450, 300, (0, 0, 1), 2)
    draw_line(context, 450, 300, 50, 300, (0, 0, 1), 2)

    draw_arc(context, 250,300, 125, math.pi, 2*math.pi, (0,0, 1), 2)
    draw_arc(context, 400, 100, 70, (math.pi/4), (5*math.pi/4), (0,0,1), 2)
    # draw_arc(context, 400, 100, 70, (math.pi / 4), (5 * math.pi / 4), (0, 0, 1), 2)


    write_to_surface(surface, context, 'output.png')

