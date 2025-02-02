# Indicium Tech Code Challenge
- Meu projeto foi desenvolvido com a extensão Subsistema do Windows para Linux (WSL) do Visual Studio Code.

## Pré-requisitos
É necessário que esteja instalado:
- [Python 3.12](https://www.python.org/downloads/)
- [Pandas](https://pandas.pydata.org/docs/getting_started/install.html)
- [Docker](https://docs.docker.com/desktop/setup/install/windows-install/)

## Inicializar o docker
Abra o programa Docker Desktop.
No diretório `code-challenge`, inicializar o docker com o comando:
```
docker compose up -d
```

## Meltano
- Criação do ambiente virtual para o Meltano:
```
python3 -m venv venv
```
- Instalação do Meltano:
```
pip install meltano
```
- Inicialização do Meltano:
```
meltano init desafio_indicium
```

## Airflow
- Criação do ambiente virtual para o Airflow:
```
python -m venv airflow_env
```
- Entrar no ambiente virtual:
```
source airflow_env/bin/activate
```
- Instalação do Airflow com suporte a PostgreSQL:
```
pip install apache-airflow[postgres]
```
- Inicialização do banco de dados:
```
airflow db init
```
- Criação de usuário:
```
airflow users create \
--username <seu-nome-de-usuario> \
--firstname <seu-primeiro-nome> \
--lastname <seu-sobrenome> \
--role Admin \
--email <seu-email>
```
- Inicializar Airflow:
> Inicializar o web server e o scheduler em terminais diferentes:

**Terminal 1:**
```
airflow webserver --port 8080
```
**Terminal 2:**
```
airflow scheduler
```


## Airflow DAGs
- Acessar a interface WEB:
Abra um navegador e vá para:
```
http://localhost:8080
```
Faça o login com o usuário criado anteriormente.
Procure por `desafio_indicium` e ligue a DAG.

### Observações finais
Meu projeto não foi concluído completamente, acredito que não deva rodar em outras máquinas, uma vez que não consegui implementar a tempo, maneiras de rodar em diretórios diferentes dos que eu estava trabalhando.<br>
Iniciei este desafio com pouco conhecimento ou experiência com os assuntos requeridos para a realização do mesmo, dei meu máximo para aprender todo o necessário nesses 7 dias, porém acabei não conseguindo finalizar o projeto.<br>
Consegui fazer ele funcionar, mas faltou ajustes finais para que a execução não dependesse do meu caminho de arquivos e fosse possível rodá-lo em qualquer máquina.<br>
No mais foi bastante desafiador para mim e uma ótima oportunidade de aprendizado, é muito gratificante chegar no ponto onde algo que inicialmente parecia complexo e intimidador, passa a fazer sentido e parecer muito mais manejável.
