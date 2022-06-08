import socket
from _thread import *
import json
from prometheus_client import start_http_server, Gauge


SERVER_HOST = '127.0.0.1'
SERVER_PORT = 1234
PROMETHEUS_PORT = 8000

def init_prometheus():
    cpu_freq_gauge = Gauge('cpu_freq', "CPU's Current Freq", ['agent'])
    memory_available_gauge = Gauge('memory_available', "Memory's Current Available Volume", ['agent'])
    disk_usage_percent_gauge = Gauge('disk_usage_percent', "Disk's Current Usage Percent", ['agent'])
    battery_percent_gauge = Gauge('battery_percent', "Battery's Remaining Percentage", ['agent'])
    return cpu_freq_gauge, memory_available_gauge, disk_usage_percent_gauge, battery_percent_gauge

def send_data_to_prometheus(data, agent_id):
    agent_string = f'agent({agent_id})'
    cpu_freq_gauge.labels(agent_string).set(data['cpu_freq'])
    memory_available_gauge.labels(agent_string).set(data['memory_available'])
    disk_usage_percent_gauge.labels(agent=agent_string).set(data['disk_usage_percent'])
    battery_percent_gauge.labels(agent=agent_string).set(data['battery_percent'])

def client_handler_thread(conn, agent_id, print_agent_data=False):
    with conn:
        while True:
            try:
                data = conn.recv(1024)
                if not data:
                    break

                send_data_to_prometheus(json.loads(data.decode('utf-8')), agent_id)

            except:
                break
            
            conn.sendall('OK'.encode('utf-8'))

            if print_agent_data:
                print('Agent {}: {}'.format(agent_id, data.decode('utf-8')))
    print('Agent ' + str(agent_id) + ' disconnected')


cpu_freq_gauge, memory_available_gauge, disk_usage_percent_gauge, battery_percent_gauge = init_prometheus()

start_http_server(PROMETHEUS_PORT)

agents_count = 0
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((SERVER_HOST, SERVER_PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        agents_count += 1
        start_new_thread(client_handler_thread, (conn, agents_count))
        print(f'New agent({agents_count}) connected by {addr}')