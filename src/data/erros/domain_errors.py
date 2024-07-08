class DomainError(Exception):
    pass


class BadRequestError(DomainError):
    def __init__(self, message="Bad request"):
        self.message = message
        super().__init__(self.message)


class NotFoundError(DomainError):
    def __init__(self, message="Not found"):
        self.message = message
        super().__init__(self.message)


class InternalServerError(DomainError):
    def __init__(self, message="Internal server error"):
        self.message = message
        super().__init__(self.message)
