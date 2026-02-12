import sys
from fontes.paquete_exemplo_JorgeDC.MatOperacion import suma

def main():
    args = sys.argv[1:]
    res = suma(args[0],args[1])
    print(f"A suma é {res}")

if __name__ == "__main__":
    main()