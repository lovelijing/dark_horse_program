import socket
import threading

end_socket = True


def send_msg(udp_socket, udp_addres):
    """获取键盘数据，并将其发送给对方"""
    global end_socket
    while True:
        send_data = input('请输入要发送的数据：')
        if send_data == 'exit' or end_socket == False:
            print('您要结束会话，请等待对方退出会话！！！')
            end_socket = False
            break
        udp_socket.sendto(send_data.encode('GBK'), udp_addres)


def recv_msg(udp_socket):
    """接收数据并显示"""
    global end_socket
    while True:
        recv_data = udp_socket.recvfrom(1024)
        if recv_data[0] == b'exit' or len(recv_data)== 0 or end_socket == False:
            print('\n对方要结束了会话了，请确认！！！')
            end_socket = False
            break
        print(f'\n收到的信息为：{recv_data[0].decode("GBK")}')


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(('192.168.2.100', 7890))
    udp_ip = input('请输入对方的IP地址：')
    udp_port = int(input('请输入对方的端口号：'))
    udp_addres = (udp_ip, udp_port)

    t_recv_thread = threading.Thread(target = recv_msg, args = (udp_socket,))
    t_send_thread = threading.Thread(target = send_msg, args = (udp_socket, udp_addres))
    t_send_thread.start()
    t_recv_thread.start()


if __name__ == '__main__':
    main()