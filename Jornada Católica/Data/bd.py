from pony.orm import *
from menu import menu
from i import *
from classes import *
db.bind(provider='sqlite', filename='data.db', create_db=True)
db.generate_mapping(create_tables=True)

with db_session:

    # nome = "São Paulo Apóstolo"
    # nascimento = "Por volta do ano 5 d.C., Tarso, Cilícia (atual Turquia)"
    # falecimento = "Por volta de 67 d.C., Roma, Império Romano"
    # vocacao = "Apóstolo e missionário cristão"
    # biografia = """
    # São Paulo, também conhecido como Paulo de Tarso, foi um dos principais líderes e teólogos do cristianismo primitivo. Nascido em Tarso, na Cilícia, era judeu da tribo de Benjamim e cidadão romano. Inicialmente chamado de Saulo, foi um fariseu zeloso que perseguiu os primeiros cristãos, participando inclusive do martírio de Santo Estêvão.

    # Sua conversão ocorreu de forma dramática na estrada de Damasco, quando teve uma visão de Jesus Cristo que o questionou: “Saulo, Saulo, por que me persegues?”. A partir desse momento, tornou-se um fervoroso seguidor de Cristo, adotando o nome Paulo e dedicando sua vida à evangelização dos gentios.

    # Paulo realizou diversas viagens missionárias pelo Império Romano, fundando comunidades cristãs e escrevendo cartas — as epístolas — que hoje compõem parte significativa do Novo Testamento. Seus escritos abordam temas como fé, graça, salvação, ética cristã e a vida em Cristo, influenciando profundamente a teologia cristã.

    # Foi preso várias vezes por causa de sua pregação e, segundo a tradição, morreu decapitado em Roma durante a perseguição aos cristãos sob o imperador Nero. Sua festa litúrgica é celebrada em 29 de junho, junto com São Pedro, e também em 25 de janeiro, data da sua conversão.

    # São Paulo é padroeiro dos autores, editores, teólogos, missionários e da cidade de São Paulo. Sua vida é um testemunho de transformação radical, coragem e dedicação ao anúncio do Evangelho.
    # """



    # santo=Santo(nome=nome, nascimento=nascimento, falecimento=falecimento, vocacao=vocacao, biografia=biografia)
    # commit()

    while 1:
        obj=menu()
        commit()