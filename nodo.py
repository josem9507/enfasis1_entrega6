from abc import ABC, abstractmethod

class Nodo:
    def __init__(self, id_grafo, estadoComun = 'activo'):
        self.estadoComun = estadoComun
        self.id_grafo = id_grafo

    def getEnlaces(self) -> []:
        pass
    
    @abstractmethod
    def funcInfoGeo(self):
        pass

class Ciudad(Nodo):
    def funcInfoGeo(self):
        return f'Información desde ciudad'

class Industria(Nodo):
    def funcInfoGeo(self):
        return f'Información desde industria'

class LugarTurismo(Nodo):
    def funcInfoGeo(self):
        return f'Información desde lugar turismo'


class Enlace:
    def __init__(self):
        # Se crea un enlace como ejemplo
        nodo = Ciudad('activo')
        nodo.funcInfoGeo()