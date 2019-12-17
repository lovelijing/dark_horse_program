import socket


class tcp_server():
    def __init__(self):
        # 01-创建监听TCP套接字（TCP链接参数为：socket.SOCK_STREAM）
        self.__socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 02-绑定本机（服务器）的IP地址和端口号 bind
        self.__socket_server.bind(('', 7890))
        # 03-将套接字由主动变为被动 listen （1-3是固定的流程）
        self.__socket_server.listen(128)
        print('\n\n服务器已启动\n')

    def server(self):
        count = 1
        while True:
            print(f'\n正在等待第{count}个客户端连接进来......')
            # 04-等待客户端的链接 accept，一旦有客户端链接就生成新的套接字和返回客户端的IP地址和端口号
            new_client_socket, new_client_addres = self.__socket_server.accept()
            print(f'第{count}个客户已连接进来，客户信息为{new_client_addres}')
            print('-----------服务开始-----------')
            while True:
                # 05-用新的套接字接收客户端数据 recv
                message = new_client_socket.recv(1024)
                if message:
                    print(message.decode('GBK'))
                    # 06-用新的套接字发送信息
                    new_client_socket.send('欢迎光临！'.encode('GBK'))
                else:
                    break
            print(f'第{count}个客户端已结束所需服务！\n\n')
            # 07-关闭 accept 生成的新套接字
            new_client_socket.close()
            count = count + 1
            if count > 3:
                yorn = input('您已为3个客户提供了服务，现在想继续为客户服务吗？(y/n)')
                if yorn.upper() == 'Y':
                    count = 1
                else:
                    break

    def __del__(self):
        # 08-关闭监听套接字
        self.__socket_server.close()
        print('服务器已停机！！！')


if __name__ == '__main__':
    myserver = tcp_server()
    myserver.server()
