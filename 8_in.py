import sqlite3

con = sqlite3.connect('Brandili.db')
cursor = con.cursor()

cursor.execute('INSERT INTO Minha_Tabela VALUES ("14/01/2020","Isa","2")')
cursor.execute('INSERT INTO Minha_Tabela VALUES("27/11/1981","Edson","40")')
cursor.execute('INSERT INTO Minha_Tabela VALUES ("14/06/1993","Josiane","30")')
cursor.execute('INSERT INTO Minha_Tabela VALUES ("01/01/2022","Rodrigo","1")')

# IN é o mesmo que dizer contém na lista
consulta = cursor.execute('''SELECT * FROM Minha_Tabela
WHERE idade IN (2,30,27)''')

for linha in consulta:
    print(linha)

