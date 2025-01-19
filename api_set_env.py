# -*- coding: utf-8 -*-
import socket
import os

try:
    from dotenv import load_dotenv, set_key
except:
    try:
        os.system("pip install python-dotenv")
    except:
        os.system("python.exe -m pip install --upgrade pip")
        os.system("pip install python-dotenv")
    from dotenv import load_dotenv, set_key

print("========================[get port]===============================")
def find_available_port():
    """find a port."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("localhost", 0)) 
        return s.getsockname()[1]

def create_env_file(port):
    """create env file"""
    file_env = ".env"
    load_dotenv(file_env)
    set_key(file_env, "API_PORT", str(port))

try:
    available_port = find_available_port()
    create_env_file(available_port)
    print(available_port)
except Exception as e:
    print(f"ERROR={e}")
print("========================================================================")