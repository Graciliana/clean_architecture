from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
    """
    Classe para gerenciar a conexão com o banco de dados utilizando SQLAlchemy.
    Implementa o protocolo de contexto para facilitar o uso com `with`.
    """
    def __init__(self) -> None:
         
        """
        Inicializa o handler da conexão.
        Cria a string de conexão e inicializa o motor de banco de dados.
        """
        self.__connection_string = "{}://{}:{}@{}:{}/{}".format(
            "mysql+pymysql",  # Driver para conexão com MySQL usando PyMySQL
            "root",  # Nome de usuário do banco de dados
            "vidaloka@88",  # Senha do banco de dados
            "172.17.0.2",  # Host (endereço do banco de dados)
            "3306",  # Porta usada pelo banco de dados
            "clean_database",  # Nome do banco de dados
        )
        # Cria o engine do SQLAlchemy com base na string de conexão
        self.__engine = self.__create_database_engine()
        # Inicializa a sessão como None; será criada em tempo de execução
        self.session = None

    def __create_database_engine(self):
        """
        Cria o motor de banco de dados usando a string de conexão.
        Retorna o objeto `engine` do SQLAlchemy.
        """
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        """
        Retorna o motor de banco de dados (`engine`) para uso direto fora do contexto.
        """
        return self.__engine

    def __enter__(self):
        """
        Método chamado ao entrar no contexto (bloco `with`).
        Cria uma sessão do banco de dados e retorna a instância da classe.
        """
        # Cria uma fábrica de sessões vinculada ao engine
        session_make = sessionmaker(bind=self.__engine)
        # Inicializa a sessão do banco de dados
        self.session = session_make()
        # Retorna a instância para uso dentro do bloco `with`
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Método chamado ao sair do contexto (bloco `with`).
        Garante que a sessão será fechada, liberando os recursos.

        Parâmetros:
        - exc_type: Tipo da exceção, se ocorrer.
        - exc_val: Valor da exceção, se ocorrer.
        - exc_tb: Traceback da exceção, se ocorrer.
        """
        if self.session:
            # Fecha a sessão para liberar conexões
            self.session.close()