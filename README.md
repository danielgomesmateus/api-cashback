# api-cashback

API desenvolvida com Django Rest, MYSQL e Docker.

## Instalação

Primeiro passo é criar uma virtualenv

```bash
virtualenv venv
```

Utilize [pip](https://pip.pypa.io/en/stable/) para instalar as dependências do projeto.

```bash
pip install -r requirements.txt
```

Para realizar os testes, utilize a [url](https://www.postman.com/collections/908cb86663db99f28d0c) com os dados da colection no Postman

## Como usar

```
# Utilize o comando abaixo para subir uma base de dados mysql
docker-compose up -d --build

# Utilize o comando abaixo para iniciar o projeto
python3 manage.py runserver

# Utilize o comando abaixo para iniciar os testes
python3 manage.py test --settings=cashback.tests_settings
```

## Documentação

Para ter acesso a documentação, basta utilizar o endereço abaixo, após ter iniciado os passos anteriores.

```
http://localhost:8000/v1/docs/
```