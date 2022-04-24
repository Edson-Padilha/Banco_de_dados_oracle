import sqlite3

con = sqlite3.connect('Brandili.db')

cursor = con.cursor()

cursor.execute('INSERT INTO Minha_Tabela VALUES("27/11/1981","Padilha","40")')
cursor.execute('INSERT INTO Minha_Tabela VALUES ("14/01/2020","Isa","2")')
cursor.execute('INSERT INTO Minha_Tabela VALUES ("14/06/1993","Josi","30")')
cursor.execute('INSERT INTO Minha_Tabela VALUES ("17/11/1953","Silvestre","60")')
cursor.execute('INSERT INTO Minha_Tabela VALUES ("18/08/1996","Lisa","27")')
# LIKE 'P%' procura por nome onde a primeira letra é P
consulta = cursor.execute('''
SELECT * FROM Minha_Tabela
WHERE nome LIKE 'P%'
 ''').fetchall()

for linha in consulta:
    print(linha)

# LIKE '%a' procura por nome onde a última letra é i
consulta = cursor.execute('''
SELECT * FROM Minha_Tabela
WHERE nome LIKE '%i'

''').fetchall()

for linha in consulta:
    print(linha)

# LIKE '%os% procura por nome onde contenha sa
consulta = cursor.execute('''
SELECT * FROM Minha_Tabela
WHERE nome LIKE '%sa%'
''').fetchall()
for linha in consulta:
    print(linha) 

# Procura por nome onde o segundo caracter é I
consulta = cursor.execute('''
SELECT * FROM Minha_Tabela
WHERE nome LIKE '_i%'
''').fetchall()

for linha in consulta:
    print(linha)

# Procura por nome onde o primeiro caracter é I
consulta = cursor.execute('''
SELECT * FROM MInha_Tabela
WHERE nome LIKE 'i_%'
''').fetchall()

for linha in consulta:
    print(linha)
# 
consulta = cursor.execute('''
SELECT * FROM MInha_Tabela
WHERE nome LIKE 'i__%'
''').fetchall()

for linha in consulta:
    print(linha)

# Busca por nomes onde inicia com P e finaliza com a
consulta = cursor.execute('''
SELECT * FROM Minha_Tabela
WHERE nome LIKE 'p%a'
''').fetchall()
for linha in consulta:
    print(linha)