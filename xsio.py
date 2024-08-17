import tkinter #tk-interface (graphical user interface library)

def set_tile(row, column):
    global curr_player

    if (game_over):
        return
     
    if board[row][column]["text"] ! ="":
        #loc deja luat
        return

    board[row][column]["text"] = curr_player #marcheaza placa

    if curr_player == playerO: #schimba jucatorul
       curr_player == playerX
    else:
        curr_player = playerO

    label["text"] = curr_player+"randul lui s"

    #verifica castigatorul
    check_winner()

def check_winner():
    global turns, game_over
    turns += 1

    #orizontal, verifica 3 coloane
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"])
        and board[row][0]["text"] ! = ""):
        label.config(text=board[row][0]["text"]+" este castigatorul!", foreground=color_yellow)
        for column in range(3):
            board[row][column].config(foreground=color_yellow, background=color_light_gray)
        game_over = True
        return
      
    #vertical verifica 3 coloane
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
            and board[0][column]["text"] ! = ""):
            label.config(text=board[0][column]["text"]+" este castigatorul!", foreground=color_yellow)
            for row in range(3):
                board[row][column].config(foreground=color_yellow, background=color_light_gray)
            game_over = True
            return

    #diagonal
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
        and board[0][0]["text"] ! =""):
        label.config(text=board[0][0]["text"]+" este castigatorul!", foreground=color_yellow)
        for i in range(3):
            board[i][i].config(foreground=color_yellow, background=color_light_gray)
        game_over = True
        return

    #anti-diagonal
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
    and board[0][2]["text"] ! = ""):
    label.config(text=board[0][2]["text"]+" este castigatorul!", foreground=color_yellow)
    board[0][2].config(foreground=color_yellow, background=color_light_gray)
    board[1][1].config(foreground=color_yellow, background=color_light_gray)
    board[2][0].config(foreground=color_yellow, background=color_light_gray)
    game_over = True
    return

    #egalitate
    if (turns == 9):
        game_over = True
        label.config(text="Egalitate!", foreground=color_yellow)


def new_game():
    global turns, game_over

    turns = 0
    game_over = False 

    label.config(text=curr_player+"s turn", foreground="white")

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=color_purple, background=color_black)

    
#setupul jocului
playerX = "X"
playerO = "O"
curr_player = playerX
board [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]

color_purple = "#6400cf"
color_yellow = "#e5ff00"
color_gray = "#333330"
color_light_gray = "#858585"

turns = 0 
game_over = False 

#window setup 
window = tkinter.Tk() #creeaza fereastra jocului
window.title("X si O")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=curr_player+"s turn", font=("Consolas", 20), background=color_gray,
                      foreground="white")
label.grid(row=0, column=0, columnspan=3, sticky="noi")

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Consolas", 50, "bold"),
                                            background=color_gray, foreground=color_purple, width=4, height=1,
                                            command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row+1, column=column)

        button = tkinter.Button(frame, text="restart", font=("Consolas", 20), background=color_gray,
                                foreground="white", command=new_game)
        button.grid(row=4, column=0, columnspan=3, sticky="we")

        frame.pack()

        #centreaza fereastra
        window.update()
        window_width = window.winfo_width()
        window_height = window.window_height()
        screen_width = window.winfo_screenwidth()
        screen_height = window.windo_screenheight()

        window_x = int((screen_width/2) - (window_width/2))
        window_y = int((screen_height/2) - (window_height/2))

        #formateaza "(w)x(h)+(x)+(y)"
        window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

        window.mainloop()
