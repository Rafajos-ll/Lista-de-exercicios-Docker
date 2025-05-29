from datetime import datetime

# Obtém a data e hora atual
agora = datetime.now()

# Formata como string: DD/MM/AAAA HH:MM:SS
data_hora_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")

# Imprime no console
print("Data e hora atual:", data_hora_formatada)