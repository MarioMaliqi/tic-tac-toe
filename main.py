#!/usr/bin/env python3
import pygame


def main():
    pygame.init()
    SCREEN_SIZE = (600, 600)
    FPS = 60

    # Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    running = True
    SCREEN = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()

    board = {i:"" for i in range(9)}
    print(board)
    player1_turn = True

    while running:

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                break

            if e.type == pygame.MOUSEBUTTONDOWN:
                cell_idx = handle_mouse(pygame.mouse.get_pos(), SCREEN_SIZE)
                if board[cell_idx] == "":
                    if player1_turn: 
                        board[cell_idx] = "X"
                        player1_turn = False 
                    else: 
                        board[cell_idx] = "O"
                        player1_turn = True 



        SCREEN.fill(BLACK)
        # drawing time
        draw_board(SCREEN, WHITE, SCREEN_SIZE, board)


        pygame.display.update()
        clock.tick(FPS)


def draw_board(screen, color, screen_size, board):
    # TODO: REFACTOR THIS ASAP
    screen_third_x = screen_size[0] // 3
    screen_third_y= screen_size[1] // 3
    screen_two_thirds_x = screen_size[0] // 3 * 2
    screen_two_thirds_y = screen_size[1] // 3 * 2

    pygame.draw.line(screen, color, (0, screen_size[1] // 3), 
                     (screen_size[0], screen_size[1] // 3))
    pygame.draw.line(screen, color, (0, screen_size[1] // 3 * 2), 
                     (screen_size[0], screen_size[1] // 3 * 2))

    pygame.draw.line(screen, color, (screen_size[1] // 3, 0), 
                     (screen_size[1] // 3, screen_size[1]))
    pygame.draw.line(screen, color, (screen_size[1] // 3 * 2, 0), 
                     (screen_size[1] // 3 * 2, screen_size[1]))


def draw_x():
    pass


def draw_o():
    pass


def handle_mouse(mouse, screen_size):
    # TODO: idk i can probably make this better
    screen_third_x = screen_size[0] // 3
    screen_third_y= screen_size[1] // 3
    screen_two_thirds_x = screen_size[0] // 3 * 2
    screen_two_thirds_y = screen_size[1] // 3 * 2


    if mouse[1] > 0 and mouse[1] < screen_third_y:
        if mouse[0] > 0 and mouse[0] < screen_third_x: 
            return 0
        if mouse[0] > screen_third_x and mouse[0] < screen_two_thirds_x:
            return 1
        if mouse[0] > screen_two_thirds_x and mouse[0] < screen_size[0]:
            return 2

    if mouse[1] > screen_third_y and mouse[1] < screen_two_thirds_y:
        if mouse[0] > 0 and mouse[0] < screen_third_x: 
            return 3
        if mouse[0] > screen_third_x and mouse[0] < screen_two_thirds_x:
            return 4
        if mouse[0] > screen_two_thirds_x and mouse[0] < screen_size[0]:
            return 5

    if mouse[1] > screen_two_thirds_y and mouse[1] < screen_size[1]:
        if mouse[0] > 0 and mouse[0] < screen_third_x: 
            return 6
        if mouse[0] > screen_third_x and mouse[0] < screen_two_thirds_x:
            return 7
        if mouse[0] > screen_two_thirds_x and mouse[0] < screen_size[0]:
            return 8


def check_win_condition():
    pass


if __name__ == "__main__":
    main()
