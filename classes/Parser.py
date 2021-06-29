import json
import os
from datetime import datetime


class Parser:
    def __init__(self):
        self.settings = Parser.json_load("settings.json")
        self.results = []
        self.results_lite = []

    def like_finder(self, prev_msg):
        curr_like = None
        for like in self.settings["likeList"]:
            if like in prev_msg:
                curr_like = like
                break
        return curr_like

    def curr_item(self, item):
        curr_item = {'name': item['name']}
        int_unix_time = int(item['startTime']) / 1000
        curr_item['startTime'] = datetime.fromtimestamp(int_unix_time).strftime('%Y-%m-%d %H:%M:%S')
        curr_item["URI"] = self.set_path_relative("dynotraceURI") + item["callURI"] + ";gf=all"
        curr_item["errorsData"] = item["errorsData"]
        curr_item["requestAttributeData"] = item["requestAttributeData"]

        return curr_item

    @staticmethod
    def json_view(results):
        results = json.dumps(results, sort_keys=False, indent=4, ensure_ascii=False)
        return results

    @staticmethod
    def json_load(source, path=""):
        with open(path + source, "r", encoding='utf-8') as txtData:
            jsonData = json.load(txtData)
        return jsonData

    @staticmethod
    def text_file_load(source):
        with open(source, "r", encoding="utf-8") as data:
            text = data.read()
        return text

    @staticmethod
    def write_data_to_file(data, path="", prefix="", extension="json"):

        if not os.path.exists(path):
            os.mkdir(path)

        encoded_unicode = data.encode("utf8")

        currDateTime = datetime.now().strftime("%d-%m-%Y_%H.%M.%S")
        a_file = open(path + prefix + "_" + currDateTime + "." + extension, "wb")
        a_file.write(encoded_unicode)

    def set_path(self, source):
        return self.settings["sources"]["dataPath"]["path"] + self.settings["sources"][source]["path"]

    def set_path_relative(self, source):
        return self.settings["sources"][source]["path"]

    def set_file(self, source):
        return self.settings["sources"][source]["source"]

    def print_results(self, data):
        if self.settings["options"]["printData"]:
            print(data)

    def write_results(self, data, path, prefix, extension):
        if self.settings["options"]["writeData"]:
            Parser.write_data_to_file(data=data, path=path, prefix=prefix, extension=extension)
