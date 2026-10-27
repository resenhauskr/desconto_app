from src.models.desconto import DescontoNormal, DescontoPremium, DescontoVIP
from src.models.pedido import Pedido
from src.services.pedido_service import PedidoService


def main():
    service = PedidoService()

    service.adicionar_pedido(Pedido("Leonardo", DescontoVIP(), 100))
    service.adicionar_pedido(Pedido("Maria", DescontoNormal(), 200))
    service.adicionar_pedido(Pedido("Carlos", DescontoPremium(), 50))

    service.processar_pedidos()


if __name__ == "__main__":
    main()