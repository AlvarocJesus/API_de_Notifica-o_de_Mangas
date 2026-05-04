# MangaTracker

Sistema em Python para acompanhar mangas/animes, coletar atualizacoes via scraping e notificar usuarios (Telegram), com base para API e interface desktop.

![Python](https://img.shields.io/badge/Python-3.14%2B-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-API-009688?logo=fastapi&logoColor=white)
![Status](https://img.shields.io/badge/Status-Em%20Evolucao-orange)
![License](https://img.shields.io/badge/License-MIT-green)

## Visao geral

O projeto foi organizado para separar claramente regras de negocio, infraestrutura e interfaces:

- Scrapers por fonte em src/infra/scrap
- Persistencia via SQLAlchemy em src/infra/db
- Notificacoes Telegram em src/config/notify
- API HTTP com FastAPI em src/interfaces/api
- App desktop com Tkinter em src/interfaces/desktop

## Funcionalidades

| Modulo | O que faz | Status atual |
|---|---|---|
| API | Endpoints basicos para leitura e escrita de mangas | Funcional (base) |
| Scraping | Coleta dados de diferentes fontes | Parcial (em ajuste) |
| Banco de dados | Insercao e atualizacao de entidades de manga | Parcial (em evolucao) |
| Notificacao | Envio de mensagens via bot Telegram | Funcional |
| Desktop | Tela inicial e fluxos iniciais de cadastro/listagem | Inicial |

## Stack tecnica

- Python 3.14+
- FastAPI + Uvicorn
- Requests + BeautifulSoup4
- SQLAlchemy + psycopg2 (via URL de conexao)
- Loguru
- Pandas
- Unidecode
- Tkinter

Dependencias em pyproject.toml.

## Estrutura do repositorio

```text
src/
  config/
    log/            # configuracao de logs
    notify/         # notificacao via Telegram
  infra/
    db/             # camada de acesso ao banco
    scrap/          # scrapers por site/fonte
  interfaces/
    api/            # FastAPI
    desktop/        # Tkinter
    web/            # base web (inicial)
```

## Requisitos

- Python 3.14 ou superior
- Ambiente virtual Python
- Banco Postgres acessivel (para funcionalidades de DB)
- Token do bot Telegram (para notificacoes)

## Quick Start

### 1. Criar ambiente e instalar dependencias

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .
```

### 2. Configurar variaveis de ambiente

Crie o arquivo .env na raiz:

```env
DATABASE_URL=postgresql+psycopg2://usuario:senha@host:5432/banco
TELEGRAM_API_KEY=seu_token_do_bot
```

### 3. Subir API

```bash
uvicorn src.interfaces.api.api:app --reload
```

API local: http://127.0.0.1:8000
Docs interativa: http://127.0.0.1:8000/docs

## Endpoints atuais

- GET /
- GET /mangas
- POST /mangas

## Executando outros modulos

### Interface desktop

```bash
PYTHONPATH=src python src/interfaces/desktop/main.py
```

### Exemplo de scraper (SussyToons)

```bash
PYTHONPATH=src python -c "from infra.scrap.SussyToons import SussyToons; SussyToons().run('https://api-dev.sussytoons.site/obras/847')"
```

Observacao: alguns scrapers ainda exigem ajustes de URL/entrada antes do run.

## Configuracoes importantes

- Notificacao Telegram: src/config/notify/Notify.py
- Banco de dados: src/infra/db/database.py
- Log da aplicacao: src/config/log/log.py
- API FastAPI: src/interfaces/api/api.py

## Qualidade e proximos passos

Backlog tecnico prioritario:

- padronizar tratamento de erros
- ampliar cobertura de testes
- evoluir endpoints (detalhe, update, delete)
- revisar fluxos de DB e validacoes de entrada
- estabilizar scrapers por fonte

Planejamento detalhado: cronograma.md

## Contribuicao

1. Faça um fork do projeto.
2. Crie uma branch para sua feature.
3. Commit suas alteracoes.
4. Envie para seu fork.
5. Abra um Pull Request.

## Licenca

Distribuido sob licenca MIT.
