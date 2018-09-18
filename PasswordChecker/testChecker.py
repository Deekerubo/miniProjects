import unittest
from unittest.mock import patch
import check_password


class ValidPassword(unittest.TestCase):
    def test_valid_password(self):
        user_input = ['Kanini24!','shakes123','nyambumo']
        output = 'Kanini24!'
        with patch('builtins.input', side_effect=user_input):
            res = check_password.PasswordValidity()
        self.assertEqual(res, output)

if __name__ == "__main__":
    unittest.main()