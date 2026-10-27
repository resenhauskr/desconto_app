from src.app.use_cases.criar_pedido import CriarPedido

if __name__ == "__main__":
    caso_de_uso = CriarPedido()

    entradas = [
        ("Leonardo", 100.0, "vip"),
        ("Maria", 200.0, "normal"),
        ("Carlos", 50.0, "premium"),
    ]

    for cliente, valor, tipo in entradas:
        pedido = caso_de_uso.executar(cliente, valor, tipo)
        print(f"Cliente: {pedido.cliente}")
        print(f"Valor final: {pedido.valor_final()}")