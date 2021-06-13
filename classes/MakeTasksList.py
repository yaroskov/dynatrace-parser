from classes.Parser import Parser
from bs4 import BeautifulSoup

class MakeTasksList(Parser):

	def __init__(self):
		super(MakeTasksList, self).__init__()

	def makeTasksList(self):

		self.settingsInclude()
		htmlDoc = Parser.textFileLoad(self.setPath("tasksSource") + self.setFile("tasksSource"))
		htmlData = BeautifulSoup(htmlDoc, 'html.parser')
		tbody = htmlData.tbody
		rows = tbody.find_all("tr", {"class": "issuerow"})

		tasks = []
		for row in rows:

			task = {}
			task["key"] = row.find("a", {"class": "issue-link"}).text
			summary = row.find("td", {"class": "summary"}).text
			task["summary"] = " ".join(summary.split())
			task["description"] = row.find("td", {"class": "description"}).text
			tasks.append(task)

		tasks = Parser.jsonView(tasks)

		self.printResults(tasks)
		Parser.writeDataToFile(data=tasks, path=self.setPath("tasks"), prefix="tasks", extension="json")
		pass