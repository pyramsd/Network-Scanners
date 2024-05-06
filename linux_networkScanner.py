import scapy.all as scapy
from scapy.layers.l2 import ARP, Ether
import socket


# nombre maquina
def getHostname(ip):
    try:
        hostname = socket.gethostbyaddr(ip)[0]
        return hostname
    except socket.herror:
        return "No se pudo obtener nombre"


# gateway
def getGateway():
    gw = scapy.conf.route.route("0.0.0.0")[2]

    return gw + "/24"


# escaneo
def scan(gateway):

    gateway = getGateway()
    
    arp_request = ARP(pdst=gateway)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list= scapy.srp(arp_request_broadcast, timeout=1, verbose=0)[0]
                                                                  
    clients_list = []
    for element in answered_list:
        client_dict = {"IP":  element[1].psrc, "MAC ADDRESS": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list


print("----------------------------------------------------------------")
print("{:<25} {:<15} {:<15}".format("Hostname","IP", "Mac address"))
print("----------------------------------------------------------------")

# imprimir resultados
def print_result(results_list):
    for client in results_list:
        print("{:<25} {:<15} {:<15}".format(getHostname(client["IP"]), 
                                                  client["IP"], client["MAC ADDRESS"]))


print_result(scan(getGateway()))
