from src.app.entities.pedido import Pedido
from src.app.gateways.pedido_gateway import IPedidoGateway


class ListarPedidos:
    def __init__(self, gateway: IPedidoGateway):
        self.gateway = gateway

    def executar(self) -> list[Pedido]:
        return self.gateway.listar()