import scapy.all as scapy
import netifaces as ni

def get_current_network_interface():
    interfaces = ni.interfaces()
    for interface in interfaces:
        if interface != "lo":
            addrs = ni.ifaddresses(interface)
            if ni.AF_INET in addrs:
                return interface

def scan_network(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    devices_list = []
    for element in answered_list:
        device = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        devices_list.append(device)
    return devices_list

def print_result(results_list):
    print("IP Address\t\tMAC Address")
    print("-----------------------------------------")
    for device in results_list:
        print(device["ip"] + "\t\t" + device["mac"])

if __name__ == "__main__":
    current_interface = get_current_network_interface()
    if current_interface:
        ip = ni.ifaddresses(current_interface)[ni.AF_INET][0]['addr']
        subnet = ip + "/24"  # Assuming it's a /24 subnet
        print(f"Scanning network {subnet} on interface {current_interface}...")
        scanned_devices = scan_network(subnet)
        print_result(scanned_devices)
    else:
        print("Failed to detect network interface. Please check your network connection.")
