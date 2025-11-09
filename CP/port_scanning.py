import socket

target = '127.0.0.1'  
ports = [80, 443, 3000, 5000, 8000]  

print(f"Scanning {target}...\n")

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is OPEN")
    else:   
        print(f"Port {port} is CLOSED")
    sock.close()