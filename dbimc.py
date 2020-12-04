
# -*- coding: utf-8 -*-

"""             Atividade - Ciclo 4 :
    Aqui criamos a conexão com banco.
"""

import sqlite3

con = sqlite3.connect('dbimc.db')
con.close()