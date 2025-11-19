# API Projetos

> Projeto Django + Django REST Framework para gerenciamento de projetos.

[![Django](https://img.shields.io/badge/Django-5.2.8-092E20?style=flat-square&logo=django)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/Django%20REST%20Framework-3.16.1-A30000?style=flat-square&logo=django)](https://www.django-rest-framework.org/)
[![Poetry](https://img.shields.io/badge/Poetry-Latest-60A5FA?style=flat-square&logo=poetry)](https://python-poetry.org/)

---

## Visão Geral

Este repositório contém uma API construída com Django (>=5.2.8) e
Django REST Framework para gerenciar projetos e usa
SQLite por padrão para facilitar o desenvolvimento.

As dependências principais (definidas em `pyproject.toml`) são:

- `django (>=5.2.8,<6.0.0)`
- `djangorestframework (>=3.16.1,<4.0.0)`

## Pré-requisitos

- Python 3.12 ou superior
- Git (para clonar o repositório)
- **Poetry** (gerenciador de dependências)

### Instalar Poetry

Se ainda não tem Poetry instalado, siga a [documentação oficial](https://python-poetry.org/docs/#installation):

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Após instalação, adicione o Poetry ao `PATH`:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Verifique a instalação:

```bash
poetry --version
```

## Instalação com Poetry

1. Clone o projeto

```bash
git clone <URL_DO_REPOSITORIO>
cd api_projetos
```

2. Instalar dependências e criar ambiente virtual

Poetry cria automaticamente um virtualenv e instala todas as dependências:

```bash
poetry install
```

3. Ativar o ambiente virtual (opcional)

O Poetry gerencia o virtualenv automaticamente. Para executar comandos dentro do ambiente:

```bash
poetry run <comando>
```

Ou, para entrar em um shell interativo:

```bash
poetry shell
```

Dentro do shell, você pode rodar comandos normalmente sem o prefixo `poetry run`.

## Configuração do banco de dados

O projeto já vem configurado para usar SQLite (arquivo `db.sqlite3` na raiz).
Para preparar o banco:

```bash
poetry run python manage.py migrate
```

Opcionalmente, criar um usuário administrador:

```bash
poetry run python manage.py createsuperuser
```

Se desejar usar outro banco (Postgres, MySQL, etc.), edite `api_projetos/settings.py`
na seção `DATABASES` e instale o driver apropriado através do Poetry ou manualmente.

## Rodando o servidor

```bash
poetry run python manage.py runserver
```

A API ficará disponível em `http://127.0.0.1:8000/` e os endpoints do app `api`
estão sob `http://127.0.0.1:8000/api/`.

## Endpoints importantes

- `GET /api/projetos/` — listar projetos
- `GET /api/projetos/{id}/` — detalhes de um projeto
- Outros endpoints registrados pelo `DefaultRouter` do DRF no `api/urls.py`.

## Dicas e troubleshooting

### Poetry não encontrado?

Se `poetry` não está no seu `PATH`, reinstale e configure corretamente:

```bash
curl -sSL https://install.python-poetry.org | python3 -
export PATH="$HOME/.local/bin:$PATH"
```

### Problemas ao rodar `poetry install`?

Verifique se a versão do Python está correta (>= 3.12):

```bash
python --version
```

Se precisar usar uma versão específica, configure no `pyproject.toml` ou use:

```bash
poetry env use python3.12
```

### Limpar cache do Poetry

Se enfrentar problemas de dependência, tente:

```bash
poetry cache clear . --all
poetry install
```

### Adicionar novas dependências

Para adicionar uma dependência (ex: `requests`):

```bash
poetry add requests
```

Para remover:

```bash
poetry remove requests
```

## Como contribuir

- Abra uma issue descrevendo o bug ou feature desejada.
- Faça um fork, crie uma branch com o prefixo `feature/` ou `fix/`, implemente e
  envie um pull request apontando para a branch `main` do repositório original.


