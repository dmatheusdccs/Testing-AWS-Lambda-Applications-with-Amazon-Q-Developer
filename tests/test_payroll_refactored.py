import pytest
from src.payroll import Payroll


@pytest.mark.parametrize("hourly_rate,hours_worked,tax_rate,expected", [
    (50.0, 40.0, 0.2, 2000.0),
    (60.0, 20.0, 0.3, 1200.0),
])
def test_gross_pay_calculation(hourly_rate, hours_worked, tax_rate, expected):
    payroll = Payroll(hourly_rate=hourly_rate, hours_worked=hours_worked, tax_rate=tax_rate)
    assert payroll.gross_pay() == expected


def test_invalid_tax_rate_raises_value_error():
    with pytest.raises(ValueError):
        Payroll(hourly_rate=10.0, hours_worked=40.0, tax_rate=-0.2)
