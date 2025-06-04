# identify_iot.py
# importing requests to fetch vendor information
import requests

def enrich_with_vendors(devices):
    """
    Enriches a list of devices with vendor information based on their MAC addresses.
    Args:
        devices (List[dict]): List of devices with 'mac' keys.
    """
    for device in devices:
        # create a mac va
        mac = device['mac']
        try:
            # Fetch vendor information from the macvendors API
            # Note: This API may have rate limits or require an API key for extensive use.
            vendor = requests.get(f"https://api.macvendors.com/{mac}").text
        except:
            # If the request fails, we can set vendor to "Unknown"
            vendor = "Unknown"
        # Add the vendor information to the device dictionary
        device['vendor'] = vendor
    return devices