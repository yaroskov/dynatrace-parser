# from classes.dynatrace_parser.functional.Data import Data
from classes.data.Data import Data
from classes.tools.Tools import Tools


class UpdateReportWithTasks(Data):
    def __init__(self, config):
        super(UpdateReportWithTasks, self).__init__(config)

    def load_tasks(self):
        return Tools.json_load(self.set_file("tasks"), self.set_path("tasks"))

    @staticmethod
    def find_task_directly(error, tasks_list):
        for task in tasks_list:
            if "like" in error:
                check_key = error["like"]
            else:
                check_key = error["exceptionMessage"]

            if check_key in task["description"]:
                error["taskName"] = task["summary"]
                error["taskNumber"] = task["key"]
                break

        return error
