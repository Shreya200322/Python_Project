import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        
        self.player1 = "Harry"
        self.player2 = "Sherry"
        self.current_player = self.player1
        self.board = [""] * 9
        
        self.buttons = [tk.Button(master, text="", font='Arial 20', width=5, height=2,
                                   command=lambda i=i: self.make_move(i)) for i in range(9)]
        
        for i, button in enumerate(self.buttons):
            button.grid(row=i // 3, column=i % 3)
        
        self.new_game_button = tk.Button(master, text="New Game", command=self.new_game)
        self.new_game_button.grid(row=3, column=0, columnspan=2)
        
        self.close_button = tk.Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=3, column=2)

    def make_move(self, index):
        if self.board[index] == "":
            self.board[index] = "X" if self.current_player == self.player1 else "O"
            self.buttons[index].config(text=self.board[index])
            if self.check_winner():
                messagebox.showinfo("Game Over", f"{self.current_player} wins!")
                self.new_game()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.new_game()
            else:
                self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontal
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertical
            (0, 4, 8), (2, 4, 6)              # diagonal
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return True
        return False

    def new_game(self):
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="")
        self.current_player = self.player1

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()