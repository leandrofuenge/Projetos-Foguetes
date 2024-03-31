import random
from flask import Flask, jsonify

app = Flask(__name__)


def gerar_variacao_angulo():
    return random.uniform(0, 360)


def gerar_variacao_tempo():
    return random.uniform(1, 5)


def calcular_velocidade_angular(angulo, delta_t):
    return angulo * delta_t


def gerar_variacao_velocidade():
    return random.uniform(0, 10)


def calcular_aceleracao(delta_v, delta_t):
    return delta_v / delta_t


def calcular_pressao_atmosferica(theta, delta_t):
    return theta * delta_t


def calcular_temperatura(tc):
    return tc + 273


def gerar_lambda():
    return random.uniform(0.1, 0.9)


def gerar_frequencia():
    return random.uniform(10, 100)


def calcular_velocidade_vibracao(lambd, frequencia):
    return lambd * frequencia


def calcular_periodo(frequencia):
    return 1 / frequencia


@app.route('/dados/velocidade', methods=['GET'])
def obter_velocidade():
    velocidade = gerar_variacao_velocidade()
    return jsonify({"velocidade": velocidade})


@app.route('/dados/aceleracao', methods=['GET'])
def obter_dados_aceleracao():
    delta_v = gerar_variacao_velocidade()
    delta_t = gerar_variacao_tempo()
    aceleracao = calcular_aceleracao(delta_v, delta_t)
    dados = {
        "variação_velocidade": delta_v,
        "variação_tempo": delta_t,
        "aceleracao": aceleracao
    }
    return jsonify(dados)


@app.route('/dados/orientacao', methods=['GET'])
def obter_dados_orientacao():
    angulo = gerar_variacao_angulo()
    delta_t = gerar_variacao_tempo()
    velocidade_angular = calcular_velocidade_angular(angulo, delta_t)
    dados = {
        "variação_angulo": angulo,
        "variação_tempo": delta_t,
        "velocidade_angular": velocidade_angular
    }
    return jsonify(dados)


@app.route('/dados/pressao_atmosferica', methods=['GET'])
def obter_dados_pressao_atmosferica():
    theta = gerar_variacao_angulo()
    delta_t = gerar_variacao_tempo()
    pressao_atmosferica = calcular_pressao_atmosferica(theta, delta_t)
    dados = {
        "variação_theta": theta,
        "variação_tempo": delta_t,
        "pressao_atmosferica": pressao_atmosferica
    }
    return jsonify(dados)


@app.route('/dados/temperatura', methods=['GET'])
def obter_dados_temperatura():
    tc = random.uniform(-20, 40)
    temperatura_kelvin = calcular_temperatura(tc)
    dados = {
        "temperatura_celsius": tc,
        "temperatura_kelvin": temperatura_kelvin
    }
    return jsonify(dados)


@app.route('/dados/vibracao', methods=['GET'])
def obter_dados_vibracao():
    lambda_valor = gerar_lambda()
    frequencia_valor = gerar_frequencia()
    velocidade_vibracao = calcular_velocidade_vibracao(lambda_valor, frequencia_valor)
    periodo = calcular_periodo(frequencia_valor)
    dados = {
        "lambda": lambda_valor,
        "frequencia": frequencia_valor,
        "velocidade_vibracao": velocidade_vibracao,
        "periodo": periodo
    }
    return jsonify(dados)


if __name__ == "__main__":
    app.run(debug=True)
