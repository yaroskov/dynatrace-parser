import copy


class Dictionaries:
    @staticmethod
    def dictionary_check(message, dictionary, tasks_list):
        results = {"pseudo": str(message), "task": None}

        for block in dictionary:
            target_copy = copy.deepcopy(block["target"])
            target_copy = target_copy.split("[[target]]")

            for string in target_copy:
                if string not in message:
                    target_copy = False
                    break

            if target_copy is not False:
                results = copy.deepcopy(block)

                if "task" not in results or results["task"] is None:
                    results["task"] = Dictionaries.task_search(target_copy, tasks_list)

                break

        if results["task"] is None:
            results["task"] = Dictionaries.task_search([message], tasks_list)

        return results

    @staticmethod
    def task_search(target_copy, tasks_list):
        results = None
        for task in tasks_list:
            results = task

            for word in target_copy:
                if word not in task["description"]:
                    results = None
                    break

            if results is not None:
                break

        return results

    @staticmethod
    def service_search(msg, dictionary):
        target = ""
        if msg == "":
            target = "Без информации о сервисе"
        else:
            for service in dictionary:
                if service["short"] in msg:
                    target = f"{service['msg']} ({service['short'][-3:]})"
                    break
                else:
                    target = f"Сервис: {msg}"

        return target
