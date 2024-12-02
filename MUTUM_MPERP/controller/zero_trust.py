import jwt
from datetime import datetime, timezone
from django.http import JsonResponse
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings  # Para acessar a chave secreta do JWT

class ZeroTrustMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            # Verifica a autenticação
            auth_header = request.META.get('HTTP_AUTHORIZATION', None)
            if auth_header is None:
                raise AuthenticationFailed("Cabeçalho de autorização ausente")

            # Extrai o token do cabeçalho Authorization
            token = self.extract_token(auth_header)
            if not token:
                raise AuthenticationFailed("Token ausente ou malformado")

            # Realizando verificações adicionais de segurança
            if not self.is_valid_token(token):
                raise AuthenticationFailed("Token inválido ou expirado")

            # Decodifica o token e recupera o usuário
            decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user_id = decoded_token.get("user_id")  # Supondo que você use esse campo para identificar o usuário

            if not user_id:
                raise AuthenticationFailed("ID de usuário não encontrado no token")

            # Aqui, você deve carregar o usuário a partir do banco de dados
            # Exemplo: user = User.objects.get(id=user_id)
            user = self.get_user(user_id)
            
            # Adiciona o usuário à requisição
            request.user = user

        except AuthenticationFailed as e:
            return JsonResponse({'error': str(e)}, status=401)

        response = self.get_response(request)
        return response

    def extract_token(self, auth_header):
        # Extrai o token do cabeçalho Authorization
        parts = auth_header.split()
        if len(parts) != 2 or parts[0].lower() != "bearer":
            return None
        return parts[1]

    def is_valid_token(self, token):
        try:
            # Decodifica o token JWT usando a chave secreta
            decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])

            # Verifica a data de expiração
            exp = decoded_token.get('exp')
            if exp is None:
                return False

            # Verifica se o token expirou
            current_time = datetime.now(timezone.utc).timestamp()
            if current_time > exp:
                return False
            return True

        except jwt.ExpiredSignatureError:
            # Se a assinatura expirar, retorna False
            return False
        except jwt.InvalidTokenError:
            # Se o token for inválido por qualquer motivo, retorna False
            return False

    def get_user(self, user_id):
        # Aqui, você deve carregar o usuário a partir do banco de dados
        # Exemplo de recuperação de usuário
        from django.contrib.auth import get_user_model
        try:
            user = get_user_model().objects.get(id=user_id)
        except get_user_model().DoesNotExist:
            raise AuthenticationFailed("Usuário não encontrado")

        return user
