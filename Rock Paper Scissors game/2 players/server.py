import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set up the server address and port
server_address = ('localhost', 8015)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(2)
print("Waiting for connections...")

# Accept two client connections
player1_socket, player1_address = server_socket.accept()
print("Player 1 connected:", player1_address)

player2_socket, player2_address = server_socket.accept()
print("Player 2 connected:", player2_address)

# Game logic
def play_game(player1_socket, player2_socket):
    while True:
        # Receive moves from both players
        player1_move = player1_socket.recv(1024).decode()
        player2_move = player2_socket.recv(1024).decode()

        # Determine the winner
        if player1_move == player2_move:
            result = "It's a tie!"
        elif (
            (player1_move == "rock" and player2_move == "scissors")
            or (player1_move == "paper" and player2_move == "rock")
            or (player1_move == "scissors" and player2_move == "paper")
        ):
            result = "Player 1 wins!"
        else:
            result = "Player 2 wins!"

        # Send the result to both players
        player1_socket.sendall(result.encode())
        player2_socket.sendall(result.encode())

        # Break the loop if any player wants to quit
        if player1_move == "quit" or player2_move == "quit":
            break

    # Close the connections
    player1_socket.close()
    player2_socket.close()
    server_socket.close()

# Start the game
play_game(player1_socket, player2_socket)
