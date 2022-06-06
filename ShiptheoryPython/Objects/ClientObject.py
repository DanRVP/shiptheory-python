import json

class ClientObject:

    def toDict(self):
        """
        Turns the ClientObject into a dict
        """
        dict = {}
        vars = self.__dict__
        for i in vars:
            stripped = i.lstrip('_')
            attr = self.__getattribute__(i)
            if (isinstance(attr, ClientObject)):
                dict[stripped] = attr.toDict()
            elif (isinstance(attr, list)):
                for j in attr:                    
                    dict[stripped] = j.toDict()
            else:
                dict[stripped] = attr
        
        return dict


    def toJson(self):
        """
        Turns the ClientObject into a JSON string. 
        """
        return json.dumps(self.toDict())
