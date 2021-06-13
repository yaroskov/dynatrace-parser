from datetime import datetime
from classes.Parser import Parser

class DynatraceParser(Parser):

	def __init__(self):

		self.results = []
		self.resultsLite = []

		self.settings = {}
		self.dataPath = ""

	def prepareData(self):

		callItems = []
		for source in self.settings["sources"]:

			jsonData = Parser.jsonLoad(source, "data/source_bags/")
			callItems += jsonData["callItems"]

		callItems = sorted(callItems, key=lambda item: item["errorsData"]["serverSide"]["exceptionMessage"])

		return callItems

	def makeFinalData(self, callItems):

		finalData = {}
		finalData["incidentsTotalNumber"] = len(callItems)
		finalData["errorsNumber"] = 0
		finalData["errors"] = []
		finalDataLite = finalData.copy()
		finalDataLite["errors"] = finalData["errors"].copy()

		prevMsg = ''
		prevGroup = {}
		prevGroupLite = {}

		for item in callItems:

			currItem = {}
			currItem['name'] = item['name']
			intUnixTime = int(item['startTime']) / 1000
			currItem['startTime'] = datetime.fromtimestamp(intUnixTime).strftime('%Y-%m-%d %H:%M:%S')
			currItem["URI"] = "https://juu410.dynatrace-managed.com/e/3051004e-37e8-4d8f-98ff-9e175c2f39eb/#servicecall;sci=SERVICE-BE720D12C8680318;callURI=" + item["callURI"] + ";gf=all"
			currItem["errorsData"] = item["errorsData"]
			currItem["requestAttributeData"] = item["requestAttributeData"]

			group = {}
			groupLite = {}
			
			isLike = False
			currLike = ""
			for like in self.settings["likeList"]:
				if like in prevMsg:
					currLike = like
					isLike = True
					break

			if prevMsg == item["errorsData"]["serverSide"]["exceptionMessage"] or isLike:
				group = prevGroup
				groupLite = prevGroupLite
				if isLike:
					group["like"] = groupLite["like"] = currLike

			else:
				finalData["errorsNumber"] += 1
				finalDataLite["errorsNumber"] += 1

				group["№"] = finalData["errorsNumber"]
				group["incidentsNumber"] = 0
				group["exceptionMessage"] = item["errorsData"]["serverSide"]["exceptionMessage"]
				group["exceptionClass"] = item["errorsData"]["serverSide"]["exceptionClass"]
				group["taskName"] = ""
				group["taskNumber"] = ""

				groupLite = group.copy()

				group["incidents"] = []

			group["incidentsNumber"] += 1
			groupLite["incidentsNumber"] += 1

			group["incidents"].append(currItem)
			prevGroup = group
			prevGroupLite = groupLite

			if prevMsg != item["errorsData"]["serverSide"]["exceptionMessage"] and not isLike:
				finalData["errors"].append(group)
				finalDataLite["errors"].append(groupLite)

			
			prevMsg = item["errorsData"]["serverSide"]["exceptionMessage"]
			self.results = finalData
			self.resultsLite = finalDataLite

		pass

	def settingsInclude(self):

		settingsAll = Parser.jsonLoad("settings.json")
		self.settings = settingsAll["reporter"]
		self.dataPath = settingsAll["dataPath"]

		pass

	def runFull(self):
		self.run()
		self.printResultsFull()
		self.writeResultsFull()

		pass

	def runLite(self):
		self.run()
		self.printResultsLite()
		self.writeResultsLite()

		pass

	def run(self):

		self.settingsInclude()

		callItems = self.prepareData()
		self.makeFinalData(callItems)

		self.results = Parser.jsonView(self.results)
		self.resultsLite = Parser.jsonView(self.resultsLite)

		pass

	def printResults(self, data):
		if self.settings["options"]["printData"]:
			print(data)

		pass

	def printResultsFull(self):
		self.printResults(self.results)

		pass

	def printResultsLite(self):
		self.printResults(self.resultsLite)

		pass

	def writeResults(self, data, path, prefix, extension):
		if self.settings["options"]["writeData"]:
			Parser.writeDataToFile(data=data, path=path, prefix=prefix, extension=extension)

		pass

	def writeResultsFull(self):
		self.writeResults(data=self.results, path="data/reports/", prefix="report_full", extension="json")

		pass

	def writeResultsLite(self):
		self.writeResults(data=self.resultsLite, path="data/reports/", prefix="report_lite", extension="json")

		pass