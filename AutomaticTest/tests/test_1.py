import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 1,  1) == 2

    def test_adding_unsuccess(self):
        assert self.calc.adding(self, 1, 1) ==3

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

    def test_subtraction(self):
        assert self.calc.subtraction(self, 5, 3) == 2

    def test_multiply(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_divsion(self):
        assert self.calc.division(self, 10, 5) == 2

    def teardown(self):
        print('Выполнение метода Teardown')