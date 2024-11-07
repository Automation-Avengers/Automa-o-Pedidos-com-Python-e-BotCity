from functools import reduce
from excecao import QuantidadeInvalidaError

# Antonio - minha parte
class Pedido:
    def __init__(self, produtos, quantidade, cliente, status="Novo"):
        if any(q <= 0 for q in quantidade.values()):
            raise QuantidadeInvalidaError("A quantidade deve ser positiva para todos os produtos.")
        
        self.produtos = produtos  
        self.quantidade = quantidade  
        self.cliente = cliente
        self.status = status

    def total_pedido(self):
        return reduce(lambda total, produto: total + produto.preco * self.quantidade[produto], self.produtos, 0)

    def detalhes_pedido(self):
        detalhes = f"Cliente: {self.cliente}\nStatus: {self.status}\n"
        detalhes += "\n".join(f"{produto.detalhes()} - Quantidade: {self.quantidade[produto]}" for produto in self.produtos)
        detalhes += f"\nTotal: {self.total_pedido()}"
        return detalhes

