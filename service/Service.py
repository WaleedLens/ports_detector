class Service:
    def __init__(self,name,port,id):
        self.name = name
        self.port = port
        self.id = id

    def get_port(self) -> int:
        return self.port
    
    def get_name(self) -> str:
        return self.name
    
    def get_id(self) -> int:
        return self.id
    
    


    