from classes.Parser import Parser
from classes.DynatraceParser import DynatraceParser
from classes.UpdateReportWithTasks import UpdateReportWithTasks
from classes.MakeBeautyReport import MakeBeautyReport

class DynatraceParserRun(DynatraceParser):

	def __init__(self):
		super(DynatraceParserRun, self).__init__()

	def prepareData(self):

		callItems = []
		for source in self.setFile("source_bags"):

			jsonData = Parser.jsonLoad(source, self.setPath("source_bags"))
			callItems += jsonData["callItems"]

		callItems = sorted(callItems, key=lambda item: item["errorsData"]["serverSide"]["exceptionMessage"])
		return callItems

	def run(self):
		callItems = self.prepareData()
		self.makeFinalData(callItems)
		pass

	def runFull(self):
		self.run()
		self.results = Parser.jsonView(self.results)
		self.printResults(self.results)
		self.writeResultsFull()
		pass

	def runLite(self):
		self.run()
		self.resultsLite = Parser.jsonView(self.resultsLite)
		self.printResults(self.resultsLite)
		self.writeResultsLite()
		pass

	def reportHandler(self, results, makeBeauty=True):
		tasks = UpdateReportWithTasks()
		tasks.updateReportInStream(report=results)

		results = Parser.jsonView(results)
		self.printResults(results)

		if self.settings["options"]["writeBeauty"] and makeBeauty:
			beauty = MakeBeautyReport()
			beauty.makeBeautyReport(tasks.reportFilled)
		return results

	def runCompleteReportLite(self):
		self.run()
		self.resultsLite = self.reportHandler(self.resultsLite)
		self.writeResultsLite()
		pass

	def runCompleteReportFull(self):
		self.run()
		self.results = self.reportHandler(self.results)
		self.writeResultsFull()
		pass

	def runCompleteReport(self):
		self.run()

		self.resultsLite = self.reportHandler(self.resultsLite)
		self.writeResultsLite()

		self.results = self.reportHandler(self.results, makeBeauty=False)
		self.writeResultsFull()

		print("report done")

	def writeResultsFull(self):
		self.writeResults(data=self.results, path=self.setPath("reports"), prefix="report_full", extension="json")
		pass

	def writeResultsLite(self):
		self.writeResults(data=self.resultsLite, path=self.setPath("reports"), prefix="report_lite", extension="json")
		pass