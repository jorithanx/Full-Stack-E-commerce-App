from django.test import SimpleTestCase, TestCase
from ..forms import UserLoginForm, UserRegistrationForm

class TestForms(SimpleTestCase):
   
   def test_user_login_form_valid_data(self):
      form = UserLoginForm(data={
         "username": "username1",
         "password": "psw123"
      })

      self.assertTrue(form.is_valid())

   def test_user_login_form_no_data(self):
      form = UserLoginForm(data={})

      self.assertFalse(form.is_valid())
      self.assertEquals(len(form.errors), 2)


class TestRegistrationForms(TestCase):
   def test_user_registration_form_valid_data(self):
      form = UserRegistrationForm(data={
         "username": "username1",
         "first_name": "Tomas",
         "last_name": "Samot",
         "email": "tomas@example.com",
         "password1": "pswPSWpsw123",
         "password2": "pswPSWpsw123",
      })

      self.assertTrue(form.is_valid())

   def test_user_registration_form_no_data(self):
      form = UserRegistrationForm(data={})

      self.assertFalse(form.is_valid())
      self.assertEquals(len(form.errors), 3)
# hobby-session-81
