import sqlite3

con = sqlite3.connect('Brandili.db')
cursor = con.cursor()

cursor.execute('INSERT INTO Minha_Tabela VALUES ("27/11/1981","EDSON","40")')
cursor.execute('INSERT INTO Minha_Tabela VALUES ("14/06/1993",NULL,NULL)')
cursor.execute('INSERT INTO Minha_Tabela VALUES (NULL,"JOSI","30")')

consulta = cursor.execute('''
SELECT * FROM Minha_Tabela
WHERE nome IS NULL''').fetchall()

for linha in consulta:
    print(linha)