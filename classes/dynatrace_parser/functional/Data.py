from datetime import datetime
from classes.tools.Tools import Tools


class Data:
    def __init__(self):
        self.settings = Tools.json_load("settings.json")
        self.like_list = Tools.json_load("like_list.json")
        self.results = []
        self.results_lite = []

    def like_finder(self, prev_msg):
        curr_like = None
        for like in self.like_list["likeList"]:
            if like in prev_msg:
                curr_like = like
                break
        return curr_like

    def curr_item(self, item):
        # curr_item = {'name': item['name']}
        curr_item = {}
        int_unix_time = int(item["infoData"]['callStartTime']) / 1000
        curr_item['startTime'] = datetime.fromtimestamp(int_unix_time).strftime('%Y-%m-%d %H:%M:%S')
        curr_item["URI"] = self.set_path_relative("dynotraceURI") + item["infoData"]["callURI"] + ";gf=all"
        curr_item["errorData"] = item["errorData"]
        if "requestAttributesData" in item:
            curr_item["requestAttributesData"] = item["requestAttributesData"]["requestAttributesList"]

        return curr_item

    def sources_number(self):
        return self.settings["sources"]["sourcesNumber"]

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
            Tools.write_data_to_file(data=data, path=path, prefix=prefix, extension=extension)
