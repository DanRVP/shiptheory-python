class Response:

    def __init__(self, body = None, code = None, url = None,):
        self.body = body
        self.code = code
        self.url = url
        self.error = None

    @property 
    def body(self) -> str|None:
        return self._body

    @body.setter
    def body(self, body: str) -> str|None:
        self._body = body

    @property 
    def code(self) -> int|None:
        return self._code

    @code.setter
    def code(self, code: int) -> int|None:
        self._code = code

    @property 
    def url(self) -> str|None:
        return self._url

    @url.setter
    def url(self, url: str) -> str|None:
        self._url = url

    @property 
    def error(self) -> str|None: 
        return self._error

    @error.setter
    def error(self, error: str) -> str|None:
        self._error = error
