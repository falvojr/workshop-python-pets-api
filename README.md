# Petstore API clone

## API de Referência

[Swagger Petstore](https://petstore.swagger.io/#/)

## Passos para execução:

1. Segmentação em um ambiente virtual (opcional):

```
pyenv virtualenv 3.9.2 pets-api
pyenv activate pets-api
```

2. Configurações Essenciais:

```sh
pip install -r requirements-dev.txt
export SQLALCHEMY_DATABASE_URL=postgresql://dssseuhz:XkETRS4ZdJDT6cc1sZOI8VwaxkrqgdSr@tuffi.db.elephantsql.com:5432/dssseuhz
```
3. Execução:

```
make run
```
