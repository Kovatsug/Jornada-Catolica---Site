from flask import Flask, render_template

import sqlite3

def buscar_santos():
    conn = sqlite3.connect('./Data/data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT nome FROM santo')
    resultados = cursor.fetchall()
    conn.close()
    return resultados



def converter(santos):
    text=""

    for i,s in enumerate(santos()):
        text+=f"<p id='{i}'>{s[0]}</p>"
    return text
    

# Criando a instância do Flask
app = Flask(__name__)

# Rota simples para a página inicial
@app.route('/')
def home():
    return render_template('modelo.html')


@app.route("/santos")
def santos():
    return f'{{ "marcacao": "{converter(buscar_santos())}" }}'

@app.route("/santos/<int:id>")
def santo(id):
    return f'{{ "marcacao": "{converter(buscar_santos()[id])}" }}'









# Rodando o servidor
if __name__ == '__main__':
    app.run(debug=True)
