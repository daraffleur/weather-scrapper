from django.urls import path
from . import views


urlpatterns = [
    path("", views.ListGuestAPIView.as_view(), name="guest_list"),
    path("create/", views.CreateGuestAPIView.as_view(), name="create_guest"),
    path("update/<int:pk>/", views.UpdateGuestAPIView.as_view(), name="update_guest"),
    path("delete/<int:pk>/", views.DeleteGuestAPIView.as_view(), name="delete_guest"),
]
