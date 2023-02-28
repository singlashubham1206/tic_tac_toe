import tkinter as tk

# GUI class for tic tac toe
class TicTacToe(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Tic Tac Toe")
        self.master.resizable(False, False)
        self.create_widgets()
        
        self.pos = ['',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        self.players = ['','']
        self.winning_conditions = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
        self.turn = 0
        
    # method to create widgets
    def create_widgets(self):
        # create board
        self.board = tk.Frame(self.master, bg='white')
        self.board.grid(row=0, column=0, padx=10, pady=10)
        for i in range(3):
            for j in range(3):
                cell = tk.Button(self.board, text="", font=('Arial', 20), width=5, height=2, command=lambda row=i, col=j:self.click_cell(row, col))
                cell.grid(row=i, column=j, padx=5, pady=5)
                self.board.grid_rowconfigure(i, weight=1)
                self.board.grid_columnconfigure(j, weight=1)
        
        # create instructions
        self.instructions = tk.Frame(self.master, bg='white')
        self.instructions.grid(row=0, column=1, padx=10, pady=10)
        tk.Label(self.instructions, text="Player 1:").grid(row=0, column=0, padx=5, pady=5)
        self.player1_entry = tk.Entry(self.instructions)
        self.player1_entry.grid(row=0, column=1, padx=5, pady=5)
        tk.Label(self.instructions, text="Player 2:").grid(row=1, column=0, padx=5, pady=5)
        self.player2_entry = tk.Entry(self.instructions)
        self.player2_entry.grid(row=1, column=1, padx=5, pady=5)
        self.start_button = tk.Button(self.instructions, text="Start Game", command=self.start_game)
        self.start_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        
    # method to handle cell clicks
    def click_cell(self, row, col):
        if self.turn % 2 == 0:
            value = 'x'
        else:
            value = '0'
        cell_value = self.pos[3*row+col+1]
        if cell_value == ' ':
            self.board.grid_slaves(row=row, column=col)[0].config(text=value)
            self.pos[3*row+col+1] = value
            winner = self.check_win(value)
            if winner is not None:
                self.end_game(winner)
                return
            self.turn += 1
    
    # method to start game
    def start_game(self):
        player1_name = self.player1_entry.get().strip()
        player2_name = self.player2_entry.get().strip()
        if player1_name and player2_name:
            self.players[0] = player1_name
            self.players[1] = player2_name
            self.instructions.grid_forget()
            self.board.grid()
        else:
            tk.messagebox.showerror("Error", "Please enter player names.")
    
    # method
