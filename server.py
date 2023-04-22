import sys
import socket


def ServeHtml(_html_file):
    with open(_html_file, "r") as f:
        html = f.read()
    response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + html
    return response


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 server.py <host> <port>")
        sys.exit(1)

    port = int(sys.argv[1])

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_add = ('127.0.0.1', port)
    sock.bind(server_add)
    sock.listen(1)

    while True:
        connection, client_address = sock.accept()

        response = ServeHtml('example.html')
        connection.sendall(response.encode())

        connection.close()


if __name__ == "__main__":
    main()
