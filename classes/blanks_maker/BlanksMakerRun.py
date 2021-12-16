from classes.blanks_maker.func.BlanksMaker import BlanksMaker
# from classes.dynatrace_parser.functional.Data import Data
# from classes.data.Data import Data


class BlanksMakerRun(BlanksMaker):
    def __init__(self, config):
        super(BlanksMakerRun, self).__init__(config)

    def run(self):
        blanks_maker = BlanksMaker(self.config)
        date_time = BlanksMaker.folder_name()
        blanks_maker.mk_folder(date_time)
        blanks_maker.mk_file(date_time, self.sources_number())
