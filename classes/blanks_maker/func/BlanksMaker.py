from classes.tools.Tools import Tools


class BlanksMaker:

    @staticmethod
    def folder_name():
        return Tools.time_now("%d.%m.%Y")

    @staticmethod
    def mk_folder(date_time):
        Tools.mkdir("data/source_bags/" + date_time)

    @staticmethod
    def mk_file(date_time):
        i = 0
        while i < 6:
            i += 1
            open(f"data/source_bags/{date_time}/{i}.json", "wb")