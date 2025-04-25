import socket
from math import sqrt

 
host = 'challenge01.root-me.org'
port = 52002
 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
 
response = client_socket.recv(1024)
response_str = response.decode('utf-8').split()

print(response_str)

value_2, value_1 = int(response_str[-2]), int(response_str[-6])
print(value_1, value_2)
result = (str(round(sqrt(value_1) * value_2, 2)) + "\n").encode()

client_socket.send(result)

response = client_socket.recv(1024).decode('utf-8')
print(response)