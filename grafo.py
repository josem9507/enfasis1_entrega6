from exportar import ExportarXML
from nodo import Ciudad, Industria, LugarTurismo

class Grafo:
    def __init__(self, id):
        self.id = id

    def getNodos(self):
        ciudades = Ciudad(self.id)
        industria = Industria(self.id)
        lugarTurismo = LugarTurismo(self.id)

        return ciudades.getEnlaces(), industria.getEnlaces(), lugarTurismo.getEnlaces()

    def exportar(self, tipo: str):
        if tipo == 'XML':
            return ExportarXML().exportar(self.getNodos)
        return 'No se encontró el tipo seleccionado'