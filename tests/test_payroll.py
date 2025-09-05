import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from payroll import Payroll
import pytest

def test_gross_pay():
    p = Payroll(hourly_rate=20, hours_worked=10, tax_rate=0.1)
    assert p.gross_pay() == 200

def test_net_pay():
    p = Payroll(hourly_rate=20, hours_worked=10, tax_rate=0.1)
    assert p.net_pay() == 180
