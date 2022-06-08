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
        try :
            s.sendall(json.dumps(data).encode('utf-8')) 
            print('Data sent')
            res = s.recv(1024)
            print('Server response: '+res.decode('utf-8'))    
        except socket.error as e:
            connected = False
            print('Connection lost')
            print('Error: '+str(e))
            print('Trying to reconnect...')

            connected = False
            while not connected: # try to reconnect
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((HOST, PORT))
                    connected = True
                    print('Connected')
                except socket.error as e:
                    print('Error: '+str(e))
                    time.sleep(1)