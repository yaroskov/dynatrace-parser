import json
import itertools
import os
from datetime import datetime
from classes.Parser import Parser

class DynatraceParser(Parser):

	def __init__(self):

		self.results = []
		self.resultsLite = []
		self.sources = []
		self.options = []

	def prepareData(self):

		callItems = []
		for source in self.sources:

			jsonData = Parser.jsonLoad(source, "sources/")
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
			
			if (prevMsg == item["errorsData"]["serverSide"]["exceptionMessage"]):
				group = prevGroup
				groupLite = prevGroupLite
				
			else:
				finalData["errorsNumber"] += 1
				finalDataLite["errorsNumber"] += 1

				group["№"] = finalData["errorsNumber"]
				group["incidentsNumber"] = 0
				group["exceptionMessage"] = item["errorsData"]["serverSide"]["exceptionMessage"]
				group["exceptionClass"] = item["errorsData"]["serverSide"]["exceptionClass"]
				groupLite = group.copy()
				groupLite["taskName"] = ""
				groupLite["taskNumber"] = ""
				group["incidents"] = []

			group["incidentsNumber"] += 1
			groupLite["incidentsNumber"] += 1

			group["incidents"].append(currItem)
			prevGroup = group
			prevGroupLite = groupLite

			if (prevMsg != group["exceptionMessage"]):
				finalData["errors"].append(group)
				finalDataLite["errors"].append(groupLite)

			
			prevMsg = group["exceptionMessage"]
			self.results = finalData
			self.resultsLite = finalDataLite

		pass

	def settings(self):

		jsonData = Parser.jsonLoad("settings.json")

		self.sources = jsonData["sources"]
		self.options = jsonData["options"]

		pass

	def run(self):

		self.settings()

		callItems = self.prepareData()
		self.makeFinalData(callItems)

		self.results = Parser.jsonView(self.results)
		self.resultsLite = Parser.jsonView(self.resultsLite)

		if self.options["printFullData"]:
			self.printResults()

		if self.options["printLiteVersion"]:
			self.printResultsLite()

		if self.options["writeFullData"]:
			self.writeResults()

		if self.options["writeLiteVersion"]:
			self.writeResultsLite()

		pass

	def printResults(self):

		print(self.results)

		pass

	def printResultsLite(self):

		print(self.resultsLite)

		pass

	def writeResults(self):

		Parser.writeDataToFile(data=self.results, path="results/", prefix="results", extension="json")

		pass

	def writeResultsLite(self):

		Parser.writeDataToFile(data=self.resultsLite, path="results/", prefix="results_lite", extension="json")

		pass