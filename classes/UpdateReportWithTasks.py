from classes.Parser import Parser

class UpdateReportWithTasks(Parser):

	def __init__(self):
		super(UpdateReportWithTasks, self).__init__()

	def updateReportFromFile(self):
		report = Parser.jsonLoad(self.setFile("reports"), self.setPath("reports"))
		self.updateReport(report)
		self.reportFilled = Parser.jsonView(report)
		self.printResults(self.reportFilled)
		Parser.writeDataToFile(data=self.reportFilled, path=self.setPath("reportsFilled"), prefix="report_filled", extension="json")
		pass

	def updateReportInStream(self, report):
		self.updateReport(report=report)
		pass

	def updateReport(self, report=None):
		tasks = Parser.jsonLoad(self.setFile("tasks"), self.setPath("tasks"))
		
		for error in report["errors"]:
			for task in tasks:
				checkKey = ''
				if "like" in error:
					checkKey = error["like"]
				else:
					checkKey = error["exceptionMessage"]

				if checkKey in task["description"]:
					error["taskName"] = task["summary"]
					error["taskNumber"] = task["key"]
					break

		self.reportFilled = report
		pass