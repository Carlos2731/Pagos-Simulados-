from pagos import Usuario, Pago

def main():
    # Crear usuarios de ejemplo
    carlos = Usuario("Carlos", 1000)
    brayan = Usuario("Brayan", 500)

    print("=== Estado inicial ===")
    print(carlos)
    print(brayan)

    # Simular transferencia
    transferencia = Pago(carlos, brayan, 200)
    resultado = transferencia.procesar()
    print(resultado)

    print("\n=== Estado final ===")
    print(carlos)
    print(brayan)

if __name__ == "__main__":
    main()
