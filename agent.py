import socket
import psutil
import json
import time

HOST = '127.0.0.1'
PORT = 12345
SEND_DATA_INTERVAL = 5

def get_sys_data():
    data = {
        "cpu_freq": psutil.cpu_freq().current,
        "memory_available": psutil.virtual_memory().available,
        "disk_usage_percent": psutil.disk_usage('/').percent,
        "battery": psutil.sensors_battery().percent
    }
    return data

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        print('Sending data...')
        data = get_sys_data()
        s.sendall(json.dumps(data).encode('utf-8')) 
        print('Data sent')
        res = s.recv(1024)
        print('Server response: '+res.decode('utf-8'))
        time.sleep(SEND_DATA_INTERVAL)