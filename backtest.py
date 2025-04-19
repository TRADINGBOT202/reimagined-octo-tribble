import pandas as pd

# Cargar datos CSV
df = pd.read_csv("BTCUSDT_1h.csv", parse_dates=["timestamp"])
df.set_index("timestamp", inplace=True)

# Parámetros de estrategia
take_profit_pct = 0.03  # 3%
stop_loss_pct = 0.02    # 2%
capital = 1000
risk_per_trade = 0.02  # 2% del capital

trades = []

for i in range(1, len(df) - 1):
    row = df.iloc[i]
    next_row = df.iloc[i + 1]

    # Señal de entrada: vela verde grande
    if row["close"] > row["open"] and (row["close"] - row["open"]) > 0.005 * row["open"]:
        entry_price = next_row["open"]
        stop_loss = entry_price * (1 - stop_loss_pct)
        take_profit = entry_price * (1 + take_profit_pct)

        # Simular el recorrido del precio
        max_price = next_row["high"]
        min_price = next_row["low"]

        result = None
        if min_price <= stop_loss:
            result = -risk_per_trade * capital
        elif max_price >= take_profit:
            result = risk_per_trade * capital * (take_profit_pct / stop_loss_pct)
        else:
            # ni TP ni SL: cerrar en cierre de vela
            result = (next_row["close"] - entry_price) / entry_price * risk_per_trade * capital

        trades.append(result)

# Resultados
total_profit = sum(trades)
win_trades = len([x for x in trades if x > 0])
loss_trades = len([x for x in trades if x < 0])
total_trades = len(trades)

print(f"Trades totales: {total_trades}")
print(f"Ganadoras: {win_trades}, Perdedoras: {loss_trades}")
print(f"Ganancia total: {total_profit:.2f} USDT"
