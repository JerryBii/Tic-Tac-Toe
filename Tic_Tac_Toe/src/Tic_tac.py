import numpy as np
import pygame
import sys
import math
ROWS = 3
COLS = 3
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def create_board():
    return np.zeros((ROWS, COLS))

def draw_board(board):
    for c in range(COLS):
        for r in range(ROWS):
            pygame.draw.rect(screen, WHITE,(c*SIZE, r*SIZE, SPOT_SIZE, SPOT_SIZE))
    for c in range(COLS):
        for r in range(ROWS):
            if board[r][c] == 1:
                pygame.draw.circle(screen, BLACK, (int(c*SIZE + SIZE/2 - X_OFFSET), int(r*SIZE + SIZE/2 - Y_OFFSET)), 70)
                pygame.draw.circle(screen, WHITE,(int(c * SIZE + SIZE / 2 - X_OFFSET), int(r * SIZE + SIZE / 2 - Y_OFFSET)), 50)
            elif board[r][c] == 2:
                x =shape.render('X', 1, BLACK)
                screen.blit(x, (int(c*SIZE + SIZE/5), int(r*SIZE - Y_OFFSET_2)))
    pygame.display.update()


def valid_spot(board, row_num, col_num):
    if board[row_num][col_num] == 0:
        return True
    else:
        return False

def place_piece(board, row_num, col_num, piece):
    board[row_num][col_num] = piece

def check_win(board, piece):
    #Horizontal wins
    for c in range(COLS - 1):
        for r in range(ROWS):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c-1] == piece:
                return True
    #Vertical wins
    for c in range(COLS):
        for r in range(ROWS - 1):
            if board[r][c] == piece and board[r+1][c] == piece and board[r-1][c] == piece:
                return True

    #sloped wins (negative)
    for c in range(COLS - 2):
        for r in range(ROWS - 2):
            if board[r][c] == piece and board[r - 1][c - 1] == piece and board[r - 2][c - 2] == piece:
                return True

    #sloped wins (positive)
    for c in range(COLS - 2):
        for r in range(ROWS - 2):
            if board[r + 2][c] == piece and board[r + 1][c + 1] == piece and board[r][c + 2] == piece:
                return True


board = create_board()
print(board)

in_play = True

pygame.init()
SIZE = 200
BOARD_SIZE = 190
SPOT_SIZE = 170
MESSAGE_BOX = 100
X_OFFSET =  15
Y_OFFSET = 15
Y_OFFSET_2 = 20

width = ROWS * BOARD_SIZE
height = COLS * BOARD_SIZE + MESSAGE_BOX

size = (width, height)

shape = pygame.font.SysFont('Arial', 180, bold= True)
message = pygame.font.SysFont('Arial', 25, bold = True)
screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

def play_again():
    new_board = create_board()
    pygame.draw.rect(screen, BLACK, (0, 500, SPOT_SIZE * 10, SPOT_SIZE))
    draw_board(new_board)
    game_play(new_board,True )

def game_play(board, in_play):
    turn = 0
    while in_play:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if turn >= 9:

                print('TIE GAME Press spacebar to play again')
                text = message.render('TIE GAME... game will restart automatically', 1, WHITE)
                screen.blit(text, (50, 600))
                pygame.display.update()
                in_play = False
                pygame.time.wait(1500)
                if not in_play:
                    board = create_board()
                    draw_board(board)
                    play_again()

            if event.type ==pygame.MOUSEMOTION:
                posx,posy = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if turn%2 == 0:
                    posx, posy = pygame.mouse.get_pos()
                    row = int(math.floor(posy/BOARD_SIZE))
                    column = int(math.floor(posx/BOARD_SIZE))
                    if valid_spot(board,row,column):
                        place_piece(board, row, column, 1)
                        draw_board(board)
                        turn += 1
                    else:
                        print('Invalid Spot, skipping your turn...')
                    if check_win(board, 1):
                        print('Player 1 WINS! Press spacebar to play again')
                        text = message.render('PLAYER 1 WINS!! game will restart automatically', 1, WHITE)
                        screen.blit(text, (50,600))
                        pygame.display.update()
                        in_play = False
                        print(board)
                        if not in_play:
                            pygame.time.wait(1500)
                            board = create_board()
                            draw_board(board)
                            play_again()


                else:
                    posx, posy = pygame.mouse.get_pos()
                    row = int(math.floor(posy / BOARD_SIZE))
                    column = int(math.floor(posx / BOARD_SIZE))
                    if valid_spot(board, row, column):
                        place_piece(board, row, column, 2)
                        draw_board(board)
                        turn += 1
                    else:
                        print('Invalid spot, skipping your turn...')
                    if check_win(board, 2):
                        print('Player 2 WINS! Press spacebar to play again')
                        text = message.render('PLAYER 2 WINS!! game will restart automatically', 1, WHITE)
                        screen.blit(text, (50, 600))
                        pygame.display.update()
                        in_play = False
                        print(board)
                        if not in_play:
                            pygame.time.wait(1500)
                            board = create_board()
                            draw_board(board)
                            play_again()

                print(board)

game_play(board,in_play)
