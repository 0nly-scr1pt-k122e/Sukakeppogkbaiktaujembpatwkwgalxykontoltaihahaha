import subprocess
import re
import os
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, HTTPServer


SSH_KEY_PATH = os.path.expanduser("~/.ssh/id_ed25519")


class HalloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        html = """
        <html>
            <head>
                <title>hallo rulzz</title>
                <style>
                    body {
                        background: #0f0f0f;
                        color: #00ff88;
                        font-family: monospace;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                        font-size: 3em;
                        text-align: center;
                    }
                </style>
            </head>
            <body>
                hallo rulzz
            </body>
        </html>
        """
        self.wfile.write(html.encode("utf-8"))

    def log_message(self, format, *args):
        pass


def start_local_server(port):
    server = HTTPServer(("0.0.0.0", port), HalloHandler)
    server.serve_forever()


def ensure_ssh_key():
    if os.path.exists(SSH_KEY_PATH):
        return

    print("[!] SSH key belum ada, generate dulu...")
    subprocess.run(
        ["ssh-keygen", "-t", "ed25519", "-f", SSH_KEY_PATH, "-N", ""],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    if not os.path.exists(SSH_KEY_PATH):
        print("[x] Gagal generate SSH key. Coba jalanin manual: ssh-keygen -t ed25519")
        sys.exit(1)

    print("[+] SSH key berhasil dibuat.")


def start_tunnel(local_port, subdomain=None, retries=3):
    ensure_ssh_key()

    remote_target = f"{subdomain}:80:localhost:{local_port}" if subdomain else f"80:localhost:{local_port}"

    for attempt in range(1, retries + 1):
        print(f"\n[+] Mencoba konek ke ssh.localhost.run (percobaan {attempt}/{retries})...")

        process = subprocess.Popen(
            [
                "ssh",
                "-o", "StrictHostKeyChecking=accept-new",
                "-R", remote_target,
                "ssh.localhost.run"
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )

        url_found = False
        buffer = ""

        try:
            while True:
                char = process.stdout.read(1)
                if char == "" and process.poll() is not None:
                    break

                if char in ("\n", "\r"):
                    line = buffer.strip()
                    buffer = ""

                    if not line or url_found:
                        continue

                    match = re.search(r"https://[a-zA-Z0-9\-]+\.lhr\.life", line)
                    if match:
                        url_found = True
                        print(f"\n{'=' * 55}")
                        print(f"  LINK: {match.group(0)}")
                        print(f"  Buka link itu -> bakal muncul 'hallo rulzz'")
                        print(f"{'=' * 55}\n")
                        print("[i] Tunnel jalan. Tekan CTRL+C buat stop.\n")
                else:
                    buffer += char

            process.wait()

        except KeyboardInterrupt:
            print("\n[!] Tunnel dihentikan manual.")
            process.terminate()
            return

        if url_found:
            print("[!] Koneksi terputus, tunnel mati.")
            return

        print(f"[x] Gagal connect (percobaan {attempt}).")
        if attempt < retries:
            time.sleep(3)

    print("[x] Semua percobaan gagal. Cek koneksi internet lo.")


if __name__ == "__main__":
    port = 5000

    server_thread = threading.Thread(target=start_local_server, args=(port,), daemon=True)
    server_thread.start()
    print(f"[+] Server lokal 'hallo rulzz' jalan di port {port}")

    time.sleep(1)

    start_tunnel(local_port=port)
