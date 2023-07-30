from django.urls import path
from .views import SubscriptionView, SubscriptionListView


app_name = 'subscriptionapp'
urlpatterns = [
    path('subscription/', SubscriptionView.as_view(), name='subscription'),
    path('list/', SubscriptionListView.as_view(), name='list'),
]
