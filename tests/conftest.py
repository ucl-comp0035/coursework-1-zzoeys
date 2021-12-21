import pytest
import user
from datetime import date

# Adapted from code written by user MrBean Bremen on Stack Overflow at https://stackoverflow.com/questions/70416805/indirect-fixture-doesnt-exist-when-parametrising-tests-with-fixtures Accessed 20/12/2021
@pytest.fixture(scope='module')
def users(request):
    if request.param == 'normal_user':
        '''Returns a normal user of age 23'''
        normal_user = user.User(first_name = 'katherine', last_name = 'rose', email = 'katherine_rose@gmail.com', password = 'london2021!', dob = date(1998, 9, 5))
        yield normal_user
    if request.param == 'missing_details':
        '''Returns a user without a first name'''
        missing_details = user.User(first_name = None, last_name = 'rose', email = 'katherine_rose@gmail.com', password = 'london2021!', dob = date(1998, 9, 5))
        yield missing_details
    if request.param == 'edge_case_dob':
        '''Returns a user whose dob is today'''
        edge_case_dob = user.User(first_name = 'zoelle', last_name = 'rose', email = 'zoelle_rose@gmail.com', password = 'singapore2021!', dob = date.today())
        yield edge_case_dob
    if request.param == 'no_dob':
        '''Returns a user without a dob'''
        no_dob = user.User(first_name = 'gabriel', last_name = 'rose', email = 'gabriel_rose.com', password = 'london2021!')
        yield no_dob
    if request.param == 'invalid_email':
        '''Returns a user without a valid email'''
        invalid_email = user.User(first_name = 'elena', last_name = 'rose', email = 'elena_rose.com', password = 'london2021!', dob = date(1998, 9, 5))
        yield invalid_email


