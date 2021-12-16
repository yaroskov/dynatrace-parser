from classes.dynatrace_parser.functional.Parser import Parser
from classes.beauty_report.MakeBeautyReport import MakeBeautyReport
from classes.tools.Tools import Tools


class Run(Parser):
    def __init__(self, config):
        super(Run, self).__init__(config)
        self.results_info = ""

    def prepare_data(self):

        call_items = []
        time_folder = Tools.time_now("%d.%m.%Y")

        i = 0
        while i < self.sources_number():
            i += 1
            json_data = Tools.json_load(str(i) + ".json", self.set_path("source_bags") + time_folder + "/")
            call_items += json_data["analysisResult"]["purePathsList"]

        call_items = sorted(call_items, key=lambda item: item["errorData"]["serverSide"]["exceptionMessage"])

        return call_items

    def run(self):
        call_items = self.prepare_data()
        self.make_final_fata(call_items)

    def run_complete_report(self):
        self.run()

        beauty = None
        if self.options["writeBeauty"]:
            beauty = MakeBeautyReport(self.config)
            beauty.make_beauty_report(self.results_lite)

        self.results_interface()
        self.results_lite = Tools.json_view(self.results_lite)
        self.print_results(self.results_lite)
        self.write_results_lite()

        if self.options["runFull"]:
            self.results = Tools.json_view(self.results)
            self.print_results(self.results)
            self.write_results_full()

        if self.options["writeBeauty"]:
            self.print_results(beauty.beauty_report)

        print(self.results_info)

    def write_results_full(self):
        self.write_results(data=self.results, path=self.set_path("reports"), prefix="report_full", extension="json")

    def write_results_lite(self):
        self.write_results(data=self.results_lite, path=self.set_path("reports"), prefix="report_lite",
                           extension="json")

    def results_interface(self):
        self.results_info = "report done with: errors: " + str(self.results_lite["errorsNumber"])
        self.results_info += "; incidents: " + str(self.results_lite["incidentsTotalNumber"])
