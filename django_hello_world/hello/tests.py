"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django_hello_world.hello.models import RequestsStorage




class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

    def test_userprofile(self):
        users = User.objects.filter()
        for user in users:
            profile = user.get_profile()
            profile.date_birth
            profile.jabber
            profile.skype
            profile.bio
            profile.other_contacts

    def test_requests_storage(self):
            requests = RequestsStorage.objects.filter()
            for request in requests:
                request.time
                request.body
                request.type

class HttpTest(TestCase):
    def test_home(self):
        c = Client()
        response = c.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello!')
        self.assertContains(response, 'Sergiy')
        self.assertContains(response, 'Shchypa')
        self.assertContains(response, 'July')
        self.assertContains(response, 'some bio text')
        self.assertContains(response, 'admin@example.com')
        self.assertContains(response, 'sergres@ubuntu-jabber.de')
        self.assertContains(response, '9543171')
