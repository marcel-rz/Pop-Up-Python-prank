import socket
import os

usb_path = os.path.dirname(os.path.abspath(__file__))

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

with open(os.path.join(usb_path, "sender.py"), "w") as f:
    f.write(f"""import socket

TARGET_IP = "{local_ip}"
PORT = 5005
MESSAGE = "💀 CRITICAL ERROR: YOUR FILES ARE BEING DELETED"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TARGET_IP, PORT))
s.send(MESSAGE.encode())
s.close()
""")

print(f"IP saved: {local_ip}")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 5005))
s.listen(1)
print("Waiting for messages...")

while True:
    conn, addr = s.accept()
    msg = conn.recv(1024).decode()
    conn.close()
    os.system(f'osascript -e \'display dialog "{msg}" with title "System Error" buttons {{"OK"}} default button "OK"\'')
