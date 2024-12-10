class InvalidEmailFormatError(Exception):
    """Custom exception raised when the email format is invalid."""
    pass

class InvalidDataFormatError(Exception):
    """Custom exception raised when data format is invalid."""
    pass

class UnauthorizedActionError(Exception):
    """Custom exception raised when an action is not authorized."""
    pass