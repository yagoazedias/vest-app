from abc import ABC, abstractmethod

class ReporterExporter(ABC):

    @abstractmethod
    def export(self):
        pass