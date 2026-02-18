import socket, threading, json, datetime
from crypto_utils import decrypt_message

clients = []
LOG_FILE = "chat.log"

def handle_client(conn, addr):
    print(f"[+] New connection from {addr}")
    clients.append(conn)
    with open(LOG_FILE, 'a') as f:
        f.write(f"{datetime.datetime.now()} - {addr} connected\n")
    while True:
        try:
            # Read message length (4 bytes)
            raw_len = conn.recv(4)
            if not raw_len:
                break
            msg_len = int.from_bytes(raw_len, 'big')
            data = b''
            while len(data) < msg_len:
                packet = conn.recv(msg_len - len(data))
                if not packet:
                    break
                data += packet
            # Parse and decrypt
            msg = json.loads(data.decode())
            iv = msg['iv']
            cipher = msg['ciphertext']
            plain = decrypt_message(iv, cipher)
            # Log
            with open(LOG_FILE, 'a') as f:
                f.write(f"{datetime.datetime.now()} - {addr}: {plain}\n")
            print(f"{addr}: {plain}")
            # Broadcast to other clients (optional)
            for c in clients:
                if c != conn:
                    try:
                        c.send(raw_len + data)   # forward encrypted message
                    except:
                        pass
        except Exception as e:
            print(f"Error with {addr}: {e}")
            break
    conn.close()
    clients.remove(conn)
    print(f"[-] {addr} disconnected")

def start_server(host='0.0.0.0', port=9999):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[*] Server listening on {host}:{port}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


if __name__ == '__main__':
    start_server()