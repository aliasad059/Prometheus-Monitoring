import socket
from _thread import *


HOST = '127.0.0.1'
PORT = 12345

def client_handler_thread(conn, agent_id, print_agent_data=False):
    with conn:
        while True:
            try:
                data = conn.recv(1024)
                if not data:
                    break
            except:
                break
            
            conn.sendall('OK'.encode('utf-8'))

            if print_agent_data:
                print('Agent {}: {}'.format(agent_id, data.decode('utf-8')))
                
    print('Agent ' + str(agent_id) + ' disconnected')
        
if __name__ == '__main__':

    agents_count = 0
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            start_new_thread(client_handler_thread, (conn, agents_count))
            agents_count += 1
            print(f'New agent({agents_count}) connected by {addr}')