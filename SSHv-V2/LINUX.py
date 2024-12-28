import socket

# Impostazioni del client
server_ip = 'VICTIM_IP'  # Cambia con l'IP della macchina Windows
server_port = 12345  # La stessa porta usata dal server

# Crea un socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connettiti al server
client_socket.connect((server_ip, server_port))

# Ricevi i dati inviati dal server
data = client_socket.recv(1024).decode()

# Stampa i dati ricevuti
print(f"{data}")  

# Chiudi la connessione
client_socket.close()
