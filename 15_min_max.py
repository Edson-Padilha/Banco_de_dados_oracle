import sqlite3

con = sqlite3.connect('Brandili.db')

cursor = con.cursor()

cursor.execute('INSERT INTO Minha_Tabela VALUES ("27/11/1981","EDSON","40")')
cursor.execute('INSERT INTO Minha_Tabela VALUES ("14/06/1993","josi","30")')
cursor.execute('INSERT INTO Minha_Tabela VALUES ("14/01/2020","ISADORA","2")')

# Trazendo a menor idade 
consulta = cursor.execute('''
SELECT MIN(idade), * FROM Minha_Tabela

''').fetchall()

for linha in consulta:
    print(linha)

# Trazendo a maior idade 
consulta = cursor.execute('''
SELECT MAX(idade), * FROM Minha_Tabela

''').fetchall()

for linha in consulta:
    print(linha)