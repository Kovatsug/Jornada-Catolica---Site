from i import *

class Santo(db.Entity):
    id=PrimaryKey(int, auto=True)
    nome=Required(str)
    nascimento=Required(str)
    falecimento=Required(str)
    vocacao=Required(str)       #leigo, sacerdote franciscano, diocesano etc.
    imagem=Optional(str)
    biografia=Required(str)
    oracoes=Set("Oracao")

class Milagre(db.Entity):
    id=PrimaryKey(int, auto=True)
    tipo=Optional(str)  
    local=Required(str)
    data=Required(str)
    descricao=Required(str)

class Oracao(db.Entity):
    id=PrimaryKey(int, auto=True)
    nome=Required(str)
    texto=Required(str)
    santo_relacionado=Optional(Santo)

class Sacramento(db.Entity):
    nome=Required(str)
    descricao=Required(str)     #oq é 
    materiais=Optional(str)     #oq usa
    ritual=Required(str)        #como faz
    ocasiao=Optional(str)       #quando faz

class Catecismo(db.Entity):
    titulo=Required(str)        #tema (10 mandamentos, pecado etc)
    descricao=Required(str)         
    texto_completo=Required(str)    
    categoria=Required(str)     #doutrina, dogma etc

class Liturgia(db.Entity):
    nome=Required(str)          #Nome da celebração ou liturgia, ex.: "Missa Dominical", "Ofício de Nossa Senhora"
    descricao=Required(str)     #Um resumo do que é a liturgia, ex.: "Celebração da Eucaristia aos domingos"
    tipo=Required(str)          #Categoria ou tipo da liturgia, ex.: "Eucaristia", "Ofício", "Novena", "Festa Litúrgica"
    data=Optional(str)          
    texto=Required(str)         #Conteúdo completo da liturgia: descrição, história, rituais detalhados etc