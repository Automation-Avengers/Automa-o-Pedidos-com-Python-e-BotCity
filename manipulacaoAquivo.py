import json
import pickle
from pedido import Pedido 

def salvar_dados_json(pedidos, arquivo="pedidos.json"):
    with open(arquivo, 'w') as file:
        json.dump([pedido.to_dict() for pedido in pedidos], file, indent=4)
    print(f"Dados salvos em {arquivo}.")

def carregar_dados_json(arquivo="pedidos.json"):
    try:
        with open(arquivo, 'r') as file:
            pedidos_data = json.load(file)
            return [Pedido.from_dict(data) for data in pedidos_data]
    except FileNotFoundError:
        print(f"O arquivo {arquivo} não foi encontrado.")
        return []

def salvar_dados_binario(pedidos, arquivo="pedidos.bin"):
    with open(arquivo, 'wb') as file:
        pickle.dump(pedidos, file)
    print(f"Dados salvos em {arquivo}.")

def carregar_dados_binario(arquivo="pedidos.bin"):
    try:
        with open(arquivo, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        print(f"O arquivo {arquivo} não foi encontrado.")
        return []
