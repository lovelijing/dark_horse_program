import socket


def tcp_clinet():
    # 01-创建TCP套接字（TCP链接参数为：socket.SOCK_STREAM）
    tcp_client_socket = (socket.socket(socket.AF_INET, socket.SOCK_STREAM))
    # 02-设置服务器IP地址和端口号
    tcp_sereer_ip = input('请输入服务器IP地址：')
    tcp_server_port = int(input('请输入服务器的端口号：'))
    tcp_addres = (tcp_sereer_ip.encode('GBK'), tcp_server_port)
    # 03-链接服务器
    tcp_client_socket.connect(tcp_addres)
    while True:
        send_data = input('请输入要发送的数据：')
        # 04-发送数据
        tcp_client_socket.send(send_data.encode('GBK'))
        if send_data == 'exit':
            print('本客户端已停止会话！')
            break
        # 05接收数据
        recv_data = tcp_client_socket.recv(1024)
        print(f"远程服务器发来的消息为：{recv_data.decode('GBK')}")
        if recv_data == b'exit':
            print('服务器端停止服务！')
            break
    # 06-关闭套接字)
    tcp_client_socket.close()


if __name__ == '__main__':
    tcp_clinet()