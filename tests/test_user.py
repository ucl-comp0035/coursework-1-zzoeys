from contextlib import contextmanager
import pytest

@contextmanager
def does_not_raise():
    yield

# Parametrized test for giving the user's full name
@pytest.mark.parametrize('users, expected, expectation', [('normal_user', 'katherine rose', does_not_raise()),
                        ('missing_details', None, pytest.raises(TypeError))],
                        indirect=['users'])
def test_parametrize_full_name(users, expected, expectation):
    '''
    GIVEN a normal user (created as a fixture)
    WHEN creating the user's full name
    THEN the user's first and last name should be shown

    GIVEN a user with a missing first name (created as a fixture)
    WHEN creating the user's full name
    THEN a TypeError is given
    '''
    with expectation:
        assert users.create_full_name() == expected

# Parametrized test for giving the user's age
@pytest.mark.parametrize('users, expected', [('normal_user', 23),
                                            ('edge_case_dob', 0),
                                            ('no_dob', 'Age not calculated, date of birth unknown')],
                         indirect=['users'])
def test_parametrize_calcalate_age(users, expected):
    '''
    GIVEN a normal user (created as a fixture)
    WHEN calculating the user's age
    THEN the user's first and last name should be shown

    GIVEN a user with a birth date of totday (created as a fixture)
    WHEN calculating the user's age
    THEN the age should correctly be shown as 0

    GIVEN a user who didn't input a birthday (created as a fixture)
    WHEN calculating the user's age
    THEN a message should be printed saying 'Age not calculated, date of birth unknown'
    '''
    assert users.calculate_age() == expected

# Parametrized test for checking if a user's email is valid
@pytest.mark.parametrize('users, expected', [('normal_user', True), ('invalid_email', False)],
                         indirect=['users'])
def test_parametrize_check_email(users, expected):
    '''
    GIVEN a normal user (created as a fixture)
    WHEN checking if their email is valid
    THEN the function should return True

    GIVEN a user who has input a email not in the correct format (created as a fixture)
    WHEN checking if their email is valid
    THEN the function should return False
    '''
    assert users.valid_email() == expected

