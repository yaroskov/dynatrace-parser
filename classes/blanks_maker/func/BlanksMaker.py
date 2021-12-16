from classes.tools.Tools import Tools
from classes.data.Data import Data


class BlanksMaker(Data):
    def __init__(self, config):
        super(BlanksMaker, self).__init__(config)

    @staticmethod
    def folder_name():
        return Tools.time_now("%d.%m.%Y")

    def mk_folder(self, date_time):
        Tools.mkdir(self.set_path("source_bags") + date_time)

    def mk_file(self, date_time, sources_number):
        i = 0
        while i < sources_number:
            i += 1
            open(f"{self.set_path('source_bags')}{date_time}/{i}.json", "wb")
