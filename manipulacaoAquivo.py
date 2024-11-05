import json
import pickle



def salvar_dados_json(self, filename="pedidos.json"):
        with open(filename, 'w') as file:
            json.dump([pedido.to_dict() for pedido in self.pedidos], file, indent=4)
        print(f"Dados salvos em {filename}.")

def carregar_dados_json(self, filename="pedidos.json"):

        try:
            with open(filename, 'r') as file:
                pedidos_data = json.load(file)
                self.pedidos = [Pedido.from_dict(data) for data in pedidos_data]
            print(f"Dados carregados de {filename}.")
        except FileNotFoundError:
            print(f"O arquivo {filename} não foi encontrado.")

def salvar_dados_binario(self, filename="pedidos.bin"):

        with open(filename, 'wb') as file:
            pickle.dump(self.pedidos, file)
        print(f"Dados salvos em {filename}.")

def carregar_dados_binario(self, filename="pedidos.bin"):

        try:
            with open(filename, 'rb') as file:
                self.pedidos = pickle.load(file)
            print(f"Dados carregados de {filename}.")
        except FileNotFoundError:
            print(f"O arquivo {filename} não foi encontrado.")