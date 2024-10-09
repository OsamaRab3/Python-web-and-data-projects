
import unittest
from modules.AccountManagement import *

class TestAccountManagement(unittest.TestCase):

    def test_login(self):
        self.assertEqual(login(), "Login successful")

    def test_sign_up(self):
        self.assertEqual(sign_up(), "Sign up successful")

    def test_profile_management(self):
        self.assertEqual(profile_management(), "Profile management accessed")

    def test_delete_account(self):
        self.assertEqual(delete_account(), "Account deleted")

    def test_update_profile(self):
        self.assertEqual(update_profile(), "Profile updated")

if __name__ == '__main__':
    unittest.main()
