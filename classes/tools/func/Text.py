import json


class Text:
    @staticmethod
    def json_view(results):
        results = json.dumps(results, sort_keys=False, indent=4, ensure_ascii=False)

        return results

    @staticmethod
    def json_load(source, path=""):
        with open(path + source, "r", encoding='utf-8') as txt_data:
            json_data = json.load(txt_data)

        return json_data

    @staticmethod
    def text_file_load(source):
        with open(source, "r", encoding="windows-1251") as data:
            text = data.read()
        data.close()

        return text

    @staticmethod
    def text_file_load_utf_8(source):
        with open(source, "r", encoding="utf_8_sig") as data:
            text = data.read()
        data.close()

        return text
