# Petstore API clone

## Segmentação em um ambiente virtual (opcional):

```
pyenv virtualenv 3.9.2 pets-api
pyenv activate pets-api
```

## Configuração do Projeto

```sh
pip install -r requirements-dev.txt
export SQLALCHEMY_DATABASE_URL=postgresql://dssseuhz:XkETRS4ZdJDT6cc1sZOI8VwaxkrqgdSr@tuffi.db.elephantsql.com:5432/dssseuhz
```
## Execução do Projeto

```
make run
```