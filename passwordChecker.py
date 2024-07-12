import argparse
import subprocess
import os

def main():
    parser = argparse.ArgumentParser(description="Verifica si la contraseña se encuentra en una lista.")
    parser.add_argument("--passwd", type=str, required=True, help="Contraseña a verificar")
    parser.add_argument("--file", type=str, required=True, help="Lista de contraseñas")
    args = parser.parse_args()

    _, extension = os.path.splitext(args.file)

    comando_gzip = f"zcat {args.file} | grep -wo {args.passwd}"
    comando_zip = f"unzip -p {args.file} | grep -wo {args.passwd}"


    if extension == '.zip':
        result = subprocess.run(comando_zip, shell=True, capture_output=True, text=True)
        unic_words = set(result.stdout.strip().splitlines())
        if unic_words:
            print(unic_words)
            
    elif extension == '.gz':
        result = subprocess.run(comando_gzip, shell=True, capture_output=True, text=True)
        unic_words = set(result.stdout.strip().splitlines())
        if unic_words:
            print(unic_words)


main()