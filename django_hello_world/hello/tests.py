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
        """
        Tests that userProfile has fields date_birth, jabber etc
        """

        users = User.objects.filter()
        for user in users:
            profile = user.get_profile()
            profile.date_birth
            profile.jabber
            profile.skype
            profile.bio
            profile.other_contacts

    def test_requests_storage(self):
            """
            Testing structure of RequestsStorage
            """
            requests = RequestsStorage.objects.filter()
            for request in requests:
                request.time
                request.body
                request.method


class HttpTest(TestCase):
    def test_home(self):
        """
        Testing that page returned by function home - contanis data about admin user(from fixtures)
        """
        c = Client()
        resp = c.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Hello!')
        self.assertContains(resp, 'Sergiy')
        self.assertContains(resp, 'Shchypa')
        self.assertContains(resp, 'July')
        self.assertContains(resp, 'some bio text')
        self.assertContains(resp, 'admin@example.com')
        self.assertContains(resp, 'sergres@ubuntu-jabber.de')
        self.assertContains(resp, '9543171')



class RequestLoggerTest(TestCase):
    def test_request_and_check_log(self):
        """
        make request to django, and test if it was logged
        """
        TEST_REQUEST = "/requestslog"
        c = Client()
        c.get(TEST_REQUEST)
        requests = RequestsStorage.objects.filter(body=TEST_REQUEST)
        for request in requests:
            self.assertEqual(request.body, TEST_REQUEST)
        #logs are not added if you are getting exception here
        self.assertIsInstance(requests[0], RequestsStorage)

    def test_request_logs_view(self):
        TEST_REQUEST = "/requestslog"
        c = Client()
        resp = c.get(TEST_REQUEST)
        self.assertEqual(resp.status_code, 200)


class ContextProcessorTest(TestCase):
        def test_my_context_processor(self):
            res_settings = my_context_processor(123)
            self.assertIsInstance(res_settings['settings'], LazySettings)
            pass


class FormTest(TestCase):
    def test_class_exisits(self):
        form = UserForm()
        form = ProfileForm()

    def test_view_edit(self):
        TEST_REQUEST = "/view_edit"
        c = Client()
        resp = c.get(TEST_REQUEST)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Sergiy')
        self.assertContains(resp, 'Shchypa')
        self.assertContains(resp, '1984')
        self.assertContains(resp, 'Skype')
        self.assertContains(resp, '954')
        # check if we gave 'profile' and 'user' into template
        self.assertTrue('profile' in resp.context)
        self.assertTrue('user' in resp.context)


class T6Test(TestCase):

    fixtures = ['initial_data.json']

    def test_inputs_for_logged_in_user(self):
        """
        Check if inputs are displayed on /view_edit screen
        of authentificated user
        """
        c = Client()
        c.login(username='admin', password='admin')
        TEST_REQUEST = "/view_edit"
        resp = c.get(TEST_REQUEST)
        self.assertContains(resp, "<input type=\"submit\"")
        self.assertContains(resp, "<input id=\"id_email\"")
        self.assertContains(resp, "<input id=\"id_skype\"")
        self.assertContains(resp, "<textarea id=\"id_other_contacts\"")

    def test_inputs_for_not_logged_in_user(self):
        """
        Check if inputs are NOT displayed on /view_edit screen
        of NOT authentificated user
        """
        c = Client()
        TEST_REQUEST = "/view_edit"
        resp = c.get(TEST_REQUEST)
        self.assertNotContains(resp, "<input type=\"submit\"")
        self.assertNotContains(resp, "<input id=\"id_email\"")
        self.assertNotContains(resp, "<input id=\"id_skype\"")
        self.assertNotContains(resp, "<textarea id=\"id_other_contacts\"")


class T8Test(TestCase):

    fixtures = ['initial_data.json']

    def test_custom_tag_for_logged_in_user(self):
        """
        Check if we are /custom_tag handler exists
        and, it should returm 200 for logged in user
        """
        c = Client()
        c.login(username='admin', password='admin')
        TEST_REQUEST = "/custom_tag"
        resp = c.get(TEST_REQUEST)
        self.assertEqual(resp.status_code, 200)

    def test_redirect_from_custom_tag_unlogged_user(self):
        """
        Check if we are /custom_tag handler exists
        and, it should returm 200 for logged in user
        """
        c = Client()
        #c.login(username='admin', password='admin')
        TEST_REQUEST = "/custom_tag"
        resp = c.get(TEST_REQUEST, Follow=True)
        self.assertEqual(resp.status_code, 302)

    def test_check_tag_results(self):
        from django_hello_world.hello.templatetags import edit_link
        users = User.objects.filter()
        user = users[0]
        edit_link = edit_link.edit_link(user)
        position = edit_link.find("a href=\"/admin/auth/user")
        if 1 != position:
            raise Exception("my tag edit_link returned error for" + user)
        pass


class T9Test(TestCase):

    fixtures = ['initial_data.json']
    command_name = 'list_models'

    def test_managepy_output(self):
        """
        run ./manage.py  and find if it outputs list_models
        """
        import os
        path = os.path.dirname(os.path.abspath(__file__)) + '/../'
        os.chdir(path)
        f = os.popen("./manage.py ")
        for i in f.readlines():
            if i.find(self.command_name) != -1:
                #print "", i
                return

        raise Exception("cannot find command \"",
            self.command_name, "\" in file ./manage.py")

    def test_run_custom_command(self):
        """
        run ./manage.py list_models and check output
        """
        import os
        path = os.path.dirname(os.path.abspath(__file__)) + '/../'
        os.chdir(path)
        #f = os.popen("./manage.py " ,self.command_name)
        f = os.popen("./manage.py list_models")
        for i in f.readlines():
                if i.find('django.contrib.auth.models.User') != -1:
                    return

        raise Exception("cannot find command \"",
            self.command_name, "\" in file ./manage.py")
