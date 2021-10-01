from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator

from booking.business_partners.models import BusinessPartners
from booking.customer.models import Customer
from booking.referee_and_referred.models import RefereeAndReferred
from points.membership_plan.models import Membership_plan
from booking.upgrade_membership.decorators import if_admin_decorator
from booking.points_log.models import PointsLog
import datetime


class Partnership:
    referedby = 0
    referedbyId = 0
    referedto = 0
    referedtoname = 'Default'
    partnershipstatus = 'Default'
    # existing partnership type
    appliedpartnershiptype = 'Default'
    # partnership type user have applied for
    appliedpartnershipID = 'Default'
    # partnership ID user have applied for
    partnershipid = 0
    # position = 0


# @method_decorator(if_admin_decorator, name='dispatch')
@if_admin_decorator
def show_partnership(request):
    # pending_customers = RefereeAndReferred.objects.filter(status='pending', membership__isnull=False)
    pending_customers = RefereeAndReferred.objects.filter(status='pending', partnership__isnull=False)
    updated_pending_customers = []

    data = {}
    for customer in pending_customers:
        obj = Partnership()

        obj.referedbyId = Customer.objects.get(user=customer.by).user.id
        obj.referedbyname = Customer.objects.get(user=customer.by).name
        obj.referedtoname = Customer.objects.get(user=customer.to).name
        obj.referedtoId = Customer.objects.get(user=customer.to).user.id
        partnership = Customer.objects.get(user=customer.to).partnerplan.id
        obj.partnershipid = partnership

        partnershiptype = RefereeAndReferred.objects.get(to=customer.to).partnership.id
        obj.appliedpartnershiptype = BusinessPartners.objects.get(id=partnershiptype).type
        pid = Customer.objects.get(user=customer.to).partnerplan.id
        obj.partnershipstatus = BusinessPartners.objects.get(id=pid).type
        obj.appliedpartnershipID = BusinessPartners.objects.get(id=pid).id
        updated_pending_customers.append(obj)
        allpartnership = BusinessPartners.objects.all()

        data = {
            'pending_customers': updated_pending_customers,
            'allmembership': allpartnership

        }

    return render(request, 'upgrade_partnership/upgradepartner.html', data)


# customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='pointsfor')
#   type = models.CharField(blank=True, null=True, max_length=50)
#   points = models.IntegerField(null=True, blank=True, default=0)
#   available = models.DateTimeField(blank=True, null=True)
#   created_at = models.DateTimeField(default=datetime.now, blank=True)
#   status = models.CharField(blank=True, null=True, max_length=50)

@if_admin_decorator
def upgrade_partnership(request):
    if request.method == 'POST':
        user = request.POST.get('referedto')
        referedById = request.POST.get('referedbyId')
        referedToId = request.POST.get('referedto')
        appliedpartnershipID = request.POST.get('appliedpartnershipID')


        creditpointforthistypeold = BusinessPartners.objects.get(id=appliedpartnershipID).credit_point_for_old
        objcpold = PointsLog()
        objcpold.customer = Customer.objects.get(user=referedById)
        objcpold.type = "CreditPoints"
        date = datetime.datetime.now()
        date += datetime.timedelta(days=7)
        objcpold.points = creditpointforthistypeold
        objcpold.available = date
        objcpold.save()

    return redirect('dashboard')
