from classes.Parser import Parser
from classes.DynatraceParser import DynatraceParser
from classes.MakeBeautyReport import MakeBeautyReport


class DynatraceParserRun(DynatraceParser):

	def __init__(self):
		super(DynatraceParserRun, self).__init__()
		self.resultsInfo = ""

	def prepare_data(self):

		callItems = []
		for source in self.set_file("source_bags"):

			jsonData = Parser.json_load(source, self.set_path("source_bags"))
			callItems += jsonData["callItems"]

		callItems = sorted(callItems, key=lambda item: item["errorsData"]["serverSide"]["exceptionMessage"])

		return callItems

	def run(self):
		callItems = self.prepare_data()
		self.make_final_fata(callItems)

	def run_complete_report(self):
		self.run()

		beauty = None
		if self.settings["options"]["writeBeauty"]:
			beauty = MakeBeautyReport()
			beauty.make_beauty_report(self.results_lite)

		self.results_interface()
		self.results_lite = Parser.json_view(self.results_lite)
		self.print_results(self.results_lite)
		self.write_results_lite()

		if self.settings["options"]["runFull"]:
			self.results = Parser.json_view(self.results)
			self.print_results(self.results)
			self.write_results_full()

		if self.settings["options"]["writeBeauty"]:
			self.print_results(beauty.beautyReport)

		print(self.resultsInfo)

	def write_results_full(self):
		self.write_results(data=self.results, path=self.set_path("reports"), prefix="report_full", extension="json")

	def write_results_lite(self):
		self.write_results(data=self.results_lite, path=self.set_path("reports"), prefix="report_lite", extension="json")

	def results_interface(self):
		self.resultsInfo = "report done with: errors: " + str(self.results_lite["errorsNumber"])
		self.resultsInfo += "; incidents: " + str(self.results_lite["incidentsTotalNumber"])
