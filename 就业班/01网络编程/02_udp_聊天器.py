import socket


def send_msg(udp_socket, ip = '127.0.0.1', port = 7788):  # 发送信息的函数
    send_data = input('请输入要发送的数据：')
    if send_data == 'exit':
        return True
    udp_socket.sendto(send_data.encode('GBK'), (ip, port))
    return False


def recv_msg(udp_socket):  # 接收信息的函数
    recv_data = udp_socket.recvfrom(1024)
    if recv_data[0] == b'exit':
        return True
    print(f"从{recv_data[1]}发来消息：{recv_data[0].decode('GBK')}")
    return False


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dest_addr = ('', 7700)
    udp_socket.bind(dest_addr)
    send_ip = input('请输入远程主机的IP(回车为本机IP):')
    if send_ip == '':
        send_ip = '127.0.0.1'
    try:
        send_port = int(input('请输入远程主机的PORT：'))
    except ValueError:
         send_port = 7788
    while True:
        if send_msg(udp_socket, send_ip, send_port):
            print('自己结束会话！')
            break
        if recv_msg(udp_socket):
            print('对方结束会话！')
            break
    udp_socket.close()


if __name__ == '__main__':
    main()
