from src.app.frameworks.database.memory_database import MemoryDatabase
from src.app.adapters.repositories.pedido_repository import PedidoRepository
from src.app.use_cases.criar_pedido import CriarPedido
from src.app.use_cases.listar_pedidos import ListarPedidos

if __name__ == "__main__":
    database = MemoryDatabase()
    repositorio = PedidoRepository(database)

    criar_pedido = CriarPedido(repositorio)
    listar_pedidos = ListarPedidos(repositorio)

    criar_pedido.executar("Leonardo", 100.0, "vip")
    criar_pedido.executar("Maria", 200.0, "normal")
    criar_pedido.executar("Carlos", 50.0, "premium")

    print("Pedidos salvos:")
    for pedido in listar_pedidos.executar():
        print(f"Cliente: {pedido.cliente}")
        print(f"Valor final: {pedido.valor_final()}")