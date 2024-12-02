class App:
    def __init__(self, name: str) -> None:
        """
        Representa um aplicativo que armazena módulos.

        :param name: Nome do aplicativo.
        """
        self.name = name
        self.modules: Dict[str, Module] = {}

    def add_module(self, module: Module) -> None:
        """
        Adiciona um módulo ao aplicativo.

        :param module: Objeto do tipo `Module` a ser adicionado.
        """
        if module.name in self.modules:
            raise ValueError(f"O módulo '{module.name}' já existe no aplicativo '{self.name}'.")
        self.modules[module.name] = module
        print(f"Módulo '{module.name}' adicionado ao aplicativo '{self.name}'.")

    def remove_module(self, module_name: str) -> None:
        """
        Remove um módulo do aplicativo.

        :param module_name: Nome do módulo a ser removido.
        """
        if module_name not in self.modules:
            raise KeyError(f"O módulo '{module_name}' não existe no aplicativo '{self.name}'.")
        del self.modules[module_name]
        print(f"Módulo '{module_name}' removido do aplicativo '{self.name}'.")

    def get_module(self, module_name: str) -> Module:
        """
        Retorna um módulo armazenado no aplicativo.

        :param module_name: Nome do módulo a ser acessado.
        :return: Objeto do tipo `Module`.
        """
        module = self.modules.get(module_name)
        if not module:
            raise KeyError(f"O módulo '{module_name}' não foi encontrado no aplicativo '{self.name}'.")
        return module

    def execute_process(self, module_name: str, process_name: str) -> None:
        """
        Executa um processo armazenado em um módulo específico.

        :param module_name: Nome do módulo onde o processo está armazenado.
        :param process_name: Nome do processo a ser executado.
        """
        module = self.get_module(module_name)
        print(f"Acessando o módulo '{module_name}'...")
        module.execute_process(process_name)

    def list_modules(self) -> List[str]:
        """
        Lista os nomes de todos os módulos armazenados no aplicativo.

        :return: Lista de nomes dos módulos.
        """
        return list(self.modules.keys())

    def __str__(self) -> str:
        return f"Aplicativo: {self.name}, Módulos: {self.list_modules()}"
