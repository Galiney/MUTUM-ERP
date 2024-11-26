class Process:
    def __init__(
        self,
        name: str,
        routines: List[Routine],
        artifacts: List[Artifact],
        informations: List[Information],
        people: List[Person],
        storage: Storage,
        calculations: Optional[Callable[..., Any]] = None,
    ) -> None:
        """
        Classe principal de Processos modulares, customizáveis e fáceis de alterar.

        :param name: Nome do processo.
        :param routines: Lista de rotinas.
        :param artifacts: Lista de artefatos.
        :param informations: Lista de informações primitivas.
        :param people: Lista de pessoas envolvidas.
        :param storage: Armazenamento do sistema.
        :param calculations: Função opcional para cálculos.
        """
        self.name = name
        self.routines = routines
        self.artifacts = artifacts
        self.informations = informations
        self.people = people
        self.storage = storage
        self.calculations = calculations

    def execute(self) -> None:
        """
        Executa o processo completo.
        """
        print(f"Iniciando o processo: {self.name}")
        for routine in self.routines:
            routine.execute()

        if self.calculations:
            print("Executando cálculos...")
            result = self.calculations()
            print(f"Resultado dos cálculos: {result}")

        print("Processo concluído.")

    def __str__(self) -> str:
        return (
            f"Processo: {self.name}\n"
            f"Rotinas: {[routine.name for routine in self.routines]}\n"
            f"Artefatos: {[artifact.name for artifact in self.artifacts]}\n"
            f"Informações: {[info.key for info in self.informations]}\n"
            f"Pessoas: {[person.name for person in self.people]}"
        )
