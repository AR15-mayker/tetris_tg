import pygame


def handle_input():
    move_left = False
    move_right = False
    rotate = False
    drop = False
    pause = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return None

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left = True
            elif event.key == pygame.K_RIGHT:
                move_right = True
            elif event.key == pygame.K_UP or event.key == pygame.K_z or event.key == pygame.K_x:
                rotate = True
            elif event.key == pygame.K_SPACE:
                drop = True
            elif event.key == pygame.K_ESCAPE:
                pause = True

    return {
        'move_left': move_left,
        'move_right': move_right,
        'rotate': rotate,
        'drop': drop,
        'pause': pause
    }
