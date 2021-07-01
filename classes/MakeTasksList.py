from classes.dynatrace_parser.Data import Data
from bs4 import BeautifulSoup


class MakeTasksList(Data):
    def __init__(self):
        super(MakeTasksList, self).__init__()

    def make_tasks_list(self):
        html_doc = Data.text_file_load(self.set_path("tasksSource") + self.set_file("tasksSource"))
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

        tasks = Data.json_view(tasks)

        self.print_results(tasks)
        Data.write_data_to_file(data=tasks, path=self.set_path("tasks"), prefix="tasks", extension="json")
