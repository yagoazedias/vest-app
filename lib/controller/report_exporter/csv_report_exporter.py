from lib.controller.report_exporter.reporter_exporter_abstract import ReporterExporter
from lib.usecase.employee.employee_usecase_factory import EmployeeUsecaseFactory


class CSVReporterExporter(ReporterExporter):
    def export(self):
        usecase = EmployeeUsecaseFactory().create_usecase()
        employees = usecase.get_all()
        csv_data = self._convert_json_to_csv(employees)
        print(csv_data)

    @staticmethod
    def _convert_json_to_csv(data):
        result = []

        for employee_id, employee in data.items():
            name = employee["name"]
            for award_id, equity in employee["equities"].items():
                result.append(f"{employee_id},{name},{award_id},{equity['amount']}")

        return "\n".join(result)
