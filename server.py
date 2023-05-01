# based on https://docs.python.org/3/library/socket.html
import sys
import sys
import socket

port = None
html = None

# Load the HTML file
with open('example.html', "r") as f:
    html = f.read()
response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + html

# Get the port number from the command line argument
if len(sys.argv) != 2:
    print("Usage: python3 server.py <port>")
    sys.exit(1)
else:
    port = int(sys.argv[1])

sock = None
for res in socket.getaddrinfo('127.0.0.1', port, socket.AF_UNSPEC, socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
    af, socktype, proto, canonname, sa = res
    try:
        sock = socket.socket(af, socktype, proto)
    except OSError as msg:
        # failed to create a socket
        sock = None
        continue
    try:
        sock.bind(sa)
        sock.listen(1)
    except OSError as msg:
        sock.close()
        sock = None
        continue
    break
if sock is None:
    print("Could not open socket")
    sys.exit(1)

# Accept connections and send the HTML response
try:
    while True:
        conn, addr = sock.accept()
        with conn:
            conn.sendall(response.encode())
finally:
    sock.close()
