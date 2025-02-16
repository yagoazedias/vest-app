from lib.controller.report_exporter.reporter_exporter_abstract import ReporterExporter
from usecase.event.event_usecase_abstract import EventUsecaseFactory


class CSVReporterExporter(ReporterExporter):
    def export(self):
        usercase = EventUsecaseFactory.create_usecase()