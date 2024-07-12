import argparse
import subprocess

def main():
    parser = argparse.ArgumentParser(description="Verifica si la contraseña se encuentra en una lista.")
    parser.add_argument("--passwd", type=str, required=True, help="Contraseña a verificar")
    parser.add_argument("--file", type=str, required=True, help="Lista de contraseñas")
    args = parser.parse_args()

    comando = f"zcat {args.file} | grep -wo {args.passwd}"


    result = subprocess.run(comando, shell=True, capture_output=True, text=True)

    unic_words = set(result.stdout.strip().splitlines())

    if unic_words:
        print(unic_words)


main()