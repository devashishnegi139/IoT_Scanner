# vuln_scan_lite.py
import nmap

def run_vuln_scan(devices):
    scanner = nmap.PortScanner()
    for device in devices:
        ip = device['ip']
        try:
            print(f"[*] Scanning {ip}...")
            scanner.scan(ip, arguments='-T4 -F')
            device['namp'] = scanner[ip]
        except Exception as e:
            device['nmap'] = {'error': str(e)}

    return devices