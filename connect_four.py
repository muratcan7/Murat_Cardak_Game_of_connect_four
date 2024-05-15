import tkinter as tk
from tkinter import messagebox

class ConnectFourGUI:  # GUI for Connect Four game
    def __init__(self, master, rows=6, cols=7, win_length=4):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.win_length = win_length
        self.grid = [['.' for _ in range(cols)] for _ in range(rows)]
        self.player_turn = 'Red' # Red goes first
        self.buttons = []

        self.master.title("Connect Four")  # Set title of window
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.create_grid_interface()
        self.label = tk.Label(self.master, text=f"{self.player_turn}'s Turn", font=("Arial", 16))
        self.label.pack(side=tk.TOP, pady=10)

    def create_grid_interface(self):  # Create grid interface for Connect Four game
        for col in range(self.cols):
            button = tk.Button(self.frame, text=str(col), command=lambda c=col: self.insert_token(c), font=("Arial", 14), height=2, width=4)
            button.grid(row=0, column=col)
            self.buttons.append(button)

        self.canvas = tk.Canvas(self.master, width=35*self.cols, height=35*self.rows)
        self.canvas.pack()
        # Draw grid lines
        for row in range(self.rows):
            for col in range(self.cols):
                self.canvas.create_rectangle(col*35, row*35, col*35+35, row*35+35, fill='white', outline='blue')

    def insert_token(self, column):  # Insert token into the grid
        if self.grid[0][column] != '.':
            messagebox.showerror("Invalid Move", "Column is full!")
            return

        for i in range(self.rows-1, -1, -1):
            if self.grid[i][column] == '.':
                self.grid[i][column] = 'R' if self.player_turn == 'Red' else 'Y'
                self.canvas.create_oval(column*35+5, i*35+5, column*35+30, i*35+30, fill='red' if self.player_turn == 'Red' else 'yellow', outline='blue')
                if self.check_winner():
                    self.end_game(f"{self.player_turn} wins!")
                else:
                    self.toggle_player()
                    self.label.config(text=f"{self.player_turn}'s Turn")
                return

    def toggle_player(self):  # Toggle player turn
        self.player_turn = 'Yellow' if self.player_turn == 'Red' else 'Red'

    def check_winner(self):  # Check if there is a winner
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] != '.':
                    for dr, dc in directions:
                        win = True
                        for n in range(1, self.win_length):
                            r, c = row + dr*n, col + dc*n
                            if r < 0 or r >= self.rows or c < 0 or c >= self.cols or self.grid[row][col] != self.grid[r][c]:
                                win = False
                                break
                        if win:
                            return True
        return False

    def end_game(self, message):  # End game
        messagebox.showinfo("Game Over", message)
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ConnectFourGUI(root)
    root.mainloop()
