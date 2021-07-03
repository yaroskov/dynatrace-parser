import json
import os
from datetime import datetime


class Tools:
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