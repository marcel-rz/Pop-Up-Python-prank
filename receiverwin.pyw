import socket
import os
import subprocess
import sys

usb_path = os.path.dirname(os.path.abspath(__file__))

try:
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    sender_code = f"""import socket

TARGET_IP = "{local_ip}"
PORT = 5005
MESSAGE = "CRITICAL ERROR: YOUR FILES ARE BEING DELETED"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TARGET_IP, PORT))
s.send(MESSAGE.encode())
s.close()
"""
    with open(os.path.join(usb_path, "sender.py"), "w", encoding="utf-8") as f:
        f.write(sender_code)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("0.0.0.0", 5005))
    server.listen(5)

    while True:
        conn, addr = server.accept()
        msg = conn.recv(1024).decode()
        conn.close()
        subprocess.Popen([sys.executable, '-c',
            f'import tkinter as t;import tkinter.messagebox as mb;r=t.Tk();r.withdraw();mb.showerror("System Error","{msg}");r.destroy()'
        ])

except Exception as e:
    desktop = os.path.join(os.path.expanduser("~"), "Desktop", "error.log")
    with open(desktop, "w") as f:
        f.write(str(e))
