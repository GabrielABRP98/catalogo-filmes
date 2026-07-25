from datetime import date

import pandas as pd
import streamlit as st

from database import (
    adicionar_filme,
    atualizar_filme,
    buscar_filme,
    excluir_filme,
    inicializar_banco,
    listar_filmes,
)
from seed_database import popular_banco


st.set_page_config(
    page_title="Catálogo de Filmes",
    page_icon="🎬",
    layout="wide",
)


def preparar_banco() -> None:
    """
    Cria o banco e adiciona os filmes demonstrativos
    quando a aplicação é executada pela primeira vez.
    """

    if "banco_preparado" in st.session_state:
        return

    inicializar_banco()

    if not listar_filmes():
        popular_banco()

    st.session_state["banco_preparado"] = True


def preparar_tabela(filmes: list[dict]) -> pd.DataFrame:
    """Converte os filmes em uma tabela adequada para exibição."""

    tabela = pd.DataFrame(filmes)

    tabela["assistido"] = tabela["assistido"].map(
        {
            1: "Sim",
            0: "Não",
        }
    )

    tabela["nota"] = tabela["nota"].apply(
        lambda valor: (
            "Sem nota"
            if pd.isna(valor)
            else f"{valor:.1f}"
        )
    )

    tabela = tabela.rename(
        columns={
            "id": "ID",
            "titulo": "Título",
            "ano": "Ano",
            "genero": "Gênero",
            "nota": "Nota",
            "assistido": "Assistido",
            "criado_em": "Cadastrado em",
        }
    )

    return tabela[
        [
            "ID",
            "Título",
            "Ano",
            "Gênero",
            "Nota",
            "Assistido",
            "Cadastrado em",
        ]
    ]


try:
    preparar_banco()
except Exception as erro:
    st.error(
        "Não foi possível preparar o banco de dados. "
        f"Detalhes: {erro}"
    )
    st.stop()


st.title("🎬 Catálogo de Filmes")

st.write(
    "Aplicação para cadastrar, consultar, editar e excluir filmes "
    "utilizando Python, Streamlit e SQLite."
)


aba_catalogo, aba_cadastro, aba_edicao = st.tabs(
    [
        "📚 Catálogo",
        "➕ Cadastrar filme",
        "✏️ Editar ou excluir",
    ]
)


with aba_catalogo:
    todos_os_filmes = listar_filmes()

    total_filmes = len(todos_os_filmes)

    total_assistidos = sum(
        1
        for filme in todos_os_filmes
        if filme["assistido"]
    )

    total_pendentes = total_filmes - total_assistidos

    notas = [
        filme["nota"]
        for filme in todos_os_filmes
        if filme["nota"] is not None
    ]

    media_notas = (
        sum(notas) / len(notas)
        if notas
        else 0
    )

    coluna1, coluna2, coluna3, coluna4 = st.columns(4)

    coluna1.metric(
        "Filmes cadastrados",
        total_filmes,
    )

    coluna2.metric(
        "Assistidos",
        total_assistidos,
    )

    coluna3.metric(
        "Pendentes",
        total_pendentes,
    )

    coluna4.metric(
        "Média das notas",
        f"{media_notas:.1f}"
        if notas
        else "Sem notas",
    )

    st.divider()

    busca = st.text_input(
        "Pesquisar",
        placeholder="Digite um título ou gênero...",
    )

    filmes_encontrados = listar_filmes(
        busca=busca,
    )

    if filmes_encontrados:
        tabela = preparar_tabela(
            filmes_encontrados
        )

        st.dataframe(
            tabela,
            use_container_width=True,
            hide_index=True,
        )

    elif busca:
        st.warning(
            "Nenhum filme encontrado para essa pesquisa."
        )

    else:
        st.info(
            "Nenhum filme foi cadastrado ainda."
        )


