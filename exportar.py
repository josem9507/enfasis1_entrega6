from abc import ABC, abstractmethod

class Exportar:
    @abstractmethod
    def exportar(self, grafo):
        pass

class ExportarXML(Exportar):
    def exportar(self, grafo):
        return f'Exportando a XML...'