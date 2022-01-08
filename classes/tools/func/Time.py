from datetime import datetime, timedelta


class Time:
    @staticmethod
    def now(style="%d-%m-%Y_%H.%M.%S"):
        return datetime.now().strftime(style)

    @staticmethod
    def now_minus_days(style="%d-%m-%Y_%H.%M.%S"):
        return (datetime.now() - timedelta(days=1)).strftime(style)
