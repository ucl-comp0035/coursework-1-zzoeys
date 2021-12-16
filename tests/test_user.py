import pytest
import user

def test_for_user_full_name(test_user_1):
    assert test_user_1.create_full_name() == 'katherine rose'

def test_for_calcalate_age(test_user_1):
    assert test_user_1.calculate_age() == 23

def test_for_calcalate_age_2(test_user_2):
    assert test_user_2.calculate_age() == 0



# test if date of birth is today, none 