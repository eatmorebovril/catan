class Port:
    def __init__(self, resource: str = None):
        self.resource = resource
        self.exchange_rate = 3 if not self.resource else 2

    def __str__(self):
        port_resource = "" if not self.resource else f" {self.resource}"
        return f"{self.exchange_rate}:1{port_resource} port"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if not isinstance(other, Port):
            return False
        return self.resource == other.resource and self.exchange_rate == other.exchange_rate
