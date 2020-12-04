# -*- coding: utf-8 -*-

"""             Atividade - Ciclo 4 :
    Aqui criamos delete que para um registro da tabela pacientes.
"""
import sqlite3

conn = sqlite3.connect('dbimc.db')
cursor = conn.cursor()

id_cliente = int (input("Informe o numero do registro a ser apagado: "))

# excluindo um registro da tabela
cursor.execute("""
DELETE FROM pacientes
WHERE id = ?
""", (id_cliente,))

conn.commit()

print('Registro excluido com sucesso.')

conn.close()