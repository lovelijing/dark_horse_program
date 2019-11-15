import socket


def send_file_to_client(tcp_client_socket):
    # 01-接收文件名信息
    file_name = (tcp_client_socket.recv(1024)).decode('GBK')
    # 02-打开文件读取数据
    file_data = None
    try:
        file_sendto = open(file_name, 'rb')
        file_data = file_sendto.read()
        file_sendto.close()
    except Exception as ret:
        print(f'打开文件：{file_name} 失败！')
    # 03-发送文件内容给客户端
    if file_data:
        tcp_client_socket.send(file_data)


def tcp_file_sendto_server():
    # 01-创建套接字
    tcp_file_sendto_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 02-绑定本地信息
    tcp_file_sendto_socket.bind(('', 7890))
    # 03-将套接字转化为被动模式
    tcp_file_sendto_socket.listen(128)
    # 04-等待客户端连接
    tcp_client_socket, tcp_client_addres = tcp_file_sendto_socket.accept()
    # 05-调用发送文件函数发送文件内容
    send_file_to_client(tcp_client_socket)
    # 06-关闭套接字
    tcp_file_sendto_socket.close()
    tcp_client_socket.close()


if __name__ == '__main__':
    tcp_file_sendto_server()