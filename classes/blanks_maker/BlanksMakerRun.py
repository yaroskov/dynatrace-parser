from classes.blanks_maker.func.BlanksMaker import BlanksMaker


class BlanksMakerRun:
    @staticmethod
    def run():
        date_time = BlanksMaker.folder_name()
        BlanksMaker.mk_folder(date_time)
        BlanksMaker.mk_file(date_time)
