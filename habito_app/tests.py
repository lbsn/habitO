from django.test import TestCase
from habito_app.forms import UserForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import os


def create_user():
# Create a user
    user, created = User.objects.get_or_create(username="testuser", password="test1234")
    user.set_password(user.password)
    user.save()
    return user

# Create your tests here.
class Tests(TestCase):
    
    def test_user_model(self):
        # Create a user
        user = create_user()

        # Check there is only the saved user is in the database
        all_users = User.objects.all()
        self.assertEquals(len(all_users), 1)

    def test_registration_form_is_displayed_correctly(self):
        #Access registration page
        try:
            response = self.client.get(reverse('register'))
        except:
            try:
                response = self.client.get(reverse('habito_app:register'))
            except:
                return False

        # Check if form is rendered correctly
        self.assertIn('Register'.lower(), response.content.lower())

        # Check form in response context is instance of UserForm
        self.assertTrue(isinstance(response.context['user_form'], UserForm))

        # Check form is displayed correctly
        self.assertEquals(response.context['user_form'].as_p(), user_form.as_p())

        # Check submit button
        self.assertIn('type="submit" value="submit"', response.content)

    def test_login_form_is_displayed_correctly(self):
        #Access login page
        try:
            response = self.client.get(reverse('login'))
        except:
            try:
                response = self.client.get(reverse('habito_app:login'))
            except:
                return False

        #Check form display
        #Header
        self.assertIn('Login'.lower(), response.content.lower())

        #Username label and input text
        self.assertIn('Username:', response.content)
        self.assertIn('input type="text" name="username" value="username"', response.content)

        #Password label and input text
        self.assertIn('Password:', response.content)
        self.assertIn('input type="password" name="password" value="password"', response.content)

        #Submit button
        self.assertIn('input type="submit" value="Submit"', response.content)

    def test_login_provides_error_message(self):
        # Access login page
        try:
            response = self.client.post(reverse('login'), {'username': 'wronguser', 'password': 'wrongpass'})
        except:
            try:
                response = self.client.post(reverse('habito_app:login'), {'username': 'wronguser', 'password': 'wrongpass'})
            except:
                return False

        print response.content
        try:
            self.assertIn('wronguser', response.content)
        except:
            self.assertIn('invalid login details', response.content)

    def test_login_redirects_to_index(self):
        # Create a user
        create_user()

        # Access login page via POST with user data
        try:
            response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'test1234'})
        except:
            try:
                response = self.client.post(reverse('habito_app:login'), {'username': 'testuser', 'password': 'test1234'})
            except:
                return False

        # Check it redirects to index
        self.assertRedirects(response, reverse('index'))

    def test_index_contains_hello_message(self):
        # Check if there is the message 
        response = self.client.get(reverse('index'))
        self.assertIn('Create a habit. And stick to it this time'.lower(), response.content.lower())

    
