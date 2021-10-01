from datetime import datetime


class Time:
    @staticmethod
    def now(style="%d-%m-%Y_%H.%M.%S"):
        return datetime.now().strftime(style)
