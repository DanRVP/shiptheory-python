import json

class ClientObject:
    def __init__(self) -> None:
        pass

    def toDict(self):
        return self.__dict__

    def toJson(self):
        return json.dumps(self.toDict())
