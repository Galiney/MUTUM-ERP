import os

class Document:
    def __init__(self, name: str, file_path: str, file_format: str) -> None:
        """
        Representa um documento no sistema, podendo ser de diferentes formatos (XML, PDF, etc).
        
        :param name: Nome do documento.
        :param file_path: Caminho do arquivo no sistema de arquivos.
        :param file_format: Formato do documento (por exemplo, 'pdf', 'xml', 'txt', etc).
        """
        self.name = name
        self.file_path = file_path
        self.file_format = file_format.lower()
        
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"O arquivo {file_path} não foi encontrado.")
        
        self.size = os.path.getsize(file_path)  # Obtém o tamanho do arquivo em bytes

    def get_info(self) -> dict:
        """
        Retorna as informações principais sobre o documento.

        :return: Dicionário com o nome, caminho, formato e tamanho do arquivo.
        """
        return {
            'name': self.name,
            'file_path': self.file_path,
            'file_format': self.file_format,
            'size': self.size,
        }

    def __str__(self) -> str:
        """
        Retorna uma representação em string do documento.

        :return: Representação do documento como string.
        """
        return f"Documento: {self.name}, Formato: {self.file_format.upper()}, Tamanho: {self.size} bytes"

    def change_file_path(self, new_path: str) -> None:
        """
        Altera o caminho do arquivo.
        
        :param new_path: Novo caminho para o arquivo.
        """
        if not os.path.exists(new_path):
            raise FileNotFoundError(f"O arquivo {new_path} não foi encontrado.")
        self.file_path = new_path
        self.size = os.path.getsize(new_path)
        print(f"Caminho do arquivo alterado para: {new_path}")

    def change_name(self, new_name: str) -> None:
        """
        Altera o nome do documento.
        
        :param new_name: Novo nome para o documento.
        """
        self.name = new_name
        print(f"Nome do documento alterado para: {new_name}")

    def get_file(self) -> bytes:
        """
        Retorna o conteúdo do arquivo em formato binário.
        
        :return: Conteúdo do arquivo em bytes.
        """
        with open(self.file_path, 'rb') as file:
            return file.read()
