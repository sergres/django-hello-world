"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django_hello_world.hello.models import *
from django_hello_world.hello.context_processors import my_context_processor

from django.conf import LazySettings



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
                request.method

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

class RequestLoggerTest(TestCase):
    def test_request_and_check_log(self):
        TEST_REQUEST = "/requestslog"
        c = Client()
        response = c.get(TEST_REQUEST)
        requests = RequestsStorage.objects.filter(body = TEST_REQUEST)
        for request in requests:
            self.assertEqual(request.body, TEST_REQUEST)
        #logs are nod added if you are getting exception here
        self.assertIsInstance(requests[0] , RequestsStorage)
    def test_request_logs_view(self):
        TEST_REQUEST = "/requestslog"
        c = Client()
        response = c.get(TEST_REQUEST)
        requests = RequestsStorage.objects.filter(body = TEST_REQUEST)
        self.assertEqual(response.status_code, 200)


class ContextProcessorTest(TestCase):
        def test_my_context_processor(self):
            res_settings = my_context_processor(123)
            self.assertIsInstance(res_settings['settings'] , LazySettings)
            pass

class FormTest(TestCase):
    def test_class_exisits(self):
        form = UserForm()
        form = ProfileForm()

    def test_request_logs_view(self):
        TEST_REQUEST = "/view_edit"
        c = Client()
        response = c.get(TEST_REQUEST)
        requests = RequestsStorage.objects.filter(body = TEST_REQUEST)
        self.assertEqual(response.status_code, 200)
