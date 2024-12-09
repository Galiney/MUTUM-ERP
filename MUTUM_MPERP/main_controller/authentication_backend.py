from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from .models import Accounts

class CustomAuthenticationBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        print("o authenticate correto foi usuado")
        try:
            # Tenta encontrar o usuário pelo nome de usuário
            user = Accounts.objects.get(user_data__username=username)
            
            # Verifica se a senha fornecida corresponde à senha armazenada
            if user.check_password(password):
                return user
            else:
                return None  # Senha incorreta
            
        except ObjectDoesNotExist:
            return None  # Usuário não encontrado

    def get_user(self, user_id):
        try:
            return get_user_model().objects.get(id=user_id)
        except ObjectDoesNotExist:
            return None
