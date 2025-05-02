import platform
import importlib
import sys

arch = platform.machine()

try:
    if "aarch64" in arch or "x86_64" in arch:
        print("[+] 64-bit system detected.")
        ap = importlib.import_module("ap_64bit")
    elif "arm" in arch or "i686" in arch:
        print("[+] 32-bit system detected.")
        ap = importlib.import_module("ap_32bit")
    else:
        print("[-] Unsupported architecture:", arch)
        sys.exit(1)

    ap.main()  # assume main() exists in both versions

except Exception as e:
    print("[-] Error loading module:", e)
