import pytest
import user
from datetime import date

@pytest.fixture(scope='module')
def normal_user():
    '''Returns a normal user of age 23'''
    normal_user = user.User('katherine', 'rose', 'katherine_rose@gmail.com', 'london2021!', date(1998, 9, 5))
    yield normal_user

@pytest.fixture(scope='module')
def edge_case_date():
    '''Returns a user whose dob is today'''
    edge_case_date = user.User('zoelle', 'rose', 'zoelle_rose@gmail.com', 'singapore2021!', date.today())
    yield edge_case_date