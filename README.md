**Title:** Advanced Tic Tac Toe Game with AI Using Pygame

---

**Description:**

This project is a fully functional Tic Tac Toe game developed using Python and Pygame. It features a simple yet engaging GUI and incorporates an AI opponent using the Minimax algorithm. The game supports single-player mode against the AI and offers a replay option once a game concludes. Below is a detailed explanation of the features and components of this project.

---

**Features:**
- **2D Game Board:** A 3x3 grid representing the Tic Tac Toe board.
- **Player vs AI:** Play against a computer opponent with the AI implementing the Minimax algorithm.
- **Game State Management:** Handles win, draw, and game restart scenarios.
- **Dynamic Graphics:** Draws circles and crosses for player moves and highlights winning lines.
- **Input Handling:** Processes mouse clicks and keyboard inputs for game interactions.
- **Replay Functionality:** Prompts the user to play again or exit after the game ends.

---

**Technical Details:**

- **Libraries Used:**
  - `pygame`: For creating the graphical user interface and handling game events.
  - `numpy`: For managing the game board and performing matrix operations.

- **Game Mechanics:**
  - **Board Representation:** Uses a 2D NumPy array to represent the board state.
  - **Drawing Functions:** Custom functions to draw lines, circles, and crosses on the game board.
  - **AI Algorithm:** Implements the Minimax algorithm to determine the optimal move for the AI player.
  - **Event Handling:** Captures and processes user inputs to make moves and restart the game.

- **Game Logic:**
  - **Win Conditions:** Checks for horizontal, vertical, and diagonal win conditions.
  - **Minimax Algorithm:** Evaluates possible moves for the AI to select the best move.
  - **User Interface:** Updates the game display based on user interactions and game state changes.

---

**Code Highlights:**

- **Drawing Functions:**
  ```python
  def draw_lines():
      # Horizontal and vertical lines for the board
      for i in range(1, board_rows):
          pygame.draw.line(screen, black, (0, i * square_size), (width, i * square_size), line_width)
      for i in range(1, board_columns):
          pygame.draw.line(screen, black, (i * square_size, 0), (i * square_size, height), line_width)
  ```

- **Minimax Algorithm:**
  ```python
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
  ```

- **Play Again Prompt:**
  ```python
  def play_again():
      screen.fill(white)
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
  ```

---

**Getting Started:**

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/twonum/tic-tac-toe-ai.git
   ```

2. **Install Dependencies:**
   Make sure you have `pygame` and `numpy` installed. You can install them using pip:
   ```bash
   pip install pygame numpy
   ```

3. **Run the Game:**
   Execute the script using Python:
   ```bash
   python tic_tac_toe.py
   ```

---

**Contributions:**

Feel free to fork the repository and make contributions. Issues and pull requests are welcome!

---

**License:**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Contact:**

For any questions or suggestions, you can reach out to me at [tahasaleem.professional@gmail.com].

---

Feel free to customize the content according to your specific needs or preferences!
