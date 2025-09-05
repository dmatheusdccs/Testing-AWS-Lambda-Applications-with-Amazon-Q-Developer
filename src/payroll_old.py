class Payroll:
    def __init__(self, hourly_rate, hours_worked, tax_rate):
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        self.tax_rate = tax_rate

    def gross_pay(self):
        return self.hourly_rate * self.hours_worked

    def net_pay(self):
        return self.gross_pay() * (1 - self.tax_rate)
