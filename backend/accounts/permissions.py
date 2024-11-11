import logging
from typing import List, Dict

# Logger para auditoria
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

class PermissionError(Exception):
    """Exception raised for errors related to permissions."""
    pass

class AuthenticationError(Exception):
    """Exception raised for unauthorized access attempts."""
    pass

class PermissionControl:
    def __init__(self):
        self._roles_permissions: Dict[str, List[str]] = {
            "administrator": ["create_enterprise", "create_department_sector", "create_team", "create_role", "create_employee", "manage_permissions"],
            "employee": ["add_expense", "add_role"]
        }
        self._user_permissions: Dict[int, List[str]] = {}

    def _is_authorized(self, user_account) -> bool:
        """Check if the user has the 'manage_permissions' permission to make changes."""
        return self.has_permission(user_account, "manage_permissions")

    def assign_role(self, requesting_user, target_user_account, role: str) -> None:
        """Assign a role to a user account if the requesting user has permission."""
        if not self._is_authorized(requesting_user):
            logger.warning("Unauthorized access attempt by user ID %s", id(requesting_user))
            raise AuthenticationError("Unauthorized to modify roles and permissions.")

        if role not in self._roles_permissions:
            raise PermissionError(f"Role '{role}' does not exist.")

        user_id = id(target_user_account)
        self._user_permissions[user_id] = self._roles_permissions[role]
        logger.info("Role '%s' assigned to user ID %s by user ID %s.", role, user_id, id(requesting_user))

    def add_permission(self, requesting_user, target_user_account, permission: str) -> None:
        """Add a specific permission to a user if the requesting user has the 'manage_permissions' permission."""
        if not self._is_authorized(requesting_user):
            logger.warning("Unauthorized permission addition attempt by user ID %s", id(requesting_user))
            raise AuthenticationError("Unauthorized to add permissions.")

        user_id = id(target_user_account)
        if user_id not in self._user_permissions:
            self._user_permissions[user_id] = []
        self._user_permissions[user_id].append(permission)
        logger.info("Permission '%s' added to user ID %s by user ID %s.", permission, user_id, id(requesting_user))

    def remove_permission(self, requesting_user, target_user_account, permission: str) -> None:
        """Remove a specific permission from a user if the requesting user has the 'manage_permissions' permission."""
        if not self._is_authorized(requesting_user):
            logger.warning("Unauthorized permission removal attempt by user ID %s", id(requesting_user))
            raise AuthenticationError("Unauthorized to remove permissions.")

        user_id = id(target_user_account)
        if permission in self._user_permissions.get(user_id, []):
            self._user_permissions[user_id].remove(permission)
            logger.info("Permission '%s' removed from user ID %s by user ID %s.", permission, user_id, id(requesting_user))

    def has_permission(self, user_account, permission: str) -> bool:
        """Check if a user has a specific permission."""
        user_id = id(user_account)
        return permission in self._user_permissions.get(user_id, [])
