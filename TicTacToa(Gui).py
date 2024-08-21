import sys
import pygame
import numpy as np
from pygame.locals import *

pygame.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
gray = (180, 180, 180)

# Proportions and sizes
width, height = 600, 600
line_width = 15
board_rows, board_columns = 3, 3
square_size = width // board_columns
circle_radius = square_size // 3
circle_width = 15
cross_width = 25
space = 55

# Screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(white)

# Board
board = np.zeros((board_rows, board_columns))

# Functions
def draw_lines():
    # Horizontal
    for i in range(1, board_rows):
        pygame.draw.line(screen, black, (0, i * square_size), (width, i * square_size), line_width)
    # Vertical
    for i in range(1, board_columns):
        pygame.draw.line(screen, black, (i * square_size, 0), (i * square_size, height), line_width)

def draw_figures():
    for row in range(board_rows):
        for column in range(board_columns):
            if board[row][column] == 1:
                pygame.draw.circle(screen, red, (int(column * square_size + square_size // 2), int(row * square_size + square_size // 2)), circle_radius, circle_width)
            elif board[row][column] == 2:
                pygame.draw.line(screen, green, (column * square_size + space, row * square_size + square_size - space), (column * square_size + square_size - space, row * square_size + space), cross_width)
                pygame.draw.line(screen, green, (column * square_size + space, row * square_size + space), (column * square_size + square_size - space, row * square_size + square_size - space), cross_width)

def mark_square(row, column, player):
    board[row][column] = player

def available_square(row, column):
    return board[row][column] == 0

def is_board_full():
    return not np.any(board == 0)

def check_win(player):
    # Vertical win check
    for column in range(board_columns):
        if board[0][column] == player and board[1][column] == player and board[2][column] == player:
            #draw_vertical_winning_line(column, player)
            return True
    # Horizontal win check
    for row in range(board_rows):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            #draw_horizontal_winning_line(row, player)
            return True
    # Asc diagonal win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        #draw_asc_diagonal(player)
        return True
    # Desc diagonal win check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        #draw_desc_diagonal(player)
        return True
    return False

def draw_vertical_winning_line(column, player):
    posX = column * square_size + square_size // 2
    color = red if player == 1 else green
    pygame.draw.line(screen, color, (posX, 15), (posX, height - 15), 15)

def draw_horizontal_winning_line(row, player):
    posY = row * square_size + square_size // 2
    color = red if player == 1 else green
    pygame.draw.line(screen, color, (15, posY), (width - 15, posY), 15)

def draw_asc_diagonal(player):
    color = red if player == 1 else green
    pygame.draw.line(screen, color, (15, height - 15), (width - 15, 15), 15)

def draw_desc_diagonal(player):
    color = red if player == 1 else green
    pygame.draw.line(screen, color, (15, 15), (width - 15, height - 15), 15)

def restart():
    screen.fill(white)
    draw_lines()
    global board, game_over, player
    board = np.zeros((board_rows, board_columns))
    game_over = False
    player = 1

# Minimax function for AI
def minimax(board, depth, is_maximizing):
    if check_win(2):
        return 1
    elif check_win(1):
        return -1
    elif is_board_full():
        return 0

    if is_maximizing:
        best_score = -np.inf
        for row in range(board_rows):
            for column in range(board_columns):
                if board[row][column] == 0:
                    board[row][column] = 2
                    score = minimax(board, depth + 1, False)
                    board[row][column] = 0
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = np.inf
        for row in range(board_rows):
            for column in range(board_columns):
                if board[row][column] == 0:
                    board[row][column] = 1
                    score = minimax(board, depth + 1, True)
                    board[row][column] = 0
                    best_score = min(score, best_score)
        return best_score

# Variables
player = 1
game_over = False

def best_move():
    best_score = -np.inf
    move = None
    for row in range(board_rows):
        for column in range(board_columns):
            if board[row][column] == 0:
                board[row][column] = 2
                score = minimax(board, 0, False)
                board[row][column] = 0
                if score > best_score:
                    best_score = score
                    move = (row, column)
    return move

# Play again prompt
def play_again():
    screen.fill(white)  # Clear the screen before showing the play again prompt
    font = pygame.font.Font(None, 74)
    text = font.render("Play Again? (Y/N)", True, black)
    screen.blit(text, (width//2 - text.get_width()//2, height//2 - text.get_height()//2))
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_y:
                    restart()
                    waiting = False
                elif event.key == K_n:
                    pygame.quit()
                    sys.exit()

# Display result message for a few seconds
def display_result_message(message):
    font = pygame.font.Font(None, 74)
    text = font.render(message, True, black)
    screen.blit(text, (width//2 - text.get_width()//2, height//2 - text.get_height()//2))
    pygame.display.flip()
    pygame.time.wait(2000)  # Show the message for 2 seconds

# Main loop
draw_lines()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            clicked_row = int(mouseY // square_size)
            clicked_column = int(mouseX // square_size)
            if available_square(clicked_row, clicked_column):
                mark_square(clicked_row, clicked_column, player)
                draw_figures()
                if check_win(player):
                    game_over = True
                    display_result_message(f"Player {player} Wins!")
                    play_again()
                elif is_board_full():
                    game_over = True
                    display_result_message("It's a Draw!")
                    play_again()
                player = player % 2 + 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()

    if player == 2 and not game_over:
        move = best_move()
        if move is not None:
            row, column = move
            mark_square(row, column, player)
            draw_figures()
            if check_win(player):
                game_over = True
                display_result_message("Player 2 Wins!")
                play_again()
            elif is_board_full():
                game_over = True
                display_result_message("It's a Draw!")
                play_again()
            player = player % 2 + 1

    pygame.display.update()
