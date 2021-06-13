from classes.Parser import Parser
from classes.DynatraceParser import DynatraceParser
from classes.UpdateReportWithTasks import UpdateReportWithTasks

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
		self.printResultsFull()
		self.writeResultsFull()
		pass

	def runLite(self):
		self.run()
		self.resultsLite = Parser.jsonView(self.resultsLite)
		self.printResultsLite()
		self.writeResultsLite()
		pass

	def runCompleteReportLite(self):
		self.run()
		tasks = UpdateReportWithTasks()
		tasks.updateReportInStream(report=self.resultsLite)
		self.resultsLite = Parser.jsonView(self.resultsLite)
		self.printResults(self.resultsLite)
		self.writeResultsLite()
		pass

	def runCompleteReportFull(self):
		self.run()
		tasks = UpdateReportWithTasks()
		tasks.updateReportInStream(report=self.results)
		self.results = Parser.jsonView(self.results)
		self.printResults(self.results)
		self.writeResultsFull()
		pass

	def printResultsFull(self):
		self.printResults(self.results)
		pass

	def printResultsLite(self):
		self.printResults(self.resultsLite)
		pass

	def writeResultsFull(self):
		self.writeResults(data=self.results, path=self.setPath("reports"), prefix="report_full", extension="json")
		pass

	def writeResultsLite(self):
		self.writeResults(data=self.resultsLite, path=self.setPath("reports"), prefix="report_lite", extension="json")
		pass