import requests

# URL da rota de velocidade
url_velocidade = 'http://127.0.0.1:5000/dados/velocidade'

# Fazendo a solicitação GET para obter a velocidade
response_velocidade = requests.get(url_velocidade)

# Verificando se a solicitação foi bem-sucedida
if response_velocidade.status_code == 200:
    dados_velocidade = response_velocidade.json()
    print("Velocidade:", dados_velocidade["velocidade"])
else:
    print("Erro ao obter a velocidade:", response_velocidade.status_code)

# URL da rota de aceleração
url_aceleracao = 'http://127.0.0.1:5000/dados/aceleracao'

# Fazendo a solicitação GET para obter os dados de aceleração
response_aceleracao = requests.get(url_aceleracao)

# Verificando se a solicitação foi bem-sucedida
if response_aceleracao.status_code == 200:
    dados_aceleracao = response_aceleracao.json()
    print("Variação de velocidade:", dados_aceleracao["variação_velocidade"])
    print("Variação de tempo:", dados_aceleracao["variação_tempo"])
    print("Aceleração:", dados_aceleracao["aceleracao"])
else:
    print("Erro ao obter os dados de aceleração:", response_aceleracao.status_code)
