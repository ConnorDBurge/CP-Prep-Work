from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import User


class AppUserTest(TestCase):

    def test_01_create_user(self):
        new_user = User(first_name='Connor', last_name='Burge',
                        email='connor@meail.com', age=12, account_type='free')
        try:
            new_user.full_clean()
        except ValidationError as e:
            self.assertTrue(
                'Ensure this value is greater than or equal to 13.' in e.message_dict['age'])

    def test_02_account_type(self):
        new_user = User(first_name='Connor', last_name='Burge',
                        email='connor@meail.com', age=15, account_type='xxxx')
        try:
            new_user.full_clean()
        except ValidationError as e:
            self.assertTrue(
                f'Invalid account type for xxxx' in e.message_dict['account_type'])
