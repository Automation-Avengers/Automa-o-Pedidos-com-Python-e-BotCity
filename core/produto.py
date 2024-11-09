from core.excecao import ValorInvalidoError

class Produto:
    def __init__(self, nome: str, preco: float, categoria: str):
        if preco < 0:
            raise ValorInvalidoError("O preço do produto deve ser positivo.")
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

    def detalhes(self):
        return f"{self.nome} - Cateagoria: {self.categoria} - Preço: R$ {self.preco}"


    def to_dict(self):
        return {
            "nome": self.nome,
            "preco": self.preco,
            "categoria": self.categoria
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["nome"], data["preco"], data["categoria"])