with aba_cadastro:
    st.subheader("Cadastrar novo filme")

    with st.form(
        "formulario_cadastro",
        clear_on_submit=True,
    ):
        titulo = st.text_input(
            "Título",
            placeholder="Exemplo: Interestelar",
        )

        coluna1, coluna2 = st.columns(2)

        with coluna1:
            ano = st.number_input(
                "Ano de lançamento",
                min_value=1888,
                max_value=2100,
                value=date.today().year,
                step=1,
            )

        with coluna2:
            genero = st.text_input(
                "Gênero",
                placeholder="Exemplo: Ficção científica",
            )

        possui_nota = st.checkbox(
            "Adicionar uma nota",
            value=True,
        )

        nota = st.number_input(
            "Nota",
            min_value=0.0,
            max_value=10.0,
            value=8.0,
            step=0.1,
            disabled=not possui_nota,
        )

        assistido = st.checkbox(
            "Filme já assistido"
        )

        cadastrar = st.form_submit_button(
            "Cadastrar filme",
            type="primary",
            use_container_width=True,
        )

    if cadastrar:
        try:
            filme_id = adicionar_filme(
                titulo=titulo,
                ano=int(ano),
                genero=genero,
                nota=(
                    float(nota)
                    if possui_nota
                    else None
                ),
                assistido=assistido,
            )

            st.success(
                "Filme cadastrado com sucesso! "
                f"ID: {filme_id}"
            )

        except ValueError as erro:
            st.error(str(erro))

        except Exception as erro:
            st.error(
                "Não foi possível cadastrar o filme. "
                f"Detalhes: {erro}"
            )


with aba_edicao:
    st.subheader("Editar ou excluir filme")

    filmes_cadastrados = listar_filmes()

    if not filmes_cadastrados:
        st.info(
            "Cadastre pelo menos um filme antes "
            "de utilizar esta seção."
        )

    else:
        opcoes = {
            (
                f'{filme["id"]} — '
                f'{filme["titulo"]} '
                f'({filme["ano"]})'
            ): filme["id"]
            for filme in filmes_cadastrados
        }

        filme_selecionado = st.selectbox(
            "Selecione um filme",
            options=list(opcoes.keys()),
        )

        filme_id = opcoes[
            filme_selecionado
        ]

        filme = buscar_filme(
            filme_id
        )

        if filme is None:
            st.error(
                "O filme selecionado não foi encontrado."
            )

        else:
            with st.form(
                "formulario_edicao"
            ):
                titulo_editado = st.text_input(
                    "Título",
                    value=filme["titulo"],
                )

                coluna1, coluna2 = st.columns(2)

                with coluna1:
                    ano_editado = st.number_input(
                        "Ano de lançamento",
                        min_value=1888,
                        max_value=2100,
                        value=int(
                            filme["ano"]
                        ),
                        step=1,
                    )

                with coluna2:
                    genero_editado = st.text_input(
                        "Gênero",
                        value=filme["genero"],
                    )

                possui_nota_editada = st.checkbox(
                    "O filme possui nota",
                    value=(
                        filme["nota"]
                        is not None
                    ),
                )

                nota_atual = (
                    float(filme["nota"])
                    if filme["nota"] is not None
                    else 0.0
                )

                nota_editada = st.number_input(
                    "Nota",
                    min_value=0.0,
                    max_value=10.0,
                    value=nota_atual,
                    step=0.1,
                    disabled=(
                        not possui_nota_editada
                    ),
                )

                assistido_editado = st.checkbox(
                    "Filme assistido",
                    value=bool(
                        filme["assistido"]
                    ),
                )

                salvar = st.form_submit_button(
                    "Salvar alterações",
                    type="primary",
                    use_container_width=True,
                )

            if salvar:
                try:
                    atualizado = atualizar_filme(
                        filme_id=filme_id,
                        titulo=titulo_editado,
                        ano=int(ano_editado),
                        genero=genero_editado,
                        nota=(
                            float(nota_editada)
                            if possui_nota_editada
                            else None
                        ),
                        assistido=(
                            assistido_editado
                        ),
                    )

                    if atualizado:
                        st.success(
                            "Filme atualizado com sucesso."
                        )
                        st.rerun()

                    else:
                        st.error(
                            "Filme não encontrado."
                        )

                except ValueError as erro:
                    st.error(str(erro))

                except Exception as erro:
                    st.error(
                        "Não foi possível atualizar "
                        "o filme. "
                        f"Detalhes: {erro}"
                    )

            st.divider()
            st.subheader("Excluir filme")

            confirmar_exclusao = st.checkbox(
                "Confirmo a exclusão de "
                f'"{filme["titulo"]}"',
                key=(
                    f"confirmar_exclusao_"
                    f"{filme_id}"
                ),
            )

            excluir = st.button(
                "Excluir permanentemente",
                type="secondary",
                disabled=(
                    not confirmar_exclusao
                ),
                use_container_width=True,
            )

            if excluir:
                try:
                    excluido = excluir_filme(
                        filme_id
                    )

                    if excluido:
                        st.success(
                            "Filme excluído com sucesso."
                        )
                        st.rerun()

                    else:
                        st.error(
                            "Filme não encontrado."
                        )

                except Exception as erro:
                    st.error(
                        "Não foi possível excluir "
                        "o filme. "
                        f"Detalhes: {erro}"
                    )