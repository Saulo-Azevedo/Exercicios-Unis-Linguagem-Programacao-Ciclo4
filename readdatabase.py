# -*- coding: utf-8 -*-

"""             Atividade - Ciclo 4 :
    Aqui criamos select que retorna as informações salvas pelo arquivo main.
"""

import sqlite3

conn = sqlite3.connect('dbimc.db')
cursor = conn.cursor()

# lendo os dados
cursor.execute("""
SELECT * FROM pacientes;
""")

for linha in cursor.fetchall():
    print(linha)

conn.close()