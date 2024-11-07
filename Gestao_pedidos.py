from functools import reduce
from typing import List, Dict
from datetime import datetime

class ValorInvalidoError(Exception):
    pass

class QuantidadeInvalidaError(Exception):
    pass

def log_atividade(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] {datetime.now()} - Executou: {func} | Args: {args[1:]} | Retorno: {result}")
        return result
    return wrapper

class Produto:
    def __init__(self, nome: str, preco: float, categoria: str):
        if preco < 0:
            raise ValorInvalidoError("O preço deve ser positivo.")
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
    def detalhes(self):
        return f"Produto: {self.nome}, Preço: R${self.preco}, Categoria: {self.categoria}"

class Pedido:
    def __init__(self, produtos: List[Produto], quantidade: Dict[Produto, int], cliente: str, status: str = "Novo"):
        self.produtos = produtos
        self.quantidade = quantidade
        self.cliente = cliente
        self.status = status
    def total_pedido(self):
        total = reduce(lambda acc, produto: acc + produto.preco * self.quantidade[produto], self.produtos, 0)
        return total

    def detalhes_pedido(self):
        return {
            "cliente": self.cliente,
            "produtos": [{ "nome": p.nome, "quantidade": self.quantidade[p] } for p in self.produtos],
            "status": self.status,
            "total": self.total_pedido()
        }


class GestorDePedidos:
    def __init__(self):
        self.pedidos = [] 

    @log_atividade
    def adicionar_pedido(self, pedido: Pedido):
        self.pedidos.append(pedido)

    @log_atividade
    def listar_pedidos_por_status(self, status: str):
        return list(filter(lambda p: p.status == status, self.pedidos))

    def pedidos_por_categoria(self, categoria: str):
        produtos_categoria = filter(lambda p: any(produto.categoria == categoria for produto in p.produtos), self.pedidos)
        return list(map(lambda p: (p.cliente, [prod.nome for prod in p.produtos if prod.categoria == categoria]), produtos_categoria))

    def total_vendas(self):
        return reduce(lambda acc, pedido: acc + pedido.total_pedido(), self.pedidos, 0)



try:
    produto = Produto("Camisa", 50.0, "Vestuário")
    print(produto.detalhes())  
except Exception as e:
    print(f"Erro inesperado: {e}")

produto1 = Produto("Camisa", 50.0, "Vestuário")
produto2 = Produto("Calça", 80.0, "Vestuário")
produtos = [produto1, produto2]
quantidade = {produto1: 2, produto2: 1}

pedido = Pedido(produtos, quantidade, "Cliente1")
print("Total do Pedido:", pedido.total_pedido()) 
print("Detalhes do Pedido:", pedido.detalhes_pedido())

gestor = GestorDePedidos()


produto1 = Produto("Camisa", 50.0, "Vestuário")
produto2 = Produto("Calça", 80.0, "Vestuário")
produtos = [produto1, produto2]
quantidade1 = {produto1: 2, produto2: 1}


produto3 = Produto("Tênis", 110.0, "Vestuário")
produto4 = Produto("Celular", 4500.0, "Eletrônico")
produtos2 = [produto3, produto4]
quantidade2 = {produto3: 2, produto4: 1}

pedido = Pedido(produtos2, quantidade2, "Diego", status="Antigo")
pedido2 = Pedido(produtos, quantidade1, "Jonas", status="Novo")
gestor.adicionar_pedido(pedido)
gestor.adicionar_pedido(pedido2)


pedidos_novos = gestor.listar_pedidos_por_status("Novo")

pedidos_antigo = gestor.listar_pedidos_por_status("Antigo")
print("Pedidos com status 'Novo':", [p.detalhes_pedido() for p in pedidos_novos])
print("Pedidos com status 'Antigo':", [p.detalhes_pedido() for p in pedidos_antigo])