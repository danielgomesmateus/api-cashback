# api-cashback

API desenvolvida com Django Rest, MYSQL e Docker.

## Instalação

Primeiro passo é ter instalado o [Docker](https://www.docker.com/). Como ele iremos iniciar a aplicação e base de 
dados do projeto.

## Endpoints da API
Para realizar os testes na API, acesse a [URL](https://www.postman.com/collections/908cb86663db99f28d0c) com os dados 
da colection no Postman.

## Como usar

```
# Utilize o comando abaixo para iniciar o projeto.
docker-compose up -d --build --force-recreate

# Após iniciar o projeto estará disponível na URL abaixo.
http://localhost:8000/
```

## Iniciar testes
```
# É necessário iniciar os testes dentro do container onde está a aplicação.
docker-compose exec -it app bash

python3 manage.py test --settings=cashback.tests_settings
```

## Documentação

Para ter acesso a documentação, basta utilizar o endereço abaixo, após ter iniciado os passos anteriores.

```
http://localhost:8000/v1/docs/
```