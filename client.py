import sys
import socket


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 client.py <host> <port>")
        sys.exit(1)
    host = sys.argv[1]
    port = int(sys.argv[2])

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = (host, port)
    sock.connect(server_address)

    request = f"GET / HTTP/1.1\r\nHost: {host}\r\n\r\n"
    sock.sendall(request.encode())

    response = sock.recv(1024).decode()
    print(response)


if __name__ == "__main__":
    main()
