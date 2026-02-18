import socket, threading, json
from crypto_utils import encrypt_message, decrypt_message

def receive_messages(sock):
    while True:
        try:
            raw_len = sock.recv(4)
            if not raw_len:
                break
            msg_len = int.from_bytes(raw_len, 'big')
            data = b''
            while len(data) < msg_len:
                packet = sock.recv(msg_len - len(data))
                if not packet:
                    break
                data += packet
            msg = json.loads(data.decode())
            iv = msg['iv']
            cipher = msg['ciphertext']
            plain = decrypt_message(iv, cipher)
            print(f"\n[Other]: {plain}")
        except:
            break

def start_client(host='127.0.0.1', port=9999):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    threading.Thread(target=receive_messages, args=(sock,), daemon=True).start()
    print("[*] Connected to chat. Type your messages (type 'quit' to exit).")
    while True:
        msg = input()
        if msg.lower() == 'quit':
            break
        iv, cipher = encrypt_message(msg)
        data = json.dumps({"iv": iv, "ciphertext": cipher}).encode()
        length = len(data).to_bytes(4, 'big')
        sock.send(length + data)
    sock.close()


if __name__ == '__main__':
    start_client()