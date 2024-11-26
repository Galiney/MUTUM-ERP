import unittest
from unittest.mock import MagicMock
from mutum_data_types import Expense, Revenue, Asset, Liability, Custom_data
from . import *

class TestEnterprise(unittest.TestCase):
    def setUp(self):
        # Cria uma instância da classe para os testes
        self.enterprise = Enterprise()
        self.mock_department_sector = MagicMock(spec=Department_sector)
        self.mock_role = MagicMock(spec=Role)
        self.mock_employee = MagicMock()  # Supondo que Employee é importado corretamente
        self.mock_document = MagicMock(spec=Custom_data)
        self.mock_asset = MagicMock(spec=Asset)
        self.mock_liability = MagicMock(spec=Liability)
        self.mock_expense = MagicMock(spec=Expense)
        self.mock_revenue = MagicMock(spec=Revenue)

    def test_register_department_sector(self):
        result = self.enterprise.register_department_sector(self.mock_department_sector)
        self.assertTrue(result)
    
    def test_register_role(self):
        result = self.enterprise.register_role(self.mock_role)
        self.assertTrue(result)

    def test_register_employee(self):
        result = self.enterprise.register_employee(self.mock_employee)
        self.assertTrue(result)

    def test_add_government_document(self):
        result = self.enterprise.add_government_document(self.mock_document)
        self.assertTrue(result)

    def test_add_asset(self):
        result = self.enterprise.add_asset(self.mock_asset)
        self.assertTrue(result)

    def test_add_liability(self):
        result = self.enterprise.add_liability(self.mock_liability)
        self.assertTrue(result)

    def test_add_expense(self):
        result = self.enterprise.add_expense(self.mock_expense)
        self.assertTrue(result)

    def test_add_revenue(self):
        result = self.enterprise.add_revenue(self.mock_revenue)
        self.assertTrue(result)

    def test_register_department_sector_failure(self):
        # Testa um caso de erro ao adicionar um departamento
        self.enterprise._Enterprise__department_sectors = None  # Simula um estado inválido
        result = self.enterprise.register_department_sector(self.mock_department_sector)
        self.assertFalse(result)

    def test_register_role_failure(self):
        # Testa um caso de erro ao adicionar uma role
        self.enterprise._Enterprise__roles = None  # Simula um estado inválido
        result = self.enterprise.register_role(self.mock_role)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
