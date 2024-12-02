from django.test import TestCase, Client
import json
from django.urls import reverse
from .models import Accounts

class AddAccountTest(TestCase):
    def setUp(self):
        print("setup iniciando")
        self.client = Client()
        print("setup client feito")
        self.url = reverse('execute_command')  # Certifique-se de que a URL esteja configurada corretamente
        print("setup url reverse execute_comando, fazendo payload")
        self.payload = {
            "command": "add",
            "parameter": "account"
        }
        print("setup payload feito", self.payload)

    def test_add_account_without_authentication(self):
        print("test add account iniciado")
        
        # Realizar a requisição POST com o comando para adicionar uma conta
        response = self.client.post(
            self.url,
            data=json.dumps(self.payload),
            content_type='application/json'
        )
        print("test add account response feito", response)

        # Verificar o código de status retornado
        self.assertEqual(response.status_code, 201)

        # Verificar a mensagem no corpo da resposta
        self.assertEqual(
            response.json().get('message'),
            "Account created without authentication."
        )

        # Verificar se a conta foi criada no banco de dados
        self.assertEqual(Accounts.objects.count(), 1)

        # Verificar as informações da conta criada (por exemplo, o campo `user_data` ou outros campos)
        created_account = Accounts.objects.first()  # Pegando a primeira conta criada
        print("Conta criada:", created_account.user_data)  # Ajuste conforme os campos reais

        # Opcional: Verificar detalhes específicos da conta
        self.assertIsNotNone(created_account.user_data)  # Exemplo de verificação

        print("test add account finalizado")