import sqlite3

con = sqlite3.connect('Brandili.db')

cursor = con.cursor()

cursor.execute('INSERT INTO Minha_Tabela VALUES ("20/11/1981","PADILHA","30")')
cursor.execute('INSERT INTO Minha_Tabela VALUES ("14/01/2020","ISADORA","2")')
cursor.execute('INSERT INTO Minha_Tabela VALUES ("14/06/1993","Josiane","30")')

cursor.execute('''
UPDATE Minha_Tabela
SET idade = "40"
WHERE nome = "PADILHA"
''')

consulta = cursor.execute('''
SELECT * FROM Minha_Tabela
''').fetchall()

for linha in (consulta):
    print(linha)