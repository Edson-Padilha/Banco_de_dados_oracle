import sqlite3

con = sqlite3.connect('Brandili.db')

cursor = con.cursor()

cursor.execute('INSERT INTO Minha_Tabela VALUES ("27/11/1981","PADILHA","40")')
cursor.execute('INSERT INTO Minha_Tabela VALUES ("NULL","NULL","NULL")')
cursor.execute('INSERT INTO Minha_Tabela VALUES ("14/06/1993","Josi","30")')

cursor.execute('''
DELETE FROM Minha_Tabela
WHERE nome = "NULL"
AND idade = "NULL"
''')

consulta = cursor.execute('''
SELECT * FROM Minha_Tabela
''').fetchall()

for linha in consulta:
    print(linha)
