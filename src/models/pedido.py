from src.models.desconto import IDesconto


class Pedido:
    """Entidade Pedido: guarda o cliente, o desconto e o valor do pedido."""

    def __init__(self, cliente, desconto: IDesconto, valor_original: float = 0.0):
        self.cliente = cliente
        self.desconto = desconto
        self.valor_original = valor_original

    def valor_final(self, valor: float) -> float:
        self.valor_original = valor
        return self.valor_original - self.desconto.calcular(self.valor_original)
