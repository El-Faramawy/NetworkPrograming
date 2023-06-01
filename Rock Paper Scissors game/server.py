import random
import socket

# Server configuration
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 5010  # The port used by the server

# Game options
OPTIONS = ['Rock', 'Paper', 'Scissors']

# Create socket connection to the client
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f'Server listening on {HOST}:{PORT}')

# Accept client connection
client_socket, _ = server_socket.accept()
print(f'Client connected: {client_socket.getsockname()}')

# Game logic
def get_game_result(move1, move2):
    if move1 == move2:
        return 'Draw'
    elif (
        (move1 == 'Rock' and move2 == 'Scissors') or
        (move1 == 'Paper' and move2 == 'Rock') or
        (move1 == 'Scissors' and move2 == 'Paper')
    ):
        return 'Player wins'
    else:
        return 'Server wins'

while True:
    data = client_socket.recv(1024).decode('utf-8')
    if not data:
        break
    if data in OPTIONS:
        server_move = random.choice(OPTIONS)
        result = get_game_result(data, server_move)
        client_socket.sendall(result.encode('utf-8'))
    else:
        client_socket.sendall('Invalid move. Please choose Rock, Paper, or Scissors.'.encode('utf-8'))

client_socket.close()
server_socket.close()
