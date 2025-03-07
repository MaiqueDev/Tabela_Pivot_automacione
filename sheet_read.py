from openpyxl import load_workbook

#Lê pasta de trabalho e planilha
wb = load_workbook("pastplanilha/pivot_table.xlsx")
sheet = wb["Relatório"]

#acessando um valor específico
print(sheet["B3"].value)

# Iteração de valor por meio do loop

for i in range(2, 5):
    ano = sheet["A%s" %i].value
    am =  sheet["B%s" %i].value
    bt =  sheet["C%s" %i].value
    print("{0} o Aston martin vendeu {1}e o Bentley vendeu {2}".format(ano, am, bt)) 