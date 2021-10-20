from rest_framework import generics

from crud.serializers import GuestSerializer
from crud.models import Guest


class ListGuestAPIView(generics.ListAPIView):
    """This endpoint list all of the available guests from the database"""

    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


class CreateGuestAPIView(generics.CreateAPIView):
    """Allows for creation of a Guest"""

    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


class UpdateGuestAPIView(generics.UpdateAPIView):
    """Allows for updating a specific Guest"""

    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


class DeleteGuestAPIView(generics.DestroyAPIView):
    """Allows for deletion of a specific Guest from the database"""

    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
