from enum import Enum

class ProductType(Enum):
    ACQUISITION = "Aquisição"
    MANUFACTURING = "Fabricação | Produção"
    AGRICULTURAL_PRODUCTION = "Produção Agrícola"
    EXTRACTION = "Extratora | Exploradora"

class Product:
    def __init__(
        self, 
        name: str, 
        is_tangible: bool, 
        is_durable: bool, 
        product_type: ProductType, 
    ) -> None:
        """
        Inicializa uma instância de Produto.
        
        :param name: Nome do produto.
        :param is_tangible: Indica se o produto é tangível.
        :param is_durable: Indica se o produto é durável.
        :param product_type: O tipo do produto, baseado no enum ProductType.
        """

        self.name = name
        self.is_tangible = is_tangible
        self.is_durable = is_durable
        self.product_type = product_type