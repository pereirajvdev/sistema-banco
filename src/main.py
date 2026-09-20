import sys
import json
from pathlib import Path


ARQUIVO_CONTA = Path(__file__).parent.parent / "data" / "conta.json"


def carregar_saldo():
    with open(ARQUIVO_CONTA, "r") as arquivo:
        conta = json.load(arquivo)

    return conta["saldo"]


def salvar_saldo(saldo):
    with open(ARQUIVO_CONTA, "w") as arquivo:
        json.dump({"saldo": saldo}, arquivo, indent=4)


def depositar(valor):
    saldo = carregar_saldo()
    saldo += valor
    salvar_saldo(saldo)

    print(f"Depósito de R$ {valor:.2f} realizado.")


def sacar(valor):
    saldo = carregar_saldo()

    if valor > saldo:
        print("Saldo insuficiente.")
        return

    saldo -= valor
    salvar_saldo(saldo)

    print(f"Saque de R$ {valor:.2f} realizado.")


def consultar_saldo():
    saldo = carregar_saldo()
    print(f"Saldo: R$ {saldo:.2f}")


if len(sys.argv) < 2:
    print("Comando não informado.")
    sys.exit()


comando = sys.argv[1]


if comando == "saldo":
    consultar_saldo()

elif comando == "depositar":
    valor = float(sys.argv[2])
    depositar(valor)

elif comando == "sacar":
    valor = float(sys.argv[2])
    sacar(valor)

else:
    print("Comando inválido.")