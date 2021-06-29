from classes.Parser import Parser
from classes.UpdateReportWithTasks import UpdateReportWithTasks


class DynatraceParser(Parser):

    def __init__(self):
        super(DynatraceParser, self).__init__()

    def make_final_fata(self, call_items):

        final_data = {"incidentsTotalNumber": len(call_items), "errorsNumber": 0, "errors": []}
        final_data_lite = final_data.copy()
        final_data_lite["errors"] = final_data["errors"].copy()

        prev_msg = ''
        prev_group = {}
        prev_group_lite = {}

        tasks = UpdateReportWithTasks()
        tasks_list = tasks.load_tasks()

        for item in call_items:

            group = {}

            currLike = self.like_finder(prev_msg)

            if prev_msg == item["errorsData"]["serverSide"]["exceptionMessage"] or currLike:
                group = prev_group
                group_lite = prev_group_lite

            else:
                final_data["errorsNumber"] += 1
                final_data_lite["errorsNumber"] += 1

                group["№"] = final_data["errorsNumber"]
                group["incidentsNumber"] = 0
                group["exceptionMessage"] = item["errorsData"]["serverSide"]["exceptionMessage"]
                group["exceptionClass"] = item["errorsData"]["serverSide"]["exceptionClass"]

                likeForGroup = self.like_finder(item["errorsData"]["serverSide"]["exceptionMessage"])
                if likeForGroup:
                    group["like"] = likeForGroup

                group = tasks.find_task_directly(group, tasks_list)
                group_lite = group.copy()
                group["incidents"] = []

            group["incidentsNumber"] += 1
            group_lite["incidentsNumber"] += 1

            currItem = self.curr_item(item)
            group["incidents"].append(currItem)
            prev_group = group
            prev_group_lite = group_lite

            if prev_msg != item["errorsData"]["serverSide"]["exceptionMessage"] and not currLike:
                final_data["errors"].append(group)
                final_data_lite["errors"].append(group_lite)

            prev_msg = item["errorsData"]["serverSide"]["exceptionMessage"]
            self.results = final_data
            self.results_lite = final_data_lite
