from django.db import models

class Accounts(models.Model):
    user_data = models.JSONField(
        null=False, blank=False,
        verbose_name="Dados do Usuário"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última Atualização")
