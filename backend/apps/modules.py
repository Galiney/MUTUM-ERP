class Module:
    def __init__(self, name: str) -> None:
        """
        Representa um módulo que armazena processos.

        :param name: Nome do módulo.
        """
        self.name = name
        self.processes: Dict[str, Process] = {}

    def add_process(self, process: Process) -> None:
        """
        Adiciona um processo ao módulo.

        :param process: Objeto do tipo `Process` a ser adicionado.
        """
        if process.name in self.processes:
            raise ValueError(f"O processo '{process.name}' já existe neste módulo.")
        self.processes[process.name] = process
        print(f"Processo '{process.name}' adicionado ao módulo '{self.name}'.")

    def remove_process(self, process_name: str) -> None:
        """
        Remove um processo do módulo.

        :param process_name: Nome do processo a ser removido.
        """
        if process_name not in self.processes:
            raise KeyError(f"O processo '{process_name}' não existe no módulo '{self.name}'.")
        del self.processes[process_name]
        print(f"Processo '{process_name}' removido do módulo '{self.name}'.")

    def execute_process(self, process_name: str) -> None:
        """
        Executa um processo armazenado no módulo.

        :param process_name: Nome do processo a ser executado.
        """
        process = self.processes.get(process_name)
        if not process:
            raise KeyError(f"O processo '{process_name}' não foi encontrado no módulo '{self.name}'.")
        print(f"Executando o processo '{process_name}' no módulo '{self.name}'...")
        process.execute()

    def list_processes(self) -> List[str]:
        """
        Lista os nomes de todos os processos armazenados no módulo.

        :return: Lista de nomes dos processos.
        """
        return list(self.processes.keys())

    def __str__(self) -> str:
        return f"Módulo: {self.name}, Processos: {self.list_processes()}"