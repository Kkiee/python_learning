class Record:
    def __init__(self, date, id, money, province):
        self.date = date
        self.id = id
        self.money = money
        self.province = province

    def __str__(self):
        return f"{self.date},{self.id},{self.money},{self.province}"