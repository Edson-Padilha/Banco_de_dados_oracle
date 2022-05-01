import sqlite3

con = sqlite3.connect('Brandili.db')

cursor = con.cursor()

cursor.execute('INSERT INTO Minha_Tabela VALUES ("27/11/1981","EDSON","40")')
cursor.execute('INSERT INTO Minha_Tabela VALUES ("14/01/2020","Isadora","2")')
cursor.execute('INSERT INTO Minha_Tabela VALUES ("14/06/1993","Josi","30")')
cursor.execute('INSERT INTO Minha_Tabela VALUES ("15/02/1942","Laurita","78")')

# Retorno uma quantidade limitade de registros
consulta = cursor.execute('''
SELECT * FROM Minha_Tabela
LIMIT 2
''').fetchall()

for linha in consulta:
    print(linha)