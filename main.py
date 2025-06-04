# main.py
from scan_network import scan

if __name__ == "__main__":
    subnet = "192.168.223.0/24"
    print("[*] Scanning network...")
    devices = scan(subnet)

    print("[*] Devices found:")
    for dev in devices:
        print(dev)
