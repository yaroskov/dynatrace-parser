from classes.dynatrace_parser.Data import Data
from classes.tools.Tools import Tools


class UpdateReportWithTasks(Data):
    def __init__(self):
        super(UpdateReportWithTasks, self).__init__()

    def load_tasks(self):
        return Tools.json_load(self.set_file("tasks"), self.set_path("tasks"))

    @staticmethod
    def find_task_directly(error, tasks_list):
        for task in tasks_list:
            if "like" in error:
                checkKey = error["like"]
            else:
                checkKey = error["exceptionMessage"]

            if checkKey in task["description"]:
                error["taskName"] = task["summary"]
                error["taskNumber"] = task["key"]
                break

        return error
