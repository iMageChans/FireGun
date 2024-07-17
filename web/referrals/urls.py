from django.urls import path
from .views import GetReferral

urlpatterns = [
    path('get-referral/', GetReferral.as_view(), name='get-referral'),
]