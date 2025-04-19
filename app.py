from registro_trader import RegistroTrader

# Crear una instancia del registro
registro = RegistroTrader()

# Simular una operación (puedes cambiar esto luego por señales reales)
par = 'BTC/USDT'
tipo_operacion = 'compra'
precio_entrada = 28000.0
precio_salida = 28500.0

# Registrar la operación
registro.registrar_operacion(par, tipo_operacion, precio_entrada, precio_salida)

print("Operación registrada correctamente.")
