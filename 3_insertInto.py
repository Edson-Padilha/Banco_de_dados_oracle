import sqlite3
import random

con = sqlite3.connect('Brandili.db')
Cursor = con.cursor()

Cursor.execute('INSERT INTO Minha_Tabela VALUES ("14/01/2020","Isa","02")')

for loop in range(10):
    numero = random.randint(10,20)
Cursor.execute(F'INSERT INTO Minha_Tabela VALUES ("17/11/1953", "Silvestre",{numero})')

print (numero)