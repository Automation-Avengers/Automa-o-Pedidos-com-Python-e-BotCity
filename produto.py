from excecao import ValorInvalidoError

# Antonio - minha parte
class Produto:
    def __init__(self, nome, preco, categoria):
        if preco < 0:
            raise ValorInvalidoError("O preço do produto deve ser positivo.")
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

    def detalhes(self):
        return f"{self.nome} - Categoria: {self.categoria} - Preço: {self.preco}"