import socket
import struct
import ipaddress
import argparse
from tabulate import tabulate
import sys

def mask(prefix) -> str:
    return socket.inet_ntoa(struct.pack(">I", (0xffffffff << (32 - prefix)) & 0xffffffff))

def header(ip: str) -> list[str]:
    return [f"IP: {ip}", "Value"]

def obteinIpClass(ip: str) -> str:
    first_octet = int(ip.split(".")[0])

    if 1 <= first_octet <= 127: return "A"
    elif 128 <= first_octet <= 191: return "B"
    elif 192 <= first_octet <= 223: return "C"
    else: return "Unknown"

def obteinMask(classIP: str) -> str:
    mask_map = {
        "A": mask(8),
        "B": mask(16),
        "C": mask(24)
    }
    return mask_map.get(classIP, "Unknown")

def obteinTypeIp(ip: str) -> str:
    network = ipaddress.IPv4Network(ip, strict=False)
    if network.is_loopback: return "Loopback"
    elif network.is_private: return "Privada"
    elif network.is_multicast: return "Multicast"
    elif network.is_reserved: return "Reservada"
    elif network.is_global and not network.is_private: return "Public"
    else: return "Unknown"

def get_broadcast_address(ip: str) -> str:
    network = ipaddress.IPv4Network(ip, strict=False)
    return str(network.broadcast_address)

def get_host_range(ip: str) -> tuple:
    network = ipaddress.IPv4Network(ip, strict=False)
    first_host = network.network_address + 1
    last_host = network.broadcast_address - 1
    return (str(first_host), str(last_host))

def get_total_hosts(ip: str) -> int:
    network = ipaddress.IPv4Network(ip, strict=False)
    return network.num_addresses - 2

def process_ip(ip: str) -> list:
    if '/' not in ip:
        class_ip = obteinIpClass(ip)
        if class_ip == "A":
            ip += "/8"
        elif class_ip == "B":
            ip += "/16"
        elif class_ip == "C":
            ip += "/24"
        else:
            print(f"Clase de IP desconocida o no válida: {ip}")
            return None
        
    try:
        network = ipaddress.IPv4Network(ip, strict=False)
        mymask = network.netmask
    except ValueError:
        print(f"Direccion IP no valida: {ip}")
        return None

    type_ip = obteinTypeIp(ip)
    class_ip = obteinIpClass(str(network.network_address))
    broadcast_ip = get_broadcast_address(ip)
    host_range = get_host_range(ip)
    total_hosts = get_total_hosts(ip)
    
    return [
        ["IP Network", str(network.network_address)],
        ["Version", f"IPV{network.version}"],
        ["Mask", str(mymask)],
        ["Type", type_ip],
        ["Class", class_ip],
        ["Broadcast", broadcast_ip],
        ["Host Range", f"De: {host_range[0]}\nHasta: {host_range[1]}"],
        ["Total Hosts", str(total_hosts)]
    ]

def main():
    parser = argparse.ArgumentParser(description="IPv4 information, just A, B and C")
    parser.add_argument("--ips", "-i", dest="ips", required=True, nargs='+', help="IP addresses")

    if len(sys.argv) <= 1:
        parser.print_help()
        exit(0)
    
    args = parser.parse_args()
    
    for ip in args.ips:
        result = process_ip(ip)
        if result:
            print(tabulate(result, header(ip), tablefmt="fancy_grid", stralign="center"))

main()
