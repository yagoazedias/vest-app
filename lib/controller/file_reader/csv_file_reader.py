import csv

from datetime import datetime

from lib.constants.events import EVENT_DATE_FORMAT
from lib.usecase.event.event_usecase_factory import EventUsecaseFactory
from lib.domain.model.event_factory import EventFactory
from lib.controller.file_reader.file_reader_abstract import FileReader


class CSVFileReader(FileReader):
    def read(self, file_path, target_date):
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                event = EventFactory.create(*row)
                target_datetime = datetime.strptime(target_date, EVENT_DATE_FORMAT)
                usecase = EventUsecaseFactory().create_usecase(event)
                usecase.process(event, target_datetime)
