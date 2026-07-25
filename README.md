# 🎬 Catálogo de Filmes

Aplicação web para gerenciamento de um catálogo pessoal de filmes, desenvolvida com **Python**, **Streamlit** e **SQLite**.

O sistema permite cadastrar, consultar, pesquisar, editar e excluir filmes, além de acompanhar quais títulos já foram assistidos e suas respectivas avaliações.

## 📋 Funcionalidades

- Cadastro de filmes
- Listagem completa do catálogo
- Pesquisa por título ou gênero
- Registro do ano de lançamento
- Registro do gênero
- Avaliação de 0 a 10
- Controle de filmes assistidos e pendentes
- Edição das informações cadastradas
- Exclusão de filmes com confirmação
- Indicadores de quantidade de filmes
- Cálculo da média das avaliações
- Persistência de dados com SQLite
- Geração automática do banco de dados
- Carregamento de dados de demonstração
- Testes automatizados com Pytest

## 📊 Indicadores exibidos

A página principal apresenta os seguintes indicadores:

- Total de filmes cadastrados
- Total de filmes assistidos
- Total de filmes pendentes
- Média das avaliações registradas

## 🛠️ Tecnologias utilizadas

- Python 3.11
- Streamlit
- SQLite
- Pandas
- Pytest
- Git
- GitHub

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
| `app.py` | Interface web desenvolvida com Streamlit |
| `database.py` | Funções de conexão e manipulação do banco SQLite |
| `seed_database.py` | Script para inserir filmes de demonstração |
| `requirements.txt` | Dependências necessárias para executar o projeto |
| `.gitignore` | Arquivos e pastas que não devem ser enviados ao GitHub |
| `tests/test_database.py` | Testes automatizados das operações do banco |

## 🚀 Como executar o projeto

### 1. Clonar o repositório

Após a publicação no GitHub, utilize:

```bash
git clone https://github.com/GabrielABRP98/catalogo-filmes.git
```

Entre na pasta do projeto:

```bash
cd catalogo-filmes
```

Enquanto o repositório ainda não estiver publicado, basta abrir a pasta local do projeto no VS Code.

### 2. Criar o ambiente virtual

No terminal, execute:

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

### 5. Carregar os dados de demonstração

O projeto possui um script com 30 filmes para demonstrar o funcionamento do sistema.

Execute:

```bash
python seed_database.py
```

Resultado esperado:

```text
Filmes adicionados: 30
Filmes já existentes: 0
Total no catálogo: 30
```

O script pode ser executado novamente sem duplicar os mesmos filmes. Os registros já existentes são identificados pelo título e pelo ano de lançamento.

### 6. Executar a aplicação

```bash
python -m streamlit run app.py
```

Depois, acesse no navegador:

```text
http://localhost:8501
```

Para encerrar a aplicação, pressione `Ctrl + C` no terminal.

## 🗄️ Banco de dados

O projeto utiliza SQLite para armazenar os dados localmente.

O arquivo do banco é criado automaticamente com o nome:

```text
catalogo_filmes.db
```

A tabela principal possui os seguintes campos:

| Campo | Descrição |
|---|---|
| `id` | Identificador único do filme |
| `titulo` | Título do filme |
| `ano` | Ano de lançamento |
| `genero` | Gênero do filme |
| `nota` | Avaliação entre 0 e 10 |
| `assistido` | Indica se o filme foi assistido |
| `criado_em` | Data e hora do cadastro |

O arquivo `catalogo_filmes.db` não é enviado ao GitHub, pois está incluído no `.gitignore`.

Cada pessoa que executar o projeto poderá gerar seu próprio banco local.

## 🧪 Testes automatizados

Os testes verificam as principais operações do banco de dados:

- Cadastro de filmes
- Listagem de filmes
- Pesquisa por identificador
- Pesquisa por título ou gênero
- Atualização de registros
- Exclusão de registros
- Validação de título obrigatório
- Validação de notas entre 0 e 10

Para executar os testes:

```bash
python -m pytest -v
```

Resultado esperado:

```text
7 passed
```

Os testes utilizam bancos temporários e não alteram o banco principal da aplicação.

## 🔒 Validações implementadas

O sistema possui validações para impedir:

- Cadastro de filmes sem título
- Cadastro de anos anteriores a 1888
- Cadastro de anos posteriores a 2100
- Cadastro de notas menores que 0
- Cadastro de notas maiores que 10
- Valores inválidos no campo de filme assistido
- Comandos SQL inseridos diretamente pelos usuários

As operações no banco utilizam consultas parametrizadas para reduzir riscos de injeção de SQL.

## 💻 Operações disponíveis

### Cadastrar

Permite registrar:

- Título
- Ano de lançamento
- Gênero
- Nota opcional
- Situação de assistido

### Consultar

Exibe os filmes cadastrados em uma tabela organizada.

### Pesquisar

Permite pesquisar filmes pelo título ou pelo gênero.

### Editar

Permite alterar os dados de um filme já cadastrado.

### Excluir

Permite remover um filme após uma confirmação do usuário.

## 🌱 Dados de demonstração

O arquivo `seed_database.py` contém uma seleção de 30 filmes de diferentes gêneros e períodos.

Ele foi criado para:

- Demonstrar o funcionamento do sistema
- Preencher os indicadores da página inicial
- Testar a ferramenta de pesquisa
- Testar filmes assistidos e pendentes
- Apresentar o projeto em um portfólio

## 📌 Possíveis melhorias futuras

- Filtro por ano de lançamento
- Filtro por situação de assistido
- Ordenação por título, ano ou nota
- Cadastro de diretor
- Cadastro de sinopse
- Inclusão de imagens e pôsteres
- Integração com uma API pública de filmes
- Sistema de usuários
- Exportação do catálogo para CSV
- Gráficos por gênero e avaliação
- Hospedagem da aplicação
- Banco de dados PostgreSQL para produção

## 🎯 Objetivo do projeto

Este projeto foi desenvolvido para praticar e demonstrar conhecimentos em:

- Desenvolvimento com Python
- Criação de interfaces web
- Manipulação de bancos de dados
- Operações CRUD
- Validação de dados
- Organização de código
- Testes automatizados
- Controle de versão com Git
- Documentação de projetos

## 👤 Autor

**Gabriel Peixoto**

GitHub: `GabrielABRP98`