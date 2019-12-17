import socket


def tcp_file_client():
    # 01-创建套接字
    tcp_file_dowload_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 02-获取服务器IP和PORT
    file_server_addres = ('127.0.0.1', 7890)
    # 03-链接服务器
    tcp_file_dowload_socket.connect(file_server_addres)
    # 04-发送文件名给服务器
    file_name = '文件.txt'
    tcp_file_dowload_socket.send(file_name.encode('GBK'))
    # 05-接收文件内容并写入本地新文件中
    recv_file_data = tcp_file_dowload_socket.recv(1024)
    with open('新'+file_name, 'wb') as file_download:
        file_download.write(recv_file_data)
    # 06-关闭套接字
    tcp_file_dowload_socket.close()


if __name__ == '__main__':
    tcp_file_client()