from abc import ABC, abstractmethod

class FileReader(ABC):
    @abstractmethod
    def read(self, file_path, target_date):
        pass
