import pandas as pd

# importando os dados

data = pd.read_excel ("pastplanilha/VendaCarros.xlsx")
#print(type(data))

#Selecionar colunas específicas do dataframe
df = data[["Fabricante", "ValorVenda", "Ano" ]]
print(df)

#criando a tabela pivot
pivot_table = df.pivot_table(
    index="Ano",
    columns="Fabricante",
    values="ValorVenda",
    aggfunc="sum"
)

print(pivot_table)

#Exportando tabela pivô em arquivo excel
pivot_table.to_excel("pastplanilha/pivot_table.xlsx", "Relatório")