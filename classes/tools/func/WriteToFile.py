from classes.tools.func.Time import Time
from classes.tools.func.MakeFolders import MakeFolders


class WriteToFile:
    @staticmethod
    def run(data, path="", prefix="", extension="json"):
        MakeFolders.mkdir(path)
        encoded_unicode = data.encode("utf8")
        a_file = open(path + prefix + "_" + Time.now() + "." + extension, "wb")
        a_file.write(encoded_unicode)
