# identify_iot.py
import requests

def enrich_with_vendors(devices):
    for device in devices:
        mac = device['mac']
        try:
            vendor = requests.get(f"https://api.macvendors.com/{mac}").text
        except:
            vendor = "Unknown"

        device['vendor'] = vendor
    return devices