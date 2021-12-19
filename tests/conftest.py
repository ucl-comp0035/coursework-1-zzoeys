import pytest
import user
from datetime import date

@pytest.fixture(scope='module')
def normal_user():
    '''Returns a normal user of age 23'''
    normal_user = user.User(first_name = 'katherine', last_name = 'rose', email = 'katherine_rose@gmail.com', password = 'london2021!', dob = date(1998, 9, 5))
    yield normal_user

@pytest.fixture(scope='module')
def missing_details():
    '''Returns a user without a last name and dob'''
    missing_details = user.User(first_name = ' ', last_name = 'rose', email = 'katherine_rose@gmail.com', password = 'london2021!', dob = date(1998, 9, 5))
    yield missing_details

@pytest.fixture(scope='module')
def invalid_email():
    '''Returns a user without a valid email'''
    invalid_email = user.User(first_name = ' elena', last_name = 'rose', email = 'elena_rose.com', password = 'london2021!', dob = date(1998, 9, 5))
    yield invalid_email

@pytest.fixture(scope='module')
def edge_case_date():
    '''Returns a user whose dob is today'''
    edge_case_date = user.User(first_name = 'zoelle', last_name = 'rose', email = 'zoelle_rose@gmail.com', password = 'singapore2021!', dob = date.today())
    yield edge_case_date

