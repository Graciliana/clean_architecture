from src.infra.db.settings.connection import DBConnectionHandler
# Importa o gerenciador de conexão com o banco de dados, responsável por criar e gerenciar as conexões.

from src.infra.db.settings.users import Users as UsersEntity  # type: ignore
# Importa a classe `Users` que representa a entidade (tabela) de usuários no banco de dados.
# O comentário `# type: ignore` é usado para ignorar erros de tipagem caso o analisador estático não consiga resolver esse import.


class UsersRepository:
    """
    Classe de repositório para gerenciar operações relacionadas à entidade `Users`.
    Segue o padrão Repository, separando a lógica de acesso a dados da lógica de negócios.
    """

    @classmethod
    def insert_user(cls, first_name: str, last_name: str, age: int) -> None:
        """
        Insere um novo usuário no banco de dados.

        Parâmetros:
        - first_name: Primeiro nome do usuário.
        - last_name: Último nome do usuário.
        - age: Idade do usuário.
        """
        # Utiliza o gerenciador de contexto para criar uma conexão com o banco
        with DBConnectionHandler() as database:
            try:
                # Cria uma nova instância da entidade Users com os dados fornecidos
                new_registry = UsersEntity(
                    first_name=first_name,  # Mapeia o primeiro nome para a coluna correspondente
                    last_name=last_name,  # Mapeia o último nome para a coluna correspondente
                    age=age,  # Mapeia a idade para a coluna correspondente
                )
                # Adiciona o novo registro na sessão do banco
                database.session.add(new_registry)
                # Persiste as alterações no banco de dados
                database.session.commit()
            except Exception as exception:
                # Em caso de erro, desfaz todas as alterações pendentes na sessão
                database.session.rollback()
                # Relança a exceção para que ela possa ser tratada em níveis superiores
                raise exception
