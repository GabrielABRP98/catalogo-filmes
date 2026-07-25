from database import adicionar_filme, inicializar_banco, listar_filmes


FILMES_EXEMPLO = [
    {
        "titulo": "Interestelar",
        "ano": 2014,
        "genero": "Ficção científica",
        "nota": 9.5,
        "assistido": True,
    },
    {
        "titulo": "O Poderoso Chefão",
        "ano": 1972,
        "genero": "Crime e drama",
        "nota": 9.8,
        "assistido": True,
    },
    {
        "titulo": "Matrix",
        "ano": 1999,
        "genero": "Ficção científica e ação",
        "nota": 9.3,
        "assistido": True,
    },
    {
        "titulo": "Parasita",
        "ano": 2019,
        "genero": "Suspense e drama",
        "nota": 9.4,
        "assistido": True,
    },
    {
        "titulo": "A Viagem de Chihiro",
        "ano": 2001,
        "genero": "Animação e fantasia",
        "nota": 9.2,
        "assistido": True,
    },
    {
        "titulo": "O Senhor dos Anéis: A Sociedade do Anel",
        "ano": 2001,
        "genero": "Fantasia e aventura",
        "nota": 9.5,
        "assistido": True,
    },
    {
        "titulo": "O Senhor dos Anéis: As Duas Torres",
        "ano": 2002,
        "genero": "Fantasia e aventura",
        "nota": 9.6,
        "assistido": True,
    },
    {
        "titulo": "O Senhor dos Anéis: O Retorno do Rei",
        "ano": 2003,
        "genero": "Fantasia e aventura",
        "nota": 9.8,
        "assistido": True,
    },
    {
        "titulo": "Pulp Fiction",
        "ano": 1994,
        "genero": "Crime e drama",
        "nota": 9.1,
        "assistido": True,
    },
    {
        "titulo": "Clube da Luta",
        "ano": 1999,
        "genero": "Drama",
        "nota": 9.0,
        "assistido": True,
    },
    {
        "titulo": "Cidade de Deus",
        "ano": 2002,
        "genero": "Crime e drama",
        "nota": 9.5,
        "assistido": True,
    },
    {
        "titulo": "Central do Brasil",
        "ano": 1998,
        "genero": "Drama",
        "nota": 9.0,
        "assistido": True,
    },
    {
        "titulo": "Bacurau",
        "ano": 2019,
        "genero": "Drama e ficção científica",
        "nota": 8.5,
        "assistido": True,
    },
    {
        "titulo": "Tropa de Elite",
        "ano": 2007,
        "genero": "Ação e crime",
        "nota": 8.8,
        "assistido": True,
    },
    {
        "titulo": "O Auto da Compadecida",
        "ano": 2000,
        "genero": "Comédia",
        "nota": 9.4,
        "assistido": True,
    },
    {
        "titulo": "Mad Max: Estrada da Fúria",
        "ano": 2015,
        "genero": "Ação e aventura",
        "nota": 9.0,
        "assistido": True,
    },
    {
        "titulo": "Blade Runner 2049",
        "ano": 2017,
        "genero": "Ficção científica",
        "nota": 9.1,
        "assistido": True,
    },
    {
        "titulo": "Alien, o Oitavo Passageiro",
        "ano": 1979,
        "genero": "Terror e ficção científica",
        "nota": 9.2,
        "assistido": True,
    },
    {
        "titulo": "O Iluminado",
        "ano": 1980,
        "genero": "Terror",
        "nota": 9.0,
        "assistido": True,
    },
    {
        "titulo": "Corra!",
        "ano": 2017,
        "genero": "Terror e suspense",
        "nota": 8.8,
        "assistido": True,
    },
    {
        "titulo": "Whiplash: Em Busca da Perfeição",
        "ano": 2014,
        "genero": "Drama e música",
        "nota": None,
        "assistido": False,
    },
    {
        "titulo": "La La Land",
        "ano": 2016,
        "genero": "Musical e romance",
        "nota": None,
        "assistido": False,
    },
    {
        "titulo": "A Origem",
        "ano": 2010,
        "genero": "Ficção científica e suspense",
        "nota": None,
        "assistido": False,
    },
    {
        "titulo": "Duna: Parte Dois",
        "ano": 2024,
        "genero": "Ficção científica e aventura",
        "nota": None,
        "assistido": False,
    },
    {
        "titulo": "Tudo em Todo Lugar ao Mesmo Tempo",
        "ano": 2022,
        "genero": "Ficção científica e comédia",
        "nota": None,
        "assistido": False,
    },
    {
        "titulo": "Homem-Aranha no Aranhaverso",
        "ano": 2018,
        "genero": "Animação e ação",
        "nota": None,
        "assistido": False,
    },
    {
        "titulo": "Toy Story",
        "ano": 1995,
        "genero": "Animação e aventura",
        "nota": None,
        "assistido": False,
    },
    {
        "titulo": "O Labirinto do Fauno",
        "ano": 2006,
        "genero": "Fantasia e drama",
        "nota": None,
        "assistido": False,
    },
    {
        "titulo": "Oldboy",
        "ano": 2003,
        "genero": "Suspense e ação",
        "nota": None,
        "assistido": False,
    },
    {
        "titulo": "Os Sete Samurais",
        "ano": 1954,
        "genero": "Drama e ação",
        "nota": None,
        "assistido": False,
    },
]


def popular_banco() -> None:
    """Adiciona filmes demonstrativos sem duplicar registros."""

    inicializar_banco()

    filmes_existentes = listar_filmes()

    chaves_existentes = {
        (filme["titulo"].casefold(), filme["ano"])
        for filme in filmes_existentes
    }

    inseridos = 0
    ignorados = 0

    for filme in FILMES_EXEMPLO:
        chave = (
            filme["titulo"].casefold(),
            filme["ano"],
        )

        if chave in chaves_existentes:
            ignorados += 1
            continue

        adicionar_filme(**filme)
        chaves_existentes.add(chave)
        inseridos += 1

    print(f"Filmes adicionados: {inseridos}")
    print(f"Filmes já existentes: {ignorados}")
    print(f"Total no catálogo: {len(listar_filmes())}")


if __name__ == "__main__":
    popular_banco()