#!/usr/bin/env python3
"""
Krypton Launcher — Desktop GUI Runner (Windows & Linux)
Opens the Krypton Launcher UI in a native window (via pywebview if installed, or default browser)
and serves a local API bridge to core/krypton_core.py.
"""
import http.server
import socketserver
import threading
import webbrowser
from pathlib import Path
from core import krypton_core

PORT = 28490
UI_DIR = Path(__file__).parent / "ui"

class KryptonHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(UI_DIR), **kwargs)

def start_server():
    krypton_core.ensure_pojav_directory_tree(krypton_core.get_pojav_minecraft_root())
    with socketserver.TCPServer(("127.0.0.1", PORT), KryptonHandler) as httpd:
        print(f"[Krypton Launcher] Local GUI Bridge running at http://127.0.0.1:{PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    t = threading.Thread(target=start_server, daemon=True)
    t.start()
    url = f"http://127.0.0.1:{PORT}/index.html"
    try:
        import webview
        webview.create_window("Krypton Launcher", url, width=1280, height=780, background_color="#070312")
        webview.start()
    except ImportError:
        webbrowser.open(url)
        input("[Krypton Launcher] Opened in browser. Press Enter to stop the launcher service...\n")
