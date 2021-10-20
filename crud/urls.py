from django.urls import path
from . import views


urlpatterns = [
    path("guests", views.ListGuestAPIView.as_view(), name="guest_list"),
    path("guests/create/", views.CreateGuestAPIView.as_view(), name="create_guest"),
    path(
        "guests/update/<int:pk>/",
        views.UpdateGuestAPIView.as_view(),
        name="update_guest",
    ),
    path(
        "guests/delete/<int:pk>/",
        views.DeleteGuestAPIView.as_view(),
        name="delete_guest",
    ),
    path("scrapper/", views.WeatherScrapperView.as_view(), name="scrape_weather"),
]
