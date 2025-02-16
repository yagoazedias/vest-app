from lib.controller.report_exporter.csv_report_exporter import CSVReporterExporter

class ReporterExporterFactory:
    @staticmethod
    def create_exporter(format: str):
        if format == 'csv':
            return CSVReporterExporter()
        else:
            raise ValueError("Unsupported format type")