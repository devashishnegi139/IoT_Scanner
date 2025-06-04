# scan_network.py
from scapy.all import ARP, Ether, srp

def scan(subnet):
    # Creating an Ethernet Frame with destination MAC address set to broadcast
    # Broadcast so that all devices in the subnet will receive this packet
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")

    # creating an ARP request packet
    # pdst is the target IP address or subnet to scan
    arp = ARP(pdst=subnet)

    # Enveloping the ARP request in the Ethernet frame
    # This creates a complete packet that can be sent on the network
    # / means we are combining the Ether and ARP layers
    packet = ether/arp

    # srp = send and recieve packets at layer 2 (Ethernet)
    # The timeout is set to 2 seconds, which means it will wait for a response for that duration
    # verbose=False suppresses the output of the packet sending process
    # [0] means only the packets that were answered will be returned
    # [1] would return the unanswered packets
    # so this all mean send the packet and wait for responses for 2 seconds and return the answered packets
    ans = srp(packet, timeout=2, verbose=False)[0]

    # creating a list to store the devices found
    devices = []

    # in the ans, we ignore the sent packets and only focus on the received packets
    for sent, received in ans:
        devices.append({'ip': received.psrc,'mac': received.hwsrc})
        # psrc = protocol source IP address
        # hwsrc = hardware source MAC address

    return devices
