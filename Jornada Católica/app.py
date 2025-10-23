from flask import Flask, render_template

# Criando a instância do Flask
app = Flask(__name__)

# Rota simples para a página inicial
@app.route('/')
def home():
    return render_template('modelo.html')


@app.route("/santos")
def santos():
    return "<p>santos aqui</p>"











# Rodando o servidor
if __name__ == '__main__':
    app.run(debug=True)
