from classes.Parser import Parser
from bs4 import BeautifulSoup


class MakeTasksList(Parser):
	def __init__(self):
		super(MakeTasksList, self).__init__()

	def make_tasks_list(self):

		html_doc = Parser.text_file_load(self.set_path("tasksSource") + self.set_file("tasksSource"))
		html_data = BeautifulSoup(html_doc, 'html.parser')
		tbody = html_data.tbody
		rows = tbody.find_all("tr", {"class": "issuerow"})

		tasks = []
		for row in rows:
			task = {"key": row.find("a", {"class": "issue-link"}).text}
			summary = row.find("td", {"class": "summary"}).text
			task["summary"] = " ".join(summary.split())
			task["description"] = row.find("td", {"class": "description"}).text
			tasks.append(task)

		tasks = Parser.json_view(tasks)

		self.print_results(tasks)
		Parser.write_data_to_file(data=tasks, path=self.set_path("tasks"), prefix="tasks", extension="json")
