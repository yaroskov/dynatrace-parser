from config import config
from classes.data.Data import Data
from classes.dictionaries.Dictionaries import Dictionaries


class MakeBeautyReport(Data):
    def __init__(self, config):
        super(MakeBeautyReport, self).__init__(config)
        self.beauty_report = ""

    def make_beauty_report(self, report_filled):
        results = '\n<!DOCTYPE html>'
        results += '\n<html lang="en">'
        results += '\n<head>'
        results += '\n<meta charset="UTF-8">'
        results += '\n<title>Dynatrace Analyse</title>'
        results += '\n<style>'
        results += '\nbody {font-size: 14px; font-family: Arial, Helvetica, sans-serif;}'
        results += '\n</style>'
        results += '\n</head>'
        results += '\n<body>'
        results += '\n<div id="header"></div>'
        results += '\n<div id="content">'
        results += '\n'
        results += '\n<ol type="I">'
        results += '\n<li>'
        results += '\nDynatrace:'
        results += '\n<ol>'

        results += '\n<li>'
        results += '\nВыявленные отказы:'
        results += '\n<ol type="a">'

        call_items = sorted(report_filled["errors"], key=lambda item: item["service"])
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

        for service in sorted_by_services:
            results += '\n<li>'
            results += f'\n{Dictionaries.service_search(service["service"], config.services)}:'
            results += '\n<ul>'

            for i, record in enumerate(service["items"]):
                results += '\n<li style="margin: 10px 0">'

                results += '\n<span style="font-style: normal">'
                results += '\n'

                if "like" in record:
                    title = record["like"]
                else:
                    title = record["exceptionMessage"]

                results += f'\n{title}'
                results += '\n'
                results += '\n</span>'

                if "taskNumber" in record and record["taskNumber"] != "":
                    results += f'\n - <a href="https://jira.egovdev.ru/browse/{record["taskNumber"]}">'
                    results += f'\n{record["taskNumber"]}'
                    results += f'\n</a>'

                end_sym = ";"
                if i >= len(service["items"]) - 1:
                    end_sym = "."

                results += '\n<span style="font-weight: bold;">'
                results += f' – {str(record["incidentsNumber"])} шт' + end_sym
                results += '\n</span>'

                results += '\n</li>'

            results += '\n</ul>'
            results += '\n</li>'

        results += '\n</ol>'
        results += '\n</li>'

        results += '\n<li>'
        results += '\nЗаведены новые дефекты:'
        results += '\n<ol type="a">'

        results += '\n</ol>'
        results += '\n</li>'

        results += '\n</ol>'
        results += '\n</li>'
        results += '\n</ol>'
        results += '\n'
        results += '\n</div>'
        results += '\n<div id="bottom"></div>'
        results += '\n</body>'
        results += '\n</html>'
        results += '\n'

        self.write_results(data=results, path=self.set_path("beauties"), prefix="beauty_report", extension="html")
        self.beauty_report = results
        self.print_results(report_filled["errors"])
