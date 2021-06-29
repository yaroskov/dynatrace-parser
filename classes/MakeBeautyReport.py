from classes.Parser import Parser


class MakeBeautyReport(Parser):
	def __init__(self):
		super(MakeBeautyReport, self).__init__()
		self.beautyReport = []

	def make_beauty_report(self, report_filled):
		beautyReport = self.beautyReport
		for record in report_filled["errors"]:
			if "taskNumber" in record and record["taskNumber"] != "":
				line = record["taskNumber"] + " " + record["taskName"] + " ~ " + str(record["incidentsNumber"])
				beautyReport.append(line)

		beautyReport = Parser.json_view(beautyReport)
		self.write_results(data=beautyReport, path=self.set_path("beauties"), prefix="beauty_report", extension="json")
		self.beautyReport = beautyReport
