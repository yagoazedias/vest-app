import csv

from usecase.event.event_usecase_factory import EventUsecaseFactory
from domain.model.event_factory import EventFactory
from lib.controller.file_reader.file_reader_abstract import FileReader

class CSVFileReader(FileReader):
    def read(self, file_path):
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                event = EventFactory.create(*row)
                usecase = EventUsecaseFactory().create_usecase(event)
                usecase.process(event)