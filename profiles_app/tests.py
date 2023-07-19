'''#from django.test import TestCase
#from django.urls import reverse
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile


class FirstTestCase(TestCase):

    def test_get_all_profiles(self):

        url = reverse("get-all-the-profiles", args=[self.profile.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
'''


'''  def test_get_all_profiles(self):
        # response = self.client.get('http://localhost:8000/profiles/', content_type='application/json', accept='application/json')
        url=reverse("get-all-the-profiles",args=self.Profile.pk)
        response=self.client.get(url)
        #response = self.client.get(reverse('profiles_app:get-all-the-profiles'), content_type='application/json')
        #print(response.charset)
        # self.assertTrue(len(response)>0)
        # self.assertContains(response, 'id')
        # self.assertContains(response, 'name')
        self.assertEqual(response.status_code, 200)   


 
    def test_get_method(self):
    url = reverse('profile_detail', args=[self.profile.pk])
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'Test')    



'''
'''

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile

class FirstTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.profile = Profile.objects.create(user=self.user, name='Test')

    def test_get_all_profiles(self):
        url = reverse("get-all-the-profiles")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


'''



from django.test import TestCase
from django.urls import reverse
from .models import Profile

class TestProfile(TestCase):
    def setUp(self):
        self.profile = Profile.objects.create(name='Test', email='test@test.com', phone_number='1234567890', pincode='123456')

    def test_get_all_profiles(self):
        url = reverse('get-all-the-profiles')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

