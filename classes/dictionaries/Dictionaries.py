import copy


class Dictionaries:
    @staticmethod
    def dictionary_check(message, dictionary):
        results = None
        for block in dictionary:
            target_copy = copy.deepcopy(block["target"])
            target_copy = target_copy.split("[[target]]")
            for string in target_copy:
                if string not in message:
                    target_copy = False
                    break
            if target_copy is not False:
                results = copy.deepcopy(block["pseudo"])
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
