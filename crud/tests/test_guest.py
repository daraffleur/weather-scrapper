from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase

# from rest_framework.test import APITestCase, APIRequestFactory
# from crud.serializers import GuestSerializer


class AccountTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path("guests", include("crud.urls")),
    ]

    def test_create_guest(self):
        """
        Ensure we can create a new guest object.
        """
        url = reverse("/guests/create/")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


# class CreateGuestTest(APITestCase):
#     def setUp(self):
#         self.client = APIRequestFactory()
#         self.data = {"name": "Don", "email": "don@test.com"}

#     def test_can_create_guest(self):
#         response = self.client.post("guests/create/", self.data, format="json")
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)


# class ReadUserTest(APITestCase):
#     def setUp(self):
#         self.superuser = Guest.objects.create_superuser(
#             "john", "john@snow.com", "johnpassword"
#         )
#         self.client.login(username="john", password="johnpassword")
#         self.Guest = Guest.objects.create(username="mike")

#     def test_can_read_user_list(self):
#         response = self.client.get(reverse("Guest-list"))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_can_read_user_detail(self):
#         response = self.client.get(reverse("Guest-detail", args=[self.Guest.id]))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)


# class UpdateUserTest(APITestCase):
#     def setUp(self):
#         self.superuser = Guest.objects.create_superuser(
#             "john", "john@snow.com", "johnpassword"
#         )
#         self.client.login(username="john", password="johnpassword")
#         self.Guest = Guest.objects.create(username="mike", first_name="Tyson")
#         self.data = UserSerializer(self.Guest).data
#         self.data.update({"first_name": "Changed"})

#     def test_can_update_user(self):
#         response = self.client.put(
#             reverse("Guest-detail", args=[self.Guest.id]), self.data
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)


# class DeleteUserTest(APITestCase):
#     def setUp(self):
#         self.superuser = Guest.objects.create_superuser(
#             "john", "john@snow.com", "johnpassword"
#         )
#         self.client.login(username="john", password="johnpassword")
#         self.Guest = Guest.objects.create(username="mikey")

#     def test_can_delete_user(self):
#         response = self.client.delete(reverse("Guest-detail", args=[self.Guest.id]))
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
