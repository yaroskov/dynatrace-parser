from classes.beauty_report.beauty_builder.BeautyBuilder import BeautyBuilder
from templates.beauty_report import main


class MakeBeautyReport(BeautyBuilder):
    def __init__(self, config):
        super(BeautyBuilder, self).__init__(config)
        self.beauty_report = ""

    def make_beauty_report(self, report_filled):
        call_items = MakeBeautyReport.sort(report_filled)
        sorted_by_services = MakeBeautyReport.restructure(call_items)

        results = self.build_data(sorted_by_services)
        template = main.template(results)

        self.write_results(data=template, path=self.set_path("beauties"), prefix="beauty_report", extension="html")
        self.beauty_report = template
