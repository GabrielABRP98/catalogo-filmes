# 🎬 Catálogo de Filmes

Aplicação web para gerenciamento de um catálogo pessoal de filmes, desenvolvida com **Python**, **Streamlit** e **SQLite**.

O sistema permite cadastrar, consultar, pesquisar, editar e excluir filmes, além de controlar quais títulos já foram assistidos e registrar avaliações de 0 a 10.

## 🌐 Demonstração online

A aplicação está publicada no Streamlit Community Cloud:

[**Acessar o Catálogo de Filmes**](https://catalogo-filmes-gabriel.streamlit.app)

> A versão online utiliza um banco SQLite local. Como o armazenamento do Streamlit Community Cloud pode ser reiniciado, alterações realizadas online podem não permanecer definitivamente.

## 📋 Funcionalidades

- Cadastro de filmes
- Listagem completa do catálogo
- Pesquisa por título ou gênero
- Registro do ano de lançamento
- Registro do gênero
- Avaliação opcional de 0 a 10
- Controle de filmes assistidos e pendentes
- Edição de informações
- Exclusão com confirmação
- Indicadores do catálogo
- Cálculo da média das avaliações
- Persistência local com SQLite
- Carregamento automático de dados demonstrativos
- Testes automatizados do banco de dados

## 📊 Indicadores

A página principal apresenta:

- Total de filmes cadastrados
- Total de filmes assistidos
- Total de filmes pendentes
- Média das avaliações registradas

## 🛠️ Tecnologias utilizadas

- Python 3.11
- Streamlit
- SQLite
- Pandas
- pytest
- Git
- GitHub
- Streamlit Community Cloud

## 📁 Estrutura do projeto

```text
catalogo-filmes/
├── app.py
├── database.py
├── seed_database.py
├── requirements.txt
├── README.md
├── .gitignore
└── tests/
    └── test_database.py
```

### Descrição dos arquivos

| Arquivo | Descrição |
|---|---|
| `app.py` | Interface web e fluxo principal da aplicação |
| `database.py` | Conexão com o SQLite e operações CRUD |
| `seed_database.py` | Inserção dos 30 filmes demonstrativos |
| `requirements.txt` | Dependências do projeto |
| `.gitignore` | Arquivos que não devem ser versionados |
| `tests/test_database.py` | Testes automatizados das operações do banco |

## 🚀 Como executar localmente

### 1. Clonar o repositório

```bash
git clone https://github.com/GabrielABRP98/catalogo-filmes.git
```

Entre na pasta:

```bash
cd catalogo-filmes
```

### 2. Criar o ambiente virtual

```bash
python -m venv .venv
```

### 3. Ativar o ambiente virtual

No Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

No Prompt de Comando do Windows:

```cmd
.venv\Scripts\activate.bat
```

No Linux ou macOS:

```bash
source .venv/bin/activate
```

Quando o ambiente estiver ativo, o terminal mostrará:

```text
(.venv)
```

### 4. Instalar as dependências

```bash
python -m pip install -r requirements.txt
```

### 5. Executar a aplicação

```bash
python -m streamlit run app.py
```

Acesse no navegador:

```text
http://localhost:8501
```

Para encerrar a aplicação, pressione `Ctrl + C` no terminal.

## 🌱 Dados de demonstração

Quando a aplicação encontra o banco vazio, os 30 filmes demonstrativos são carregados automaticamente.

Também é possível executar o script manualmente:

```bash
python seed_database.py
```

Resultado esperado na primeira execução:

```text
Filmes adicionados: 30
Filmes já existentes: 0
Total no catálogo: 30
```

O script identifica filmes existentes pelo título e pelo ano, evitando que os mesmos registros sejam inseridos novamente.

## 🗄️ Banco de dados

O projeto utiliza SQLite para armazenar os dados.

O arquivo é criado automaticamente com o nome:

```text
catalogo_filmes.db
```

### Estrutura da tabela `filmes`

| Campo | Descrição |
|---|---|
| `id` | Identificador único do filme |
| `titulo` | Título do filme |
| `ano` | Ano de lançamento |
| `genero` | Gênero do filme |
| `nota` | Avaliação opcional entre 0 e 10 |
| `assistido` | Indica se o filme foi assistido |
| `criado_em` | Data e hora do cadastro |

O arquivo `catalogo_filmes.db` está incluído no `.gitignore` e não é enviado ao GitHub.

Cada instalação local gera seu próprio banco de dados.

## 💻 Operações disponíveis

### Cadastrar

Permite registrar:

- Título
- Ano de lançamento
- Gênero
- Nota opcional
- Situação de assistido

### Consultar

Apresenta os filmes cadastrados em uma tabela organizada.

### Pesquisar

Filtra os registros pelo título ou gênero.

### Editar

Permite alterar as informações de um filme existente.

### Excluir

Remove um filme após a confirmação do usuário.

## 🔒 Validações implementadas

O sistema impede:

- Cadastro sem título
- Ano anterior a 1888
- Ano posterior a 2100
- Nota menor que 0
- Nota maior que 10
- Valor inválido no campo de situação do filme

As operações utilizam consultas SQL parametrizadas, evitando a inserção direta dos valores do usuário nos comandos SQL.

## 🧪 Testes automatizados

Os testes verificam:

- Cadastro de filmes
- Listagem de filmes
- Busca por identificador
- Pesquisa por título ou gênero
- Atualização de registros
- Exclusão de registros
- Validação de título obrigatório
- Validação de notas

Execute:

```bash
python -m pytest -v
```

Resultado esperado:

```text
7 passed
```

Os testes utilizam bancos temporários e não alteram o banco principal da aplicação.

## 📌 Melhorias futuras

- Filtros por ano e situação
- Ordenação por título, ano ou nota
- Cadastro de diretor
- Cadastro de sinopse
- Inclusão de pôsteres
- Integração com uma API de filmes
- Exportação do catálogo para CSV
- Gráficos por gênero e avaliação
- Autenticação de usuários
- Banco PostgreSQL para persistência em produção
- Interface responsiva aprimorada

## 🎯 Objetivo do projeto

O projeto foi desenvolvido para praticar e demonstrar conhecimentos em:

- Desenvolvimento com Python
- Criação de interfaces web
- Operações CRUD
- Manipulação de bancos de dados
- Validação de dados
- Consultas SQL parametrizadas
- Organização e separação de responsabilidades
- Testes automatizados
- Controle de versão com Git
- Documentação técnica
- Publicação de aplicações web

## 👤 Autor

**Gabriel Peixoto**

- GitHub: [GabrielABRP98](https://github.com/GabrielABRP98)
- Aplicação: [Catálogo de Filmes](https://catalogo-filmes-gabriel.streamlit.app)