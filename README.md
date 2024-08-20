# Cibersecurity-Tools
Herrameintas de seguridad informática

## Network_scanner.sh
Ejecución:
```bash
sudo ./network_scanners.sh
```
En caso de que no tenga permisos de ejecución:
```bash
chmod +x network_scanners.sh
```

<p align=center>
    <img src="./images/image_network_scanners.sh.png"/>
</p>


## windows_networkScanner.py
Ejecución:
```bash
python windows_networkScanner.py
```
> Te perdirá permisos de administrador


## linux_networkScanner.py
Ejecución:
```bash
sudo python3 linux_networkScanner.py
```

<p align=center>Output de linux y windows networkScanners.py</p>
<p align=center>
    <img src="./images/output_networkScanners.py.png"/>
</p>

## passwordChecker.py
Ejecución:
```bash
usage: passwordChecker.py [-h] --passwd PASSWD --file FILE

Verifica si la contraseña se encuentra en una lista.

options:
  -h, --help       show this help message and exit
  --passwd PASSWD  Contraseña a verificar
  --file FILE      Lista de contraseñas
```