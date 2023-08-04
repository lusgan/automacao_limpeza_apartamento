# -*- coding: utf-8 -*-
"""
Created on Wed May 31 18:29:51 2023

@author: balbi
"""

import yagmail
import time
import datetime
import math
import time


def rotaciona(dic):
    novo_dic = dic.copy()
    novo_dic["Sala e Lavanderia"] = dic["Descanso"]
    novo_dic["Banheiro"] = dic["Sala e Lavanderia"]
    novo_dic["Descanso"] = dic["Banheiro"]
    novo_dic["Lixo da semana"] = dic["Banheiro"]
    novo_dic["data"] = dic["data"]+datetime.timedelta(7)
    return novo_dic

#definindo a data inicial,e o dicionario que contem o que cada um vai fazer
dataInicial = datetime.date(2023,4,28)
dic = {"Sala e Lavanderia":"Terceiro morador","Banheiro":"Lucas","Descanso":"Samuel","Lixo da semana":"Samuel","data" : dataInicial}

# caso queira ver se ta certo as datas: proximoDia = dataInicial + datetime.timedelta(7)
#calculando a quantidade de dias desde a data inicial
qtd_dias_passaram = (datetime.date.today() - dataInicial).days
qtd_dias_passaram  = math.floor(qtd_dias_passaram/7)*7

#se tiver passado 1 semana, o programa vai rotacionar, se tiver passado x semanas, o programa vai rotacionar x vezes.
if(qtd_dias_passaram%7 == 0):
    qtd_semanas = int(qtd_dias_passaram/7)
    novo_dic = dic.copy()
    
    for i in range(qtd_semanas):
        novo_dic = rotaciona(dic)
        dic = novo_dic
    
    if novo_dic["data"].month<10:
        mes = '0'+str(novo_dic['data'].month)
        dia = str(novo_dic['data'].day)
        
        if(int(dia)<10):
            dia = '0'+dia
            
        ano = str(novo_dic['data'].year)
        novo_dic["data"] = dia+'/'+mes+'/'+ano
        
    else:
        novo_dic["data"] = f'{novo_dic["data"].day}/{novo_dic["data"].month}/{novo_dic["data"].year}'

'''print(f'Sala e lavanderia: {novo_dic["Sala e Lavanderia"]}')
print(f'Banheiro: {novo_dic["Banheiro"]}')
print(f'Descanso: {novo_dic["Descanso"]}')
print(f'Lixo da semana: {novo_dic["Lixo da semana"]}')
print(f'Referente ao dia: {novo_dic["data"]}')
print("\n\nObs: o programa atualiza sozinnho a data de referência, e faz a rotação das tarefas de cada um automaticamente")
'''

try:
    with open("senha.txt",'r') as file:
        senha = file.readlines()
        senha_do_email = senha[0]

    
    user = yagmail.SMTP(user="botthomas35@gmail.com",password=senha_do_email)
    user.send(to=["balbinogandolfo@gmail.com","samuelcamargo931@gmail.com"],subject="Limpeza do apartamento", contents = f'Sala e lavanderia: {novo_dic["Sala e Lavanderia"]}\nBanheiro: {novo_dic["Banheiro"]}\nDescanso: {novo_dic["Descanso"]}\nLixo da semana: {novo_dic["Lixo da semana"]} \nReferente ao dia: {novo_dic["data"]}\n\nObs: o programa atualiza sozinnho a data de referência, e faz a rotação das tarefas de cada um automaticamente')
    
    print("email enviado")
    time.sleep(5)
except Exception as error:
    print("Email nao enviado, erro abaixo:")
    print(error)
    time.sleep(5)
