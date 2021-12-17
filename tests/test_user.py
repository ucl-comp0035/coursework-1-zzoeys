import pytest
import user

def test_for_user_full_name(normal_user):
    '''
    GIVEN
    '''
    assert normal_user.create_full_name() == 'katherine rose'

def test_for_calcalate_age(normal_user):
    assert normal_user.calculate_age() == 23

def test_for_calcalate_age_2(edge_case_date):
    assert edge_case_date.calculate_age() == 0



# test if date of birth is today, none 

# python -m pytest -v
# pytest --cov=.
# python -m pytest --cov-report term-missing --cov=user tests/