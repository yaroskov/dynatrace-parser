from classes.dynatrace_parser.functional.Data import Data
from bs4 import BeautifulSoup
from classes.tools.Tools import Tools


class MakeTasksList(Data):
    def __init__(self):
        super(MakeTasksList, self).__init__()

    def make_tasks_list(self):
        html_doc = Tools.text_file_load_utf8(self.set_path("tasksSource") + self.set_file("tasksSource"))
        html_data = BeautifulSoup(html_doc, 'html.functional')
        t_body = html_data.tbody
        rows = t_body.find_all("tr", {"class": "issuerow"})

        tasks = []
        for row in rows:
            task = {"key": row.find("a", {"class": "issue-link"}).text}
            summary = row.find("td", {"class": "summary"}).text
            task["summary"] = " ".join(summary.split())
            task["description"] = row.find("td", {"class": "description"}).text
            tasks.append(task)

        tasks = Tools.json_view(tasks)

        self.print_results(tasks)
        Tools.write_data_to_file(data=tasks, path=self.set_path("tasks"), prefix="tasks", extension="json")
