from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():

    dados = request.get_json()
    expressao = dados['expressao']

    try:

        permitidos = {
            "sqrt": math.sqrt,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "log": math.log10,
            "ln": math.log,
            "pi": math.pi,
            "e": math.e,
            "pow": pow
        }

        resultado = eval(expressao, {"__builtins__": None}, permitidos)

        return jsonify({
            "resultado": resultado
        })

    except Exception:
        return jsonify({
            "resultado": "Erro"
        })

if __name__ == '__main__':
    app.run(debug=True)
