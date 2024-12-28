import socket
import os
import platform

# Funzione per ottenere l'IP IPv4 della macchina Windows
def get_ipv4():
    hostname = socket.gethostname()
    ipv4 = socket.gethostbyname(hostname)
    return ipv4

# Funzione per ottenere l'username della macchina Windows
def get_username():
    return os.getlogin()

# Impostazioni del server
host = '0.0.0.0'  # Accetta connessioni da qualsiasi indirizzo IP
port = 12345  # Porta su cui il server ascolterà

# Crea un socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Lega il socket all'indirizzo e alla porta
server_socket.bind((host, port))

# Inizia ad ascoltare le connessioni in arrivo
server_socket.listen(5)

while True:
    # Accetta una connessione in entrata
    client_socket, client_address = server_socket.accept()

    # Ottieni l'IP e l'username
    ipv4 = get_ipv4()
    username = get_username()

    # Prepara il messaggio da inviare al client
    message = f"Username: {username}, IPv4: {ipv4}"

    # Invia il messaggio al client
    client_socket.send(message.encode())

    # Chiudi la connessione con il client
    client_socket.close()
