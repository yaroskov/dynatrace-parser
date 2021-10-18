from classes.blanks_maker.func.BlanksMaker import BlanksMaker
from classes.dynatrace_parser.functional.Data import Data


class BlanksMakerRun(Data):
    def run(self):
        date_time = BlanksMaker.folder_name()
        BlanksMaker.mk_folder(date_time)
        BlanksMaker.mk_file(date_time, self.sources_number())
