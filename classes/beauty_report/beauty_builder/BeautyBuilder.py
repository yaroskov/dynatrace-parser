from classes.data.Data import Data
from classes.dictionaries.Dictionaries import Dictionaries
from templates.beauty_report.blocks.lists import ol
from templates.beauty_report.blocks.lists import ul
from templates.beauty_report.blocks import span
from templates.beauty_report.blocks import a


class BeautyBuilder(Data):
    def __init__(self, config):
        super(BeautyBuilder, self).__init__(config)
        self.beauty_report = ""

    @staticmethod
    def sort(report_filled):
        return sorted(report_filled["errors"], key=lambda item: item["service"])

    @staticmethod
    def restructure(call_items):
        prev_service = None
        sorted_by_services = []
        i = 0
        new_item = {}
        for item in call_items:
            if item["service"] != prev_service:
                prev_service = item["service"]
                new_item = {"service": item["service"], "items": [item]}
                sorted_by_services.append(new_item)
                i += 1
            else:
                new_item["items"].append(item)

        return sorted_by_services

    @staticmethod
    def incidents_data(service):
        list_data = []
        for i, record in enumerate(service["items"]):
            if "like" in record:
                title = record["like"]
            else:
                title = record["exceptionMessage"]

            list_text = span.template(value=title, style="font-style: normal")
            if "taskNumber" in record and record["taskNumber"] != "":
                list_text += " " + a.template(value=record["taskNumber"],
                                              href=f'https://jira.egovdev.ru/browse/{record["taskNumber"]}')
            end_sym = ";"
            if i >= len(service["items"]) - 1:
                end_sym = "."
            list_text += span.template(value=f' – {str(record["incidentsNumber"])} шт' + end_sym,
                                       style="font-weight: bold;")
            list_data.append(list_text)

        return ul.template(lis=list_data, li_style="margin: 10px 0;")

    def build_data(self, sorted_by_services):
        list_data = []
        for service in sorted_by_services:
            list_text = Dictionaries.service_search(service["service"], self.config.services) + ":"
            list_text += self.incidents_data(service)
            list_data.append(list_text)

        return ol.template(list_data, "a")
