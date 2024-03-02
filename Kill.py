import socket

host = input("Enter the host: ")
port = int(input("Enter the port: "))
buffer_size = int(input("Enter the buffer size: "))
custom_request = input("Enter the custom HTTP request: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    s.sendall(custom_request.encode())

    response = b""
    while True:
        data = s.recv(buffer_size)
        if not data:
            break
        response += data

print(response.decode())

