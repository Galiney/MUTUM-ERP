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
                "permission_1": False,
                "permission_2": False,
                "permission_3": False,
            },
            "system_administrator": { #modificações de sistema e estrutural
                "create_account": False,
                "exclude_account": False,
                "modify_account": False,
                "create_enterprise": False,
                "exclude_enterprise": False,
                "modify_enterprise": False,
                "create_department": False,
                "exclude_department": False,
                "modify_department": False,
                "create_team": False,
                "exclude_team": False,
                "modify_team": False,
                "create_role": False,
                "exclude_role": False,
                "modify_role": False,
            }
        }