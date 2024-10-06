import tkinter as tk
from random import choice

def play_game(user_choice):
    u=user_choice
    options = ['Rock', 'Paper', 'Scissors']
    computer_choice = choice(options)
    c=computer_choice
    result_label.config(text=f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        result_var.set("It's a tie!")
    elif (
        (user_choice == 'Rock' and computer_choice == 'Scissors') or
        (user_choice == 'Paper' and computer_choice == 'Rock') or
        (user_choice == 'Scissors' and computer_choice == 'Paper')
    ):
        result_var.set(str(u)+" VS " +str(c)+" You win!")
    else:
        result_var.set(str(u)+" VS " +str(c)+" You lose!")

# Create the main window
window = tk.Tk()
window.title("Rock, Paper, Scissors Game")

# Create buttons
rock_button = tk.Button(window, text="Rock", command=lambda: play_game('Rock'))
paper_button = tk.Button(window, text="Paper", command=lambda: play_game('Paper'))
scissors_button = tk.Button(window, text="Scissors", command=lambda: play_game('Scissors'))

# Create result label
result_var = tk.StringVar()
result_label = tk.Label(window, textvariable=result_var, font=('Helvetica', 24, 'bold'))

# Place buttons and result label in the window
rock_button.pack(pady=50)
paper_button.pack(pady=50)
scissors_button.pack(pady=50)
result_label.pack(pady=50)

# Start the GUI event loop
window.mainloop()