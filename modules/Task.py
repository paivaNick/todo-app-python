from datetime import date


class Task():

    def __init__(self, name, desc="", date=date.today()):
        self.name = name
        self.date = str(date)
        self.status = False
        self.id = 0
        self.desc = desc
        self._body = {
            "name": self.name,
            "date": self.date,
            "status": self.status,
            "id": self.id,
            "desc": self.desc
        }
