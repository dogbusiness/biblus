class EmptyFields(Exception):

    def __init__(self):
        super().__init__(self)
        self.detail = "fields you use for search are empty"


class NotFound(Exception):

    def __init__(self):
        super().__init__(self)
        self.detail = "object(s) not found"
