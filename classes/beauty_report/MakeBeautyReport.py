from classes.dynatrace_parser.functional.Data import Data
from classes.tools.Tools import Tools


class MakeBeautyReport(Data):
    def __init__(self):
        super(MakeBeautyReport, self).__init__()
        self.beauty_report = ""

    def make_beauty_report(self, report_filled):
        # beauty_report = self.beauty_report

        text = f"Отчет от {Tools.time_now('%d.%m.%Y')} г."
        # text += "\nСписок задач с количеством (шт.) инцидентов за сутки:"
        text += "\n"
        text += f"\nЗаведенные ДО {Tools.time_now('%d.%m.%Y')} г.:"
        text += "\n"

        incidents_num_total = 0
        tasks_num = 0
        for record in report_filled["errors"]:
            if "taskNumber" in record and record["taskNumber"] != "" and record['incidentsNumber'] > 4:
                text += f"\n\t{record['taskNumber']} {record['taskName']} [~ {str(record['incidentsNumber'])} шт.]"
                tasks_num += 1
                incidents_num_total += record["incidentsNumber"]

        text += "\n"
        # text += f"\nВсего: {str(incidents_num_total)} инцидентов в {str(tasks_num)} задачах:"
        # text += "\n"

        """for record in report_filled["errors"]:
            if "taskNumber" in record and record["taskNumber"] != "":
                line = record["taskNumber"] + " " + record["taskName"] + " ~ " + str(record["incidentsNumber"])
                beauty_report.append(line)

        beauty_report = Tools.json_view(beauty_report)"""

        self.write_results(data=text, path=self.set_path("beauties"), prefix="beauty_report", extension="txt")
        self.beauty_report = text
