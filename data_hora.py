from datetime import datetime, timedelta

tipo_carro = "p"
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == "p":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou: {data_atual} e ficará pronto às: {data_estimada}")

elif tipo_carro == "m" :
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"O carro chegou: {data_atual} e ficará pronto às: {data_estimada}")


else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"O carro chegou: {data_atual} e ficará pronto às: {data_estimada}")




#STRFTIME  >> FORMATAR E CONVERTER DATA PARA BR:

d = datetime.now()

print(d.strftime("%d/%m/%Y %H:%M")) #dia/mes/ano  hora:minutos

#CONVERTENDO STRING PARA DATETIME:
date_string = "20/07/2026 16:30"
d = datetime.strptime(date_string, "%d/%m/%Y %H:%M")
print(d)

#PYTZ >> fusorario

import pytz

data = datetime.now(pytz.timezone("Europe/Oslo"))
data2 = datetime.now(pytz.timezone("America/Sao_Paulo"))

print(data)
print(data2)