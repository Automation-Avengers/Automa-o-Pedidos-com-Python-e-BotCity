from functools import reduce
from typing import List, Dict
from datetime import datetime
from core.pedido import Pedido
import core.manipulacaoAquivo

def log_atividade(func):
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        
        if resultado is None:
            resultado_info = f"Função {func.__name__} executada com sucesso (sem retorno)."
        else:
            if isinstance(resultado, list) and all(isinstance(p, Pedido) for p in resultado):
                resultado_info = [
                    f"Cliente: {p.cliente}, Status: {p.status}, Total: R$ {p.total_pedido():.2f}"
                    for p in resultado
                ]
            else:
                resultado_info = resultado
        
        pedidos_info = ", ".join(
            f"Cliente: {pedido.cliente}, Status: {pedido.status}" 
            for pedido in args[1:] if isinstance(pedido, Pedido)
        )
        
        print(f"[LOG] {datetime.now()} - Executou: {func.__name__} | Args: {pedidos_info} | Retorno: {resultado_info}")
        return resultado
    return wrapper


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

    def salvar_dados_json(self, arquivo="pedidos.json"):
        core.manipulacaoAquivo.salvar_dados_json(self.pedidos, arquivo)

    def carregar_dados_json(self, arquivo="pedidos.json"):
        self.pedidos = core.manipulacaoAquivo.carregar_dados_json(arquivo)

    def salvar_dados_binario(self, arquivo="pedidos.pkl"):
        core.manipulacaoAquivo.salvar_dados_binario(self.pedidos, arquivo)

    def carregar_dados_binario(self, arquivo="pedidos.pkl"):
        self.pedidos = core.manipulacaoAquivo.carregar_dados_binario(arquivo)
