#import json
#import itertools
#import os
#from datetime import datetime
from classes.Parser import Parser
from bs4 import BeautifulSoup

class DailyReport(Parser):

	def __init__(self):

		self.settings = {}
		self.dataPath = ""

		self.tasks = []

	def makeTasksList(self):

		self.settingsInclude()
		htmlDoc = Parser.textFileLoad(self.dataPath + self.settings["sources"]["tasksSource"]["path"] + self.settings["sources"]["tasksSource"]["source"])
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
		
		self.tasks = tasks

		print(self.tasks)
		Parser.writeDataToFile(data=self.tasks, path=self.dataPath + self.settings["sources"]["tasks"]["path"], prefix="tasks", extension="json")
		
		pass

	def updateReportWithTasks(self):

		self.settingsInclude()
		report = Parser.jsonLoad(self.settings["sources"]["report"]["source"], self.dataPath + self.settings["sources"]["report"]["path"])
		tasks = Parser.jsonLoad(self.settings["sources"]["tasks"]["source"], self.dataPath + self.settings["sources"]["tasks"]["path"])
		print(Parser.jsonView(tasks))
		
		for error in report["errors"]:
			for task in tasks:
				checkKey = ''
				if "like" in error:
					checkKey = error["like"]
				else:
					checkKey = error["exceptionMessage"]

				if checkKey in task["description"]:
					error["taskName"] = task["summary"]
					error["taskNumber"] = task["key"]
					break

		report = Parser.jsonView(report)
		print(report)

		Parser.writeDataToFile(data=report, path=self.dataPath + self.settings["sources"]["reportsFilled"]["path"], prefix="report_filled", extension="json")

		pass

	def settingsInclude(self):

		settingsAll = Parser.jsonLoad("settings.json")
		self.settings = settingsAll["tasksHandler"]
		self.dataPath = settingsAll["dataPath"]

		pass