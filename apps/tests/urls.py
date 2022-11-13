from django.urls import path

# import views
from . import views

urlpatterns = [
    path('mail-test/', views.MailTest.as_view(), name='activity-type-listing'),
]
