from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Users
import json


class TestUsers(APITestCase):

    def setUp(self) -> None:
        Users.objects.create(username="Test1", first_name="Adam", last_name="Adamowski")
        Users.objects.create(username="Test2", first_name="Bdam", last_name="Bdamowski")
        Users.objects.create(username="Test3", first_name="Cdam", last_name="Cdamowski")
        Users.objects.create(username="Test4", first_name="Ddam", last_name="Ddamowski")

    def test_get_latest(self):
        url = reverse('users-latest')
        response = self.client.get(url)
        json_response = json.loads(response.content.decode('utf-8'))
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 4
        assert json_response == [
            {'user_id': 4, 'url': 'http://testserver/users/4/', 'first_name': 'Ddam', 'last_name': 'Ddamowski',
             'username': 'Test4', 'role': None, 'city': None, 'photo_url': None, 'video': None, 'description': None,
             'genres': [], 'professions': [], 'bands': [], 'adverts': []},
            {'user_id': 3, 'url': 'http://testserver/users/3/', 'first_name': 'Cdam', 'last_name': 'Cdamowski',
             'username': 'Test3', 'role': None, 'city': None, 'photo_url': None, 'video': None, 'description': None,
             'genres': [], 'professions': [], 'bands': [], 'adverts': []},
            {'user_id': 2, 'url': 'http://testserver/users/2/', 'first_name': 'Bdam', 'last_name': 'Bdamowski',
             'username': 'Test2', 'role': None, 'city': None, 'photo_url': None, 'video': None, 'description': None,
             'genres': [], 'professions': [], 'bands': [], 'adverts': []},
            {'user_id': 1, 'url': 'http://testserver/users/1/', 'first_name': 'Adam', 'last_name': 'Adamowski',
             'username': 'Test1', 'role': None, 'city': None, 'photo_url': None, 'video': None, 'description': None,
             'genres': [], 'professions': [], 'bands': [], 'adverts': []},
        ]

    def test_user_register(self):
        Users.objects.all().delete()  # Deleting users from setUp
        url = reverse('register-list')
        resp = self.client.post(url, data={
            'username': 'test_user',
            'password': 'tester',
            'password2': 'tester',
            'email': 'email@test.pl',
            'email2': 'email@test.pl'
        })
        assert resp.status_code == status.HTTP_201_CREATED
        assert Users.objects.count() == 1  # As 4 users are created on setup
        assert Users.objects.get().username == 'test_user'
        assert Users.objects.get().is_active is False

    def test_user_register_with_not_same_password_email(self):
        url = reverse('register-list')
        resp = self.client.post(url, data={
            'username': 'test_user',
            'password': 'tester',
            'password2': 'not_same',
            'email': 'email@test.pl',
            'email2': 'not_same@test.pl'
        })
        json_response = json.loads(resp.content.decode('utf-8'))
        assert resp.status_code == status.HTTP_400_BAD_REQUEST
        assert json_response == {
            "password": [
                "Password must match"
            ],
            "email": [
                "Emails must match"
            ]
        }
