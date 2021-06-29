from classes.Parser import Parser


class MakeBeautyReport(Parser):
    def __init__(self):
        super(MakeBeautyReport, self).__init__()
        self.beauty_report = []

    def make_beauty_report(self, report_filled):
        beauty_report = self.beauty_report
        for record in report_filled["errors"]:
            if "taskNumber" in record and record["taskNumber"] != "":
                line = record["taskNumber"] + " " + record["taskName"] + " ~ " + str(record["incidentsNumber"])
                beauty_report.append(line)

        beauty_report = Parser.json_view(beauty_report)
        self.write_results(data=beauty_report, path=self.set_path("beauties"), prefix="beauty_report", extension="json")
        self.beauty_report = beauty_report
