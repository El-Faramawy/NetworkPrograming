import socket
import tkinter as tk
from tkinter import messagebox

# Server configuration
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 5010  # The port used by the server

# GUI configuration
BUTTON_WIDTH = 15
BUTTON_HEIGHT = 3

# Initialize Tkinter
root = tk.Tk()
root.title('Rock Paper Scissors')

# Create socket connection to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Handle move selection
def on_move_selection(move):
    client_socket.sendall(move.encode('utf-8'))
    result = client_socket.recv(1024).decode('utf-8')
    messagebox.showinfo('Result', result)
    root.quit()

# Create move buttons
rock_btn = tk.Button(root, text='Rock', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                     command=lambda: on_move_selection('Rock'))
rock_btn.pack()

paper_btn = tk.Button(root, text='Paper', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                      command=lambda: on_move_selection('Paper'))
paper_btn.pack()

scissors_btn = tk.Button(root, text='Scissors', width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                         command=lambda: on_move_selection('Scissors'))
scissors_btn.pack()

root.mainloop()
