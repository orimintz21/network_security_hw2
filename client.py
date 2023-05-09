# based on https://docs.python.org/3/library/socket.html
import sys
import socket

host = None
port = None
# Get the host and port number from the command line arguments
if len(sys.argv) != 3:
    print("Usage: python3 client.py <host> <port>")
    sys.exit(1)
else:
    host = sys.argv[1]
    port = int(sys.argv[2])

# Connect to the server and send a GET request
for res in socket.getaddrinfo(host, port, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        sock = socket.socket(af, socktype, proto)
    except OSError as msg:
        # failed to create a socket
        sock = None
        continue
    try:
        sock.connect(sa)
    except OSError as msg:
        # failed to connect to the socket
        sock.close()
        sock = None
        continue
    break
# If we could not open a socket, exit
if sock is None:
    print("could not open socket")
    sys.exit(1)
# Send the GET request
with sock:
    request = "GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(host)
    sock.send(request.encode())
    response = sock.recv(1024).decode()
print(response)
