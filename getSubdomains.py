import sublist3r
import argparse
import sys


def enurateSubdomains(pagina, output:str=None, bruteForce:bool=False):
    return sublist3r.main(pagina, 50, savefile=output, ports=None, silent=False, verbose=True, enable_bruteforce=bruteForce, engines=None)


def main():
    parser = argparse.ArgumentParser(description="Enumerar subdominios de una página")
    parser.add_argument("-p", dest="pagina", required=True, type=str, help="Pagina")
    parser.add_argument("-o", dest="output", type=str, help="Guardar output en un archivo")
    parser.add_argument("-b", dest="bruteforce", action="store_true", help="Fuerza bruta para que pueda devolver más subdominios")
    
    if len(sys.argv) <= 1:
        parser.print_help()
        exit(0)

    args = parser.parse_args()

    enurateSubdomains(args.pagina, output=args.output, bruteForce=args.bruteforce)


main()