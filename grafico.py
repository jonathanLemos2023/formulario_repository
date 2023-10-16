from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Armazenar mensagens enviadas no formulário em uma lista
mensagens = []

@app.route('/')
def index():
    return render_template('index.html', mensagens=mensagens)

@app.route('/enviar', methods=['POST'])
def enviar():
    if request.method == 'POST':
        mensagem = request.form['mensagem']
        mensagens.append(mensagem)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)