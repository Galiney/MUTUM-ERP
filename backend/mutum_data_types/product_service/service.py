from enum import Enum

class ServiceDeliveryType(Enum):
    IN_PERSON = "Presencial"
    REMOTE = "Remoto"
    HYBRID = "Híbrido"

class ServiceNature(Enum):
    EXPERIENCE = "Experiências"
    PRODUCTION = "Produção"
    CONSULTANCY_AND_INFORMATION = "Consultoria e Informação"
    EXECUTION = "Execução"
    PROVIDER = "Provedor"

class Service:
    def __init__(
        self, 
        name: str, 
        delivery_type: ServiceDeliveryType, 
        nature: ServiceNature, 
    ) -> None:
        """
        Inicializa uma instância de Serviço.

        :param name: Nome do serviço.
        :param delivery_type: Tipo de entrega do serviço, baseado no enum ServiceDeliveryType.
        :param nature: Natureza do serviço, baseado no enum ServiceNature.
        :param description: Descrição opcional do serviço.
        """
        self.name = name
        self.delivery_type = delivery_type
        self.nature = nature
