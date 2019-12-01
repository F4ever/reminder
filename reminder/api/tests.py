import pytz
from django.test import TestCase, Client
from faker import Faker

from core.models import User
from notification.models import Notification


class ConsumerAPITest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        fake = Faker()

        # Setup test user
        user = User.objects.create(
            email='admin@gmail.com',
            username='admin',
        )
        user.set_password('admin')
        user.save()

        notification = Notification.objects.create(
            head='Mail head',
            body='Mail body',
            place='Fake place',
            date=fake.future_datetime(end_date="+1d", tzinfo=pytz.UTC),
            creator=user,
        )
        # --------------------------
        # -----Setup other data ----
        users = []

        for _ in range(5):
            user = User(
               email=fake.free_email(),
               username=fake.name(),
            )
            users.append(user)

            # LifeHack
            user.save()

        # OMG MySQL does not support returning ids bulk_create
        # If the model’s primary key is an AutoField it does not
        # retrieve and set the primary key attribute, as save() does, unless the database backend supports it (
        # currently PostgreSQL).
        # user_objects = User.objects.bulk_create(users)

        notifications = []

        for i in range(10):
            notification = Notification(
                head='Mail head',
                body='Mail body',
                place='Fake place',
                date=fake.future_datetime(end_date='+1d', tzinfo=pytz.UTC),
                creator=users[i % 5],
            )
            notifications.append(notification)

        Notification.objects.bulk_create(notifications)

    def setUp(self):
        self.fake = Faker()
        self.django_client = Client()
        self.django_client.login(username='admin@gmail.com', password='admin')

    def test_get_user_list(self):
        response = self.django_client.get('/api/v1/users/')

        assert response.status_code == 200
        assert len(response.data['results']) == 6

    def test_get_notification_list(self):
        response = self.django_client.get('/api/v1/notifications/')

        assert response.status_code == 200
        # He must get only his own notification
        assert len(response.data['results']) == 1

    def test_create_notification(self):
        # Here have to be factory boy, but I dont have enough time to write all what I want
        response = self.django_client.get('/api/v1/users/')

        assert response.status_code == 200

        response = self.django_client.post(
            '/api/v1/notifications/',
            data={
                "head": "meeting",
                "body": "Some body here",
                "place": "Here",
                "date": self.fake.future_datetime(end_date='+1d', tzinfo=pytz.UTC),
                "participators": [user['id'] for user in response.data['results']]
            }
        )

        assert response.status_code == 201

        response = self.django_client.get('/api/v1/notifications/')

        assert response.status_code == 200
        assert len(response.data['results']) == 2

    def test_edit_notification(self):
        response = self.django_client.post(
            '/api/v1/notifications/',
            data={
                "head": "meeting",
                "body": "Some body here",
                "place": "Here",
                "date": self.fake.future_datetime(end_date='+1d', tzinfo=pytz.UTC),
                "participators": []
            }
        )

        assert response.status_code == 201

        notification_id = response.data['id']
        response = self.django_client.patch(
            f'/api/v1/notifications/{notification_id}/',
            data={
                "head": "Meeting",
                "body": "Some body",
                "place": "Here",
            },
            content_type='application/json',
        )

        assert response.status_code == 200
        assert response.data['head'] == 'Meeting'

    def test_delete_notification(self):
        response = self.django_client.post(
            '/api/v1/notifications/',
            data={
                "head": "meeting",
                "body": "Some body here",
                "place": "Here",
                "date": self.fake.future_datetime(end_date='+1d', tzinfo=pytz.UTC),
                "participators": []
            }
        )

        assert response.status_code == 201
        notification_id = response.data['id']

        response = self.django_client.delete(
            f'/api/v1/notifications/{notification_id}/'
        )

        assert response.status_code == 204

        response = self.django_client.get('/api/v1/notifications/')

        assert response.status_code == 200
        assert len(response.data['results']) == 1
