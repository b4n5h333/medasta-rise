import socket
from math import sqrt

host = 'challenge01.root-me.org'
port = 	52018
 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

def polynomial_solver(a:int, b:int, c:int) -> float:
        D = (b ** 2) - (4 * a * c)

        if D > 0:
            x_1 = ((b * -1) + sqrt(D)) / (2 * a)
            x_2 = ((b * -1) - sqrt(D)) / (2 * a)
            return str("x1: " + ('%.3f' % x_1) + " ; " + "x2: " + ('%.3f' % x_2) + "\n").encode()
        elif D == 0:
            x = (b * -1) / (2 * a)
            return str("x:" + ('%.3f' % x) + "\n").encode()
        else:
            return ("Not possible" + "\n").encode()
        
while True:
    response = client_socket.recv(1024).decode().split()
    print(response)

    a_value = int(response[-8].split(".")[0])
    b_value = int(response[-7] + response[-6].split(".")[0])
    c_value = int(response[-5] + response[-4]) + (int(response[-2]) * -1)

    client_socket.send(polynomial_solver(a_value,b_value,c_value))

    