from django.test import TestCase, Client
import json
from django.urls import reverse
from .models import Accounts
from django.contrib.auth.models import User

class AddAccountTest(TestCase):
    def setUp(self):
        print("setup iniciando")
        self.client = Client()
        print("setup client feito")
        self.url = reverse('execute_command')  
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

class AccountRemoveTest(TestCase):
    def setUp(self):
        print("setup iniciando")
        self.client = Client()
        print("setup client feito")
        self.url = reverse('execute_command')  # URL para o comando de execução
        print("setup url reverse execute_command, fazendo payload")

        # Criando um usuário para autenticação
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        print("setup user criado", self.user)

        # Criando uma conta para teste de remoção
        self.account = Accounts.objects.create(
            user_data={
                "creator": str(self.user.id),
                "email": "testuser@example.com",
                "phone": "123456789"
            }
        )
        print("setup account criada", self.account)

        # Payload para remover a conta
        self.remove_payload = {
            "command": "remove",
            "parameter": "account"
        }
        print("setup remove_payload feito", self.remove_payload)

    def test_remove_account_without_authentication(self):
        print("test remove account without authentication iniciado")

        # Realizar a requisição POST sem autenticação, tentando remover a conta
        response = self.client.post(
            self.url,
            data=json.dumps(self.remove_payload),
            content_type='application/json'
        )
        print("test remove account response feito", response)

        # Verificar o código de status retornado
        self.assertEqual(response.status_code, 401)

        # Verificar a mensagem no corpo da resposta
        self.assertEqual(response.json().get('message'), "Authentication required to remove an account.")

        # Verificar que a conta ainda existe no banco de dados
        self.assertEqual(Accounts.objects.count(), 1)

        print("test remove account without authentication finalizado")

    def test_remove_account_with_wrong_user(self):
        print("test remove account with wrong user iniciado")

        # Criar um segundo usuário
        wrong_user = User.objects.create_user(username='wronguser', password='wrongpassword')

        # Realizar a requisição de remoção autenticado com outro usuário
        self.client.login(username='wronguser', password='wrongpassword')

        response = self.client.post(
            self.url,
            data=json.dumps(self.remove_payload),
            content_type='application/json'
        )
        print("test remove account with wrong user response feito", response)

        # Verificar o código de status retornado
        self.assertEqual(response.status_code, 403)

        # Verificar a mensagem no corpo da resposta
        self.assertEqual(response.json().get('message'), "You do not have permission to delete this account.")

        # Verificar que a conta ainda existe no banco de dados
        self.assertEqual(Accounts.objects.count(), 1)

        print("test remove account with wrong user finalizado")

    def test_remove_account_success(self):
        print("test remove account success iniciado")

        # Fazer login com o usuário correto
        self.client.login(username='testuser', password='testpassword')

        # Realizar a requisição de remoção da conta
        response = self.client.post(
            self.url,
            data=json.dumps(self.remove_payload),
            content_type='application/json'
        )
        print("test remove account success response feito", response)

        # Verificar o código de status retornado
        self.assertEqual(response.status_code, 200)

        # Verificar a mensagem no corpo da resposta
        self.assertEqual(response.json().get('message'), "Account removed successfully.")

        # Verificar que a conta foi removida do banco de dados
        self.assertEqual(Accounts.objects.count(), 0)

        print("test remove account success finalizado")
