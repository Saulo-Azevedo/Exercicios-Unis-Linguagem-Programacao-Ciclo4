# -*- coding: utf-8 -*-

"""             Atividade - Ciclo 4 :
    Aqui criamos tabela que serão usadas no arquivo main para registro das informções.
"""
import sqlite3

# conectando...
conn = sqlite3.connect('dbimc.db')
# definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute("""
CREATE TABLE pacientes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        endereco TEXT NOT NULL ,
        altura     VARCHAR(4) NOT NULL,
        peso     VARCHAR(4) NOT NULL,
        imc     VARCHAR (5) NOT NULL         
);
""")

print('Tabela criada com sucesso.')
# desconectando...
conn.close()