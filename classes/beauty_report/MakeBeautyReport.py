from classes.data.Data import Data
from classes.tools.Tools import Tools


class MakeBeautyReport(Data):
    def __init__(self, config):
        super(MakeBeautyReport, self).__init__(config)
        self.beauty_report = ""

    def make_beauty_report(self, report_filled):
        text = f"Отчет по мониторингу логов от {Tools.time_now('%d.%m.%Y')} г."
        text += "\n"
        text += f"\nПериод наблюдения: c 00:00 {Tools.now_minus_days('%d.%m.%Y')} г. по 00:00 {Tools.time_now('%d.%m.%Y')} г."
        text += "\n"
        text += f"\nТикеты, заведенные до {Tools.time_now('%d.%m.%Y')} г.:"
        text += "\n"

        incidents_num_total = 0
        tasks_num = 0
        for record in report_filled["errors"]:
            if "taskNumber" in record and record["taskNumber"] != "" and record['incidentsNumber'] > 4:
                text += f"\n\t{record['taskNumber']} {record['taskName']} [~ {str(record['incidentsNumber'])} шт.]"
                tasks_num += 1
                incidents_num_total += record["incidentsNumber"]

        text += "\n"
        text += f"\nТикеты, заведенные после {Tools.time_now('%d.%m.%Y')} г.:"
        text += "\n"

        self.write_results(data=text, path=self.set_path("beauties"), prefix="beauty_report", extension="html")
        self.beauty_report = text
