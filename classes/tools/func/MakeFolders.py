import os


class MakeFolders:
    @staticmethod
    def mkdir(path):
        folders = path.split("/")
        if len(folders[-1]) < 1:
            del folders[-1]

        new_folders = []
        i = 0
        while i < len(folders):
            new_path = ""
            j = 0
            while j <= i:
                new_path += folders[j]
                new_path += "/"
                j += 1
            new_folders.append(new_path)
            if not os.path.exists(new_path):
                os.mkdir(new_path)
            i += 1
