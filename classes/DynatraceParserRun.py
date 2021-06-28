from classes.Parser import Parser
from classes.DynatraceParser import DynatraceParser
from classes.UpdateReportWithTasks import UpdateReportWithTasks
from classes.MakeBeautyReport import MakeBeautyReport

class DynatraceParserRun(DynatraceParser):

	def __init__(self):
		super(DynatraceParserRun, self).__init__()
		self.resultsInfo = ""

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

	def runCompleteReport(self):
		self.run()

		if self.settings["options"]["writeBeauty"]:
			beauty = MakeBeautyReport()
			beauty.makeBeautyReport(self.resultsLite)

		self.resultsInterface()
		self.resultsLite = Parser.jsonView(self.resultsLite)
		self.printResults(self.resultsLite)
		self.writeResultsLite()

		if self.settings["options"]["runFull"]:
			self.results = Parser.jsonView(self.results)
			self.printResults(self.results)
			self.writeResultsFull()

		if self.settings["options"]["writeBeauty"]:
			self.printResults(beauty.beautyReport)

		print(self.resultsInfo)

	def writeResultsFull(self):
		self.writeResults(data=self.results, path=self.setPath("reports"), prefix="report_full", extension="json")

	def writeResultsLite(self):
		self.writeResults(data=self.resultsLite, path=self.setPath("reports"), prefix="report_lite", extension="json")

	def resultsInterface(self):
		errorsNumber = self.resultsLite["errorsNumber"]
		incidentsTotalNumber = self.resultsLite["incidentsTotalNumber"]

		self.resultsInfo = "report done with: errors: " + str(errorsNumber) + "; incidents: " + str(incidentsTotalNumber)