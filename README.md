# My Python Project

This is a Python project that contains the following files:

- `src/main.py`: This file is the main entry point of the Python project. It contains the code for the main functionality of the project.

- `.env`: This file is an environment file. It is used to store environment variables for the project, such as API keys or database connection strings.


## Ideia

Gerar uma interface para o usuário interagir com uma base de dados informada onde será possível usar linguagem natural para realizar consultas além de gerar gráficos e relatórios.
Uma segunda etapa seria permitir usar os outputs gerados para alimentar um software de BI como o PowerBI ou o Weknow.


### Workflow

1. Usuário informa a base(s) de dados e tabela(s) (que podem estar previamente cadastrados)
2. Usuário digita o que ele quer extrair dos dados, em gráfico, relatório ou uma resposta em texto
3. O sistema irá extrair todos os dados necessários e indexar usando o LlamaIndex ou ferramenta similar
4. Após indexar, o sistema irá enviar os dados indexados ao LLM juntamente com a query do usuário e receber a resposta

### Problemas do Workflow

- Indexar os dados pode ser um processo demorado
- A indexação pode ser custosa em termos de recursos
- A indexação pode ser custosa em termos de espaço (verificar o tamanho)
- A indexação no workflow atual não é armazenada para consultas futuras
- Como traduzir o retorno em gráfico/relatório para um software de BI?
- Custo do LLM

# Instalação

## Instalação do Python no Windows

Instalação do Python no Windows é um processo simples. Pode ser usada uma das alterantivas a seguir:

- Instalação do Python via site oficial
- Instalação do Python via Winget
- Instalação do Python via WingetUI

## Instalação do Pipenv no Windows

 `pip install --user pipenv`

Depois é necessário adicionar o diretório de instalação do Pipenv ao PATH do Windows e em seguida reiniciar. Por ex.: `C:\Users\username\AppData\Roaming\Python\Python312\Scripts`

## Instalação das dependências

 `pipenv install`



