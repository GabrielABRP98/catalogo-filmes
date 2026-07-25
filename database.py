from pathlib import Path
import sqlite3


DB_PATH = Path(__file__).resolve().parent / "catalogo_filmes.db"


def conectar(caminho_banco: str | Path = DB_PATH) -> sqlite3.Connection:
    """Cria uma conexão com o banco SQLite."""

    conexao = sqlite3.connect(caminho_banco)
    conexao.row_factory = sqlite3.Row
    return conexao


def inicializar_banco(caminho_banco: str | Path = DB_PATH) -> None:
    """Cria a tabela de filmes caso ela ainda não exista."""

    with conectar(caminho_banco) as conexao:
        conexao.execute(
            """
            CREATE TABLE IF NOT EXISTS filmes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                ano INTEGER NOT NULL CHECK (ano BETWEEN 1888 AND 2100),
                genero TEXT NOT NULL DEFAULT 'Não informado',
                nota REAL CHECK (nota IS NULL OR nota BETWEEN 0 AND 10),
                assistido INTEGER NOT NULL DEFAULT 0
                    CHECK (assistido IN (0, 1)),
                criado_em TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )


def validar_filme(
    titulo: str,
    ano: int,
    genero: str,
    nota: float | None,
) -> tuple[str, int, str, float | None]:
    """Valida e normaliza os dados informados."""

    titulo = titulo.strip()
    genero = genero.strip() or "Não informado"

    if not titulo:
        raise ValueError("O título do filme é obrigatório.")

    if not 1888 <= int(ano) <= 2100:
        raise ValueError("O ano deve estar entre 1888 e 2100.")

    if nota is not None and not 0 <= float(nota) <= 10:
        raise ValueError("A nota deve estar entre 0 e 10.")

    nota_convertida = float(nota) if nota is not None else None

    return titulo, int(ano), genero, nota_convertida


def adicionar_filme(
    titulo: str,
    ano: int,
    genero: str,
    nota: float | None = None,
    assistido: bool = False,
    caminho_banco: str | Path = DB_PATH,
) -> int:
    """Adiciona um filme e retorna seu identificador."""

    titulo, ano, genero, nota = validar_filme(titulo, ano, genero, nota)

    with conectar(caminho_banco) as conexao:
        cursor = conexao.execute(
            """
            INSERT INTO filmes (titulo, ano, genero, nota, assistido)
            VALUES (?, ?, ?, ?, ?)
            """,
            (titulo, ano, genero, nota, int(assistido)),
        )

        return int(cursor.lastrowid)


def listar_filmes(
    busca: str = "",
    caminho_banco: str | Path = DB_PATH,
) -> list[dict]:
    """Retorna todos os filmes ou filtra pelo título e gênero."""

    busca = busca.strip()

    with conectar(caminho_banco) as conexao:
        if busca:
            termo = f"%{busca}%"

            cursor = conexao.execute(
                """
                SELECT id, titulo, ano, genero, nota, assistido, criado_em
                FROM filmes
                WHERE titulo LIKE ? OR genero LIKE ?
                ORDER BY titulo COLLATE NOCASE
                """,
                (termo, termo),
            )
        else:
            cursor = conexao.execute(
                """
                SELECT id, titulo, ano, genero, nota, assistido, criado_em
                FROM filmes
                ORDER BY titulo COLLATE NOCASE
                """
            )

        return [dict(linha) for linha in cursor.fetchall()]


def buscar_filme(
    filme_id: int,
    caminho_banco: str | Path = DB_PATH,
) -> dict | None:
    """Busca um filme pelo identificador."""

    with conectar(caminho_banco) as conexao:
        linha = conexao.execute(
            """
            SELECT id, titulo, ano, genero, nota, assistido, criado_em
            FROM filmes
            WHERE id = ?
            """,
            (filme_id,),
        ).fetchone()

        return dict(linha) if linha else None


def atualizar_filme(
    filme_id: int,
    titulo: str,
    ano: int,
    genero: str,
    nota: float | None = None,
    assistido: bool = False,
    caminho_banco: str | Path = DB_PATH,
) -> bool:
    """Atualiza um filme e informa se ele foi encontrado."""

    titulo, ano, genero, nota = validar_filme(titulo, ano, genero, nota)

    with conectar(caminho_banco) as conexao:
        cursor = conexao.execute(
            """
            UPDATE filmes
            SET titulo = ?,
                ano = ?,
                genero = ?,
                nota = ?,
                assistido = ?
            WHERE id = ?
            """,
            (titulo, ano, genero, nota, int(assistido), filme_id),
        )

        return cursor.rowcount > 0


def excluir_filme(
    filme_id: int,
    caminho_banco: str | Path = DB_PATH,
) -> bool:
    """Exclui um filme e informa se ele foi encontrado."""

    with conectar(caminho_banco) as conexao:
        cursor = conexao.execute(
            "DELETE FROM filmes WHERE id = ?",
            (filme_id,),
        )

        return cursor.rowcount > 0

if __name__ == "__main__":
    inicializar_banco()
    print("Banco criado com sucesso.")