import socket, sys

myDomain = sys.argv[1]

def whois_lookup():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('whois.iana.org',43))
    s.send(f'{myDomain}\r\n'.encode())
    response = s.recv(4096).decode()
    s.close()
    return response

print(whois_lookup())