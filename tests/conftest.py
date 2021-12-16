import pytest
import user as user
from datetime import date

@pytest.fixture(scope='module')
def test_user_1():
    test_user_1 = user.User('katherine', 'rose', 'katherine_rose@gmail.com', 'london2021!', date(1998, 9, 5))
    yield test_user_1

@pytest.fixture(scope='module')
def test_user_2():
    test_user_2 = user.User('zoelle', 'rose', 'zoelle_rose@gmail.com', 'singapore2021!', date.today())
    yield test_user_2