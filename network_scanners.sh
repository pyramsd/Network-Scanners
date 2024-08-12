#!/bin/bash

if [ $EUID -ne 0 ]; then
	echo "Pemission denied"
	exit 1
fi

echo -e "\033[33m
 ▄▄▄   ▄▄                                                   ▄▄                 
 ███   ██              ██                                   ██                 
 ██▀█  ██   ▄████▄   ███████  ██      ██  ▄████▄   ██▄████  ██ ▄██▀            
 ██ ██ ██  ██▄▄▄▄██    ██     ▀█  ██  █▀ ██▀  ▀██  ██▀      ██▄██              
 ██  █▄██  ██▀▀▀▀▀▀    ██      ██▄██▄██  ██    ██  ██       ██▀██▄             
 ██   ███  ▀██▄▄▄▄█    ██▄▄▄   ▀██  ██▀  ▀██▄▄██▀  ██       ██  ▀█▄            
 ▀▀   ▀▀▀    ▀▀▀▀▀      ▀▀▀▀    ▀▀  ▀▀     ▀▀▀▀    ▀▀       ▀▀   ▀▀▀           
                                                                                
                                                                                
                                                                                
                                                    
 ▄▄█████▄   ▄█████▄   ▄█████▄  ██▄████▄  ██▄████▄   ▄████▄   ██▄████  ▄▄█████▄ 
 ██▄▄▄▄ ▀  ██▀    ▀   ▀ ▄▄▄██  ██▀   ██  ██▀   ██  ██▄▄▄▄██  ██▀      ██▄▄▄▄ ▀ 
  ▀▀▀▀██▄  ██        ▄██▀▀▀██  ██    ██  ██    ██  ██▀▀▀▀▀▀  ██        ▀▀▀▀██▄ 
 █▄▄▄▄▄██  ▀██▄▄▄▄█  ██▄▄▄███  ██    ██  ██    ██  ▀██▄▄▄▄█  ██       █▄▄▄▄▄██ 
  ▀▀▀▀▀▀     ▀▀▀▀▀    ▀▀▀▀ ▀▀  ▀▀    ▀▀  ▀▀    ▀▀    ▀▀▀▀▀   ▀▀        ▀▀▀▀▀▀ \033[0m"

echo "Choice the scanner:"
echo "-------------------"
echo -e "\033[35m1.\033[0m arp-scan (Specify NIC)"
echo -e "\033[35m2.\033[0m nmap"
echo -e "\033[35m3.\033[0m hping3"
echo -e "\033[35m4.\033[0m netdiscover (Specify NIC)"

read -p $'\e[31m>>> \e[0m' ch

if [ $ch -eq 1 ] || [ $ch -eq 2 ] || [ $ch -eq 3 ] || [ $ch -eq 4 ]; then

	# scanner 1
	if [ $ch -eq 1 ]; then
		read -p "NIC: " nic
		arp-scan -I $nic --localnet

	# scanner 2
	elif [ $ch -eq 2 ]; then
		ipred=$(route -n | grep "Destination" -A 2 | tail -n 1 | awk '{print $1}')
		nmap -sP $ipred/24
	
	# scanner 3
	elif [ $ch -eq 3 ]; then
		echo "IPs en red:"
		ipred=$(hostname -I | awk -F'.' '{print $1"."$2"."$3}')
		for host in {1..254}; do
			ip=${ipred}.${host}
			if hping3 -c 1 -p 80 -s 5050 -A "$ip" > /dev/null 2>&1; then
				echo $ip
			fi
		done
	
	# scanner 4
	elif [ $ch -eq 4 ]; then
		read -p "NIC: " nic
		ipred=$(route -n | grep "Destination" -A 2 | tail -n 1 | awk '{print $1}')
		netdiscover -i $nic -r $ipred

	fi

else
	echo "Wrong choice"
fi
