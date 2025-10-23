from classes import *

def menu():
    options=["1. Add Santo", "2. Add Oração", "3. Add Milagre", "4. add sacramento", "5. add catecismo", "6. add liturgia"]
    for i in options:
        print(i)
    op=int(input("Escolha:   "))

    if op==1 :
        name=input("nome: ")
        data_nasc=input("data de nascimento: ")
        data_falec=input("data de falecimento: ")
        voc=input("vocação: ")        
        biografia=input("Biografia: ")
        santo=Santo(nome=name, nascimento=data_nasc, falecimento=data_falec, vocacao=voc, biografia=biografia)
        return(santo)

    elif op==2 :
        name=input("Nome: ")
        texto=input("Texto da oração: ")
        santo_relacionado=input("Santo relacionado: ")
        oracao=Oracao(nome=name, texto=texto, santo_relacionado=santo_relacionado)
        return(oracao)
    
    elif op==3 :
        tipo=input("Tipo do milagre: ")
        local=input("Local do milagre: ")
        data=input("Data de acontecimento do milagre: ")
        descricao=input("Descrição do milagre: ")
        santo_relacionado=input("Santo relacionado(se houver): ")
        milagre=Milagre(tipo=tipo, local=local, data=data, descricao=descricao, santo_relacionado=santo_relacionado)
        return(milagre)
    
    elif op==4:
        nome=input("Nome do sacramento: ")
        descricao=input("Descricao: ")
        materiais=input("Materiais usados: ")
        ritual=input("Ritual (como faz): ")
        ocasiao=input("Quando se faz: ")
        sacramento=Sacramento(nome=nome, descricao=descricao, materiais=materiais, ritual=ritual, ocasiao=ocasiao)
        return(sacramento)

    elif op==5:
        titulo=input("Título: ")
        descricao=input("Descrição: ")
        texto_completo=input("Texto completo: ")
        categoria=input("Categoria (doutrina, dogma etc): ")
        catecismo=Catecismo(titulo=titulo, descricao=descricao, texto_completo=texto_completo, categoria=categoria)
        return(catecismo)
    
    elif op==6:
        nome=input("Nome da celebração ou liturgia: ")
        descricao=input("Descrição: ")
        tipo=input("Tipo (Eucaristia, Ofício, Novena, Festa Litúrgica etc): ")
        data=input("Data (se aplicável): ")
        texto=input("Texto completo da liturgia: ")
        liturgia=Liturgia(nome=nome, descricao=descricao, tipo=tipo, data=data, texto=texto)
        return(liturgia)
    
    else:
        print("Opção inválida.")

