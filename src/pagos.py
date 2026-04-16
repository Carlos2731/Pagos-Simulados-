class Usuario:
    def __init__(self, nombre, saldo=0):
        self.nombre = nombre
        self.saldo = saldo

    def __str__(self):
        return f"{self.nombre} - Saldo: ${self.saldo:.2f}"


class Pago:
    def __init__(self, remitente, destinatario, monto):
        self.remitente = remitente
        self.destinatario = destinatario
        self.monto = monto

    def procesar(self):
        if self.remitente.saldo >= self.monto:
            self.remitente.saldo -= self.monto
            self.destinatario.saldo += self.monto
            return f"✅ Transferencia exitosa: {self.remitente.nombre} → {self.destinatario.nombre} (${self.monto:.2f})"
        else:
            return f"❌ Error: {self.remitente.nombre} no tiene saldo suficiente."
