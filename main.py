# main.py
from scan_network import scan
from identify_iot import enrich_with_vendors

if __name__ == "__main__":
    subnet = "192.168.223.0/24"
    print("[*] Scanning network...")
    devices = scan(subnet)

    print("[*] Devices found:")
    for dev in devices:
        print(dev)

    print(f"[*] Found {len(devices)} devices. Identifying vendors...")
    devices = enrich_with_vendors(devices)