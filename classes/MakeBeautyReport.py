from classes.Parser import Parser

class MakeBeautyReport(Parser):

	def __init__(self):
		super(MakeBeautyReport, self).__init__()
		self.beautyReport = []

	def makeBeautyReport(self, reportFilled):
		#print(reportFilled)
		beautyReport = []
		for record in reportFilled["errors"]:
			if "taskNumber" in record and record["taskNumber"] != "":
				line = record["taskNumber"] + " " + record["taskName"] + " ~ " + str(record["incidentsNumber"])
				beautyReport.append(line)

		beautyReport = Parser.jsonView(beautyReport)
		self.printResults(beautyReport)
		self.writeResults(data=beautyReport, path=self.setPath("beauties"), prefix="beauty_report", extension="json")

		self.beautyReport = beautyReport
		pass