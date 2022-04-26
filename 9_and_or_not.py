import sqlite3

con = sqlite3.connect('Brandili.db')
cursor = con.cursor()

cursor.execute('INSERT INTO Minha_Tabela VALUES ("27/11/1981","Padilha","40")')
cursor.execute('INSERT INTO Minha_Tabela VALUES ("26/08/1964","Margarete","58")')
cursor.execute('INSERT INTO MInha_Tabela VALUES ("14/01/2020","Isadora","2")')
cursor.execute('INSERT INTO MInha_Tabela VALUES ("14/06/1993","Josiane","30")')

# And
consulta = cursor.execute('''
SELECT * FROM Minha_Tabela
WHERE idade > 50 and idade < 60 
''').fetchall()

for linha in consulta:
    print(linha)

# OR

consulta = cursor.execute('''
SELECT * FROM Minha_Tabela
WHERE idade < 10 OR idade > 30
''').fetchall()

for linha in consulta:
    print(linha)

# NOT

consulta = cursor.execute('''
SELECT * FROM Minha_Tabela
WHERE idade > 30 AND NOT idade = 58
''').fetchall()

for linha in consulta:
    print("NOT",  linha)