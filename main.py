from functions import *

if __name__ == '__main__':
    # print('Hello, World!')
    surface, context = create_surface(600, 400, (0.8, 0.8, 0.8))

    write_to_surface(surface, context, 'output.png')
