from classes.dynatrace_parser.functional.Data import Data
from classes.tools.Tools import Tools


class MakeBeautyReport(Data):
    def __init__(self):
        super(MakeBeautyReport, self).__init__()
        self.beauty_report = ""

    def make_beauty_report(self, report_filled):
        text = f"Отчет Dynatrace от {Tools.time_now('%d.%m.%Y')} г."
        text += "\n"
        text += f"\nТикеты, заведенные ДО {Tools.time_now('%d.%m.%Y')} г.:"
        text += "\n"

        incidents_num_total = 0
        tasks_num = 0
        for record in report_filled["errors"]:
            if "taskNumber" in record and record["taskNumber"] != "" and record['incidentsNumber'] > 4:
                text += f"\n\t{record['taskNumber']} {record['taskName']} [~ {str(record['incidentsNumber'])} шт.]"
                tasks_num += 1
                incidents_num_total += record["incidentsNumber"]

        text += "\n"

        self.write_results(data=text, path=self.set_path("beauties"), prefix="beauty_report", extension="txt")
        self.beauty_report = text
