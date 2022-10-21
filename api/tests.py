import base64
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class PersonTests(APITestCase):
    def setUp(self) -> None:
        self.username = 'admin'
        self.password = 'admin123456'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.credentials = base64.b64encode(f'{self.username}:{self.password}'.encode('utf-8'))
        self.body = {
            "name": "Teste",
            "vehicles": [
                {
                    "color": "yellow",
                    "model": "hatch"
                },
                {
                    "color": "blue",
                    "model": "sedan"
                },
                {
                    "color": "gray",
                    "model": "hatch"
                }
            ]
        }

    def test_without_authorization(self):
        resp = self.client.get('/api/person/')
        self.assertEqual(resp.status_code, 401)

    def test_list_person(self):
        self.client.credentials(HTTP_AUTHORIZATION='Basic {}'.format(self.credentials.decode('utf-8')))
        resp = self.client.get('/api/person/')
        self.assertEqual(resp.status_code, 200)

    def test_list_person_with_data(self):
        self.client.credentials(HTTP_AUTHORIZATION='Basic {}'.format(self.credentials.decode('utf-8')))
        self.client.post('/api/person/', self.body, format='json')

        resp = self.client.get('/api/person/')

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.json()), 1)

    def test_create_person_without_cars(self):
        self.client.credentials(HTTP_AUTHORIZATION='Basic {}'.format(self.credentials.decode('utf-8')))
        body = {
            "name": "Teste",
        }
        expected_body = {
            "id": 1,
            "name": "Teste",
            "vehicles": [],
            "sales_opportunity": True
        }

        resp = self.client.post('/api/person/', body, format='json')
        self.assertEqual(resp.status_code, 201)
        self.assertDictEqual(resp.json(), expected_body)

    def test_create_person_with_one_model_repeated(self):
        self.client.credentials(HTTP_AUTHORIZATION='Basic {}'.format(self.credentials.decode('utf-8')))
        expected_body = {
            "id": 1,
            "name": "Teste",
            "vehicles": [
                {
                    "id": 1,
                    "color": "yellow",
                    "model": "hatch"
                },
                {
                    "id": 2,
                    "color": "blue",
                    "model": "sedan"
                }
            ],
            "sales_opportunity": False
        }

        resp = self.client.post('/api/person/', self.body, format='json')
        self.assertEqual(resp.status_code, 201)
        self.assertDictEqual(resp.json(), expected_body)

    def test_update_person_with_two_models_repeated(self):
        self.client.credentials(HTTP_AUTHORIZATION='Basic {}'.format(self.credentials.decode('utf-8')))
        body_update = {
            "name": "Teste2",
            "vehicles": [
                {
                    "color": "yellow",
                    "model": "hatch"
                },
                {
                    "color": "blue",
                    "model": "sedan"
                },
                {
                    "color": "gray",
                    "model": "convertible"
                }
            ]
        }

        expected_body = {
            "id": 1,
            "name": "Teste2",
            "vehicles": [
                {
                    "id": 1,
                    "color": "yellow",
                    "model": "hatch"
                },
                {
                    "id": 2,
                    "color": "blue",
                    "model": "sedan"
                },
                {
                    "id": 3,
                    "color": "gray",
                    "model": "convertible"
                }
            ],
            "sales_opportunity": False
        }

        inserted = self.client.post('/api/person/', self.body, format='json')

        updated = self.client.patch(f'/api/person/{inserted.json()["id"]}/', body_update, format='json')
        self.assertEqual(updated.status_code, 200)
        self.assertEqual(updated.json(), expected_body)

    def test_delete_person_with_one_model_repeated(self):
        self.client.credentials(HTTP_AUTHORIZATION='Basic {}'.format(self.credentials.decode('utf-8')))
        resp = self.client.post('/api/person/', self.body, format='json')

        resp2 = self.client.delete(f'/api/person/{resp.json()["id"]}/')
        self.assertEqual(resp2.status_code, 204)
        self.assertEqual(resp2.content, b"")
