from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path(
        "register/",
        views.register_complaint,
        name="register_complaint"
    ),

    path(
        "complaint-success/",
        views.complaint_success,
        name="complaint_success"
    ),

    path(
        "track/",
        views.track_complaint,
        name="track_complaint"
    ),
]
 