
from django.urls import path
from .views import HomepageView

urlpatterns = [
    path('home/', HomepageView.as_view(), name='home-page'),
]