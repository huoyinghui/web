from django.test import TestCase, Client

# Create your tests here.


class MessageTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_form(self):
        resp = self.client.get('/form/')
        self.assertEqual(resp.status_code, 200, 'status code must be 200!')
