from datetime import datetime
from classes.Parser import Parser
from classes.UpdateReportWithTasks import UpdateReportWithTasks

class DynatraceParser(Parser):

	def __init__(self):
		super(DynatraceParser, self).__init__()

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
			currItem["URI"] = self.setPathRelative("dynotraceURI") + item["callURI"] + ";gf=all"
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