# API de Dados em Tempo Real

Este aplicativo Flask serve como uma API de dados em tempo real, fornecendo vários endpoints para obter dados simulados relacionados à velocidade, aceleração, orientação, pressão atmosférica, temperatura e vibração. Os dados são gerados aleatoriamente dentro de intervalos especificados para fins de demonstração.

## Instalação

Para executar o aplicativo, siga estas etapas:

1. Clone o repositório:

    git clone https://github.com/seu-nome-de-usuario/api-dados-tempo-real.git

2. Navegue até o diretório do projeto:

    cd api-dados-tempo-real
   

3. Instale as dependências necessárias:

  
    pip install -r requirements.txt


## Uso

Inicie o servidor Flask executando o seguinte comando:

python dados.py

## Endpoints

/dados/velocidade: Obtenha dados simulados de velocidade.
/dados/aceleracao: Obtenha dados simulados de aceleração.
/dados/orientacao: Obtenha dados simulados de orientação.
/dados/pressao_atmosferica: Obtenha dados simulados de pressão atmosférica.
/dados/temperatura: Obtenha dados simulados de temperatura.
/dados/vibracao: Obtenha dados simulados de vibração.

Obter dados de velocidade
http://localhost:5000/dados/velocidade

Obter dados de aceleração
http://localhost:5000/dados/aceleracao

Obter dados de orientação
http://localhost:5000/dados/orientacao

Obter dados de pressão atmosférica
http://localhost:5000/dados/pressao_atmosferica

Obter dados de temperatura
http://localhost:5000/dados/temperatura

Obter dados de vibração
http://localhost:5000/dados/vibracao
