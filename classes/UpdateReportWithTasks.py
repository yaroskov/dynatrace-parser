from classes.Parser import Parser

class UpdateReportWithTasks(Parser):

	def __init__(self):
		super(UpdateReportWithTasks, self).__init__()

	def loadTasks(self):
		return Parser.jsonLoad(self.setFile("tasks"), self.setPath("tasks"))

	def findTaskDirectly(self, error, tasksList):
		for task in tasksList:
			checkKey = ''
			if "like" in error:
				checkKey = error["like"]
			else:
				checkKey = error["exceptionMessage"]

			if checkKey in task["description"]:
				error["taskName"] = task["summary"]
				error["taskNumber"] = task["key"]
				break

		return error