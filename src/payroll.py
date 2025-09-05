# src/payroll.py
"""
This module provides a Payroll class to calculate the net pay for an employee.

The Payroll class takes in the hourly rate, hours worked, and tax rate, and
calculates the gross pay, tax amount, and net pay.
"""

class Payroll:
    """
    A class to handle payroll calculations.
    """

    def __init__(self, hourly_rate: float, hours_worked: float, tax_rate: float):
        self._validate_inputs(hourly_rate, hours_worked, tax_rate)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        self.tax_rate = tax_rate

    def _validate_inputs(self, hourly_rate: float, hours_worked: float, tax_rate: float) -> None:
        """
        Validate the input values for the Payroll class.
        """
        if hourly_rate <= 0:
            raise ValueError("Hourly rate must be a non-negative number.")
        if hours_worked < 0:
            raise ValueError("Hours worked must be a non-negative number.")
        if tax_rate < 0 or tax_rate >= 1:
            raise ValueError("Tax rate must be between 0 and 1.")

    def gross_pay(self) -> float:
        return self.hourly_rate * self.hours_worked

    def tax_amount(self) -> float:
        return self.gross_pay() * self.tax_rate

    def net_pay(self) -> float:
        return self.gross_pay() - self.tax_amount()
