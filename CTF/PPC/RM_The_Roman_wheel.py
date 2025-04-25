import socket
import codecs


host = 'challenge01.root-me.org'
port = 52021
 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
 
response = client_socket.recv(1024)
response_str = response.decode('utf-8').split()

roman_wheel_value = str(codecs.decode(response_str[-6][1:-2], "rot_13") + '\n').encode()

client_socket.send(roman_wheel_value)

response = client_socket.recv(1024).decode('utf-8')
print(response)