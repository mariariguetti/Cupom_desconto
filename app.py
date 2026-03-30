from flask import Flask, jsonify, request
from datetime import datetime
from flask_pydantic_spec import FlaskPydanticSpec

app = Flask(__name__)

spec = FlaskPydanticSpec('flask',
                         title='First API - SENAI',
                         version='1.0.0')
spec.register(app)


@app.route('/desconto', methods=['POST'])
def desconto():
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
        dados_entrada = request.get_json()
        valor_inicial = float(dados_entrada["valor_inicial"])
        primeira_compra = dados_entrada["primeira_compra"].upper
        desconto = 0

        if valor_inicial <= 100:
            desconto = 0

        elif valor_inicial >= 500:
            desconto = valor_inicial * (10 / 100)

        else:
            desconto = valor_inicial * (5 / 100)

        if primeira_compra == "True" and (valor_inicial > 50):
            desconto = desconto + 25
        valor_final = valor_inicial - desconto

        data_processamento = datetime.today().isoformat()

        dados = {
            "data_processamento": data_processamento,
            "valor_inicial": valor_inicial,
            "valor_desconto": desconto,
            "valor_final": valor_final
        }

        return jsonify(dados), 400

    except Exception as e:
       return jsonify({"msg": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5002, host='0.0.0.0')
