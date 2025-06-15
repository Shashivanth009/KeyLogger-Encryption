import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))
server.listen(1)
print("[*] Waiting for logs...")

while True:
    client, addr = server.accept()
    data = client.recv(4096)
    print(f"\n[+] Logs received from {addr}:\n{data.decode(errors='ignore')}")
    client.close()
