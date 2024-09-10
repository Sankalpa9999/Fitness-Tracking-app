# urls.py
from django.urls import path
from . import views
from .views import simulate_payment, esewa_success, esewa_failure

urlpatterns = [
    path('membership-plans/', views.membership_plans, name='membership_plans'),
    path('purchase-membership/<str:plan_type>/', views.purchase_membership, name='purchase_membership'),
    path('simulate-payment/<str:plan_type>/', views.simulate_payment, name='simulate_payment'),
    path('membership-status/', views.membership_status, name='membership_status'),
    path('payment/', simulate_payment, name='simulate_payment'),
    path('success/', esewa_success, name='esewa_success'),
    path('failure/', esewa_failure, name='esewa_failure'),
    # Add other service views here
]
