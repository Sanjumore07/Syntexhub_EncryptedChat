# 🔒 SecureChat: AES-GCM Encrypted Messaging System

## 📄 Project Overview
**SecureChat** is a Python-based encrypted chat application designed to demonstrate **Crypto-Agility** and **Network Security** concepts. Unlike standard chat apps, this project focuses on the visualization of encryption in transit.

It features a unique **"Hacker View" (Traffic Sniffer Mode)** on the server side, which displays the raw, garbled ciphertext in real-time. This serves as a visual proof-of-concept that data is mathematically impossible to interpret without the correct keys, even if intercepted by a Man-in-the-Middle (MITM).

## ✨ Key Features (Unique Selling Points)
* **AES-256-GCM Encryption:** Uses the industry-standard *Galois/Counter Mode* for both confidentiality and message integrity.
* **Safe IV Usage:** Generates a unique 12-byte **Nonce (IV)** for *every single message* to prevent Replay Attacks.
* **Real-Time Traffic Sniffing:** The server console acts as a network monitor, printing the raw HEX of encrypted packets to demonstrate security.
* **Multi-Client Architecture:** Supports multiple users chatting simultaneously using Python `threading`.
* **Tamper Detection:** If a message is altered in transit, the GCM mode authentication tag will fail, and the system will reject the packet.

## 🛠️ Technologies Used
* **Language:** Python 3.x
* **Cryptography:** `cryptography` library (hazmat primitives)
* **Networking:** `socket` (TCP/IP)
* **Concurrency:** `threading`

## 📂 Project Structure
* `crypto_utils.py`: The core security engine. Handles AES-GCM encryption/decryption and key management.
* `server.py`: The central hub. Routes messages and displays the "Encrypted Traffic" logs (Hacker View).
* `client.py`: The user interface. Handles sending/receiving messages and local decryption.

## 🚀 Installation & Setup

### 1. Prerequisites
Ensure you have Python installed. You will need the `cryptography` library.
```bash
pip install cryptography

2. How to Run the Project
To demonstrate the project effectively, use a split-terminal view (like in VS Code).

Step 1: Start the Server (The "Spy" Console)

Type Command
python server.py
The server will start listening.

Step 2: Start Client 1 (User A) Open a new terminal and run:

Type Command
python client.py
Enter a nickname (e.g.,Tanushri).

Step 3: Start Client 2 (User B) Open another terminal and run:

Type Command
python client.py
Enter a nickname (e.g., Dhanshri).

3. Usage
Type a message in any Client terminal and press Enter.

Observe the Server Terminal: You will see the raw encrypted bytes (e.g., a1b2...) passing through.

Observe the Other Client: You will see the decrypted, readable message.

🔮 Future Scope
Diffie-Hellman Key Exchange: Implementing a dynamic key exchange handshake instead of a pre-shared key.

GUI: Creating a frontend using Tkinter or PyQt.

Database Integration: Storing encrypted chat logs for later retrieval.

👤 Author
Sanjivani More B.Tech Computer Science (Cyber Security) Sanjivani University
