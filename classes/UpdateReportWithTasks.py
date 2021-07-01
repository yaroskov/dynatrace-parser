from classes.dynatrace_parser.Data import Data


class UpdateReportWithTasks(Data):
    def __init__(self):
        super(UpdateReportWithTasks, self).__init__()

    def load_tasks(self):
        return Data.json_load(self.set_file("tasks"), self.set_path("tasks"))

    def find_task_directly(self, error, tasks_list):
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
