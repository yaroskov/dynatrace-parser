from classes.Parser import Parser


class UpdateReportWithTasks(Parser):
    def __init__(self):
        super(UpdateReportWithTasks, self).__init__()

    def load_tasks(self):
        return Parser.json_load(self.set_file("tasks"), self.set_path("tasks"))

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
