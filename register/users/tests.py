from django.test import TestCase,Client
from students.models import Student,Quota
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your tests here.
class UsersTestCase(TestCase):

    def setup(self):
        User.objects.create_user('gerrard', 'cn331admin')
        Student.objects.create(first="stever",last="gerrard",username='gerrard')


    def test_login(self):
        c = Client()
        response = c.post('/login', {'username': 'gerrard', 'password': 'cn331admin'})
        self.assertEqual(response.status_code,200)
    def test_(self):
        c = Client()
        response = c.get('/logout')
        self.assertEqual(response.status_code,200)