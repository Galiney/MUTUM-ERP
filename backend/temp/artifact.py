class Artifact:
    def __init__(self, name: str, data: dict) -> None:
        """
        Representa um artefato no sistema. Um artefato é formado a partir de um conjunto de informações
        e é formatado para atingir um objetivo específico.

        :param name: Nome do artefato.
        :param data: Dados que formam o artefato, como um dicionário de informações.
        """
        self.name = name
        self.data = data  # Dados que representam o artefato

    def format_data(self) -> str:
        """
        Formata os dados do artefato para exibição ou armazenamento de maneira legível.

        :return: Dados formatados como uma string.
        """
        return f"Artefato: {self.name}, Dados: {self.data}"

    def add_information(self, key: str, value: any) -> None:
        """
        Adiciona uma nova informação ao artefato.

        :param key: Chave da informação.
        :param value: Valor da informação.
        """
        self.data[key] = value
        print(f"Informação '{key}' adicionada ao artefato '{self.name}'.")

    def get_information(self, key: str) -> any:
        """
        Obtém o valor de uma informação do artefato.

        :param key: Chave da informação.
        :return: Valor da informação associada à chave.
        """
        return self.data.get(key, "Informação não encontrada.")

    def remove_information(self, key: str) -> None:
        """
        Remove uma informação do artefato.

        :param key: Chave da informação a ser removida.
        """
        if key in self.data:
            del self.data[key]
            print(f"Informação '{key}' removida do artefato '{self.name}'.")
        else:
            print(f"A informação '{key}' não existe no artefato '{self.name}'.")

    def __str__(self) -> str:
        """
        Representação em string do artefato.

        :return: Representação do artefato como string.
        """
        return self.format_data()