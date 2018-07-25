from django.test import TestCase
from users.models import UserProfile

# Create your tests here.


class UserTestCase(TestCase):
    def setUp(self):
        user = UserProfile()
        user.username = 'huoyinghui'
        user.nick_name = 'hyh'
        user.password = '123'
        user.is_superuser = 0
        user.first_name = 'huo'
        user.last_name = 'yinghui'
        user.email = 'hyhlinux@163.com'
        print(user)
        user.save()

    def test_filter(self):
        user = UserProfile.objects.all().filter(username='huoyinghui')
        self.assertEqual(user.count(), 1, 'only one is right')
        self.assertEqual(user[0].username, 'huoyinghui', 'only one is right')
