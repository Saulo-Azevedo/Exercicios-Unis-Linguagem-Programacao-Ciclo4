# -*- coding: utf-8 -*-

"""             Atividade - Ciclo 4 :
    Criação de um programa em python, que calcula IMC e registra as informações
    em  um banco de dados SQLite.
"""
import sqlite3

conn = sqlite3.connect('dbimc.db')
cursor = conn.cursor()

p_nome = input("Nome Completo: ")
p_endereco = input("Endereço Completo: ")
p_altura = float(input(("Digite sua altura:")))
p_peso =float(input("Digite seu peso: "))

p_imc = round(p_peso  / (p_altura) ** 2,2)

if p_imc< 16:
    print("Seu IMC é: %.2f" % p_imc,"Magreza grave")
elif p_imc < 17:
    print("Seu IMC é: %.2f" % p_imc,"Muito abaixo do peso")
elif p_imc< 18.49:
    print("Seu IMC é: %.2f" % p_imc,"Abaixo do peso")
elif p_imc < 24.99:
    print("Seu IMC é: %.2f" % p_imc,"Peso normal")
elif p_imc < 29.99:
    print("Seu IMC é: %.2f" % p_imc,"Acima do peso")
elif p_imc < 34.99:
    print("Seu IMC é: %.2f" % p_imc,"Obesidade I")
elif p_imc < 39.99:
    print("Seu IMC é: %.2f" % p_imc,"Obesidade II (severa)")
else:
    print("Seu IMC é: %.2f" % p_imc,"Obesidade Grau III (mórbida)")

# inserindo dados na tabela
cursor.execute("""
INSERT INTO pacientes (nome, endereco, altura, peso, imc)
VALUES (?,?,?,?,?)
""", (p_nome, p_endereco, p_altura, p_peso, p_imc))

conn.commit()

print('Dados inseridos com sucesso.')

conn.close()