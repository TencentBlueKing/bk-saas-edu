# -*- coding: utf-8 -*-
class ApiResultError(Exception):
    def __init__(self, message):
        super().__init__(self)
        self.message = message

    def __str__(self):
        return f"call API error; message: {self.message}"
