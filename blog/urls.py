from django.urls import path
from blog.views import IndexView

app_name = "blog"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
