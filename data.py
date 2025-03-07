import pandas as pd

data = pd.read_excel("pastplanilha/VendaCarros.xlsx")
print(data)

print(data.head())

# 2- Listando os  primeiros registros. caso eu não passe um parâmetro ele puxa os 5 primeiros
print(data.head())

# Lista os últimos registros
print(data.tail())

# situação hipotética : REALIZANDO A CONTAGEM DE VALORES POR FABRICANTE