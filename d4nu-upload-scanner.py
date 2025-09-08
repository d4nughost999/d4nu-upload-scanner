#!/usr/bin/env python3
import requests
import sys
import re
from colorama import Fore, Style

def banner():
    print(Fore.CYAN + r"""
    ╔══════════════════════════════════╗
      d4nu-upload-scanner v1.0
      Simple File Upload Form Scanner
    ╚══════════════════════════════════╝
    """ + Style.RESET_ALL)

def scan(url):
    try:
        print(Fore.YELLOW + f"[+] Scanning target: {url}" + Style.RESET_ALL)
        r = requests.get(url, timeout=10)
        html = r.text.lower()

        # Cari input type file
        if re.search(r'<input[^>]+type=["\']?file', html):
            print(Fore.RED + "[!] Upload form ditemukan ⚠️" + Style.RESET_ALL)
            print(Fore.GREEN + "[*] Potensi file upload vulnerability 🚨" + Style.RESET_ALL)
        else:
            print(Fore.BLUE + "[-] Tidak ada form upload ditemukan." + Style.RESET_ALL)

    except Exception as e:
        print(Fore.RED + f"[x] Error: {e}" + Style.RESET_ALL)

def usage():
    print("Usage: python3 d4nu-upload-scanner.py <url>")
    print("Example: python3 d4nu-upload-scanner.py http://target.com/page")

if name == "main":
    banner()
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    target = sys.argv[1]
    scan(target)
