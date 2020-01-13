import socket


def http_client(new_socket):
    get_data = new_socket.recv(1024)
    print(get_data)
    html_data = "http/1.1 200 ok\r\n\r\n <h1>你好！我还在运行着。</h1>"
    new_socket.send(html_data.encode('GBK'))
    new_socket.close()


def main():
    http_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    http_socket.bind(('', 17788))
    http_socket.listen(128)
    while True:
        new_socket, client_address = http_socket.accept()
        http_client(new_socket)
    http_socket.close()


if __name__ == '__main__':
    main()