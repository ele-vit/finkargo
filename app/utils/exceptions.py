class MyCustomException(Exception):
    """A simple class for our own exception type"""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
