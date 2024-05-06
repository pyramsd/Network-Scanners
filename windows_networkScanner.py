import socket
import os
import threading
import scapy.all as scapy

def search(ip_address):
    command = "ping -n 1 " + ip_address
    response = os.popen(command).read()
    if "TTL=" in response:
        return ip_address
    
def get_Mac(ip_adderss):
    mac = scapy.getmacbyip(ip_adderss)
    return mac

def ping_and_print(ip):
    ip_address = search(ip)
    if ip_address:
        try:
            mac = scapy.getmacbyip(ip)
            nombre = socket.gethostbyaddr(ip_address)[0]
            print("{:25} {:<15} {:<16}".format(nombre, ip, mac))
        except Exception as e:
            print(f"Error obteniendo el nombre para {ip_address}: {e}")

def main():
    print("-----------------------------------------------------------")
    print("{:25} {:<15} {:<16}".format("Hostname", "IP", "MAC"))
    print("-----------------------------------------------------------")
    threads = []
    for i in range(1, 255):
        current_ip = "192.168.1." + str(i)
        thread = threading.Thread(target=ping_and_print, args=(current_ip,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()

