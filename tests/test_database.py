import pytest

from database import (
    adicionar_filme,
    atualizar_filme,
    buscar_filme,
    excluir_filme,
    inicializar_banco,
    listar_filmes,
)


@pytest.fixture
def banco_teste(tmp_path):
    """Cria um banco temporário separado para cada teste."""

    caminho = tmp_path / "catalogo_teste.db"
    inicializar_banco(caminho)

    return caminho


def test_adicionar_e_listar_filme(banco_teste):
    filme_id = adicionar_filme(
        titulo="Interestelar",
        ano=2014,
        genero="Ficção científica",
        nota=9.5,
        assistido=True,
        caminho_banco=banco_teste,
    )

    filmes = listar_filmes(caminho_banco=banco_teste)

    assert filme_id > 0
    assert len(filmes) == 1
    assert filmes[0]["titulo"] == "Interestelar"
    assert filmes[0]["ano"] == 2014
    assert filmes[0]["genero"] == "Ficção científica"
    assert filmes[0]["nota"] == 9.5
    assert filmes[0]["assistido"] == 1


def test_buscar_filme_por_id(banco_teste):
    filme_id = adicionar_filme(
        titulo="O Poderoso Chefão",
        ano=1972,
        genero="Drama",
        nota=10,
        caminho_banco=banco_teste,
    )

    filme = buscar_filme(
        filme_id,
        caminho_banco=banco_teste,
    )

    assert filme is not None
    assert filme["id"] == filme_id
    assert filme["titulo"] == "O Poderoso Chefão"


def test_atualizar_filme(banco_teste):
    filme_id = adicionar_filme(
        titulo="Matrix",
        ano=1999,
        genero="Ação",
        nota=8.5,
        caminho_banco=banco_teste,
    )

    atualizado = atualizar_filme(
        filme_id=filme_id,
        titulo="Matrix",
        ano=1999,
        genero="Ficção científica",
        nota=9.0,
        assistido=True,
        caminho_banco=banco_teste,
    )

    filme = buscar_filme(
        filme_id,
        caminho_banco=banco_teste,
    )

    assert atualizado is True
    assert filme is not None
    assert filme["genero"] == "Ficção científica"
    assert filme["nota"] == 9.0
    assert filme["assistido"] == 1


def test_excluir_filme(banco_teste):
    filme_id = adicionar_filme(
        titulo="Parasita",
        ano=2019,
        genero="Suspense",
        nota=9.0,
        caminho_banco=banco_teste,
    )

    excluido = excluir_filme(
        filme_id,
        caminho_banco=banco_teste,
    )

    filme = buscar_filme(
        filme_id,
        caminho_banco=banco_teste,
    )

    assert excluido is True
    assert filme is None
    assert listar_filmes(caminho_banco=banco_teste) == []


def test_filtrar_filmes_por_titulo_ou_genero(banco_teste):
    adicionar_filme(
        "Alien",
        1979,
        "Terror",
        9.0,
        caminho_banco=banco_teste,
    )

    adicionar_filme(
        "Toy Story",
        1995,
        "Animação",
        8.5,
        caminho_banco=banco_teste,
    )

    resultado_titulo = listar_filmes(
        busca="Alien",
        caminho_banco=banco_teste,
    )

    resultado_genero = listar_filmes(
        busca="Animação",
        caminho_banco=banco_teste,
    )

    assert len(resultado_titulo) == 1
    assert resultado_titulo[0]["titulo"] == "Alien"

    assert len(resultado_genero) == 1
    assert resultado_genero[0]["titulo"] == "Toy Story"


def test_impedir_titulo_vazio(banco_teste):
    with pytest.raises(
        ValueError,
        match="O título do filme é obrigatório",
    ):
        adicionar_filme(
            titulo="",
            ano=2020,
            genero="Drama",
            nota=8.0,
            caminho_banco=banco_teste,
        )


def test_impedir_nota_invalida(banco_teste):
    with pytest.raises(
        ValueError,
        match="A nota deve estar entre 0 e 10",
    ):
        adicionar_filme(
            titulo="Filme inválido",
            ano=2020,
            genero="Drama",
            nota=15,
            caminho_banco=banco_teste,
        )