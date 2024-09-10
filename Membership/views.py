from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Membership, UserMembership
from datetime import timedelta
from.utils import generate_signature
import uuid



@login_required
def simulate_payment(request, plan_type):
    membership = Membership.objects.get(plan_type=plan_type)
    end_date = timezone.now() + timedelta(days=membership.duration_days)
    UserMembership.objects.update_or_create(
        user=request.user,
        defaults={'membership': membership, 'start_date': timezone.now(), 'end_date': end_date}
    )
    return redirect('membership_status')

@login_required
def membership_plans(request):
    memberships = Membership.objects.all()
    return render(request, 'Membership/membership_plans.html', {'memberships': memberships})

@login_required
def membership_status(request):
    user_membership = UserMembership.objects.filter(user=request.user).first()
    return render(request, 'Membership/membership_status.html', {'user_membership': user_membership})

@login_required
def purchase_membership(request, plan_type):
    membership = Membership.objects.get(plan_type=plan_type)
    user = request.user
    amount = membership.price
    transaction_uuid = uuid.uuid4().hex
    ESEWA_SECRET_KEY = '8gBm/:&EnhH.1/q'
    
    ESEWA_SUCCESS_URL = 'https://esewa.com.np'
    ESEWA_FAILURE_URL = 'https://google.com'

    # Create a UserMembership entry with Pending status
    start_date = timezone.now()
    end_date = start_date + timedelta(days=membership.duration_days)
    UserMembership.objects.update_or_create(
        user=user,
        defaults={'membership': membership, 'start_date': start_date, 'end_date': end_date}
    )

    # Data for signature generation
    data = {
        'total_amount': str(amount),
        'transaction_uuid': transaction_uuid,
        'product_code': 'EPAYTEST',
    }
    signed_field_names = "total_amount,transaction_uuid,product_code"
    signature = generate_signature(ESEWA_SECRET_KEY, data, signed_field_names)
    
    context = {
        # 'esewa_payment_url': ESEWA_PAYMENT_URL,
        'amount': amount,
        'transaction_uuid': transaction_uuid,
        'product_code': 'MEMBERSHIP',
        'success_url': ESEWA_SUCCESS_URL,
        'failure_url': ESEWA_FAILURE_URL,
        'signed_field_names': signed_field_names,
        'signature': signature,
    }
    return render(request, 'Membership/esewa_payment.html', context)



@csrf_exempt
def esewa_success(request):
    if request.method == 'POST':
        transaction_uuid = request.POST.get('oid')
        amount = request.POST.get('amt')
        refId = request.POST.get('refId')

        # Verify the transaction and update the membership status
        try:
            user_membership = UserMembership.objects.get(user=request.user)
            if user_membership and user_membership.membership.price == float(amount):
                user_membership.status = 'Paid'
                user_membership.save()
                return HttpResponse('Payment Successful')
            else:
                return HttpResponse('Invalid Transaction')
        except UserMembership.DoesNotExist:
            return HttpResponse('Invalid Transaction')

    return HttpResponse('Invalid Request')


@csrf_exempt
def esewa_failure(request):
    if request.method == 'POST':
        transaction_uuid = request.POST.get('oid')

        # Handle the failure logic
        try:
            user_membership = UserMembership.objects.get(user=request.user)
            user_membership.status = 'Failed'
            user_membership.save()
            return HttpResponse('Payment Failed')
        except UserMembership.DoesNotExist:
            return HttpResponse('Invalid Transaction')

    return HttpResponse('Invalid Request')
