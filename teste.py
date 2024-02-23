import socket

# Define o endereço IP e a porta para o servidor
HOST = '0.0.0.0'  # IP do servidor (0.0.0.0 significa todas as interfaces disponíveis)
PORT = 12345      # Porta a ser usada

# Cria o socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associa o socket com o endereço e porta especificados
server_socket.bind((HOST, PORT))

# Coloca o servidor em modo de escuta
server_socket.listen(1)

print(f"Servidor escutando em {HOST}:{PORT}")

# Aguarda por conexões
while True:
    # Aceita uma conexão
    client_socket, client_address = server_socket.accept()
    
    print(f"Conexão recebida de {client_address}")
    
    # Recebe os dados enviados pelo cliente
    data = client_socket.recv(1024)
    if not data:
        break
    
    print(f"Dados recebidos: {data.decode()}")
    
    # Envie uma resposta de volta ao cliente
    client_socket.sendall(b"Recebido. Obrigado!")

# Fecha a conexão com o cliente
client_socket.close()

# Fecha o socket do servidor
server_socket.close()