import socket
import base64
import re
host = 'challenge01.root-me.org'
port = 52017
 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

def base32_decode(line: str) -> str:
    return base64.b32decode(line).decode() 

def base85_decode(line: str) -> str:
    return base64.b85decode(line).decode()

def base64_decode(line: str) -> str:
    return base64.b64decode(line).decode()

def hex_decode(line: str) -> str:
    return bytes.fromhex(line).decode('utf-8')

def morse_decode(line: str) -> str:
    line = line.replace("/", " ")
    encode_table = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    " ": "SPACE",
    }
    decode_table = {v: k for k, v in encode_table.items()}
    symbols = line.replace("   ", " SPACE ").split(" ")
    return "".join(decode_table[x] for x in symbols)


for i in range(200):
    response = client_socket.recv(1024)
    print(response)
    response_str = response.decode('utf-8').split()[-2][1:-1]
    result = 0 
    if re.fullmatch(r'[./-]+', response_str):
        result = (morse_decode(response_str).lower() + "\n").encode()
    elif re.fullmatch(r'[0-9a-f]+', response_str):
        result = (hex_decode(response_str) + "\n").encode()
    elif re.fullmatch(r'[A-Z2-7=]+', response_str):
        result = (base32_decode(response_str) + "\n").encode()
    elif re.fullmatch(r'[A-Za-z0-9+/=]+', response_str):
        result = (base64_decode(response_str) + "\n").encode()
    else:
        result = (base85_decode(response_str) + "\n").encode()
    client_socket.sendall(result)