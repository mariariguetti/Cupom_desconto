from flask import Flask, jsonify, request
from datetime import datetime
from flask_pydantic_spec import FlaskPydanticSpec

app = Flask(__name__)

spec = FlaskPydanticSpec('flask',
                         title='First API - SENAI',
                         version='1.0.0')
spec.register(app)


@app.route('/desconto/<valor_inicial>/<primeira_compra>/', methods = ['GET'])
def desconto(valor_inicial, primeira_compra):
    """
        **API para calcular desconto**

        ##Endpoint:
        GET / desconto

        ##Parâmetros:
        {
            "valor_inicial": "100",
            "primeira_compra": True
        }

        ##Resposta (JSON)
        {
            "data_processamento": data_processamento,
            "valor_inicial": valor_inicial,
            "desconto": desconto,
            "desconto_primeira_compra": primeira_compra,
            "valor_final": desconto
        }


        :return:
        """

    try:
        valor_inicial = float(valor_inicial)
        primeira_compra = bool(primeira_compra)

        if valor_inicial <= 100:
            desconto = valor_inicial

        elif valor_inicial >= 101 or valor_inicial <= 500:
            desconto = valor_inicial * 0.05

        else:
            desconto = valor_inicial * 0.1

        if primeira_compra == True:
            desconto = valor_inicial - 25

        data_processamento = datetime.today().strftime("%d/%m/%Y")

        dados = {
            "data_processamento": data_processamento,
            "valor_inicial": valor_inicial,
            "desconto": desconto,
            "desconto_primeira_compra": primeira_compra,
            "valor_final": desconto
        }

    except ValueError:
        dados = {
            "status": "error",
            "msg": "Dados Inválidos"
        }
        return jsonify(dados), 400

    return jsonify(dados)


if __name__ == '__main__':
    app.run(debug=True, port=5002, host='0.0.0.0')
