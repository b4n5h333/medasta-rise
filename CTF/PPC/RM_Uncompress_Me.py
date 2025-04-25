import socket
import zlib
import base64
host = 'challenge01.root-me.org'
port = 52022
 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
 
while True:
    response = client_socket.recv(1024)
    print(response)
    response_str = str(zlib.decompress(base64.b64decode(response.decode('utf-8').split()[-6][1:-2])).decode() + "\n").encode()

    client_socket.send(response_str)

