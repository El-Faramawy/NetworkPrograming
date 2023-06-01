import socket
import tkinter as tk

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set up the server address and port
server_address = ('localhost', 8015)

# Connect to the server
client_socket.connect(server_address)

# GUI
def send_move(move):
    # Send the player's move to the server
    client_socket.sendall(move.encode())
	
    	
    # Receive and display the result from the server
    result = client_socket.recv(1024).decode()
    label_result['text'] = result

# Create a Tkinter window
window = tk.Tk()
window.geometry("200x200")
window.title("Rock Paper Scissors")

# Create a label for instructions
label_instructions = tk.Label(window, text="Player 1")
label_instructions.configure(fg="red")
label_instructions.pack()

label_instructions2 = tk.Label(window, text="Choose your move:")
label_instructions2.pack()


# Create buttons for rock, paper, and scissors
button_rock = tk.Button(window, text="Rock", command=lambda: send_move("rock"))
button_rock.pack()

button_paper = tk.Button(window, text="Paper", command=lambda: send_move("paper"))
button_paper.pack()

button_scissors = tk.Button(window, text="Scissors", command=lambda: send_move("scissors"))
button_scissors.pack()

# Create a label for displaying the result
label_result = tk.Label(window, text="")
label_result.configure(fg="red")
label_result.pack()

# Start the Tkinter event loop
window.mainloop()

# Close the connection
client_socket.close()
