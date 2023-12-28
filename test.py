import socks
import socket
import requests

def set_proxy():
    socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 21080)
    socket.socket = socks.socksocket

def connect_with_proxy():
    # 这里进行网络连接操作
    print(requests.get('http://myip.ipip.net/').text)

# 设置代理
set_proxy()

# 使用代理进行连接
connect_with_proxy()
