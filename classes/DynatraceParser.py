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

		tasks = UpdateReportWithTasks()
		tasksList = tasks.loadTasks()
		currLike = None

		for item in callItems:

			group = {}
			groupLite = {}
			
			currLike = self.likeFinder(prevMsg)

			if prevMsg == item["errorsData"]["serverSide"]["exceptionMessage"] or currLike:
				group = prevGroup
				groupLite = prevGroupLite

			else:
				finalData["errorsNumber"] += 1
				finalDataLite["errorsNumber"] += 1

				group["№"] = finalData["errorsNumber"]
				group["incidentsNumber"] = 0
				group["exceptionMessage"] = item["errorsData"]["serverSide"]["exceptionMessage"]
				group["exceptionClass"] = item["errorsData"]["serverSide"]["exceptionClass"]

				likeForGroup = self.likeFinder(item["errorsData"]["serverSide"]["exceptionMessage"])
				if likeForGroup:
					group["like"] = likeForGroup

				group = tasks.findTaskDirectly(group, tasksList)
				groupLite = group.copy()
				group["incidents"] = []

			group["incidentsNumber"] += 1
			groupLite["incidentsNumber"] += 1

			currItem = self.currItem(item)
			group["incidents"].append(currItem)
			prevGroup = group
			prevGroupLite = groupLite

			if prevMsg != item["errorsData"]["serverSide"]["exceptionMessage"] and not currLike:
				finalData["errors"].append(group)
				finalDataLite["errors"].append(groupLite)
			
			prevMsg = item["errorsData"]["serverSide"]["exceptionMessage"]
			self.results = finalData
			self.resultsLite = finalDataLite