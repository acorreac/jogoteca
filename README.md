# Jogoteca

Webapp com Python e Flask.

## Objetivo

Desenvolver um sistema para Internet que sirva como uma página de cadastro de jogos.

## Tecnologias

![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

## Como executar o projeto
<h3>Para executar o projeto é necessário ter instalado em seu computador o Pyhton 3 e um sistema de gerenciamento de dados(Mysql, MariaDB etc)</h3>

> Python 3.10 - https://www.python.org/ <br>

<h3>Após instalado deverá clonar o repositório</h3>

> https://github.com/acorreac/jogoteca.git
<br>

<h3>Se seu sistema operacional for Windows</h3>
<br>

![Windows](https://img.shields.io/badge/Windows-017AD7?style=for-the-badge&logo=windows&logoColor=white)

<h3>Deverá abrir o CMD e com o comando CD navegar até a pasta onde o repositório foi clonado e executar o seguinte comando para criar o ambiente virtual:</h3>

```python
	python -m venv env
```

```python
	venv\Scripts\Activate.ps1
```

<h3>Em seguida deverá instalar as bibliotecas necessárias do projeto, contidas no arquivo requirements.txt, com comando a baixo:</h3>

```python
	pip install -r requirements.txt
```

<h3>É necessário rodar o comando abaixo para criar o banco de dados do projeto na máquina local:</h3>

```python
  python3 prepara_banco.py
```

<h3>Após instalado corretamente, executar a aplicação através do comando:</h3>

```python
	flask run
```

<h3>Se seu sistema operacional for Linux</h3>
<br> 

![Linux](https://img.shields.io/badge/Linux-E34F26?style=for-the-badge&logo=linux&logoColor=black)

<h3>Deverá abrir o terminal e com o comando CD navegar até a pasta onde o repositório foi clonado e executar o seguinte comando para criar o ambiente virtual:</h3>

```python
	python3 -m venv env
```

```python
	source venv/bin/activate
```

<h3>Em seguida deverá instalar as bibliotecas necessárias do projeto, contidas no arquivo requirements.txt, com comando a baixo:</h3>

```python
	pip install -r requirements.txt
```

<h3>É necessário rodar o comando abaixo para criar o banco de dados do projeto na máquina local:</h3>

```python
  python3 prepara_banco.py
```

<h3>Renomear o arquivo de inicialização padrão do flask_app com o comando:</h3>

```python
	export FLASK_APP=jogoteca.py
```

<h3>E ativar o ambiente virtual como development com o comando:</h3>

```python
    export FLASK_ENV=development
```

<h4>E por fim com o comando abaixo inicializar o projeto:</h4>

```python
	flask run
```

<h4>No terminal será mostrado uma mensagem com um link igual a este 'http://127.0.0.1:5000', na qual deverá ser copiado e colado no navegador de sua preferência para visualização da aplicação.</h4>

<h4>FIM</h4>
