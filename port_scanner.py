import socket, sys

host = '192.168.1.1'
ports = [21, 22, 25, 53,67, 68,80,110,123,143,443,465,631,993,995,3306,3389,8080]

def port_scanner():
    for port in ports:
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
        response = s.recv(1024)
        response = response.decode(errors='ignore').split('\n')[0]
        s.settimeout(2)

        result = s.connect_ex((host, port))
        if result == 0:
            print(f"Puerto {port} <---- ABIERTO {response}")
        else:
            print(f"Puerto {port} cerrado")

        s.close()

port_scanner()