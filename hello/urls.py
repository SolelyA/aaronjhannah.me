from django.urls import path
from hello import views
from hello.models import LogMessage

urlpatterns = [
    path("", views.splashPage, name="splash"),
    path("home/", views.home, name="home"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("project/", views.project, name="project"),
]

