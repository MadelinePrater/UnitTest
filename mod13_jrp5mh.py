import unittest
import datetime

def test_alpha(self):
    self.assertTrue(self.isalpha())

def test_upper(self):
    self.assertTrue(self.isupper())

def test_length(self, lower, upper):
    self.assertTrue(len(self) >= lower and len(self) <= upper)

def test_digit(self):
    self.assertTrue(self.isdigit)

def test_in_range(self, lower, upper):
    self.assertTrue(self >= lower and self <= upper)

def test_datetime_object(self):
    self.assertIsInstance(self, datetime)

def test_datetime_format(self):
    self.assertTrue(bool(datetime.strptime(self, '%Y-%m-%d')))



def test_symbol(self):
    test_alpha(self)
    test_upper(self)
    test_length(self, 1, 7)

def test_chart_type(self):
    test_digit(self)
    test_length(self, 1, 1)
    test_in_range(self, 1, 2)

def test_time_series(self):
    test_digit(self)
    test_length(self, 1, 1)
    test_in_range(self, 1, 4)

def test_start_date(self):
    test_datetime_object(self)
    test_datetime_format(self)

def test_end_date(self):
    test_datetime_object(self)
    test_datetime_format(self)