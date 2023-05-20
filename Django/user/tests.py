from django.test import TestCase
from .models import User
import random
import factory


class RandomUser(factory.django.DjangoModelFactory):
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    age = random.randint(18, 120)

    class Meta:
        model = User


class RandomYoungUser(factory.django.DjangoModelFactory):
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    age = random.randint(1, 18)

    class Meta:
        model = User


class RandomTurtle(factory.django.DjangoModelFactory):
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    age = random.randint(120, 300)

    class Meta:
        model = User


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.human_user = RandomUser.create()
        cls.young_human_user = RandomYoungUser.create()
        cls.turtle_user = RandomTurtle.create()

    def test_user(self):
        self.assertIsNotNone(self.human_user.last_name)

    def is_human(self):
        self.assertTrue(self.human_user.is_human())
        self.assertTrue(self.young_human_user.is_human())
        self.assertFalse(self.turtle_user.is_human())


class UserViewSetTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.human_user = RandomUser.create()

    def test_user_detail(self):
        resp = self.client.get(f"/user/{self.human_user.id}/")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json().get("first_name"), self.user.first_name)

    def test_user_create(self):
        user_create_data = {
            "first_name": "Maria",
            "last_name": "Rosa",
            "age": 22
        }
        resp = self.client.post("/user/", data=user_create_data)
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.json().get("first_name"), user_create_data.get("first_name"))

    def test_user_delete(self):
        resp = self.client.delete("/user/{self.human_user.id}/")
        self.assertEqual(resp.status_code, 204)




