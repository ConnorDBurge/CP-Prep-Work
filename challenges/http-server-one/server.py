import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# so you don't have to change ports when restarting
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('localhost', 9292))
print('Waiting For Connection...')
server.listen()

while True:
    client_connection, _client_address = server.accept()
    data = client_connection.recv(1024).decode()

    print('GET request received')
    message = "HTTP/1.0 200 OK\nContent-Type: text\plain\n\n<html><body><p>Hello World!</p></body></html>\n".encode()
    client_connection.send(message)

    client_connection.close()
