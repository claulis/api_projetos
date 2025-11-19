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

### API de Gerenciamento de Projetos, Tarefas e Responsáveis  
**Base URL (dev):** `http://127.0.0.1:8000/api/`  
**Django 5.2 + DRF 3.16**  
**Permissões atuais:** `AllowAny` (aberta para testes)

> Rode o servidor com:  
> ```bash
> poetry run python manage.py runserver
> ```

---

### 1. Responsáveis (/responsaveis/)

| Método | Endpoint                     | Descrição                        | Campos obrigatórios          |
|--------|------------------------------|----------------------------------|------------------------------|
| GET    | `/api/responsaveis/`         | Lista todos os responsáveis      | -                            |
| GET    | `/api/responsaveis/{id}/`    | Detalhe de um responsável        | -                            |
| POST   | `/api/responsaveis/`         | Cria novo responsável            | `nome`, `email`              |
| PUT    | `/api/responsaveis/{id}/`    | Atualiza todos os campos         | `nome`, `email`              |
| PATCH  | `/api/responsaveis/{id}/`    | Atualiza campos parciais         | -                            |
| DELETE | `/api/responsaveis/{id}/`    | Remove responsável               | -                            |

**Exemplo de body (POST/PUT):**
```json
{
  "nome": "Maria Silva",
  "email": "maria@empresa.com",
  "telefone": "(11) 98765-4321"
}
```

---

### 2. Projetos (/projetos/)

| Método | Endpoint                  | Descrição                     | Campos obrigatórios |
|--------|---------------------------|-------------------------------|---------------------|
| GET    | `/api/projetos/`          | Lista todos os projetos       | -                   |
| GET    | `/api/projetos/{id}/`     | Detalhe do projeto + tarefas  | -                   |
| POST   | `/api/projetos/`          | Cria novo projeto             | `nome`              |
| PUT    | `/api/projetos/{id}/`     | Atualiza projeto              | `nome`              |
| PATCH  | `/api/projetos/{id}/`     | Atualiza parcial              | -                   |
| DELETE | `/api/projetos/{id}/`     | Remove projeto (cascade)      | -                   |

**Exemplo de criação:**
```json
{
  "nome": "Sistema de RH",
  "descricao": "Novo sistema interno de recursos humanos",
  "ativo": true
}
```

**Resposta com tarefas aninhadas (GET detalhe):**
```json
{
  "id": 1,
  "nome": "Sistema de RH",
  "descricao": "...",
  "data_criacao": "2025-11-19T10:00:00Z",
  "ativo": true,
  "tarefas": [
    {
      "id": 3,
      "titulo": "Criar models",
      "status": "concluida",
      ...
    }
  ]
}
```

---

### 3. Tarefas (/tarefas/)

| Método | Endpoint                | Descrição                  | Campos obrigatórios          |
|--------|-------------------------|----------------------------|------------------------------|
| GET    | `/api/tarefas/`         | Lista todas as tarefas     | -                            |
| GET    | `/api/tarefas/{id}/`    | Detalhe da tarefa          | -                            |
| POST   | `/api/tarefas/`         | Cria nova tarefa           | `titulo`, `projeto`          |
| PUT    | `/api/tarefas/{id}/`    | Atualiza tarefa completa   | `titulo`, `projeto`          |
| PATCH  | `/api/tarefas/{id}/`    | Atualiza parcial           | -                            |
| DELETE | `/api/tarefas/{id}/`    | Remove tarefa              | -                            |

**Exemplo de body (POST):**
```json
{
  "titulo": "Implementar autenticação JWT",
  "descricao": "Usar djangorestframework-simplejwt",
  "projeto": 1,
  "responsavel": 2,
  "status": "em_andamento"
}
```

> **Importante:**  
> - `projeto` → ID do projeto (ex: 1)  
> - `responsavel` → ID do responsável (pode ser omitido ou null)

**Status possíveis:**
```json
"pendente" | "em_andamento" | "concluida"
```

---

### Fluxo típico de testes (passo a passo)

```bash
# 1. Criar responsável
POST   http://127.0.0.1:8000/api/responsaveis/
→ pega o id retornado (ex: 1)

# 2. Criar projeto
POST   http://127.0.0.1:8000/api/projetos/
→ pega o id (ex: 1)

# 3. Criar tarefas
POST   http://127.0.0.1:8000/api/tarefas/
{
  "titulo": "Criar banco de dados",
  "projeto": 1,
  "responsavel": 1,
  "status": "concluida"
}

# 4. Listar projeto com tarefas aninhadas
GET    http://127.0.0.1:8000/api/projetos/1/
```

---

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


