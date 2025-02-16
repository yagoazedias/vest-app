from lib.controller.file_reader.csv_file_reader import CSVFileReader

class FileReaderFactory:
    @staticmethod
    def create_interface(file_path):
        if file_path.endswith('.csv'):
            return CSVFileReader()
        else:
            raise ValueError("Unsupported file type")