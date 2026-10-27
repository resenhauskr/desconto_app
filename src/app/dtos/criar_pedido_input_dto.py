from dataclasses import dataclass


@dataclass
class CriarPedidoInputDTO:
    cliente: str
    valor_original: float
    tipo_desconto: str