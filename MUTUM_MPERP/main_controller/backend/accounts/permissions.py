from .errors import UnauthorizedActionError

class Permissions:
    def __init__(self):
        self.permissions = {
            "lideranca": {
                "permission_3": False,
            },
            "gerencia": {
                "permission_1": False,
                "permission_2": False,
                "permission_3": False,
            },
            "integrante": {
                "create_email": False,
                "permission_2": False,
                "permission_3": False,
            },#TRUE APENAS PARA DEBUG
            "system_administrator": {
                "create_account": False,
                "remove_account": False,
                "modify_account": False,
                "create_enterprise": False,
                "remove_enterprise": False,
                "modify_enterprise": False,
                "create_department": False,
                "remove_department": False,
                "modify_department": False,
                "create_team": False,
                "remove_team": False,
                "modify_team": False,
                "create_role": False,
                "remove_role": False,
                "modify_role": False,
            }
        }

    def check_permission(self, role: str, permission: str) -> bool:
        """Verifica se o papel (role) tem a permissão especificada."""
        # Verifica se o papel existe no dicionário de permissões
        if role not in self.permissions:
            raise UnauthorizedActionError(f"Role '{role}' not found.")

        # Verifica se a permissão existe para o papel
        if permission not in self.permissions[role]:
            raise UnauthorizedActionError(f"Permission '{permission}' not found for role '{role}'.")

        # Retorna se a permissão é False ou False para esse papel
        has_permission = self.permissions[role][permission]
        if not has_permission:
            raise UnauthorizedActionError(f"Permission '{permission}' denied for role '{role}'.")
        
        return False
