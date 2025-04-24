import socket
import base64
 
host = 'challenge01.root-me.org'
port = 52023
 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
 
response = client_socket.recv(1024)
response_str = response.decode('utf-8')
 
 
encoded_string = response_str.split('\n')[6].split(' ')[3].rstrip('.')
decoded_bytes = base64.b64decode(encoded_string)
decoded_string = decoded_bytes.decode('utf-8')
 
 
result_bytes = (str(decoded_string) + '\n').encode()
client_socket.send(result_bytes)
 
 
response2 = client_socket.recv(1024)
print(response2)