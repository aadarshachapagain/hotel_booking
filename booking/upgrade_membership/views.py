from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator

from booking.customer.models import Customer
from booking.referee_and_referred.models import RefereeAndReferred
from points.membership_plan.models import Membership_plan
from booking.upgrade_membership.decorators import if_admin_decorator
from booking.points_log.models import PointsLog
import datetime
from booking.business_partners.models import BusinessPartners



class Membership:
    referedby = 0
    referedbyId = 0
    referedto = 0
    referedtoname = 'Default'
    membershipstatus = 'Default'
    membershipid = 0
    position = 0


# @method_decorator(if_admin_decorator, name='dispatch')
@if_admin_decorator
def show_membership(request):
    pending_customers = RefereeAndReferred.objects.filter(status='pending', membership__isnull=False)
    updated_pending_customers = []

    for customer in pending_customers:
        obj = Membership()
        obj.referedbyId = Customer.objects.get(user=customer.by).user.id
        obj.referedby = Customer.objects.get(user=customer.by).name
        obj.referedtoname = Customer.objects.get(user=customer.to).name
        obj.referedto = Customer.objects.get(user=customer.to).user.id
        membership = Customer.objects.get(user=customer.to).memplan.id
        obj.membershipid = membership
        obj.membershipstatus = Membership_plan.objects.get(id=membership).type
        obj.position = Membership_plan.objects.get(id=membership).position
        updated_pending_customers.append(obj)
    allMembership = Membership_plan.objects.all()

    data = {
        'pending_customers': updated_pending_customers,
        'allmembership': allMembership

    }

    return render(request, 'upgrade_membership/upgrade.html', data)


# customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='pointsfor')
#   type = models.CharField(blank=True, null=True, max_length=50)
#   points = models.IntegerField(null=True, blank=True, default=0)
#   available = models.DateTimeField(blank=True, null=True)
#   created_at = models.DateTimeField(default=datetime.now, blank=True)
#   status = models.CharField(blank=True, null=True, max_length=50)

@if_admin_decorator
def upgrade_membership(request):
    if request.method == 'POST':
        user = request.POST.get('referedto')
        referedById = request.POST.get('referedbyId')
        referedToId = request.POST.get('referedto')

        type = 'type' + user
        upgradedtype = request.POST.get(type)

        Rewardpointforthistype = Membership_plan.objects.get(id=upgradedtype).reward_point
        upgradedrp = Membership_plan.objects.get(id=upgradedtype).upgrade_reward_point
        virtualpointforthistypeold = Membership_plan.objects.get(id=upgradedtype).virtual_point_for_old
        virtualpointforthistypenew = Membership_plan.objects.get(id=upgradedtype).virtual_point
        creditpointforthistypeold = Membership_plan.objects.get(id=upgradedtype).credit_point_for_old

        # Accourding to admin assigned membership, membership plan is updated anc status is changed from
        # pending to completed
        updatemembership = Customer.objects.get(user=user)
        # change membership Plan  of the user
        updatemembership.memplan = Membership_plan.objects.get(id=upgradedtype)
        updatemembership.save()
        userinrefertable = RefereeAndReferred.objects.get(to=user)
        userinrefertable.status = 'Completed'
        userinrefertable.save()

        # Add reward point to newcustomer on the basis of membership plan subscribed to pointsLog table
        obj = PointsLog()
        obj.customer = Customer.objects.get(user=referedToId)
        # obj.type = Membership_plan.objects.get(id=upgradedtype)
        obj.type = "RewardPoints"
        date = datetime.datetime.now()
        date += datetime.timedelta(days=1)
        obj.points = Rewardpointforthistype + upgradedrp
        obj.available = date
        obj.save()

        # Add virtual point to newcustomer on the basis of membership plan subscribed to pointsLog table
        objvpold = PointsLog()
        objvpold.customer = Customer.objects.get(user=referedToId)
        # obj.type = Membership_plan.objects.get(id=upgradedtype)
        objvpold.type = "VirtualPoints"
        date = datetime.datetime.now()
        date += datetime.timedelta(days=1)
        objvpold.points = virtualpointforthistypenew
        objvpold.available = date
        objvpold.save()

        # Add virtual point to oldcustomer(referrer) on the basis of membership plan subscribed to pointsLog table
        objvpnew = PointsLog()
        objvpnew.customer = Customer.objects.get(user=referedById)
        # obj.type = Membership_plan.objects.get(id=upgradedtype)
        objvpnew.type = "VirtualPoints"
        date = datetime.datetime.now()
        date += datetime.timedelta(days=1)
        objvpnew.points = virtualpointforthistypeold
        objvpnew.available = date
        objvpnew.save()

        # Add credit point to oldcustomer(referrer) on the basis of membership plan subscribed to pointsLog table
        objcpold = PointsLog()
        objcpold.customer = Customer.objects.get(user=referedById)
        objcpold.type = "CreditPoints"
        date = datetime.datetime.now()
        date += datetime.timedelta(days=7)
        objcpold.points = creditpointforthistypeold
        objcpold.available = date
        objcpold.save()

    return redirect('dashboard')
