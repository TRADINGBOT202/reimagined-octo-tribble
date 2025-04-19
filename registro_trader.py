import csv
import os
from datetime import datetime

class RegistroTrader:
    def __init__(self, archivo='registro_operaciones.csv'):
        self.archivo = archivo
        self.campos = ['fecha', 'par', 'tipo_operacion', 'precio_entrada', 'precio_salida', 'ganancia']
        self._crear_archivo()

    def _crear_archivo(self):
        if not os.path.exists(self.archivo):
            with open(self.archivo, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.campos)
                writer.writeheader()

    def registrar_operacion(self, par, tipo_operacion, precio_entrada, precio_salida):
        ganancia = round(precio_salida - precio_entrada, 2) if tipo_operacion == 'compra' else round(precio_entrada - precio_salida, 2)
        with open(self.archivo, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.campos)
            writer.writerow({
                'fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'par': par,
                'tipo_operacion': tipo_operacion,
                'precio_entrada': precio_entrada,
                'precio_salida': precio_salida,
                'ganancia': ganancia
            })

# Ejemplo de uso
if __name__ == '__main__':
    registro = RegistroTrader()
    registro.registrar_operacion('BTC/USDT', 'compra', 28000.0, 28500.0)
