import sqlite3

con = sqlite3.connect('Brandili.db')
Cursor = con.cursor()

Cursor.execute('CREATE TABLE Minha_Tabela ( Data text, Nome text, Idade Real)')
con.commit()

