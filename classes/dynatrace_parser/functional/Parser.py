# from classes.dynatrace_parser.functional.Data import Data
from classes.tasks_list.UpdateReportWithTasks import UpdateReportWithTasks
from classes.data.Data import Data


class Parser(Data):
    def __init__(self, config):
        super(Parser, self).__init__(config)

    def make_final_fata(self, call_items):

        final_data = {"incidentsTotalNumber": len(call_items), "errorsNumber": 0, "errors": []}
        final_data_lite = final_data.copy()
        final_data_lite["errors"] = final_data["errors"].copy()

        prev_msg = ''
        prev_group = {}
        prev_group_lite = {}

        tasks = UpdateReportWithTasks(self.config)
        tasks_list = tasks.load_tasks()

        for item in call_items:

            group = {}

            curr_like = self.like_finder(prev_msg)

            if prev_msg == item["errorData"]["serverSide"]["exceptionMessage"] or curr_like:
                group = prev_group
                group_lite = prev_group_lite

            else:
                final_data["errorsNumber"] += 1
                final_data_lite["errorsNumber"] += 1

                group["№"] = final_data["errorsNumber"]
                group["incidentsNumber"] = 0
                group["exceptionMessage"] = item["errorData"]["serverSide"]["exceptionMessage"]
                group["exceptionClass"] = item["errorData"]["serverSide"]["exceptionClass"]

                like_for_group = self.like_finder(item["errorData"]["serverSide"]["exceptionMessage"])
                if like_for_group:
                    group["like"] = like_for_group

                group = tasks.find_task_directly(group, tasks_list)
                group_lite = group.copy()
                group["incidents"] = []

            group["incidentsNumber"] += 1
            group_lite["incidentsNumber"] += 1

            curr_item = self.curr_item(item)
            group["incidents"].append(curr_item)
            prev_group = group
            prev_group_lite = group_lite

            if prev_msg != item["errorData"]["serverSide"]["exceptionMessage"] and not curr_like:
                final_data["errors"].append(group)
                final_data_lite["errors"].append(group_lite)

            prev_msg = item["errorData"]["serverSide"]["exceptionMessage"]
            self.results = final_data
            self.results_lite = final_data_lite